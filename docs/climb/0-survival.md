---
title: Tier 0 — Survival
---
<div class="tierwrap" data-tier="survival" markdown>

# Tier 0 — Survival

> Stone, sticks, and the next few hours. Solve water, fire, food, and sleep before they solve you.

<div class="tier-gate" markdown>
<div class="tier-gate__num">0</div>
<div class="tier-gate__body" markdown>
<div class="tier-gate__name">Tier 0 — Survival</div>
<div class="tier-gate__flow"><span class="tg-in">Unlocks after: You wake up with nothing.</span><span class="tg-arrow">→</span><span class="tg-out">Leads to: Fiber, fire, water, a cutting edge — a night you survive.</span></div>
</div>
</div>

<p class="chapter-stats">13 quests · 10 on the win-path · 2 branches</p>

<section class="quest-card qtype-info" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-info">Briefing</span>
<h3 class="quest-card__title">You Woke Up Here</h3>
</header>
<div class="quest-summary" markdown>
### Conduvia

You woke up here with nothing. Happens to the best of us.

Stone, sticks, and the next few hours -- that's the starting inventory.
The long-term plan is to build systems that build systems, but first: survive tonight.

**Four things will get you if you ignore them:**

1. **Water**
2. **Fire**
3. **Food**
4. **Sleep**

In that order, roughly. Try not to lose track of the first one while solving the fourth.

**The rungs:** Tier 0 (stone) → Tier 1 (camp) → Tier 2 (steam + steel) → Tier 3+ (electric + automation). The bottom is slow on purpose.



<div class="qb-hint" markdown>
**Tip** · Open Settings → Controls to rebind anything.
</div>
</div>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Controls

| Action | Key |
|---|---|
| Quest Log | **J** |
| Inventory | **Tab** |
| Interact / Pick up | **F** |
| Sort Inventory | **G** |
| Menu | **P** |
| Recipes for item | **R** (hover item) |
| Uses for item | **U** (hover item) |
| Drop one | **Q** |
| Map | **M** |
| Sprint | **Left Shift** |
| Crouch | **Left Ctrl** |

**Backspace will almost always go back or close a panel.**

### How to gather things

Most materials come from walking up to something and pressing **F**.

- **Plant fibers** -- F on tall grass, ferns, or leafy shrubs
- **River stones** -- F on rocks near water or rocky ground
- **Bark slabs / bark strips** -- F on tree trunks (aim at the bark, not the canopy)
- **Twigs / sticks** -- F on fallen branches and forest floor debris
- **Berries / nuts** -- F on shrubs and tree drip lines
- **Dry logs** -- F on dead snags (the bare-trunk dead trees)

If nothing happens when you press F: try crouching (**Left Ctrl**) or getting closer.



<div class="qb-hint" markdown>
**Tip** · Hover anything in your inventory and press **U** to see every recipe that uses it. R goes the other way -- "what recipes make this?"
</div>



### Quest book

The left rail is the chapter list -- each chapter is one tier of progression. Nodes inside a chapter are quests; lines between them are prerequisites. Click any node to see what it needs and what it rewards.

Bookmarks (left rail of the crafting pane) let you pin favorite items and recipes you're actively tracking.

### Crafting + items

Press **R** on any item to see recipes that produce it. Press **U** to see what it's used in. Press **A** to favorite it. Some recipes need a station -- the quest will say which one. Drop a station from your inventory to place it.

### Death + respawn

Dying leaves a **gravestone** at the death site holding your inventory. A waypoint auto-marks it on the map so you can walk back. The grave doesn't expire and is open to anyone nearby.

Craft a **bedroll** and hold **F** on it to claim a spawn point. You'll respawn there instead of the default pad.

### What kind of game is this?

Conduvia is a survival → automation → industry game. The loop: gather → craft → build → automate → repeat, at larger scale each time. The challenge isn't combat -- it's managing complexity without letting things fall apart.
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Cordage (The First Multiplier)</h3>
</header>
<p class="quest-pre">Unlocks after: <em>You Woke Up Here</em></p>
<div class="quest-summary" markdown>
### Cordage

Rope is the duct tape of prehistory. It shows up in basically every recipe that isn't just "rock."

Get some. More than you think you need.



