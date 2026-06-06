# Sync Report — generated guide vs your LIVE codebase

*Generated 2026-06-06. Compares the canonical data set (685 recipes / 836 items / 153 stations, 27 chains) against the uploaded live tree `Code/` (Shared/SRC ... ReplicatedStorage/Conduvia).*

## TL;DR

Your live game has the **raw-ore nodes** and the **stone-age / era packs**, but **none of the 27 processing chains** have been dropped in yet (you'd only been downloading zips). The good news: **the formats already match**, so this is a copy-in, not a rewrite.

- **Recipe format** — our `RecipeCard` rows match your `RecipeDBController` `RecipeCard` type exactly (id, categoryId, inputs, outputs, time, notes, stationIds, energy{amount,unit}, source, kind, tier).
- **Item format** — our 17-field positional `DataRow` matches your `ItemDatabase/Data/*.luau` schema exactly.
- **Station format** — our keyed `StationDef` matches your `Stations/StationDefs.luau` shape.

## What to update — A) DOCS (mkdocs field guide)

The whole `docs/` tree + `mkdocs.yml` in this guide is ahead of your live copy. Field guides now cover all 27 chains, newest = **flint.md** and **obsidian.md**. Replace your live `docs/` + `mkdocs.yml` with the ones in `Conduvia_Docs.zip`.

## What to update — B) CODE (Roblox Luau)

Copy from the **drop-in bundle** (`Conduvia_DropIn.zip`), which mirrors your tree paths:

| Drop into (your tree) | Files | Wiring needed |
|---|---|---|
| `ReplicatedStorage/Conduvia/ItemDatabase/Data/` | 27 item packs (`*_Items.luau`) | **None** — `ItemController` auto-loads every module in `Data/` via `GetChildren()`. |
| `ReplicatedStorage/Conduvia/ItemRecipes/RecipeDBController/` | 27 recipe packs (`*_Recipes.luau`) | Auto-discovered under `ItemRecipes`; recipes also auto-build from each item's `ext`. |
| `ReplicatedStorage/Conduvia/Stations/` | `Conduvia_GeneratedStations.luau` (153 defs) | **Merge** missing keys into `StationDefs.luau` — see below. Your hand-authored UI/body/hint entries win on conflict. |

### Concrete diff vs live
- **120 item ids are brand-new** (absent from your entire live tree). The other ~716 share an id token with existing content, but all 27 item *modules* are new files to add.
- **69 of 153 stations are new** (missing from `StationDefs.luau`).
- **All 27 recipe packs are new modules** (no `Conduvia_*`/`T?_*` pack id exists in live yet).

### Station merge snippet
At the top of `StationDefs.luau`, after the `Stations` table is built:
```lua
local Generated = require(script.Parent:WaitForChild("Conduvia_GeneratedStations"))
for id, def in pairs(Generated) do
    if Stations[id] == nil then       -- never clobber hand-authored UI/body/hint
        Stations[id] = def
    end
end
```

### New stations added by this drop (69)
- `absorption_tower`
- `air_separation_unit`
- `aluminothermic_crucible`
- `amine_gas_treater`
- `anode_baking_furnace`
- `aod_converter`
- `apt_crystallizer`
- `basic_oxygen_furnace`
- `bayer_digester`
- `brine_treatment_unit`
- `carbonation_reactor`
- `caustic_digester_autoclave`
- `caustic_evaporator`
- `cement_ball_mill`
- `claus_sulfur_unit`
- `contact_converter`
- `copper_converter`
- `cryo_helium_unit`
- `cupellation_hearth`
- `czochralski_crystal_puller`
- `dri_shaft_furnace`
- `electrolytic_refining_cell`
- `electrowinning_cell`
- `fire_refining_furnace`
- `flash_smelting_furnace`
- `fluidized_bed_chlorinator`
- `fluoride_digestion_reactor`
- `fluorine_cell`
- `froth_flotation_cell`
- `fuel_rod_assembly_line`
- `gas_centrifuge_cascade`
- `gas_well_derrick`
- `haber_bosch_reactor`
- `hall_heroult_cell`
- `heap_leach_pad`
- `helium_purifier`
- `hf_zr_separation_column`
- `hunter_reduction_retort`
- `hydrogen_reduction_furnace`
- `knapping_station`
- `lead_chamber`
- `li_acid_roast_kiln`
- `magnetic_separator`
- `mannheim_furnace`
- `membrane_electrolysis_cell`
- `mg_chloride_chlorinator`
- `mg_electrolysis_cell`
- `mg_flux_remelt_furnace`
- `pelletizer_disc`
- `pidgeon_retort`
- `powder_press_sinter_furnace`
- `precipitation_tank`
- `reactor_assembly_bay`
- `reagent_filling_line`
- `reverberatory_furnace`
- `rotary_calciner_kiln`
- `sheet_metal_press`
- `siemens_cvd_reactor`
- `sinter_strand`
- `steam_reformer`
- `submerged_arc_furnace`
- `sulfur_burner`
- `sx_mixer_settler`
- `ticl4_distillation_column`
- `uranium_conversion_reactor`
- `vacuum_arc_remelt_furnace`
- `wafer_fab_line`
- `yellowcake_precipitator`
- `zinc_distillation_retort`

## Icon-pipeline contract — data hygiene done this pass

- **Explicit `tier` added** to items.json (icon team prefers it over `_sourceFile` inference): now **301/836** items carry an explicit `tier`; the ~535 without are the organic/wildlife/farming branch (no producing recipe). All chain items are covered.
- **`craftStation` prose -> station id**: normalized **130** legacy rows (e.g. `"stamp mill (manual trip hammer)"` -> `stamp_mill_manual_trip_hammer`). **9** prose values still point to stations that don't exist as defs and were left as-is: fluid handler station, gas compressor, small blast furnace, drying rack, stone anvil, bessemer converter, DC dynamo (workshop), mercury-arc rectifier, vent stack. (Recommend either adding those station defs or remapping.)
- **subtype / tagsCsv**: every chain step carries a distinct subtype word (Raw Ore / Crushed Ore / Ground Ore / Calcine / Pellet / Matte / Ingot / Metal Form / Gas / Liquid ...) and material tags, so each step renders as its own icon.
- **No id renames** this pass; nothing to add to `aliases.json` for the icon side.

**Snapshot to send the icon team:** `Conduvia_Progress.zip` (carries the updated `data/items.json` with tier + craftStation fixes) or `data/items.json` directly.
