---
title: Tier 7 — Space
---
<div class="tierwrap" data-tier="space" markdown>

# Tier 7 — Space

> The win. Cryogenic oxygen, titanium, superalloys, composites — assemble an engine, a stage, a vehicle, and launch.

<div class="tier-gate" markdown>
<div class="tier-gate__num">7</div>
<div class="tier-gate__body" markdown>
<div class="tier-gate__name">Tier 7 — Space</div>
<div class="tier-gate__flow"><span class="tg-in">Unlocks after: Wafers, automation, superalloys.</span><span class="tg-arrow">→</span><span class="tg-out">Leads to: Cryogenics, titanium, the rocket. ORBITAL LAUNCH (win).</span></div>
</div>
</div>

<p class="chapter-stats">14 quests · 12 on the win-path · 1 branches</p>

<section class="quest-card qtype-info" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-info">Briefing</span>
<h3 class="quest-card__title">Rockets, Reactors and Orbit</h3>
</header>
<div class="quest-summary" markdown>
### Tier 6 is where the factory looks outward

You have an automated, solid-state industrial base.
It produces electricity, refined materials, and precision components without you touching most of it.

Tier 6 uses that base to do something no earlier tier could: leave.

The arc of this chapter:

- **Propellants and test stands** -- liquid-fuel rocketry. Kerosene and LOX. Instrumented engine runs before anything leaves the ground.
- **First orbital launch** -- a three-stage rocket placing hardware in orbit. Not a suborbital hop. Actual orbit.
- **Satellite network** -- communications and sensing infrastructure. Your world gains persistent orbital coverage.
- **Nuclear base-load power** -- the grid problem at this scale is real. Nuclear solves it without burning anything.
- **Orbital station** -- orbit becomes a place where work happens, not just a trajectory.
- **Lunar ISRU demo** -- a robotic lander extracts resources in-situ. The Moon starts feeding the supply chain.
- **Mass driver** -- bulk lunar material launched without rockets. Energy cost drops by an order of magnitude.
- **Orbital solar power** -- the grid reaches into space. Base-load from orbit, beamed down.

This is only possible because T3 through T5 automated the supply chain that feeds it.
Without the blast furnace chain, the ore processing line, the solid-state fab -- none of this lifts off.
</div>
</section>

## Launch & Orbital Infrastructure

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Propellants and Test Stands</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Rockets, Reactors and Orbit</em></p>
<div class="quest-summary" markdown>
Refine kerosene and liquid oxygen, build a vertical engine test stand and fire modern liquid-fuel rocket engines under instrumentation.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a vertical engine test stand.
    <br>yields: :ci[test_stand_vertical|1]
- <span class="task-kind task-retrieve">retrieve</span> Produce and load propellants for test firing.
    <br>yields: :ci[propellant_kerosene_refined|40] :ci[propellant_lox_distilled|40]
- <span class="task-kind task-retrieve">retrieve</span> Fire kerolox test engines with high-pressure instruments.
    <br>yields: :ci[rocket_engine_kerolox_test|2] :ci[instrument_pressure_high|4]
</div>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">First Orbital Launch</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Propellants and Test Stands</em></p>
<div class="quest-summary" markdown>
Construct a launch pad and three-stage rocket capable of placing a small uncrewed satellite into low orbit, then prove you can reach space reliably.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a launch pad complex and tracking radar.
    <br>yields: :ci[launch_pad_complex_basic|1] :ci[tracking_radar_ground|1]
- <span class="task-kind task-retrieve">retrieve</span> Assemble a three-stage orbital rocket with a tech demo satellite.
    <br>yields: :ci[rocket_stack_orbital_three_stage|1] :ci[satellite_tech_demo|1]
</div>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Satellites for Comms and Sensing</h3>
</header>
<p class="quest-pre">Unlocks after: <em>First Orbital Launch</em></p>
<div class="quest-summary" markdown>
Deploy a small constellation of communication or relay satellites and tie them into ground stations so your world has continuous coverage over key regions.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Launch three communication satellites into orbit.
    <br>yields: :ci[satellite_comms_basic|3]
- <span class="task-kind task-retrieve">retrieve</span> Have or place ground stations, tracking radar and a relay station.
    <br>yields: :ci[ground_station_dish|1] :ci[tracking_radar_ground|1] :ci[relay_station_hilltop|1]
