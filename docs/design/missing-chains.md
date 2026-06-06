# Missing-chains roadmap

Generated from `tools/missing_chains.py`, which walks the recipe graph from
mineable ore + world-gathered inputs and flags every recipe that can't bottom
out. The blocking inputs below are the **chains we still owe**, ranked by how
many recipes and downstream items they gate.

!!! note "Two kinds of gap"
    **NEEDS NEW CHAIN** — the reagent is never produced anywhere; it requires a
    brand-new process chain.<br>
    **mid-chain gap** — the reagent *is* produced, but its own inputs are blocked
    upstream. Fixing the root chain cascades and clears these automatically.

## Priority industrial chains to build next

| Chain | Real process | Unlocks | Notes |
|-------|--------------|---------|-------|
| **Sulfuric acid** (`acid_sulfuric`) | Contact Process: SO₂ → SO₃ → oleum → H₂SO₄ | Copper oxide/SX-EW route, leaching, electrolyte, batteries | **Do this next.** Copper roasting + converting already emit the SO₂ feedstock — closes a real byproduct loop. |
| **Chlor-alkali** (`sodium_hydroxide`, `gas_chlorine`, `gas_hydrogen`) | Brine electrolysis: 2NaCl + 2H₂O → 2NaOH + Cl₂ + H₂ | Lye, bleach, PVC, alumina (Bayer), H₂ for ammonia | Feedstock is `raw_ore_halite` (already mineable). One cell, three products. |
| **Ammonia** (`gas_ammonia`) | Haber-Bosch: N₂ + 3H₂ → 2NH₃ | Fertilizer, nitric acid, explosives | Needs H₂ from chlor-alkali (or steam reforming) + N₂ from air separation. |
| **Air separation** (`cylinder_gas_basic` → O₂/N₂/Ar) | Cryogenic distillation of liquefied air | Oxygen enrichment for smelting, N₂ for Haber, inert gas | Container/cylinder intermediate is also a true gap. |
| **Water supply** (`water_raw`) | Gather/pipe fresh water | 14 recipes downstream | Trivial gathering recipe; add a world-source recipe and the cascade clears. |

## Cascade roots (fix once, clear many)

These block the most recipes but are themselves *made* — so the real fix is
upstream:

- **`steel_plate_rolled` (blocks 41)** and **`steel_beam` (blocks 16)** → finish the
  **iron → steel → rolled-stock** chain to the same depth as copper. Highest leverage
  in the whole graph.
- **`alloy_aluminum_aerospace` (11)**, **`metal_aluminum_ingot` (4)** → the
  **bauxite → alumina (Bayer) → aluminum (Hall-Héroult)** chain, which itself needs
  NaOH (chlor-alkali) and a lot of DC power.
- **`avionics_flight_computer`, `plc_*`, `motor_ac_induction` …** → late-tier
  electronics/space assemblies; they clear naturally once metals + chemistry land.

## Recommended build order

1. **Sulfuric acid** (closes copper's SO₂ loop, unlocks copper oxide/SX-EW route)
2. **Iron → steel → rolled stock** (clears the single biggest cascade, 41+16 recipes)
3. **Chlor-alkali** (NaOH/Cl₂/H₂ from halite — feeds aluminum + ammonia)
4. **Aluminum** (Bayer + Hall-Héroult)
5. **Air separation + ammonia** (gases, fertilizer, nitric acid)

!!! info "Not real gaps"
    Wildlife carcasses, berries, acorns, hides, and tallow show up as
    "NEEDS NEW CHAIN" only because they are **world-gathered**, not crafted. They
    are not processing-chain gaps and are excluded from the priorities above.
