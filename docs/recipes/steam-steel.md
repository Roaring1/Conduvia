# Tier 3–4 — Steam, Coke & Steel

<p class="chapter-stats">22 recipes</p>

## Electric power
<p class="chapter-stats">6 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_steam_charge["<img src='/Conduvia/assets/icons/steam_charge.png' class='mmd-ico' />steam charge"]
  i_dc_charge["<img src='/Conduvia/assets/icons/dc_charge.png' class='mmd-ico' />DC power charge"]
  i_ac_charge["<img src='/Conduvia/assets/icons/ac_charge.png' class='mmd-ico' />AC power charge"]
  p_e6_dynamo_dc_charge{"DC Workshop Dynamo"}
  p_e6_generator_ac_small_charge{"Small AC Generator"}
  p_e6_generator_three_phase_charge{"Three-Phase AC Generator"}
  p_e6_rectify_ac_to_dc{"Mercury Arc Rectifier"}
  p_e6_transformer_step_up{"Step-Up Transformer"}
  p_e6_transformer_step_down{"Step-Down Transformer"}
  i_steam_charge --> |"x1"| p_e6_dynamo_dc_charge
  p_e6_dynamo_dc_charge --> |"x1"| i_dc_charge
  i_steam_charge --> |"x1"| p_e6_generator_ac_small_charge
  p_e6_generator_ac_small_charge --> |"x1"| i_ac_charge
  i_steam_charge --> |"x1"| p_e6_generator_three_phase_charge
  p_e6_generator_three_phase_charge --> |"x3"| i_ac_charge
  i_ac_charge --> |"x3"| p_e6_rectify_ac_to_dc
  p_e6_rectify_ac_to_dc --> |"x2"| i_dc_charge
  i_ac_charge --> |"x1"| p_e6_transformer_step_up
  p_e6_transformer_step_up --> |"x2"| i_ac_charge
  i_ac_charge --> |"x2"| p_e6_transformer_step_down
  p_e6_transformer_step_down --> |"x1"| i_ac_charge
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_e6_dynamo_dc_charge proc;
  class p_e6_generator_ac_small_charge proc;
  class p_e6_generator_three_phase_charge proc;
  class p_e6_rectify_ac_to_dc proc;
  class p_e6_transformer_step_up proc;
  class p_e6_transformer_step_down proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-power" markdown>
