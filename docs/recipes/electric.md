# Tier 5 — Electric & Chemistry

<p class="chapter-stats">83 recipes</p>

## Aluminum chain
<p class="chapter-stats">6 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_bauxite["<img src='/Conduvia/assets/icons/raw_ore_bauxite.png' class='mmd-ico' />raw bauxite ore"]
  i_crushed_ore_bauxite["<img src='/Conduvia/assets/icons/crushed_ore_bauxite.png' class='mmd-ico' />crushed bauxite"]
  i_stone_dust["<img src='/Conduvia/assets/icons/stone_dust.png' class='mmd-ico' />stone dust"]
  i_sodium_hydroxide["<img src='/Conduvia/assets/icons/sodium_hydroxide.png' class='mmd-ico' />sodium hydroxide"]
  i_liquor_sodium_aluminate["<img src='/Conduvia/assets/icons/liquor_sodium_aluminate.png' class='mmd-ico' />sodium aluminate liquor"]
  i_waste_red_mud["<img src='/Conduvia/assets/icons/waste_red_mud.png' class='mmd-ico' />red mud"]
  i_hydrate_gibbsite["<img src='/Conduvia/assets/icons/hydrate_gibbsite.png' class='mmd-ico' />aluminum hydroxide (gibbsite)"]
  i_intermediate_alumina["<img src='/Conduvia/assets/icons/intermediate_alumina.png' class='mmd-ico' />alumina"]
  i_coke_fuel["<img src='/Conduvia/assets/icons/coke_fuel.png' class='mmd-ico' />coke fuel"]
  i_anode_carbon["<img src='/Conduvia/assets/icons/anode_carbon.png' class='mmd-ico' />prebaked carbon anode"]
  i_cryolite["<img src='/Conduvia/assets/icons/cryolite.png' class='mmd-ico' />cryolite"]
  i_metal_aluminum_ingot["<img src='/Conduvia/assets/icons/metal_aluminum_ingot.png' class='mmd-ico' />aluminum ingot"]
  i_gas_co2["<img src='/Conduvia/assets/icons/gas_co2.png' class='mmd-ico' />carbon dioxide gas"]
  p_al_crush_bauxite{"Trip Hammer"}
  p_al_digest_bauxite{"Bayer Digestion Autoclave"}
  p_al_precipitate_gibbsite{"Gibbsite Precipitation Tank"}
  p_al_calcine_alumina{"Rotary Calcining Kiln (RKEF dry/reduce)"}
  p_al_bake_anode{"Prebake Anode Furnace"}
  p_al_hall_heroult_smelt{"Hall-Heroult Reduction Cell (Pot)"}
  i_raw_ore_bauxite --> |"x2"| p_al_crush_bauxite
  p_al_crush_bauxite --> |"x2"| i_crushed_ore_bauxite
  p_al_crush_bauxite --> |"x1"| i_stone_dust
  i_crushed_ore_bauxite --> |"x3"| p_al_digest_bauxite
  i_sodium_hydroxide --> |"x2"| p_al_digest_bauxite
  p_al_digest_bauxite --> |"x3"| i_liquor_sodium_aluminate
  p_al_digest_bauxite --> |"x2"| i_waste_red_mud
  i_liquor_sodium_aluminate --> |"x3"| p_al_precipitate_gibbsite
  p_al_precipitate_gibbsite --> |"x2"| i_hydrate_gibbsite
  p_al_precipitate_gibbsite --> |"x1"| i_sodium_hydroxide
  i_hydrate_gibbsite --> |"x3"| p_al_calcine_alumina
  p_al_calcine_alumina --> |"x2"| i_intermediate_alumina
  i_coke_fuel --> |"x2"| p_al_bake_anode
  p_al_bake_anode --> |"x1"| i_anode_carbon
  i_intermediate_alumina --> |"x2"| p_al_hall_heroult_smelt
  i_anode_carbon --> |"x1"| p_al_hall_heroult_smelt
  i_cryolite --> |"x1"| p_al_hall_heroult_smelt
  p_al_hall_heroult_smelt --> |"x2"| i_metal_aluminum_ingot
  p_al_hall_heroult_smelt --> |"x2"| i_gas_co2
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_al_crush_bauxite proc;
  class p_al_digest_bauxite proc;
  class p_al_precipitate_gibbsite proc;
  class p_al_calcine_alumina proc;
  class p_al_bake_anode proc;
  class p_al_hall_heroult_smelt proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-forming" markdown>
<div class="rc-out">:ci[anode_carbon|1]</div>
<div class="rc-flow">:ci[coke_fuel|2] <span class="rc-arrow">→</span> :ci[anode_carbon|1]</div>
<div class="rc-meta"><span class="rc-stn">Prebake Anode Furnace</span> <span class="rc-time">75s</span> <span class="rc-tier">T3</span> <span class="rc-energy">90 kJ</span></div>
<div class="rc-note">Bind petroleum coke with pitch and bake it into a dense, conductive block. These prebaked anodes are fed into the pots and slowly eaten as the cell runs.</div>
<div class="rc-id"><code>al_bake_anode</code></div>
</div>
<div class="recipe-card cat-crushing" markdown>
<div class="rc-out">:ci[crushed_ore_bauxite|2] :ci[stone_dust|1]</div>
<div class="rc-flow">:ci[raw_ore_bauxite|2] <span class="rc-arrow">→</span> :ci[crushed_ore_bauxite|2] :ci[stone_dust|1]</div>
<div class="rc-meta"><span class="rc-stn">Trip Hammer</span> <span class="rc-time">30s</span> <span class="rc-tier">T2</span> <span class="rc-energy">16 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Mill the bauxite fine so hot caustic can reach every grain. No flotation here -- bauxite is refined chemically, not concentrated mechanically.</div>
<div class="rc-id"><code>al_crush_bauxite</code></div>
</div>
<div class="recipe-card cat-precipitation" markdown>
<div class="rc-out">:ci[hydrate_gibbsite|2] :ci[sodium_hydroxide|1]</div>
<div class="rc-flow">:ci[liquor_sodium_aluminate|3] <span class="rc-arrow">→</span> :ci[hydrate_gibbsite|2] :ci[sodium_hydroxide|1]</div>
<div class="rc-meta"><span class="rc-stn">Gibbsite Precipitation Tank</span> <span class="rc-time">180s</span> <span class="rc-tier">T3</span> <span class="rc-energy">35 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Cool the supersaturated liquor and seed it with fine gibbsite. Over hours, Al(OH)3 crystallises out: NaAlO2 + 2 H2O -> Al(OH)3 + NaOH. The freed caustic soda is pumped back to digestion -- the Bayer circuit recycles its own lye.</div>
<div class="rc-id"><code>al_precipitate_gibbsite</code></div>
</div>
<div class="recipe-card cat-calcining" markdown>
<div class="rc-out">:ci[intermediate_alumina|2]</div>
<div class="rc-flow">:ci[hydrate_gibbsite|3] <span class="rc-arrow">→</span> :ci[intermediate_alumina|2]</div>
<div class="rc-meta"><span class="rc-stn">Rotary Calcining Kiln (RKEF dry/reduce)</span> <span class="rc-time">90s</span> <span class="rc-tier">T3</span> <span class="rc-energy">120 kJ</span></div>
<div class="rc-note">Fire the gibbsite white-hot in the rotary kiln to drive off its chemical water: 2 Al(OH)3 -> Al2O3 + 3 H2O. Out comes smelter-grade alumina, a free-flowing white sand.</div>
<div class="rc-id"><code>al_calcine_alumina</code></div>
</div>
<div class="recipe-card cat-leaching" markdown>
<div class="rc-out">:ci[liquor_sodium_aluminate|3] :ci[waste_red_mud|2]</div>
<div class="rc-flow">:ci[crushed_ore_bauxite|3] :ci[sodium_hydroxide|2] <span class="rc-arrow">→</span> :ci[liquor_sodium_aluminate|3] :ci[waste_red_mud|2]</div>
<div class="rc-meta"><span class="rc-stn">Bayer Digestion Autoclave</span> <span class="rc-time">120s</span> <span class="rc-tier">T3</span> <span class="rc-energy">140 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Cook the bauxite in hot, pressurised caustic soda. The alumina dissolves as sodium aluminate while iron oxide, silica and titania refuse to and settle out as red mud: ~1-1.5 t of red mud per t of alumina, the industry's great unsolved waste stream. Decant the clear liquor off the mud.</div>
<div class="rc-id"><code>al_digest_bauxite</code></div>
</div>
<div class="recipe-card cat-electrolysis" markdown>
<div class="rc-out">:ci[metal_aluminum_ingot|2] :ci[gas_co2|2]</div>
<div class="rc-flow">:ci[intermediate_alumina|2] :ci[anode_carbon|1] :ci[cryolite|1] <span class="rc-arrow">→</span> :ci[metal_aluminum_ingot|2] :ci[gas_co2|2]</div>
<div class="rc-meta"><span class="rc-stn">Hall-Heroult Reduction Cell (Pot)</span> <span class="rc-time">200s</span> <span class="rc-tier">T4</span> <span class="rc-energy">600 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Dissolve the alumina in a molten cryolite bath (~960 C) and drive a brutal DC current through it. Oxygen migrates to the carbon anode and burns it away while pure aluminum pools at the cathode: 2 Al2O3 + 3 C -> 4 Al + 3 CO2. At ~17,000 kWh per tonne this is the most energy-hungry single step in the whole tech tree -- aluminum is, quite literally, solid electricity.</div>
<div class="rc-id"><code>al_hall_heroult_smelt</code></div>
</div>
</div>

## Cells chain
<p class="chapter-stats">6 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_stainless_steel_sheet["<img src='/Conduvia/assets/icons/stainless_steel_sheet.png' class='mmd-ico' />stainless steel sheet"]
  i_cell_metal["<img src='/Conduvia/assets/icons/cell_metal.png' class='mmd-ico' />metal cell"]
  i_glass_tube["<img src='/Conduvia/assets/icons/glass_tube.png' class='mmd-ico' />borosilicate glass tube"]
  i_cell_glass["<img src='/Conduvia/assets/icons/cell_glass.png' class='mmd-ico' />glass cell"]
  i_water_raw["<img src='/Conduvia/assets/icons/water_raw.png' class='mmd-ico' />raw water"]
  i_cell_metal_water_raw["<img src='/Conduvia/assets/icons/cell_metal_water_raw.png' class='mmd-ico' />metal cell (water)"]
  i_acid_sulfuric["<img src='/Conduvia/assets/icons/acid_sulfuric.png' class='mmd-ico' />sulfuric acid"]
  i_cell_metal_acid_sulfuric["<img src='/Conduvia/assets/icons/cell_metal_acid_sulfuric.png' class='mmd-ico' />metal cell (sulfuric acid)"]
  i_sodium_hydroxide["<img src='/Conduvia/assets/icons/sodium_hydroxide.png' class='mmd-ico' />sodium hydroxide"]
  i_cell_metal_sodium_hydroxide["<img src='/Conduvia/assets/icons/cell_metal_sodium_hydroxide.png' class='mmd-ico' />metal cell (sodium hydroxide)"]
  i_cell_glass_water_raw["<img src='/Conduvia/assets/icons/cell_glass_water_raw.png' class='mmd-ico' />glass cell (water)"]
  p_cell_form_metal{"Sheet-Metal Forming & Seaming Press"}
  p_cell_form_glass{"Glass Bench"}
  p_cell_fill_metal_water{"Reagent Filling & Sealing Line"}
  p_cell_fill_metal_acid{"Reagent Filling & Sealing Line"}
  p_cell_fill_metal_caustic{"Reagent Filling & Sealing Line"}
  p_cell_fill_glass_water{"Reagent Filling & Sealing Line"}
  i_stainless_steel_sheet --> |"x2"| p_cell_form_metal
  p_cell_form_metal --> |"x2"| i_cell_metal
  i_glass_tube --> |"x2"| p_cell_form_glass
  p_cell_form_glass --> |"x2"| i_cell_glass
  i_cell_metal --> |"x1"| p_cell_fill_metal_water
  i_water_raw --> |"x1"| p_cell_fill_metal_water
  p_cell_fill_metal_water --> |"x1"| i_cell_metal_water_raw
  i_cell_metal --> |"x1"| p_cell_fill_metal_acid
  i_acid_sulfuric --> |"x1"| p_cell_fill_metal_acid
  p_cell_fill_metal_acid --> |"x1"| i_cell_metal_acid_sulfuric
  i_cell_metal --> |"x1"| p_cell_fill_metal_caustic
  i_sodium_hydroxide --> |"x1"| p_cell_fill_metal_caustic
  p_cell_fill_metal_caustic --> |"x1"| i_cell_metal_sodium_hydroxide
  i_cell_glass --> |"x1"| p_cell_fill_glass_water
  i_water_raw --> |"x1"| p_cell_fill_glass_water
  p_cell_fill_glass_water --> |"x1"| i_cell_glass_water_raw
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_cell_form_metal proc;
  class p_cell_form_glass proc;
  class p_cell_fill_metal_water proc;
  class p_cell_fill_metal_acid proc;
  class p_cell_fill_metal_caustic proc;
  class p_cell_fill_glass_water proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-glassworking" markdown>
<div class="rc-out">:ci[cell_glass|2]</div>
<div class="rc-flow">:ci[glass_tube|2] <span class="rc-arrow">→</span> :ci[cell_glass|2]</div>
<div class="rc-meta"><span class="rc-stn">Glass Bench</span> <span class="rc-time">45s</span> <span class="rc-tier">T3</span> <span class="rc-energy">60 kJ</span></div>
<div class="rc-note">Blow and seal borosilicate tube into a glass cell -- inert to acids and thermal shock, for corrosive contents you want to see.</div>
<div class="rc-id"><code>cell_form_glass</code></div>
</div>
<div class="recipe-card cat-filling" markdown>
<div class="rc-out">:ci[cell_glass_water_raw|1]</div>
<div class="rc-flow">:ci[cell_glass|1] :ci[water_raw|1] <span class="rc-arrow">→</span> :ci[cell_glass_water_raw|1]</div>
<div class="rc-meta"><span class="rc-stn">Reagent Filling & Sealing Line</span> <span class="rc-time">20s</span> <span class="rc-tier">T3</span> <span class="rc-energy">15 kJ</span></div>
<div class="rc-note">Charge a borosilicate cell with raw water and seal -- a clear, inert canister.</div>
<div class="rc-id"><code>cell_fill_glass_water</code></div>
</div>
<div class="recipe-card cat-metal-forming" markdown>
<div class="rc-out">:ci[cell_metal|2]</div>
<div class="rc-flow">:ci[stainless_steel_sheet|2] <span class="rc-arrow">→</span> :ci[cell_metal|2]</div>
<div class="rc-meta"><span class="rc-stn">Sheet-Metal Forming & Seaming Press</span> <span class="rc-time">60s</span> <span class="rc-tier">T4</span> <span class="rc-energy">90 kJ</span></div>
<div class="rc-note">Deep-draw and seam-weld stainless sheet into an empty cell body. Stainless, not plain steel or aluminium, because this one container has to survive both acid and caustic fills.</div>
<div class="rc-id"><code>cell_form_metal</code></div>
</div>
<div class="recipe-card cat-filling" markdown>
<div class="rc-out">:ci[cell_metal_acid_sulfuric|1]</div>
<div class="rc-flow">:ci[cell_metal|1] :ci[acid_sulfuric|1] <span class="rc-arrow">→</span> :ci[cell_metal_acid_sulfuric|1]</div>
<div class="rc-meta"><span class="rc-stn">Reagent Filling & Sealing Line</span> <span class="rc-time">25s</span> <span class="rc-tier">T4</span> <span class="rc-energy">20 kJ</span></div>
<div class="rc-note">Charge a stainless cell with sulfuric acid. The stainless body earns its cost here -- acid would eat an ordinary can.</div>
<div class="rc-id"><code>cell_fill_metal_acid</code></div>
</div>
<div class="recipe-card cat-filling" markdown>
<div class="rc-out">:ci[cell_metal_sodium_hydroxide|1]</div>
<div class="rc-flow">:ci[cell_metal|1] :ci[sodium_hydroxide|1] <span class="rc-arrow">→</span> :ci[cell_metal_sodium_hydroxide|1]</div>
<div class="rc-meta"><span class="rc-stn">Reagent Filling & Sealing Line</span> <span class="rc-time">25s</span> <span class="rc-tier">T4</span> <span class="rc-energy">20 kJ</span></div>
<div class="rc-note">Charge a stainless cell with sodium hydroxide. Caustic in aluminium would dissolve the can and vent hydrogen; stainless holds it safely.</div>
<div class="rc-id"><code>cell_fill_metal_caustic</code></div>
</div>
<div class="recipe-card cat-filling" markdown>
<div class="rc-out">:ci[cell_metal_water_raw|1]</div>
<div class="rc-flow">:ci[cell_metal|1] :ci[water_raw|1] <span class="rc-arrow">→</span> :ci[cell_metal_water_raw|1]</div>
<div class="rc-meta"><span class="rc-stn">Reagent Filling & Sealing Line</span> <span class="rc-time">20s</span> <span class="rc-tier">T4</span> <span class="rc-energy">15 kJ</span></div>
<div class="rc-note">Charge a stainless cell with raw water and seal it -- the neutral reference fill.</div>
<div class="rc-id"><code>cell_fill_metal_water</code></div>
</div>
</div>

