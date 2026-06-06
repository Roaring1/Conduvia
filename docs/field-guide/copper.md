# Copper — full processing chain

Copper is the first metal in Conduvia to get the **deep treatment**: real flotation
chemistry, a partial roast, matte smelting, converting, two refining grades, and a
fan-out into metal forms. Every step below mirrors industrial practice and is
backed by the recipe data the game actually runs.

!!! abstract "Two real routes"
    **Sulfide route (built):** chalcopyrite → concentrate → matte → blister → refined copper.
    This is ~80% of world production and the one you climb in-game today.
    **Oxide route (SX-EW, planned):** leach → solvent extraction → electrowinning.
    It needs a sulfuric-acid chain first — see the [Missing-chains roadmap](../design/missing-chains.md).

## The sulfide chain, step by step

| # | Step · station | In → Out | Byproduct | Tier · time · energy |
|---|----------------|----------|-----------|----------------------|
| 1 | Crush · stamp mill | 6 chalcopyrite → 5 crushed | stone dust | T1 · 45s · — |
| 2 | Grind · stamp mill | 5 crushed → 4 ground | stone dust | T1 · 60s · — |
| 3 | **Froth flotation** · flotation cell | 4 ground → 3 concentrate | tailings | T1 · 120s · 25 kJ |
| 4 | **Partial roast** · roasting pit | 3 concentrate → 2 calcine | SO₂ gas | T1 · 180s · 30 kJ |
| 5 | **Matte smelt** (+silica) · reverb furnace | 2 calcine + silica + charcoal → 1 matte | fayalite slag ×2 | T2 · 240s · 140 kJ |
| 6 | **Convert** · Peirce-Smith converter | 2 matte + silica → 1 blister | SO₂ + slag | T2 · 200s · 110 kJ |
| 7a | **Fire refine** (poling) · anode furnace | 2 blister + charcoal → 2 tough-pitch ingot | refining slag | T2 · 150s · 90 kJ |
| 7b | Cast anode → **electrorefine** · tankhouse | anode → 99.99% cathode | anode slime (Au/Ag/Se/Te) | T4 · 600s · 850 kJ |
| 8 | Forms · rolling mill / mill | ingot → plate → foil; ingot → rod, dust; refined → wire | — | T1–T3 |

## The chemistry (why each step exists)

**Flotation.** Ground ore is conditioned with **lime** (depresses pyrite, pH ≈ 9–12),
a **xanthate** collector, and a **pine-oil/MIBC** frother. Copper sulfide floats on
the froth; silicate gangue sinks as tailings.

**Partial roast.** Burns off part of the sulfur and starts oxidizing iron:

$$2\,CuFeS_2 + O_2 \rightarrow Cu_2S + 2\,FeS + SO_2$$

**Matte smelt** with silica flux. Iron leaves as iron-silicate (fayalite) slag;
copper and sulfur collect as a molten matte (Cu₂S·FeS, ~45–60% Cu):

$$2\,CuFeS_2 + 2\,SiO_2 + 4\,O_2 \rightarrow Cu_2S + 2\,FeSiO_3 + 3\,SO_2$$

**Convert** (Peirce-Smith, two blows). Slag blow burns the remaining iron sulfide,
then the copper blow finishes to blister copper (~98–99.5%):

$$2\,FeS + 3\,O_2 \rightarrow 2\,FeO + 2\,SO_2 \qquad Cu_2S + O_2 \rightarrow 2\,Cu + SO_2$$

**Fire refine.** Oxidize off residual S/Fe/Pb/Zn, then **pole** with green wood or
charcoal to reduce the Cu₂O back to metal — tough-pitch copper (~99%).

**Electrorefine.** Cast anodes dissolve in CuSO₄/H₂SO₄; pure copper plates the
cathode at 99.99%, while gold, silver, selenium, and tellurium drop as anode slime.

!!! tip "Byproduct loop"
    The **SO₂** from roasting and converting is not waste — it is the feedstock for
    the **Contact Process** that makes sulfuric acid. Build that chain and copper's
    off-gas becomes the acid that unlocks the oxide (SX-EW) route.

## Where to find these recipes

The crush/grind/float/roast/smelt steps live under
**Recipes → Tier 1 (Stone & materials)** and **Tier 2 (Metal Ages)**; electrorefining
sits in **Tier 5 (Electric & chemistry)**. Every copper item links back to the
recipe that makes it from the **Items & Ores → Tier 2 — Metal Ages** catalogue.