<div class="rc-out">:ci[ac_charge|1]</div>
<div class="rc-flow">:ci[steam_charge|1] <span class="rc-arrow">→</span> :ci[ac_charge|1]</div>
<div class="rc-meta"><span class="rc-stn">Small AC Generator</span> <span class="rc-time">25.0s</span> <span class="rc-tier">T3</span></div>
<div class="rc-note">Slip rings instead of a commutator let the alternating current through unchanged. One steam charge per output cycle at single-phase workshop voltage.</div>
<div class="rc-id"><code>e6_generator_ac_small_charge</code></div>
</div>
<div class="recipe-card cat-power" markdown>
<div class="rc-out">:ci[ac_charge|3]</div>
<div class="rc-flow">:ci[steam_charge|1] <span class="rc-arrow">→</span> :ci[ac_charge|3]</div>
<div class="rc-meta"><span class="rc-stn">Three-Phase AC Generator</span> <span class="rc-time">25.0s</span> <span class="rc-tier">T3</span></div>
<div class="rc-note">Three-phase windings at 120° offset triple the power of a single-phase machine from the same prime-mover input. The three-phase output powers large AC induction motors and district distribution.</div>
<div class="rc-id"><code>e6_generator_three_phase_charge</code></div>
</div>
<div class="recipe-card cat-power" markdown>
<div class="rc-out">:ci[ac_charge|2]</div>
<div class="rc-flow">:ci[ac_charge|1] <span class="rc-arrow">→</span> :ci[ac_charge|2]</div>
<div class="rc-meta"><span class="rc-stn">Step-Up Transformer</span> <span class="rc-time">8.0s</span> <span class="rc-tier">T3</span></div>
<div class="rc-note">Iron-core transformer steps voltage up for long-distance transmission, doubling the effective charge throughput per cycle at the cost of matching step-down at the far end. AC-only -- DC has no transformer equivalent.</div>
<div class="rc-id"><code>e6_transformer_step_up</code></div>
</div>
<div class="recipe-card cat-power" markdown>
<div class="rc-out">:ci[ac_charge|1]</div>
<div class="rc-flow">:ci[ac_charge|2] <span class="rc-arrow">→</span> :ci[ac_charge|1]</div>
<div class="rc-meta"><span class="rc-stn">Step-Down Transformer</span> <span class="rc-time">8.0s</span> <span class="rc-tier">T3</span></div>
<div class="rc-note">Reduces high-voltage transmission AC back to working distribution voltage. Pair with step-up at the generator end.</div>
<div class="rc-id"><code>e6_transformer_step_down</code></div>
</div>
<div class="recipe-card cat-power" markdown>
<div class="rc-out">:ci[dc_charge|1]</div>
<div class="rc-flow">:ci[steam_charge|1] <span class="rc-arrow">→</span> :ci[dc_charge|1]</div>
<div class="rc-meta"><span class="rc-stn">DC Workshop Dynamo</span> <span class="rc-time">25.0s</span> <span class="rc-tier">T3</span></div>
<div class="rc-note">The dynamo's commutator and brushes rectify the armature's generated AC into smoothed DC. One steam charge (one engine cycle) drives one output charge.</div>
<div class="rc-id"><code>e6_dynamo_dc_charge</code></div>
</div>
<div class="recipe-card cat-power" markdown>
<div class="rc-out">:ci[dc_charge|2]</div>
<div class="rc-flow">:ci[ac_charge|3] <span class="rc-arrow">→</span> :ci[dc_charge|2]</div>
<div class="rc-meta"><span class="rc-stn">Mercury Arc Rectifier</span> <span class="rc-time">10.0s</span> <span class="rc-tier">T3</span></div>
<div class="rc-note">Mercury arc rectifier: AC strikes an arc at the mercury pool cathode; only forward-biased half-cycles conduct. The arc voltage drop and mercury vapour loss consume ~33% of the input power -- two DC charges out for every three AC charges in.</div>
<div class="rc-id"><code>e6_rectify_ac_to_dc</code></div>
</div>
</div>

