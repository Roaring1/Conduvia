#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JSON -> Luau emitter. Renders chain content back into the three Conduvia
Luau dialects so every ore chain ships as BOTH Luau packs and docs.

  recipes -> RecipeCard table  (T1_OreProcessing.luau dialect, energy={amount,unit})
  items   -> positional 17-field DATA rows (Items_OreSchema.luau dialect)
  stations-> keyed StationDef table (StationDefs.luau dialect)

Usage:
  python3 tools/emit_luau.py copper
Selects the id sets for one chain (registered in CHAINS below) and writes
<Chain>_{Recipes,Items,Stations}.luau into luau_out/.
"""
import json, os, sys

DATA = os.environ.get('CONDUVIA_DATA', '/data/conduvia-guide/data')
if 'CONDUVIA_LUAU' not in os.environ:
    sys.exit('ERROR: set CONDUVIA_LUAU to the target Code output dir before running emit_luau.py')
OUT  = os.environ['CONDUVIA_LUAU']
os.makedirs(OUT, exist_ok=True)

items    = json.load(open(DATA + '/items.json'))
recipes  = {r['id']: r for r in json.load(open(DATA + '/recipes.json'))}
stations = json.load(open(DATA + '/stations.json'))
try:
    aliases = json.load(open(DATA + '/aliases.json'))
except Exception:
    aliases = {}

ITEM_FIELDS = ['id','name','category','subtype','purpose','description','placeable',
               'isTool','toolType','durabilityMax','stackSize','craftStation',
               'recipe','byproducts','tagsCsv','neiVisible','notes']

# Which ids belong to each chain. Extend this dict as new ore chains are built.
CHAINS = {
  'copper': {
    'pack_id': 'Conduvia_Copper_v1',
    'items': ['crushed_ore_chalcopyrite','ground_ore_chalcopyrite','calcine_chalcopyrite',
              'copper_matte','copper_anode','copper_plate','copper_foil','copper_rod',
              'copper_dust','tailings','stone_dust','gas_so2','anode_slime',
              'copper_blister','copper_cathode'],
    'stations': ['froth_flotation_cell','reverberatory_furnace','copper_converter',
                 'fire_refining_furnace','electrolytic_refining_cell'],
    'recipes': ['cu_crush_chalcopyrite','cu_grind_chalcopyrite','cu_float_chalcopyrite',
                'cu_roast_chalcopyrite','cu_matte_smelt','cu_convert_blister',
                'cu_fire_refine','cu_cast_anode','cu_electrorefine','cu_cathode_remelt',
                'cu_form_plate','cu_form_foil','cu_form_rod','cu_form_dust',
                't1_smelt_native_copper','t3_draw_copper_wire'],
  },
  'sulfuric_acid': {
    'pack_id': 'Conduvia_SulfuricAcid_v1',
    'items': ['gas_so2','gas_so3','oleum','acid_sulfuric_dilute','acid_sulfuric'],
    'stations': ['sulfur_burner','lead_chamber','contact_converter','absorption_tower'],
    'recipes': ['acid_roast_pyrite','acid_so2_to_so3','acid_form_oleum',
                'acid_dilute_oleum','acid_lead_chamber','acid_concentrate_chamber'],
  },
}

# ---- Lua literal helpers --------------------------------------------------
def lua_str(s):
    if s is None:
        return '""'
    s = str(s).replace('\\', '\\\\').replace('"', '\\"')
    s = s.replace('\n', ' ').replace('\r', '')
    return '"%s"' % s

def lua_bool(b):
    return 'true' if b else 'false'

def lua_num_or_nil(v):
    return 'nil' if v is None else ('%g' % v if isinstance(v, float) else str(v))

# ---- renderers ------------------------------------------------------------
def render_recipes(chain, ids):
    L = ['--!strict',
         '-- AUTO-GENERATED from JSON by tools/emit_luau.py -- do not hand-edit; edit JSON + re-emit.',
         '-- %s recipe pack' % chain.title(),
         '',
         'type Ingredient = { id: string, count: number? }',
         'type EnergyInfo = { amount: number?, unit: string? }',
         'type RecipeCard = {',
         '\tid: string?, categoryId: string, inputs: { Ingredient }, outputs: { Ingredient },',
         '\ttime: number?, notes: string?, stationIds: { string }?, energy: EnergyInfo?,',
         '\tsource: string?, kind: string?, tier: number?,',
         '}',
         '',
         'local PACK_ID = %s' % lua_str(CHAINS[chain]['pack_id']),
         '',
         'local cards: { RecipeCard } = {',
         '']
    def ing_list(side):
        parts = ['{ id = %s, count = %s }' % (lua_str(e['id']), e.get('count', 1)) for e in side]
        return '{ ' + ', '.join(parts) + ' }'
    for rid in ids:
        r = recipes.get(rid)
        if not r:
            L.append('\t-- MISSING in JSON: %s' % rid); continue
        L.append('\t{')
        L.append('\t\tid         = %s,' % lua_str(r['id']))
        L.append('\t\tcategoryId = %s,' % lua_str(r.get('category') or 'crafting'))
        if r.get('tier') is not None:
            L.append('\t\ttier       = %g,' % float(r['tier']))
        sts = r.get('stations') or []
        if sts:
            L.append('\t\tstationIds = { %s },' % ', '.join(lua_str(s) for s in sts))
        L.append('\t\tinputs  = %s,' % ing_list(r.get('inputs') or []))
        L.append('\t\toutputs = %s,' % ing_list(r.get('outputs') or []))
        if r.get('time'):
            L.append('\t\ttime    = %s,' % r['time'])
        if r.get('energy') is not None:
            L.append('\t\tenergy  = { amount = %s, unit = "kJ" },' % r['energy'])
        if r.get('notes'):
            L.append('\t\tnotes   = %s,' % lua_str(r['notes']))
        L.append('\t\tsource  = PACK_ID,')
        L.append('\t},')
        L.append('')
    L.append('}')
    L.append('')
    L.append('return cards')
    L.append('')
    return '\n'.join(L)

def render_items(chain, ids):
    L = ['--!strict',
         '-- AUTO-GENERATED from JSON by tools/emit_luau.py -- do not hand-edit; edit JSON + re-emit.',
         '-- %s item rows (positional 17-field schema)' % chain.title(),
         '',
         'export type DataRow = {any}',
         'local DATA: {DataRow} = {',
         '']
    for iid in ids:
        it = items.get(iid)
        if not it:
            L.append('\t-- MISSING in JSON: %s' % iid); continue
        vals = []
        for f in ITEM_FIELDS:
            v = it.get(f)
            if f in ('placeable', 'isTool'):
                vals.append(lua_bool(v))
            elif f == 'neiVisible':
                vals.append(lua_bool(v if v is not None else True))
            elif f == 'durabilityMax':
                vals.append(lua_num_or_nil(v))
            elif f == 'stackSize':
                vals.append(lua_num_or_nil(v if v is not None else 64))
            else:
                vals.append(lua_str(v))
        row = '\t{%s}' % ','.join(vals)
        if it.get('aliases'):
            row += '  -- aliases: %s' % ', '.join(it['aliases'])
        L.append(row + ',')
    L.append('}')
    L.append('')
    L.append('return DATA')
    L.append('')
    return '\n'.join(L)

def render_stations(chain, ids):
    L = ['--!strict',
         '-- AUTO-GENERATED from JSON by tools/emit_luau.py -- do not hand-edit; edit JSON + re-emit.',
         '-- %s station defs' % chain.title(),
         '',
         'export type StationDef = {',
         '\tid: string, displayName: string, uiModule: string?,',
         '\tcontainers: { input: { size: number }, output: { size: number } },',
         '\tcraftStationId: string?,',
         '}',
         '',
         'local Stations: { [string]: StationDef } = {',
         '']
    for sid in ids:
        s = stations.get(sid)
        if not s:
            L.append('\t-- MISSING in JSON: %s' % sid); continue
        c = s.get('containers', {})
        isz = (c.get('input') or {}).get('size', 4)
        osz = (c.get('output') or {}).get('size', 3)
        L.append('\t%s = {' % sid)
        L.append('\t\tid = %s,' % lua_str(s['id']))
        L.append('\t\tdisplayName = %s,' % lua_str(s.get('displayName')))
        L.append('\t\tuiModule = %s,' % lua_str(s.get('uiModule')))
        L.append('\t\tcontainers = { input = { size = %s }, output = { size = %s } },' % (isz, osz))
        L.append('\t\tcraftStationId = %s,' % lua_str(s.get('craftStationId') or s['id']))
        L.append('\t},')
    L.append('}')
    L.append('')
    L.append('return Stations')
    L.append('')
    return '\n'.join(L)

# ---- main -----------------------------------------------------------------
def emit(chain):
    spec = CHAINS[chain]
    cap = chain.title()
    files = {
        '%s_Recipes.luau' % cap: render_recipes(chain, spec['recipes']),
        '%s_Items.luau' % cap:   render_items(chain, spec['items']),
        '%s_Stations.luau' % cap: render_stations(chain, spec['stations']),
    }
    for fn, body in files.items():
        with open(os.path.join(OUT, fn), 'w') as f:
            f.write(body)
        print('wrote', os.path.join(OUT, fn), '(%d lines)' % (body.count('\n') + 1))

if __name__ == '__main__':
    chain = sys.argv[1] if len(sys.argv) > 1 else 'copper'
    if chain not in CHAINS:
        print('unknown chain %r; known: %s' % (chain, ', '.join(CHAINS)))
        sys.exit(2)
    emit(chain)