</div>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Nuclear Power for Heavy Industry</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Propellants and Test Stands</em></p>
<div class="quest-summary" markdown>
Build a grid-connected nuclear power station that can provide steady base-load electricity for launches and heavy industry without relying on fossil fuels.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a light water reactor and cooling towers.
    <br>yields: :ci[reactor_nuclear_light_water|1] :ci[cooling_tower_pair|1]
- <span class="task-kind task-retrieve">retrieve</span> Load enriched uranium fuel rods into the reactor.
    <br>yields: :ci[fuel_rod_uranium_enriched|40]
- <span class="task-kind task-retrieve">retrieve</span> Connect the reactor output to a high-voltage switchyard.
    <br>yields: :ci[switchyard_high_voltage|1]
</div>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Orbital Workshop and Habitat</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Satellites for Comms and Sensing</em></p>
<div class="quest-summary" markdown>
Assemble a modular orbital station with power, life support and docking, turning orbit from a fly-through into a place where work can happen continuously.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Launch and assemble the core station module with solar trusses.
    <br>yields: :ci[station_module_core|1] :ci[station_module_solar_truss|2]
- <span class="task-kind task-retrieve">retrieve</span> Install docking ports and a life support loop.
    <br>yields: :ci[docking_port_standard|2] :ci[life_support_loop_basic|1]
</div>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Robotic Lander and Lunar ISRU Demo</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Orbital Workshop and Habitat</em></p>
<div class="quest-summary" markdown>
Send an uncrewed lander to a lunar site, drill regolith or ice, run a small in-situ resource utilisation demo and return data or samples to orbit or ground.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Build a robotic lunar lander with a regolith drill.
    <br>yields: :ci[lander_lunar_robotic|1] :ci[drill_regolith_robotic|1]
- <span class="task-kind task-retrieve">retrieve</span> Equip the lander with an ISRU demo unit and sample return capsule.
    <br>yields: :ci[isru_ice_extractor_demo|1] :ci[sample_return_capsule|1]
</div>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Mass Driver for Bulk Lunar Exports</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Robotic Lander and Lunar ISRU Demo</em></p>
<div class="quest-summary" markdown>
Construct a prototype electromagnetic mass driver on the Moon to fling processed regolith or ore pods into lunar orbit instead of launching them by rocket.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Build the mass driver track with guidance coil arrays.
    <br>yields: :ci[mass_driver_lunar_track|1] :ci[guidance_coil_array|4]
- <span class="task-kind task-retrieve">retrieve</span> Install a lunar solar power plant and bulk regolith hopper.
    <br>yields: :ci[power_plant_lunar_solar|1] :ci[hopper_regolith_bulk|1]
</div>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Solar Power from Orbit</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Orbital Workshop and Habitat</em></p>
<div class="quest-summary" markdown>
Build a solar power satellite with large arrays in orbit that beams energy down to a rectenna field, supplementing your ground grid with space-based power.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Build and launch a solar power satellite with attitude control.
    <br>yields: :ci[sps_solar_array_huge|1] :ci[attitude_control_array|1]
- <span class="task-kind task-retrieve">retrieve</span> Install the microwave beamer and ground rectenna field.
    <br>yields: :ci[microwave_beamer_downlink|1] :ci[rectenna_ground_field|1]
</div>
</section>

## Milestone & Trade-In

<section class="quest-card qtype-checkpoint" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-checkpoint">Checkpoint</span>
<h3 class="quest-card__title">Tier 6 -- Space Age and High-Energy Online</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Solar Power from Orbit, Mass Driver for Bulk Lunar Exports, Zircaloy and Inconel Superalloy</em></p>
<div class="quest-summary" markdown>
Confirm that liquid-fuel rocketry, orbital launch, satellite networks, nuclear base-load power, an orbital station, lunar ISRU, a mass driver and space-based solar power are all operating together in your ecosystem.
</div>
<p class="quest-rewards">Rewards: :ci[lootbag_tier_VII|1]</p>
</section>

<section class="quest-card qtype-exchange" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-exchange">Exchange</span>
<h3 class="quest-card__title">Trade In: Tech VI → VII</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Tier 6 -- Space Age and High-Energy Online</em></p>
<div class="quest-summary" markdown>
Exchange Tier VI tech tokens for Tier VII. Repeatable.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-do">do</span> 
</div>
<p class="quest-rewards costs">Costs: :ci[tech_VI|5]</p>
<p class="quest-rewards">Rewards: :ci[tech_VII|1]</p>
</section>