## Ferroalloys chain
<p class="chapter-stats">6 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_chromite["<img src='/Conduvia/assets/icons/raw_ore_chromite.png' class='mmd-ico' />raw chromite ore"]
  i_crushed_ore_chromite["<img src='/Conduvia/assets/icons/crushed_ore_chromite.png' class='mmd-ico' />crushed chromite ore"]
  i_stone_dust["<img src='/Conduvia/assets/icons/stone_dust.png' class='mmd-ico' />stone dust"]
  i_pellet_chromite["<img src='/Conduvia/assets/icons/pellet_chromite.png' class='mmd-ico' />indurated chromite pellet"]
  i_coke_fuel["<img src='/Conduvia/assets/icons/coke_fuel.png' class='mmd-ico' />coke fuel"]
  i_burned_lime_quicklime["<img src='/Conduvia/assets/icons/burned_lime_quicklime.png' class='mmd-ico' />burned lime (quicklime)"]
  i_ferrochrome["<img src='/Conduvia/assets/icons/ferrochrome.png' class='mmd-ico' />ferrochrome"]
  i_slag["<img src='/Conduvia/assets/icons/slag.png' class='mmd-ico' />slag"]
  i_gas_co2["<img src='/Conduvia/assets/icons/gas_co2.png' class='mmd-ico' />carbon dioxide gas"]
  i_raw_ore_nickel_laterite["<img src='/Conduvia/assets/icons/raw_ore_nickel_laterite.png' class='mmd-ico' />nickel laterite (saprolite)"]
  i_nickel_laterite_calcine["<img src='/Conduvia/assets/icons/nickel_laterite_calcine.png' class='mmd-ico' />reduced laterite calcine"]
  i_ferronickel["<img src='/Conduvia/assets/icons/ferronickel.png' class='mmd-ico' />ferronickel"]
  p_fcr_crush_chromite{"Trip Hammer"}
  p_fcr_pelletize_chromite{"Pelletizing Disc + Induration Kiln"}
  p_fcr_saf_smelt{"Submerged-Arc Furnace (SAF)"}
  p_gather_ore_nickel_laterite{"Gather"}
  p_fni_calcine_laterite{"Rotary Calcining Kiln (RKEF dry/reduce)"}
  p_fni_smelt_ferronickel{"Submerged-Arc Furnace (SAF)"}
  i_raw_ore_chromite --> |"x2"| p_fcr_crush_chromite
  p_fcr_crush_chromite --> |"x2"| i_crushed_ore_chromite
  p_fcr_crush_chromite --> |"x1"| i_stone_dust
  i_crushed_ore_chromite --> |"x3"| p_fcr_pelletize_chromite
  p_fcr_pelletize_chromite --> |"x3"| i_pellet_chromite
  i_pellet_chromite --> |"x3"| p_fcr_saf_smelt
  i_coke_fuel --> |"x3"| p_fcr_saf_smelt
  i_burned_lime_quicklime --> |"x1"| p_fcr_saf_smelt
  p_fcr_saf_smelt --> |"x2"| i_ferrochrome
  p_fcr_saf_smelt --> |"x2"| i_slag
  p_fcr_saf_smelt --> |"x2"| i_gas_co2
  src_world["world"]:::world --> p_gather_ore_nickel_laterite
  p_gather_ore_nickel_laterite --> |"x3"| i_raw_ore_nickel_laterite
  i_raw_ore_nickel_laterite --> |"x3"| p_fni_calcine_laterite
  i_coke_fuel --> |"x1"| p_fni_calcine_laterite
  p_fni_calcine_laterite --> |"x3"| i_nickel_laterite_calcine
  p_fni_calcine_laterite --> |"x1"| i_gas_co2
  i_nickel_laterite_calcine --> |"x3"| p_fni_smelt_ferronickel
  i_coke_fuel --> |"x2"| p_fni_smelt_ferronickel
  i_burned_lime_quicklime --> |"x1"| p_fni_smelt_ferronickel
  p_fni_smelt_ferronickel --> |"x2"| i_ferronickel
  p_fni_smelt_ferronickel --> |"x2"| i_slag
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_fcr_crush_chromite proc;
  class p_fcr_pelletize_chromite proc;
  class p_fcr_saf_smelt proc;
  class p_gather_ore_nickel_laterite proc;
  class p_fni_calcine_laterite proc;
  class p_fni_smelt_ferronickel proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-crushing" markdown>
