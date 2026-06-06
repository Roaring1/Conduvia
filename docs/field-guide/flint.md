# Flint — knapping, fire-steel & potters' flint

**Tier 1–2 · Branch · Pack `T1_Flint.luau`**

Flint is cryptocrystalline quartz (chert). It breaks by *conchoidal fracture* —
a sharp blow shears off a razor flake — so it was the first tool stone there is.
It started as a dead `raw_ore_flint` with nothing downstream. Two honest non-
survival tie-ins keep the chain from being mere fluff: a **flint-and-steel fire
striker** (which reaches back into the steel chain) and **calcined potters'
flint**, a real ceramic-body silica.

## Flow

```mermaid
flowchart TD
    ore["raw_ore_flint"] -->|knap (hammerstone)| flake["flint flake"]
    ore --> deb["stone debitage (byproduct)"]
    flake -->|retouch| blade["knapped flint blade"]
    flake -->|shape| arrow["flint arrowhead"]
    ore -->|+ steel, struck| fs["flint-and-steel striker"]
    steel["steel_ingot"] --> fs
    ore -->|calcine ~600C + grind| silica["calcined potters' flint"]
```

## Steps

| # | Recipe | Station | In | Out |
|---|--------|---------|----|-----|
| 1 | `fl_knap_flint` | Knapping Station | 2 raw flint | 3 flake + 1 stone debitage |
| 2 | `fl_knap_blade` | Knapping Station | 2 flake | 1 knapped blade |
| 3 | `fl_make_arrowhead` | Knapping Station | 1 flake | 2 arrowhead |
| 4 | `fl_fire_steel` | Workbench | 1 flint + 1 steel ingot | 2 fire-steel striker |
| 5 | `fl_calcine_silica` | Rotary Calciner Kiln | 2 flint | 2 calcined potters' flint |

## Why it's built this way

- **Conchoidal fracture is the mechanic.** Striking a flint core with a
  hammerstone shears off sharp flakes; the blunt shatter and trimming chips fall
  away as **stone debitage** — recovered as temper/abrasive grit, so the
  previously producer-less `stone_flakes` item finally has an honest source.
- **Flakes fork into tools.** A flake retouched down one edge becomes a durable
  knife/scraper blade; bifacially worked, it becomes a barbed projectile point.
- **Flint-and-steel is real chemistry, not magic.** The flint edge is harder
  than steel, so a hard scrape shaves off tiny white-hot iron particles — the
  sparks — which catch in char tinder. It ties the most primitive ore directly
  to the steel chain.
- **Calcined potters' flint is a genuine industrial use.** Flint calcined near
  600 °C turns friable and grinds to a fine silica powder that partly inverts to
  cristobalite. Added to clay bodies and glazes it stiffens the body and puts the
  cooled glaze film under compression, suppressing crazing.

## Byproducts & sinks

- **stone debitage** (`stone_flakes`) — temper, abrasive grit, kiln filler.
- **calcined potters' flint** (`flint_calcined_silica`) — feeds ceramic/glaze
  bodies; a clean silica source parallel to `raw_ore_silica`.
- **fire-steel striker** — survival/utility tool; consumes a steel ingot.

---

*Verified 2026-06-05 against Digitalfire (Flint), the Cambridge Mineralogical
Magazine note on raw vs calcined flint, and Wikipedia (Fire striker, Knapping,
Flint). Calcination temperature, cristobalite inversion, and the flint-harder-
than-steel spark mechanism are all confirmed.*
