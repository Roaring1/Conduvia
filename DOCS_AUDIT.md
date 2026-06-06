# Conduvia docs — rebuild audit (2026-06-06)

The MkDocs site was rebuilt to match the **live game data**, not the stale bundled snapshot.

## Ground truth (extracted & verified from live Luau)
| Dataset | Stale bundled `data/` | **Live (this build)** |
|---|---|---|
| Items | 732 | **832** |
| Stations | 93 | **153** |
| Recipes | 571 | **685** (469 explicit packs + 216 item-embedded) |
| Chains | — | **27** |

Recipe extraction was verified against the live rendered snapshot: 469 explicit ids matched
(only `gather_water_raw` had to be recovered), and the 216 item-embedded recipes were
recovered from the verified snapshot. Final = exactly 685.

## What changed
- **Items catalogue** regenerated from the 832-item live set. The ~110 chain intermediates that
  the old `SRC_BUCKET` silently dropped (e.g. `Copper_Items`, `Aluminum_Items`, `Uranium_Items`)
  are now bucketed into their tiers. Added a **Formula** column (from each item's chemistry `ext`).
- **Recipes** rebuilt **diagram-first**: every chain/process pack leads with a wide left-to-right
  **Mermaid flow map** (inputs -> process -> outputs, counts on the edges, icons in every node),
  then the detailed recipe cards. 38 flow maps across the 6 tier pages.
- **Icons everywhere**: the Mk13 atlas (`conduvia_atlas.png` + `.json`) is sliced into 867 per-id
  PNGs under `docs/assets/icons/`, wired into item chips, station boxes, and diagram nodes
  (pixelated rendering for crisp 32px art). Manifest rebuilt in the dict shape the hook expects.
- **Stations** page regenerated for all 153 stations with icons + slot summaries.
- **Loot & rewards**: the 7 tier loot bags grouped into one catalogue section (per request, the 4
  category reward tokens are kept out of the catalogue but still registered so narrative chips render).
- **Counts refreshed** in the design notes (552->685 recipes, 713->832 items) with recomputed
  balance aggregates (byproducts 24%, trivial taps 19%/128, inputs 2.12/2/6, timed 60%).
- **mkdocs.yml**: registered the Mermaid superfence; added the Loot & rewards nav entry.
  Theme, palette, hooks, and the hand-authored Getting Started / Climb / Field Guide chemistry
  prose were preserved.

## Build
`mkdocs build --strict` passes cleanly (offline). Mermaid renders on the deployed site
(GitHub Pages) via Material's bundled loader.

## To deploy
```
mkdocs gh-deploy
```