<div class="rc-out">:ci[crushed_ore_chromite|2] :ci[stone_dust|1]</div>
<div class="rc-flow">:ci[raw_ore_chromite|2] <span class="rc-arrow">→</span> :ci[crushed_ore_chromite|2] :ci[stone_dust|1]</div>
<div class="rc-meta"><span class="rc-stn">Trip Hammer</span> <span class="rc-time">30s</span> <span class="rc-tier">T2</span> <span class="rc-energy">16 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Crush friable lump chromite to an even grain. Chromite is brittle and sheds fines, so it is crushed deliberately and then re-agglomerated rather than charged as-mined.</div>
<div class="rc-id"><code>fcr_crush_chromite</code></div>
</div>
<div class="recipe-card cat-smelting" markdown>
<div class="rc-out">:ci[ferrochrome|2] :ci[slag|2] :ci[gas_co2|2]</div>
<div class="rc-flow">:ci[pellet_chromite|3] :ci[coke_fuel|3] :ci[burned_lime_quicklime|1] <span class="rc-arrow">→</span> :ci[ferrochrome|2] :ci[slag|2] :ci[gas_co2|2]</div>
<div class="rc-meta"><span class="rc-stn">Submerged-Arc Furnace (SAF)</span> <span class="rc-time">150s</span> <span class="rc-tier">T4</span> <span class="rc-energy">380 kJ</span> <span class="rc-bp">+2 byproducts</span></div>
<div class="rc-note">Bury the electrodes in a charge of pellets, coke and lime and pour the power in: FeCr2O4 + 4 C -> Fe + 2 Cr + 4 CO. The carbon strips the oxygen, lime fluxes the Mg/Al/Si gangue into a fluid slag, and the CO off-gas burns off as CO2. Taps as high-carbon ferrochrome. One of the most energy-hungry steps in the whole tech tree.</div>
<div class="rc-id"><code>fcr_saf_smelt</code></div>
</div>
<div class="recipe-card cat-smelting" markdown>
<div class="rc-out">:ci[ferronickel|2] :ci[slag|2]</div>
<div class="rc-flow">:ci[nickel_laterite_calcine|3] :ci[coke_fuel|2] :ci[burned_lime_quicklime|1] <span class="rc-arrow">→</span> :ci[ferronickel|2] :ci[slag|2]</div>
<div class="rc-meta"><span class="rc-stn">Submerged-Arc Furnace (SAF)</span> <span class="rc-time">150s</span> <span class="rc-tier">T4</span> <span class="rc-energy">360 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Reduction-smelt the hot calcine in the electric (submerged-arc) furnace. Nickel and a controlled amount of iron drop out together as a dense crude ferronickel; the silicate gangue floats off as slag. ~99% of the nickel is recovered -- the E and F of RKEF.</div>
<div class="rc-id"><code>fni_smelt_ferronickel</code></div>
</div>
<div class="recipe-card cat-calcining" markdown>
<div class="rc-out">:ci[nickel_laterite_calcine|3] :ci[gas_co2|1]</div>
<div class="rc-flow">:ci[raw_ore_nickel_laterite|3] :ci[coke_fuel|1] <span class="rc-arrow">→</span> :ci[nickel_laterite_calcine|3] :ci[gas_co2|1]</div>
<div class="rc-meta"><span class="rc-stn">Rotary Calcining Kiln (RKEF dry/reduce)</span> <span class="rc-time">90s</span> <span class="rc-tier">T3</span> <span class="rc-energy">120 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Tumble the wet saprolite down a fired rotary kiln to drive off free and crystal water and pre-reduce the NiO/FeO with coke and CO. The hot calcine is rushed straight to the furnace to keep its heat -- the R and K of RKEF.</div>
<div class="rc-id"><code>fni_calcine_laterite</code></div>
</div>
<div class="recipe-card cat-agglomeration" markdown>
<div class="rc-out">:ci[pellet_chromite|3]</div>
<div class="rc-flow">:ci[crushed_ore_chromite|3] <span class="rc-arrow">→</span> :ci[pellet_chromite|3]</div>
<div class="rc-meta"><span class="rc-stn">Pelletizing Disc + Induration Kiln</span> <span class="rc-time">45s</span> <span class="rc-tier">T3</span> <span class="rc-energy">40 kJ</span></div>
<div class="rc-note">Roll the chromite fines into green balls on the disc and fire them hard in the induration kiln. Indurated pellets keep the furnace burden permeable so reducing gas can climb through it.</div>
<div class="rc-id"><code>fcr_pelletize_chromite</code></div>
</div>
<div class="recipe-card cat-gathering" markdown>
<div class="rc-out">:ci[raw_ore_nickel_laterite|3]</div>
<div class="rc-meta"><span class="rc-time">30s</span> <span class="rc-tier">T2</span></div>
<div class="rc-note">Strip-mine the soft, deeply weathered nickel laterite. Low grade but enormous and shallow -- no shaft, no concentration, straight to the kiln.</div>
<div class="rc-id"><code>gather_ore_nickel_laterite</code></div>
</div>
</div>