## Chloralkali chain
<p class="chapter-stats">4 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_halite["<img src='/Conduvia/assets/icons/raw_ore_halite.png' class='mmd-ico' />raw halite ore"]
  i_water_raw["<img src='/Conduvia/assets/icons/water_raw.png' class='mmd-ico' />raw water"]
  i_brine_solution["<img src='/Conduvia/assets/icons/brine_solution.png' class='mmd-ico' />brine solution"]
  i_brine_purified["<img src='/Conduvia/assets/icons/brine_purified.png' class='mmd-ico' />purified brine"]
  i_waste_tailings["<img src='/Conduvia/assets/icons/waste_tailings.png' class='mmd-ico' />tailings"]
  i_gas_chlorine["<img src='/Conduvia/assets/icons/gas_chlorine.png' class='mmd-ico' />chlorine gas"]
  i_caustic_dilute["<img src='/Conduvia/assets/icons/caustic_dilute.png' class='mmd-ico' />dilute cell caustic"]
  i_gas_hydrogen["<img src='/Conduvia/assets/icons/gas_hydrogen.png' class='mmd-ico' />hydrogen gas"]
  i_sodium_hydroxide["<img src='/Conduvia/assets/icons/sodium_hydroxide.png' class='mmd-ico' />sodium hydroxide"]
  p_ca_dissolve_brine{"Brine Saturation & Softening Unit"}
  p_ca_purify_brine{"Brine Saturation & Softening Unit"}
  p_ca_membrane_cell{"Chlor-Alkali Membrane Cell"}
  p_ca_concentrate_caustic{"Caustic Concentration Evaporator"}
  i_raw_ore_halite --> |"x2"| p_ca_dissolve_brine
  i_water_raw --> |"x1"| p_ca_dissolve_brine
  p_ca_dissolve_brine --> |"x2"| i_brine_solution
  i_brine_solution --> |"x2"| p_ca_purify_brine
  p_ca_purify_brine --> |"x2"| i_brine_purified
  p_ca_purify_brine --> |"x1"| i_waste_tailings
  i_brine_purified --> |"x2"| p_ca_membrane_cell
  p_ca_membrane_cell --> |"x1"| i_gas_chlorine
  p_ca_membrane_cell --> |"x2"| i_caustic_dilute
  p_ca_membrane_cell --> |"x1"| i_gas_hydrogen
  i_caustic_dilute --> |"x2"| p_ca_concentrate_caustic
  p_ca_concentrate_caustic --> |"x1"| i_sodium_hydroxide
  p_ca_concentrate_caustic --> |"x1"| i_water_raw
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_ca_dissolve_brine proc;
  class p_ca_purify_brine proc;
  class p_ca_membrane_cell proc;
  class p_ca_concentrate_caustic proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-refining" markdown>
<div class="rc-out">:ci[brine_purified|2] :ci[waste_tailings|1]</div>
<div class="rc-flow">:ci[brine_solution|2] <span class="rc-arrow">→</span> :ci[brine_purified|2] :ci[waste_tailings|1]</div>
<div class="rc-meta"><span class="rc-stn">Brine Saturation & Softening Unit</span> <span class="rc-time">45s</span> <span class="rc-tier">T3</span> <span class="rc-energy">40 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Pass the brine through ion-exchange softening to strip calcium and magnesium to ppb levels. Skip this and the cell membrane fouls within days -- brine purity is the hidden discipline of a chlor-alkali plant.</div>
<div class="rc-id"><code>ca_purify_brine</code></div>
</div>
<div class="recipe-card cat-mixing" markdown>
<div class="rc-out">:ci[brine_solution|2]</div>
<div class="rc-flow">:ci[raw_ore_halite|2] :ci[water_raw|1] <span class="rc-arrow">→</span> :ci[brine_solution|2]</div>
<div class="rc-meta"><span class="rc-stn">Brine Saturation & Softening Unit</span> <span class="rc-time">30s</span> <span class="rc-tier">T2</span> <span class="rc-energy">20 kJ</span></div>
<div class="rc-note">Dissolve rock salt in water to a saturated brine -- the raw feedstock for the whole plant. Salt is cheap and the sea is endless; the cost here is all electricity downstream.</div>
<div class="rc-id"><code>ca_dissolve_brine</code></div>
</div>
<div class="recipe-card cat-electrolysis" markdown>
<div class="rc-out">:ci[gas_chlorine|1] :ci[caustic_dilute|2] :ci[gas_hydrogen|1]</div>
<div class="rc-flow">:ci[brine_purified|2] <span class="rc-arrow">→</span> :ci[gas_chlorine|1] :ci[caustic_dilute|2] :ci[gas_hydrogen|1]</div>
<div class="rc-meta"><span class="rc-stn">Chlor-Alkali Membrane Cell</span> <span class="rc-time">120s</span> <span class="rc-tier">T3</span> <span class="rc-energy">350 kJ</span> <span class="rc-bp">+2 byproducts</span></div>
<div class="rc-note">Electrolyse the purified brine across an ion-selective membrane: chlorine bubbles off the anode, hydrogen off the cathode, and sodium ions cross the membrane to leave caustic soda behind. 2 NaCl + 2 H2O -> Cl2 + H2 + 2 NaOH. The single biggest electricity draw outside the aluminium pots.</div>
<div class="rc-id"><code>ca_membrane_cell</code></div>
</div>
<div class="recipe-card cat-evaporation" markdown>
<div class="rc-out">:ci[sodium_hydroxide|1] :ci[water_raw|1]</div>
<div class="rc-flow">:ci[caustic_dilute|2] <span class="rc-arrow">→</span> :ci[sodium_hydroxide|1] :ci[water_raw|1]</div>
<div class="rc-meta"><span class="rc-stn">Caustic Concentration Evaporator</span> <span class="rc-time">60s</span> <span class="rc-tier">T3</span> <span class="rc-energy">110 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Boil the weak cell liquor down to ~50% caustic soda, recovering the water. Evaporation is energy-hungry in its own right, which is why caustic is sold by the tonne, not the litre.</div>
<div class="rc-id"><code>ca_concentrate_caustic</code></div>
</div>
</div>

## Cobalt chain
<p class="chapter-stats">4 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_cobaltite["<img src='/Conduvia/assets/icons/raw_ore_cobaltite.png' class='mmd-ico' />raw cobaltite ore"]
  i_gas_oxygen["<img src='/Conduvia/assets/icons/gas_oxygen.png' class='mmd-ico' />oxygen gas"]
  i_cobalt_oxide_roasted["<img src='/Conduvia/assets/icons/cobalt_oxide_roasted.png' class='mmd-ico' />roasted cobalt oxide"]
  i_gas_so2["<img src='/Conduvia/assets/icons/gas_so2.png' class='mmd-ico' />sulfur dioxide gas"]
  i_arsenic_trioxide["<img src='/Conduvia/assets/icons/arsenic_trioxide.png' class='mmd-ico' />arsenic trioxide (toxic)"]
  i_acid_sulfuric["<img src='/Conduvia/assets/icons/acid_sulfuric.png' class='mmd-ico' />sulfuric acid"]
  i_cobalt_sulfate_solution["<img src='/Conduvia/assets/icons/cobalt_sulfate_solution.png' class='mmd-ico' />cobalt sulfate liquor"]
  i_waste_tailings["<img src='/Conduvia/assets/icons/waste_tailings.png' class='mmd-ico' />tailings"]
  i_cobalt_purified_solution["<img src='/Conduvia/assets/icons/cobalt_purified_solution.png' class='mmd-ico' />purified cobalt solution"]
  i_nickel_concentrate["<img src='/Conduvia/assets/icons/nickel_concentrate.png' class='mmd-ico' />nickel concentrate"]
  i_dc_charge["<img src='/Conduvia/assets/icons/dc_charge.png' class='mmd-ico' />DC power charge"]
  i_cobalt_cathode["<img src='/Conduvia/assets/icons/cobalt_cathode.png' class='mmd-ico' />cobalt cathode"]
  i_slag["<img src='/Conduvia/assets/icons/slag.png' class='mmd-ico' />slag"]
  p_co_roast_cobaltite{"Roasting Pit"}
  p_co_leach{"Heap Leach Pad (acid irrigation)"}
  p_co_solvent_extract{"Solvent-Extraction Mixer-Settler (LIX)"}
  p_co_electrowin{"Electrowinning Cell (Pb anode / SS cathode)"}
  i_raw_ore_cobaltite --> |"x2"| p_co_roast_cobaltite
  i_gas_oxygen --> |"x1"| p_co_roast_cobaltite
  p_co_roast_cobaltite --> |"x1"| i_cobalt_oxide_roasted
  p_co_roast_cobaltite --> |"x1"| i_gas_so2
  p_co_roast_cobaltite --> |"x1"| i_arsenic_trioxide
  i_cobalt_oxide_roasted --> |"x2"| p_co_leach
  i_acid_sulfuric --> |"x2"| p_co_leach
  p_co_leach --> |"x2"| i_cobalt_sulfate_solution
  p_co_leach --> |"x1"| i_waste_tailings
  i_cobalt_sulfate_solution --> |"x2"| p_co_solvent_extract
  p_co_solvent_extract --> |"x1"| i_cobalt_purified_solution
  p_co_solvent_extract --> |"x1"| i_nickel_concentrate
  i_cobalt_purified_solution --> |"x1"| p_co_electrowin
  i_dc_charge --> |"x2"| p_co_electrowin
  p_co_electrowin --> |"x1"| i_cobalt_cathode
  p_co_electrowin --> |"x1"| i_slag
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_co_roast_cobaltite proc;
  class p_co_leach proc;
  class p_co_solvent_extract proc;
  class p_co_electrowin proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-electrowinning" markdown>
<div class="rc-out">:ci[cobalt_cathode|1] :ci[slag|1]</div>
<div class="rc-flow">:ci[cobalt_purified_solution|1] :ci[dc_charge|2] <span class="rc-arrow">→</span> :ci[cobalt_cathode|1] :ci[slag|1]</div>
<div class="rc-meta"><span class="rc-stn">Electrowinning Cell (Pb anode / SS cathode)</span> <span class="rc-time">120s</span> <span class="rc-tier">T4</span> <span class="rc-energy">200 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Electrowin bright cobalt metal onto starter sheets -- the pure cathode that finally lets the carbide insert use its correct binder.</div>
<div class="rc-id"><code>co_electrowin</code></div>
</div>
<div class="recipe-card cat-roasting" markdown>
<div class="rc-out">:ci[cobalt_oxide_roasted|1] :ci[gas_so2|1] :ci[arsenic_trioxide|1]</div>
<div class="rc-flow">:ci[raw_ore_cobaltite|2] :ci[gas_oxygen|1] <span class="rc-arrow">→</span> :ci[cobalt_oxide_roasted|1] :ci[gas_so2|1] :ci[arsenic_trioxide|1]</div>
<div class="rc-meta"><span class="rc-stn">Roasting Pit</span> <span class="rc-time">100s</span> <span class="rc-tier">T3</span> <span class="rc-energy">110 kJ</span> <span class="rc-bp">+2 byproducts</span></div>
<div class="rc-note">Dead-roast cobaltite (CoAsS): sulfur leaves as SO2 for the acid plant, arsenic is captured as toxic As2O3 from the flue rather than vented, and cobalt stays as a roasted oxide.</div>
<div class="rc-id"><code>co_roast_cobaltite</code></div>
</div>
<div class="recipe-card cat-solvent-extraction" markdown>
<div class="rc-out">:ci[cobalt_purified_solution|1] :ci[nickel_concentrate|1]</div>
<div class="rc-flow">:ci[cobalt_sulfate_solution|2] <span class="rc-arrow">→</span> :ci[cobalt_purified_solution|1] :ci[nickel_concentrate|1]</div>
<div class="rc-meta"><span class="rc-stn">Solvent-Extraction Mixer-Settler (LIX)</span> <span class="rc-time">140s</span> <span class="rc-tier">T4</span> <span class="rc-energy">120 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Solvent-extract the liquor to separate cobalt from its near-twin nickel (and copper). Cobalt and nickel always travel together in nature, so the stripped nickel is recovered as concentrate, not wasted.</div>
<div class="rc-id"><code>co_solvent_extract</code></div>
</div>
<div class="recipe-card cat-leaching" markdown>
<div class="rc-out">:ci[cobalt_sulfate_solution|2] :ci[waste_tailings|1]</div>
<div class="rc-flow">:ci[cobalt_oxide_roasted|2] :ci[acid_sulfuric|2] <span class="rc-arrow">→</span> :ci[cobalt_sulfate_solution|2] :ci[waste_tailings|1]</div>
<div class="rc-meta"><span class="rc-stn">Heap Leach Pad (acid irrigation)</span> <span class="rc-time">120s</span> <span class="rc-tier">T4</span> <span class="rc-energy">90 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Leach the roasted oxide in sulfuric acid to a pink cobalt sulfate liquor, leaving the inert gangue as tailings.</div>
<div class="rc-id"><code>co_leach</code></div>
</div>
</div>

