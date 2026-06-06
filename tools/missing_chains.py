#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Find the chains we still need to build.

Walks the recipe graph from mineable/world sources; any recipe whose output
never bottoms out is 'blocked'. The inputs that block it are missing reagents.
Ranks missing reagents by how many recipes + downstream items they gate, so we
know which chain to author next (e.g. sulfuric acid, oxygen, chlor-alkali).
"""
import json, os, collections

DATA = os.environ.get('CONDUVIA_DATA', '/data/conduvia-guide/data')
items    = json.load(open(DATA + '/items.json'))
recipes  = json.load(open(DATA + '/recipes.json'))
try:
    aliases = json.load(open(DATA + '/aliases.json'))
except Exception:
    aliases = {}

def canon(i):
    return aliases.get(i, i)

# seed obtainable set: raw/node ores, inputless recipe outputs, base world inputs
obtainable = set()
for iid, it in items.items():
    tags = it.get('tagsCsv') or ''
    if 'raw_ore' in tags or 'node_ore' in tags:
        obtainable.add(iid)
for r in recipes:
    if not (r.get('inputs')):
        for o in r.get('outputs') or []:
            obtainable.add(canon(o['id']))
WORLD = {'charcoal','wood','water','air','coke_fuel','resin','sail_cloth','clay',
         'sand','stone','log','plant_fiber','bone_raw_small','bone_raw_large'}
obtainable |= WORLD

changed = True
while changed:
    changed = False
    for r in recipes:
        ins = r.get('inputs') or []
        if ins and all(canon(i['id']) in obtainable for i in ins):
            for o in r.get('outputs') or []:
                c = canon(o['id'])
                if c not in obtainable:
                    obtainable.add(c); changed = True

# blocked recipes + the specific missing inputs
block_count = collections.Counter()   # missing reagent -> # recipes it blocks
gated_items = collections.defaultdict(set)  # missing reagent -> downstream outputs gated
for r in recipes:
    ins = r.get('inputs') or []
    if not ins:
        continue
    missing = [canon(i['id']) for i in ins if canon(i['id']) not in obtainable]
    if missing:
        outs = [canon(o['id']) for o in r.get('outputs') or []]
        for m in missing:
            block_count[m] += 1
            for o in outs:
                gated_items[m].add(o)

# a 'missing reagent' that is itself produced by some recipe is a mid-chain gap;
# one that is never produced anywhere is a true raw gap (needs a brand-new chain).
produced = set()
for r in recipes:
    for o in r.get('outputs') or []:
        produced.add(canon(o['id']))

print('=' * 70)
print('MISSING-CHAINS REPORT  (reagents that block recipes from bottoming out)')
print('=' * 70)
print('%-34s %6s %8s  %s' % ('missing reagent', 'blocks', 'made?', 'kind'))
print('-' * 70)
for reagent, n in block_count.most_common():
    made = 'yes' if reagent in produced else 'NO'
    kind = 'mid-chain gap' if reagent in produced else 'NEEDS NEW CHAIN'
    print('%-34s %6d %8s  %s' % (reagent, n, made, kind))
print('-' * 70)
print('total blocked-input reagents:', len(block_count))
print('  - true raw gaps (never produced):', sum(1 for r in block_count if r not in produced))
print('  - mid-chain gaps (produced but unreachable):', sum(1 for r in block_count if r in produced))
