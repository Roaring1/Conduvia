# Conduvia docs — fix log (this session)

All fixes edit the **committed markdown / CSS / config directly**. The generator
(`tools/gen_pages.py`) is intentionally NOT re-run, because the committed
`data/*.json` is stale (732 items / 571 recipes / 93 stations) versus the
published site (832 / 685 / 153). Regenerating would revert the site and drop
the Formula column. Source of truth for canonical numbers: **832 items · 685
recipes · 153 stations · 27 chains**.

---

## Theme 1 — Math rendering (F1 / F36 / F60 / F70)

**Problem:** `$$…$$` chemistry equations rendered as literal LaTeX because
`mkdocs.yml` had no math extension and no MathJax loader.

**Fixes:**
- `mkdocs.yml`: added `pymdownx.arithmatex: {generic: true}` to
  `markdown_extensions`, and added an `extra_javascript` block loading
  `assets/js/mathjax-config.js` + MathJax 3 (`tex-mml-chtml.js`).
- `docs/assets/js/mathjax-config.js`: new file — MathJax 3 config wired to
  arithmatex generic mode, with Material instant-navigation re-typeset hook.
- `docs/field-guide/copper.md`: converted the 3 fragile single-line `$$…$$`
  equations (L36/41/46) to safe multi-line block form, matching the style used
  in air-ammonia/silicon/zirconium.
- `docs/field-guide/copper-oxide-sx-ew.md`: fixed the chemistry typo
  **H₂SO₂₄ → H₂SO₄** in prose at lines 8 and 20 (the page already wrote the
  correct H₂SO₄ in its equations).

**Validation:** `mkdocs.yml` parses as valid YAML; arithmatex present;
zero remaining single-line `$$…$$`; zero remaining `H₂SO₂₄`.

---

## Theme 2 — Stale roadmap / forward-looking prose (F3 / F17 / F34 / F35)

**Problem:** Several pages still described already-built chains as future work.

**Fixes:**
- `docs/design/todo.md`: rewritten. Moved the “Copper chain — next working
  session” item and all completed chains into **Done**; added a success banner
  noting all 27 chains (832/685/153) are built; corrected the false “0 real
  PNGs” icon claim; reframed the remaining backlog as balance/docs/presentation.
- `docs/design/missing-chains.md`: rewritten from a “chains we still owe” roadmap
  into a “roadmap cleared” record, each former-priority chain now linking to its
  built field guide.
- `docs/field-guide/copper.md`: “Oxide route (SX-EW, planned)” → “(built)”, and
  the roadmap link now points to the SX-EW field guide; byproduct-loop tip
  reworded from “Build that chain…” to “That chain is built…”.
- `docs/field-guide/iron-steel.md`: ferrochrome/ferronickel “placeholders …
  upcoming work” note rewritten to point at the built Ferroalloys field guide.

**Validation:** all newly referenced field-guide/design pages exist; no residual
stale promise words remain in the design pages.

---

## Theme 3 — Stat contradictions (F4 / F5 / F12 / F32 / F38)

**Problem:** `docs/design/balance-review.md` contradicted itself — the top
metrics table held the correct figures, but the prose below restated stale ones.

**Fixes (prose reconciled to the canonical table + 832-item base):**
- multi-output: “We're at 16%” → “We're at 24%” (matches the 24% in the table).
- trivial taps: “### 4. Kill or enrich the 103 trivial taps” → “128 trivial taps”
  (matches the 19% / 128 figure in the table).
- time coverage: “Over half of recipes are instant … extend coverage from 44% →
  ~100%” → “About 40% of recipes are instant … extend coverage from 60% →
  ~100%” (matches the 60% timed figure in the table).
- reachability: removed the stale “454 / 713” base and the precise 133/131
  splits (computed on an old 713-item set) and reframed against the canonical
  **832-item** set without inventing new precise counts; kept the keystone list
  and the qualitative conclusion.

**Validation:** no residual `713` / `454` / `16%` / `44%` / `103 trivial` /
“Over half … instant” strings remain; canonical 24% / 60% / 128 / 832 present.

---

## Theme 4 — “Generated from source” claim + Formula column (F16 / F63 / F25 / F49 / F69)

**Problem:** The site claimed it was generated from game data, but the committed
`gen_pages.py` emits a 4-column item table with **no Formula column**, while the
committed item pages are 5-column **with** Formula (F63), and the committed
`data/*.json` is stale versus the live world (F71). So “regenerate it” would
*revert* content. The Formula column is also ~84% empty (699/832 blank).

**Fixes:**
- `overrides/main.html`: announce banner “generated from … game data. If the game
  changes, regenerate it.” → “built from … game data and then hand-tuned. If the
  game changes, re-sync it.”
- `docs/reference/how-this-site-is-built.md`: reworded the opening claim to
  “generated … then hand-tuned”; added a warning box that the committed
  `data/*.json` can lag the live game (832/685/153) and that pages carry
  hand-added detail (e.g. the Formula column) the generator does not emit, so
  re-running it against a stale snapshot reverts rather than refreshes; reworded
  “Everything … is generated” to “scaffolded … then hand-augmented.”

