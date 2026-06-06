# Recipe balance review — the GregTech lens

!!! note "Dev / design note"
    This is a design document, not a player guide page. It records a full pass over the **merged recipe graph** — **685 recipes** (469 from the explicit RecipeDB packs + 216 item-embedded recipes) — measured against the question: *does this feel like a GregTech-grade industrial chain?*

## The numbers

| Metric | Conduvia today | GregTech-like target |
|---|---|---|
| Max crafting depth (steps from raw) | **7** | 12–18+ |
| Depth distribution | 100 @ d1 · 97 @ d2 · 64 @ d3, then falls off | a fat middle at d5–d10 |
| Recipes with byproducts (>1 output) | **24%** | 40–60% (ore lines especially) |
| Trivial 1-in → 1-out taps | **19%** (128 recipes) | near zero |
| Inputs per recipe (mean / median / max) | **2.12 / 2 / 6** | 4–9 common |
| Recipes with a time cost | **60%** (median 40s, max 720s) | ~100% |

The tell is in the keystone metals:

```text
copper_ingot   = depth 2
bronze_ingot   = depth 2
iron_bloom     = depth 2
wrought_iron   = depth 3
steel_ingot    = depth 3
charcoal       = depth 1
```

In GregTech, copper alone is *crush → wash → centrifuge → smelt*, and steel is a whole saga. Right now `raw_ore_native_copper → smelt → ingot` is essentially the entire copper economy.

## Verdict

**The chemistry is honest, but the graph is shallow and byproduct-poor.** It currently reads closer to *Minecraft+* than GregTech. The good news: the realism is already there, so deepening the chain is mostly *adding the real intermediate steps that actually exist in metallurgy and chemistry* — not inventing fake busywork.

## Where it's thin — and how to deepen it

### 1. Ore → metal is one tap. Make it a line.
This is the single biggest, most realistic win. Replace `ore → smelt → ingot` with the real pipeline:

```text
crush → wash / sieve → concentrate (gravity or froth flotation) → roast / calcine → smelt → refine / cast
```

Every stage is real metallurgy, and every stage naturally produces **byproducts** — stone dust, gangue, slag, and **secondary metals** from polymetallic ores (chalcopyrite → copper **+** pyrite/sulfur; galena → lead **+** silver). One change raises depth, byproduct rate, and realism at once. The `T1_OreProcessing` pack (16 recipes today) is the seed — it wants to be ~50.

### 2. Add the GregTech "material forms" fan-out.
Once you have an ingot, real fabrication makes a *family*, each at a distinct station:

```text
ingot → plate → foil
ingot → rod → bolt / screw
ingot → wire → fine wire
```

Low design cost, high step-density, and exactly how GT stretches one metal into 20–30 recipes.

### 3. Lean into byproducts you already have the chemistry for.
- Charcoal kiln → charcoal **+ wood tar + pyroligneous acid**
- Smelting → **slag** (the `waste_slag` / `crushed_slag` items already exist — wire them in everywhere)
- Chlor-alkali → **Cl₂ + H₂ + NaOH** (triple output)

We're at 16% multi-output; the chemistry to reach ~40% is already real.

### 4. Kill or enrich the 103 trivial taps.
Free clicks like `stone_river_rounded → stone`, `hammerstone → tool_hammerstone_basic`, and `2× tar → pitch` should either be **merged** upstream or **gated** behind a tool + time + a byproduct so they earn their slot.

### 5. Put time (and eventually energy) on everything.
Over half of recipes are instant. GregTech's entire pacing *is* time × power per step. Even before an EU-style energy system, giving every processing recipe a `time` tied to its station tier will make the climb *feel* industrial. The existing range is sane (median 40s, max 720s) — just extend coverage from 44% → ~100%.

## What's already good (don't lose it)

- **Zero broken references** — every recipe input resolves to a real item. The graph is structurally sound.
- **~85% honest chemistry holds** — bronze casting reusing a `stone_mold_ingot`, blood → blood-meal drying, fat → tallow rendering are all real and correctly modeled.
- **The survival/food tier is already deep** (88 food recipes with real preservation). The shallowness is specifically in **ore → metal → industry** — which is exactly the spine to thicken for the rocket climb.

## Reachability sanity (not a bug)

From 54 world-gather outputs plus 81 world-supplied primitives, **454 / 713** items are reachable. **133** are gated behind a handful of **keystones** — `water_raw`, `steam_charge`, `steel_plate_rolled`, `sodium_hydroxide`, `metal_aluminum_ingot`, `plc_*` — and **131** are true orphans (in no recipe and unreachable, mostly late-game placeholders). The keystones are **items to audit**, not missing recipes; the most load-bearing one is `water_raw`.

## The 85% rule

85% real-process fidelity is a **floor, not a ceiling**. Where a mechanic feels shallow or weird, we go *above* it — more steps, more honest byproducts, more intermediate forms — rather than capping the realism to hit a number.
