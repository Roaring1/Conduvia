# Obsidian — volcanic glass to a surgical blade

**Tier 1–3 · Branch · Pack `T1_Obsidian.luau`**

Obsidian is natural rhyolitic glass: amorphous, no crystal grain, so it fractures
along molecular-scale lines. A pressure-flaked obsidian edge is about **3 nm**
(30 Å) wide — finer than the best steel scalpels (300–600 Å) and approaching
diamond. That is why a handful of surgeons still use obsidian blades for fine,
low-scarring incisions. It started as a dead `raw_ore_obsidian`; the payoff item
is a real precision instrument, not survival filler.

## Flow

```mermaid
flowchart TD
    ore["raw_ore_obsidian"] -->|knap (hammerstone)| flake["obsidian flake"]
    ore --> deb["stone debitage (byproduct)"]
    flake -->|pressure-flake (wood billet)| blade["pressure-flaked blade"]
    flake -->|shape| arrow["obsidian dart point"]
    blade -->|haft to handle| scalpel["obsidian scalpel"]
```

## Steps

| # | Recipe | Station | In | Out |
|---|--------|---------|----|-----|
| 1 | `ob_knap_obsidian` | Knapping Station | 2 raw obsidian | 3 flake + 1 stone debitage |
| 2 | `ob_pressure_blade` | Knapping Station | 2 flake + 1 wood | 1 pressure-flaked blade |
| 3 | `ob_make_arrowhead` | Knapping Station | 1 flake | 2 dart point |
| 4 | `ob_make_scalpel` | Carving Bench | 1 blade + 1 wood | 1 obsidian scalpel |

## Why it's built this way

- **Amorphous glass = the sharpest edge in the game.** Because obsidian has no
  grain it shears along molecular lines; straight off the hammerstone a flake is
  already keener than knapped flint.
- **Pressure flaking refines the edge.** Pressing tiny chips off with a wood or
  antler billet takes the edge down to ~3 nm. The billet is consumed.
- **The scalpel is the real-world payoff.** Hafted to a carved handle, the micro-
  blade parts tissue *between* cells rather than tearing them, giving
  exceptionally clean, low-inflammation cuts — a genuine precision instrument and
  a high-tier sink for an otherwise primitive ore.
- **Brittle, brilliant trade-off.** Obsidian is sharper than steel but shatters
  on impact — fine cutting, not chopping.

## Byproducts & sinks

- **stone debitage** (`stone_flakes`) — shared knapping byproduct with flint.
- **dart point** (`obsidian_arrowhead`) — hunting/ceremony projectile.
- **obsidian scalpel** (`obsidian_scalpel`) — precision/surgical instrument; the
  chain's terminal high-value product.

---

*Verified 2026-06-05 against CNN/NCBI on obsidian scalpel edge geometry (~30 Å
vs 300–600 Å for steel), the PubMed obsidian-vs-steel wound-healing study, Fine
Science Tools' wood-handled obsidian scalpel product, and Wikipedia (Obsidian,
Pressure flaking, Knapping).*