## Gases chain
<p class="chapter-stats">5 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_air_raw["<img src='/Conduvia/assets/icons/air_raw.png' class='mmd-ico' />compressed air"]
  i_liquid_air["<img src='/Conduvia/assets/icons/liquid_air.png' class='mmd-ico' />liquid air"]
  i_gas_nitrogen["<img src='/Conduvia/assets/icons/gas_nitrogen.png' class='mmd-ico' />nitrogen gas"]
  i_gas_oxygen["<img src='/Conduvia/assets/icons/gas_oxygen.png' class='mmd-ico' />oxygen gas"]
  i_gas_argon["<img src='/Conduvia/assets/icons/gas_argon.png' class='mmd-ico' />argon gas"]
  i_gas_hydrogen["<img src='/Conduvia/assets/icons/gas_hydrogen.png' class='mmd-ico' />hydrogen gas"]
  i_gas_ammonia["<img src='/Conduvia/assets/icons/gas_ammonia.png' class='mmd-ico' />ammonia gas"]
  i_steel_ingot["<img src='/Conduvia/assets/icons/steel_ingot.png' class='mmd-ico' />steel ingot"]
  i_cylinder_gas_basic["<img src='/Conduvia/assets/icons/cylinder_gas_basic.png' class='mmd-ico' />basic gas cylinder"]
  p_gather_air_raw{"Gas Compressor"}
  p_asu_liquefy_air{"Cryogenic Air Separation Unit (ASU)"}
  p_asu_rectify_air{"Cryogenic Air Separation Unit (ASU)"}
  p_hb_synthesize_ammonia{"Haber-Bosch Ammonia Converter (iron cat., high P)"}
  p_gas_fab_cylinder{"Steam Machine Shop"}
  src_world["world"]:::world --> p_gather_air_raw
  p_gather_air_raw --> |"x10"| i_air_raw
  i_air_raw --> |"x10"| p_asu_liquefy_air
  p_asu_liquefy_air --> |"x10"| i_liquid_air
  i_liquid_air --> |"x10"| p_asu_rectify_air
  p_asu_rectify_air --> |"x7"| i_gas_nitrogen
  p_asu_rectify_air --> |"x2"| i_gas_oxygen
  p_asu_rectify_air --> |"x1"| i_gas_argon
  i_gas_nitrogen --> |"x1"| p_hb_synthesize_ammonia
  i_gas_hydrogen --> |"x3"| p_hb_synthesize_ammonia
  p_hb_synthesize_ammonia --> |"x2"| i_gas_ammonia
  i_steel_ingot --> |"x1"| p_gas_fab_cylinder
  p_gas_fab_cylinder --> |"x2"| i_cylinder_gas_basic
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_gather_air_raw proc;
  class p_asu_liquefy_air proc;
  class p_asu_rectify_air proc;
  class p_hb_synthesize_ammonia proc;
  class p_gas_fab_cylinder proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-gathering" markdown>
<div class="rc-out">:ci[air_raw|10]</div>
<div class="rc-meta"><span class="rc-stn">Gas Compressor</span> <span class="rc-time">5s</span> <span class="rc-tier">T1</span></div>
<div class="rc-note">Draw in and filter atmospheric air. Free and inexhaustible -- the feedstock for everything downstream of the ASU.</div>
<div class="rc-id"><code>gather_air_raw</code></div>
</div>
<div class="recipe-card cat-fabrication" markdown>
<div class="rc-out">:ci[cylinder_gas_basic|2]</div>
<div class="rc-flow">:ci[steel_ingot|1] <span class="rc-arrow">→</span> :ci[cylinder_gas_basic|2]</div>
<div class="rc-meta"><span class="rc-stn">Steam Machine Shop</span> <span class="rc-time">70s</span> <span class="rc-tier">T3</span> <span class="rc-energy">90 kJ</span></div>
<div class="rc-note">Deep-draw and spin a steel billet into a seamless high-pressure cylinder, empty and ready to fill. The reusable container behind every compressed-gas product.</div>
<div class="rc-id"><code>gas_fab_cylinder</code></div>
</div>
<div class="recipe-card cat-synthesis" markdown>
<div class="rc-out">:ci[gas_ammonia|2]</div>
<div class="rc-flow">:ci[gas_nitrogen|1] :ci[gas_hydrogen|3] <span class="rc-arrow">→</span> :ci[gas_ammonia|2]</div>
<div class="rc-meta"><span class="rc-stn">Haber-Bosch Ammonia Converter (iron cat., high P)</span> <span class="rc-time">150s</span> <span class="rc-tier">T4</span> <span class="rc-energy">320 kJ</span></div>
<div class="rc-note">Fix nitrogen: N2 + 3 H2 -> 2 NH3 over a promoted-iron catalyst at ~450C and >100 bar. Only a fraction converts per pass, so the unreacted gas is recycled. Hydrogen comes from the chlor-alkali cell, nitrogen from the ASU -- the two new gas plants closing into one.</div>
<div class="rc-id"><code>hb_synthesize_ammonia</code></div>
</div>
<div class="recipe-card cat-distillation" markdown>
<div class="rc-out">:ci[gas_nitrogen|7] :ci[gas_oxygen|2] :ci[gas_argon|1]</div>
<div class="rc-flow">:ci[liquid_air|10] <span class="rc-arrow">→</span> :ci[gas_nitrogen|7] :ci[gas_oxygen|2] :ci[gas_argon|1]</div>
<div class="rc-meta"><span class="rc-stn">Cryogenic Air Separation Unit (ASU)</span> <span class="rc-time">90s</span> <span class="rc-tier">T3</span> <span class="rc-energy">120 kJ</span> <span class="rc-bp">+2 byproducts</span></div>
<div class="rc-note">Rectify liquid air in a double column: counter-current distillation pulls volatile nitrogen (-196C) up and out the top, oxygen (-183C) collects at the bottom, and argon (-186C) is drawn from a side column. One feed, three pure products -- the cleanest multi-output in the plant.</div>
<div class="rc-id"><code>asu_rectify_air</code></div>
</div>
<div class="recipe-card cat-cryogenics" markdown>
<div class="rc-out">:ci[liquid_air|10]</div>
<div class="rc-flow">:ci[air_raw|10] <span class="rc-arrow">→</span> :ci[liquid_air|10]</div>
<div class="rc-meta"><span class="rc-stn">Cryogenic Air Separation Unit (ASU)</span> <span class="rc-time">60s</span> <span class="rc-tier">T3</span> <span class="rc-energy">220 kJ</span></div>
<div class="rc-note">Compress filtered air, scrub out CO2 and moisture (they freeze and plug the column), then chill it against the cold product streams until it condenses. Liquefying the air is the energy-hungry step; the separation that follows is nearly free.</div>
<div class="rc-id"><code>asu_liquefy_air</code></div>
</div>
</div>

## Gypsum chain
<p class="chapter-stats">5 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_gypsum["<img src='/Conduvia/assets/icons/raw_ore_gypsum.png' class='mmd-ico' />raw gypsum ore"]
  i_plaster_of_paris["<img src='/Conduvia/assets/icons/plaster_of_paris.png' class='mmd-ico' />plaster of Paris"]
  i_waste_gypsum_refined["<img src='/Conduvia/assets/icons/waste_gypsum_refined.png' class='mmd-ico' />refined gypsum"]
  i_water_raw["<img src='/Conduvia/assets/icons/water_raw.png' class='mmd-ico' />raw water"]
  i_gypsum_board["<img src='/Conduvia/assets/icons/gypsum_board.png' class='mmd-ico' />gypsum board (drywall)"]
  i_coke_fuel["<img src='/Conduvia/assets/icons/coke_fuel.png' class='mmd-ico' />coke fuel"]
  i_raw_ore_silica["<img src='/Conduvia/assets/icons/raw_ore_silica.png' class='mmd-ico' />raw silica ore"]
  i_gas_so2["<img src='/Conduvia/assets/icons/gas_so2.png' class='mmd-ico' />sulfur dioxide gas"]
  i_cement_clinker["<img src='/Conduvia/assets/icons/cement_clinker.png' class='mmd-ico' />cement clinker"]
  i_portland_cement["<img src='/Conduvia/assets/icons/portland_cement.png' class='mmd-ico' />Portland cement"]
  p_gyp_calcine_plaster{"Rotary Calcining Kiln (RKEF dry/reduce)"}
  p_gyp_recover_waste_plaster{"Rotary Calcining Kiln (RKEF dry/reduce)"}
  p_gyp_cast_board{"Clay Casting Pit"}
  p_gyp_muller_kuhne{"Rotary Calcining Kiln (RKEF dry/reduce)"}
  p_gyp_grind_portland{"Cement Ball Mill"}
  i_raw_ore_gypsum --> |"x2"| p_gyp_calcine_plaster
  p_gyp_calcine_plaster --> |"x2"| i_plaster_of_paris
  i_waste_gypsum_refined --> |"x2"| p_gyp_recover_waste_plaster
  p_gyp_recover_waste_plaster --> |"x2"| i_plaster_of_paris
  i_plaster_of_paris --> |"x2"| p_gyp_cast_board
  i_water_raw --> |"x1"| p_gyp_cast_board
  p_gyp_cast_board --> |"x2"| i_gypsum_board
  i_raw_ore_gypsum --> |"x2"| p_gyp_muller_kuhne
  i_coke_fuel --> |"x1"| p_gyp_muller_kuhne
  i_raw_ore_silica --> |"x1"| p_gyp_muller_kuhne
  p_gyp_muller_kuhne --> |"x1"| i_gas_so2
  p_gyp_muller_kuhne --> |"x2"| i_cement_clinker
  i_cement_clinker --> |"x2"| p_gyp_grind_portland
  i_raw_ore_gypsum --> |"x1"| p_gyp_grind_portland
  p_gyp_grind_portland --> |"x2"| i_portland_cement
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_gyp_calcine_plaster proc;
  class p_gyp_recover_waste_plaster proc;
  class p_gyp_cast_board proc;
  class p_gyp_muller_kuhne proc;
  class p_gyp_grind_portland proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-thermal-decomposition" markdown>
<div class="rc-out">:ci[gas_so2|1] :ci[cement_clinker|2]</div>
<div class="rc-flow">:ci[raw_ore_gypsum|2] :ci[coke_fuel|1] :ci[raw_ore_silica|1] <span class="rc-arrow">→</span> :ci[gas_so2|1] :ci[cement_clinker|2]</div>
<div class="rc-meta"><span class="rc-stn">Rotary Calcining Kiln (RKEF dry/reduce)</span> <span class="rc-time">260s</span> <span class="rc-tier">T4</span> <span class="rc-energy">250 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Mueller-Kuehne: starve gypsum of oxygen with coke at ~1400 C and it splits -- sulfur leaves as SO2 (sent to the contact acid plant) while the lime sinters with silica into cement clinker. One kiln makes both sulfuric acid AND cement, the classic move where native sulfur is scarce.</div>
<div class="rc-id"><code>gyp_muller_kuhne</code></div>
</div>
<div class="recipe-card cat-forming" markdown>
<div class="rc-out">:ci[gypsum_board|2]</div>
<div class="rc-flow">:ci[plaster_of_paris|2] :ci[water_raw|1] <span class="rc-arrow">→</span> :ci[gypsum_board|2]</div>
<div class="rc-meta"><span class="rc-stn">Clay Casting Pit</span> <span class="rc-time">40s</span> <span class="rc-tier">T2</span> <span class="rc-energy">20 kJ</span></div>
<div class="rc-note">Slurry plaster with water between paper sheets and let it re-hydrate to set rock-hard: gypsum board. The reaction is just the calcination run backwards.</div>
<div class="rc-id"><code>gyp_cast_board</code></div>
</div>
<div class="recipe-card cat-calcination" markdown>
<div class="rc-out">:ci[plaster_of_paris|2]</div>
<div class="rc-flow">:ci[raw_ore_gypsum|2] <span class="rc-arrow">→</span> :ci[plaster_of_paris|2]</div>
<div class="rc-meta"><span class="rc-stn">Rotary Calcining Kiln (RKEF dry/reduce)</span> <span class="rc-time">70s</span> <span class="rc-tier">T2</span> <span class="rc-energy">70 kJ</span></div>
<div class="rc-note">Gently calcine gypsum near 150 C to the hemihydrate -- plaster of Paris. Overshoot the temperature and you get dead-burnt anhydrite that will not set, so this is a low, controlled bake.</div>
<div class="rc-id"><code>gyp_calcine_plaster</code></div>
</div>
<div class="recipe-card cat-calcination" markdown>
<div class="rc-out">:ci[plaster_of_paris|2]</div>
<div class="rc-flow">:ci[waste_gypsum_refined|2] <span class="rc-arrow">→</span> :ci[plaster_of_paris|2]</div>
<div class="rc-meta"><span class="rc-stn">Rotary Calcining Kiln (RKEF dry/reduce)</span> <span class="rc-time">70s</span> <span class="rc-tier">T3</span> <span class="rc-energy">70 kJ</span></div>
<div class="rc-note">The HF chain throws off refined gypsum as a waste; calcine it the same way to plaster, turning a disposal problem into feedstock and closing the loop.</div>
<div class="rc-id"><code>gyp_recover_waste_plaster</code></div>
</div>
<div class="recipe-card cat-comminution" markdown>
<div class="rc-out">:ci[portland_cement|2]</div>
<div class="rc-flow">:ci[cement_clinker|2] :ci[raw_ore_gypsum|1] <span class="rc-arrow">→</span> :ci[portland_cement|2]</div>
<div class="rc-meta"><span class="rc-stn">Cement Ball Mill</span> <span class="rc-time">90s</span> <span class="rc-tier">T3</span> <span class="rc-energy">90 kJ</span></div>
<div class="rc-note">Grind clinker with a few percent raw gypsum as a set-retarder: Portland cement. Without that gypsum the cement would flash-set in the mixer before you could pour it.</div>
<div class="rc-id"><code>gyp_grind_portland</code></div>
</div>
</div>

## Lead chain
<p class="chapter-stats">6 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_galena["<img src='/Conduvia/assets/icons/raw_ore_galena.png' class='mmd-ico' />raw galena ore"]
  i_concentrate_galena["<img src='/Conduvia/assets/icons/concentrate_galena.png' class='mmd-ico' />galena concentrate"]
  i_waste_tailings["<img src='/Conduvia/assets/icons/waste_tailings.png' class='mmd-ico' />tailings"]
  i_gas_oxygen["<img src='/Conduvia/assets/icons/gas_oxygen.png' class='mmd-ico' />oxygen gas"]
  i_lead_sinter_oxide["<img src='/Conduvia/assets/icons/lead_sinter_oxide.png' class='mmd-ico' />lead oxide sinter"]
  i_gas_so2["<img src='/Conduvia/assets/icons/gas_so2.png' class='mmd-ico' />sulfur dioxide gas"]
  i_coke_fuel["<img src='/Conduvia/assets/icons/coke_fuel.png' class='mmd-ico' />coke fuel"]
  i_limestone_flux["<img src='/Conduvia/assets/icons/limestone_flux.png' class='mmd-ico' />limestone flux"]
  i_lead_bullion["<img src='/Conduvia/assets/icons/lead_bullion.png' class='mmd-ico' />crude lead bullion"]
  i_slag["<img src='/Conduvia/assets/icons/slag.png' class='mmd-ico' />slag"]
  i_gas_co2["<img src='/Conduvia/assets/icons/gas_co2.png' class='mmd-ico' />carbon dioxide gas"]
  i_metal_zinc_ingot["<img src='/Conduvia/assets/icons/metal_zinc_ingot.png' class='mmd-ico' />zinc ingot"]
  i_lead_softened["<img src='/Conduvia/assets/icons/lead_softened.png' class='mmd-ico' />softened lead"]
  i_silver_zinc_crust["<img src='/Conduvia/assets/icons/silver_zinc_crust.png' class='mmd-ico' />silver-zinc crust"]
  i_silver_dore["<img src='/Conduvia/assets/icons/silver_dore.png' class='mmd-ico' />silver dore"]
  i_litharge_pbo["<img src='/Conduvia/assets/icons/litharge_pbo.png' class='mmd-ico' />litharge (PbO)"]
  i_metal_lead_ingot["<img src='/Conduvia/assets/icons/metal_lead_ingot.png' class='mmd-ico' />lead ingot"]
  p_pb_froth_flotation{"Froth Flotation Cell"}
  p_pb_sinter_roast{"Sinter Strand (Dwight-Lloyd)"}
  p_pb_blast_reduce{"Blast Furnace"}
  p_pb_parkes_desilver{"Fire-Refining Furnace"}
  p_pb_cupellation{"Cupellation Hearth (silver assay/refine)"}
  p_pb_refine_cast{"Fire-Refining Furnace"}
  i_raw_ore_galena --> |"x3"| p_pb_froth_flotation
  p_pb_froth_flotation --> |"x2"| i_concentrate_galena
  p_pb_froth_flotation --> |"x1"| i_waste_tailings
  i_concentrate_galena --> |"x2"| p_pb_sinter_roast
  i_gas_oxygen --> |"x1"| p_pb_sinter_roast
  p_pb_sinter_roast --> |"x2"| i_lead_sinter_oxide
  p_pb_sinter_roast --> |"x1"| i_gas_so2
  i_lead_sinter_oxide --> |"x2"| p_pb_blast_reduce
  i_coke_fuel --> |"x1"| p_pb_blast_reduce
  i_limestone_flux --> |"x1"| p_pb_blast_reduce
  p_pb_blast_reduce --> |"x2"| i_lead_bullion
  p_pb_blast_reduce --> |"x1"| i_slag
  p_pb_blast_reduce --> |"x1"| i_gas_co2
  i_lead_bullion --> |"x2"| p_pb_parkes_desilver
  i_metal_zinc_ingot --> |"x1"| p_pb_parkes_desilver
  p_pb_parkes_desilver --> |"x2"| i_lead_softened
  p_pb_parkes_desilver --> |"x1"| i_silver_zinc_crust
  i_silver_zinc_crust --> |"x1"| p_pb_cupellation
  i_gas_oxygen --> |"x1"| p_pb_cupellation
  p_pb_cupellation --> |"x1"| i_silver_dore
  p_pb_cupellation --> |"x1"| i_litharge_pbo
  i_lead_softened --> |"x2"| p_pb_refine_cast
  p_pb_refine_cast --> |"x2"| i_metal_lead_ingot
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_pb_froth_flotation proc;
  class p_pb_sinter_roast proc;
  class p_pb_blast_reduce proc;
  class p_pb_parkes_desilver proc;
  class p_pb_cupellation proc;
  class p_pb_refine_cast proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-beneficiation" markdown>