**Deliberately NOT done:** auto-filling the 699 blank Formula cells. Fabricating
chemical formulae would introduce inaccuracy (the opposite of the audit’s goal);
the gap is now disclosed honestly and left on the backlog (todo.md) for a
sourced backfill. Raw gathered items legitimately have no formula.

**Validation:** remaining “regenerate/regenerated” hits in docs are chemistry
prose (acid loops), not build claims.

---

## Theme 5 — Station-name normalization (F8 / F10 / F42 / F53 / F62 / F64 / F65)

**Problem:** Station labels drifted across surfaces. The item “Made at” column
matched the station catalogue **0/39** (raw `snake_case` ids like
`arc_furnace_electric` and invented names like `machine shop (electric)`), and
recipe cards matched only 107/121. The canonical names live in the 153 station
boxes in `stations/index.md` (each box has an `id` + a displayName).

**Fix:** Built an id→displayName map from the 153 station boxes, plus a
normalized-name and normalized-id index, and rewrote every station label on both
surfaces to the canonical displayName:
- **Item “Made at” column:** 285 cells normalized across all 11 item pages
  (e.g. `` `arc_furnace_electric` `` → *Electric Arc Furnace*,
  `machine shop (electric)` → *Electric Machine Shop*,
  `iron anvil block` → *Iron Anvil*, `assembler_workshop` → *Assembly Cell*).
- **Recipe `rc-stn`:** 153 labels normalized
  (e.g. *Machine Shop (Electric)* → *Electric Machine Shop*,
  *Iron Anvil Block* → *Iron Anvil*, *Earthen Kiln (Updraft)* → *Earthen Kiln*,
  *Stamp Mill (Manual Trip Hammer)* → *Trip Hammer*, *Coke Oven (Beehive)* →
  *Beehive Coke Oven*).
- A few near-misses mapped explicitly: *Fluid Handler Station* → *Fluid Handler*,
  *Small Blast Furnace* → *Blast Furnace*, *Campfire* → *Survival Campfire*,
  *DC dynamo (workshop)* → *DC Workshop Dynamo*.

**Intentionally left as-is:** “Hand” (2×2 inventory hand-crafting) — there is no
station box for it, so both surfaces now show a single consistent **Hand** label
rather than inventing a station.

**Validation:** re-audit confirms every station label on both surfaces resolves
to a real catalogue station, with only the intentional **Hand** label remaining.

---

## Theme 6 — Hyperlinking (F6 / F46 / F66 + F15 / F26 / F30 / F33)

**Problem:** The audit found ~4,574 item chips but only ~74 real links, with
51 of 71 pages containing zero links. The `:ci[…]` shortcode rendered every item
as a non-clickable `<span class="ci">`, and station references were plain text,
so the catalogue was effectively un-navigable.

**Fix — item chips are now links:**
- Added a per-item anchor (`<span class="item-anchor" id="i-<id>">`) to all 832
  catalogue rows across the 11 item pages, giving every item a stable deep-link
  target.
- Generated `docs/assets/data/linkmap.json` (832 entries) mapping each item id
  to its catalogue page + anchor.
- Modified the `:ci` shortcode hook (`hooks/shortcodes.py`) to load the linkmap
  and wrap every full chip in `<a class="ci-link" href="…">`, with the relative
  path computed per rendering page (works at every directory depth). Bare
  `:icon[…]` glyphs are intentionally left unlinked. Chips for ids not in the
  catalogue (e.g. orphan byproduct ids) gracefully stay non-links.
  → This makes every catalogued item chip clickable on every recipe, item, and
  guide page — thousands of new links from a single hook change.

**Fix — station references are now links:**
- Linked 560 recipe-card `rc-stn` labels and 260 item “Made at” cells to their
  station box in the catalogue (`stations/#<station_id>`), reusing the existing
  per-box `id` anchors. “Hand” (no station box) is intentionally left as plain
  text.

**Styling:** Added `.ci-link` / `.stn-link` rules to `conduvia.css` so links
inherit the chip/label styling (no default blue underline) with a quiet hover
and keyboard focus ring.

**Validation:** hook compiles; offline render simulation confirms chips become
`<a>` links with correct relative paths at root, item, and recipe depths;
linkmap = 832 entries; all 832 item rows keep exactly 5 columns (no table
breakage); CSS braces balanced.

---

## Theme 8 — Accuracy & polish cleanup (F22/F23/F68, F24/F56, F41, F52, F11/F57, F27, F44)

### Controls keymap (F22 / F23 / F68) — the audit was internally contradictory; resolved against source
F22 (read from `Schema.luau`) said Inventory = `Tab`, Quest Log = `J`; F68
(read from `ControlsBinder.client.luau` + NEI) said Inventory = `E`, Quest Log =
`Backquote`, and claimed an `R` Sort-vs-Recipes conflict. These disagree, so I
read the actual source:
- The binder file is literally named **`disable _ ControlsBinder.client.luau`**
  (disabled), and its hardcoded `Key` table even writes a setting path
  (`client.controls.inventoryToggle`) that **does not exist** in `Schema.luau`
  (which uses `inventory`). So the binder is stale/inactive.
