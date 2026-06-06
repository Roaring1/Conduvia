---
title: Tier 5 — Electric
---
<div class="tierwrap" data-tier="electric" markdown>

# Tier 5 — Electric

> The chemistry gateway. An AC grid powers electrolysis: aluminum, chlor-alkali, ferroalloys, metallurgical silicon.

<div class="tier-gate" markdown>
<div class="tier-gate__num">5</div>
<div class="tier-gate__body" markdown>
<div class="tier-gate__name">Tier 5 — Electric</div>
<div class="tier-gate__flow"><span class="tg-in">Unlocks after: Steel and a DC dynamo.</span><span class="tg-arrow">→</span><span class="tg-out">Leads to: AC grid, electrolysis, arc furnace — the chemistry gateway.</span></div>
</div>
</div>

<p class="chapter-stats">17 quests · 15 on the win-path · 1 branches</p>

<section class="quest-card qtype-info" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-info">Briefing</span>
<h3 class="quest-card__title">AC Grids and Early Automation</h3>
</header>
<div class="quest-summary" markdown>
### Tier 4 is the "site becomes a power system"

Steel/DC got you: heavy plant, dynamos, local DC networks, and motors.
Now you add what makes power go *far* and *scale*:

- AC generation and switching practice
- transformers (step up / step down)
- three-phase transmission for distance + motors
- rectification back to DC for old loads and heavy processes
- early electronics (vacuum tubes) as the bridge into instrumentation + control
- plant-wide meters, relays, alarms
- early regulation and automatic control
- a central control room that makes the plant readable
</div>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Test Alternating Current</h3>
</header>
<p class="quest-pre">Unlocks after: <em>AC Grids and Early Automation</em></p>
<div class="quest-summary" markdown>
### Build a small AC test bay

Goal: a controlled place where you can safely energize circuits, switch loads,
and prove you can run lamps without "mystery wiring".

This is where AC becomes a tool instead of a theory.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a small AC generator/alternator for test power.
    <br>yields: :ci[generator_ac_small|1]
- <span class="task-kind task-retrieve">retrieve</span> Have or place a basic switchboard panel (mounting + isolation point).
    <br>yields: :ci[switchboard_panel_wooden|1]
- <span class="task-kind task-retrieve">retrieve</span> Stock heavy knife switches for isolation points.
    <br>yields: :ci[knife_switch_heavy|2]
- <span class="task-kind task-retrieve">retrieve</span> Bring lamps online (fixtures + carbon-filament lamps).
    <br>yields: :ci[lamp_fixture_industrial|4] :ci[incandescent_lamp_carbon|4]
- <span class="task-kind task-craft">craft</span> Craft the AC generator set (optional if obtained another way). <span class="task-opt">optional</span>
    <br>yields: :ci[generator_ac_small|1]
</div>
<p class="quest-rewards">Rewards: :ci[copper_wire_insulated|20] :ci[fuse_rewireable|4]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Step Up, Step Down</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Test Alternating Current</em></p>
<div class="quest-summary" markdown>
### Build a transformer yard

Place step-up near generation and step-down near loads.
Run a short "high voltage" span between them using proper insulators.

This teaches the real AC advantage: distance without absurd copper loss.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a step-up transformer near generation, and a step-down near loads.
    <br>yields: :ci[transformer_step_up|1] :ci[transformer_step_down|1]
- <span class="task-kind task-retrieve">retrieve</span> Stock insulators, insulated wire, and copper bus bars for a safe yard build.
    <br>yields: :ci[porcelain_insulator_pin|24] :ci[copper_wire_insulated|80] :ci[bus_bar_copper|8]
- <span class="task-kind task-craft">craft</span> Craft the transformer sets (optional if obtained another way). <span class="task-opt">optional</span>
    <br>yields: :ci[transformer_step_up|1] :ci[transformer_step_down|1]
</div>
<p class="quest-rewards">Rewards: :ci[porcelain_insulator_pin|12] :ci[bus_bar_copper|4]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Switchgear & Protection</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Step Up, Step Down</em></p>
<div class="quest-summary" markdown>
### Switchgear and protection discipline

Before you push power farther, you need safe isolation and protection:
switches, fuses, bus bars, and insulating hardware.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place switchboard panels for mounting protection hardware.
    <br>yields: :ci[switchboard_panel_wooden|2]
- <span class="task-kind task-retrieve">retrieve</span> Stock heavy knife switches and rewireable fuses for isolation and protection.
    <br>yields: :ci[knife_switch_heavy|4] :ci[fuse_rewireable|12]
- <span class="task-kind task-retrieve">retrieve</span> Stock copper bus bars and insulators for safe mounting and clearance.
    <br>yields: :ci[bus_bar_copper|6] :ci[porcelain_insulator_pin|12]