<div class="rc-out">:ci[concentrate_galena|2] :ci[waste_tailings|1]</div>
<div class="rc-flow">:ci[raw_ore_galena|3] <span class="rc-arrow">→</span> :ci[concentrate_galena|2] :ci[waste_tailings|1]</div>
<div class="rc-meta"><span class="rc-stn">Froth Flotation Cell</span> <span class="rc-time">60s</span> <span class="rc-tier">T2</span> <span class="rc-energy">40 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Froth-float crushed galena: the heavy lead sulfide rides the bubbles to a concentrate, the silica gangue sinks as tailings.</div>
<div class="rc-id"><code>pb_froth_flotation</code></div>
</div>
<div class="recipe-card cat-smelting" markdown>
<div class="rc-out">:ci[lead_bullion|2] :ci[slag|1] :ci[gas_co2|1]</div>
<div class="rc-flow">:ci[lead_sinter_oxide|2] :ci[coke_fuel|1] :ci[limestone_flux|1] <span class="rc-arrow">→</span> :ci[lead_bullion|2] :ci[slag|1] :ci[gas_co2|1]</div>
<div class="rc-meta"><span class="rc-stn">Blast Furnace</span> <span class="rc-time">220s</span> <span class="rc-tier">T3</span> <span class="rc-energy">240 kJ</span> <span class="rc-bp">+2 byproducts</span></div>
<div class="rc-note">Reduce the lead sinter with coke in a blast furnace to crude bullion. The silver in the ore reports almost entirely into the molten lead; iron and rock leave as slag.</div>
<div class="rc-id"><code>pb_blast_reduce</code></div>
</div>
<div class="recipe-card cat-roasting" markdown>
<div class="rc-out">:ci[lead_sinter_oxide|2] :ci[gas_so2|1]</div>
<div class="rc-flow">:ci[concentrate_galena|2] :ci[gas_oxygen|1] <span class="rc-arrow">→</span> :ci[lead_sinter_oxide|2] :ci[gas_so2|1]</div>
<div class="rc-meta"><span class="rc-stn">Sinter Strand (Dwight-Lloyd)</span> <span class="rc-time">110s</span> <span class="rc-tier">T3</span> <span class="rc-energy">120 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Roast-sinter the concentrate: PbS burns to PbO and a hard sinter cake, throwing SO2 to the contact acid plant -- sulfide metallurgy always feeds an acid plant.</div>
<div class="rc-id"><code>pb_sinter_roast</code></div>
</div>
<div class="recipe-card cat-refining" markdown>
<div class="rc-out">:ci[lead_softened|2] :ci[silver_zinc_crust|1]</div>
<div class="rc-flow">:ci[lead_bullion|2] :ci[metal_zinc_ingot|1] <span class="rc-arrow">→</span> :ci[lead_softened|2] :ci[silver_zinc_crust|1]</div>
<div class="rc-meta"><span class="rc-stn">Fire-Refining Furnace</span> <span class="rc-time">130s</span> <span class="rc-tier">T3</span> <span class="rc-energy">110 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">The Parkes process: stir zinc into the molten bullion. Silver is far more soluble in zinc than in lead, so it floats out as a zinc-silver crust that is skimmed off, leaving softened lead. (This is why lead refining quietly consumes zinc.)</div>
<div class="rc-id"><code>pb_parkes_desilver</code></div>
</div>
<div class="recipe-card cat-casting" markdown>
<div class="rc-out">:ci[metal_lead_ingot|2]</div>
<div class="rc-flow">:ci[lead_softened|2] <span class="rc-arrow">→</span> :ci[metal_lead_ingot|2]</div>
<div class="rc-meta"><span class="rc-stn">Fire-Refining Furnace</span> <span class="rc-time">90s</span> <span class="rc-tier">T3</span> <span class="rc-energy">80 kJ</span></div>
<div class="rc-note">Fire-refine and cast the softened lead into clean ingots -- corrosion-proof, dense, and ready for shielding, batteries, and chamber-acid plumbing.</div>
<div class="rc-id"><code>pb_refine_cast</code></div>
</div>
<div class="recipe-card cat-cupellation" markdown>
<div class="rc-out">:ci[silver_dore|1] :ci[litharge_pbo|1]</div>
<div class="rc-flow">:ci[silver_zinc_crust|1] :ci[gas_oxygen|1] <span class="rc-arrow">→</span> :ci[silver_dore|1] :ci[litharge_pbo|1]</div>
<div class="rc-meta"><span class="rc-stn">Cupellation Hearth (silver assay/refine)</span> <span class="rc-time">150s</span> <span class="rc-tier">T3</span> <span class="rc-energy">140 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Cupel the crust under an air blast: zinc and lead oxidise to litharge and are absorbed/skimmed, leaving a noble button of dore silver. The oldest assay there is.</div>
<div class="rc-id"><code>pb_cupellation</code></div>
</div>
</div>

## Lithium chain
<p class="chapter-stats">5 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_spodumene["<img src='/Conduvia/assets/icons/raw_ore_spodumene.png' class='mmd-ico' />raw spodumene ore"]
  i_spodumene_beta["<img src='/Conduvia/assets/icons/spodumene_beta.png' class='mmd-ico' />beta-spodumene"]
  i_acid_sulfuric["<img src='/Conduvia/assets/icons/acid_sulfuric.png' class='mmd-ico' />sulfuric acid"]
  i_lithium_sulfate_crude["<img src='/Conduvia/assets/icons/lithium_sulfate_crude.png' class='mmd-ico' />crude lithium sulfate"]
  i_waste_tailings["<img src='/Conduvia/assets/icons/waste_tailings.png' class='mmd-ico' />tailings"]
  i_burned_lime_quicklime["<img src='/Conduvia/assets/icons/burned_lime_quicklime.png' class='mmd-ico' />burned lime (quicklime)"]
  i_lithium_sulfate_solution["<img src='/Conduvia/assets/icons/lithium_sulfate_solution.png' class='mmd-ico' />lithium sulfate liquor"]
  i_sodium_hydroxide["<img src='/Conduvia/assets/icons/sodium_hydroxide.png' class='mmd-ico' />sodium hydroxide"]
  i_lithium_hydroxide["<img src='/Conduvia/assets/icons/lithium_hydroxide.png' class='mmd-ico' />lithium hydroxide monohydrate"]
  i_salt_sodium_sulfate["<img src='/Conduvia/assets/icons/salt_sodium_sulfate.png' class='mmd-ico' />sodium sulfate"]
  i_gas_co2["<img src='/Conduvia/assets/icons/gas_co2.png' class='mmd-ico' />carbon dioxide gas"]
  i_lithium_carbonate["<img src='/Conduvia/assets/icons/lithium_carbonate.png' class='mmd-ico' />lithium carbonate (battery grade)"]
  p_li_decrepitate{"Rotary Calcining Kiln (RKEF dry/reduce)"}
  p_li_acid_bake{"Sulfation Acid-Roast Kiln"}
  p_li_leach_purify{"Heap Leach Pad (acid irrigation)"}
  p_li_causticize{"Caustic Digester Autoclave (alkali leach)"}
  p_li_carbonate{"Carbonation Precipitation Reactor"}
  i_raw_ore_spodumene --> |"x2"| p_li_decrepitate
  p_li_decrepitate --> |"x2"| i_spodumene_beta
  i_spodumene_beta --> |"x2"| p_li_acid_bake
  i_acid_sulfuric --> |"x1"| p_li_acid_bake
  p_li_acid_bake --> |"x2"| i_lithium_sulfate_crude
  p_li_acid_bake --> |"x1"| i_waste_tailings
  i_lithium_sulfate_crude --> |"x2"| p_li_leach_purify
  i_burned_lime_quicklime --> |"x1"| p_li_leach_purify
  p_li_leach_purify --> |"x2"| i_lithium_sulfate_solution
  p_li_leach_purify --> |"x1"| i_waste_tailings
  i_lithium_sulfate_solution --> |"x2"| p_li_causticize
  i_sodium_hydroxide --> |"x2"| p_li_causticize
  p_li_causticize --> |"x2"| i_lithium_hydroxide
  p_li_causticize --> |"x1"| i_salt_sodium_sulfate
  i_lithium_hydroxide --> |"x2"| p_li_carbonate
  i_gas_co2 --> |"x1"| p_li_carbonate
  p_li_carbonate --> |"x1"| i_lithium_carbonate
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_li_decrepitate proc;
  class p_li_acid_bake proc;
  class p_li_leach_purify proc;
  class p_li_causticize proc;
  class p_li_carbonate proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-precipitation" markdown>
<div class="rc-out">:ci[lithium_carbonate|1]</div>
<div class="rc-flow">:ci[lithium_hydroxide|2] :ci[gas_co2|1] <span class="rc-arrow">→</span> :ci[lithium_carbonate|1]</div>
<div class="rc-meta"><span class="rc-stn">Carbonation Precipitation Reactor</span> <span class="rc-time">90s</span> <span class="rc-tier">T4</span> <span class="rc-energy">70 kJ</span></div>
<div class="rc-note">Bubble CO2 through lithium hydroxide to drop battery-grade lithium carbonate: 2 LiOH + CO2 -> Li2CO3 + H2O. The classic lithium-ion feedstock.</div>
<div class="rc-id"><code>li_carbonate</code></div>
</div>
<div class="recipe-card cat-metathesis" markdown>
<div class="rc-out">:ci[lithium_hydroxide|2] :ci[salt_sodium_sulfate|1]</div>
<div class="rc-flow">:ci[lithium_sulfate_solution|2] :ci[sodium_hydroxide|2] <span class="rc-arrow">→</span> :ci[lithium_hydroxide|2] :ci[salt_sodium_sulfate|1]</div>
<div class="rc-meta"><span class="rc-stn">Caustic Digester Autoclave (alkali leach)</span> <span class="rc-time">110s</span> <span class="rc-tier">T4</span> <span class="rc-energy">80 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Causticise the liquor with caustic soda: Li2SO4 + 2 NaOH -> 2 LiOH + Na2SO4. The lithium hydroxide crystallises out and the sodium sulfate byproduct is recovered as a salable salt.</div>
<div class="rc-id"><code>li_causticize</code></div>
</div>
<div class="recipe-card cat-acid-roast" markdown>
<div class="rc-out">:ci[lithium_sulfate_crude|2] :ci[waste_tailings|1]</div>
<div class="rc-flow">:ci[spodumene_beta|2] :ci[acid_sulfuric|1] <span class="rc-arrow">→</span> :ci[lithium_sulfate_crude|2] :ci[waste_tailings|1]</div>
<div class="rc-meta"><span class="rc-stn">Sulfation Acid-Roast Kiln</span> <span class="rc-time">200s</span> <span class="rc-tier">T4</span> <span class="rc-energy">200 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Bake beta-spodumene with concentrated sulfuric acid at ~250 C: lithium ion-exchanges onto the sulfate, leaving the alumino-silicate skeleton as inert residue.</div>
<div class="rc-id"><code>li_acid_bake</code></div>
</div>
<div class="recipe-card cat-leaching" markdown>
<div class="rc-out">:ci[lithium_sulfate_solution|2] :ci[waste_tailings|1]</div>
<div class="rc-flow">:ci[lithium_sulfate_crude|2] :ci[burned_lime_quicklime|1] <span class="rc-arrow">→</span> :ci[lithium_sulfate_solution|2] :ci[waste_tailings|1]</div>
<div class="rc-meta"><span class="rc-stn">Heap Leach Pad (acid irrigation)</span> <span class="rc-time">120s</span> <span class="rc-tier">T4</span> <span class="rc-energy">90 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Water-leach the bake and add lime to precipitate iron and aluminium, leaving a clean lithium sulfate liquor.</div>
<div class="rc-id"><code>li_leach_purify</code></div>
</div>
<div class="recipe-card cat-calcination" markdown>
<div class="rc-out">:ci[spodumene_beta|2]</div>
<div class="rc-flow">:ci[raw_ore_spodumene|2] <span class="rc-arrow">→</span> :ci[spodumene_beta|2]</div>
<div class="rc-meta"><span class="rc-stn">Rotary Calcining Kiln (RKEF dry/reduce)</span> <span class="rc-time">180s</span> <span class="rc-tier">T4</span> <span class="rc-energy">240 kJ</span></div>
<div class="rc-note">Decrepitate spodumene near 1100 C: the alpha crystal flips to the open beta form. Skip this and acid simply will not attack the ore -- the step everyone forgets.</div>
<div class="rc-id"><code>li_decrepitate</code></div>
</div>
</div>

