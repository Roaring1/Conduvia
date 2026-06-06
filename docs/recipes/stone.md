# Tier 1 — Stone & Early Materials

<p class="chapter-stats">45 recipes</p>

## Farming
<p class="chapter-stats">2 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_forest_seed_mix_dry["<img src='../../assets/icons/forest_seed_mix_dry.png' class='mmd-ico' />dry forest seed mix"]
  i_flax_seed["<img src='../../assets/icons/flax_seed.png' class='mmd-ico' />flax seed"]
  i_turnip_seed["<img src='../../assets/icons/turnip_seed.png' class='mmd-ico' />turnip seed"]
  i_carrot_seed["<img src='../../assets/icons/carrot_seed.png' class='mmd-ico' />carrot seed"]
  i_flax["<img src='../../assets/icons/flax.png' class='mmd-ico' />flax stalks"]
  i_plant_fibers["<img src='../../assets/icons/plant_fibers.png' class='mmd-ico' />plant fibers"]
  p_e1_sort_seed_mix{"Camp Marker"}
  p_e1_ret_flax{"Camp Marker"}
  i_forest_seed_mix_dry --> |"x3"| p_e1_sort_seed_mix
  p_e1_sort_seed_mix --> |"x2"| i_flax_seed
  p_e1_sort_seed_mix --> |"x2"| i_turnip_seed
  p_e1_sort_seed_mix --> |"x2"| i_carrot_seed
  i_flax --> |"x2"| p_e1_ret_flax
  p_e1_ret_flax --> |"x3"| i_plant_fibers
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_e1_sort_seed_mix proc;
  class p_e1_ret_flax proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[forest_seed_mix_dry|3] <span class="rc-arrow">→</span> :ci[flax_seed|2] :ci[turnip_seed|2] :ci[carrot_seed|2]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">120s</span> <span class="rc-tier">T0</span> <span class="rc-bp">+2 byproducts</span></div>
<div class="rc-note">Winnow and pick the dry mix apart into seed you can actually sow on purpose.</div>
<div class="rc-id"><code>e1_sort_seed_mix</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[flax|2] <span class="rc-arrow">→</span> :ci[plant_fibers|3]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">300s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Soak the pulled stalks until the core rots free, then beat out the long bast.</div>
<div class="rc-id"><code>e1_ret_flax</code></div>
</div>
</div>

## Flint chain
<p class="chapter-stats">5 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_flint["<img src='../../assets/icons/raw_ore_flint.png' class='mmd-ico' />raw flint"]
  i_flint_flake["<img src='../../assets/icons/flint_flake.png' class='mmd-ico' />flint flake"]
  i_stone_flakes["<img src='../../assets/icons/stone_flakes.png' class='mmd-ico' />stone flakes"]
  i_flint_blade_knapped["<img src='../../assets/icons/flint_blade_knapped.png' class='mmd-ico' />knapped flint blade"]
  i_flint_arrowhead["<img src='../../assets/icons/flint_arrowhead.png' class='mmd-ico' />flint arrowhead"]
  i_steel_ingot["<img src='../../assets/icons/steel_ingot.png' class='mmd-ico' />steel ingot"]
  i_fire_steel_striker["<img src='../../assets/icons/fire_steel_striker.png' class='mmd-ico' />flint-and-steel striker"]
  i_flint_calcined_silica["<img src='../../assets/icons/flint_calcined_silica.png' class='mmd-ico' />calcined potters’ flint"]
  p_fl_knap_flint{"Knapping Station (anvil stone + billet)"}
  p_fl_knap_blade{"Knapping Station (anvil stone + billet)"}
  p_fl_make_arrowhead{"Knapping Station (anvil stone + billet)"}
  p_fl_fire_steel{"Workbench"}
  p_fl_calcine_silica{"Rotary Calcining Kiln (RKEF dry/reduce)"}
  i_raw_ore_flint --> |"x2"| p_fl_knap_flint
  p_fl_knap_flint --> |"x3"| i_flint_flake
  p_fl_knap_flint --> |"x1"| i_stone_flakes
  i_flint_flake --> |"x2"| p_fl_knap_blade
  p_fl_knap_blade --> |"x1"| i_flint_blade_knapped
  i_flint_flake --> |"x1"| p_fl_make_arrowhead
  p_fl_make_arrowhead --> |"x2"| i_flint_arrowhead
  i_raw_ore_flint --> |"x1"| p_fl_fire_steel
  i_steel_ingot --> |"x1"| p_fl_fire_steel
  p_fl_fire_steel --> |"x2"| i_fire_steel_striker
  i_raw_ore_flint --> |"x2"| p_fl_calcine_silica
  p_fl_calcine_silica --> |"x2"| i_flint_calcined_silica
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_fl_knap_flint proc;
  class p_fl_knap_blade proc;
  class p_fl_make_arrowhead proc;
  class p_fl_fire_steel proc;
  class p_fl_calcine_silica proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-assembly" markdown>