## Industrial processing
<p class="chapter-stats">6 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_steel_ingot["<img src='/Conduvia/assets/icons/steel_ingot.png' class='mmd-ico' />steel ingot"]
  i_steam_charge["<img src='/Conduvia/assets/icons/steam_charge.png' class='mmd-ico' />steam charge"]
  i_steel_plate_rolled["<img src='/Conduvia/assets/icons/steel_plate_rolled.png' class='mmd-ico' />rolled steel plate"]
  i_pig_iron_ingot["<img src='/Conduvia/assets/icons/pig_iron_ingot.png' class='mmd-ico' />pig iron ingot"]
  i_steel_rail["<img src='/Conduvia/assets/icons/steel_rail.png' class='mmd-ico' />steel rail"]
  i_steel_beam["<img src='/Conduvia/assets/icons/steel_beam.png' class='mmd-ico' />rolled steel beam"]
  i_coal_bituminous["<img src='/Conduvia/assets/icons/coal_bituminous.png' class='mmd-ico' />bituminous coal"]
  i_slag_ironmaking["<img src='/Conduvia/assets/icons/slag_ironmaking.png' class='mmd-ico' />blast-furnace slag"]
  i_raw_ore_silica["<img src='/Conduvia/assets/icons/raw_ore_silica.png' class='mmd-ico' />raw silica ore"]
  i_charcoal["<img src='/Conduvia/assets/icons/charcoal.png' class='mmd-ico' />charcoal"]
  i_glass_tube["<img src='/Conduvia/assets/icons/glass_tube.png' class='mmd-ico' />borosilicate glass tube"]
  i_carbon_filament_preform["<img src='/Conduvia/assets/icons/carbon_filament_preform.png' class='mmd-ico' />carbon filament preform"]
  i_copper_wire_insulated["<img src='/Conduvia/assets/icons/copper_wire_insulated.png' class='mmd-ico' />insulated copper wire"]
  i_incandescent_lamp_carbon["<img src='/Conduvia/assets/icons/incandescent_lamp_carbon.png' class='mmd-ico' />incandescent lamp (carbon)"]
  p_t3_roll_steel_plate{"Steam Rolling Mill"}
  p_t3_roll_steel_rail{"Steam Rolling Mill"}
  p_t3_roll_steel_beam{"Steam Rolling Mill"}
  p_t3_open_hearth_steel{"Open Hearth Furnace"}
  p_t3_glass_tube{"Glass Bench"}
  p_t3_glass_lamp_bulb{"Glass Bench"}
  i_steel_ingot --> |"x2"| p_t3_roll_steel_plate
  i_steam_charge --> |"x1"| p_t3_roll_steel_plate
  p_t3_roll_steel_plate --> |"x2"| i_steel_plate_rolled
  i_pig_iron_ingot --> |"x4"| p_t3_roll_steel_rail
  i_steam_charge --> |"x1"| p_t3_roll_steel_rail
  p_t3_roll_steel_rail --> |"x2"| i_steel_rail
  i_steel_ingot --> |"x3"| p_t3_roll_steel_beam
  i_steam_charge --> |"x1"| p_t3_roll_steel_beam
  p_t3_roll_steel_beam --> |"x2"| i_steel_beam
  i_pig_iron_ingot --> |"x6"| p_t3_open_hearth_steel
  i_coal_bituminous --> |"x3"| p_t3_open_hearth_steel
  p_t3_open_hearth_steel --> |"x5"| i_steel_ingot
  p_t3_open_hearth_steel --> |"x2"| i_slag_ironmaking
  i_raw_ore_silica --> |"x2"| p_t3_glass_tube
  i_charcoal --> |"x2"| p_t3_glass_tube
  p_t3_glass_tube --> |"x4"| i_glass_tube
  i_glass_tube --> |"x1"| p_t3_glass_lamp_bulb
  i_carbon_filament_preform --> |"x1"| p_t3_glass_lamp_bulb
  i_copper_wire_insulated --> |"x1"| p_t3_glass_lamp_bulb
  p_t3_glass_lamp_bulb --> |"x2"| i_incandescent_lamp_carbon
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_t3_roll_steel_plate proc;
  class p_t3_roll_steel_rail proc;
  class p_t3_roll_steel_beam proc;
  class p_t3_open_hearth_steel proc;
  class p_t3_glass_tube proc;
  class p_t3_glass_lamp_bulb proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-industry" markdown>