## Magnesium chain
<p class="chapter-stats">7 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_dolomite["<img src='/Conduvia/assets/icons/raw_ore_dolomite.png' class='mmd-ico' />dolomite"]
  i_dolime_calcined["<img src='/Conduvia/assets/icons/dolime_calcined.png' class='mmd-ico' />calcined dolime (MgO·CaO)"]
  i_gas_co2["<img src='/Conduvia/assets/icons/gas_co2.png' class='mmd-ico' />carbon dioxide gas"]
  i_raw_ore_silica["<img src='/Conduvia/assets/icons/raw_ore_silica.png' class='mmd-ico' />raw silica ore"]
  i_pig_iron_ingot["<img src='/Conduvia/assets/icons/pig_iron_ingot.png' class='mmd-ico' />pig iron ingot"]
  i_coke_fuel["<img src='/Conduvia/assets/icons/coke_fuel.png' class='mmd-ico' />coke fuel"]
  i_ferrosilicon["<img src='/Conduvia/assets/icons/ferrosilicon.png' class='mmd-ico' />ferrosilicon (FeSi)"]
  i_magnesium_crown["<img src='/Conduvia/assets/icons/magnesium_crown.png' class='mmd-ico' />magnesium crown (crude)"]
  i_dicalcium_silicate_slag["<img src='/Conduvia/assets/icons/dicalcium_silicate_slag.png' class='mmd-ico' />dicalcium silicate slag"]
  i_magnesium_ingot["<img src='/Conduvia/assets/icons/magnesium_ingot.png' class='mmd-ico' />magnesium ingot"]
  i_brine_solution["<img src='/Conduvia/assets/icons/brine_solution.png' class='mmd-ico' />brine solution"]
  i_burned_lime_quicklime["<img src='/Conduvia/assets/icons/burned_lime_quicklime.png' class='mmd-ico' />burned lime (quicklime)"]
  i_magnesium_hydroxide["<img src='/Conduvia/assets/icons/magnesium_hydroxide.png' class='mmd-ico' />magnesium hydroxide"]
  i_waste_tailings["<img src='/Conduvia/assets/icons/waste_tailings.png' class='mmd-ico' />tailings"]
  i_gas_chlorine["<img src='/Conduvia/assets/icons/gas_chlorine.png' class='mmd-ico' />chlorine gas"]
  i_magnesium_chloride_anhydrous["<img src='/Conduvia/assets/icons/magnesium_chloride_anhydrous.png' class='mmd-ico' />anhydrous magnesium chloride"]
  i_dc_charge["<img src='/Conduvia/assets/icons/dc_charge.png' class='mmd-ico' />DC power charge"]
  p_mg_calcine_dolomite{"Rotary Calcining Kiln (RKEF dry/reduce)"}
  p_mg_make_ferrosilicon{"Submerged-Arc Furnace (SAF)"}
  p_mg_pidgeon_reduce{"Pidgeon Vacuum Retort (silicothermic)"}
  p_mg_remelt_ingot{"Flux-Protected Remelt Furnace (Mg)"}
  p_mg_precipitate_hydroxide{"Caustic Digester Autoclave (alkali leach)"}
  p_mg_chlorinate_mgcl2{"Carbo-Chlorination Reactor (MgCl2)"}
  p_mg_electrolysis{"Fused-Salt Electrolysis Cell (Mg)"}
  i_raw_ore_dolomite --> |"x2"| p_mg_calcine_dolomite
  p_mg_calcine_dolomite --> |"x2"| i_dolime_calcined
  p_mg_calcine_dolomite --> |"x1"| i_gas_co2
  i_raw_ore_silica --> |"x2"| p_mg_make_ferrosilicon
  i_pig_iron_ingot --> |"x1"| p_mg_make_ferrosilicon
  i_coke_fuel --> |"x2"| p_mg_make_ferrosilicon
  p_mg_make_ferrosilicon --> |"x1"| i_ferrosilicon
  p_mg_make_ferrosilicon --> |"x1"| i_gas_co2
  i_dolime_calcined --> |"x4"| p_mg_pidgeon_reduce
  i_ferrosilicon --> |"x1"| p_mg_pidgeon_reduce
  p_mg_pidgeon_reduce --> |"x2"| i_magnesium_crown
  p_mg_pidgeon_reduce --> |"x1"| i_dicalcium_silicate_slag
  i_magnesium_crown --> |"x2"| p_mg_remelt_ingot
  p_mg_remelt_ingot --> |"x1"| i_magnesium_ingot
  i_brine_solution --> |"x2"| p_mg_precipitate_hydroxide
  i_burned_lime_quicklime --> |"x1"| p_mg_precipitate_hydroxide
  p_mg_precipitate_hydroxide --> |"x1"| i_magnesium_hydroxide
  p_mg_precipitate_hydroxide --> |"x1"| i_waste_tailings
  i_magnesium_hydroxide --> |"x1"| p_mg_chlorinate_mgcl2
  i_gas_chlorine --> |"x1"| p_mg_chlorinate_mgcl2
  i_coke_fuel --> |"x1"| p_mg_chlorinate_mgcl2
  p_mg_chlorinate_mgcl2 --> |"x1"| i_magnesium_chloride_anhydrous
  p_mg_chlorinate_mgcl2 --> |"x1"| i_gas_co2
  i_magnesium_chloride_anhydrous --> |"x2"| p_mg_electrolysis
  i_dc_charge --> |"x2"| p_mg_electrolysis
  p_mg_electrolysis --> |"x2"| i_magnesium_ingot
  p_mg_electrolysis --> |"x1"| i_gas_chlorine
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_mg_calcine_dolomite proc;
  class p_mg_make_ferrosilicon proc;
  class p_mg_pidgeon_reduce proc;
  class p_mg_remelt_ingot proc;
  class p_mg_precipitate_hydroxide proc;
  class p_mg_chlorinate_mgcl2 proc;
  class p_mg_electrolysis proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-calcination" markdown>
<div class="rc-out">:ci[dolime_calcined|2] :ci[gas_co2|1]</div>
<div class="rc-flow">:ci[raw_ore_dolomite|2] <span class="rc-arrow">→</span> :ci[dolime_calcined|2] :ci[gas_co2|1]</div>
<div class="rc-meta"><span class="rc-stn">Rotary Calcining Kiln (RKEF dry/reduce)</span> <span class="rc-time">90s</span> <span class="rc-tier">T3</span> <span class="rc-energy">100 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Calcine dolomite to dolime, driving off CO2 and leaving mixed MgO/CaO -- the charge the Pidgeon retort will reduce.</div>
<div class="rc-id"><code>mg_calcine_dolomite</code></div>
</div>
<div class="recipe-card cat-smelting" markdown>
<div class="rc-out">:ci[ferrosilicon|1] :ci[gas_co2|1]</div>
<div class="rc-flow">:ci[raw_ore_silica|2] :ci[pig_iron_ingot|1] :ci[coke_fuel|2] <span class="rc-arrow">→</span> :ci[ferrosilicon|1] :ci[gas_co2|1]</div>
<div class="rc-meta"><span class="rc-stn">Submerged-Arc Furnace (SAF)</span> <span class="rc-time">130s</span> <span class="rc-tier">T3</span> <span class="rc-energy">260 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Smelt silica with iron and coke in a submerged-arc furnace to ferrosilicon -- a steel deoxidiser, and here the reductant that will free magnesium from dolime.</div>
<div class="rc-id"><code>mg_make_ferrosilicon</code></div>
</div>
<div class="recipe-card cat-carbo-chlorination" markdown>
<div class="rc-out">:ci[magnesium_chloride_anhydrous|1] :ci[gas_co2|1]</div>
<div class="rc-flow">:ci[magnesium_hydroxide|1] :ci[gas_chlorine|1] :ci[coke_fuel|1] <span class="rc-arrow">→</span> :ci[magnesium_chloride_anhydrous|1] :ci[gas_co2|1]</div>
<div class="rc-meta"><span class="rc-stn">Carbo-Chlorination Reactor (MgCl2)</span> <span class="rc-time">130s</span> <span class="rc-tier">T4</span> <span class="rc-energy">140 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Carbo-chlorinate the hydroxide to bone-dry MgCl2 (carbon scavenges the oxygen as CO2, chlorine takes the magnesium). Anhydrous feed is essential -- any water hydrolyses it back to oxide.</div>
<div class="rc-id"><code>mg_chlorinate_mgcl2</code></div>
</div>
<div class="recipe-card cat-silicothermic-reduction" markdown>
<div class="rc-out">:ci[magnesium_crown|2] :ci[dicalcium_silicate_slag|1]</div>
<div class="rc-flow">:ci[dolime_calcined|4] :ci[ferrosilicon|1] <span class="rc-arrow">→</span> :ci[magnesium_crown|2] :ci[dicalcium_silicate_slag|1]</div>
<div class="rc-meta"><span class="rc-stn">Pidgeon Vacuum Retort (silicothermic)</span> <span class="rc-time">300s</span> <span class="rc-tier">T4</span> <span class="rc-energy">220 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">The Pidgeon step: under vacuum at ~1200 C, silicon in ferrosilicon reduces magnesia (2 MgO.CaO + Si -> 2 Mg + Ca2SiO4). Magnesium boils off and condenses as a crown at the cold end; dicalcium-silicate slag stays behind.</div>
<div class="rc-id"><code>mg_pidgeon_reduce</code></div>
</div>
<div class="recipe-card cat-precipitation" markdown>
<div class="rc-out">:ci[magnesium_hydroxide|1] :ci[waste_tailings|1]</div>
<div class="rc-flow">:ci[brine_solution|2] :ci[burned_lime_quicklime|1] <span class="rc-arrow">→</span> :ci[magnesium_hydroxide|1] :ci[waste_tailings|1]</div>
<div class="rc-meta"><span class="rc-stn">Caustic Digester Autoclave (alkali leach)</span> <span class="rc-time">80s</span> <span class="rc-tier">T3</span> <span class="rc-energy">60 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Stir lime into magnesium-bearing brine; magnesium drops out as a milky Mg(OH)2 precipitate, the same trick used to win magnesium from seawater.</div>
<div class="rc-id"><code>mg_precipitate_hydroxide</code></div>
</div>
<div class="recipe-card cat-casting" markdown>
<div class="rc-out">:ci[magnesium_ingot|1]</div>
<div class="rc-flow">:ci[magnesium_crown|2] <span class="rc-arrow">→</span> :ci[magnesium_ingot|1]</div>
<div class="rc-meta"><span class="rc-stn">Flux-Protected Remelt Furnace (Mg)</span> <span class="rc-time">110s</span> <span class="rc-tier">T4</span> <span class="rc-energy">100 kJ</span></div>
<div class="rc-note">Remelt the crude crown under a protective salt flux (magnesium burns in air) and cast a clean magnesium ingot.</div>
<div class="rc-id"><code>mg_remelt_ingot</code></div>
</div>
<div class="recipe-card cat-electrolysis" markdown>
<div class="rc-out">:ci[magnesium_ingot|2] :ci[gas_chlorine|1]</div>
<div class="rc-flow">:ci[magnesium_chloride_anhydrous|2] :ci[dc_charge|2] <span class="rc-arrow">→</span> :ci[magnesium_ingot|2] :ci[gas_chlorine|1]</div>
<div class="rc-meta"><span class="rc-stn">Fused-Salt Electrolysis Cell (Mg)</span> <span class="rc-time">240s</span> <span class="rc-tier">T4</span> <span class="rc-energy">420 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Electrolyse molten MgCl2: magnesium metal collects at the cathode and chlorine gas comes off the anode -- piped straight back to the chlorinator, closing the chlorine loop just like the sodium loop in titanium.</div>
<div class="rc-id"><code>mg_electrolysis</code></div>
</div>
</div>

## Natural Gas chain
<p class="chapter-stats">9 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_natural_gas_raw["<img src='/Conduvia/assets/icons/natural_gas_raw.png' class='mmd-ico' />raw natural gas"]
  i_gas_methane["<img src='/Conduvia/assets/icons/gas_methane.png' class='mmd-ico' />methane gas"]
  i_gas_co2["<img src='/Conduvia/assets/icons/gas_co2.png' class='mmd-ico' />carbon dioxide gas"]
  i_gas_hydrogen_sulfide["<img src='/Conduvia/assets/icons/gas_hydrogen_sulfide.png' class='mmd-ico' />hydrogen sulfide gas"]
  i_gas_oxygen["<img src='/Conduvia/assets/icons/gas_oxygen.png' class='mmd-ico' />oxygen gas"]
  i_sulfur_recovered["<img src='/Conduvia/assets/icons/sulfur_recovered.png' class='mmd-ico' />recovered sulfur"]
  i_water_raw["<img src='/Conduvia/assets/icons/water_raw.png' class='mmd-ico' />raw water"]
  i_crude_helium["<img src='/Conduvia/assets/icons/crude_helium.png' class='mmd-ico' />crude helium"]
  i_gas_nitrogen["<img src='/Conduvia/assets/icons/gas_nitrogen.png' class='mmd-ico' />nitrogen gas"]
  i_gas_helium["<img src='/Conduvia/assets/icons/gas_helium.png' class='mmd-ico' />helium gas"]
  i_cylinder_gas_basic["<img src='/Conduvia/assets/icons/cylinder_gas_basic.png' class='mmd-ico' />basic gas cylinder"]
  i_cylinder_helium["<img src='/Conduvia/assets/icons/cylinder_helium.png' class='mmd-ico' />helium cylinder"]
  i_gas_syngas["<img src='/Conduvia/assets/icons/gas_syngas.png' class='mmd-ico' />synthesis gas"]
  i_gas_hydrogen["<img src='/Conduvia/assets/icons/gas_hydrogen.png' class='mmd-ico' />hydrogen gas"]
  i_gas_so2["<img src='/Conduvia/assets/icons/gas_so2.png' class='mmd-ico' />sulfur dioxide gas"]
  p_ng_gather_natural_gas{"Natural-Gas Well & Derrick"}
  p_ng_amine_sweeten{"Amine Gas-Sweetening Unit"}
  p_ng_claus_sulfur{"Claus Sulfur-Recovery Unit"}
  p_ng_cryo_recover_helium{"Cryogenic Helium Recovery (N2 rejection) Unit"}
  p_ng_purify_helium{"Helium PSA Purifier"}
  p_he_fill_cylinder{"Gas Compressor"}
  p_smr_steam_reform{"Steam-Methane Reformer"}
  p_smr_water_gas_shift{"Steam-Methane Reformer"}
  p_ng_burn_sulfur{"Sulfur Burner / Pyrite Roaster"}
  src_world["world"]:::world --> p_ng_gather_natural_gas
  p_ng_gather_natural_gas --> |"x2"| i_natural_gas_raw
  i_natural_gas_raw --> |"x3"| p_ng_amine_sweeten
  p_ng_amine_sweeten --> |"x2"| i_gas_methane
  p_ng_amine_sweeten --> |"x1"| i_gas_co2
  p_ng_amine_sweeten --> |"x1"| i_gas_hydrogen_sulfide
  i_gas_hydrogen_sulfide --> |"x3"| p_ng_claus_sulfur
  i_gas_oxygen --> |"x1"| p_ng_claus_sulfur
  p_ng_claus_sulfur --> |"x3"| i_sulfur_recovered
  p_ng_claus_sulfur --> |"x2"| i_water_raw
  i_gas_methane --> |"x4"| p_ng_cryo_recover_helium
  p_ng_cryo_recover_helium --> |"x1"| i_crude_helium
  p_ng_cryo_recover_helium --> |"x2"| i_gas_nitrogen
  i_crude_helium --> |"x2"| p_ng_purify_helium
  p_ng_purify_helium --> |"x1"| i_gas_helium
  i_cylinder_gas_basic --> |"x1"| p_he_fill_cylinder
  i_gas_helium --> |"x1"| p_he_fill_cylinder
  p_he_fill_cylinder --> |"x1"| i_cylinder_helium
  i_gas_methane --> |"x1"| p_smr_steam_reform
  i_water_raw --> |"x2"| p_smr_steam_reform
  p_smr_steam_reform --> |"x3"| i_gas_syngas
  i_gas_syngas --> |"x3"| p_smr_water_gas_shift
  i_water_raw --> |"x1"| p_smr_water_gas_shift
  p_smr_water_gas_shift --> |"x4"| i_gas_hydrogen
  p_smr_water_gas_shift --> |"x1"| i_gas_co2
  i_sulfur_recovered --> |"x2"| p_ng_burn_sulfur
  i_gas_oxygen --> |"x2"| p_ng_burn_sulfur
  p_ng_burn_sulfur --> |"x2"| i_gas_so2
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_ng_gather_natural_gas proc;
  class p_ng_amine_sweeten proc;
  class p_ng_claus_sulfur proc;
  class p_ng_cryo_recover_helium proc;
  class p_ng_purify_helium proc;
  class p_he_fill_cylinder proc;
  class p_smr_steam_reform proc;
  class p_smr_water_gas_shift proc;
  class p_ng_burn_sulfur proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-cryogenic-separation" markdown>