</div>
<p class="quest-rewards">Rewards: :ci[knife_switch_heavy|2] :ci[fuse_rewireable|6]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Three-Phase for Distance and Motors</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Switchgear & Protection</em></p>
<div class="quest-summary" markdown>
### Upgrade to three-phase

Three-phase is the serious industrial standard:
smooth rotating fields for motors, and copper-efficient transmission.

Bring up a three-phase alternator and a district AC network segment.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a three-phase generator/alternator.
    <br>yields: :ci[generator_ac_three_phase|1]
- <span class="task-kind task-retrieve">retrieve</span> Have or place a district AC network segment (substation/network anchor).
    <br>yields: :ci[network_ac_district|1]
- <span class="task-kind task-retrieve">retrieve</span> Stock the extra insulators and insulated wire required for multi-phase distribution.
    <br>yields: :ci[porcelain_insulator_pin|36] :ci[copper_wire_insulated|120]
</div>
<p class="quest-rewards">Rewards: :ci[copper_wire_insulated|40] :ci[porcelain_insulator_pin|12]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Induction Motors on the Floor</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Three-Phase for Distance and Motors</em></p>
<div class="quest-summary" markdown>
### Put motors where the work is

Replace some shaft-only dependency with local induction motors.
Not everything becomes electric overnight -- but critical tools stop being hostage to long line shafts.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place induction motors for key tools/hoists.
    <br>yields: :ci[motor_ac_induction_small|4]
