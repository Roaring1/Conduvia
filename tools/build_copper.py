#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Copper pilot: deep, web-verified chalcopyrite -> copper chain in the JSON
datasets (JSON-first planning surface; ported to .luau after sign-off).

Reactions/reagents verified against LibreTexts, 911 Metallurgist, AusIMM
flotation guidebook, Deutsches Kupferinstitut, MDPI/ScienceDirect (2026-06-05).
Idempotent: re-running reapplies the same normalized state.
"""
import json, os

DATA = os.environ.get('CONDUVIA_DATA', '/data/conduvia-guide/data')
items    = json.load(open(DATA + '/items.json'))
recipes  = json.load(open(DATA + '/recipes.json'))
stations = json.load(open(DATA + '/stations.json'))

# ---------------------------------------------------------------------------
# 1) ALIAS / NORMALIZE legacy ids
# ---------------------------------------------------------------------------
ALIASES = {
    'copper_anode_blister': 'copper_blister',
    'metal_copper_cathode': 'copper_cathode',
    'waste_slag':           'slag',
}

def rename_item(old, new, name=None, desc=None):
    src = items.pop(old, None)
    dst = items.get(new)
    rec = dst if dst else (src or {})
    if src and not dst:
        rec = src
    if name: rec['name'] = name
    if desc: rec['description'] = desc
    al = set(rec.get('aliases', [])); al.add(old)
    rec['aliases'] = sorted(al)
    rec['id'] = new
    items[new] = rec

rename_item('copper_anode_blister', 'copper_blister',
            name='blister copper',
            desc='~98-99.5% Cu tapped from the Peirce-Smith converter, blistered by trapped SO2. Either fire-refined to tough-pitch ingot or cast to anodes for the tankhouse.')
rename_item('metal_copper_cathode', 'copper_cathode',
            name='copper cathode',
            desc='99.99% Cu plated out in the electrolytic refining cell. Remelted under charcoal cover into oxygen-free refined ingot for wire and electronics.')
if 'waste_slag' in items:
    items.pop('waste_slag', None)

for r in recipes:
    for side in ('inputs', 'outputs'):
        for ent in r.get(side) or []:
            if ent.get('id') in ALIASES:
                ent['id'] = ALIASES[ent['id']]

json.dump(ALIASES, open(DATA + '/aliases.json', 'w'), indent=1)

# ---------------------------------------------------------------------------
# 2) REMOVE shallow shortcut recipes (concentrate -> refined/blister in 1 step)
# ---------------------------------------------------------------------------
DROP = {'emb_copper_ingot_refined', 'emb_copper_anode_blister'}
recipes[:] = [r for r in recipes if r.get('id') not in DROP]
for iid in ('copper_ingot_refined', 'copper_blister'):
    if iid in items:
        items[iid]['recipe'] = ''

# ---------------------------------------------------------------------------
# 3) NEW ITEMS
# ---------------------------------------------------------------------------
def item(id, name, subtype, purpose, description, cat='Material',
         stack=64, tags='', notes='', src='Tier2_MetalAges', byproducts=''):
    items[id] = {
        'id': id, 'name': name, 'category': cat, 'subtype': subtype,
        'purpose': purpose, 'description': description,
        'placeable': False, 'isTool': False, 'toolType': '',
        'durabilityMax': None, 'stackSize': stack, 'craftStation': '',
        'recipe': '', 'byproducts': byproducts, 'tagsCsv': tags,
        'neiVisible': True, 'notes': notes, '_sourceFile': src,
    }

item('crushed_ore_chalcopyrite', 'crushed chalcopyrite', 'Crushed Ore',
     'Coarse-crushed sulfide feed (copper)',
     'Chalcopyrite stamped to gravel to begin liberating sulfide grains from silicate gangue.',
     tags='crushed_ore,sulfide,chalcopyrite,copper',
     notes='formula=CuFeS2,chemName=Chalcopyrite,elements=Cu:1|Fe:1|S:2', src='Items_OreSchema')
item('ground_ore_chalcopyrite', 'ground chalcopyrite', 'Ground Ore',
     'Flotation-grind sulfide feed (copper)',
     'Chalcopyrite ground to ~75 micron so sulfide liberates cleanly for froth flotation.',
     tags='ground_ore,sulfide,chalcopyrite,copper',
     notes='formula=CuFeS2,chemName=Chalcopyrite,elements=Cu:1|Fe:1|S:2', src='Items_OreSchema')
item('calcine_chalcopyrite', 'roasted chalcopyrite calcine', 'Calcine',
     'Partly-desulfurized Cu2S/FeS calcine (copper)',
     'Concentrate after a partial roast: part of the sulfur is burned off as SO2 and iron begins to oxidize, leaving a Cu2S + FeS calcine. Feed to the matte smelt.',
     tags='calcine,roasted,chalcopyrite,copper',
     notes='reaction=2CuFeS2+O2->Cu2S+2FeS+SO2', src='Items_OreSchema')
item('copper_matte', 'copper matte', 'Intermediate',
     'Molten Cu2S.FeS sulfide matte (~45-60% Cu)',
     'Copper and sulfur collected as a molten sulfide matte (Cu2S.FeS) beneath iron-silicate slag in the matte smelt. Converter feed.',
     tags='matte,sulfide,copper,intermediate',
     notes='chemName=CopperMatte,formula=Cu2S.FeS,grade=45-60pct_Cu', src='Tier2_MetalAges')
item('copper_anode', 'copper anode', 'Intermediate',
     'Cast impure-copper anode for electrorefining',
     'Blister/fire-refined copper cast as a flat anode and hung in the tankhouse. Dissolves into CuSO4/H2SO4; pure copper plates the cathode, precious metals drop as slime.',
     tags='anode,copper,electrorefining,intermediate',
     notes='chemName=Copper,formula=Cu,purity=98-99pct', src='Tier5_Electric')
item('copper_plate', 'copper plate', 'Metal Form',
     'Rolled copper sheet stock', 'Hot-rolled copper plate -- stock for sheet parts, heat exchangers, and electrical buswork.',
     tags='metal,copper,plate,form', notes='formula=Cu,form=plate', src='Tier2_MetalAges')
item('copper_foil', 'copper foil', 'Metal Form',
     'Thin cold-rolled copper foil', 'Copper rolled down thin -- gaskets, shielding, and early circuit/coil work.',
     tags='metal,copper,foil,form', notes='formula=Cu,form=foil', src='Tier2_MetalAges')
item('copper_rod', 'copper rod', 'Metal Form',
     'Round copper rod stock', 'Rolled/forged round copper rod -- feedstock for fasteners, contacts, and mechanical parts.',
     tags='metal,copper,rod,form', notes='formula=Cu,form=rod', src='Tier2_MetalAges')
item('copper_dust', 'copper dust', 'Metal Form',
     'Copper metal powder', 'Filed/ground copper powder for alloying, brazing pastes, and powder metallurgy.',
     tags='metal,copper,dust,powder,form', notes='formula=Cu,form=dust', src='Tier2_MetalAges')

def byproduct(id, name, purpose, description, cat='Material', tags='', notes='', src='Tier2_MetalAges'):
    if id in items:
        return
    item(id, name, 'Byproduct', purpose, description, cat=cat, tags=tags, notes=notes, src=src)

byproduct('tailings', 'tailings',
          'Gangue rejected in flotation',
          'Silicate gangue and pyrite depressed and rejected during froth flotation. Largely inert; impounded or back-filled.',
          tags='byproduct,tailings,gangue', src='Items_OreSchema')
byproduct('stone_dust', 'stone dust',
          'Rock fines from crushing/grinding',
          'Fine rock powder thrown off by the stamp mill. Usable as aggregate, abrasive, or kiln filler.',
          tags='byproduct,stone_dust,fines', src='Items_OreSchema')
byproduct('gas_so2', 'sulfur dioxide gas',
          'SO2 driven off roasting/converting sulfides',
          'Sulfur dioxide off-gas from roasting and converting. Real plants capture it for the Contact Process -- feedstock for sulfuric acid, not just waste.',
          cat='Gas', tags='byproduct,gas,so2,sulfur,acid_feed',
          notes='formula=SO2,chemName=SulfurDioxide,feeds=acid_sulfuric', src='Tier3_Steam')
byproduct('anode_slime', 'anode slime',
          'Precious-metal sludge from electrorefining',
          'Insoluble Au/Ag/Se/Te sludge that drops beneath the anodes in the copper tankhouse. Refined separately for precious metals.',
          tags='byproduct,anode_slime,precious_metals', src='Tier5_Electric')

# ---------------------------------------------------------------------------
# 4) NEW STATIONS (close 5 ore-processing gaps)
# ---------------------------------------------------------------------------
def station(id, display, ui, isize, osize):
    if id in stations:
        return
    stations[id] = {'id': id, 'displayName': display, 'uiModule': ui,
                    'containers': {'input': {'size': isize}, 'output': {'size': osize}},
                    'craftStationId': id}

station('froth_flotation_cell', 'Froth Flotation Cell', 'ProcessingUI', 6, 3)
station('reverberatory_furnace', 'Reverberatory Furnace', 'SmeltingUI', 6, 3)
station('copper_converter', 'Copper Converter (Peirce-Smith)', 'SmeltingUI', 4, 3)
station('fire_refining_furnace', 'Fire-Refining Furnace', 'SmeltingUI', 4, 3)
station('electrolytic_refining_cell', 'Electrolytic Refining Cell', 'ElectrolysisUI', 4, 3)

# ---------------------------------------------------------------------------
# 5) RECIPES -- the deep copper chain
# ---------------------------------------------------------------------------
def R(id, pack, cat, tier, station, ins, outs, time, energy, notes):
    return {'id': id, 'pack': pack, 'category': cat, 'kind': None, 'tier': tier,
            'stations': [station] if station else [], 'energy': energy,
            'inputs': [{'id': a, 'count': b} for a, b in ins],
            'outputs': [{'id': a, 'count': b} for a, b in outs],
            'worldSources': [], 'time': time, 'notes': notes}

NEW = [
  R('cu_crush_chalcopyrite', 'T1_OreProcessing.luau', 'crusher', 1,
    'stamp_mill_manual_trip_hammer',
    [('raw_ore_chalcopyrite', 6)], [('crushed_ore_chalcopyrite', 5), ('stone_dust', 1)],
    45, 0,
    'Coarse stamp-crush to liberate chalcopyrite from gangue. ~1 in 6 reports to fines as stone dust. Muscle/trip-hammer -- pay in time, not energy.'),
  R('cu_grind_chalcopyrite', 'T1_OreProcessing.luau', 'crusher', 1,
    'stamp_mill_manual_trip_hammer',
    [('crushed_ore_chalcopyrite', 5)], [('ground_ore_chalcopyrite', 4), ('stone_dust', 1)],
    60, 0,
    'Fine grind to ~75 micron flotation size. Over-grind sheds a little more stone dust.'),
  R('cu_float_chalcopyrite', 'T1_OreProcessing.luau', 'separation', 1,
    'froth_flotation_cell',
    [('ground_ore_chalcopyrite', 4)], [('concentrate_chalcopyrite', 3), ('tailings', 1)],
    120, 25,
    'Condition with lime (depress pyrite, pH ~9-12), add a xanthate collector + pine-oil frother; copper sulfide floats off, silicate gangue sinks as tailings. 4 ground -> 3 concentrate.'),
  R('cu_roast_chalcopyrite', 'T1_OreProcessing.luau', 'kiln', 1,
    'roasting_pit',
    [('concentrate_chalcopyrite', 3)], [('calcine_chalcopyrite', 2), ('gas_so2', 1)],
    180, 30,
    'Partial roast: 2CuFeS2 + O2 -> Cu2S + 2FeS + SO2. Burns off part of the sulfur (SO2 captured for the acid plant) and starts oxidizing iron. Mass drops with the lost sulfur.'),
  R('cu_matte_smelt', 'T1_OreProcessing.luau', 'smelting', 2,
    'reverberatory_furnace',
    [('calcine_chalcopyrite', 2), ('raw_ore_silica', 1), ('charcoal', 2)],
    [('copper_matte', 1), ('slag', 2)],
    240, 140,
    'Matte smelt with silica flux. Overall: 2CuFeS2 + 2SiO2 + 4O2 -> Cu2S + 2FeSiO3 + 3SO2. Iron leaves as iron-silicate (fayalite) slag; copper + sulfur collect as matte (Cu2S.FeS, ~45-60% Cu).'),
  R('cu_convert_blister', 'T1_OreProcessing.luau', 'smelting', 2,
    'copper_converter',
    [('copper_matte', 2), ('raw_ore_silica', 1)],
    [('copper_blister', 1), ('gas_so2', 1), ('slag', 1)],
    200, 110,
    'Peirce-Smith two-blow. Slag blow: 2FeS + 3O2 -> 2FeO + 2SO2, then 2FeO + SiO2 -> fayalite slag. Copper blow: Cu2S + O2 -> 2Cu + SO2. Taps blister copper, ~98-99.5% Cu.'),
  R('cu_fire_refine', 'T1_OreProcessing.luau', 'refining', 2,
    'fire_refining_furnace',
    [('copper_blister', 2), ('charcoal', 1)], [('copper_ingot', 2), ('refining_slag', 1)],
    150, 90,
    'Anode-furnace fire refining: oxidize off S/Fe/Pb/Zn, then \"pole\" with green wood/charcoal to reduce Cu2O back to metal -- tough-pitch copper (~99%). Drops a copper-rich refining slag (recycled).'),
  R('cu_cast_anode', 'T1_OreProcessing.luau', 'casting', 2,
    'clay_casting_pit',
    [('copper_blister', 2)], [('copper_anode', 2)],
    60, 45,
    'Cast blister/fire-refined copper into flat anodes for the electrorefining tankhouse.'),
  R('cu_electrorefine', 'E6_ElectricPower.luau', 'electro', 4,
    'electrolytic_refining_cell',
    [('copper_anode', 4)], [('copper_cathode', 4), ('anode_slime', 1)],
    600, 850,
    'Electrolytic refining in CuSO4/H2SO4. Anode: Cu -> Cu2+ + 2e-; cathode: Cu2+ + 2e- -> Cu (99.99%). Au/Ag/Se/Te drop as anode slime.'),
  R('cu_cathode_remelt', 'E6_ElectricPower.luau', 'refining', 4,
    'fire_refining_furnace',
    [('copper_cathode', 2)], [('copper_ingot_refined', 2)],
    120, 320,
    'Remelt cathode under charcoal cover and cast oxygen-free refined ingot for wire and electronics.'),
  R('cu_form_plate', 'T2_SteelProcessing.luau', 'forming', 3,
    'rolling_mill_steam',
    [('copper_ingot', 2)], [('copper_plate', 2)],
    60, 50, 'Hot-roll copper ingot to plate stock.'),
  R('cu_form_foil', 'T2_SteelProcessing.luau', 'forming', 3,
    'rolling_mill_steam',
    [('copper_plate', 1)], [('copper_foil', 2)],
    50, 55, 'Cold-roll plate down to thin foil.'),
  R('cu_form_rod', 'T2_SteelProcessing.luau', 'forming', 3,
    'rolling_mill_steam',
    [('copper_ingot', 1)], [('copper_rod', 2)],
    45, 40, 'Roll/forge ingot to round rod stock.'),
  R('cu_form_dust', 'T1_OreProcessing.luau', 'forming', 1,
    'stamp_mill_manual_trip_hammer',
    [('copper_ingot', 1)], [('copper_dust', 2)],
    30, 0, 'File/grind ingot to copper powder for alloying and powder metallurgy.'),
]

NEW_IDS = {r['id'] for r in NEW}
recipes[:] = [r for r in recipes if r.get('id') not in NEW_IDS]
recipes.extend(NEW)

# stamp energy/tier onto the two existing copper recipes we keep
for r in recipes:
    if r.get('id') == 't1_smelt_native_copper':
        r['energy'] = 35; r['tier'] = 1
    if r.get('id') == 't3_draw_copper_wire':
        r['energy'] = 45  # electrical wire stays drawn from electrorefined (oxygen-free) copper

json.dump(items,    open(DATA + '/items.json', 'w'),    indent=1, ensure_ascii=False)
json.dump(recipes,  open(DATA + '/recipes.json', 'w'),  indent=1, ensure_ascii=False)
json.dump(stations, open(DATA + '/stations.json', 'w'), indent=1, ensure_ascii=False)
print('copper chain applied:', len(NEW), 'new recipes |', len(items), 'items |', len(stations), 'stations')