<div class="rc-out">:ci[crude_helium|1] :ci[gas_nitrogen|2]</div>
<div class="rc-flow">:ci[gas_methane|4] <span class="rc-arrow">→</span> :ci[crude_helium|1] :ci[gas_nitrogen|2]</div>
<div class="rc-meta"><span class="rc-stn">Cryogenic Helium Recovery (N2 rejection) Unit</span> <span class="rc-time">120s</span> <span class="rc-tier">T5</span> <span class="rc-energy">200 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Chill the sweet gas until everything but helium liquefies (nitrogen rejection). You process a huge volume of gas to skim off a little crude helium -- but natural gas is the only place on Earth helium is concentrated enough to catch.</div>
<div class="rc-id"><code>ng_cryo_recover_helium</code></div>
</div>
<div class="recipe-card cat-cylinder-fill" markdown>
<div class="rc-out">:ci[cylinder_helium|1]</div>
<div class="rc-flow">:ci[cylinder_gas_basic|1] :ci[gas_helium|1] <span class="rc-arrow">→</span> :ci[cylinder_helium|1]</div>
<div class="rc-meta"><span class="rc-stn">Gas Compressor</span> <span class="rc-time">30s</span> <span class="rc-tier">T4</span> <span class="rc-energy">40 kJ</span></div>
<div class="rc-note">Compress purified helium into a cylinder for storage and transport. Seal it well -- helium leaks through gaskets that hold any other gas.</div>
<div class="rc-id"><code>he_fill_cylinder</code></div>
</div>
<div class="recipe-card cat-gas-purification" markdown>
<div class="rc-out">:ci[gas_helium|1]</div>
<div class="rc-flow">:ci[crude_helium|2] <span class="rc-arrow">→</span> :ci[gas_helium|1]</div>
<div class="rc-meta"><span class="rc-stn">Helium PSA Purifier</span> <span class="rc-time">90s</span> <span class="rc-tier">T5</span> <span class="rc-energy">130 kJ</span></div>
<div class="rc-note">Polish crude helium to 99.999% by pressure-swing adsorption and a final cold trap. Some is lost to the tails -- helium is too fugitive to chase the last fraction of a percent cheaply.</div>
<div class="rc-id"><code>ng_purify_helium</code></div>
</div>
<div class="recipe-card cat-shift" markdown>
<div class="rc-out">:ci[gas_hydrogen|4] :ci[gas_co2|1]</div>
<div class="rc-flow">:ci[gas_syngas|3] :ci[water_raw|1] <span class="rc-arrow">→</span> :ci[gas_hydrogen|4] :ci[gas_co2|1]</div>
<div class="rc-meta"><span class="rc-stn">Steam-Methane Reformer</span> <span class="rc-time">70s</span> <span class="rc-tier">T4</span> <span class="rc-energy">110 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Water-gas shift: CO + H2O -> CO2 + H2. Convert the carbon monoxide in syngas into still more hydrogen, leaving CO2 to vent or capture. This is the cheap bulk-hydrogen route most ammonia and refining actually run on.</div>
<div class="rc-id"><code>smr_water_gas_shift</code></div>
</div>
<div class="recipe-card cat-gas-treating" markdown>
<div class="rc-out">:ci[gas_methane|2] :ci[gas_co2|1] :ci[gas_hydrogen_sulfide|1]</div>
<div class="rc-flow">:ci[natural_gas_raw|3] <span class="rc-arrow">→</span> :ci[gas_methane|2] :ci[gas_co2|1] :ci[gas_hydrogen_sulfide|1]</div>
<div class="rc-meta"><span class="rc-stn">Amine Gas-Sweetening Unit</span> <span class="rc-time">70s</span> <span class="rc-tier">T4</span> <span class="rc-energy">90 kJ</span> <span class="rc-bp">+2 byproducts</span></div>
<div class="rc-note">Wash the raw gas with an amine solution to strip the acid gases: out comes sweet pipeline methane, plus the CO2 and hydrogen sulfide that each have to be dealt with separately.</div>
<div class="rc-id"><code>ng_amine_sweeten</code></div>
</div>
<div class="recipe-card cat-combustion" markdown>
<div class="rc-out">:ci[gas_so2|2]</div>
<div class="rc-flow">:ci[sulfur_recovered|2] :ci[gas_oxygen|2] <span class="rc-arrow">→</span> :ci[gas_so2|2]</div>
<div class="rc-meta"><span class="rc-stn">Sulfur Burner / Pyrite Roaster</span> <span class="rc-time">40s</span> <span class="rc-tier">T4</span> <span class="rc-energy">60 kJ</span></div>
<div class="rc-note">Burn recovered sulfur in air: S + O2 -> SO2. A cleaner SO2 feed for the contact sulfuric-acid plant than roasting pyrite -- and, in the real world, the dominant modern route to acid.</div>
<div class="rc-id"><code>ng_burn_sulfur</code></div>
</div>
<div class="recipe-card cat-reforming" markdown>
<div class="rc-out">:ci[gas_syngas|3]</div>
<div class="rc-flow">:ci[gas_methane|1] :ci[water_raw|2] <span class="rc-arrow">→</span> :ci[gas_syngas|3]</div>
<div class="rc-meta"><span class="rc-stn">Steam-Methane Reformer</span> <span class="rc-time">90s</span> <span class="rc-tier">T4</span> <span class="rc-energy">160 kJ</span></div>
<div class="rc-note">Steam-methane reforming: CH4 + H2O -> CO + 3 H2 over a nickel catalyst at red heat. The workhorse first step of industrial hydrogen, turning methane and steam into synthesis gas.</div>
<div class="rc-id"><code>smr_steam_reform</code></div>
</div>
<div class="recipe-card cat-extraction" markdown>
<div class="rc-out">:ci[natural_gas_raw|2]</div>
<div class="rc-meta"><span class="rc-stn">Natural-Gas Well & Derrick</span> <span class="rc-time">60s</span> <span class="rc-tier">T4</span> <span class="rc-energy">40 kJ</span></div>
<div class="rc-note">Drill a gas well and bring sour natural gas up the derrick. What comes up is mostly methane, with CO2, hydrogen sulfide and -- in helium-rich fields -- a trace of helium along for the ride.</div>
<div class="rc-id"><code>ng_gather_natural_gas</code></div>
</div>
<div class="recipe-card cat-sulfur-recovery" markdown>
<div class="rc-out">:ci[sulfur_recovered|3] :ci[water_raw|2]</div>
<div class="rc-flow">:ci[gas_hydrogen_sulfide|3] :ci[gas_oxygen|1] <span class="rc-arrow">→</span> :ci[sulfur_recovered|3] :ci[water_raw|2]</div>
<div class="rc-meta"><span class="rc-stn">Claus Sulfur-Recovery Unit</span> <span class="rc-time">80s</span> <span class="rc-tier">T4</span> <span class="rc-energy">110 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Run the toxic H2S through a Claus unit: 2 H2S + O2 -> 2 S + 2 H2O. A hazard becomes a product -- this is where most of the world's sulfur actually comes from.</div>
<div class="rc-id"><code>ng_claus_sulfur</code></div>
</div>
</div>

## Nickel Sulfide chain
<p class="chapter-stats">5 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_pentlandite["<img src='/Conduvia/assets/icons/raw_ore_pentlandite.png' class='mmd-ico' />raw pentlandite ore"]
  i_nickel_concentrate["<img src='/Conduvia/assets/icons/nickel_concentrate.png' class='mmd-ico' />nickel concentrate"]
  i_waste_tailings["<img src='/Conduvia/assets/icons/waste_tailings.png' class='mmd-ico' />tailings"]
  i_raw_ore_silica["<img src='/Conduvia/assets/icons/raw_ore_silica.png' class='mmd-ico' />raw silica ore"]
  i_gas_oxygen["<img src='/Conduvia/assets/icons/gas_oxygen.png' class='mmd-ico' />oxygen gas"]
  i_nickel_matte["<img src='/Conduvia/assets/icons/nickel_matte.png' class='mmd-ico' />nickel furnace matte"]
  i_slag["<img src='/Conduvia/assets/icons/slag.png' class='mmd-ico' />slag"]
  i_gas_so2["<img src='/Conduvia/assets/icons/gas_so2.png' class='mmd-ico' />sulfur dioxide gas"]
  i_nickel_converter_matte["<img src='/Conduvia/assets/icons/nickel_converter_matte.png' class='mmd-ico' />nickel converter matte (Ni3S2)"]
  i_nickel_oxide_sinter["<img src='/Conduvia/assets/icons/nickel_oxide_sinter.png' class='mmd-ico' />nickel oxide sinter"]
  i_dc_charge["<img src='/Conduvia/assets/icons/dc_charge.png' class='mmd-ico' />DC power charge"]
  i_nickel_cathode["<img src='/Conduvia/assets/icons/nickel_cathode.png' class='mmd-ico' />nickel cathode"]
  p_nis_froth_flotation{"Froth Flotation Cell"}
  p_nis_flash_smelt{"Flash Smelting Furnace (autogenous, O2-enriched)"}
  p_nis_converter{"Copper Converter (Peirce-Smith)"}
  p_nis_roast_matte{"Roasting Pit"}
  p_nis_electrowin{"Electrowinning Cell (Pb anode / SS cathode)"}
  i_raw_ore_pentlandite --> |"x3"| p_nis_froth_flotation
  p_nis_froth_flotation --> |"x2"| i_nickel_concentrate
  p_nis_froth_flotation --> |"x1"| i_waste_tailings
  i_nickel_concentrate --> |"x2"| p_nis_flash_smelt
  i_raw_ore_silica --> |"x1"| p_nis_flash_smelt
  i_gas_oxygen --> |"x1"| p_nis_flash_smelt
  p_nis_flash_smelt --> |"x1"| i_nickel_matte
  p_nis_flash_smelt --> |"x1"| i_slag
  p_nis_flash_smelt --> |"x1"| i_gas_so2
  i_nickel_matte --> |"x2"| p_nis_converter
  i_gas_oxygen --> |"x1"| p_nis_converter
  p_nis_converter --> |"x1"| i_nickel_converter_matte
  p_nis_converter --> |"x1"| i_slag
  p_nis_converter --> |"x1"| i_gas_so2
  i_nickel_converter_matte --> |"x1"| p_nis_roast_matte
  i_gas_oxygen --> |"x1"| p_nis_roast_matte
  p_nis_roast_matte --> |"x1"| i_nickel_oxide_sinter
  p_nis_roast_matte --> |"x1"| i_gas_so2
  i_nickel_oxide_sinter --> |"x1"| p_nis_electrowin
  i_dc_charge --> |"x2"| p_nis_electrowin
  p_nis_electrowin --> |"x1"| i_nickel_cathode
  p_nis_electrowin --> |"x1"| i_slag
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_nis_froth_flotation proc;
  class p_nis_flash_smelt proc;
  class p_nis_converter proc;
  class p_nis_roast_matte proc;
  class p_nis_electrowin proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-electrowinning" markdown>
<div class="rc-out">:ci[nickel_cathode|1] :ci[slag|1]</div>
<div class="rc-flow">:ci[nickel_oxide_sinter|1] :ci[dc_charge|2] <span class="rc-arrow">→</span> :ci[nickel_cathode|1] :ci[slag|1]</div>
<div class="rc-meta"><span class="rc-stn">Electrowinning Cell (Pb anode / SS cathode)</span> <span class="rc-time">120s</span> <span class="rc-tier">T4</span> <span class="rc-energy">200 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Dissolve and electrowin the nickel oxide onto starter sheets: pure nickel cathode plates out, gangue drops as anode slag. The same cathode the laterite route eventually reaches -- and the feed for Inconel.</div>
<div class="rc-id"><code>nis_electrowin</code></div>
</div>
<div class="recipe-card cat-beneficiation" markdown>
<div class="rc-out">:ci[nickel_concentrate|2] :ci[waste_tailings|1]</div>
<div class="rc-flow">:ci[raw_ore_pentlandite|3] <span class="rc-arrow">→</span> :ci[nickel_concentrate|2] :ci[waste_tailings|1]</div>
<div class="rc-meta"><span class="rc-stn">Froth Flotation Cell</span> <span class="rc-time">70s</span> <span class="rc-tier">T2</span> <span class="rc-energy">50 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Grind and float pentlandite: sulfide grains ride the froth while silicate gangue sinks, upgrading the ore into a nickel sulfide concentrate before any heat is spent.</div>
<div class="rc-id"><code>nis_froth_flotation</code></div>
</div>
<div class="recipe-card cat-converting" markdown>
<div class="rc-out">:ci[nickel_converter_matte|1] :ci[slag|1] :ci[gas_so2|1]</div>
<div class="rc-flow">:ci[nickel_matte|2] :ci[gas_oxygen|1] <span class="rc-arrow">→</span> :ci[nickel_converter_matte|1] :ci[slag|1] :ci[gas_so2|1]</div>
<div class="rc-meta"><span class="rc-stn">Copper Converter (Peirce-Smith)</span> <span class="rc-time">100s</span> <span class="rc-tier">T3</span> <span class="rc-energy">120 kJ</span> <span class="rc-bp">+2 byproducts</span></div>
<div class="rc-note">Blow air/oxygen through the molten matte in a Peirce-Smith converter to oxidise out the remaining iron (slagged with silica), leaving high-grade Ni3S2 converter matte and more SO2 for the acid plant.</div>
<div class="rc-id"><code>nis_converter</code></div>
</div>
<div class="recipe-card cat-smelting" markdown>
<div class="rc-out">:ci[nickel_matte|1] :ci[slag|1] :ci[gas_so2|1]</div>
<div class="rc-flow">:ci[nickel_concentrate|2] :ci[raw_ore_silica|1] :ci[gas_oxygen|1] <span class="rc-arrow">→</span> :ci[nickel_matte|1] :ci[slag|1] :ci[gas_so2|1]</div>
<div class="rc-meta"><span class="rc-stn">Flash Smelting Furnace (autogenous, O2-enriched)</span> <span class="rc-time">110s</span> <span class="rc-tier">T3</span> <span class="rc-energy">140 kJ</span> <span class="rc-bp">+2 byproducts</span></div>
<div class="rc-note">Flash-smelt the concentrate in an oxygen-enriched blast: the sulfide burns its own fuel (autogenous), iron slags off with silica flux, and the sulfur leaves as SO2 -- piped straight to the contact acid plant. The molten matte is tapped below.</div>
<div class="rc-id"><code>nis_flash_smelt</code></div>
</div>
<div class="recipe-card cat-roasting" markdown>
<div class="rc-out">:ci[nickel_oxide_sinter|1] :ci[gas_so2|1]</div>
<div class="rc-flow">:ci[nickel_converter_matte|1] :ci[gas_oxygen|1] <span class="rc-arrow">→</span> :ci[nickel_oxide_sinter|1] :ci[gas_so2|1]</div>
<div class="rc-meta"><span class="rc-stn">Roasting Pit</span> <span class="rc-time">90s</span> <span class="rc-tier">T3</span> <span class="rc-energy">90 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Dead-roast the converter matte to nickel oxide, driving off the last sulfur as SO2. Three SO2 streams from one metal -- sulfide nickel, like sulfide copper, always comes with an acid plant attached.</div>
<div class="rc-id"><code>nis_roast_matte</code></div>
</div>
</div>

