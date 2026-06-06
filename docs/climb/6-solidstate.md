---
title: Tier 6 — Solid State
---
<div class="tierwrap" data-tier="solidstate" markdown>

# Tier 6 — Solid State

> Semiconductors and automation. Grow a silicon crystal, slice wafers, and let machines run the line.

<div class="tier-gate" markdown>
<div class="tier-gate__num">6</div>
<div class="tier-gate__body" markdown>
<div class="tier-gate__name">Tier 6 — Solid State</div>
<div class="tier-gate__flow"><span class="tg-in">Unlocks after: Industrial electricity and pure silicon.</span><span class="tg-arrow">→</span><span class="tg-out">Leads to: Polysilicon, wafers, ICs, automation.</span></div>
</div>
</div>

<p class="chapter-stats">13 quests · 11 on the win-path · 1 branches</p>

<section class="quest-card qtype-info" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-info">Briefing</span>
<h3 class="quest-card__title">Transistors, PLCs and Robots</h3>
</header>
<div class="quest-summary" markdown>
Introduces Tier 5 as the moment your heavy-electric plant learns solid-state electronics, programmable controllers, CNC and the first industrial robots.
</div>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Diodes, Rectifiers and Transistors</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Transistors, PLCs and Robots</em></p>
<div class="quest-summary" markdown>
Set up a small electronics bench to make basic silicon diodes, rectifier bridges and low-power transistors for switching and amplification.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a glass electronics bench.
    <br>yields: :ci[glass_bench|1]
- <span class="task-kind task-retrieve">retrieve</span> Process raw silicon wafers on the bench.
    <br>yields: :ci[silicon_wafer_raw|8]
- <span class="task-kind task-retrieve">retrieve</span> Produce diodes, rectifier bridges and transistors.
    <br>yields: :ci[diode_silicon_small|16] :ci[rectifier_bridge_silicon|4] :ci[transistor_npn_signal|16]
</div>
<p class="quest-rewards">Rewards: :ci[diode_silicon_small|8] :ci[transistor_npn_signal|8]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Logic Gates and Flip-Flops</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Diodes, Rectifiers and Transistors</em></p>
<div class="quest-summary" markdown>
Assemble small logic modules that bundle transistors and diodes into reusable AND, OR, NOT and flip-flop building blocks for control circuits.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Craft AND/OR logic modules from transistors and diodes.
    <br>yields: :ci[logic_module_and_or|12]
- <span class="task-kind task-retrieve">retrieve</span> Craft NOT gates and flip-flop modules.
    <br>yields: :ci[logic_module_not|4] :ci[logic_module_flipflop|4]
- <span class="task-kind task-retrieve">retrieve</span> Have electromagnetic relays for hybrid control circuits.
    <br>yields: :ci[relay_electromagnetic|8]
</div>
<p class="quest-rewards">Rewards: :ci[logic_module_and_or|6] :ci[relay_electromagnetic|4]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">First PLC Rack</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Logic Gates and Flip-Flops</em></p>
<div class="quest-summary" markdown>
Build a basic programmable logic controller rack with a CPU and several I/O modules that can scan inputs and drive outputs in a fixed cycle.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a PLC rack with CPU and I/O modules.
    <br>yields: :ci[plc_rack_basic|1] :ci[plc_cpu_module|1] :ci[plc_io_module|4]
- <span class="task-kind task-retrieve">retrieve</span> Install a switchboard panel with metering instruments.
    <br>yields: :ci[switchboard_panel_wooden|1] :ci[instrument_ammeter_panel|2] :ci[instrument_voltmeter_panel|2]
</div>
<p class="quest-rewards">Rewards: :ci[plc_io_module|2]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Automate a Line with a PLC</h3>
</header>
<p class="quest-pre">Unlocks after: <em>First PLC Rack</em></p>
<div class="quest-summary" markdown>
Use your PLC to fully automate at least one production line, handling start, stop, interlocks and alarms without manual switch juggling.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Write and load program cartridges for the PLC.
    <br>yields: :ci[controller_program_cartridge|2]
- <span class="task-kind task-retrieve">retrieve</span> Install relays and alarm bells for interlock circuits.
    <br>yields: :ci[relay_electromagnetic|12] :ci[alarm_bell_electric|2]
- <span class="task-kind task-retrieve">retrieve</span> Place level and speed sensors on the automated line.
    <br>yields: :ci[sensor_level_tank|2] :ci[sensor_speed_line|2]
</div>
<p class="quest-rewards">Rewards: :ci[controller_program_cartridge|2] :ci[relay_electromagnetic|4]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">CNC Machines in the Shop</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Automate a Line with a PLC</em></p>
<div class="quest-summary" markdown>
Upgrade your machine shop with a CNC mill and CNC lathe that follow stored programs to cut parts to precise dimensions. This only works once you have stable power, precision measurement, and standardized fasteners.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a CNC mill and CNC lathe.
    <br>yields: :ci[cnc_mill_basic|1] :ci[cnc_lathe_basic|1]
- <span class="task-kind task-retrieve">retrieve</span> Have an electric machine shop and industrial computer online.
    <br>yields: :ci[machine_shop_electric|1] :ci[computer_industrial_rugged|1]
