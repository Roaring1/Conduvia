# -*- coding: utf-8 -*-
"""Native MkDocs hook (no plugin install required).

Expands inline shortcodes in page markdown:

    :ci[item_id]            -> item chip (icon + name)
    :ci[item_id|3]          -> item chip with a count
    :icon[item_id]          -> bare icon glyph only

Icons resolve to docs/assets/icons/<id>.png via the icon manifest. Until a real
icon exists, a category-tinted two-letter monogram shows in its place, so the
site is fully legible while the art is still being drawn.

Works with `use_directory_urls: true` (the default). The relative asset prefix
is computed from each rendered page's directory depth so icons resolve from any
page.
"""
import json
import os
import re
import html

_MANIFEST = None
_LINKMAP = None
_CI_RE = re.compile(r':ci\[([a-zA-Z0-9_\-./]+?)(?:\|([0-9]+))?\]')
_ICON_RE = re.compile(r':icon\[([a-zA-Z0-9_\-./]+?)\]')

# Category -> accent colour for the monogram fallback chip.
_CAT_COLOR = {
    'Material': '#9c6b3f', 'Food': '#6f8f4e', 'Tool': '#5a626b',
    'Station': '#b08d57', 'Component': '#b5713b', 'Chemistry': '#2f7fd1',
    'Space': '#3a3f7a', 'Machine': '#5a626b', 'Container': '#8d8a82',
    'Electronics': '#7d5bd6', 'Power': '#f0a830', 'Ore': '#9c6b3f',
    'Fluid': '#38c6e0', 'Gas': '#38c6e0', 'Token': '#c79a3a',
}


def _load_manifest(config):
    global _MANIFEST
    if _MANIFEST is not None:
        return _MANIFEST
    docs_dir = config.get('docs_dir')
    path = os.path.join(docs_dir, 'assets', 'icons', 'manifest.json')
    try:
        with open(path) as f:
            _MANIFEST = json.load(f)
    except Exception:
        _MANIFEST = {}
    return _MANIFEST


def _load_linkmap(config):
    global _LINKMAP
    if _LINKMAP is not None:
        return _LINKMAP
    docs_dir = config.get('docs_dir')
    path = os.path.join(docs_dir, 'assets', 'data', 'linkmap.json')
    try:
        with open(path) as f:
            _LINKMAP = json.load(f)
    except Exception:
        _LINKMAP = {}
    return _LINKMAP


def _prefix(page):
    # Compute the relative path back to the site root for the page's RENDERED
    # location. With use_directory_urls: true, 'a/b.md' is served at 'a/b/'
    # (depth 2) and 'a/index.md' at 'a/' (depth 1); 'index.md' is the root.
    src = page.file.src_uri  # e.g. 'climb/0-survival.md'
    parts = src.split('/')
    stem = parts[-1].rsplit('.', 1)[0]
    depth = len(parts) - 1 if stem == 'index' else len(parts)
    return '../' * depth


def _monogram(name):
    parts = [p for p in re.split(r'[\s_\-]+', name) if p]
    if len(parts) >= 2:
        return (parts[0][0] + parts[1][0]).upper()
    return name[:2].upper()


def _chip(item_id, count, manifest, prefix, icon_only=False, linkmap=None):
    meta = manifest.get(item_id, {})
    name = meta.get('name', item_id.replace('_', ' '))
    cat = meta.get('cat', 'Item')
    fname = meta.get('file', item_id + '.png')
    color = _CAT_COLOR.get(cat, '#7a6a55')
    src = prefix + 'assets/icons/' + fname
    mono = _monogram(name)
    safe_name = html.escape(name)
    glyph = (
        '<span class="ci-glyph">'
        '<span class="ci-mono" style="--ci-color:%s">%s</span>'
        '<img class="ci-ico" src="%s" alt="" loading="lazy" '
        'onerror="this.style.display=&#39;none&#39;">'
        '</span>'
    ) % (color, html.escape(mono), html.escape(src))
    if icon_only:
        return '<span class="ci icon-only" title="%s">%s</span>' % (safe_name, glyph)
    cnt = ''
    if count:
        cnt = '<span class="ci-count">\u00d7%s</span>' % html.escape(str(count))
    chip = ('<span class="ci" data-cat="%s" title="%s">%s'
            '<span class="ci-name">%s</span>%s</span>') % (
        html.escape(cat), safe_name, glyph, safe_name, cnt)
    # Wrap in a link to the item's catalogue entry when we know where it lives.
    target = (linkmap or {}).get(item_id)
    if target:
        href = html.escape(prefix + target)
        return '<a class="ci-link" href="%s">%s</a>' % (href, chip)
    return chip


# Fenced code blocks (``` / ~~~) and inline code spans (`...`). Shortcodes
# inside these must NOT be expanded, so syntax examples like `:ci[item_id]`
# render literally instead of turning into chips.
_CODE_RE = re.compile(r'(```.*?```|~~~.*?~~~|`[^`\n]*`)', re.DOTALL)


def on_page_markdown(markdown, page, config, files):
    manifest = _load_manifest(config)
    linkmap = _load_linkmap(config)
    prefix = _prefix(page)

    def ci_sub(m):
        return _chip(m.group(1), m.group(2), manifest, prefix, icon_only=False, linkmap=linkmap)

    def icon_sub(m):
        return _chip(m.group(1), None, manifest, prefix, icon_only=True)

    # Split on code segments; expand only the non-code parts (odd indices are
    # the captured code spans, left untouched).
    out = []
    for i, seg in enumerate(_CODE_RE.split(markdown)):
        if i % 2 == 1:
            out.append(seg)
        else:
            seg = _ICON_RE.sub(icon_sub, seg)
            seg = _CI_RE.sub(ci_sub, seg)
            out.append(seg)
    return ''.join(out)
