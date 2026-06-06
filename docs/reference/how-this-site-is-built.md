# How this site is built

This manual is **mostly generated from Conduvia’s own source data**, so it can’t
drift far from what the game actually does.

## Pipeline

```text
Game Lua sources
   QuestBook/Content/Chapters/*.luau   (quests)
   ItemDatabase/Data/*.luau            (items)
   Stations/StationDefs.luau           (stations)
        |
        |  tools/lualit.py   (tolerant Lua-literal reader, no Lua runtime)
        |  tools/extract.py  ->  data/{quests,items,stations}.json
        v
   tools/gen_pages.py  ->  docs/  (the climb, field guides, stations, items, home)
        |
        v
   mkdocs build  ->  site/
```

- **`tools/lualit.py`** parses Lua table literals directly in Python — strings,
  long-brackets, comments, computed keys, trailing commas, type casts, and string
  concatenation — so no Lua interpreter is needed to read the data.
- **`tools/extract.py`** walks the chapters, item database, and station defs and
  emits clean JSON.
- **`tools/gen_pages.py`** turns that JSON into the markdown you’re reading,
  plus the icon `manifest.json`.

## What’s hand-written

The onboarding (**Getting Started**) and these **Reference** pages are written by
hand — they’re explanation, not data. Everything under **The Climb**,
**Field Guides**, **Stations**, and **Items & Ores** is generated.

## Regenerating

```bash
python tools/extract.py --code /path/to/Conduvia/Code --out data
CONDUVIA_DATA=data CONDUVIA_DOCS=docs python tools/gen_pages.py
mkdocs build
```

## Custom components

The look comes from `docs/assets/css/conduvia.css` (the field-manual design
system) and `tiers.css` (per-tier accents). The `:ci[item_id]` item chips and
`:icon[item_id]` glyphs are expanded by a native MkDocs hook,
`hooks/shortcodes.py` — no third-party plugin required.
