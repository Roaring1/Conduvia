# TODO / Backlog

!!! note "The running list"
    What we've found and will tackle, in priority order. This mirrors the **Conduvia Dev Tracker** in Notion. Check things off as we go; add new items at the bottom of the right section.

## Now / next

- [ ] **Copper chain — full real-life processing.** Design the complete end-to-end copper line (mine → crush → wash → concentrate → roast → smelt → refine → cast/forms) with realistic byproducts, stations, and time costs. This is the **GregTech pilot template** the other metals will be patterned on. *(next working session)*
- [ ] **Audit the `water_raw` keystone.** It gates 15+ downstream recipes (buckets, brine, treated water, ammonium line, electrolysis). Confirm there's an early, obvious, low-friction way to get it. Most load-bearing single item in the graph.

## Recipe balance — GregTech-ification &nbsp;·&nbsp; High

From the [balance review](balance-review.md):

- [ ] **Multi-stage ore → metal lines.** Replace single-tap smelting with `crush → wash/sieve → concentrate → roast → smelt → refine`. Start with `T1_OreProcessing` (16 → ~50 recipes).
- [ ] **Realistic byproducts everywhere.** Stone dust, slag (`waste_slag`/`crushed_slag` already exist), secondary metals from polymetallic ores, wood tar + pyroligneous acid from the charcoal kiln, Cl₂ + H₂ + NaOH from chlor-alkali. Target **≥40% multi-output** (currently 16%).
- [ ] **Material-forms fan-out.** `ingot → plate → foil`, `→ rod → bolt/screw`, `→ wire → fine wire`, each at its own station.
- [ ] **Time on every processing recipe.** Currently only 44% are timed; extend to ~100% and tie duration to station tier. Energy/EU system is a later pass.
- [ ] **Fix the 103 trivial 1-in → 1-out taps.** Merge upstream, or gate behind a tool + time + byproduct (e.g. `stone_river_rounded → stone`, `hammerstone → tool_hammerstone_basic`, `2× tar → pitch`).
- [ ] **Deepen the metal keystones.** `copper_ingot` (d2), `bronze_ingot` (d2), `steel_ingot` (d3) are far too shallow vs GT's 8–15+.

## Content gaps &nbsp;·&nbsp; Medium

- [ ] **131 orphan items** appear in no recipe and are unreachable — decide per item: wire into the graph, or cut. Mostly late-game placeholders.
- [ ] **Token / reward economy** — confirm the category-token upgrade and bundle exchange rates feel earned (Survival/Industry/Tech/Food, tiers I–X).
- [ ] **Geology timeline** entries are generated in-game — confirm the world data drives them correctly on the live site.
- [ ] **Item icon art** — 753 manifest entries, **0 real PNGs** yet; every chip shows the category-tinted monogram fallback. Biggest visual gap. Drop art into `docs/assets/icons/<item_id>.png` (filenames are already mapped in the manifest).
- [ ] **Station-name normalization** — 24 station names used by recipes (e.g. `campfire`, `coke oven (beehive)`, `bessemer converter`) aren’t keys in the stations DB, so they don’t link to a station entry. Reconcile recipe `stations[]` with `stations.json` ids.

## Bugs / risks

- [ ] **Item names are lowercase in source.** 832 items carry lowercase `name` strings; decide on a display-case convention (title-case at render vs. fix at source) so chips and tooltips read cleanly.
- [ ] **224 code TODOs** flagged across the codebase — triage which block the win-path vs. which are cosmetic.

## Done

- [x] Parse **all 685 recipes** into structured data (469 explicit packs + 216 item-embedded), 0 broken references.
- [x] Build the full reachability + orphan analysis across the 832-item set, keystones + orphans identified.
- [x] Run the GregTech balance pass (depth, byproducts, input cardinality, time coverage) — see the [balance review](balance-review.md).
- [x] Publish the full **Recipes** browser on this site (every recipe, byproducts flagged).
- [x] Fix the docs-deploy bugs (Unicode escape artifacts in 15 files; 404s from directory-URL mismatch).
- [x] Site hole-audit: 0 broken links; registered 5 missing byproduct items (CO₂, ash, wood gas, slag, refining slag); replaced the empty geology-timeline page with a real field-manual page.