<div class="rc-out">:ci[glass_tube|4]</div>
<div class="rc-flow">:ci[raw_ore_silica|2] :ci[charcoal|2] <span class="rc-arrow">→</span> :ci[glass_tube|4]</div>
<div class="rc-meta"><span class="rc-stn">Glass Bench</span> <span class="rc-time">180s</span> <span class="rc-tier">T3</span></div>
<div class="rc-note">Quartz silica is melted in the lampworking burner flame and drawn by hand into tube stock. Borosilicate composition (with trace mineral impurities) tolerates rapid thermal cycling without cracking.</div>
<div class="rc-id"><code>t3_glass_tube</code></div>
</div>
<div class="recipe-card cat-industry" markdown>
<div class="rc-out">:ci[incandescent_lamp_carbon|2]</div>
<div class="rc-flow">:ci[glass_tube|1] :ci[carbon_filament_preform|1] :ci[copper_wire_insulated|1] <span class="rc-arrow">→</span> :ci[incandescent_lamp_carbon|2]</div>
<div class="rc-meta"><span class="rc-stn">Glass Bench</span> <span class="rc-time">90s</span> <span class="rc-tier">T3</span></div>
<div class="rc-note">Glass tube is collapsed over the filament mount, the air evacuated, and the stem sealed with a gas flame. Using pre-drawn tube stock is faster than blowing a bulb from scratch and gives consistent wall thickness.</div>
<div class="rc-id"><code>t3_glass_lamp_bulb</code></div>
</div>
<div class="recipe-card cat-industry" markdown>
<div class="rc-out">:ci[steel_beam|2]</div>
<div class="rc-flow">:ci[steel_ingot|3] :ci[steam_charge|1] <span class="rc-arrow">→</span> :ci[steel_beam|2]</div>
<div class="rc-meta"><span class="rc-stn">Steam Rolling Mill</span> <span class="rc-time">120s</span> <span class="rc-tier">T3</span></div>
<div class="rc-note">Universal H-beam section rolled from steel billets. Structurally superior to wrought-iron box girders for the same mass -- flanges carry bending load, web carries shear.</div>
<div class="rc-id"><code>t3_roll_steel_beam</code></div>
</div>
<div class="recipe-card cat-kiln" markdown>
<div class="rc-out">:ci[steel_ingot|5] :ci[slag_ironmaking|2]</div>
<div class="rc-flow">:ci[pig_iron_ingot|6] :ci[coal_bituminous|3] <span class="rc-arrow">→</span> :ci[steel_ingot|5] :ci[slag_ironmaking|2]</div>
<div class="rc-meta"><span class="rc-stn">Open Hearth Furnace</span> <span class="rc-time">600s</span> <span class="rc-tier">T3</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Regenerative open-hearth process: incoming cold gas heats through a brick checker-work that was itself heated by the last exhaust stroke. The reversal cycle maintains furnace temperature while using far less fuel than a non-regenerative flame. Operator controls carbon content precisely -- Bessemer is faster but open-hearth produces more consistent structural steel grades.</div>
<div class="rc-id"><code>t3_open_hearth_steel</code></div>
</div>
<div class="recipe-card cat-industry" markdown>
<div class="rc-out">:ci[steel_plate_rolled|2]</div>
<div class="rc-flow">:ci[steel_ingot|2] :ci[steam_charge|1] <span class="rc-arrow">→</span> :ci[steel_plate_rolled|2]</div>
<div class="rc-meta"><span class="rc-stn">Steam Rolling Mill</span> <span class="rc-time">90s</span> <span class="rc-tier">T3</span></div>
<div class="rc-note">Steel ingots are passed between hardened rolls under full steam pressure. The rolling action reduces cross-section, work-hardens the surface, and aligns the grain for better tensile properties.</div>
<div class="rc-id"><code>t3_roll_steel_plate</code></div>
</div>
<div class="recipe-card cat-industry" markdown>
<div class="rc-out">:ci[steel_rail|2]</div>
<div class="rc-flow">:ci[pig_iron_ingot|4] :ci[steam_charge|1] <span class="rc-arrow">→</span> :ci[steel_rail|2]</div>
<div class="rc-meta"><span class="rc-stn">Steam Rolling Mill</span> <span class="rc-time">120s</span> <span class="rc-tier">T3</span></div>
<div class="rc-note">Hot pig iron rolled through a profiled rail die. The I-section profile distributes wheel load across the foot and head; air-cooling after rolling relieves thermal stress.</div>
<div class="rc-id"><code>t3_roll_steel_rail</code></div>
</div>
</div>

