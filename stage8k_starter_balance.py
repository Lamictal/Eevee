#!/usr/bin/env python3
"""Stage 8K: balanced Route 102 encounters and Eevee as selectable starter.

The current three-slot Birch starter chooser cannot represent four options
without UI work. Replace the grass slot with Eevee for this prototype only.
This does not grant Eevee to an existing save; the starter choice happens on
a new game. Preserve Torchic and Mudkip. Do not change any species IDs.
"""
from pathlib import Path
import argparse
import json
import re

WEIGHTS=(20,20,10,10,10,10,5,5,4,4,1,1)
def main(root):
    root=root.resolve()
    if not (root/"Makefile").is_file():
        raise SystemExit("Expected pokeemerald-expansion checkout")
    path=root/"src/data/wild_encounters.json"
    original=path.read_text(encoding="utf-8")
    marker='"map": "MAP_ROUTE102"'
    if original.count(marker)!=1:raise ValueError("Route102 unexpected")
    start=original.index(marker)
    stop=original.find('"water_mons"',start)
    if stop<0:raise ValueError("Route102 water boundary absent")
    route=original[start:stop]
    pat=re.compile(r'\{\s*"min_level":\s*\d+,\s*"max_level":\s*\d+,\s*"species":\s*"SPECIES_[A-Z0-9_]+"\s*\}')
    matches=list(pat.finditer(route))
    if len(matches)!=12:raise ValueError(f"Route102 expected 12 slots, saw {len(matches)}")
    tree=json.loads(original)
    matches_table=[item for group in tree['wild_encounter_groups'] for item in group.get('encounters',[]) if item.get('map')=="MAP_ROUTE102" and item.get('land_mons')]
    if len(matches_table)!=1:raise ValueError("Unexpected Route102 table")
    old=[e['species'] for e in matches_table[0]['land_mons']['mons']]
    assert len(old)==12
    expected={0:"SPECIES_AERIEON",2:"SPECIES_AERARTHEON",7:"SPECIES_AERIEON",10:"SPECIES_AERARTHEON"}
    for i,name in expected.items():
        if old[i]!=name: raise ValueError(f"Expected Stage8G slot {i}: {name}; got {old[i]}")
    # Restore Poochyena first slot and Zigzagoon in the second old canary slot,
    # use the 10% slot for Aerieon and 1% slot for rarer Aerartheon.
    updates={0:("SPECIES_POOCHYENA",3,3),2:("SPECIES_AERIEON",5,5),
             7:("SPECIES_ZIGZAGOON",3,3)}
    for idx in sorted(updates,reverse=True):
        species,lo,hi=updates[idx]
        a,b=matches[idx].span()
        updated=route[a:b]
        updated=re.sub(r'(?<="min_level": )\d+',str(lo),updated,count=1)
        updated=re.sub(r'(?<="max_level": )\d+',str(hi),updated,count=1)
        updated=re.sub(r'"species": "SPECIES_[A-Z0-9_]+"',f'"species": "{species}"',updated,count=1)
        route=route[:a]+updated+route[b:]
    result=original[:start]+route+original[stop:]
    verified=json.loads(result)
    mons=[item['land_mons']['mons'] for group in verified['wild_encounter_groups'] for item in group.get('encounters',[]) if item.get('map')=="MAP_ROUTE102" and item.get('land_mons')]
    if len(mons)!=1:raise ValueError("Route102 postpatch bad")
    counts={}
    for idx,e in enumerate(mons[0]):
        counts[e['species']]=counts.get(e['species'],0)+WEIGHTS[idx]
    if counts.get("SPECIES_AERIEON")!=10 or counts.get("SPECIES_AERARTHEON")!=1:
        raise ValueError(f"Bad encounter rate calculation {counts}")
    starter=root/"src/starter_choose.c"
    old_starter=starter.read_text(encoding="utf-8")
    needle="#define GRASS_STARTER (IS_FRLG ? SPECIES_BULBASAUR  : SPECIES_TREECKO)"
    if old_starter.count(needle)!=1:raise ValueError("Starter chooser changed, refusing overwrite")
    new_starter=old_starter.replace(needle,"#define GRASS_STARTER (IS_FRLG ? SPECIES_BULBASAUR  : SPECIES_EEVEE) // STAGE8K_EEVEE_STARTER: grass-position ball; still Eevee (Normal type)",1)
    # One of the baseline starter options is intentionally displaced, rather than
    # modifying the three-slot graphics/selection state machine unsafely.
    path.write_text(result,encoding="utf-8")
    starter.write_text(new_starter,encoding="utf-8")
    print("Stage 8K: Route 102 Aerieon=10%, Aerartheon=1%, other Pokémon=89%.")
    print("Stage 8K: Eevee replaces Treecko only in the three-choice Birch starter bag.")
    print("Stage 8K: Torchic and Mudkip remain; existing saves/starter remain unchanged.")
    print("Stage 8K: Native graphics/effectiveness, Dex, and follower settings retained.")

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("checkout",type=Path)
    main(p.parse_args().checkout)
