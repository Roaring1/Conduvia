---
title: Tier 3 — Steam
---
<div class="tierwrap" data-tier="steam" markdown>

# Tier 3 — Steam

> Mechanical power. Coke gives you furnace-grade heat; steam gives you work that never gets tired.

<div class="tier-gate" markdown>
<div class="tier-gate__num">3</div>
<div class="tier-gate__body" markdown>
<div class="tier-gate__name">Tier 3 — Steam</div>
<div class="tier-gate__flow"><span class="tg-in">Unlocks after: Bronze and wrought iron tools.</span><span class="tg-arrow">→</span><span class="tg-out">Leads to: Coke, coal tar, mechanical power.</span></div>
</div>
</div>

<p class="chapter-stats">11 quests · 9 on the win-path · 1 branches</p>

<section class="quest-card qtype-info" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-info">Briefing</span>
<h3 class="quest-card__title">Coal, Waterpower, and Early Steam</h3>
</header>
<div class="quest-summary" markdown>
### Tier 2 is where "site" starts to matter

You are no longer just a camp with better tools.
You are a **works**:

- waterpower with line-shaft distribution
- coal access (the fuel that breaks woodland limits)
- coke production for ironworks-grade heat
- a boiler house with a real steam loop
- your first serious steam use is mine drainage (pumping), then expanded into rotary shop drive



<div class="qb-hint" markdown>
**Tip** · You need a **bronze pickaxe or iron hammer** (from the Metal Ages chapter) to mine coal and hematite.  Make sure you have one before tackling coal access.
</div>
</div>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Keep this tier honest

Steam starts as **stationary power**.
Not trains. Not magic torque.
Pumps first. Rotation second.
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Put a Stream to Work</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Coal, Waterpower, and Early Steam</em></p>
<div class="quest-summary" markdown>
### Put a stream to work

Build an overshot wheel where you have **usable head** and couple it to a short shaft.

Waterpower is old -- and that's the point:
it's reliable when the site supports it.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place an overshot waterwheel.
    <br>yields: :ci[waterwheel_overshot|1]
- <span class="task-kind task-retrieve">retrieve</span> Have a first short line shaft coupled to the wheel (basic mechanical output).
    <br>yields: :ci[line_shaft_wrought|1]
</div>
<p class="quest-rewards">Rewards: :ci[line_shaft_wrought|1]</p>
<details class="quest-lore" markdown>
<summary>Background</summary>

### What "good placement" means

- you need fall (head), not just flow
- you need a stable channel intake
- you need a safe spot for the rotating assembly

You could have built a wooden wheel centuries ago. You couldn't have built the iron shaft, stone millrace, and timber gearing that make it actually useful. Now you can.
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Line-Shaft Workshop Bay</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Put a Stream to Work</em></p>
<div class="quest-summary" markdown>
### Line-shaft workshop bay

Extend shafting and use belts + sheaves to distribute power to tools.

This is the "factory floor" pattern:
one prime mover → many driven stations.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have additional shafting and belt drive parts ready.
    <br>yields: :ci[line_shaft_wrought|2] :ci[flat_belt_leather|4] :ci[sheave|4]
- <span class="task-kind task-retrieve">retrieve</span> Bring at least one driven tool online (air for fire or force for forming).
    <br>yields: :ci[bellows|1] :ci[lever_press|1]
</div>
<p class="quest-rewards">Rewards: :ci[flat_belt_leather|2] :ci[sheave|2]</p>
<details class="quest-lore" markdown>
<summary>Background</summary>

### What this unlocks

You stop asking:
"can I power this tool?"

You start asking:
"how many tools can this shaft feed?"
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Open the Coal Measures</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Coal, Waterpower, and Early Steam</em></p>
<div class="quest-summary" markdown>
### Open the coal measures

Find and work a coal seam until you have a steady supply flowing to your works.

Coal changes scale:
it's why steam becomes practical on sites that outgrow woodland fuel.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Mine bituminous coal from a seam and deliver it to your works.
    <br>yields: :ci[coal_bituminous|50]
</div>
<p class="quest-rewards">Rewards: :ci[coal_bituminous|30]</p>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Reality check

Mines flood.
That problem is why early steam engines get built at all.
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Make Coke for Industrial Heat</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Open the Coal Measures</em></p>
<div class="quest-summary" markdown>
### Make coke for industrial heat

Convert coal into coke: hotter, cleaner-burning, and suited for ironworks-scale firing.