## Steam processing
<p class="chapter-stats">1 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_water_raw["<img src='/Conduvia/assets/icons/water_raw.png' class='mmd-ico' />raw water"]
  i_charcoal["<img src='/Conduvia/assets/icons/charcoal.png' class='mmd-ico' />charcoal"]
  i_steam_charge["<img src='/Conduvia/assets/icons/steam_charge.png' class='mmd-ico' />steam charge"]
  p_e5_boil_steam_charge{"Riveted Boiler"}
  i_water_raw --> |"x1"| p_e5_boil_steam_charge
  i_charcoal --> |"x1"| p_e5_boil_steam_charge
  p_e5_boil_steam_charge --> |"x1"| i_steam_charge
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_e5_boil_steam_charge proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-industry" markdown>
<div class="rc-out">:ci[steam_charge|1]</div>
<div class="rc-flow">:ci[water_raw|1] :ci[charcoal|1] <span class="rc-arrow">→</span> :ci[steam_charge|1]</div>
<div class="rc-meta"><span class="rc-stn">Riveted Boiler</span> <span class="rc-time">20.0s</span> <span class="rc-tier">T4</span></div>
<div class="rc-note">Boil the charge until pressure builds and tap one puff into a holding flask. Water goes in the input, charcoal in the fuel slot.</div>
<div class="rc-id"><code>e5_boil_steam_charge</code></div>
</div>
</div>

## Steel processing
<p class="chapter-stats">3 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_crushed_ore_hematite["<img src='/Conduvia/assets/icons/crushed_ore_hematite.png' class='mmd-ico' />crushed hematite"]
  i_coke_fuel["<img src='/Conduvia/assets/icons/coke_fuel.png' class='mmd-ico' />coke fuel"]
  i_limestone_flux["<img src='/Conduvia/assets/icons/limestone_flux.png' class='mmd-ico' />limestone flux"]
  i_pig_iron_ingot["<img src='/Conduvia/assets/icons/pig_iron_ingot.png' class='mmd-ico' />pig iron ingot"]
  i_waste_slag["<img src='/Conduvia/assets/icons/waste_slag.png' class='mmd-ico' />slag"]
  i_steel_ingot["<img src='/Conduvia/assets/icons/steel_ingot.png' class='mmd-ico' />steel ingot"]
  i_crushed_slag["<img src='/Conduvia/assets/icons/crushed_slag.png' class='mmd-ico' />crushed slag"]
  i_waste_tailings["<img src='/Conduvia/assets/icons/waste_tailings.png' class='mmd-ico' />tailings"]
  p_t2_blast_furnace_pig_iron{"Blast Furnace"}
  p_t2_bessemer_steel{"Bessemer Converter"}
  p_t2_slag_reprocess{"Trip Hammer"}
  i_crushed_ore_hematite --> |"x6"| p_t2_blast_furnace_pig_iron
  i_coke_fuel --> |"x3"| p_t2_blast_furnace_pig_iron
  i_limestone_flux --> |"x2"| p_t2_blast_furnace_pig_iron
  p_t2_blast_furnace_pig_iron --> |"x4"| i_pig_iron_ingot
  p_t2_blast_furnace_pig_iron --> |"x3"| i_waste_slag
  i_pig_iron_ingot --> |"x4"| p_t2_bessemer_steel
  p_t2_bessemer_steel --> |"x3"| i_steel_ingot
  p_t2_bessemer_steel --> |"x1"| i_waste_slag
  i_waste_slag --> |"x6"| p_t2_slag_reprocess
  p_t2_slag_reprocess --> |"x4"| i_crushed_slag
  p_t2_slag_reprocess --> |"x2"| i_waste_tailings
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_t2_blast_furnace_pig_iron proc;
  class p_t2_bessemer_steel proc;
  class p_t2_slag_reprocess proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-crusher" markdown>