- <span class="task-kind task-retrieve">retrieve</span> Keep some mechanical distribution parts on hand (transition is real: shafts + belts don't instantly vanish).
    <br>yields: :ci[line_shaft_wrought|2] :ci[flat_belt_leather|4]
- <span class="task-kind task-retrieve">retrieve</span> Have or place an electric-capable machine shop bay.
    <br>yields: :ci[machine_shop_electric|1]
</div>
<p class="quest-rewards">Rewards: :ci[motor_ac_induction_small|2]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Meters, Relays and Alarms</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Induction Motors on the Floor</em></p>
<div class="quest-summary" markdown>
### Make the plant readable and protected

Install meters, relays, and alarms so operators can *see load* and *get warned*
before failures cascade.

Target at least:
- one boiler house feed
- one generator feeder
- one outgoing line/load bay
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Stock panel meters: ammeters and voltmeters.
    <br>yields: :ci[instrument_ammeter_panel|4] :ci[instrument_voltmeter_panel|4]
- <span class="task-kind task-retrieve">retrieve</span> Stock relays and alarms for basic protection and operator warning.
    <br>yields: :ci[relay_electromagnetic|8] :ci[alarm_bell_electric|2]
- <span class="task-kind task-retrieve">retrieve</span> Stock protection + isolation hardware: switches and fuses.
    <br>yields: :ci[knife_switch_heavy|4] :ci[fuse_rewireable|12]
</div>
<p class="quest-rewards">Rewards: :ci[relay_electromagnetic|4] :ci[fuse_rewireable|6]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">AC In, Heavy DC Out</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Meters, Relays and Alarms</em></p>
<div class="quest-summary" markdown>
### Feed DC loads from the AC plant

You already own DC infrastructure from Tier 3.
Now you build the bridge: a rectifier bay that takes incoming AC and produces heavy DC.

This is historically honest: AC doesn't delete DC -- it *feeds and extends it*.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a mercury-arc rectifier set (or equivalent heavy rectifier).
    <br>yields: :ci[rectifier_mercury_arc|1]
- <span class="task-kind task-retrieve">retrieve</span> Stock copper bus bars, switches, and fuses for a protected DC output bay.
    <br>yields: :ci[bus_bar_copper|8] :ci[switchboard_panel_wooden|1] :ci[knife_switch_heavy|4] :ci[fuse_rewireable|8]
</div>
<p class="quest-rewards">Rewards: :ci[bus_bar_copper|4]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Vacuum Tubes: First Electronics</h3>
</header>
<p class="quest-pre">Unlocks after: <em>AC In, Heavy DC Out</em></p>
<div class="quest-summary" markdown>
### Build the first electronics capability

Set up a glass + vacuum bench and produce simple diodes and triodes.
You're not building a full radio stack here -- you're proving:
- one-way conduction (diode)
- controlled gain/switching behavior (triode)

This becomes a bridge into sensing, amplification, and control.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a glass bench and lab vacuum pump (the minimum tube-making setup).
    <br>yields: :ci[glass_bench|1] :ci[vacuum_pump_lab|1]
- <span class="task-kind task-retrieve">retrieve</span> Have a filament supply (low-voltage DC) for tube heating and test circuits.
    <br>yields: :ci[filament_supply_dc|1]
- <span class="task-kind task-produce">produce</span> Produce a starter batch of diodes and triodes.
</div>
<p class="quest-rewards">Rewards: :ci[tube_diode_glass|4] :ci[tube_triode_glass|4]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Regulators and Pneumatic Control</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Vacuum Tubes: First Electronics</em></p>
<div class="quest-summary" markdown>
### Regulators and closed-loop control

Bring in early automatic regulation (pneumatic/analog controllers):
- sensors read process value
- regulators compare to a setpoint
- control valves move steam or feedwater

This is the shift from "watching gauges" to supervising systems that hold steady on their own.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have regulators/controllers available (pneumatic or analog control class).
    <br>yields: :ci[controller_regulator_pneumatic|2]
- <span class="task-kind task-retrieve">retrieve</span> Stock sensors for pressure and level measurement.
    <br>yields: :ci[sensor_pressure_boiler|2] :ci[sensor_level_tank|2]
- <span class="task-kind task-retrieve">retrieve</span> Stock control valves so the controller can actually move the process.
    <br>yields: :ci[control_valve_steam|2]
</div>
<p class="quest-rewards">Rewards: :ci[sensor_pressure_boiler|2] :ci[control_valve_steam|1]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Control Room and Mimic Board</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Regulators and Pneumatic Control</em></p>
<div class="quest-summary" markdown>
### Centralize supervision

Build a control room wall:
- mimic diagram showing boilers, generators, transformers, feeders, and key loops
- meters and alarms that pull plant state into one place

This is the shift from "walking the site" to "running the site".
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a mimic panel for the AC grid (central visualization).
    <br>yields: :ci[panel_mimic_ac_grid|1]
- <span class="task-kind task-retrieve">retrieve</span> Have or place switchboard panels for the control room wall.
    <br>yields: :ci[switchboard_panel_wooden|2]
- <span class="task-kind task-retrieve">retrieve</span> Stock meters and alarms for the control room wall.
    <br>yields: :ci[instrument_ammeter_panel|4] :ci[instrument_voltmeter_panel|4] :ci[alarm_bell_electric|2]
</div>
<p class="quest-rewards">Rewards: :ci[instrument_ammeter_panel|2] :ci[instrument_voltmeter_panel|2]</p>
</section>

<section class="quest-card qtype-checkpoint" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-checkpoint">Checkpoint</span>
<h3 class="quest-card__title">Tier 4 -- AC Grid & Automation Online</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Control Room and Mimic Board, Electrorefining and Stainless Steel, Hall-Heroult Aluminium</em></p>
<div class="quest-summary" markdown>
### Tier 4 online

Confirm the full integration:

- three-phase AC grid and distribution
- induction motors on the floor
- rectifier bay feeding heavy DC loads
- vacuum tube electronics capability
- plant-wide instrumentation and protection
- regulators and automatic control
- a control room that makes the whole site readable

Next tier can go solid-state (diodes/transistors), electronic control, and then digital.
</div>
<p class="quest-rewards">Rewards: :ci[lootbag_tier_V|1]</p>
</section>

<section class="quest-card qtype-exchange" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-exchange">Exchange</span>
<h3 class="quest-card__title">Trade In: Industry IV → Tech V</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Tier 4 -- AC Grid & Automation Online</em></p>
<div class="quest-summary" markdown>
Bridge the industrial era to the tech era. Exchange 5 Tier IV industry tokens for 1 Tier V tech token. Repeatable.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-do">do</span> 
</div>
<p class="quest-rewards costs">Costs: :ci[industry_IV|5]</p>
<p class="quest-rewards">Rewards: :ci[tech_V|1]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Chlor-Alkali and the Chemical Gateway</h3>
</header>
<p class="quest-pre">Unlocks after: <em>AC In, Heavy DC Out</em></p>
<div class="quest-summary" markdown>
### Electrolysis opens the chemical frontier

Your rectifier bay now outputs heavy DC. The next step: using that current
to split matter into things that don't occur naturally in pure form.

- **Chlor-alkali cell** (DiAPHRAGM or membrane): NaCl brine + DC → Cl2 + NaOH + H2
- **Downs cell** (fused-salt): molten NaCl + DC → Na metal + Cl2
- **Müller-Kühne HF**: CaF2 (fluorite) + H2SO4 → HF + CaSO4

These are the three master reagents for all Tier 4+ chemistry:
Cl2 for chlorination, NaOH for leaching/digestion, HF for niobium/zirconium/fluorite processing.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Process brine solution through the chlor-alkali cell.
    <br>yields: :ci[brine_solution|8]
- <span class="task-kind task-retrieve">retrieve</span> Collect chlorine gas and sodium hydroxide (caustic soda) from the cell outputs.
    <br>yields: :ci[gas_chlorine|4] :ci[sodium_hydroxide|4]
- <span class="task-kind task-retrieve">retrieve</span> Produce hydrofluoric acid from fluorite + sulfuric acid.
    <br>yields: :ci[acid_hydrofluoric|2]
- <span class="task-kind task-retrieve">retrieve</span> Produce sodium metal via the Downs cell (fused-salt electrolysis of NaCl).
    <br>yields: :ci[sodium_metal|2]
</div>
<p class="quest-rewards">Rewards: :ci[gas_chlorine|4] :ci[sodium_hydroxide|4]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Arc Furnace Chemistry</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Chlor-Alkali and the Chemical Gateway</em></p>
<div class="quest-summary" markdown>
### Electric arc furnace chemistry chain

The electric arc furnace does more than make steel: its extreme temperatures
drive carbothermic and thermite reactions conventional furnaces cannot reach.

- **MG-Si** (98% silicon): SiO2 + 2C → Si + 2CO at ~2000°C -- gateway to semiconductor silicon
- **Ferrochrome**: chromite + coke → FeCr -- essential for stainless and superalloy grades
- **Ferronickel**: pentlandite + coke + limestone → FeNi -- nickel source for stainless, Inconel
- **Stainless steel 18-8**: Fe + FeCr + FeNi in argon-oxygen decarburization converter
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Produce metallurgical-grade silicon (98% pure) by carbothermic reduction of silica.
    <br>yields: :ci[silicon_mg_grade|4]
- <span class="task-kind task-retrieve">retrieve</span> Smelt ferrochrome (from chromite + coke) and ferronickel (from pentlandite + coke).
    <br>yields: :ci[ferrochrome|2] :ci[ferronickel|2]
- <span class="task-kind task-retrieve">retrieve</span> Smelt a stainless steel 18-8 ingot from the ferroalloys in an AOD converter.
    <br>yields: :ci[stainless_steel_ingot|1]
</div>
<p class="quest-rewards">Rewards: :ci[stainless_steel_sheet|4] :ci[silicon_mg_grade|2]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Hall-Heroult Aluminium</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Chlor-Alkali and the Chemical Gateway</em></p>
<div class="quest-summary" markdown>
### Smelt aluminium from bauxite

Aluminium is the most abundant structural metal on Earth but
exists only as oxides locked in bauxite. Two electrochemical steps liberate it:

1. **Bayer process**: NaOH dissolves bauxite → aluminium hydroxide → filter → calcine → Al2O3
2. **Hall-Heroult cell**: Al2O3 dissolved in molten cryolite + DC + carbon anodes → liquid Al + CO2

Result: one of the lightest, most corrosion-proof structural metals.
Essential for aircraft, vehicles, overhead power cables, and all future rocketry.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have cryolite bath salt and baked carbon anodes ready for the reduction pot.
    <br>yields: :ci[cryolite|2] :ci[carbon_anode|4]
- <span class="task-kind task-retrieve">retrieve</span> Produce aluminium ingots via Hall-Heroult electrolysis.
    <br>yields: :ci[metal_aluminum_ingot|8]
- <span class="task-kind task-retrieve">retrieve</span> Roll sheet and produce an aerospace-grade Al alloy for structures.
    <br>yields: :ci[metal_aluminum_sheet|4] :ci[alloy_aluminum_aerospace|2]
</div>
<p class="quest-rewards">Rewards: :ci[metal_aluminum_sheet|4] :ci[alloy_aluminum_aerospace|1]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Electrorefining and Stainless Steel</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Arc Furnace Chemistry</em></p>
<div class="quest-summary" markdown>
### Purify metals to industry-grade purity

**Copper electrorefining**: blister copper (~98.5%) cast as anodes, dissolved in
CuSO4/H2SO4, and re-deposited onto stainless cathodes → 99.99% Cu.
Precious metals (Ag, Au, Se) fall as valuable anode slime.

**Nickel electrorefining (Sherritt Gordon process)**: pentlandite concentrate
→ ammoniacal leach → purification → electrodeposition → 99.9% Ni cathode.

Nickel cathode is the input for all downstream superalloy VIM melts: stainless, Inconel.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Provide blister copper anodes for the electrorefining bath.
    <br>yields: :ci[copper_anode_blister|4]
- <span class="task-kind task-retrieve">retrieve</span> Process nickel concentrate through the Sherritt Gordon leach-electro route.
    <br>yields: :ci[nickel_concentrate|4] :ci[nickel_cathode|4]
- <span class="task-kind task-retrieve">retrieve</span> Roll stainless steel sheet for fabrication stock.
    <br>yields: :ci[stainless_steel_sheet|4]
</div>
<p class="quest-rewards">Rewards: :ci[nickel_cathode|2] :ci[stainless_steel_sheet|2]</p>
</section>

</div>

<div class="chapter-nav">[← Steel & DC](4-steel.md)  ·  [Solid State →](6-solidstate.md)</div>