<div class="qb-hint" markdown>
**Tip** · **Plant fibers come from three places:** (1) **fern shrubs** drop them directly when you press F, (2) **willow shrubs** at riverside drop them, OR (3) if neither grows nearby, **ret bark**: pick `forest_bark_strip` (F on a tree trunk -- aim at the bark, not the canopy), put 3 strips + 1 `bark_bucket_water` in the camp marker and craft `plant_fibers`. The water soaks the bast fiber loose from the woody cortex; the bucket comes back empty.
</div>





<div class="qb-hint" markdown>
**Tip** · Rope itself is hand-crafted from 3 plant_fibers. R on `rope` in your inventory shows it.
</div>
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have at least 2 rope in your inventory.
    <br>yields: :ci[rope|2]
- <span class="task-kind task-craft">craft</span> Craft rope from plant fibers. <span class="task-opt">optional</span>
    <br>needs: :ci[plant_fibers|10]
    <br>yields: :ci[rope|2]
</div>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Cordage isn't flashy -- it just keeps showing up.

The three obtain paths for plant fibers (fern, willow, bark-retting) mean you're never truly stuck for cordage as long as you have a forest to work with.
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Get a Starter Pile + Mark a Spot</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Cordage (The First Multiplier)</em></p>
<div class="quest-summary" markdown>
### Get a starter pile + mark a spot

Grab a bit of everything, then pick somewhere to work from.

The temptation early on is to do "just one more trip." Resist it. Grab a bunch now while you're already out.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Gather a basic starter pile: twigs, stone, fibers. <span class="task-opt">optional</span>
    <br>yields: :ci[forest_twigs_fine|20] :ci[stone_river_rounded|10] :ci[plant_fibers|16] <span class="alt">(or :ci[stone|10])</span>
