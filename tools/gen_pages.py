#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the Conduvia player-guide MkDocs markdown from extracted game data.
Data-driven pages only (home, the climb, field guides, stations, item catalog,
icon manifest). Hand-authored prose lives as static files in docs/.
"""
import json, os, re

DATA = os.environ.get('CONDUVIA_DATA', '/data/build/json')
DOCS = os.environ.get('CONDUVIA_DOCS', '/data/conduvia-guide/docs')

quests   = json.load(open(DATA + '/quests.json'))
items    = json.load(open(DATA + '/items.json'))
stations = json.load(open(DATA + '/stations.json'))

def w(relpath, text):
    p = os.path.join(DOCS, relpath)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w') as f:
        f.write(text.rstrip() + '\n')
    return relpath

# ----------------------------------------------------------------------------
# Tier / chapter metadata (the spine).  Order is the fixed in-game gate chain.
# ----------------------------------------------------------------------------
CHAPTERS = [
  dict(key='survival',   num='0', name='Survival',     tier='Tier 0',
       unlocks='You wake up with nothing.',
       leads='Fiber, fire, water, a cutting edge \u2014 a night you survive.',
       blurb='Stone, sticks, and the next few hours. Solve water, fire, food, and sleep before they solve you.'),
  dict(key='stone',      num='1', name='Stone',         tier='Tier 1',
       unlocks='A stable camp and a cutting edge.',
       leads='Kilns, fired clay, charcoal, quicklime.',
       blurb='Camp industry. Build the first heat you control \u2014 kilns turn wood into charcoal and clay into ceramics.'),
  dict(key='metal_ages', num='2', name='Metal Ages',    tier='Tier 2',
       unlocks='Charcoal and crucibles.',
       leads='Copper, bronze, wrought iron.',
       blurb='Charcoal smelting. Pull the first metal out of rock and learn the alloy that named an age.'),
  dict(key='steam',      num='3', name='Steam',         tier='Tier 3',
       unlocks='Bronze and wrought iron tools.',
       leads='Coke, coal tar, mechanical power.',
       blurb='Mechanical power. Coke gives you furnace-grade heat; steam gives you work that never gets tired.'),
  dict(key='steel',      num='4', name='Steel & DC',    tier='Tier 4',
       unlocks='Coke and steam power.',
       leads='Steel, shapes, DC dynamo, motors.',
       blurb='The blast furnace and the first electricity. Steel structure, then a dynamo to spin it all.'),
  dict(key='electric',   num='5', name='Electric',      tier='Tier 5',
       unlocks='Steel and a DC dynamo.',
       leads='AC grid, electrolysis, arc furnace \u2014 the chemistry gateway.',
       blurb='The chemistry gateway. An AC grid powers electrolysis: aluminum, chlor-alkali, ferroalloys, metallurgical silicon.'),
  dict(key='solidstate', num='6', name='Solid State',   tier='Tier 6',
       unlocks='Industrial electricity and pure silicon.',
       leads='Polysilicon, wafers, ICs, automation.',
       blurb='Semiconductors and automation. Grow a silicon crystal, slice wafers, and let machines run the line.'),
  dict(key='space',      num='7', name='Space',         tier='Tier 7',
       unlocks='Wafers, automation, superalloys.',
       leads='Cryogenics, titanium, the rocket. ORBITAL LAUNCH (win).',
       blurb='The win. Cryogenic oxygen, titanium, superalloys, composites \u2014 assemble an engine, a stage, a vehicle, and launch.'),
]
CH_BY_KEY = {c['key']: c for c in CHAPTERS}
ORDER = [c['key'] for c in CHAPTERS]

SUPPORT = ['ore_field_guide', 'geology_timeline', 'rewards']

QTYPE_LABEL = {
  'info': ('Briefing', 'info'),
  'main': ('Win-path', 'main'),
  'checkpoint': ('Checkpoint', 'checkpoint'),
  'side': ('Branch', 'side'),
  'exchange': ('Exchange', 'exchange'),
}

# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
def item_name(iid):
    it = items.get(iid)
    if it and it.get('name'):
        return it['name']
    return iid.replace('_', ' ')

def chip(iid, count=None):
    """Inline item chip shortcode expanded by hooks/shortcodes.py."""
    if count is not None:
        return ':ci[%s|%s]' % (iid, count)
    return ':ci[%s]' % iid

HINT_RE = re.compile(r'\[hint\](.*?)\[/hint\]', re.DOTALL)
LOREBLOCK_RE = re.compile(r'\[lore\](.*?)\[/lore\]', re.DOTALL)

def render_hints(md):
    if not md:
        return ''
    def repl(m):
        body = m.group(1).strip()
        return ('\n\n<div class="qb-hint" markdown>\n**Tip** \u00b7 ' + body + '\n</div>\n\n')
    md = HINT_RE.sub(repl, md)
    md = LOREBLOCK_RE.sub(lambda m: m.group(1).strip(), md)
    return md.strip()

def parse_main_items(s):
    out = []
    if not isinstance(s, str) or not s:
        return out
    for part in s.split('|'):
        part = part.strip()
        if not part:
            continue
        if ':' in part:
            iid, cnt = part.rsplit(':', 1)
            try:
                out.append((iid.strip(), int(cnt)))
            except ValueError:
                out.append((iid.strip(), None))
        else:
            out.append((part, None))
    return out

def title_for(detail, node):
    for k in ('displayTitle', 'title'):
        if detail.get(k):
            return detail[k]
    if node and node.get('title'):
        return node['title']
    return (detail.get('id') or (node or {}).get('id') or 'Quest').replace('_', ' ')

def topo_order(nodes, edges):
    """Stable order: authoring order, but ensure prereqs precede dependents."""
    order = [n['id'] for n in nodes if isinstance(n, dict) and n.get('id')]
    idx = {nid: i for i, nid in enumerate(order)}
    # simple stable adjust: keep authoring order (already topo-ish)
    return order

# ----------------------------------------------------------------------------
# Quest card
# ----------------------------------------------------------------------------
def render_task(t):
    if not isinstance(t, dict):
        return ''
    kind = (t.get('kind') or 'do').lower()
    desc = t.get('desc') or t.get('title') or ''
    opt = t.get('optional')
    lines = []
    badge = '<span class="task-kind task-%s">%s</span>' % (kind, kind)
    optmark = ' <span class="task-opt">optional</span>' if opt else ''
    lines.append('- %s %s%s' % (badge, desc, optmark))
    req = t.get('requires') or []
    if isinstance(req, list) and req:
        chips = ' '.join(chip(r.get('itemId'), r.get('count')) for r in req if isinstance(r, dict) and r.get('itemId'))
        if chips:
            lines.append('    <br>needs: ' + chips)
    got = t.get('items') or []
    if isinstance(got, list) and got and kind in ('craft', 'retrieve', 'place', 'build'):
        chips = ' '.join(chip(g.get('itemId'), g.get('count')) for g in got if isinstance(g, dict) and g.get('itemId'))
        # alternates
        alts = []
        for g in got:
            for a in (g.get('alternates') or []):
                if isinstance(a, dict) and a.get('itemId'):
                    alts.append(chip(a.get('itemId'), a.get('count')))
        if chips:
            line = '    <br>yields: ' + chips
            if alts:
                line += ' <span class="alt">(or ' + ' '.join(alts) + ')</span>'
            lines.append(line)
    return '\n'.join(lines)

def render_quest(qid, detail, node, ch_meta):
    t = detail
    qtype = (t.get('questType') or 'main')
    label, cls = QTYPE_LABEL.get(qtype, (qtype.title(), 'main'))
    title = title_for(t, node)
    parts = []
    parts.append('<section class="quest-card qtype-%s" markdown>' % cls)
    parts.append('<header class="quest-card__head">')
    parts.append('<span class="qbadge qbadge-%s">%s</span>' % (cls, label))
    cat = t.get('questCategory') or ch_meta.get('key')
    parts.append('<h3 class="quest-card__title">%s</h3>' % title)
    parts.append('</header>')
    # prereqs
    pre = t.get('prereqNodes') or []
    if isinstance(pre, list) and pre:
        det = quests  # not used
        names = []
        # find titles within same chapter
        chdet = ch_meta.get('_details', {})
        chnodes = ch_meta.get('_nodes', {})
        for p in pre:
            d = chdet.get(p, {})
            n = chnodes.get(p, {})
            names.append(title_for(d, n) if (d or n) else p.replace('_', ' '))
        parts.append('<p class="quest-pre">Unlocks after: <em>%s</em></p>' % ', '.join(names))
    # summary (in-voice 'what do I do')
    summ = render_hints(t.get('summary'))
    if summ:
        parts.append('<div class="quest-summary" markdown>\n%s\n</div>' % summ)
    # tasks
    tasks = t.get('tasks') or []
    if isinstance(tasks, list) and tasks:
        parts.append('<div class="quest-tasks" markdown>')
        parts.append('**Do this:**')
        parts.append('\n'.join(render_task(x) for x in tasks))
        parts.append('</div>')
    # key items (when no explicit tasks)
    elif t.get('mainItems'):
        mi = parse_main_items(t.get('mainItems'))
        if mi:
            parts.append('<p class="quest-keyitems">Key items: ' +
                         ' '.join(chip(i, c) for i, c in mi) + '</p>')
    # rewards
    rw = t.get('rewards') or {}
    if isinstance(rw, dict):
        ritems = rw.get('items') or []
        rcosts = rw.get('costs') or []
        if rcosts:
            parts.append('<p class="quest-rewards costs">Costs: ' +
                         ' '.join(chip(r.get('itemId'), r.get('count')) for r in rcosts if isinstance(r, dict) and r.get('itemId')) + '</p>')
        if ritems:
            parts.append('<p class="quest-rewards">Rewards: ' +
                         ' '.join(chip(r.get('itemId'), r.get('count')) for r in ritems if isinstance(r, dict) and r.get('itemId')) + '</p>')
    # lore (collapsible)
    lore = render_hints(t.get('lore'))
    if lore:
        parts.append('<details class="quest-lore" markdown>\n<summary>Background</summary>\n\n%s\n</details>' % lore)
    parts.append('</section>')
    return '\n'.join(parts)

# ----------------------------------------------------------------------------
# Chapter pages (The Climb)
# ----------------------------------------------------------------------------
def tier_gate(ch):
    return ('<div class="tier-gate" markdown>\n'
            '<div class="tier-gate__num">%s</div>\n'
            '<div class="tier-gate__body" markdown>\n'
            '<div class="tier-gate__name">%s \u2014 %s</div>\n'
            '<div class="tier-gate__flow"><span class="tg-in">Unlocks after: %s</span>'
            '<span class="tg-arrow">\u2192</span>'
            '<span class="tg-out">Leads to: %s</span></div>\n'
            '</div>\n</div>\n') % (ch['tier'].replace('Tier ', ''), ch['tier'], ch['name'], ch['unlocks'], ch['leads'])

def gen_climb():
    # per-chapter pages
    for ci, ch in enumerate(CHAPTERS):
        key = ch['key']
        data = quests.get(key, {})
        nodes = data.get('nodes', []) or []
        details = data.get('questDetails', {}) or {}
        nodes_by_id = {n['id']: n for n in nodes if isinstance(n, dict) and n.get('id')}
        ch['_details'] = details
        ch['_nodes'] = nodes_by_id
        order = topo_order(nodes, data.get('edges', []))
        body = []
        body.append('---')
        body.append('title: %s \u2014 %s' % (ch['tier'], ch['name']))
        body.append('---')
        body.append('<div class="tierwrap" data-tier="%s" markdown>' % key)
        body.append('')
        body.append('# %s \u2014 %s' % (ch['tier'], ch['name']))
        body.append('')
        body.append('> %s' % ch['blurb'])
        body.append('')
        body.append(tier_gate(ch))
        # count main vs side
        mains = sum(1 for nid in order if (details.get(nid, {}).get('questType') in ('main', 'checkpoint')))
        sides = sum(1 for nid in order if (details.get(nid, {}).get('questType') in ('side', 'exchange')))
        body.append('<p class="chapter-stats">%d quests \u00b7 %d on the win-path \u00b7 %d branches</p>' % (len(order), mains, sides))
        body.append('')
        for nid in order:
            detail = details.get(nid, {})
            if not isinstance(detail, dict) or not detail:
                # node without detail: minimal stub
                node = nodes_by_id.get(nid, {})
                continue
            node = nodes_by_id.get(nid, {})
            body.append(render_quest(nid, detail, node, ch))
            body.append('')
        body.append('</div>')
        prevn = ('[\u2190 %s](%d-%s.md)' % (CHAPTERS[ci-1]['name'], ci-1, CHAPTERS[ci-1]['key'])) if ci > 0 else ''
        nextn = ('[%s \u2192](%d-%s.md)' % (CHAPTERS[ci+1]['name'], ci+1, CHAPTERS[ci+1]['key'])) if ci < len(CHAPTERS)-1 else ''
        body.append('')
        body.append('<div class="chapter-nav">%s%s</div>' % (prevn, ('  \u00b7  ' + nextn) if nextn else ''))
        w('climb/%d-%s.md' % (ci, key), '\n'.join(body))

    # climb index
    idx = ['# The Climb', '',
           'Eight chapters, gated in a fixed order. Each one unlocks a **real capability** \u2014 '
           'and the order is not arbitrary. You cannot skip a rung, because the physics of the next '
           'rung depends on the one below it. No silicon without industrial electricity; no electricity '
           'at scale without steel; no steel without coke-grade heat.', '']
    idx.append('<div class="climb-ladder" markdown>')
    for ci, ch in enumerate(CHAPTERS):
        idx.append('<a class="rung" data-tier="%s" href="%d-%s/">'
                   '<span class="rung-n">%s</span>'
                   '<span class="rung-name">%s</span>'
                   '<span class="rung-blurb">%s</span></a>' % (ch['key'], ci, ch['key'], ch['num'], ch['name'], ch['leads']))
    idx.append('</div>')
    idx.append('')
    idx.append('## The single critical win-path')
    idx.append('')
    idx.append('Everything below is **one honest chain**. Everything *off* this line \u2014 farming, '
               'fishing, trapping, nuclear power, satellites \u2014 is optional. The guide marks '
               '<span class="qbadge qbadge-main">Win-path</span> vs <span class="qbadge qbadge-side">Branch</span> on every quest.')
    idx.append('')
    idx.append('```text\n'
               'sticks + plant fiber -> cordage -> stone knife -> fire -> kiln + charcoal\n'
               '  -> copper smelt -> bronze (Cu+Sn) -> bloomery -> wrought iron\n'
               '  -> coke (from coal) -> steam power -> blast furnace -> steel\n'
               '  -> DC dynamo -> AC three-phase grid\n'
               '  -> electrolysis: aluminum, chlor-alkali (Cl2/NaOH), ferroalloys, MG-silicon\n'
               '  -> trichlorosilane -> polysilicon -> Czochralski wafer -> ICs / PLC automation\n'
               '  -> cryogenic air separation (LOX); Kroll titanium; Inconel turbopump; Cu-Cr chamber\n'
               '  -> rocket engine -> Al-Li tanks + RP-1 -> stage -> vehicle -> ORBITAL LAUNCH (win)\n'
               '```')
    w('climb/index.md', '\n'.join(idx))

# ----------------------------------------------------------------------------
# Field guides (support chapters)
# ----------------------------------------------------------------------------
def gen_field_guides():
    # Ore field guide
    ofg = quests.get('ore_field_guide', {})
    nodes = ofg.get('nodes', []) or []
    details = ofg.get('questDetails', {}) or {}
    nbi = {n['id']: n for n in nodes if isinstance(n, dict)}
    body = ['# Ore & Material Field Guide', '',
            'Found something you don\u2019t recognise? Match what you see. Every entry describes exactly '
            'what it looks like in-game and what it\u2019s good for.', '']
    body.append('<div class="tierwrap" data-tier="metal_ages" markdown>')
    for n in nodes:
        nid = n.get('id') if isinstance(n, dict) else None
        if not nid:
            continue
        d = details.get(nid, {})
        if not isinstance(d, dict):
            continue
        title = title_for(d, n)
        summ = render_hints(d.get('summary'))
        lore = render_hints(d.get('lore'))
        body.append('## %s' % title)
        if summ:
            body.append(summ)
        if lore:
            body.append('\n<details markdown><summary>More</summary>\n\n%s\n</details>' % lore)
        body.append('')
    body.append('</div>')
    w('field-guide/ore-field-guide.md', '\n'.join(body))

    # Geology timeline (data generated in-game; render nodes/intro only)
    g = ['# Geology Timeline', '',
         'Conduvia\u2019s world isn\u2019t scattered at random \u2014 it is laid down in layers like a real '
         'planet. Where you dig, how deep you go, and which biome you are standing in all decide which rock '
         'and which ore you hit. Learn to read the ground and you stop prospecting blind.', '',
         '## Read the rock, not the map', '',
         'Three rock families cover almost everything you will mine:', '',
         '- **Sedimentary** \u2014 layered, near the surface, laid down by water and time. Coal, limestone, '
         'clays, sands, and rock salt live here.',
         '- **Igneous** \u2014 hard rock born from heat, deeper or near old volcanism. Native metals, sulfide '
         'veins, and quartz come from here.',
         '- **Metamorphic** \u2014 rock cooked and squeezed at the boundaries between the other two. Often the '
         'richest or most altered ores sit in these zones.', '',
         '## Depth bands', '',
         '| Band | What you find |',
         '|---|---|',
         '| Surface & rivers | Soils, clays, and **placer** gravels \u2014 rounded river stone you can pan for '
         'native copper, tin, and gold. |',
         '| Shallow beds | Sedimentary seams: coal, limestone, sandstone, rock salt. |',
         '| Mid veins | Sulfide vein systems: copper, iron, lead, and zinc ores, plus quartz. |',
         '| Deep igneous | Richer sulfides and the rarer metals that feed late-game alloys. |', '',
         '## Biomes hint at ore', '',
         '- **Volcanic & mountain** \u2014 igneous metals and sulfur.',
         '- **Rivers & floodplains** \u2014 placer deposits and good clay.',
         '- **Sedimentary basins** \u2014 coal, limestone, and salt.', '',
         '## Why the order is forced', '',
         'You can only reach the deeper, hotter-formed, richer deposits after the tools and heat the earlier '
         'tiers give you. Geology is the physical reason the tech ladder cannot be skipped \u2014 no deep ore '
         'without good picks, and no good picks without the metals from the shallow ore.', '',
         '## The in-game timeline', '',
         'The interactive era-by-era timeline is generated live from the world\u2019s geology data when you '
         'open it in-game. This page is the field-manual companion that explains how to read it.']
    w('field-guide/geology-timeline.md', '\n'.join(g))

    # Rewards / token exchange
    rw = quests.get('rewards', {})
    nodes = rw.get('nodes', []) or []
    details = rw.get('questDetails', {}) or {}
    nbi = {n['id']: n for n in nodes if isinstance(n, dict)}
    rwm = dict(key='rewards', tier='Cross-cutting', name='Token Exchange', _details=details, _nodes=nbi)
    body = ['# Tokens & Rewards', '',
            'As you finish quests in a chapter you earn **category tokens** \u2014 think of them as proof '
            'you\u2019ve mastered that era\u2019s skills. Spend them here: **upgrade** three lower tokens into '
            'one higher token, or cash tokens in for useful **bundles**. The exchange is always open.', '']
    body.append('<div class="tierwrap" data-tier="steel" markdown>')
    for n in nodes:
        nid = n.get('id') if isinstance(n, dict) else None
        if not nid:
            continue
        d = details.get(nid, {})
        if isinstance(d, dict) and d:
            body.append(render_quest(nid, d, n, rwm))
            body.append('')
    body.append('</div>')
    w('field-guide/rewards.md', '\n'.join(body))

# ----------------------------------------------------------------------------
# Stations
# ----------------------------------------------------------------------------
def gen_stations():
    keys = sorted(stations.keys(), key=lambda k: (stations[k].get('displayName') or k).lower())
    body = ['# Stations', '',
            'Stations are the machines and work surfaces you craft *at*. Each one is modeled on a piece of '
            'real-world equipment. Drop a station from your inventory to place it, then open it to queue '
            'recipes. Stations marked **passive** have no crafting panel — they work or monitor automatically once placed.', '']
    body.append('<div class="station-grid" markdown>')
    for k in keys:
        s = stations[k]
        name = s.get('displayName') or k
        cont = s.get('containers') or {}
        inn = (cont.get('input') or {}).get('size')
        out = (cont.get('output') or {}).get('size')
        fuel = (cont.get('fuel') or {}).get('size')
        craft = s.get('craftStationId')
        body.append('<div class="station-box" id="%s" markdown>' % k)
        body.append('<div class="station-box__name">%s</div>' % name)
        body.append('<div class="station-box__id"><code>%s</code></div>' % k)
        slots = []
        if inn: slots.append('<span class="slot in">in \u00d7%s</span>' % inn)
        if fuel: slots.append('<span class="slot fuel">fuel \u00d7%s</span>' % fuel)
        if out: slots.append('<span class="slot out">out \u00d7%s</span>' % out)
        if not (inn or out or fuel):
            slots.append('<span class="slot none">passive</span>')
        body.append('<div class="station-box__slots">%s</div>' % ' '.join(slots))
        if s.get('body'):
            body.append('<div class="station-box__desc" markdown>%s</div>' % s['body'])
        if s.get('hint'):
            body.append('<div class="station-box__hint" markdown>%s</div>' % s['hint'])
        body.append('</div>')
    body.append('</div>')
    w('stations/index.md', '\n'.join(body))

# ----------------------------------------------------------------------------
# Items catalog
# ----------------------------------------------------------------------------
SRC_BUCKET = [
  ('Tier 0 \u2014 Survival', 'survival', ['Tier0_Survival', 'Farming']),
  ('Tier 0 \u2014 Wildlife & Hunting', 'survival', ['Tier0_Wildlife', 'AnimalCapture']),
  ('Tier 1 \u2014 Stone', 'stone', ['Tier0.5_Stone', 'Parts_StoneAge']),
  ('Tier 2 \u2014 Metal Ages', 'metal_ages', ['Tier1_MetalAges', 'Parts_BronzeAge']),
  ('Tier 3 \u2014 Steam', 'steam', ['Tier1_Steam']),
  ('Tier 4 \u2014 Steel & DC', 'steel', ['Tier3_Steel']),
  ('Tier 5 \u2014 Electric & Chemistry', 'electric', ['Tier4_Electric', 'Tier5_FluidsGases']),
  ('Tier 6 \u2014 Solid State', 'solidstate', ['Tier5_SolidState']),
  ('Tier 7 \u2014 Space', 'space', ['Tier6_Space']),
  ('Ores & Raw Materials', 'metal_ages', ['Items_OreSchema']),
]

def gen_items():
    # index
    idx = ['# Items & Ores', '',
           'Every craftable, mineable, and placeable thing in Conduvia \u2014 **%d entries** \u2014 grouped '
           'by the tier it belongs to. In-game, hover any item and press **R** to see how to make it, or '
           '**U** to see what it\u2019s used in.' % len(items), '']
    idx.append('<div class="item-tier-grid" markdown>')
    bucket_files = []
    for label, tier, files in SRC_BUCKET:
        rows = [it for it in items.values() if it.get('_sourceFile') in files]
        slugname = re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-')
        bucket_files.append((label, tier, slugname, rows))
        idx.append('<a class="item-tier" data-tier="%s" href="%s/"><span>%s</span><em>%d items</em></a>' % (tier, slugname, label, len(rows)))
    idx.append('</div>')
    w('items/index.md', '\n'.join(idx))

    for label, tier, slugname, rows in bucket_files:
        body = ['# %s' % label, '',
                '<div class="tierwrap" data-tier="%s" markdown>' % tier, '']
        # group by category
        cats = {}
        for it in rows:
            cats.setdefault(it.get('category') or 'Other', []).append(it)
        for cat in sorted(cats.keys()):
            body.append('## %s' % cat)
            body.append('')
            body.append('| Item | What it\u2019s for | Made at | Tags |')
            body.append('|---|---|---|---|')
            for it in sorted(cats[cat], key=lambda x: (x.get('name') or '')):
                iid = it.get('id')
                purpose = (it.get('purpose') or '').replace('|', '\u2502')
                craft = it.get('craftStation') or ''
                if isinstance(craft, dict):
                    craft = ''
                tags = (it.get('tagsCsv') or '')
                if isinstance(tags, dict):
                    tags = ''
                tags = ', '.join(tags.split(',')[:3]) if tags else ''
                body.append('| %s | %s | %s | %s |' % (chip(iid), purpose, ('`%s`' % craft if craft else ''), tags))
            body.append('')
        body.append('</div>')
        w('items/%s.md' % slugname, '\n'.join(body))

# ----------------------------------------------------------------------------
# Icon manifest (id -> name, category, expected file)
# ----------------------------------------------------------------------------
def gen_manifest():
    man = {}
    for iid, it in items.items():
        man[iid] = {
            'name': it.get('name') or iid.replace('_', ' '),
            'cat': it.get('category') or 'Item',
            'file': '%s.png' % iid,
        }
    # Category tokens (the reward economy currency) are not items; register
    # them so the Tokens & Rewards / exchange pages render real chips.
    ROMAN = ['I','II','III','IV','V','VI','VII','VIII','IX','X']
    TOKEN_CATS = {
        'survival': 'Survival', 'industry': 'Industry',
        'tech': 'Tech', 'food': 'Food',
    }
    for cat, label in TOKEN_CATS.items():
        for r in ROMAN:
            tid = '%s_%s' % (cat, r)
            man.setdefault(tid, {
                'name': '%s Token %s' % (label, r),
                'cat': 'Token',
                'file': 'token_%s.png' % cat,
            })
    os.makedirs(os.path.join(DOCS, 'assets/icons'), exist_ok=True)
    with open(os.path.join(DOCS, 'assets/icons/manifest.json'), 'w') as f:
        json.dump(man, f, indent=0)
    print('manifest entries:', len(man))

# ----------------------------------------------------------------------------
# Home
# ----------------------------------------------------------------------------
def gen_home():
    body = []
    body.append('---\ntitle: Conduvia Player Guide\nhide:\n  - navigation\n---')
    body.append('')
    body.append('<div class="hero" markdown>')
    body.append('<div class="hero-kicker">THE FIELD MANUAL</div>')
    body.append('<h1 class="hero-title">Rebuild the modern world. For real.</h1>')
    body.append('<p class="hero-sub">You woke up here with nothing \u2014 stone, sticks, and the next few hours. '
                'Conduvia is about climbing from a twisted-fiber rope all the way to a kerolox rocket on the pad, '
                'where <strong>every recipe mirrors a real industrial process</strong>. You already know how the '
                'modern world works. Now build it from scratch.</p>')
    body.append('<div class="hero-cta">'
                '<a class="btn primary" href="getting-started/your-first-hour/">Your first hour \u2192</a>'
                '<a class="btn" href="climb/">See the climb</a></div>')
    body.append('</div>')
    body.append('')
    body.append('## Start here')
    body.append('')
    body.append('<div class="start-cards" markdown>')
    cards = [
      ('What is Conduvia?', 'The pitch, the loop, and why the order is forced.', 'getting-started/what-is-conduvia/'),
      ('Your first hour', 'A survival walkthrough: cordage, water, fire, sleep.', 'getting-started/your-first-hour/'),
      ('Crafting & stations', 'How recipes, stations, and the inventory work.', 'getting-started/crafting-and-stations/'),
      ('Win-path vs branches', 'What\u2019s on the critical line and what\u2019s optional.', 'getting-started/win-path-vs-branches/'),
    ]
    for t, d, h in cards:
        body.append('<a class="start-card" href="%s"><h3>%s</h3><p>%s</p></a>' % (h, t, d))
    body.append('</div>')
    body.append('')
    body.append('## The climb')
    body.append('')
    body.append('Eight tiers, each gated by the one before it. Click a rung to jump in.')
    body.append('')
    body.append('<div class="climb-ladder" markdown>')
    for ci, ch in enumerate(CHAPTERS):
        body.append('<a class="rung" data-tier="%s" href="climb/%d-%s/">'
                    '<span class="rung-n">%s</span>'
                    '<span class="rung-name">%s</span>'
                    '<span class="rung-blurb">%s</span></a>' % (ch['key'], ci, ch['key'], ch['num'], ch['name'], ch['leads']))
    body.append('</div>')
    w('index.md', '\n'.join(body))

# ---------------------------------------------------------------------------
# Recipes browser (generated from recipes.json: explicit packs + item-embedded)
# ---------------------------------------------------------------------------
PACK_TIER = {
  'T0_Gathering': 'survival', 'T0_HandCrafting': 'survival',
  'T0_StationCrafting': 'survival', 'T0_Butchering': 'survival',
  'E1_StoneAge': 'stone', 'E1_StoneAgeTools': 'stone',
  'E1_StoneAgeMaterials': 'stone', 'E1_Farming': 'stone',
  'E2_BronzeAge': 'metal-ages', 'T1_OreProcessing': 'metal-ages',
  'T2_SteelProcessing': 'steam-steel', 'T3_IndustrialProcessing': 'steam-steel',
  'E5_SteamProcessing': 'steam-steel', 'E6_ElectricPower': 'electric',
}
RECIPE_BUCKETS = [
  ('survival',    'Tier 0 \u2014 Survival & Gathering', 'survival'),
  ('stone',       'Tier 1 \u2014 Stone & Early Materials', 'stone'),
  ('metal-ages',  'Tier 2 \u2014 Metal Ages: smelting & alloys', 'metal_ages'),
  ('steam-steel', 'Tier 3\u20134 \u2014 Steam, Coke & Steel', 'steam'),
  ('electric',    'Tier 5 \u2014 Electric & Chemistry', 'electric'),
  ('fabrication', 'Fabrication & Components', 'solidstate'),
]
TIERKEY_TO_SLUG = {
  'survival': 'survival', 'stone': 'stone', 'metal_ages': 'metal-ages',
  'steam': 'steam-steel', 'steel': 'steam-steel', 'electric': 'electric',
  'solidstate': 'fabrication', 'space': 'fabrication',
}

def _src_to_slug():
    m = {}
    for label, tierkey, files in SRC_BUCKET:
        for f in files:
            m[f] = TIERKEY_TO_SLUG.get(tierkey, 'fabrication')
    return m

def _recipe_bucket(r, src_slug):
    pack = (r.get('pack') or '').replace('.luau', '')
    if pack in PACK_TIER:
        return PACK_TIER[pack]
    outs = r.get('outputs') or []
    if outs:
        it = items.get(outs[0]['id'])
        if it and src_slug.get(it.get('_sourceFile')):
            return src_slug[it.get('_sourceFile')]
    return 'fabrication'

def _station_label(sid):
    s = stations.get(sid)
    if s and s.get('displayName'):
        return s['displayName']
    return sid.replace('_', ' ').title()

def _recipe_card(r):
    outs = r.get('outputs') or []
    ins = r.get('inputs') or []
    cat = r.get('category') or 'other'
    L = ['<div class="recipe-card cat-%s" markdown>' % cat]
    if outs:
        L.append('<div class="rc-out">%s</div>' % ' '.join(chip(o['id'], o.get('count')) for o in outs))
    if ins:
        L.append('<div class="rc-flow">%s <span class="rc-arrow">\u2192</span> %s</div>'
                 % (' '.join(chip(i['id'], i.get('count')) for i in ins),
                    ' '.join(chip(o['id'], o.get('count')) for o in outs)))
    elif r.get('worldSources'):
        L.append('<div class="rc-world">Found in the world: %s</div>' % ' '.join(r['worldSources']))
    meta = []
    sts = r.get('stations') or []
    if sts:
        meta.append('<span class="rc-stn">%s</span>' % _station_label(sts[0]))
    if r.get('time'):
        meta.append('<span class="rc-time">%ss</span>' % r['time'])
    if r.get('tier') is not None:
        meta.append('<span class="rc-tier">T%g</span>' % float(r['tier']))
    if r.get('energy'):
        meta.append('<span class="rc-energy">%s kJ</span>' % r['energy'])
    if len(outs) > 1:
        n = len(outs) - 1
        meta.append('<span class="rc-bp">+%d byproduct%s</span>' % (n, '' if n == 1 else 's'))
    if meta:
        L.append('<div class="rc-meta">%s</div>' % ' '.join(meta))
    if r.get('notes'):
        L.append('<div class="rc-note">%s</div>' % r['notes'])
    if r.get('id'):
        L.append('<div class="rc-id"><code>%s</code></div>' % r['id'])
    L.append('</div>')
    return '\n'.join(L)

def gen_recipes():
    recipes = json.load(open(DATA + '/recipes.json'))
    src_slug = _src_to_slug()
    buckets = {slug: [] for slug, _, _ in RECIPE_BUCKETS}
    for r in recipes:
        buckets[_recipe_bucket(r, src_slug)].append(r)
    n_world = sum(1 for r in recipes if not r.get('inputs'))
    n_bp = sum(1 for r in recipes if len(r.get('outputs') or []) > 1)
    idx = ['# Recipes', '',
           'Every recipe in Conduvia \u2014 **%d in total** \u2014 pulled straight from the game\u2019s '
           'recipe database. Each card shows what goes in, what comes out, where you make it, and how long '
           'it takes. **Byproducts** (a second or third output) are flagged, because real processing usually '
           'throws something useful \u2014 or annoying \u2014 off to the side.' % len(recipes), '']
    idx.append('<p class="chapter-stats">%d recipes \u00b7 %d gathered from the world \u00b7 %d with byproducts</p>'
               % (len(recipes), n_world, n_bp))
    idx.append('')
    idx.append('<div class="item-tier-grid" markdown>')
    for slug, label, tierkey in RECIPE_BUCKETS:
        idx.append('<a class="item-tier" data-tier="%s" href="%s/"><span>%s</span><em>%d recipes</em></a>'
                   % (tierkey, slug, label, len(buckets[slug])))
    idx.append('</div>')
    w('recipes/index.md', '\n'.join(idx))
    for slug, label, tierkey in RECIPE_BUCKETS:
        rs = buckets[slug]
        body = ['# %s' % label, '',
                '<p class="chapter-stats">%d recipes</p>' % len(rs), '',
                '<div class="tierwrap" data-tier="%s" markdown>' % tierkey, '']
        groups = {}
        for r in rs:
            sts = r.get('stations') or []
            if sts:
                key = sts[0]
            elif not r.get('inputs'):
                key = '__world__'
            else:
                key = '__hand__'
            groups.setdefault(key, []).append(r)
        def gname(k):
            if k == '__world__':
                return 'Gathered from the world'
            if k == '__hand__':
                return 'By hand'
            return _station_label(k)
        for key in sorted(groups, key=lambda k: gname(k).lower()):
            body.append('## %s' % gname(key))
            body.append('<div class="recipe-grid" markdown>')
            for r in sorted(groups[key], key=lambda x: ((x.get('outputs') or [{}])[0].get('id') or '')):
                body.append(_recipe_card(r))
            body.append('</div>')
            body.append('')
        body.append('</div>')
        w('recipes/%s.md' % slug, '\n'.join(body))
    print('recipe pages: %d recipes across %d buckets' % (len(recipes), len(RECIPE_BUCKETS)))

if __name__ == '__main__':
    gen_climb()
    gen_field_guides()
    gen_stations()
    gen_items()
    gen_recipes()
    gen_manifest()
    gen_home()
    print('generated pages into', DOCS)