</div>
<p class="quest-rewards">Rewards: :ci[computer_industrial_rugged|1]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">First Industrial Robot Cell</h3>
</header>
<p class="quest-pre">Unlocks after: <em>CNC Machines in the Shop</em></p>
<div class="quest-summary" markdown>
Install a simple programmable robot arm in a fenced cell to load and unload hot or repetitive work from a machine, such as a press or CNC station.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a robot arm with a safety cage.
    <br>yields: :ci[robot_arm_industrial_basic|1] :ci[safety_cage_industrial|1]
- <span class="task-kind task-retrieve">retrieve</span> Install a powered conveyor and position sensors for the cell.
    <br>yields: :ci[conveyor_powered|1] :ci[sensor_position_limit|4]
</div>
<p class="quest-rewards">Rewards: :ci[sensor_position_limit|4]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Digital Monitoring and Alarms</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Automate a Line with a PLC</em></p>
<div class="quest-summary" markdown>
Add a digital overview panel and simple HMI screens that collect status from PLCs and sensors, so you can watch lines and acknowledge alarms from a central point.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place HMI panels and a rugged industrial computer.
    <br>yields: :ci[panel_hmi_basic|2] :ci[computer_industrial_rugged|1]
- <span class="task-kind task-retrieve">retrieve</span> Install the AC grid mimic panel with metering instruments.
    <br>yields: :ci[panel_mimic_ac_grid|1] :ci[instrument_ammeter_panel|4] :ci[instrument_voltmeter_panel|4]
</div>
<p class="quest-rewards">Rewards: :ci[instrument_ammeter_panel|2] :ci[instrument_voltmeter_panel|2]</p>
</section>

<section class="quest-card qtype-checkpoint" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-checkpoint">Checkpoint</span>
<h3 class="quest-card__title">Tier 5 -- Solid-State and Automation Online</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Digital Monitoring and Alarms, First Industrial Robot Cell, Czochralski Wafers and Logic Chips, Carbon Fiber and CFRP</em></p>
<div class="quest-summary" markdown>
Confirm that discrete semiconductors, logic modules, PLC racks, at least one PLC-run line, CNC machines, robot cells and digital plant monitoring are all running together.
</div>
<p class="quest-rewards">Rewards: :ci[lootbag_tier_VI|1]</p>
</section>

<section class="quest-card qtype-exchange" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-exchange">Exchange</span>
<h3 class="quest-card__title">Trade In: Tech V → VI</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Tier 5 -- Solid-State and Automation Online</em></p>
<div class="quest-summary" markdown>
Exchange Tier V tech tokens for Tier VI. Repeatable.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-do">do</span> 
</div>
<p class="quest-rewards costs">Costs: :ci[tech_V|5]</p>
<p class="quest-rewards">Rewards: :ci[tech_VI|1]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Trichlorosilane and Pure Silicon</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Diodes, Rectifiers and Transistors</em></p>
<div class="quest-summary" markdown>
Upgrade from raw silicon wafers to device-grade monocrystalline wafers by building the full trichlorosilane / Siemens CVD / Czochralski pull sequence: MG-Si + HCl → SiHCl3 → (CVD) → 9N poly → (CZ pull) → ingot → (wire saw + CMP) → polished wafer.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> React MG-Si with HCl gas to produce trichlorosilane (SiHCl3).
    <br>yields: :ci[trichlorosilane|4]
- <span class="task-kind task-retrieve">retrieve</span> Run the Siemens CVD bell-jar reactor to deposit 9N polysilicon on hot rods.
    <br>yields: :ci[polysilicon_9n|4]
- <span class="task-kind task-retrieve">retrieve</span> Pull a Czochralski monocrystalline ingot and saw it into polished device-grade wafers.
    <br>yields: :ci[silicon_ingot_czochralski|1] :ci[silicon_wafer_polished|8]
</div>
<p class="quest-rewards">Rewards: :ci[silicon_wafer_polished|4]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Czochralski Wafers and Logic Chips</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Trichlorosilane and Pure Silicon</em></p>
<div class="quest-summary" markdown>
Fabricate integrated circuit logic chips from polished Czochralski wafers: define active regions by ion implantation, grow gate oxide, pattern and etch multiple metal interconnect layers by photolithography, then dice into individual chips.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Fab logic chips from polished wafers and copper interconnects.
    <br>yields: :ci[logic_chip|8]
</div>
<p class="quest-rewards">Rewards: :ci[logic_chip|4]</p>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Carbon Fiber and CFRP</h3>
</header>
<p class="quest-pre">Unlocks after: <em>CNC Machines in the Shop</em></p>
<div class="quest-summary" markdown>
Produce carbon fiber reinforced polymer (CFRP) structural panels: coal tar → acrylonitrile (Sohio process) → polyacrylonitrile (PAN) fiber → stabilize → carbonize at 1200°C → impregnate with epoxy → autoclave cure at 130-180°C.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Produce acrylonitrile via the Sohio process, then polymerize and spin PAN fiber.
    <br>yields: :ci[acrylonitrile|4] :ci[pan_fiber|2]
- <span class="task-kind task-retrieve">retrieve</span> Stabilize PAN fiber and carbonize at 1200°C in nitrogen to form carbon fiber tow.
    <br>yields: :ci[carbon_fiber|4]
- <span class="task-kind task-retrieve">retrieve</span> Produce epoxy resin and autoclave-cure CFRP structural panels.
    <br>yields: :ci[epoxy_resin|2] :ci[cfrp_panel|2]
</div>
<p class="quest-rewards">Rewards: :ci[cfrp_panel|2]</p>
</section>

</div>

<div class="chapter-nav">[← Electric](5-electric.md)  ·  [Space →](7-space.md)</div>