## Spaceflight Materials

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Titanium Processing Chain</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Propellants and Test Stands</em></p>
<div class="quest-summary" markdown>
Process ilmenite ore through the full titanium chain: fluidized-bed chlorination (TiO2 + 2Cl2 + 2C → TiCl4 + 2CO) → fractional distillation → Hunter reduction (TiCl4 + 4Na → Ti + 4NaCl) → vacuum arc remelting (VAR, triple-melt for rotating parts) → Ti-6Al-4V alloying → plate forging and rolling.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Chlorinate ilmenite ore in a fluidized bed to produce TiCl4 ('tickle').
    <br>yields: :ci[titanium_tetrachloride|4]
- <span class="task-kind task-retrieve">retrieve</span> Run Hunter reduction (TiCl4 + 4Na) and vacuum arc remelt the sponge.
    <br>yields: :ci[titanium_sponge|4] :ci[titanium_ingot|2]
- <span class="task-kind task-retrieve">retrieve</span> VAR-alloy Ti-6Al-4V and hot-roll titanium plate for structural use.
    <br>yields: :ci[alloy_ti_6al_4v|2] :ci[titanium_plate|4]
</div>
<p class="quest-rewards">Rewards: :ci[titanium_plate|4]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Tungsten and Ferroniobium</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Propellants and Test Stands</em></p>
<div class="quest-summary" markdown>
Produce refractory and strategic metals: wolframite → NaOH pressure digest → solvent extraction → APT precipitation → calcine WO3 → H2 reduction → W powder → press/sinter/swage W rod; and columbite → HF digest → MIBK solvent extraction → Nb2O5 calcine → aluminothermic reduction → ferroniobium.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Digest wolframite in NaOH, solvent-extract, and calcine APT to produce WO3.
    <br>yields: :ci[tungsten_oxide|4]
- <span class="task-kind task-retrieve">retrieve</span> H2-reduce WO3 to W powder, cold-press, sinter at 2300u00b0C, and swage into dense W rods.
    <br>yields: :ci[tungsten_powder|4] :ci[tungsten_sintered_rod|2]
- <span class="task-kind task-retrieve">retrieve</span> HF-digest columbite, MIBK-extract Nb, calcine to Nb2O5, and aluminothermically reduce to ferroniobium.
    <br>yields: :ci[niobium_oxide|2] :ci[ferroniobium|2]
</div>
<p class="quest-rewards">Rewards: :ci[tungsten_sintered_rod|2] :ci[ferroniobium|2]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Zircaloy and Inconel Superalloy</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Titanium Processing Chain, Tungsten and Ferroniobium</em></p>
<div class="quest-summary" markdown>
Complete the high-performance alloy matrix. Zirconium chain: zircon → carbo-chlorination → ZrCl4 → Hf separation (< 100 ppm Hf for nuclear grade) → Kroll reduction → vacuum-induction melt → zircaloy-2 cladding alloy (Zr + 1.3% Sn + 0.1% Fe + 0.1% Cr). Superalloy chain: nickel cathode + ferrochrome + steel_ingot + ferroniobium → VIM then VAR → Inconel 718-like ingot.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Carbo-chlorinate zircon to ZrCl4 and Kroll-reduce to hafnium-free sponge.
    <br>yields: :ci[zirconium_tetrachloride|4] :ci[zirconium_sponge|4]
- <span class="task-kind task-retrieve">retrieve</span> Vacuum-induction melt zircaloy-2 from Hf-free sponge (nuclear-grade fuel rod cladding).
    <br>yields: :ci[alloy_zircaloy|2]
- <span class="task-kind task-retrieve">retrieve</span> VIM + VAR melt Inconel 718-like superalloy from nickel cathode + ferrochrome + ferroniobium.
    <br>yields: :ci[inconel_ingot|2]
</div>
<p class="quest-rewards">Rewards: :ci[alloy_zircaloy|2] :ci[inconel_ingot|1]</p>
</section>

</div>

<div class="chapter-nav">[← Solid State](6-solidstate.md)</div>
