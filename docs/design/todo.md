# TODO / Backlog

!!! note "The running list"
    What we've found and will tackle, in priority order. This mirrors the **Conduvia Dev Tracker** in Notion. Check things off as we go; add new items at the bottom of the right section.

!!! success "All 27 industrial chains are built"
    The current world ships **832 items · 685 recipes · 153 stations** across all
    27 chains — survival → stone → metal ages → steam → steel → electric →
    solid-state → space. Copper (sulfide **and** oxide/SX-EW), sulfuric acid,
    chlor-alkali, ammonia, air separation, iron→steel, ferroalloys, aluminum,
    silicon, titanium, zirconium, uranium and the rest each have a
    [field guide](../field-guide/ore-field-guide.md). The remaining work below is
    **balance, docs, and presentation** — not missing content.

## Now / next

- [ ] **Docs navigation pass.** The catalogue surface (items/, recipes/, stations/) is almost entirely un-hyperlinked — chips render as inert text. Make `:ci[…]` chips link to the item/station they name. *(in progress this session)*
- [ ] **Station-name normalization.** Recipe cards and the item “Made at” column show a mix of raw `snake_case` ids and drifted display names that don’t match the station catalogue. Reconcile every label to the canonical `stations` displayName.
- [ ] **Audit the `water_raw` keystone.** It gates 15+ downstream recipes (buckets, brine, treated water, ammonium line, electrolysis). Confirm there's an early, obvious, low-friction way to get it. Most load-bearing single item in the graph.

## Recipe balance — GregTech-ification &nbsp;·&nbsp; High

From the [balance review](balance-review.md):

- [ ] **Deepen the remaining shallow taps.** Merge or gate the trivial 1-in → 1-out conversions (e.g. `stone_river_rounded → stone`, `hammerstone → tool_hammerstone_basic`, `2× tar → pitch`) behind a tool + time + byproduct.
- [ ] **Material-forms fan-out.** Continue `ingot → plate → foil`, `→ rod → bolt/screw`, `→ wire → fine wire`, each at its own station, for metals that don’t yet have it.
- [ ] **Time + energy coverage.** Extend processing-time coverage toward ~100% and tie duration to station tier; finish the energy/EU pass and settle on one unit convention per card (see balance review).
- [ ] **Multi-output target.** Keep pushing realistic byproducts (stone dust, slag, secondary metals, kiln tar, chlor-alkali co-products) toward the multi-output target tracked in the balance review.

## Content gaps &nbsp;·&nbsp; Medium

- [ ] **Orphan items.** A handful of items still appear in no recipe — decide per item: wire into the graph, or cut.
- [ ] **Token / reward economy** — confirm the category-token upgrade and bundle exchange rates feel earned (Survival/Industry/Tech/Food, tiers I–X).
- [ ] **Geology timeline** entries are generated in-game — confirm the world data drives them correctly on the live site.
- [ ] **Formula column fill.** The item catalogue’s `Formula` column is mostly empty; backfill chemical formulae where they apply (raw gathered items legitimately have none).

## Bugs / risks

- [ ] **224 code TODOs** flagged across the codebase — triage which block the win-path vs. which are cosmetic.

## Done

- [x] **Copper chain — full real-life processing.** Complete end-to-end copper line (mine → crush → float → roast → matte smelt → convert → fire/electro-refine → forms) **plus** the oxide SX-EW route. This was the GregTech pilot template the other metals followed.
- [x] **Build all priority industrial chains.** Sulfuric acid, iron→steel→rolled stock, chlor-alkali, aluminum (Bayer + Hall-Héroult), air separation + ammonia, ferroalloys, and the late-tier chemistry/electronics/space assemblies are all in-world. (Closes the old *missing-chains* roadmap.)
- [x] **Item icon art.** The icon set is in `docs/assets/icons/` and wired through the manifest; chips show real art (category-tinted monogram only as a fallback).
- [x] **Display-case convention.** Item names render Title-cased across the catalogue and chips.
- [x] Parse **all 685 recipes** into structured data (469 explicit packs + 216 item-embedded), 0 broken references.
- [x] Build the full reachability + orphan analysis across the 832-item set, keystones + orphans identified.
- [x] Run the GregTech balance pass (depth, byproducts, input cardinality, time coverage) — see the [balance review](balance-review.md).
- [x] Publish the full **Recipes** browser on this site (every recipe, byproducts flagged).
- [x] Fix the docs-deploy bugs (Unicode escape artifacts in 15 files; 404s from directory-URL mismatch).
- [x] Site hole-audit: 0 broken links; registered missing byproduct items (CO₂, ash, wood gas, slag, refining slag); replaced the empty geology-timeline page with a real field-manual page.
- [x] **Math rendering.** Wired `pymdownx.arithmatex` + MathJax so the chemistry equations render instead of printing as literal `$$…$$`.
