#!/usr/bin/env python3
"""Extract Conduvia game data (quests, items, stations) into /data/build/json."""
import os, json, glob, sys
from lualit import parse_assignment

ROOT = '/data/code/Code'
Q_DIR = ROOT + '/Forest_Standard/SRC/ReplicatedStorage/QuestBook/Content/Chapters'
ITEM_DIR = ROOT + '/Shared/SRC/ReplicatedStorage/Conduvia/ItemDatabase/Data'
STATION_FILE = ROOT + '/Shared/SRC/ReplicatedStorage/Conduvia/Stations/StationDefs.luau'
OUT = '/data/build/json'
os.makedirs(OUT, exist_ok=True)

# 17-field item record order (from handoff + file headers)
ITEM_FIELDS = ['id','name','category','subtype','purpose','description','placeable',
               'isTool','toolType','durabilityMax','stackSize','craftStation',
               'recipe','byproducts','tagsCsv','neiVisible','notes']

report = {}

# ---------- QUESTS ----------
quests = {}
q_err = {}
for path in sorted(glob.glob(Q_DIR + '/*.luau')):
    base = os.path.basename(path)[:-5]
    try:
        with open(path) as f:
            src = f.read()
        ch = parse_assignment(src, 'CH')
        quests[base] = ch
    except Exception as e:
        q_err[base] = str(e)
with open(OUT + '/quests.json','w') as f:
    json.dump(quests, f, indent=1)
report['quest_chapters_ok'] = sorted(quests.keys())
report['quest_chapters_err'] = q_err
# count quests with details
qcount = {}
for k, ch in quests.items():
    nodes = ch.get('nodes', []) if isinstance(ch, dict) else []
    det = ch.get('questDetails', {}) if isinstance(ch, dict) else {}
    qcount[k] = {'nodes': len(nodes) if isinstance(nodes,list) else 0,
                 'details': len(det) if isinstance(det,dict) else 0}
report['quest_counts'] = qcount

# ---------- ITEMS ----------
items = {}
item_err = {}
SKIP_ITEM_FILES = {'rewards', 'Token_CategoryTokens'}  # reward bundles + generated tokens, not catalog rows
for path in sorted(glob.glob(ITEM_DIR + '/*.luau')):
    base = os.path.basename(path)[:-5]
    if base in SKIP_ITEM_FILES:
        continue
    try:
        with open(path) as f:
            src = f.read()
        data = None
        for var in ('DATA', 'rows'):
            try:
                data = parse_assignment(src, var)
                break
            except Exception:
                continue
        if data is None:
            raise ValueError('no DATA/rows var')
        rows = []
        for row in data:
            if not isinstance(row, list):
                continue
            rec = {}
            for idx, fld in enumerate(ITEM_FIELDS):
                rec[fld] = row[idx] if idx < len(row) else None
            rec['_sourceFile'] = base
            rows.append(rec)
            if isinstance(rec.get('id'), str):
                items[rec['id']] = rec
    except Exception as e:
        item_err[base] = str(e)
with open(OUT + '/items.json','w') as f:
    json.dump(items, f, indent=1)
report['item_files_err'] = item_err
report['item_total'] = len(items)

# ---------- STATIONS ----------
try:
    with open(STATION_FILE) as f:
        src = f.read()
    stations = parse_assignment(src, 'Stations')
    # keep only string-keyed station defs
    stations = {k:v for k,v in stations.items() if isinstance(v, dict)}
    with open(OUT + '/stations.json','w') as f:
        json.dump(stations, f, indent=1)
    report['station_total'] = len(stations)
except Exception as e:
    report['station_err'] = str(e)

print(json.dumps(report, indent=2))
