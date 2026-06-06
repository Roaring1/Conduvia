"""Tolerant parser for Lua *data* literals (tables, strings, numbers, bools, nil).
Handles: line/block comments, long strings [[..]] / [==[..]==], single+double
quoted strings, computed [key]=, Name=, positional values, trailing commas,
type casts (:: T) and unknown expressions (require(...), Color3.fromRGB(...)) which
are captured as raw strings. Good enough for Conduvia's data modules.
"""
import re, json, sys

class LuaParser:
    def __init__(self, s):
        self.s = s
        self.i = 0
        self.n = len(s)

    # ---- whitespace + comments ----
    def skipws(self):
        s, n = self.s, self.n
        while self.i < n:
            c = s[self.i]
            if c in ' \t\r\n':
                self.i += 1
                continue
            if c == '-' and self.i + 1 < n and s[self.i+1] == '-':
                self.i += 2
                # block comment?
                lb = self._try_long_bracket_open()
                if lb is not None:
                    self._read_long_bracket_body(lb)
                else:
                    while self.i < n and s[self.i] != '\n':
                        self.i += 1
                continue
            break

    def _try_long_bracket_open(self):
        # at s[i]=='[' possibly; returns level (# of '=') if a long bracket opener, else None
        s, n = self.s, self.n
        if self.i >= n or s[self.i] != '[':
            return None
        j = self.i + 1
        eqs = 0
        while j < n and s[j] == '=':
            eqs += 1
            j += 1
        if j < n and s[j] == '[':
            self.i = j + 1
            return eqs
        return None

    def _read_long_bracket_body(self, level):
        close = ']' + '=' * level + ']'
        idx = self.s.find(close, self.i)
        if idx == -1:
            body = self.s[self.i:]
            self.i = self.n
        else:
            body = self.s[self.i:idx]
            self.i = idx + len(close)
        # Lua: leading newline immediately after opener is stripped
        if body.startswith('\n'):
            body = body[1:]
        elif body.startswith('\r\n'):
            body = body[2:]
        return body

    # ---- value dispatch ----
    def parse_value(self):
        v = self._parse_primary()
        self._skip_type_cast()
        # string concatenation chains: a .. b .. c
        while True:
            save = self.i
            self.skipws()
            if self.s[self.i:self.i+2] == '..' and self.s[self.i:self.i+3] != '...':
                self.i += 2
                rhs = self._parse_primary()
                self._skip_type_cast()
                v = self._concat(v, rhs)
            else:
                self.i = save
                break
        return v

    @staticmethod
    def _concat(a, b):
        def sx(x):
            if isinstance(x, str): return x
            if isinstance(x, (int, float)): return str(x)
            if isinstance(x, dict) and '__id__' in x: return x['__id__']
            if isinstance(x, dict) and '__expr__' in x: return x['__expr__']
            return str(x)
        return sx(a) + sx(b)

    def _parse_primary(self):
        self.skipws()
        c = self.s[self.i]
        if c == '{':
            v = self.parse_table()
        elif c == '"' or c == "'":
            v = self.parse_quoted(c)
        elif c == '[':
            lvl = self._try_long_bracket_open()
            if lvl is not None:
                v = self._read_long_bracket_body(lvl)
            else:
                raise ValueError('unexpected [ at %d' % self.i)
        elif c == '-' or c == '+' or c.isdigit() or (c == '.' and self.i+1 < self.n and self.s[self.i+1].isdigit()):
            v = self.parse_number()
        else:
            v = self.parse_word_or_expr()
        return v

    def _skip_type_cast(self):
        # consume optional ':: Type' after a value
        save = self.i
        self.skipws()
        if self.i+1 < self.n and self.s[self.i] == ':' and self.s[self.i+1] == ':':
            self.i += 2
            self._skip_type_expr()
        else:
            self.i = save

    def _skip_type_expr(self):
        # read a type expression until a top-level delimiter
        depth = 0
        s, n = self.s, self.n
        self.skipws()
        while self.i < n:
            c = s[self.i]
            if c in '{([<':
                depth += 1; self.i += 1
            elif c in '})]>':
                if depth == 0:
                    break
                depth -= 1; self.i += 1
            elif c in ',;' and depth == 0:
                break
            elif c == '\n' and depth == 0:
                break
            else:
                self.i += 1

    def parse_quoted(self, q):
        s, n = self.s, self.n
        self.i += 1
        out = []
        while self.i < n:
            c = s[self.i]
            if c == '\\':
                nx = s[self.i+1] if self.i+1 < n else ''
                mp = {'n':'\n','t':'\t','r':'\r','"':'"',"'":"'",'\\':'\\','0':'\0','a':'\a','b':'\b','f':'\f','v':'\v'}
                out.append(mp.get(nx, nx))
                self.i += 2
                continue
            if c == q:
                self.i += 1
                break
            out.append(c)
            self.i += 1
        return ''.join(out)

    def parse_number(self):
        s, n = self.s, self.n
        start = self.i
        if s[self.i] in '+-':
            self.i += 1
        if s[self.i:self.i+2].lower() == '0x':
            self.i += 2
            while self.i < n and (s[self.i] in '0123456789abcdefABCDEF'):
                self.i += 1
        else:
            while self.i < n and (s[self.i].isdigit() or s[self.i] in '.eE+-'):
                # stop '+'/'-' unless preceded by e/E
                if s[self.i] in '+-' and s[self.i-1] not in 'eE':
                    break
                self.i += 1
        tok = s[start:self.i]
        try:
            if '.' in tok or 'e' in tok.lower() or 'x' in tok.lower():
                return float(int(tok,16)) if tok.lower().startswith('0x') else float(tok)
            return int(tok)
        except ValueError:
            return tok

    def parse_word_or_expr(self):
        s, n = self.s, self.n
        start = self.i
        m = re.match(r'[A-Za-z_][A-Za-z0-9_]*', s[self.i:])
        if not m:
            raise ValueError('cannot parse value at %d: %r' % (self.i, s[self.i:self.i+30]))
        word = m.group(0)
        end = self.i + len(word)
        # literals
        save = self.i
        self.i = end
        # peek for expression continuation: . : ( [ ..
        self.skipws()
        cont = self.i < n and (s[self.i] in '.:([' or s[self.i:self.i+2] == '..')
        if not cont:
            self.i = end
            if word == 'true': return True
            if word == 'false': return False
            if word == 'nil': return None
            return {'__id__': word}  # bare identifier ref
        # raw expression: scan balanced until top-level , ; } ] newline
        self.i = save
        depth = 0
        estart = self.i
        while self.i < n:
            c = s[self.i]
            if c in '([{':
                depth += 1; self.i += 1
            elif c in ')]}':
                if depth == 0:
                    break
                depth -= 1; self.i += 1
            elif c in ',;' and depth == 0:
                break
            elif c == '\n' and depth == 0:
                break
            elif c in '"\'':
                self.parse_quoted(c)
            else:
                self.i += 1
        return {'__expr__': s[estart:self.i].strip()}

    def parse_table(self):
        s, n = self.s, self.n
        assert s[self.i] == '{'
        self.i += 1
        arr = []
        d = {}
        is_map = False
        while True:
            self.skipws()
            if self.i >= n:
                break
            if s[self.i] == '}':
                self.i += 1
                break
            # computed key [k] =
            if s[self.i] == '[':
                lvl = self._peek_long_bracket()
                if lvl is None:
                    self.i += 1
                    key = self.parse_value()
                    self.skipws()
                    assert s[self.i] == ']', 'expected ] at %d' % self.i
                    self.i += 1
                    self.skipws()
                    assert s[self.i] == '=', 'expected = at %d' % self.i
                    self.i += 1
                    val = self.parse_value()
                    if isinstance(key, dict):
                        key = json.dumps(key)
                    d[key] = val; is_map = True
                    self._consume_sep(); continue
            # Name = value ?
            m = re.match(r'[A-Za-z_][A-Za-z0-9_]*', s[self.i:])
            if m:
                save = self.i
                name = m.group(0)
                self.i += len(name)
                self.skipws()
                if self.i < n and s[self.i] == '=' and (self.i+1 >= n or s[self.i+1] != '='):
                    self.i += 1
                    val = self.parse_value()
                    d[name] = val; is_map = True
                    self._consume_sep(); continue
                self.i = save
            # positional value
            val = self.parse_value()
            arr.append(val)
            self._consume_sep()
        if is_map:
            # attach positional entries under integer keys if both present
            for idx, v in enumerate(arr, 1):
                d.setdefault(idx, v)
            return d
        return arr

    def _peek_long_bracket(self):
        s, n = self.s, self.n
        if s[self.i] != '[':
            return None
        j = self.i + 1
        while j < n and s[j] == '=':
            j += 1
        if j < n and s[j] == '[':
            return j - self.i - 1
        return None

    def _consume_sep(self):
        self.skipws()
        if self.i < self.n and self.s[self.i] in ',;':
            self.i += 1


def parse_assignment(src, varname):
    """Find `local <varname> ... = <value>` and parse the value."""
    m = re.search(r'\blocal\s+' + re.escape(varname) + r'\b', src)
    if not m:
        raise ValueError('var %s not found' % varname)
    # find first '=' that is an assignment after the name (skip type annot which has no '=')
    i = m.end()
    while i < len(src):
        if src[i] == '=' and src[i+1] != '=' and src[i-1] not in '=<>~':
            break
        i += 1
    p = LuaParser(src)
    p.i = i + 1
    return p.parse_value()


if __name__ == '__main__':
    path = sys.argv[1]; var = sys.argv[2]
    with open(path) as f:
        src = f.read()
    val = parse_assignment(src, var)
    print(json.dumps(val, indent=2)[:4000])
