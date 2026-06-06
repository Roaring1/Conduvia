#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sulfuric-acid chain: web-verified Contact Process (DCDA) + historical Lead
Chamber route, in the JSON datasets (JSON-first; ported to .luau via emit_luau).

Verified 2026-06-05 against: Wikipedia (Contact process / Oleum / Lead chamber
process), Chemistry LibreTexts (The Contact Process), chemguide, HORIBA DCDA,
sulphuric-acid.com metallurgical, ScienceDirect (smelter off-gas 3-13% SO2).

Chemistry modelled:
  Dead-roast pyrite : 4 FeS2 + 11 O2 -> 2 Fe2O3 + 8 SO2        (also feeds iron)
  Contact (V2O5)    : 2 SO2 + O2 <=> 2 SO3   dH=-196 kJ/mol, ~450C, 1-2 atm, ~98%
  Absorb (oleum)    : SO3 + H2SO4 -> H2S2O7   (never SO3 + water directly -> mist)
  Dilute            : H2S2O7 + H2O -> 2 H2SO4 (~98%)
  Lead chamber      : SO2 + NOx + moist air -> ~65-78% chamber acid (historical)

Idempotent: re-running reapplies the same normalized state.
"""
import json, os

DATA = os.environ.get('CONDUVIA_DATA', '/data/conduvia-guide/data')
items    = json.load(open(DATA + '/items.json'))
recipes  = json.load(open(DATA + '/recipes.json'))
stations = json.load(open(DATA + '/stations.json'))

ACID_CAT = (items.get('acid_sulfuric') or {}).get('category', 'Material') or 'Material'

# ---------------------------------------------------------------------------
# 1) ITEMS
# ---------------------------------------------------------------------------
def item(id, name, subtype, purpose, description, cat='Material',
         stack=64, tags='', notes='', src='Tier3_Steam', byproducts=''):
    rec = items.get(id, {})
    rec.update({
        'id': id, 'name': name, 'category': cat, 'subtype': subtype,
        'purpose': purpose, 'description': description,
        'placeable': rec.get('placeable', False), 'isTool': False, 'toolType': '',
        'durabilityMax': None, 'stackSize': stack,
        'craftStation': rec.get('craftStation', ''),
        'recipe': rec.get('recipe', ''), 'byproducts': byproducts, 'tagsCsv': tags,
        'neiVisible': True, 'notes': notes, '_sourceFile': rec.get('_sourceFile', src),
    })
    items[id] = rec

item('gas_so3', 'sulfur trioxide gas', 'Gas',
     'SO3 from catalytic oxidation of SO2',
     'Sulfur trioxide off the V2O5 contact beds. Fiercely hygroscopic -- never fed straight to water (it flashes to an unmanageable acid mist), so it is absorbed into strong acid as oleum instead.',
     cat='Gas', tags='gas,so3,sulfur,acid_intermediate',
     notes='formula=SO3,chemName=SulfurTrioxide', src='Tier3_Steam')
item('oleum', 'oleum (fuming sulfuric acid)', 'Intermediate',
     'SO3 dissolved in H2SO4 (H2S2O7)',
     'Fuming sulfuric acid: SO3 absorbed into 97-98% acid. The safe carrier for SO3 -- diluted with a controlled amount of water it yields concentrated H2SO4 without the runaway mist.',
     cat=ACID_CAT, tags='acid,oleum,fuming,h2s2o7,acid_intermediate',
     notes='formula=H2S2O7,chemName=Oleum/DisulfuricAcid', src='Tier3_Steam')
item('acid_sulfuric_dilute', 'chamber acid (dilute H2SO4)', 'Intermediate',
     'Low-grade ~65-78% acid from the lead chamber',
     'Weak, slightly nitrous sulfuric acid straight from the lead chambers. Capped near 78% by the process -- good enough for pickling and fertilizer, but must be boiled down (Glover tower) for concentrated acid.',
     cat=ACID_CAT, tags='acid,sulfuric,dilute,chamber',
     notes='formula=H2SO4(aq),chemName=SulfuricAcid(dilute)', src='Tier3_Steam')

# upgrade the existing sulfuric-acid target (was a dangling input with no recipe)
if 'acid_sulfuric' in items:
    a = items['acid_sulfuric']
    a['description'] = ('Concentrated ~98% sulfuric acid -- the keystone industrial reagent. '
                        'Made by the Contact Process (SO2->SO3->oleum->acid) or, earlier and weaker, '
                        'the lead chamber route. Feeds leaching, electrolyte, HF, and yellowcake chains.')
    a.setdefault('tagsCsv', 'acid,sulfuric,h2so4,reagent')
    a['category'] = a.get('category', ACID_CAT) or ACID_CAT

# ---------------------------------------------------------------------------
# 2) STATIONS
# ---------------------------------------------------------------------------
def station(id, display, ui, isize, osize):
    if id in stations:
        return
    stations[id] = {'id': id, 'displayName': display, 'uiModule': ui,
                    'containers': {'input': {'size': isize}, 'output': {'size': osize}},
                    'craftStationId': id}

station('sulfur_burner', 'Sulfur Burner / Pyrite Roaster', 'SmeltingUI', 4, 3)
station('lead_chamber', 'Lead Chamber (NOx)', 'ProcessingUI', 4, 3)
station('contact_converter', 'Contact Converter (V2O5 beds, DCDA)', 'ProcessingUI', 4, 3)
station('absorption_tower', 'Oleum Absorption Tower', 'ProcessingUI', 4, 3)

# ---------------------------------------------------------------------------
# 3) RECIPES -- two real routes, both bottoming out at minable pyrite
# ---------------------------------------------------------------------------
PACK = 'T3_SulfuricAcid.luau'
def R(id, cat, tier, station, ins, outs, time, energy, notes):
    return {'id': id, 'pack': PACK, 'category': cat, 'kind': None, 'tier': tier,
            'stations': [station] if station else [], 'energy': energy,
            'inputs': [{'id': a, 'count': b} for a, b in ins],
            'outputs': [{'id': a, 'count': b} for a, b in outs],
            'worldSources': [], 'time': time, 'notes': notes}

NEW = [
  # --- SO2 generation (also a real iron feed: pyrite cinder is Fe2O3) ---
  R('acid_roast_pyrite', 'roaster', 2, 'sulfur_burner',
    [('raw_ore_pyrite', 4)], [('gas_so2', 6), ('roasted_ore_hematite', 2)],
    50, 40,
    'Dead-roast pyrite in excess air: 4 FeS2 + 11 O2 -> 2 Fe2O3 + 8 SO2. Drives off the SO2 acid feed AND leaves an iron-oxide cinder -- the same roasted hematite the iron chain smelts. One of the oldest acid feedstocks; the other is captured copper-smelter SO2.'),
  # --- Contact Process (modern, high purity) ---
  R('acid_so2_to_so3', 'chemistry', 4, 'contact_converter',
    [('gas_so2', 2)], [('gas_so3', 2)],
    30, 60,
    'Catalytic oxidation over vanadium(V) oxide beds: 2 SO2 + O2 <=> 2 SO3 (dH=-196 kJ/mol), ~450C and 1-2 atm. Exothermic + reversible, so heat is pulled between beds; double-contact/double-absorption (DCDA) pushes ~98%+ conversion and keeps SO2 stack emissions low.'),
  R('acid_form_oleum', 'chemistry', 4, 'absorption_tower',
    [('gas_so3', 3), ('water_raw', 1)], [('oleum', 2)],
    20, 18,
    'Absorb SO3 into circulating strong acid: SO3 + H2SO4 -> H2S2O7 (oleum). SO3 is never fed to water directly -- the hydration is so violent it forms a fog of acid mist that will not condense. Make-up water keeps the loop charged.'),
  R('acid_dilute_oleum', 'chemistry', 4, 'absorption_tower',
    [('oleum', 2), ('water_raw', 1)], [('acid_sulfuric', 3)],
    20, 12,
    'Bleed oleum down with a metered water add: H2S2O7 + H2O -> 2 H2SO4. Yields concentrated ~98% acid; part is drawn off as product, part recycled back to the absorption tower.'),
  # --- Lead Chamber Process (historical, lower grade) ---
  R('acid_lead_chamber', 'chemistry', 3, 'lead_chamber',
    [('gas_so2', 3), ('water_raw', 1)], [('acid_sulfuric_dilute', 2)],
    40, 15,
    'The pre-Contact route (Roebuck, 1746): SO2 oxidised by moist air with recycled nitrogen oxides (NOx) as catalyst inside lead-lined chambers. Cheap and robust but caps out near 65-78% acid. NOx is recovered in the Gay-Lussac/Glover towers and reused.'),
  R('acid_concentrate_chamber', 'chemistry', 3, 'lead_chamber',
    [('acid_sulfuric_dilute', 2)], [('acid_sulfuric', 1)],
    35, 25,
    'Boil chamber acid up in the Glover tower to drive off water and lift it toward concentrated strength. Tier-3 path to H2SO4 before the vanadium contact plant is available.'),
]

# water_raw is a GATHERED world resource (lakes/rivers/wells/rain) -- give it an
# inputless world-gather recipe so it bottoms out. Previously dangling, it blocked
# the acid dilution steps plus ~14 other *_water_raw recipes.
NEW.append({
    'id': 'gather_water_raw', 'pack': PACK, 'category': 'gathering', 'kind': None,
    'tier': 0, 'stations': [], 'energy': 0, 'inputs': [],
    'outputs': [{'id': 'water_raw', 'count': 4}],
    'worldSources': ['surface water: lake, river, rain barrel, or hand-dug well'],
    'time': 10,
    'notes': 'Scoop raw, untreated water from any surface source. Gathered, not crafted -- the base input for acid dilution, slurries, quench, and cooling. Boil/filter downstream for potable or process-grade water.',
})

# de-dupe by id, then append
have = {r.get('id') for r in recipes}
for r in NEW:
    if r['id'] in have:
        recipes[:] = [x for x in recipes if x.get('id') != r['id']]
recipes.extend(NEW)

# point the produced items at a representative recipe (for item-page back-refs)
for iid, rid in [('acid_sulfuric', 'acid_dilute_oleum'),
                 ('oleum', 'acid_form_oleum'),
                 ('gas_so3', 'acid_so2_to_so3'),
                 ('acid_sulfuric_dilute', 'acid_lead_chamber')]:
    if iid in items:
        items[iid]['recipe'] = rid

json.dump(items,    open(DATA + '/items.json', 'w'),    indent=1, ensure_ascii=False)
json.dump(recipes,  open(DATA + '/recipes.json', 'w'),  indent=1, ensure_ascii=False)
json.dump(stations, open(DATA + '/stations.json', 'w'), indent=1, ensure_ascii=False)

print('acid chain applied: +%d recipes | %d items | %d stations'
      % (len(NEW), len(items), len(stations)))
print('routes: pyrite-roast/copper-SO2 -> [contact: SO3->oleum->H2SO4] and [lead-chamber: ->dilute->H2SO4]')
print('cross-link: acid_roast_pyrite also outputs roasted_ore_hematite (iron feed)')