This is the fuel bridge between "some coal" and "serious heat on demand".



<div class="qb-hint" markdown>
**Tip** · **Don't skip the coal buffer.**  Producing 40 coke consumes roughly 80 coal, and your blast furnace (built in the Steel chapter, but usable now) will need even more.  The 80-coal stock task below is not optional -- treat it as the minimum working supply.
</div>
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a coke oven.
    <br>yields: :ci[coke_oven_beehive|1]
- <span class="task-kind task-produce">produce</span> Run a first coke burn and produce a starter batch.
- <span class="task-kind task-retrieve">retrieve</span> Keep 80 coal on hand -- this supply will be consumed making the coke you already burned plus the next batch.
    <br>yields: :ci[coal_bituminous|80]
</div>
<p class="quest-rewards">Rewards: :ci[coke_fuel|20]</p>
<details class="quest-lore" markdown>
<summary>Background</summary>

### About the oven form

Early coke can be made in clamps/heaps; beehive ovens are a later high-throughput form.
Functionally, the point is the same: controlled off-gassing to turn coal into coke.

### Coal ratio reality

The coal→coke conversion is roughly 2:1 by mass in a beehive oven.
40 coke costs you ~80 coal.  When the blast furnace is running it will consume coke
continuously -- keep your coal supply well ahead of your coke demand.
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Low-Pressure Boiler House</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Open the Coal Measures</em></p>
<div class="quest-summary" markdown>
### Low-pressure boiler house

Assemble a conservative stationary boiler plant:
shell, firebox, pipes, feedwater loop, condensation/cooling hardware, and basic safety.

This is **low-pressure practice**:
enough to run early engines, not a racing locomotive.



<div class="qb-hint" markdown>
**Tip** · The cast-iron firebox and cylinder both require **pig iron**.  Pig iron needs a small blast furnace (refractory bricks + coke + limestone → blast_furnace_small).  Build that first -- hover `blast_furnace_small` and press **R** for the recipe.
</div>





