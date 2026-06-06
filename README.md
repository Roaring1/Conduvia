# Conduvia — Player Field Manual (MkDocs)

The player-facing help site for **Conduvia**, a survival-to-orbit game where
every recipe mirrors a real industrial process. This is a **“what do I do”**
guide for end users, with the **questbook as its spine**.

Most of the site is **generated from the game’s own Lua data** — quests, items,
and stations — so the manual stays honest to what actually ships.

---

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve          # preview at http://127.0.0.1:8000
mkdocs build          # output to ./site
```

> The repo ships with pre-generated pages in `docs/`, so it builds immediately
> — no game source needed just to preview.

## Deploy to GitHub Pages

```bash
mkdocs gh-deploy      # builds and pushes to the gh-pages branch
```

The site is configured for `https://roaring1.github.io/Conduvia/`.

---

## Regenerating from the game

When quests/items/stations change, regenerate the data-driven pages from a
checkout of the game code:

```bash
# 1. extract structured JSON from the Lua sources
python tools/extract.py --code /path/to/Conduvia/Code --out data

# 2. rebuild the markdown pages from that JSON
CONDUVIA_DATA=data CONDUVIA_DOCS=docs python tools/gen_pages.py
```

`tools/lualit.py` is a tolerant Lua-literal reader used by the extractor (no Lua
runtime required). See `tools/` for details.

---

## Icons (work in progress)

Item icons are referenced through `docs/assets/icons/manifest.json` (item id →
expected `*.png`). Until the real art lands, each item shows a category-tinted
two-letter monogram, so the site is fully legible today. Drop finished icons
into `docs/assets/icons/<item_id>.png` and they appear automatically — no code
changes. See `docs/assets/icons/README.md`.

---

## Layout

```
mkdocs.yml              site config, nav, theme
hooks/shortcodes.py     :ci[id] item-chip + :icon[id] shortcodes (native hook)
overrides/              theme template tweaks (fonts, announce bar)
docs/
  index.md              home
  getting-started/      hand-written onboarding
  climb/                THE CLIMB — one page per tier (generated)
  field-guide/          ore guide, geology, tokens (generated)
  stations/             station infoboxes (generated)
  items/                full item catalogue by tier (generated)
  reference/            legends + real-process glossary (hand-written)
  assets/css/           the field-manual design system
  assets/icons/         icon manifest + drop-in art
tools/                  extractor + page generator
data/                   extracted JSON snapshot
```

## Design intent

This is meant to read like **an engineer’s field manual**, not a wiki: paper /
blueprint substrate, a humanist sans paired with a technical mono, a per-tier
colour palette, icons over emoji, and purpose-built components (quest cards,
tier-gate banners, station infoboxes, “why this is real” notes). Keep that bar.
