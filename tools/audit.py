#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chain validator for the Conduvia recipe graph.

Checks:
  1. integrity   - every recipe input/output id resolves to a known item (or alias)
  2. stations    - every recipe station id resolves to a real station
  3. reachability- items obtainable by BFS from world/raw sources; flags orphans
  4. depth       - longest production depth to key copper targets
  5. metrics     - recipe count, multi-output (byproduct) %, energy/tier coverage

Exit code 0 if no hard errors (unknown ids), 1 otherwise. Station/orphan issues
are reported as warnings.
"""
import json, os, sys, collections

DATA = os.environ.get('CONDUVIA_DATA', '/data/conduvia-guide/data')
items    = json.load(open(DATA + '/items.json'))
recipes  = json.load(open(DATA + '/recipes.json'))
stations = json.load(open(DATA + '/stations.json'))
try:
    aliases = json.load(open(DATA + '/aliases.json'))
except Exception:
    aliases = {}

known = set(items) | set(aliases)
errors, warns = [], []

# --- 1) integrity ---------------------------------------------------------
for r in recipes:
    for side in ('inputs', 'outputs'):
        for e in r.get(side) or []:
            if e.get('id') not in known:
                errors.append('recipe %s: %s id %r not an item' % (r.get('id'), side[:-1], e.get('id')))

# --- 2) stations ----------------------------------------------------------
station_miss = collections.Counter()
for r in recipes:
    for sid in r.get('stations') or []:
        if sid not in stations:
            station_miss[sid] += 1
for sid, n in sorted(station_miss.items()):
    warns.append('station not defined: %r (%d recipes) -- free-text or TODO' % (sid, n))

# --- 3) reachability ------------------------------------------------------
def canon(i):
    return aliases.get(i, i)

obtainable = set()
for iid, it in items.items():
    tags = (it.get('tagsCsv') or '')
    if 'raw_ore' in tags or 'node_ore' in tags:
        obtainable.add(iid)
for r in recipes:
    if not (r.get('inputs')):
        for o in r.get('outputs') or []:
            obtainable.add(canon(o['id']))
# also treat a few base world inputs as available
obtainable |= {'charcoal', 'wood', 'water', 'air', 'coke_fuel', 'resin', 'sail_cloth'}

changed = True
while changed:
    changed = False
    for r in recipes:
        ins = r.get('inputs') or []
        if not ins:
            continue
        if all(canon(i['id']) in obtainable for i in ins):
            for o in r.get('outputs') or []:
                c = canon(o['id'])
                if c not in obtainable:
                    obtainable.add(c); changed = True

produced = set()
for r in recipes:
    for o in r.get('outputs') or []:
        produced.add(canon(o['id']))
unreachable = sorted(produced - obtainable)
for iid in unreachable:
    warns.append('unreachable output (inputs never bottom out in world/raw): %s' % iid)

# --- 4) depth to copper targets ------------------------------------------
best = {}
for iid in obtainable:
    best[iid] = 0
for _ in range(40):
    for r in recipes:
        ins = r.get('inputs') or []
        if not ins:
            continue
        if all(canon(i['id']) in best for i in ins):
            d = 1 + max(best[canon(i['id'])] for i in ins)
            for o in r.get('outputs') or []:
                c = canon(o['id'])
                if d > best.get(c, -1):
                    best[c] = d

# --- 5) metrics -----------------------------------------------------------
n = len(recipes)
multi = sum(1 for r in recipes if len(r.get('outputs') or []) > 1)
with_e = sum(1 for r in recipes if r.get('energy') is not None)
with_t = sum(1 for r in recipes if r.get('tier') is not None)
with_time = sum(1 for r in recipes if r.get('time'))

print('=' * 64)
print('CONDUVIA CHAIN AUDIT')
print('=' * 64)
print('recipes: %d | items: %d | stations: %d' % (n, len(items), len(stations)))
print('multi-output (byproduct) recipes: %d (%.0f%%)' % (multi, 100.0*multi/n))
print('energy set: %d (%.0f%%) | tier set: %d (%.0f%%) | time set: %d (%.0f%%)'
      % (with_e, 100.0*with_e/n, with_t, 100.0*with_t/n, with_time, 100.0*with_time/n))
print('-' * 64)
print('COPPER targets (production depth from raw/world):')
for iid in ['copper_ingot','copper_blister','copper_matte','calcine_chalcopyrite',
            'concentrate_chalcopyrite','copper_cathode','copper_ingot_refined',
            'copper_plate','copper_foil','copper_rod','copper_dust','copper_wire_drawn']:
    d = best.get(iid)
    mark = ('depth %d' % d) if d is not None else 'UNREACHABLE'
    print('  %-28s %s' % (iid, mark))
print('-' * 64)
if errors:
    print('HARD ERRORS (%d):' % len(errors))
    for e in errors[:60]:
        print('  X', e)
else:
    print('HARD ERRORS: none')
print('WARNINGS (%d):' % len(warns))
for wmsg in warns[:80]:
    print('  !', wmsg)
print('=' * 64)
sys.exit(1 if errors else 0)