## Potash chain
<p class="chapter-stats">3 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_sylvite["<img src='/Conduvia/assets/icons/raw_ore_sylvite.png' class='mmd-ico' />raw sylvite ore"]
  i_potash_muriate["<img src='/Conduvia/assets/icons/potash_muriate.png' class='mmd-ico' />muriate of potash (KCl)"]
  i_salt["<img src='/Conduvia/assets/icons/salt.png' class='mmd-ico' />salt lick"]
  i_acid_sulfuric["<img src='/Conduvia/assets/icons/acid_sulfuric.png' class='mmd-ico' />sulfuric acid"]
  i_potash_sulfate["<img src='/Conduvia/assets/icons/potash_sulfate.png' class='mmd-ico' />sulfate of potash (K2SO4)"]
  i_gas_hcl["<img src='/Conduvia/assets/icons/gas_hcl.png' class='mmd-ico' />hydrochloric acid gas"]
  i_water_raw["<img src='/Conduvia/assets/icons/water_raw.png' class='mmd-ico' />raw water"]
  i_dc_charge["<img src='/Conduvia/assets/icons/dc_charge.png' class='mmd-ico' />DC power charge"]
  i_potassium_hydroxide["<img src='/Conduvia/assets/icons/potassium_hydroxide.png' class='mmd-ico' />caustic potash (KOH)"]
  i_gas_chlorine["<img src='/Conduvia/assets/icons/gas_chlorine.png' class='mmd-ico' />chlorine gas"]
  i_gas_hydrogen["<img src='/Conduvia/assets/icons/gas_hydrogen.png' class='mmd-ico' />hydrogen gas"]
  p_k_froth_flotation{"Froth Flotation Cell"}
  p_k_mannheim_sop{"Mannheim Muffle Furnace"}
  p_k_membrane_koh{"Chlor-Alkali Membrane Cell"}
  i_raw_ore_sylvite --> |"x3"| p_k_froth_flotation
  p_k_froth_flotation --> |"x2"| i_potash_muriate
  p_k_froth_flotation --> |"x1"| i_salt
  i_potash_muriate --> |"x2"| p_k_mannheim_sop
  i_acid_sulfuric --> |"x1"| p_k_mannheim_sop
  p_k_mannheim_sop --> |"x2"| i_potash_sulfate
  p_k_mannheim_sop --> |"x1"| i_gas_hcl
  i_potash_muriate --> |"x2"| p_k_membrane_koh
  i_water_raw --> |"x2"| p_k_membrane_koh
  i_dc_charge --> |"x2"| p_k_membrane_koh
  p_k_membrane_koh --> |"x2"| i_potassium_hydroxide
  p_k_membrane_koh --> |"x1"| i_gas_chlorine
  p_k_membrane_koh --> |"x1"| i_gas_hydrogen
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_k_froth_flotation proc;
  class p_k_mannheim_sop proc;
  class p_k_membrane_koh proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-beneficiation" markdown>
<div class="rc-out">:ci[potash_muriate|2] :ci[salt|1]</div>
<div class="rc-flow">:ci[raw_ore_sylvite|3] <span class="rc-arrow">→</span> :ci[potash_muriate|2] :ci[salt|1]</div>
<div class="rc-meta"><span class="rc-stn">Froth Flotation Cell</span> <span class="rc-time">80s</span> <span class="rc-tier">T3</span> <span class="rc-energy">55 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Float sylvinite with an amine collector: the KCl rides the froth as muriate of potash while the common salt (NaCl) sinks and is recovered as a salable byproduct rather than waste.</div>
<div class="rc-id"><code>k_froth_flotation</code></div>
</div>
<div class="recipe-card cat-metathesis" markdown>
<div class="rc-out">:ci[potash_sulfate|2] :ci[gas_hcl|1]</div>
<div class="rc-flow">:ci[potash_muriate|2] :ci[acid_sulfuric|1] <span class="rc-arrow">→</span> :ci[potash_sulfate|2] :ci[gas_hcl|1]</div>
<div class="rc-meta"><span class="rc-stn">Mannheim Muffle Furnace</span> <span class="rc-time">180s</span> <span class="rc-tier">T4</span> <span class="rc-energy">170 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Mannheim process: react KCl with sulfuric acid in a heated muffle -- 2 KCl + H2SO4 -> K2SO4 + 2 HCl. Yields chloride-free sulfate of potash and drives off hydrogen chloride gas as a genuine co-product.</div>
<div class="rc-id"><code>k_mannheim_sop</code></div>
</div>
<div class="recipe-card cat-electrolysis" markdown>
<div class="rc-out">:ci[potassium_hydroxide|2] :ci[gas_chlorine|1] :ci[gas_hydrogen|1]</div>
<div class="rc-flow">:ci[potash_muriate|2] :ci[water_raw|2] :ci[dc_charge|2] <span class="rc-arrow">→</span> :ci[potassium_hydroxide|2] :ci[gas_chlorine|1] :ci[gas_hydrogen|1]</div>
<div class="rc-meta"><span class="rc-stn">Chlor-Alkali Membrane Cell</span> <span class="rc-time">160s</span> <span class="rc-tier">T4</span> <span class="rc-energy">420 kJ</span> <span class="rc-bp">+2 byproducts</span></div>
<div class="rc-note">Electrolyse a KCl brine in a membrane cell -- the potassium analogue of chlor-alkali: caustic potash at the cathode, chlorine at the anode, hydrogen alongside.</div>
<div class="rc-id"><code>k_membrane_koh</code></div>
</div>
</div>

## Silicon chain
<p class="chapter-stats">7 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_silica["<img src='/Conduvia/assets/icons/raw_ore_silica.png' class='mmd-ico' />raw silica ore"]
  i_coke_fuel["<img src='/Conduvia/assets/icons/coke_fuel.png' class='mmd-ico' />coke fuel"]
  i_silicon_mg_grade["<img src='/Conduvia/assets/icons/silicon_mg_grade.png' class='mmd-ico' />metallurgical-grade silicon"]
  i_gas_co2["<img src='/Conduvia/assets/icons/gas_co2.png' class='mmd-ico' />carbon dioxide gas"]
  i_gas_hcl["<img src='/Conduvia/assets/icons/gas_hcl.png' class='mmd-ico' />hydrochloric acid gas"]
  i_trichlorosilane["<img src='/Conduvia/assets/icons/trichlorosilane.png' class='mmd-ico' />trichlorosilane"]
  i_gas_hydrogen["<img src='/Conduvia/assets/icons/gas_hydrogen.png' class='mmd-ico' />hydrogen gas"]
  i_silicon_tetrachloride["<img src='/Conduvia/assets/icons/silicon_tetrachloride.png' class='mmd-ico' />silicon tetrachloride"]
  i_polysilicon_9n["<img src='/Conduvia/assets/icons/polysilicon_9n.png' class='mmd-ico' />electronic-grade polysilicon"]
  i_silicon_ingot_czochralski["<img src='/Conduvia/assets/icons/silicon_ingot_czochralski.png' class='mmd-ico' />Czochralski silicon ingot"]
  i_silicon_wafer_raw["<img src='/Conduvia/assets/icons/silicon_wafer_raw.png' class='mmd-ico' />raw silicon wafer"]
  i_silicon_wafer_polished["<img src='/Conduvia/assets/icons/silicon_wafer_polished.png' class='mmd-ico' />polished silicon wafer"]
  p_si_carbothermic_silicon{"Submerged-Arc Furnace (SAF)"}
  p_si_make_trichlorosilane{"Fluidised-Bed Chlorinator"}
  p_si_redistribute_sicl4{"Fluidised-Bed Chlorinator"}
  p_si_siemens_polysilicon{"Siemens CVD Reactor (polysilicon deposition)"}
  p_si_czochralski_ingot{"Czochralski Crystal Puller"}
  p_si_slice_wafer{"Wafer Slicing & Polishing Line"}
  p_si_polish_wafer{"Wafer Slicing & Polishing Line"}
  i_raw_ore_silica --> |"x2"| p_si_carbothermic_silicon
  i_coke_fuel --> |"x2"| p_si_carbothermic_silicon
  p_si_carbothermic_silicon --> |"x1"| i_silicon_mg_grade
  p_si_carbothermic_silicon --> |"x2"| i_gas_co2
  i_silicon_mg_grade --> |"x1"| p_si_make_trichlorosilane
  i_gas_hcl --> |"x3"| p_si_make_trichlorosilane
  p_si_make_trichlorosilane --> |"x1"| i_trichlorosilane
  p_si_make_trichlorosilane --> |"x1"| i_gas_hydrogen
  i_silicon_tetrachloride --> |"x3"| p_si_redistribute_sicl4
  i_silicon_mg_grade --> |"x1"| p_si_redistribute_sicl4
  i_gas_hydrogen --> |"x2"| p_si_redistribute_sicl4
  p_si_redistribute_sicl4 --> |"x4"| i_trichlorosilane
  i_trichlorosilane --> |"x3"| p_si_siemens_polysilicon
  i_gas_hydrogen --> |"x2"| p_si_siemens_polysilicon
  p_si_siemens_polysilicon --> |"x1"| i_polysilicon_9n
  p_si_siemens_polysilicon --> |"x3"| i_gas_hcl
  p_si_siemens_polysilicon --> |"x1"| i_silicon_tetrachloride
  i_polysilicon_9n --> |"x4"| p_si_czochralski_ingot
  p_si_czochralski_ingot --> |"x1"| i_silicon_ingot_czochralski
  i_silicon_ingot_czochralski --> |"x1"| p_si_slice_wafer
  p_si_slice_wafer --> |"x8"| i_silicon_wafer_raw
  i_silicon_wafer_raw --> |"x1"| p_si_polish_wafer
  p_si_polish_wafer --> |"x1"| i_silicon_wafer_polished
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_si_carbothermic_silicon proc;
  class p_si_make_trichlorosilane proc;
  class p_si_redistribute_sicl4 proc;
  class p_si_siemens_polysilicon proc;
  class p_si_czochralski_ingot proc;
  class p_si_slice_wafer proc;
  class p_si_polish_wafer proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-deposition" markdown>