<div class="rc-out">:ci[crushed_slag|4] :ci[waste_tailings|2]</div>
<div class="rc-flow">:ci[waste_slag|6] <span class="rc-arrow">→</span> :ci[crushed_slag|4] :ci[waste_tailings|2]</div>
<div class="rc-meta"><span class="rc-stn">Trip Hammer</span> <span class="rc-time">90s</span> <span class="rc-tier">T2</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Blast furnace slag contains 0.5-1.5% trapped iron particles and glassy silicate phases. Crushing liberates the iron granules for magnetic or gravity separation in later tiers. The silicate fines become tailings; the iron-rich fraction can be re-fed to the blast furnace at small loss.</div>
<div class="rc-id"><code>t2_slag_reprocess</code></div>
</div>
<div class="recipe-card cat-kiln" markdown>
<div class="rc-out">:ci[pig_iron_ingot|4] :ci[waste_slag|3]</div>
<div class="rc-flow">:ci[crushed_ore_hematite|6] :ci[coke_fuel|3] :ci[limestone_flux|2] <span class="rc-arrow">→</span> :ci[pig_iron_ingot|4] :ci[waste_slag|3]</div>
<div class="rc-meta"><span class="rc-stn">Blast Furnace</span> <span class="rc-time">480s</span> <span class="rc-tier">T2</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">The blast furnace drives a continuous reduction column: coke burns to CO at tuyere level (~1600 degC), CO reduces Fe2O3 to iron as the burden descends, and limestone flux (CaO after calcination) reacts with gangue silica to form liquid slag (CaSiO3) that floats above liquid pig iron. Pig iron absorbs ~4% C from coke -- it is hard but brittle. The slag must be tapped separately from the iron notch.</div>
<div class="rc-id"><code>t2_blast_furnace_pig_iron</code></div>
</div>
<div class="recipe-card cat-kiln" markdown>
<div class="rc-out">:ci[steel_ingot|3] :ci[waste_slag|1]</div>
<div class="rc-flow">:ci[pig_iron_ingot|4] <span class="rc-arrow">→</span> :ci[steel_ingot|3] :ci[waste_slag|1]</div>
<div class="rc-meta"><span class="rc-stn">Bessemer Converter</span> <span class="rc-time">300s</span> <span class="rc-tier">T2</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">The Bessemer blow forces cold air through liquid pig iron from tuyeres at the converter base. Oxygen in the air burns out carbon, silicon, and manganese in a violent 15-20 minute exothermic reaction -- the heat released is so intense that no external fuel is needed after ignition. Carbon drops from ~4% to ~0.2-0.5%, producing steel. The blow must be stopped at the right carbon level; over-blowing produces wrought iron, under-blowing leaves cast iron.</div>
<div class="rc-id"><code>t2_bessemer_steel</code></div>
</div>
</div>