<div class="rc-flow">:ci[raw_ore_flint|1] :ci[steel_ingot|1] <span class="rc-arrow">→</span> :ci[fire_steel_striker|2]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#workbench">Workbench</a></span> <span class="rc-time">60s</span> <span class="rc-tier">T2</span> <span class="rc-energy">25 kJ</span></div>
<div class="rc-note">Forge/fit a high-carbon steel striker to a flint nodule. Real flint-and-steel: the harder flint shaves heated steel particles that ignite -- the most primitive ore meets the steel chain.</div>
<div class="rc-id"><code>fl_fire_steel</code></div>
</div>
<div class="recipe-card cat-knapping" markdown>
<div class="rc-flow">:ci[flint_flake|1] <span class="rc-arrow">→</span> :ci[flint_arrowhead|2]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#knapping_station">Knapping Station (anvil stone + billet)</a></span> <span class="rc-time">25s</span> <span class="rc-tier">T1</span> <span class="rc-energy">5 kJ</span></div>
<div class="rc-note">Bifacially work a flake into a tipped, barbed projectile point for arrows and darts.</div>
<div class="rc-id"><code>fl_make_arrowhead</code></div>
</div>
<div class="recipe-card cat-knapping" markdown>
<div class="rc-flow">:ci[flint_flake|2] <span class="rc-arrow">→</span> :ci[flint_blade_knapped|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#knapping_station">Knapping Station (anvil stone + billet)</a></span> <span class="rc-time">40s</span> <span class="rc-tier">T1</span> <span class="rc-energy">8 kJ</span></div>
<div class="rc-note">Pressure-retouch a flake down one edge into a straight, durable knife/scraper blade.</div>
<div class="rc-id"><code>fl_knap_blade</code></div>
</div>
<div class="recipe-card cat-calcination" markdown>
<div class="rc-flow">:ci[raw_ore_flint|2] <span class="rc-arrow">→</span> :ci[flint_calcined_silica|2]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#rotary_calciner_kiln">Rotary Calcining Kiln (RKEF dry/reduce)</a></span> <span class="rc-time">200s</span> <span class="rc-tier">T2</span> <span class="rc-energy">150 kJ</span></div>
<div class="rc-note">Calcine flint near 600 C until it crumbles, then grind to a fine silica powder (partly cristobalite). The classic potters’ flint for clay bodies and glazes.</div>
<div class="rc-id"><code>fl_calcine_silica</code></div>
</div>
<div class="recipe-card cat-knapping" markdown>
<div class="rc-flow">:ci[raw_ore_flint|2] <span class="rc-arrow">→</span> :ci[flint_flake|3] :ci[stone_flakes|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#knapping_station">Knapping Station (anvil stone + billet)</a></span> <span class="rc-time">30s</span> <span class="rc-tier">T1</span> <span class="rc-energy">6 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Strike a flint core with a hammerstone: conchoidal fracture shears off sharp flakes. The blunt shatter and trimming chips fall away as stone debitage -- a salvage byproduct, not loss.</div>
<div class="rc-id"><code>fl_knap_flint</code></div>
</div>
</div>

## Obsidian chain
<p class="chapter-stats">4 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_raw_ore_obsidian["<img src='../../assets/icons/raw_ore_obsidian.png' class='mmd-ico' />raw obsidian"]
  i_obsidian_flake["<img src='../../assets/icons/obsidian_flake.png' class='mmd-ico' />obsidian flake"]
  i_stone_flakes["<img src='../../assets/icons/stone_flakes.png' class='mmd-ico' />stone flakes"]
  i_wood["<img src='../../assets/icons/wood.png' class='mmd-ico' />construction wood"]
  i_obsidian_blade_pressure["<img src='../../assets/icons/obsidian_blade_pressure.png' class='mmd-ico' />pressure-flaked obsidian blade"]
  i_obsidian_arrowhead["<img src='../../assets/icons/obsidian_arrowhead.png' class='mmd-ico' />obsidian dart point"]
  i_obsidian_scalpel["<img src='../../assets/icons/obsidian_scalpel.png' class='mmd-ico' />obsidian scalpel"]
  p_ob_knap_obsidian{"Knapping Station (anvil stone + billet)"}
  p_ob_pressure_blade{"Knapping Station (anvil stone + billet)"}
  p_ob_make_arrowhead{"Knapping Station (anvil stone + billet)"}
  p_ob_make_scalpel{"Carving Bench"}
  i_raw_ore_obsidian --> |"x2"| p_ob_knap_obsidian
  p_ob_knap_obsidian --> |"x3"| i_obsidian_flake
  p_ob_knap_obsidian --> |"x1"| i_stone_flakes
  i_obsidian_flake --> |"x2"| p_ob_pressure_blade
  i_wood --> |"x1"| p_ob_pressure_blade
  p_ob_pressure_blade --> |"x1"| i_obsidian_blade_pressure
  i_obsidian_flake --> |"x1"| p_ob_make_arrowhead
  p_ob_make_arrowhead --> |"x2"| i_obsidian_arrowhead
  i_obsidian_blade_pressure --> |"x1"| p_ob_make_scalpel
  i_wood --> |"x1"| p_ob_make_scalpel
  p_ob_make_scalpel --> |"x1"| i_obsidian_scalpel
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_ob_knap_obsidian proc;
  class p_ob_pressure_blade proc;
  class p_ob_make_arrowhead proc;
  class p_ob_make_scalpel proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-knapping" markdown>
<div class="rc-flow">:ci[obsidian_flake|1] <span class="rc-arrow">→</span> :ci[obsidian_arrowhead|2]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#knapping_station">Knapping Station (anvil stone + billet)</a></span> <span class="rc-time">25s</span> <span class="rc-tier">T1</span> <span class="rc-energy">5 kJ</span></div>
<div class="rc-note">Bifacially pressure-flake a flake into a razor projectile point for arrows and atlatl darts.</div>
<div class="rc-id"><code>ob_make_arrowhead</code></div>
</div>
<div class="recipe-card cat-knapping" markdown>
<div class="rc-flow">:ci[obsidian_flake|2] :ci[wood|1] <span class="rc-arrow">→</span> :ci[obsidian_blade_pressure|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#knapping_station">Knapping Station (anvil stone + billet)</a></span> <span class="rc-time">50s</span> <span class="rc-tier">T2</span> <span class="rc-energy">10 kJ</span></div>
<div class="rc-note">Pressure-flake a flake with a wood/antler billet, pressing off tiny chips to refine the edge to ~3 nm -- sharper than surgical steel. The billet is consumed.</div>
<div class="rc-id"><code>ob_pressure_blade</code></div>
</div>
<div class="recipe-card cat-knapping" markdown>
<div class="rc-flow">:ci[raw_ore_obsidian|2] <span class="rc-arrow">→</span> :ci[obsidian_flake|3] :ci[stone_flakes|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#knapping_station">Knapping Station (anvil stone + billet)</a></span> <span class="rc-time">30s</span> <span class="rc-tier">T1</span> <span class="rc-energy">6 kJ</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Strike an obsidian core: the glass fractures conchoidally into flakes already keener than flint. Shatter and trim chips fall away as stone debitage.</div>
<div class="rc-id"><code>ob_knap_obsidian</code></div>
</div>
<div class="recipe-card cat-assembly" markdown>
<div class="rc-flow">:ci[obsidian_blade_pressure|1] :ci[wood|1] <span class="rc-arrow">→</span> :ci[obsidian_scalpel|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#carving_bench">Carving Bench</a></span> <span class="rc-time">90s</span> <span class="rc-tier">T3</span> <span class="rc-energy">30 kJ</span></div>
<div class="rc-note">Haft an obsidian micro-blade to a carved wooden handle: a surgical-grade scalpel whose edge cuts between cells for clean, low-scarring incisions.</div>
<div class="rc-id"><code>ob_make_scalpel</code></div>
</div>
</div>

## Stone age
<p class="chapter-stats">3 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_stone_river_rounded["<img src='../../assets/icons/stone_river_rounded.png' class='mmd-ico' />rounded river stone"]
  i_hammerstone["<img src='../../assets/icons/hammerstone.png' class='mmd-ico' />hammerstone"]
  i_stone_axe_head["<img src='../../assets/icons/stone_axe_head.png' class='mmd-ico' />stone axe head"]
  i_stone_flakes["<img src='../../assets/icons/stone_flakes.png' class='mmd-ico' />stone flakes"]
  i_stick_dry_small["<img src='../../assets/icons/stick_dry_small.png' class='mmd-ico' />small dry sticks"]
  i_wood_haft["<img src='../../assets/icons/wood_haft.png' class='mmd-ico' />wood haft"]
  i_rope["<img src='../../assets/icons/rope.png' class='mmd-ico' />rope"]
  i_stone_axe_ground["<img src='../../assets/icons/stone_axe_ground.png' class='mmd-ico' />ground stone axe"]
  p_e1_knap_stone_axe_head{"Camp Marker"}
  p_e1_carve_wood_haft{"Camp Marker"}
  p_e1_assemble_stone_axe{"Camp Marker"}
  i_stone_river_rounded --> |"x2"| p_e1_knap_stone_axe_head
  i_hammerstone --> p_e1_knap_stone_axe_head
  p_e1_knap_stone_axe_head --> |"x1"| i_stone_axe_head
  p_e1_knap_stone_axe_head --> |"x3"| i_stone_flakes
  i_stick_dry_small --> |"x1"| p_e1_carve_wood_haft
  i_stone_flakes --> |"x1"| p_e1_carve_wood_haft
  p_e1_carve_wood_haft --> |"x1"| i_wood_haft
  i_stone_axe_head --> |"x1"| p_e1_assemble_stone_axe
  i_wood_haft --> |"x1"| p_e1_assemble_stone_axe
  i_rope --> |"x1"| p_e1_assemble_stone_axe
  p_e1_assemble_stone_axe --> |"x1"| i_stone_axe_ground
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_e1_knap_stone_axe_head proc;
  class p_e1_carve_wood_haft proc;
  class p_e1_assemble_stone_axe proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[stone_axe_head|1] :ci[wood_haft|1] :ci[rope|1] <span class="rc-arrow">→</span> :ci[stone_axe_ground|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">240s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Seat the head in a split or notch in the haft and lash it tight; wet rope shrinks as it dries.</div>
<div class="rc-id"><code>e1_assemble_stone_axe</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[stone_river_rounded|2] :ci[hammerstone|0] <span class="rc-arrow">→</span> :ci[stone_axe_head|1] :ci[stone_flakes|3]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">600s</span> <span class="rc-tier">T0</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Hard-hammer percussion to rough the wedge, then grind the edge on coarse stone.</div>
<div class="rc-id"><code>e1_knap_stone_axe_head</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[stick_dry_small|1] :ci[stone_flakes|1] <span class="rc-arrow">→</span> :ci[wood_haft|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">300s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Strip the bark and whittle the stick straight and smooth with a fresh flake edge.</div>
<div class="rc-id"><code>e1_carve_wood_haft</code></div>
</div>
</div>

## Stone age materials
<p class="chapter-stats">15 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_dirt["<img src='../../assets/icons/dirt.png' class='mmd-ico' />loose dirt"]
  i_bark_bucket_water["<img src='../../assets/icons/bark_bucket_water.png' class='mmd-ico' />water-filled bark bucket"]
  i_plant_fibers["<img src='../../assets/icons/plant_fibers.png' class='mmd-ico' />plant fibers"]
  i_clay["<img src='../../assets/icons/clay.png' class='mmd-ico' />raw clay"]
  i_fat_raw["<img src='../../assets/icons/fat_raw.png' class='mmd-ico' />raw animal fat"]
  i_grease_tallow["<img src='../../assets/icons/grease_tallow.png' class='mmd-ico' />grease (tallow)"]
  i_hemp_fiber["<img src='../../assets/icons/hemp_fiber.png' class='mmd-ico' />hemp fiber"]
  i_sail_cloth["<img src='../../assets/icons/sail_cloth.png' class='mmd-ico' />sail cloth"]
  i_earthenware_brick["<img src='../../assets/icons/earthenware_brick.png' class='mmd-ico' />earthenware brick"]
  i_pestle_stone["<img src='../../assets/icons/pestle_stone.png' class='mmd-ico' />stone pestle"]
  i_grog_crushed_ceramic_temper["<img src='../../assets/icons/grog_crushed_ceramic_temper.png' class='mmd-ico' />grog (crushed ceramic temper)"]
  i_sand["<img src='../../assets/icons/sand.png' class='mmd-ico' />loose sand"]
  i_temper_sand_or_grog["<img src='../../assets/icons/temper_sand_or_grog.png' class='mmd-ico' />temper (sand or grog)"]
  i_wood["<img src='../../assets/icons/wood.png' class='mmd-ico' />construction wood"]
  i_plain_bearing_wood["<img src='../../assets/icons/plain_bearing_wood.png' class='mmd-ico' />plain bearing (wood)"]
  i_stone_flakes["<img src='../../assets/icons/stone_flakes.png' class='mmd-ico' />stone flakes"]
  i_wooden_peg["<img src='../../assets/icons/wooden_peg.png' class='mmd-ico' />wooden peg"]
  i_board_plank_rough["<img src='../../assets/icons/board_plank_rough.png' class='mmd-ico' />rough board plank"]
  i_rope["<img src='../../assets/icons/rope.png' class='mmd-ico' />rope"]
  i_wooden_tub["<img src='../../assets/icons/wooden_tub.png' class='mmd-ico' />wooden tub"]
  i_stone["<img src='../../assets/icons/stone.png' class='mmd-ico' />fieldstone"]
  i_charcoal_retort_kiln["<img src='../../assets/icons/charcoal_retort_kiln.png' class='mmd-ico' />charcoal retort kiln"]
  i_charcoal["<img src='../../assets/icons/charcoal.png' class='mmd-ico' />charcoal"]
  i_tar["<img src='../../assets/icons/tar.png' class='mmd-ico' />tar"]
  i_pitch["<img src='../../assets/icons/pitch.png' class='mmd-ico' />pitch"]
  i_log_medium_dry["<img src='../../assets/icons/log_medium_dry.png' class='mmd-ico' />medium dry log"]
  i_tool_stone_flake["<img src='../../assets/icons/tool_stone_flake.png' class='mmd-ico' />stone flake"]
  i_stripped_log["<img src='../../assets/icons/stripped_log.png' class='mmd-ico' />stripped log"]
  i_forest_bark_slabs["<img src='../../assets/icons/forest_bark_slabs.png' class='mmd-ico' />bark slabs"]
  i_forest_bark_strip["<img src='../../assets/icons/forest_bark_strip.png' class='mmd-ico' />curled bark strip"]
  i_stick_dry_small["<img src='../../assets/icons/stick_dry_small.png' class='mmd-ico' />small dry sticks"]
  i_wood_haft["<img src='../../assets/icons/wood_haft.png' class='mmd-ico' />wood haft"]
  p_e1_wash_dirt_for_clay{"Camp Marker"}
  p_e1_render_grease_tallow{"Survival Campfire"}
  p_e1_ret_hemp_fiber{"Camp Marker"}
  p_e1_weave_sail_cloth{"Camp Marker"}
  p_e1_crush_grog{"Camp Marker"}
  p_e1_screen_temper_sand{"Camp Marker"}
  p_e1_fit_plain_bearing_wood{"Camp Marker"}
  p_e1_carve_wooden_peg{"Camp Marker"}
  p_e1_build_wooden_tub{"Camp Marker"}
  p_e1_build_charcoal_retort_kiln{"Camp Marker"}
  p_e1_char_retort{"Charcoal Retort Kiln"}
  p_e1_reduce_pitch{"Survival Campfire"}
  p_e1_strip_log{"Camp Marker"}
  p_e1_saw_planks_from_stripped{"Camp Marker"}
  p_e1_carve_haft_from_stripped{"Camp Marker"}
  i_dirt --> |"x4"| p_e1_wash_dirt_for_clay
  i_bark_bucket_water --> |"x1"| p_e1_wash_dirt_for_clay
  i_plant_fibers --> |"x1"| p_e1_wash_dirt_for_clay
  p_e1_wash_dirt_for_clay --> |"x1"| i_clay
  i_fat_raw --> |"x2"| p_e1_render_grease_tallow
  p_e1_render_grease_tallow --> |"x1"| i_grease_tallow
  i_plant_fibers --> |"x3"| p_e1_ret_hemp_fiber
  p_e1_ret_hemp_fiber --> |"x1"| i_hemp_fiber
  i_hemp_fiber --> |"x4"| p_e1_weave_sail_cloth
  p_e1_weave_sail_cloth --> |"x1"| i_sail_cloth
  i_earthenware_brick --> |"x1"| p_e1_crush_grog
  i_pestle_stone --> p_e1_crush_grog
  p_e1_crush_grog --> |"x2"| i_grog_crushed_ceramic_temper
  i_sand --> |"x2"| p_e1_screen_temper_sand
  p_e1_screen_temper_sand --> |"x1"| i_temper_sand_or_grog
  i_wood --> |"x1"| p_e1_fit_plain_bearing_wood
  i_grease_tallow --> |"x1"| p_e1_fit_plain_bearing_wood
  p_e1_fit_plain_bearing_wood --> |"x1"| i_plain_bearing_wood
  i_wood --> |"x1"| p_e1_carve_wooden_peg
  i_stone_flakes --> |"x1"| p_e1_carve_wooden_peg
  p_e1_carve_wooden_peg --> |"x4"| i_wooden_peg
  i_board_plank_rough --> |"x2"| p_e1_build_wooden_tub
  i_rope --> |"x1"| p_e1_build_wooden_tub
  p_e1_build_wooden_tub --> |"x1"| i_wooden_tub
  i_earthenware_brick --> |"x6"| p_e1_build_charcoal_retort_kiln
  i_clay --> |"x4"| p_e1_build_charcoal_retort_kiln
  i_stone --> |"x4"| p_e1_build_charcoal_retort_kiln
  p_e1_build_charcoal_retort_kiln --> |"x1"| i_charcoal_retort_kiln
  i_wood --> |"x8"| p_e1_char_retort
  p_e1_char_retort --> |"x5"| i_charcoal
  p_e1_char_retort --> |"x1"| i_tar
  i_tar --> |"x2"| p_e1_reduce_pitch
  p_e1_reduce_pitch --> |"x1"| i_pitch
  i_log_medium_dry --> |"x1"| p_e1_strip_log
  i_tool_stone_flake --> p_e1_strip_log
  p_e1_strip_log --> |"x1"| i_stripped_log
  p_e1_strip_log --> |"x2"| i_forest_bark_slabs
  p_e1_strip_log --> |"x2"| i_forest_bark_strip
  i_stripped_log --> |"x1"| p_e1_saw_planks_from_stripped
  i_tool_stone_flake --> p_e1_saw_planks_from_stripped
  p_e1_saw_planks_from_stripped --> |"x2"| i_board_plank_rough
  p_e1_saw_planks_from_stripped --> |"x1"| i_stick_dry_small
  i_stripped_log --> |"x1"| p_e1_carve_haft_from_stripped
  i_stone_flakes --> |"x1"| p_e1_carve_haft_from_stripped
  p_e1_carve_haft_from_stripped --> |"x3"| i_wood_haft
  p_e1_carve_haft_from_stripped --> |"x2"| i_stick_dry_small
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_e1_wash_dirt_for_clay proc;
  class p_e1_render_grease_tallow proc;
  class p_e1_ret_hemp_fiber proc;
  class p_e1_weave_sail_cloth proc;
  class p_e1_crush_grog proc;
  class p_e1_screen_temper_sand proc;
  class p_e1_fit_plain_bearing_wood proc;
  class p_e1_carve_wooden_peg proc;
  class p_e1_build_wooden_tub proc;
  class p_e1_build_charcoal_retort_kiln proc;
  class p_e1_char_retort proc;
  class p_e1_reduce_pitch proc;
  class p_e1_strip_log proc;
  class p_e1_saw_planks_from_stripped proc;
  class p_e1_carve_haft_from_stripped proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[stripped_log|1] :ci[tool_stone_flake|0] <span class="rc-arrow">→</span> :ci[board_plank_rough|2] :ci[stick_dry_small|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">200s</span> <span class="rc-tier">T0</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Score and split a stripped log lengthwise into rough flat planks. Slow without a metal saw, but the planks unlock shovel scoops and cooperage.</div>
<div class="rc-id"><code>e1_saw_planks_from_stripped</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[wood|8] <span class="rc-arrow">→</span> :ci[charcoal|5] :ci[tar|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#charcoal_retort_kiln">Charcoal Retort Kiln</a></span> <span class="rc-time">720s</span> <span class="rc-tier">T0</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Bake a sealed charge so it carbonises without burning; the offtake condenses the wood tar the clamp lets escape.</div>
<div class="rc-id"><code>e1_char_retort</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[earthenware_brick|6] :ci[clay|4] :ci[stone|4] <span class="rc-arrow">→</span> :ci[charcoal_retort_kiln|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">600s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Lay a sealed brick chamber with a condensing offtake; the wood gas is driven through it instead of up a vent.</div>
<div class="rc-id"><code>e1_build_charcoal_retort_kiln</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[dirt|4] :ci[bark_bucket_water|1] :ci[plant_fibers|1] <span class="rc-arrow">→</span> :ci[clay|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">30s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Slurry dirt with water in the bucket, let it settle, and screen the heavy clay fraction through plant fibre. Wet, dirty, low-yield -- but it works anywhere with dirt and a water source.</div>
<div class="rc-id"><code>e1_wash_dirt_for_clay</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[fat_raw|2] <span class="rc-arrow">→</span> :ci[grease_tallow|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#campfire_survival">Survival Campfire</a></span> <span class="rc-time">240s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Render trimmed fat low and slow, skim the clean tallow off the cracklings, and let it set hard.</div>
<div class="rc-id"><code>e1_render_grease_tallow</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[earthenware_brick|1] :ci[pestle_stone|0] <span class="rc-arrow">→</span> :ci[grog_crushed_ceramic_temper|2]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">180s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Pound a spare fired brick to grit; mixed back into raw clay it stops the shrink-cracks that ruin a pot.</div>
<div class="rc-id"><code>e1_crush_grog</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[plant_fibers|3] <span class="rc-arrow">→</span> :ci[hemp_fiber|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">360s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Soak the stalks until the woody core rots free, then beat and comb out the long bast -- the line fibre for cloth and packing.</div>
<div class="rc-id"><code>e1_ret_hemp_fiber</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[tar|2] <span class="rc-arrow">→</span> :ci[pitch|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#campfire_survival">Survival Campfire</a></span> <span class="rc-time">240s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Boil tar down until the light fractions cook off and it sets stiff -- pitch that seals seams hard instead of staying tacky.</div>
<div class="rc-id"><code>e1_reduce_pitch</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[wood|1] :ci[grease_tallow|1] <span class="rc-arrow">→</span> :ci[plain_bearing_wood|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">200s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Bore a hardwood block to the shaft and pack it with tallow; it runs cool enough for slow mill work.</div>
<div class="rc-id"><code>e1_fit_plain_bearing_wood</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[hemp_fiber|4] <span class="rc-arrow">→</span> :ci[sail_cloth|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">480s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Weave the line fibre tight on a warped frame; close, even cloth that holds wind without tearing.</div>
<div class="rc-id"><code>e1_weave_sail_cloth</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[log_medium_dry|1] :ci[tool_stone_flake|0] <span class="rc-arrow">→</span> :ci[stripped_log|1] :ci[forest_bark_slabs|2] :ci[forest_bark_strip|2]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">180s</span> <span class="rc-tier">T0</span> <span class="rc-bp">+2 byproducts</span></div>
<div class="rc-note">Score the bark, peel it off in slabs, and curl the inner bark into strips -- the log is now clean stock.</div>
<div class="rc-id"><code>e1_strip_log</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[sand|2] <span class="rc-arrow">→</span> :ci[temper_sand_or_grog|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">90s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Screen river sand to an even grit -- the sand option when no fired ceramic is spare to crush for grog.</div>
<div class="rc-id"><code>e1_screen_temper_sand</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[stripped_log|1] :ci[stone_flakes|1] <span class="rc-arrow">→</span> :ci[wood_haft|3] :ci[stick_dry_small|2]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">240s</span> <span class="rc-tier">T0</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Quarter the stripped log into hafts and trim the offcuts into kindling sticks.</div>
<div class="rc-id"><code>e1_carve_haft_from_stripped</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[wood|1] :ci[stone_flakes|1] <span class="rc-arrow">→</span> :ci[wooden_peg|4]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">150s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Split a billet and whittle a handful of tapered pegs; driven dry they swell into the hole and lock.</div>
<div class="rc-id"><code>e1_carve_wooden_peg</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[board_plank_rough|2] :ci[rope|1] <span class="rc-arrow">→</span> :ci[wooden_tub|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">300s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Stand split staves in a ring and bind them with a tight rope hoop; swelling wood seals the seams.</div>
<div class="rc-id"><code>e1_build_wooden_tub</code></div>
</div>
</div>

## Stone age tools
<p class="chapter-stats">16 recipes</p>

```mermaid
%%{init: {'securityLevel':'loose','flowchart':{'htmlLabels':true,'curve':'basis','nodeSpacing':38,'rankSpacing':70}, 'theme':'base', 'themeVariables':{'fontSize':'13px'}}}%%
graph LR
  i_stone["<img src='../../assets/icons/stone.png' class='mmd-ico' />fieldstone"]
  i_hammerstone["<img src='../../assets/icons/hammerstone.png' class='mmd-ico' />hammerstone"]
  i_stone_adze_head["<img src='../../assets/icons/stone_adze_head.png' class='mmd-ico' />stone adze head"]
  i_stone_flakes["<img src='../../assets/icons/stone_flakes.png' class='mmd-ico' />stone flakes"]
  i_stone_hoe_blade["<img src='../../assets/icons/stone_hoe_blade.png' class='mmd-ico' />stone hoe blade"]
  i_wood_haft["<img src='../../assets/icons/wood_haft.png' class='mmd-ico' />wood haft"]
  i_rope["<img src='../../assets/icons/rope.png' class='mmd-ico' />rope"]
  i_adze["<img src='../../assets/icons/adze.png' class='mmd-ico' />adze"]
  i_hoe["<img src='../../assets/icons/hoe.png' class='mmd-ico' />hoe"]
  i_board_plank_rough["<img src='../../assets/icons/board_plank_rough.png' class='mmd-ico' />rough board plank"]
  i_shovel["<img src='../../assets/icons/shovel.png' class='mmd-ico' />crude shovel"]
  i_wood["<img src='../../assets/icons/wood.png' class='mmd-ico' />construction wood"]
  i_mallet["<img src='../../assets/icons/mallet.png' class='mmd-ico' />mallet"]
  i_wedge["<img src='../../assets/icons/wedge.png' class='mmd-ico' />wedge"]
  i_lever_pry_bar["<img src='../../assets/icons/lever_pry_bar.png' class='mmd-ico' />lever (pry bar)"]
  i_gold_pan["<img src='../../assets/icons/gold_pan.png' class='mmd-ico' />gold pan"]
  i_stick_dry_small["<img src='../../assets/icons/stick_dry_small.png' class='mmd-ico' />small dry sticks"]
  i_chisel["<img src='../../assets/icons/chisel.png' class='mmd-ico' />chisel"]
  i_drawknife["<img src='../../assets/icons/drawknife.png' class='mmd-ico' />drawknife"]
  i_bow_saw_frame["<img src='../../assets/icons/bow_saw_frame.png' class='mmd-ico' />bow saw frame"]
  i_shaft_wood_round["<img src='../../assets/icons/shaft_wood_round.png' class='mmd-ico' />wooden shaft (round)"]
  i_bow_drill["<img src='../../assets/icons/bow_drill.png' class='mmd-ico' />bow drill"]
  i_plant_fibers["<img src='../../assets/icons/plant_fibers.png' class='mmd-ico' />plant fibers"]
  i_spindle_drill["<img src='../../assets/icons/spindle_drill.png' class='mmd-ico' />spindle drill"]
  i_measuring_cord["<img src='../../assets/icons/measuring_cord.png' class='mmd-ico' />measuring cord"]
  i_plumb_bob["<img src='../../assets/icons/plumb_bob.png' class='mmd-ico' />plumb bob"]
  p_e1_knap_stone_adze_head{"Camp Marker"}
  p_e1_knap_stone_hoe_blade{"Camp Marker"}
  p_e1_assemble_adze{"Camp Marker"}
  p_e1_assemble_hoe{"Camp Marker"}
  p_e1_assemble_shovel_wood{"Camp Marker"}
  p_e1_assemble_mallet{"Camp Marker"}
  p_e1_carve_wedge{"Camp Marker"}
  p_e1_carve_lever_pry_bar{"Camp Marker"}
  p_e1_carve_gold_pan{"Camp Marker"}
  p_e1_haft_chisel{"Camp Marker"}
  p_e1_haft_drawknife{"Camp Marker"}
  p_e1_build_bow_saw_frame{"Camp Marker"}
  p_e1_build_bow_drill{"Camp Marker"}
  p_e1_build_spindle_drill{"Camp Marker"}
  p_e1_knot_measuring_cord{"Camp Marker"}
  p_e1_shape_plumb_bob{"Camp Marker"}
  i_stone --> |"x2"| p_e1_knap_stone_adze_head
  i_hammerstone --> p_e1_knap_stone_adze_head
  p_e1_knap_stone_adze_head --> |"x1"| i_stone_adze_head
  p_e1_knap_stone_adze_head --> |"x2"| i_stone_flakes
  i_stone --> |"x2"| p_e1_knap_stone_hoe_blade
  i_hammerstone --> p_e1_knap_stone_hoe_blade
  p_e1_knap_stone_hoe_blade --> |"x1"| i_stone_hoe_blade
  p_e1_knap_stone_hoe_blade --> |"x2"| i_stone_flakes
  i_stone_adze_head --> |"x1"| p_e1_assemble_adze
  i_wood_haft --> |"x1"| p_e1_assemble_adze
  i_rope --> |"x1"| p_e1_assemble_adze
  p_e1_assemble_adze --> |"x1"| i_adze
  i_stone_hoe_blade --> |"x1"| p_e1_assemble_hoe
  i_wood_haft --> |"x1"| p_e1_assemble_hoe
  i_rope --> |"x1"| p_e1_assemble_hoe
  p_e1_assemble_hoe --> |"x1"| i_hoe
  i_board_plank_rough --> |"x1"| p_e1_assemble_shovel_wood
  i_wood_haft --> |"x1"| p_e1_assemble_shovel_wood
  i_rope --> |"x1"| p_e1_assemble_shovel_wood
  p_e1_assemble_shovel_wood --> |"x1"| i_shovel
  i_wood --> |"x1"| p_e1_assemble_mallet
  i_wood_haft --> |"x1"| p_e1_assemble_mallet
  i_rope --> |"x1"| p_e1_assemble_mallet
  p_e1_assemble_mallet --> |"x1"| i_mallet
  i_wood --> |"x1"| p_e1_carve_wedge
  i_stone_flakes --> |"x1"| p_e1_carve_wedge
  p_e1_carve_wedge --> |"x1"| i_wedge
  i_wood --> |"x1"| p_e1_carve_lever_pry_bar
  i_stone_flakes --> |"x1"| p_e1_carve_lever_pry_bar
  p_e1_carve_lever_pry_bar --> |"x1"| i_lever_pry_bar
  i_wood --> |"x1"| p_e1_carve_gold_pan
  i_stone_flakes --> |"x1"| p_e1_carve_gold_pan
  p_e1_carve_gold_pan --> |"x1"| i_gold_pan
  i_stone_flakes --> |"x1"| p_e1_haft_chisel
  i_stick_dry_small --> |"x1"| p_e1_haft_chisel
  i_rope --> |"x1"| p_e1_haft_chisel
  p_e1_haft_chisel --> |"x1"| i_chisel
  i_stone_flakes --> |"x1"| p_e1_haft_drawknife
  i_stick_dry_small --> |"x2"| p_e1_haft_drawknife
  i_rope --> |"x1"| p_e1_haft_drawknife
  p_e1_haft_drawknife --> |"x1"| i_drawknife
  i_wood --> |"x1"| p_e1_build_bow_saw_frame
  i_rope --> |"x1"| p_e1_build_bow_saw_frame
  p_e1_build_bow_saw_frame --> |"x1"| i_bow_saw_frame
  i_stick_dry_small --> |"x1"| p_e1_build_bow_drill
  i_rope --> |"x1"| p_e1_build_bow_drill
  i_shaft_wood_round --> |"x1"| p_e1_build_bow_drill
  p_e1_build_bow_drill --> |"x1"| i_bow_drill
  i_shaft_wood_round --> |"x1"| p_e1_build_spindle_drill
  i_stone --> |"x1"| p_e1_build_spindle_drill
  i_plant_fibers --> |"x2"| p_e1_build_spindle_drill
  p_e1_build_spindle_drill --> |"x1"| i_spindle_drill
  i_rope --> |"x1"| p_e1_knot_measuring_cord
  i_stick_dry_small --> |"x1"| p_e1_knot_measuring_cord
  p_e1_knot_measuring_cord --> |"x1"| i_measuring_cord
  i_stone --> |"x1"| p_e1_shape_plumb_bob
  i_stone_flakes --> |"x1"| p_e1_shape_plumb_bob
  i_plant_fibers --> |"x1"| p_e1_shape_plumb_bob
  p_e1_shape_plumb_bob --> |"x1"| i_plumb_bob
  classDef proc fill:#3b2f1e,stroke:#d98a2b,stroke-width:1px,color:#ffd9a0;
  classDef world fill:#1d2a1d,stroke:#5a8f4d,color:#bfe6b0;
  class p_e1_knap_stone_adze_head proc;
  class p_e1_knap_stone_hoe_blade proc;
  class p_e1_assemble_adze proc;
  class p_e1_assemble_hoe proc;
  class p_e1_assemble_shovel_wood proc;
  class p_e1_assemble_mallet proc;
  class p_e1_carve_wedge proc;
  class p_e1_carve_lever_pry_bar proc;
  class p_e1_carve_gold_pan proc;
  class p_e1_haft_chisel proc;
  class p_e1_haft_drawknife proc;
  class p_e1_build_bow_saw_frame proc;
  class p_e1_build_bow_drill proc;
  class p_e1_build_spindle_drill proc;
  class p_e1_knot_measuring_cord proc;
  class p_e1_shape_plumb_bob proc;
```

<div class="recipe-grid" markdown>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[stone_adze_head|1] :ci[wood_haft|1] :ci[rope|1] <span class="rc-arrow">→</span> :ci[adze|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">240s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Seat the bit transverse on a knee-bend haft and lash it tight; the edge faces the worker.</div>
<div class="rc-id"><code>e1_assemble_adze</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[stick_dry_small|1] :ci[rope|1] :ci[shaft_wood_round|1] <span class="rc-arrow">→</span> :ci[bow_drill|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">150s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Loop the cord once around a straight spindle so sawing the bow spins it -- drills holes and starts fire.</div>
<div class="rc-id"><code>e1_build_bow_drill</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[wood|1] :ci[rope|1] <span class="rc-arrow">→</span> :ci[bow_saw_frame|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">180s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Bend a green stave into a bow and string it tight; the cutting blade is fitted later when metal exists.</div>
<div class="rc-id"><code>e1_build_bow_saw_frame</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[stone_flakes|1] :ci[stick_dry_small|1] :ci[rope|1] <span class="rc-arrow">→</span> :ci[chisel|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">180s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Set a narrow flake end-on in a split stick and bind it so a mallet blow drives straight through.</div>
<div class="rc-id"><code>e1_haft_chisel</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[stone_flakes|1] :ci[stick_dry_small|2] :ci[rope|1] <span class="rc-arrow">→</span> :ci[drawknife|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">200s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Lash a long flake between two short grips so it can be pulled toward you to shave bark and round stock.</div>
<div class="rc-id"><code>e1_haft_drawknife</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[wood|1] :ci[stone_flakes|1] <span class="rc-arrow">→</span> :ci[gold_pan|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">240s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Hollow a shallow batea from a wood round; the gentle dish lets heavy fines settle while you swirl off the light sand.</div>
<div class="rc-id"><code>e1_carve_gold_pan</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[stone_hoe_blade|1] :ci[wood_haft|1] :ci[rope|1] <span class="rc-arrow">→</span> :ci[hoe|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">240s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Lash the blade across the haft at a chopping-down angle for turning soil.</div>
<div class="rc-id"><code>e1_assemble_hoe</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[wood|1] :ci[stone_flakes|1] <span class="rc-arrow">→</span> :ci[lever_pry_bar|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">150s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Strip a stout pole and flatten one end into a prying tip; the longer the pole the more it lifts.</div>
<div class="rc-id"><code>e1_carve_lever_pry_bar</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[wood|1] :ci[wood_haft|1] :ci[rope|1] <span class="rc-arrow">→</span> :ci[mallet|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">240s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Bore a dense billet, drive the haft through, and bind the cheeks so it cannot split out.</div>
<div class="rc-id"><code>e1_assemble_mallet</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[rope|1] :ci[stick_dry_small|1] <span class="rc-arrow">→</span> :ci[measuring_cord|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">90s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Tie even knots along a stretched rope as repeatable length marks; wind it on a stick to carry.</div>
<div class="rc-id"><code>e1_knot_measuring_cord</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[stone|1] :ci[stone_flakes|1] :ci[plant_fibers|1] <span class="rc-arrow">→</span> :ci[plumb_bob|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">120s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Peck a groove round a small stone, tie on a line, and let it hang -- it finds true vertical every time.</div>
<div class="rc-id"><code>e1_shape_plumb_bob</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[board_plank_rough|1] :ci[wood_haft|1] :ci[rope|1] <span class="rc-arrow">→</span> :ci[shovel|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">300s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Dish a rough board into a scoop, split the haft to grip its neck, and lash it fast.</div>
<div class="rc-id"><code>e1_assemble_shovel_wood</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[shaft_wood_round|1] :ci[stone|1] :ci[plant_fibers|2] <span class="rc-arrow">→</span> :ci[spindle_drill|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">180s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Weight a spindle with a holed stone whorl so a flick of the cords keeps it turning through the bore.</div>
<div class="rc-id"><code>e1_build_spindle_drill</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[stone|2] :ci[hammerstone|0] <span class="rc-arrow">→</span> :ci[stone_adze_head|1] :ci[stone_flakes|2]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">540s</span> <span class="rc-tier">T0</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Knap a core to a gouging lip set across the long axis, then grind it keen for transverse cuts.</div>
<div class="rc-id"><code>e1_knap_stone_adze_head</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[stone|2] :ci[hammerstone|0] <span class="rc-arrow">→</span> :ci[stone_hoe_blade|1] :ci[stone_flakes|2]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">540s</span> <span class="rc-tier">T0</span> <span class="rc-bp">+1 byproduct</span></div>
<div class="rc-note">Flake a flat, broad blade and grind one long edge; it lashes broad-side to the haft.</div>
<div class="rc-id"><code>e1_knap_stone_hoe_blade</code></div>
</div>
<div class="recipe-card cat-crafting" markdown>
<div class="rc-flow">:ci[wood|1] :ci[stone_flakes|1] <span class="rc-arrow">→</span> :ci[wedge|1]</div>
<div class="rc-meta"><span class="rc-stn"><a class="stn-link" href="../../stations/#camp_marker_basic">Camp Marker</a></span> <span class="rc-time">120s</span> <span class="rc-tier">T0</span></div>
<div class="rc-note">Whittle a hardwood billet to a clean taper; season it hard so it bites instead of crushing.</div>
<div class="rc-id"><code>e1_carve_wedge</code></div>
</div>
</div>