<div class="qb-hint" markdown>
**Tip** · **Limestone gotcha:** mining limestone nodes yields `raw_ore_limestone` (the geologic ore form). The blast furnace recipe expects `limestone_rock` (discrete nodules). Convert at hand with `raw_ore_limestone -> limestone_rock` (1:1, free). Same trick applies to most "raw_ore_X" + "X_rock" pairs.
</div>
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have the boiler shell + cast-iron firebox ready. (Firebox needs pig iron -- build a blast_furnace_small first if you haven't.)
    <br>yields: :ci[boiler_shell_riveted|1] :ci[firebox_cast_iron|1]
- <span class="task-kind task-retrieve">retrieve</span> Have piping + feedwater hardware ready for a complete loop.
    <br>yields: :ci[steam_pipe_wrought|8] :ci[feedwater_pump_simple|1] :ci[cooling_tank_wooden|1]
- <span class="task-kind task-retrieve">retrieve</span> Have basic safety + level indication online.
    <br>yields: :ci[safety_valve_weighted|1] :ci[water_level|1]
</div>
<p class="quest-rewards">Rewards: :ci[steam_pipe_wrought|4]</p>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Non-negotiables

- you must control pressure (relief)
- you must control water level (don't expose iron to direct fire dry)
- you must move water back in (feedwater loop)

### Pig iron in the Steam era

Early boiler makers used small cupola-style furnaces long before the large Bessemer converters
of the Steel age.  Your `blast_furnace_small` recipe reflects this -- it is buildable now, not
gated behind the Steel chapter.  Build it, charge it with coke + hematite + limestone, and tap
enough pig iron to cast the firebox and cylinder.

### Why this gate exists

Safe pressure vessels require **repeatable metallurgy, tight machining tolerances, and standardized fasteners**.
If you can't make consistent plates, rivets, and seals, you don't get steam.
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Atmospheric Pump for a Wet Shaft</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Low-Pressure Boiler House</em></p>
<div class="quest-summary" markdown>
### Atmospheric pump for a wet shaft

Put steam to work where it historically earns its keep first:
**mine drainage**.

Build a simple pumping engine set (atmospheric-style behavior, condensation-driven cycle)
and show it can keep a wet shaft workable.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have the basic engine + cylinder assembly ready. (Cast-iron cylinder needs pig iron from your blast furnace.)
    <br>yields: :ci[steam_engine_simple|1] :ci[steam_cylinder_cast_iron|1] :ci[steam_piston_rod|1]
- <span class="task-kind task-retrieve">retrieve</span> Have condensation + sealing materials ready (cycle reliability).
    <br>yields: :ci[condenser_jet|1] :ci[gland_packing_steam|4]
</div>
<p class="quest-rewards">Rewards: :ci[gland_packing_steam|4]</p>
<details class="quest-lore" markdown>
<summary>Background</summary>

### What makes it "early steam"

It's not about high pressure.
It's about cycling steam and condensation to drive a piston and pump rod reliably.
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Turn Steam into Rotation</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Atmospheric Pump for a Wet Shaft</em></p>
<div class="quest-summary" markdown>
### Turn steam into rotation

Upgrade from "pumps only" to **general drive**:
add flywheel, rotary conversion, speed regulation, and belt/shaft outputs.

Now the steam plant can drive the same shop logic as waterpower:
shafts, belts, and stations.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have the rotary power train parts ready.
    <br>yields: :ci[flywheel|1] :ci[crank_iron_forged|1] :ci[flyball_governor|1]
- <span class="task-kind task-retrieve">retrieve</span> Have belts/pulleys/shafting ready to distribute steam power into a workshop.
    <br>yields: :ci[belt_pulley_iron|2] :ci[flat_belt_leather|4] :ci[line_shaft_wrought|2]
</div>
<p class="quest-rewards">Rewards: :ci[flat_belt_leather|4] :ci[belt_pulley_iron|2]</p>
<details class="quest-lore" markdown>
<summary>Background</summary>

### What changes

- flywheel smooths cyclic power
- rotary conversion enables continuous drives
- governor prevents runaway and stabilizes machine work
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Mechanised Stamp Milling</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Line-Shaft Workshop Bay, Turn Steam into Rotation</em></p>
<div class="quest-summary" markdown>
### Mechanised stamp milling

Connect your powertrain to an ore crushing station.
Cams lift and drop stamps to break raw ore into fine feed for furnaces.

Route hematite from your ore supply into the mill input.
Crushed ore flows out the other side.

This is throughput -- not glamour.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a stamp mill assembly connected to your powertrain.
    <br>yields: :ci[stamp_mill_manual_trip_hammer|1]
- <span class="task-kind task-retrieve">retrieve</span> Feed raw hematite ore to the stamp mill input.
    <br>yields: :ci[raw_ore_hematite|60]
- <span class="task-kind task-produce">produce</span> Produce crushed ore output from the stamp mill.
</div>
<p class="quest-rewards">Rewards: :ci[crushed_ore_hematite|20] :ci[coal_bituminous|20]</p>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Why this sits here

Your ironwork stops being "small batch heroic"
and becomes "repeatable processing".

That is the real steam-era shift.
</details>
</section>

<section class="quest-card qtype-checkpoint" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-checkpoint">Checkpoint</span>
<h3 class="quest-card__title">Tier 2 -- Steam Age Online</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Mechanised Stamp Milling</em></p>
<div class="quest-summary" markdown>
### Tier 2 complete -- Steam Age online

You have a real early-industrial works package:

- waterwheel + line-shaft workshop distribution
- coal access as a sustained fuel supply
- coke production as an industrial heat chain
- a conservative boiler house + steam loop discipline
- steam justified first by mine drainage, then extended into rotary shop power
- mechanised ore crushing throughput (stamp milling)

Next: Steel takes this into **high steam** and **DC power**.
</div>
<p class="quest-rewards">Rewards: :ci[lootbag_tier_III|1]</p>
<details class="quest-lore" markdown>
<summary>Background</summary>

### The line this draws

From here forward, the game can assume:
- prime movers exist (water + steam)
- fuel is industrial (coal + coke chain)
- power distribution exists (shafts/belts now; wires later)
- ore prep is mechanised

That's the on-ramp to high-pressure steam and electrical systems.
</details>
</section>

<section class="quest-card qtype-exchange" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-exchange">Exchange</span>
<h3 class="quest-card__title">Trade In: Industry II → III</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Tier 2 -- Steam Age Online</em></p>
<div class="quest-summary" markdown>
Exchange Tier II industry tokens for Tier III. Repeatable.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-do">do</span> 
</div>
<p class="quest-rewards costs">Costs: :ci[industry_II|5]</p>
<p class="quest-rewards">Rewards: :ci[industry_III|1]</p>
</section>

</div>

<div class="chapter-nav">[← Metal Ages](2-metal_ages.md)  ·  [Steel & DC →](4-steel.md)</div>