<div class="rc-out">:ci[polysilicon_9n|1] :ci[gas_hcl|3] :ci[silicon_tetrachloride|1]</div>
<div class="rc-flow">:ci[trichlorosilane|3] :ci[gas_hydrogen|2] <span class="rc-arrow">→</span> :ci[polysilicon_9n|1] :ci[gas_hcl|3] :ci[silicon_tetrachloride|1]</div>
<div class="rc-meta"><span class="rc-stn">Siemens CVD Reactor (polysilicon deposition)</span> <span class="rc-time">200s</span> <span class="rc-tier">T4</span> <span class="rc-energy">380 kJ</span> <span class="rc-bp">+2 byproducts</span></div>
<div class="rc-note">The Siemens process: pass trichlorosilane and hydrogen over glowing silicon rods so hyper-pure silicon deposits atom by atom (SiHCl3 + H2 -> Si + 3 HCl). Recovers HCl for the chlorinator and sheds SiCl4 for redistribution. The single most energy-hungry step in all of electronics.</div>
<div class="rc-id"><code>si_siemens_polysilicon</code></div>
</div>
<div class="recipe-card cat-crystal-growth" markdown>
<div class="rc-out">:ci[silicon_ingot_czochralski|1]</div>
<div class="rc-flow">:ci[polysilicon_9n|4] <span class="rc-arrow">→</span> :ci[silicon_ingot_czochralski|1]</div>
<div class="rc-meta"><span class="rc-stn">Czochralski Crystal Puller</span> <span class="rc-time">180s</span> <span class="rc-tier">T4</span> <span class="rc-energy">300 kJ</span></div>
<div class="rc-note">Melt the polysilicon and pull a single crystal: dip a seed into the melt and draw it slowly upward while rotating, so one continuous, flawless lattice grows from the bath. The whole ingot is one crystal.</div>
<div class="rc-id"><code>si_czochralski_ingot</code></div>
</div>
<div class="recipe-card cat-smelting" markdown>
<div class="rc-out">:ci[silicon_mg_grade|1] :ci[gas_co2|2]</div>
<div class="rc-flow">:ci[raw_ore_silica|2] :ci[coke_fuel|2] <span class="rc-arrow">→</span> :ci[silicon_mg_grade|1] :ci[gas_co2|2]</div>
<div class="rc-meta"><span class="rc-stn">Submerged-Arc Furnace (SAF)</span> <span class="rc-time">120s</span> <span class="rc-tier">T3</span> <span class="rc-energy">260 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Reduce quartz with carbon in a submerged-arc furnace at ~1900C: SiO2 + 2 C -> Si + 2 CO. Brutally energy-hungry (~11 kWh/kg), and the product is still only ~98% silicon -- metallurgical grade, good for alloys but far too dirty for chips.</div>
<div class="rc-id"><code>si_carbothermic_silicon</code></div>
</div>
<div class="recipe-card cat-finishing" markdown>
<div class="rc-out">:ci[silicon_wafer_polished|1]</div>
<div class="rc-flow">:ci[silicon_wafer_raw|1] <span class="rc-arrow">→</span> :ci[silicon_wafer_polished|1]</div>
<div class="rc-meta"><span class="rc-stn">Wafer Slicing & Polishing Line</span> <span class="rc-time">50s</span> <span class="rc-tier">T4</span> <span class="rc-energy">70 kJ</span></div>
<div class="rc-note">Chemically-mechanically polish (CMP) an as-cut wafer to an atomically smooth, defect-free mirror -- the pristine substrate fine logic circuits demand.</div>
<div class="rc-id"><code>si_polish_wafer</code></div>
</div>
<div class="recipe-card cat-machining" markdown>
<div class="rc-out">:ci[silicon_wafer_raw|8]</div>
<div class="rc-flow">:ci[silicon_ingot_czochralski|1] <span class="rc-arrow">→</span> :ci[silicon_wafer_raw|8]</div>
<div class="rc-meta"><span class="rc-stn">Wafer Slicing & Polishing Line</span> <span class="rc-time">60s</span> <span class="rc-tier">T4</span> <span class="rc-energy">80 kJ</span></div>
<div class="rc-note">Slice the monocrystal ingot into thin wafers with a wire saw and lap them flat. As-cut wafers are matte and saw-damaged -- ready for rugged devices or for polishing.</div>
<div class="rc-id"><code>si_slice_wafer</code></div>
</div>
<div class="recipe-card cat-chlorination" markdown>
<div class="rc-out">:ci[trichlorosilane|1] :ci[gas_hydrogen|1]</div>
<div class="rc-flow">:ci[silicon_mg_grade|1] :ci[gas_hcl|3] <span class="rc-arrow">→</span> :ci[trichlorosilane|1] :ci[gas_hydrogen|1]</div>
<div class="rc-meta"><span class="rc-stn">Fluidised-Bed Chlorinator</span> <span class="rc-time">70s</span> <span class="rc-tier">T4</span> <span class="rc-energy">90 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Hydrochlorinate metallurgical silicon in a fluidised bed: Si + 3 HCl -> SiHCl3 + H2. The point is to turn solid silicon into a volatile liquid that can be fractionally distilled to a purity no solid could ever reach.</div>
<div class="rc-id"><code>si_make_trichlorosilane</code></div>
</div>
<div class="recipe-card cat-chlorination" markdown>
<div class="rc-out">:ci[trichlorosilane|4]</div>
<div class="rc-flow">:ci[silicon_tetrachloride|3] :ci[silicon_mg_grade|1] :ci[gas_hydrogen|2] <span class="rc-arrow">→</span> :ci[trichlorosilane|4]</div>
<div class="rc-meta"><span class="rc-stn">Fluidised-Bed Chlorinator</span> <span class="rc-time">80s</span> <span class="rc-tier">T4</span> <span class="rc-energy">110 kJ</span></div>
<div class="rc-note">Redistribute silicon tetrachloride back into useful trichlorosilane: 3 SiCl4 + Si + 2 H2 -> 4 SiHCl3. This recycles the SiCl4 thrown off by the Siemens reactor (and consumes the zirconium plant's chlorinator byproduct) instead of dumping it.</div>
<div class="rc-id"><code>si_redistribute_sicl4</code></div>
</div>
</div>

## Sulfuric Acid chain
<p class="chapter-stats">6 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_pyrite["<img src='/Conduvia/assets/icons/raw_ore_pyrite.png' class='mmd-ico' />raw pyrite ore"]
  i_gas_so2["<img src='/Conduvia/assets/icons/gas_so2.png' class='mmd-ico' />sulfur dioxide gas"]
  i_roasted_ore_hematite["<img src='/Conduvia/assets/icons/roasted_ore_hematite.png' class='mmd-ico' />roasted hematite"]
  i_gas_so3["<img src='/Conduvia/assets/icons/gas_so3.png' class='mmd-ico' />sulfur trioxide gas"]
  i_water_raw["<img src='/Conduvia/assets/icons/water_raw.png' class='mmd-ico' />raw water"]
  i_oleum["<img src='/Conduvia/assets/icons/oleum.png' class='mmd-ico' />oleum (fuming sulfuric acid)"]
  i_acid_sulfuric["<img src='/Conduvia/assets/icons/acid_sulfuric.png' class='mmd-ico' />sulfuric acid"]
  i_acid_sulfuric_dilute["<img src='/Conduvia/assets/icons/acid_sulfuric_dilute.png' class='mmd-ico' />chamber acid (dilute H2SO4)"]
  p_acid_roast_pyrite{"Sulfur Burner / Pyrite Roaster"}
  p_acid_so2_to_so3{"Contact Converter (V2O5 beds, DCDA)"}
  p_acid_form_oleum{"Oleum Absorption Tower"}
  p_acid_dilute_oleum{"Oleum Absorption Tower"}
  p_acid_lead_chamber{"Lead Chamber (NOx)"}
  p_acid_concentrate_chamber{"Lead Chamber (NOx)"}
  i_raw_ore_pyrite --> |"x4"| p_acid_roast_pyrite
  p_acid_roast_pyrite --> |"x6"| i_gas_so2
  p_acid_roast_pyrite --> |"x2"| i_roasted_ore_hematite
  i_gas_so2 --> |"x2"| p_acid_so2_to_so3
  p_acid_so2_to_so3 --> |"x2"| i_gas_so3
  i_gas_so3 --> |"x3"| p_acid_form_oleum
  i_water_raw --> |"x1"| p_acid_form_oleum
  p_acid_form_oleum --> |"x2"| i_oleum
  i_oleum --> |"x2"| p_acid_dilute_oleum
  i_water_raw --> |"x1"| p_acid_dilute_oleum
  p_acid_dilute_oleum --> |"x3"| i_acid_sulfuric
  i_gas_so2 --> |"x3"| p_acid_lead_chamber
  i_water_raw --> |"x1"| p_acid_lead_chamber
  p_acid_lead_chamber --> |"x2"| i_acid_sulfuric_dilute
  i_acid_sulfuric_dilute --> |"x2"| p_acid_concentrate_chamber
  p_acid_concentrate_chamber --> |"x1"| i_acid_sulfuric
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_acid_roast_pyrite proc;
  class p_acid_so2_to_so3 proc;
  class p_acid_form_oleum proc;
  class p_acid_dilute_oleum proc;
  class p_acid_lead_chamber proc;
  class p_acid_concentrate_chamber proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-chemistry" markdown>
<div class="rc-out">:ci[acid_sulfuric|3]</div>
<div class="rc-flow">:ci[oleum|2] :ci[water_raw|1] <span class="rc-arrow">→</span> :ci[acid_sulfuric|3]</div>
<div class="rc-meta"><span class="rc-stn">Oleum Absorption Tower</span> <span class="rc-time">20s</span> <span class="rc-tier">T4</span> <span class="rc-energy">12 kJ</span></div>
<div class="rc-note">Bleed oleum down with a metered water add: H2S2O7 + H2O -> 2 H2SO4. Yields concentrated ~98% acid; part is drawn off as product, part recycled back to the absorption tower.</div>
<div class="rc-id"><code>acid_dilute_oleum</code></div>
</div>
<div class="recipe-card cat-chemistry" markdown>
<div class="rc-out">:ci[acid_sulfuric|1]</div>
<div class="rc-flow">:ci[acid_sulfuric_dilute|2] <span class="rc-arrow">→</span> :ci[acid_sulfuric|1]</div>
<div class="rc-meta"><span class="rc-stn">Lead Chamber (NOx)</span> <span class="rc-time">35s</span> <span class="rc-tier">T3</span> <span class="rc-energy">25 kJ</span></div>
<div class="rc-note">Boil chamber acid up in the Glover tower to drive off water and lift it toward concentrated strength. Tier-3 path to H2SO4 before the vanadium contact plant is available.</div>
<div class="rc-id"><code>acid_concentrate_chamber</code></div>
</div>
<div class="recipe-card cat-chemistry" markdown>
<div class="rc-out">:ci[acid_sulfuric_dilute|2]</div>
<div class="rc-flow">:ci[gas_so2|3] :ci[water_raw|1] <span class="rc-arrow">→</span> :ci[acid_sulfuric_dilute|2]</div>
<div class="rc-meta"><span class="rc-stn">Lead Chamber (NOx)</span> <span class="rc-time">40s</span> <span class="rc-tier">T3</span> <span class="rc-energy">15 kJ</span></div>
<div class="rc-note">The pre-Contact route (Roebuck, 1746): SO2 oxidised by moist air with recycled nitrogen oxides (NOx) as catalyst inside lead-lined chambers. Cheap and robust but caps out near 65-78% acid. NOx is recovered in the Gay-Lussac/Glover towers and reused.</div>
<div class="rc-id"><code>acid_lead_chamber</code></div>
</div>
<div class="recipe-card cat-roaster" markdown>
<div class="rc-out">:ci[gas_so2|6] :ci[roasted_ore_hematite|2]</div>
<div class="rc-flow">:ci[raw_ore_pyrite|4] <span class="rc-arrow">→</span> :ci[gas_so2|6] :ci[roasted_ore_hematite|2]</div>
<div class="rc-meta"><span class="rc-stn">Sulfur Burner / Pyrite Roaster</span> <span class="rc-time">50s</span> <span class="rc-tier">T2</span> <span class="rc-energy">40 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Dead-roast pyrite in excess air: 4 FeS2 + 11 O2 -> 2 Fe2O3 + 8 SO2. Drives off the SO2 acid feed AND leaves an iron-oxide cinder -- the same roasted hematite the iron chain smelts. One of the oldest acid feedstocks; the other is captured copper-smelter SO2.</div>
<div class="rc-id"><code>acid_roast_pyrite</code></div>
</div>
<div class="recipe-card cat-chemistry" markdown>
<div class="rc-out">:ci[gas_so3|2]</div>
<div class="rc-flow">:ci[gas_so2|2] <span class="rc-arrow">→</span> :ci[gas_so3|2]</div>
<div class="rc-meta"><span class="rc-stn">Contact Converter (V2O5 beds, DCDA)</span> <span class="rc-time">30s</span> <span class="rc-tier">T4</span> <span class="rc-energy">60 kJ</span></div>
<div class="rc-note">Catalytic oxidation over vanadium(V) oxide beds: 2 SO2 + O2 <=> 2 SO3 (dH=-196 kJ/mol), ~450C and 1-2 atm. Exothermic + reversible, so heat is pulled between beds; double-contact/double-absorption (DCDA) pushes ~98%+ conversion and keeps SO2 stack emissions low.</div>
<div class="rc-id"><code>acid_so2_to_so3</code></div>
</div>
<div class="recipe-card cat-chemistry" markdown>
<div class="rc-out">:ci[oleum|2]</div>
<div class="rc-flow">:ci[gas_so3|3] :ci[water_raw|1] <span class="rc-arrow">→</span> :ci[oleum|2]</div>
<div class="rc-meta"><span class="rc-stn">Oleum Absorption Tower</span> <span class="rc-time">20s</span> <span class="rc-tier">T4</span> <span class="rc-energy">18 kJ</span></div>
<div class="rc-note">Absorb SO3 into circulating strong acid: SO3 + H2SO4 -> H2S2O7 (oleum). SO3 is never fed to water directly -- the hydration is so violent it forms a fog of acid mist that will not condense. Make-up water keeps the loop charged.</div>
<div class="rc-id"><code>acid_form_oleum</code></div>
</div>
</div>

## Zinc chain
<p class="chapter-stats">5 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_sphalerite["<img src='/Conduvia/assets/icons/raw_ore_sphalerite.png' class='mmd-ico' />raw sphalerite ore"]
  i_concentrate_sphalerite["<img src='/Conduvia/assets/icons/concentrate_sphalerite.png' class='mmd-ico' />sphalerite concentrate"]
  i_waste_tailings["<img src='/Conduvia/assets/icons/waste_tailings.png' class='mmd-ico' />tailings"]
  i_gas_oxygen["<img src='/Conduvia/assets/icons/gas_oxygen.png' class='mmd-ico' />oxygen gas"]
  i_zinc_calcine_oxide["<img src='/Conduvia/assets/icons/zinc_calcine_oxide.png' class='mmd-ico' />zinc oxide calcine"]
  i_gas_so2["<img src='/Conduvia/assets/icons/gas_so2.png' class='mmd-ico' />sulfur dioxide gas"]
  i_acid_sulfuric["<img src='/Conduvia/assets/icons/acid_sulfuric.png' class='mmd-ico' />sulfuric acid"]
  i_zinc_sulfate_solution["<img src='/Conduvia/assets/icons/zinc_sulfate_solution.png' class='mmd-ico' />zinc sulfate liquor"]
  i_dc_charge["<img src='/Conduvia/assets/icons/dc_charge.png' class='mmd-ico' />DC power charge"]
  i_metal_zinc_ingot["<img src='/Conduvia/assets/icons/metal_zinc_ingot.png' class='mmd-ico' />zinc ingot"]
  i_coke_fuel["<img src='/Conduvia/assets/icons/coke_fuel.png' class='mmd-ico' />coke fuel"]
  i_gas_co2["<img src='/Conduvia/assets/icons/gas_co2.png' class='mmd-ico' />carbon dioxide gas"]
  p_zn_froth_flotation{"Froth Flotation Cell"}
  p_zn_roast{"Roasting Pit"}
  p_zn_leach{"Heap Leach Pad (acid irrigation)"}
  p_zn_electrowin{"Electrowinning Cell (Pb anode / SS cathode)"}
  p_zn_retort_thermal{"Zinc Distillation Retort (thermal)"}
  i_raw_ore_sphalerite --> |"x3"| p_zn_froth_flotation
  p_zn_froth_flotation --> |"x2"| i_concentrate_sphalerite
  p_zn_froth_flotation --> |"x1"| i_waste_tailings
  i_concentrate_sphalerite --> |"x2"| p_zn_roast
  i_gas_oxygen --> |"x1"| p_zn_roast
  p_zn_roast --> |"x2"| i_zinc_calcine_oxide
  p_zn_roast --> |"x1"| i_gas_so2
  i_zinc_calcine_oxide --> |"x2"| p_zn_leach
  i_acid_sulfuric --> |"x2"| p_zn_leach
  p_zn_leach --> |"x2"| i_zinc_sulfate_solution
  p_zn_leach --> |"x1"| i_waste_tailings
  i_zinc_sulfate_solution --> |"x2"| p_zn_electrowin
  i_dc_charge --> |"x2"| p_zn_electrowin
  p_zn_electrowin --> |"x2"| i_metal_zinc_ingot
  p_zn_electrowin --> |"x1"| i_acid_sulfuric
  i_zinc_calcine_oxide --> |"x2"| p_zn_retort_thermal
  i_coke_fuel --> |"x2"| p_zn_retort_thermal
  p_zn_retort_thermal --> |"x2"| i_metal_zinc_ingot
  p_zn_retort_thermal --> |"x2"| i_gas_co2
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_zn_froth_flotation proc;
  class p_zn_roast proc;
  class p_zn_leach proc;
  class p_zn_electrowin proc;
  class p_zn_retort_thermal proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-beneficiation" markdown>
<div class="rc-out">:ci[concentrate_sphalerite|2] :ci[waste_tailings|1]</div>
<div class="rc-flow">:ci[raw_ore_sphalerite|3] <span class="rc-arrow">→</span> :ci[concentrate_sphalerite|2] :ci[waste_tailings|1]</div>
<div class="rc-meta"><span class="rc-stn">Froth Flotation Cell</span> <span class="rc-time">60s</span> <span class="rc-tier">T2</span> <span class="rc-energy">40 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Froth-float sphalerite to a zinc-sulfide concentrate, rejecting the silica gangue as tailings.</div>
<div class="rc-id"><code>zn_froth_flotation</code></div>
</div>
<div class="recipe-card cat-electrowinning" markdown>
<div class="rc-out">:ci[metal_zinc_ingot|2] :ci[acid_sulfuric|1]</div>
<div class="rc-flow">:ci[zinc_sulfate_solution|2] :ci[dc_charge|2] <span class="rc-arrow">→</span> :ci[metal_zinc_ingot|2] :ci[acid_sulfuric|1]</div>
<div class="rc-meta"><span class="rc-stn">Electrowinning Cell (Pb anode / SS cathode)</span> <span class="rc-time">150s</span> <span class="rc-tier">T4</span> <span class="rc-energy">380 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Electrowin zinc onto aluminium cathodes; the cell regenerates sulfuric acid that is piped straight back to the leach, closing the acid loop. Strip, melt and cast to ingot.</div>
<div class="rc-id"><code>zn_electrowin</code></div>
</div>
<div class="recipe-card cat-carbothermic-distillation" markdown>
<div class="rc-out">:ci[metal_zinc_ingot|2] :ci[gas_co2|2]</div>
<div class="rc-flow">:ci[zinc_calcine_oxide|2] :ci[coke_fuel|2] <span class="rc-arrow">→</span> :ci[metal_zinc_ingot|2] :ci[gas_co2|2]</div>
<div class="rc-meta"><span class="rc-stn">Zinc Distillation Retort (thermal)</span> <span class="rc-time">180s</span> <span class="rc-tier">T3</span> <span class="rc-energy">260 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">The old way: reduce the calcine with coke and distil the zinc off as vapour (zinc boils at 907 C), condensing it to metal. Energy-hungry but needs no electricity -- the historic and Imperial-Smelting route.</div>
<div class="rc-id"><code>zn_retort_thermal</code></div>
</div>
<div class="recipe-card cat-roasting" markdown>
<div class="rc-out">:ci[zinc_calcine_oxide|2] :ci[gas_so2|1]</div>
<div class="rc-flow">:ci[concentrate_sphalerite|2] :ci[gas_oxygen|1] <span class="rc-arrow">→</span> :ci[zinc_calcine_oxide|2] :ci[gas_so2|1]</div>
<div class="rc-meta"><span class="rc-stn">Roasting Pit</span> <span class="rc-time">110s</span> <span class="rc-tier">T3</span> <span class="rc-energy">120 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Roast the concentrate: ZnS burns to ZnO calcine, the sulfur leaving as SO2 for the contact acid plant. Both zinc routes start from this calcine.</div>
<div class="rc-id"><code>zn_roast</code></div>
</div>
<div class="recipe-card cat-leaching" markdown>
<div class="rc-out">:ci[zinc_sulfate_solution|2] :ci[waste_tailings|1]</div>
<div class="rc-flow">:ci[zinc_calcine_oxide|2] :ci[acid_sulfuric|2] <span class="rc-arrow">→</span> :ci[zinc_sulfate_solution|2] :ci[waste_tailings|1]</div>
<div class="rc-meta"><span class="rc-stn">Heap Leach Pad (acid irrigation)</span> <span class="rc-time">120s</span> <span class="rc-tier">T3</span> <span class="rc-energy">80 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Leach the calcine in sulfuric acid to a zinc sulfate liquor, leaving the iron-rich residue behind.</div>
<div class="rc-id"><code>zn_leach</code></div>
</div>
</div>