- <span class="task-kind task-craft">craft</span> Twist a quick rope tie (you'll use cordage constantly). <span class="task-opt">optional</span>
    <br>needs: :ci[plant_fibers|4]
    <br>yields: :ci[rope|1]
- <span class="task-kind task-craft">craft</span> Craft a simple camp marker. <span class="task-opt">optional</span>
    <br>needs: :ci[forest_twigs_fine|8] :ci[stone_river_rounded|2] :ci[rope|1]
    <br>yields: :ci[camp_marker_basic|1]
- <span class="task-kind task-retrieve">retrieve</span> Place your camp marker somewhere sensible. Not in water. Not on a cliff. (You could, I guess.)
    <br>yields: :ci[camp_marker_basic|1]
</div>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Batches, not crumbs

Every trip should bring back more than you need right now.
Early survival falls apart when every task becomes a separate emergency.
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Get One Real Cutting Edge</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Get a Starter Pile + Mark a Spot</em></p>
<div class="quest-summary" markdown>
### Get a cutting edge

Your hands are terrible scissors. Fix that.

A stone flake is the first tool that earns its name -- something that actually cuts on purpose.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have a sharp stone flake.
    <br>yields: :ci[tool_stone_flake|1]
- <span class="task-kind task-craft">craft</span> Craft a basic stone flake. <span class="task-opt">optional</span>
    <br>needs: :ci[stone_river_rounded|2]
    <br>yields: :ci[tool_stone_flake|1]
</div>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Real tech

A flake is the sharp piece you get when you strike stone against stone the right way.
Knapping is a genuine skill. In-game you just craft it -- appreciate the shortcut.

### Hunting basics

A stone flake is also your first hunting tool. To kill an animal:

1. **Equip** the stone flake (or any tool) from your hotbar.
2. Walk up to an animal and **left-click** to strike.
3. Keep swinging -- most animals take several hits. Predators (wolves, bears) fight back.

When an animal dies it leaves a **carcass** on the ground. Press **F** to pick it up.
Take it to a **butchering block** (basic) and press F to break it down into meat, hide, and bones.

**Start with passive animals:** Rabbit, Bird, Deer, Cow, or Sheep won't attack you.
Wolves and bears will. Start passive and upgrade your tools before picking fights with predators.



<div class="qb-hint" markdown>
**Tip** · The hide you get from butchering is how you make `rawhide_cord` -- essential for the trapping quest and better tools.
</div>
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Solve Water (For Now)</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Cordage (The First Multiplier), Get One Real Cutting Edge</em></p>
<div class="quest-summary" markdown>
### Solve water (for now)

Find a water source, bring it back, make it safe.

The real problem isn't finding water -- it's the ten round trips after your camp is set up somewhere else.
Make a bark bucket. Carrying water in cupped hands is technically possible but deeply inefficient.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Gather bark strips and a dry stick (for the bucket handle). <span class="task-opt">optional</span>
    <br>yields: :ci[forest_bark_strip|3] :ci[stick_dry_small|1]
- <span class="task-kind task-craft">craft</span> Craft a bark bucket (3 bark strips + 2 plant fibers + 1 stick, at camp marker). <span class="task-opt">optional</span>
    <br>needs: :ci[forest_bark_strip|3] :ci[plant_fibers|2] :ci[stick_dry_small|1]
    <br>yields: :ci[bark_bucket|1]
- <span class="task-kind task-retrieve">retrieve</span> Bring water back to your camp.
    <br>yields: :ci[bark_bucket_water|1]
- <span class="task-kind task-craft">craft</span> Treat the water so it's safe to drink.
    <br>needs: :ci[bark_bucket_water|1]
    <br>yields: :ci[bark_bucket_water_treated|1]
</div>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Carrying water is a container problem

Early camps don't fail because there's no water.
They fail because water is a long walk, five times a day.

### Boiling guidance

- Rolling boil for **1 minute** at low altitude.
- Rolling boil for **3 minutes** at high altitude.

If your container can't sit in flame (like a bark bucket), use hot-stone boiling.
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Make Fire Repeatable</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Get One Real Cutting Edge, Cordage (The First Multiplier)</em></p>
<div class="quest-summary" markdown>
### Make fire repeatable

Getting fire isn't the hard part. Keeping it alive is.

Three-layer stack -- each one depends on the last:
- **Tinder** -- catches the spark (dry fiber tinder)
- **Kindling** -- builds it into a flame (dry kindling sticks)
- **Fuel** -- keeps it going long enough to matter (small dry sticks or logs)

To **light** the campfire: equip the **fire_drill_kit**, walk up to a placed campfire, and **hold RMB**. An animation plays; after a moment the fire catches. The kit wears with use -- craft a spare.



<div class="qb-hint" markdown>
**Tip** · The fire ring (6 river stones at camp marker) is optional -- a campfire without a ring still works, it just doesn't look intentional.
</div>
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have a fire drill kit in your inventory.
    <br>yields: :ci[fire_drill_kit|1]
- <span class="task-kind task-place">place</span> Place a survival campfire (crafted at the camp marker).
    <br>yields: :ci[campfire_survival|1]
- <span class="task-kind task-retrieve">retrieve</span> Optional: build a stone fire ring first (6 river stones at camp marker). <span class="task-opt">optional</span>
    <br>yields: :ci[fire_ring_stones|1]
- <span class="task-kind task-retrieve">retrieve</span> Optional: stock tinder and kindling before building. <span class="task-opt">optional</span>
    <br>yields: :ci[tinder_dry_fibers|3] :ci[stick_kindling_dry|8]
- <span class="task-kind task-retrieve">retrieve</span> Optional: stock dry fuel sticks. <span class="task-opt">optional</span>
    <br>yields: :ci[stick_dry_small|6]
- <span class="task-kind task-craft">craft</span> Craft a basic fire drill kit (camp marker: 2 dry sticks + rope + stone flake). <span class="task-opt">optional</span>
    <br>needs: :ci[stick_dry_small|2] :ci[rope|1] :ci[tool_stone_flake|1]
    <br>yields: :ci[fire_drill_kit|1]
- <span class="task-kind task-craft">craft</span> Build a stone fire ring (camp marker: 6 river stones). <span class="task-opt">optional</span>
    <br>needs: :ci[stone_river_rounded|6]
    <br>yields: :ci[fire_ring_stones|1]
- <span class="task-kind task-craft">craft</span> Build a survival campfire (camp marker: fire ring + tinder + kindling + logs). <span class="task-opt">optional</span>
    <br>needs: :ci[fire_ring_stones|1] :ci[tinder_dry_fibers|2] :ci[stick_kindling_dry|4] :ci[log_small_dry|2]
    <br>yields: :ci[campfire_survival|1]
</div>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Controlled fire

You want: small fire, steady feed, easy to kill.
If you don't have enough fuel, cooking and boil timers pause -- and that is annoying.

**The fire_drill_kit** is a usable tool: equip it, hold RMB near the campfire. It spins, uses tinder, and the fire catches.
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Set Up a Night That Doesn't Wipe You</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Get Calories In</em></p>
<div class="quest-summary" markdown>
### Set up a night that doesn't wreck you

The ground steals your body heat. Put something between you and it.

Make a straw bedroll, find somewhere reasonably sheltered, and put it down.



<div class="qb-hint" markdown>
**Tip** · **To sleep:** place the bedroll, walk up to it, and press **F** to interact.
You'll get a rest prompt. Sleeping restores stamina and skips to morning.
</div>





<div class="qb-hint" markdown>
**Tip** · Hover `bedroll_straw` and press **R** to see the crafting recipe
(2× thatch bundle + plant fibres, at a camp marker).
</div>
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have or place a straw bedroll.
    <br>yields: :ci[bedroll_straw|1]
- <span class="task-kind task-craft">craft</span> Craft a straw bedroll (2× thatch bundle + plant fibres, at camp marker). <span class="task-opt">optional</span>
    <br>needs: :ci[thatch_bundle|2] :ci[plant_fibers|1]
    <br>yields: :ci[bedroll_straw|1]
- <span class="task-kind task-place">place</span> Place your bedroll somewhere sheltered, then press F to sleep. <span class="task-opt">optional</span>
    <br>yields: :ci[bedroll_straw|1]
</div>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Bedding is layered

Grass, leaves, dry boughs -- piled thick.
If the ground's cold, you'll feel it through almost anything thin.

Wind and wet can drop your temperature even above freezing.
A windbreak and a roof matter as much as the bedding itself.
</details>
</section>

<section class="quest-card qtype-checkpoint" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-checkpoint">Checkpoint</span>
<h3 class="quest-card__title">Tier 0 Stable</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Set Up a Night That Doesn't Wipe You</em></p>
<div class="quest-summary" markdown>
### Tier 0 -- Stable

Not bad for someone who started with nothing.

You can now:

- get water without a trip every hour
- make fire on purpose
- keep food coming
- sleep without bleeding heat all night

**Reward: First Camp Gift** -- a starter kit to get Tier 1 moving.
Includes a fire ring, bedroll, storage pits, waste midden, firewood rack, water level gauge, and rope.
Nothing duplicates what you already have.

Next: turn that marked spot into an actual camp.
</div>
<p class="quest-rewards">Rewards: :ci[lootbag_curated_first_camp|1]</p>
<details class="quest-lore" markdown>
<summary>Background</summary>

### This is the line

The next chapter (Tier 1) assumes you can stay alive while you build things.
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">A Quieter Hunt</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Cordage (The First Multiplier)</em></p>
<div class="quest-summary" markdown>
### A Quieter Hunt

Not everything is worth killing.

A lasso and a basket let you move small animals around -- relocate prey closer to camp, or just keep a few around for the mid-game when you need steady yields without burning through your hunting stock.

**How it works:**

1. Craft a **rope lasso** (2 rope + 1 rawhide cord) at the hand-crafting grid.
2. Craft a **wicker basket** (2 willow + 1 plant fibers).
3. Equip the lasso. Walk within about 15 studs of a Rabbit, Bird, or Owl and left-click.
4. The animal is packed into a basket in your inventory.
5. Equip the occupied basket and left-click to release the animal wherever you want it.

**Getting rawhide cord:**
To craft the lasso you need `rawhide_cord`. Kill a passive animal (Rabbit, Deer, Cow) by equipping your stone flake and left-clicking it. Pick up the carcass with F, take it to a **butchering block**, and press F to get hide. Then hand-craft: `hide + stone_flake → rawhide_cord`.

**Alternative -- snares:**
Rather than chasing animals, set a passive snare. Craft a `snare_simple` (rope + 2 forest_twigs_fine, hand grid) and drop it near an animal trail. Small game will walk into it and you'll find a carcass when you come back.



<div class="qb-hint" markdown>
**Tip** · **Rope lasso** is single-use -- it's consumed on a successful catch. Bring a few if you plan to move a group.
</div>




<div class="qb-hint" markdown>
**Tip** · For **medium animals** (Cow, Sheep, Deer, Red Fox) you need a **wooden cage** (2 wood + 1 rope + 1 rawhide cord). Same mechanic.
</div>




<div class="qb-hint" markdown>
**Tip** · **Wolves** and **bears** can't be lassooed. Craft a **wolf lure** (cooked meat + rope) or **bear lure** (2 safe berries + rope) instead -- place it and step back. The animal arrives on its own, then you deal with it however you like.
</div>
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-craft">craft</span> Craft a rope lasso.
    <br>needs: :ci[rope|2] :ci[rawhide_cord|1]
    <br>yields: :ci[rope_lasso|1]
- <span class="task-kind task-craft">craft</span> Craft a wicker basket (2 willow wands + 1 plant fibers, hand-crafted).
    <br>yields: :ci[wicker_basket|1]
- <span class="task-kind task-retrieve">retrieve</span> Catch a small animal (have any occupied basket).
    <br>yields: :ci[wicker_basket_rabbit|1] :ci[wicker_basket_bird|1] :ci[wicker_basket_owl|1]
- <span class="task-kind task-craft">craft</span> Optional: also set a snare for passive trapping (rope + 2 twigs, hand grid). <span class="task-opt">optional</span>
    <br>needs: :ci[rope|1] :ci[forest_twigs_fine|2]
    <br>yields: :ci[snare_simple|1]
</div>
<p class="quest-rewards">Rewards: :ci[rope_lasso|2] :ci[wicker_basket|1] :ci[snare_simple|2]</p>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Why bother?

Lasso-and-basket is a soft version of ranching. You're not taming the animals -- they're still wild when you release them. But being able to relocate them means you can consolidate livestock near camp, seed a pond with birds, or just move a cow somewhere convenient before the mid-game farms come online.

The wooden cage opens up deer relocation, which feeds into leather supply chains before you get consistent hunting going.

### Snare vs lasso

Snares are for food. Lassos are for relocation. Both require rawhide cord, but snares are lighter to set up and let you trap passively while you do other things. A few snares set before bed means meat in the morning without a hunt.
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">First Cast</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Get One Real Cutting Edge</em></p>
<div class="quest-summary" markdown>
### First Cast

Still water holds food.

Craft a basic fishing rod at your camp marker and try your luck near a river or pond.
It takes patience -- the float bobs, then dips. Press **F** when it dips.

**How it works:**

1. Craft a **fishing rod** at the camp marker (2 dry sticks + 3 plant fibers + 1 stone knife flake).
2. Stand within 14 studs of water. Right-click to cast.
3. Wait for the float to dip -- then press **F** to reel in.



<div class="qb-hint" markdown>
**Tip** · The bite window is short (~1.8 s). Watch the timing bar and don't wait too long.
</div>




<div class="qb-hint" markdown>
**Tip** · Missed the window? Right-click to cast again. Rod has limited durability -- around 20 catches.
</div>
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-craft">craft</span> Craft a basic fishing rod.
    <br>yields: :ci[fishing_rod_basic|1]
- <span class="task-kind task-retrieve">retrieve</span> Catch a raw fish.
    <br>yields: :ci[fish_raw|1]
</div>
<p class="quest-rewards">Rewards: :ci[fishing_rod_basic|1] :ci[fish_raw|2]</p>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Fishing is patience, not luck.

The float dips when the fish strikes. React within the window or the fish spits the hook.

A good riverside camp near the water means you can fish between other tasks without burning much time.
</details>
</section>

<section class="quest-card qtype-side" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-side">Branch</span>
<h3 class="quest-card__title">Get Calories In</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Make Fire Repeatable</em></p>
<div class="quest-summary" markdown>
### Get some calories in

Go find food. Cook some of it.

Different shrubs and trees drop different fruits and nuts -- blueberry, blackberry, hawthorn, sea buckthorn, juniper, rowan; hazelnut, acorn, nut bundles. Any pair of the **same** kind sorts at hand into one safe-edible portion (R-key the berry to see the recipe). Cooked food beats raw food.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Gather a small amount of safe foods.
    <br>yields: :ci[food_berries_safe|8] :ci[food_nuts_safe|4]
- <span class="task-kind task-retrieve">retrieve</span> Have at least one simple cooked ration ready.
    <br>yields: :ci[food_cooked_simple|1]
- <span class="task-kind task-produce">produce</span> Cook one simple ration at your campfire. <span class="task-opt">optional</span>
</div>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Don't eat it all immediately

If you're always running at zero food, every other task gets harder.

Cook a small batch, eat one, keep the rest. Running a surplus sounds boring -- it isn't, once you see what it unlocks.



<div class="qb-hint" markdown>
**Tip** · The world has an **assortment** of fruits and nuts, not just one generic kind. Pick whichever your area happens to grow -- they all funnel into the same `food_berries_safe` / `food_nuts_safe` output.
</div>
</details>
</section>

<section class="quest-card qtype-main" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-main">Win-path</span>
<h3 class="quest-card__title">Dirt Under Your Nails</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Get Calories In</em></p>
<div class="quest-summary" markdown>
### Dirt Under Your Nails

Foraging works today. Next week it won't.

Gathering seeds now means you hit Tier 0.5 with something ready to plant.

**Getting seeds:**

Flowers and spent grass heads drop `forest_seed_mix_dry` when you press F. Take 3 handfuls to your **camp marker** and sort them into crop seeds (recipe: "sort seed mix" in the camp marker's crafting list). This gives flax, turnip, AND carrot seeds in one pass.

**The full farming loop (needs hoe, available in Tier 0.5):**

1. Equip a hoe and swing it at open ground (grass or dirt) to till a patch.
2. Walk up to the tilled soil with seeds in your inventory and press **F** to plant.
3. Wait for the sprout to change colour -- it's ripe when it glows bright.
4. Press **F** to harvest: you get crop + a seed back, so the supply sustains itself.



<div class="qb-hint" markdown>
**Tip** · Turnip is the staple starter crop -- fast and hardy. Carrot is a bit slower but useful for variety.
</div>
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-retrieve">retrieve</span> Have carrot seeds. Sort them at your camp marker (3 seed mix → all three seed types) or via the hand grid (2 seed mix + plant fibers → carrot seed).
    <br>yields: :ci[carrot_seed|2]
- <span class="task-kind task-retrieve">retrieve</span> Also have some turnip seeds for the staple crop. <span class="task-opt">optional</span>
    <br>yields: :ci[turnip_seed|2]
</div>
<p class="quest-rewards">Rewards: :ci[carrot_seed|4] :ci[turnip_seed|4]</p>
<details class="quest-lore" markdown>
<summary>Background</summary>

### Why bother with farming?

Hunting and foraging are unreliable and biome-dependent. Farming gives you a controlled, renewable food loop that works regardless of how far you've explored.

One tilled row of turnips takes less time per calorie than any hunting route.

Starting the seed collection now means you hit Tier 0.5 with something to plant immediately rather than having to backtrack for seeds after you've built the hoe.
</details>
</section>

<section class="quest-card qtype-side" markdown>
<header class="quest-card__head">
<span class="qbadge qbadge-side">Branch</span>
<h3 class="quest-card__title">Keep What You Find</h3>
</header>
<p class="quest-pre">Unlocks after: <em>Set Up a Night That Doesn't Wipe You</em></p>
<div class="quest-summary" markdown>
### Keep What You Find

Your pack fills fast. A bark storage crate holds 27 stacks and keeps its contents between sessions -- everything you place in it stays there when you log off.

**To craft one**, open your camp marker and queue a bark storage crate:
- 8 × forest bark strip
- 2 × branch bundle
- 2 × rope

The camp marker shows a progress bar while it builds (~50 s). When done, place the crate near your bedroll.

**To use it**, left-click the crate to open it. Shift+click moves items between your inventory and the crate instantly.
</div>
<div class="quest-tasks" markdown>
**Do this:**
- <span class="task-kind task-craft">craft</span> Queue 'bark storage crate' at the camp marker (8 bark strips + 2 branch bundles + 2 rope).
    <br>needs: :ci[forest_bark_strip|8] :ci[branch_bundle|2] :ci[rope|2]
    <br>yields: :ci[storage_crate_bark|1]
- <span class="task-kind task-place">place</span> Equip the bark storage crate and press F to place it near camp.
    <br>yields: :ci[storage_crate_bark|1]
</div>
<p class="quest-rewards">Rewards: :ci[forest_bark_strip|6] :ci[rope|2]</p>
</section>

</div>

<div class="chapter-nav">  ·  [Stone →](1-stone.md)</div>
