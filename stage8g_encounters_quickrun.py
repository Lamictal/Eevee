#!/usr/bin/env python3
"""Stage 8G: increase Route 102 canary encounters and add double-B wild escape.
Run on the clean expansion clone AFTER Stage 8C species installation, before make.
Does not change species IDs, trainer battles, or Evergreen.
"""
import argparse
import json
from pathlib import Path
import re

def patch(checkout: Path):
    checkout=checkout.resolve()
    if not (checkout/'Makefile').is_file():
        raise ValueError('Missing expansion Makefile')

    encounters=checkout/'src/data/wild_encounters.json'
    source=encounters.read_text(encoding='utf-8')
    marker='"map": "MAP_ROUTE102"'
    if source.count(marker)!=1:
        raise ValueError('Expected exactly one Route 102 encounter list')
    start=source.index(marker)
    stop=source.find('"water_mons"',start)
    if stop<0:
        raise ValueError('Missing Route 102 water encounter section')
    route=source[start:stop]
    pat=re.compile(r'\{\s*"min_level":\s*\d+,\s*"max_level":\s*\d+,\s*"species":\s*"SPECIES_[A-Z0-9_]+"\s*\}')
    matches=list(pat.finditer(route))
    if len(matches)!=12:
        raise ValueError(f'Expected 12 Route 102 land slots, got {len(matches)}')

    all_enc=json.loads(source)
    found=[e for g in all_enc['wild_encounter_groups'] for e in g.get('encounters',[]) if e.get('map')=='MAP_ROUTE102' and e.get('land_mons')]
    if len(found)!=1:
        raise ValueError('Expected one Route 102 grass encounter table')
    mons=found[0]['land_mons']['mons']
    if len(mons)!=12 or mons[7]['species']!='SPECIES_AERIEON' or mons[10]['species']!='SPECIES_AERARTHEON':
        raise ValueError('Stage 8C canary species not installed correctly')
    if mons[0]['species']!='SPECIES_POOCHYENA' or mons[2]['species']!='SPECIES_POOCHYENA':
        raise ValueError('Expected original Poochyena slots 0 and 2')

    # Standard slot weights: 0=20%, 2=10%, 7=5%, 10=1%.
    # Thus Aerieon 20+5 = 25%; Aerartheon 10+1 = 11%.
    for ix,species,lv in ((2,'SPECIES_AERARTHEON',6),(0,'SPECIES_AERIEON',5)):
        m=matches[ix]
        segment=route[m.start():m.end()]
        segment=re.sub(r'(?<="min_level": )\d+',str(lv),segment)
        segment=re.sub(r'(?<="max_level": )\d+',str(lv),segment)
        segment=re.sub(r'"species": "SPECIES_[A-Z0-9_]+"',f'"species": "{species}"',segment)
        route=route[:m.start()]+segment+route[m.end():]
    new_enc=source[:start]+route+source[stop:]
    verified=[e for g in json.loads(new_enc)['wild_encounter_groups'] for e in g.get('encounters',[]) if e.get('map')=='MAP_ROUTE102' and e.get('land_mons')]
    if len(verified)!=1 or [verified[0]['land_mons']['mons'][i]['species'] for i in (0,2,7,10)]!=['SPECIES_AERIEON','SPECIES_AERARTHEON','SPECIES_AERIEON','SPECIES_AERARTHEON']:
        raise ValueError('Route 102 post-patch check failed')

    config=checkout/'include/config/battle.h'
    current_config=config.read_text(encoding='utf-8')
    regex=re.compile(r'^(#define\s+B_QUICK_MOVE_CURSOR_TO_RUN\s+)(FALSE)(\s+//[^\n]*)$',re.M)
    if len(list(regex.finditer(current_config)))!=1:
        raise ValueError('Missing disabled B-to-Run battle config')
    new_config=regex.sub(lambda m:m.group(1)+'TRUE'+m.group(3),current_config,count=1)

    controller=checkout/'src/battle_controller_player.c'
    source_ctl=controller.read_text(encoding='utf-8')
    old='''            if (!(gBattleTypeFlags & BATTLE_TYPE_TRAINER)) // If wild battle, pressing B moves cursor to "Run".
            {
                PlaySE(SE_SELECT);
                ActionSelectionDestroyCursorAt(gActionSelectionCursor[battler]);'''
    new='''            if (!(gBattleTypeFlags & BATTLE_TYPE_TRAINER)) // Wild battle: first B focuses Run, second B tries escaping.
            {
                if (JOY_NEW(B_BUTTON) && gActionSelectionCursor[battler] == 3)
                {
                    PlaySE(SE_SELECT);
                    TryHideLastUsedBall();
                    BtlController_EmitTwoReturnValues(battler, B_COMM_TO_ENGINE, B_ACTION_RUN, 0);
                    BtlController_Complete(battler);
                    return;
                }
                PlaySE(SE_SELECT);
                ActionSelectionDestroyCursorAt(gActionSelectionCursor[battler]);'''
    if source_ctl.count(old)!=1:
        raise ValueError('Unknown battle controller layout; refusing B-button patch')
    new_ctl=source_ctl.replace(old,new,1)

    # All prechecks are done before modifying any file.
    for path,changed in ((encounters,new_enc),(config,new_config),(controller,new_ctl)):
        if path.read_text(encoding='utf-8')==changed:
            raise ValueError(f'No source change detected in {path}')
    encounters.write_text(new_enc,encoding='utf-8')
    config.write_text(new_config,encoding='utf-8')
    controller.write_text(new_ctl,encoding='utf-8')
    print('Stage 8G: Route 102 Aerieon 25%, Aerartheon 11%, ordinary Pokémon 64%.')
    print('Stage 8G: In wild battles first B focuses Run, second B attempts escape.')
    print('Stage 8G: Species IDs and trainer-battle handling unchanged.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkout',type=Path)
    patch(parser.parse_args().checkout)