- The authoritative live config is `Schema.luau` → `controls = { ... }`:
  Inventory `Tab`, Quest Log `J`, Interact `F`, Drop `Q`, **Sort Inventory `G`**,
  Map `M`, Add-Waypoint `B`, Waypoint-List `N`, Push-to-Talk `V`, Screenshot
  `Print`, Sprint `LeftShift`, Crouch `LeftControl`, Slide `C`, Menu `P`;
  NEI: Recipes `R`, Uses `U`, Bookmark `K`, Favourite `A`.

**Verdict:** **F22 is correct; F68 is a false positive** (it read a disabled
script). There is **no real `R` conflict** — Recipes is `R`, Sort Inventory is
`G`.

**Fix:**
- `getting-started/controls.md`: rebuilt the key table from `Schema.luau`
  (Inventory `Tab`, Quest Log `J`, fixed the bogus `Backspace` = Back row to
  Menu `P`, and added the ~8 missing real binds: Sort `G`, Bookmark `K`,
  Waypoint `B`/`N`, Push-to-talk `V`, Slide `C`, Menu `P`, Screenshot). Added a
  note clarifying `R` = Recipes vs `G` = Sort (no conflict).
- `getting-started/your-first-hour.md`: Quest Log `` ` `` → `J`.
- `climb/0-survival.md`: controls table Quest Log → `J`, Inventory → `Tab`,
  Menu → `P`, added Sort `G`; and fixed two “press **E** to interact / sleep”
  instructions to `F` (the real interact key).

### “~85% honest” badge (F24 / F56)
The number is an unsourced vibe-figure. Kept the (accurate) prose and dropped
the made-up percentage — retitled both callouts to **“Honest by design”**
(`reference/glossary.md`, `getting-started/what-is-conduvia.md`).

### Orphan byproduct ids (F41)
Four recipe byproducts used ids absent from the item catalogue. Normalized each
to its canonical id (verified present in both the icon manifest and linkmap, so
they now render **and** link to an item page):
- `CO2` → `gas_co2` (fabrication.md, limestone → quicklime)
- `ash` → `wood_ash` (fabrication.md, campfire cooking)
- `gas` → `gas_syngas` (fabrication.md, coke-oven byproduct)
- `refining_slag` → `slag` (fabrication.md steelmaking + metal-ages.md copper
  fire-refining; matched the metal-ages mermaid node label too)
Confirmed this was the exhaustive set — no loose byproduct ids remain.

### Recipe time formatting (F52)
Normalized `rc-time` so identical durations don't render two ways. Stripped the
trailing `.0` from **217** float-formatted times (`90.0s` → `90s`); verified no
genuine fractional-second values existed, so nothing lossy.

### Hardcoded `/Conduvia/` icon paths (F11 / F57)
Rewrote **590** absolute `/Conduvia/assets/...` `<img>` paths (station boxes and
mermaid diagram icons) to page-relative paths so they resolve under local
`mkdocs serve`, GitHub Pages, and any future base path — matching the relative
prefix the `:ci[]` chip hook already uses:
- `recipes/*.md` → `../../assets/...`
- `stations/index.md` → `../assets/...`
Left the single `/Conduvia/Code --out data` occurrence in
`how-this-site-is-built.md` untouched — it's a CLI example, not an image.

### Recipe cards printed outputs twice (F27)
Every card showed products in a bold `rc-out` line **and** again after the `→`
in the `rc-flow` equation — doubling height for multi-output recipes. Dropped the
redundant `rc-out` **only on the 625 cards that have an equation** (the `rc-flow`
already shows the outputs), while **preserving `rc-out` on the 60 input-less
gathering/world-drop cards** that have no equation. Result: every recipe shows
its outputs exactly once.

### Flow-map promise (F44)
`recipes/index.md` claimed “each chain leads with a flow map,” but survival
(tier-0, the largest page) has none. Softened to “most processing chains lead
with a flow map … Tier-0 gathering and a few simple chains skip the map.”

### Deliberately NOT auto-changed (logged, not silently skipped)
- **F28 — energy-unit mismatch** (`rc-energy` mixes energy `kJ`/`kJ_th` with
  power `W_human`/`W_mech`). Reconciling dimensions requires per-recipe time
  data; converting would mean inventing numbers, so this needs source-data
  normalization, not a doc edit. Left as-is to preserve accuracy.
- **F59 — recipe-id prefix scheme** (45 ad-hoc families). Ids are unique and
  stable; renaming them would break cross-references and the chip/anchor system.
  Cosmetic; out of scope for a safe doc-only pass.

**Validation:** 0 loose byproduct ids; 0 stray `.0s` times; 0 hardcoded
`/Conduvia/assets` paths; recipe cards = 60 `rc-out` / 625 `rc-flow` as intended;
shortcodes hook still compiles.
