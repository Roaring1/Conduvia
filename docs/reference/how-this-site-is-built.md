# How this site is built

This manual is **mostly generated from Conduvia’s own source data, then hand-tuned**.
The generator gives it a structure that tracks the game; the hand-tuning adds the
extra detail (chemistry formulae, prose, diagrams) that the raw data doesn’t carry.

!!! warning "The committed `data/*.json` can lag the live game"
    The published site reflects the current world (**832 items · 685 recipes ·
    153 stations**). The JSON snapshot checked into `data/` can be older than
    that, and the pages here include hand-added detail (e.g. the **Formula**
    column on item tables) that `gen_pages.py` does not emit. Treat the generator
    as a scaffolder, not the literal source of every page — re-running it against
    a stale snapshot would *revert* content, not refresh it. Always re-extract
    from the live game code first (see **Regenerating** below).

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
hand — they’re explanation, not data. The pages under **The Climb**,
**Field Guides**, **Stations**, and **Items & Ores** are *scaffolded* by the
generator and then hand-augmented — the field-guide chemistry, the item-table
**Formula** column, and the narrative notes are added on top of the generated
structure and are not produced by `gen_pages.py` alone.

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
