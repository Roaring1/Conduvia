# Sulfuric acid — the keystone reagent

Sulfuric acid (H₂SO₄) is the most-produced industrial chemical on Earth, and in
Conduvia it is the first **pure chemistry chain**: no ore body of its own, it is
built entirely from gas you already make. It closes the copper smelter's sulfur
loop and unlocks leaching, electrolyte, hydrofluoric-acid and yellowcake work
downstream. Every step below mirrors industrial practice and is backed by the
recipe data the game runs.

!!! abstract "Two real routes"
    **Contact Process / DCDA (built, Tier 4):** SO₂ → SO₃ over a vanadium catalyst → oleum → ~98% acid.
    The modern, high-purity route — what ~all the world's acid uses today.
    **Lead Chamber Process (built, Tier 3):** SO₂ + NOₓ + moist air in lead chambers → ~65–78% "chamber acid" → boil up.
    The historical route (Roebuck, 1746). Lower tech, lower grade — your *early* path to acid before a contact plant exists.

## Where the sulfur comes from

The acid never starts from an "acid ore" — it starts from **SO₂ gas**, which you
get two honest ways:

- **Dead-roast pyrite** — `4 FeS₂ + 11 O₂ → 2 Fe₂O₃ + 8 SO₂`. Pyrite is a common, minable sulfide. The roast drives off SO₂ **and** leaves an iron-oxide cinder that is literally the *roasted hematite the iron chain smelts* — a real cross-chain feed, not a throwaway.
- **Capture copper-smelter off-gas** — the copper roast and converter already emit `gas_so2`. Real smelters pipe that 3–13% SO₂ straight into an acid plant instead of venting it. Same item, so your copper line feeds your acid line for free.

## The chain, step by step

| # | Step · station | In → Out | Byproduct / note | Tier · time · energy |
|---|----------------|----------|------------------|----------------------|
| 0 | Gather water · — | → 4 raw water | world resource | T0 · 10s · — |
| 1 | **Dead-roast pyrite** · sulfur burner | 4 pyrite → 6 SO₂ | **+2 roasted hematite → iron chain** | T2 · 50s · 40 kJ |
| — | *(or reuse copper-smelter SO₂)* | copper line → SO₂ | loop closed | — |
| **Contact route** ||||
| 2 | **Oxidise** · contact converter (V₂O₅) | 2 SO₂ → 2 SO₃ | 450 °C, 1–2 atm, ~98% | T4 · 30s · 60 kJ |
| 3 | **Absorb to oleum** · absorption tower | 3 SO₃ + 1 water → 2 oleum | never SO₃ + water direct! | T4 · 20s · 18 kJ |
| 4 | **Dilute oleum** · absorption tower | 2 oleum + 1 water → 3 H₂SO₄ | ~98% product | T4 · 20s · 12 kJ |
| **Lead-chamber route** ||||
| 5 | **Chamber acid** · lead chamber | 3 SO₂ + 1 water → 2 dilute H₂SO₄ | NOₓ catalysed, ~78% cap | T3 · 40s · 15 kJ |
| 6 | **Concentrate** · Glover tower | 2 dilute → 1 H₂SO₄ | boil down | T3 · 35s · 25 kJ |

## The chemistry (why each step exists)

**Oxidation (the heart).** `2 SO₂ + O₂ ⇌ 2 SO₃` is reversible and strongly
exothermic (ΔH = −196 kJ/mol). Le Chatelier says low temperature favours SO₃ —
but cold kills the rate, so plants compromise at **~450 °C** over a **vanadium(V)
oxide (V₂O₅)** catalyst at just **1–2 atm** (the equilibrium already favours the
product, so high pressure isn't worth the cost). **Double-contact/double-
absorption (DCDA)** pulls the gas out, strips the SO₃, and re-passes it to reach
~98%+ conversion while keeping SO₂ stack emissions low.

**Why oleum, never water.** SO₃ + water is so violently exothermic it flashes the
product into a fine **acid mist** that refuses to condense — you lose it up the
stack. So SO₃ is absorbed into existing strong acid instead: `SO₃ + H₂SO₄ →
H₂S₂O₇` (oleum, fuming sulfuric acid). Oleum is then bled down with a *metered*
water add — `H₂S₂O₇ + H₂O → 2 H₂SO₄` — which is controllable. This oleum detour
is the single most important "gotcha" of the whole process.

**The historical route.** Before vanadium catalysts, acid came from the **lead
chamber process**: SO₂ oxidised by moist air with recycled **nitrogen oxides
(NOₓ)** as a gas-phase catalyst inside lead-lined rooms. Cheap and famously
robust, but it caps out around **65–78%** acid — fine for fertiliser and pickling,
too weak for oleum or anhydrous work. The Gay-Lussac and Glover towers recover
and recycle the NOₓ. It's the authentic Tier-3 stepping stone.

## The byproduct loop

```
copper roast/convert ─┐
                      ├─► SO₂ ──(V₂O₅)──► SO₃ ──► oleum ──► H₂SO₄ ──► leaching / HF / electrolyte / yellowcake
pyrite dead-roast  ───┘        │
                               └─► roasted hematite ──► iron chain (bloomery / blast furnace)
```

Nothing is wasted: the sulfur that copper smelting would have vented becomes acid,
and the iron in the pyrite becomes feed for the iron chain.

## Where to find these recipes

- **In-game / NEI:** search the `T3_SulfuricAcid` pack, or any of the stations — *Sulfur Burner / Pyrite Roaster*, *Contact Converter (V₂O₅ beds, DCDA)*, *Oleum Absorption Tower*, *Lead Chamber (NOₓ)*.
- **In these docs:** the [recipe index](../recipes/index.md) lists every step by id (`acid_roast_pyrite`, `acid_so2_to_so3`, `acid_form_oleum`, `acid_dilute_oleum`, `acid_lead_chamber`, `acid_concentrate_chamber`).
- **Unlocks next:** with acid in hand, the deferred **copper oxide / SX-EW route** (leach → solvent extraction → electrowinning) becomes buildable — see the [Missing-chains roadmap](../design/missing-chains.md).
