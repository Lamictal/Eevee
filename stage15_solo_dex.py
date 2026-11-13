#!/usr/bin/env python3
"""Stage 15: native Hoenn starters; all 1,025 National species catchable solo.

Adds small, biome-aware bonus encounter pools, not replacements for original
Hoenn grass tables, Eevee spawns, fishing, surfing or save data. Other Eevee
forms continue to be available by their existing custom evolutions.
"""
import argparse
import hashlib
import json
import re
from functools import lru_cache
from collections import defaultdict
from pathlib import Path

# Evolution and event exclusives appear directly in the wild, so no trading is
# ever required for a canonical National Dex entry. Legendary species are
# deliberately assigned to harder, late-game caves and routes.
RARE = set('''ARTICUNO ZAPDOS MOLTRES MEWTWO MEW RAIKOU ENTEI SUICUNE LUGIA HO_OH CELEBI REGIROCK REGICE REGISTEEL LATIAS LATIOS KYOGRE GROUDON RAYQUAZA JIRACHI DEOXYS UXIE MESPRIT AZELF DIALGA PALKIA HEATRAN REGIGIGAS GIRATINA CRESSELIA PHIONE MANAPHY DARKRAI SHAYMIN ARCEUS VICTINI COBALION TERRAKION VIRIZION TORNADUS THUNDURUS RESHIRAM ZEKROM LANDORUS KYUREM KELDEO MELOETTA GENESECT XERNEAS YVELTAL ZYGARDE DIANCIE HOOPA VOLCANION TAPU_KOKO TAPU_LELE TAPU_BULU TAPU_FINI COSMOG COSMOEM SOLGALEO LUNALA NIHILEGO BUZZWOLE PHEROMOSA XURKITREE CELESTEELA KARTANA GUZZLORD NECROZMA MAGEARNA MARSHADOW POIPOLE NAGANADEL STAKATAKA BLACEPHALON ZERAORA MELTAN MELMETAL ZACIAN ZAMAZENTA ETERNATUS KUBFU URSHIFU ZARUDE REGIELEKI REGIDRAGO GLASTRIER SPECTRIER CALYREX ENAMORUS WO_CHIEN CHIEN_PAO TING_LU CHI_YU KORAIDON MIRAIDON WALKING_WAKE IRON_LEAVES OKIDOGI MUNKIDORI FEZANDIPITI OGERPON GOUGING_FIRE RAGING_BOLT IRON_BOULDER IRON_CROWN TERAPAGOS PECHARUNT'''.split())
RARE_AREAS = 'MAP_SKY_PILLAR_1F MAP_SKY_PILLAR_3F MAP_SKY_PILLAR_5F MAP_VICTORY_ROAD_1F MAP_VICTORY_ROAD_B1F MAP_VICTORY_ROAD_B2F MAP_METEOR_FALLS_B1F_2R MAP_METEOR_FALLS_STEVENS_CAVE MAP_MT_PYRE_6F MAP_MT_PYRE_SUMMIT MAP_DESERT_UNDERPASS MAP_SHOAL_CAVE_LOW_TIDE_ICE_ROOM'.split()
STARTERS = {
 'BULBASAUR':'MAP_PETALBURG_WOODS','CHARMANDER':'MAP_FIERY_PATH','SQUIRTLE':'MAP_ROUTE118',
 'CHIKORITA':'MAP_ROUTE119','CYNDAQUIL':'MAP_JAGGED_PASS','TOTODILE':'MAP_ROUTE118',
 'TREECKO':'MAP_PETALBURG_WOODS','TORCHIC':'MAP_FIERY_PATH','MUDKIP':'MAP_ROUTE118',
 'TURTWIG':'MAP_ROUTE119','CHIMCHAR':'MAP_JAGGED_PASS','PIPLUP':'MAP_SHOAL_CAVE_LOW_TIDE_ENTRANCE_ROOM',
 'SNIVY':'MAP_ROUTE119','TEPIG':'MAP_FIERY_PATH','OSHAWOTT':'MAP_ROUTE118',
 'CHESPIN':'MAP_ROUTE119','FENNEKIN':'MAP_JAGGED_PASS','FROAKIE':'MAP_ROUTE118',
 'ROWLET':'MAP_ROUTE119','LITTEN':'MAP_JAGGED_PASS','POPPLIO':'MAP_ROUTE118',
 'GROOKEY':'MAP_PETALBURG_WOODS','SCORBUNNY':'MAP_FIERY_PATH','SOBBLE':'MAP_ROUTE118',
 'SPRIGATITO':'MAP_PETALBURG_WOODS','FUECOCO':'MAP_FIERY_PATH','QUAXLY':'MAP_ROUTE118'
}

# STAGE15_BALANCE: narrative progression buckets, no changes to native Hoenn tables.
# Story-based location is more reliable than the National Dex entry order.
EARLY_MAPS = {
 'MAP_ROUTE103', 'MAP_ROUTE104', 'MAP_ROUTE110', 'MAP_ROUTE116',
 'MAP_PETALBURG_WOODS', 'MAP_RUSTURF_TUNNEL',
}
MID_MAPS = {
 'MAP_ROUTE111', 'MAP_ROUTE112', 'MAP_ROUTE113', 'MAP_ROUTE114',
 'MAP_ROUTE115', 'MAP_ROUTE117', 'MAP_ROUTE118', 'MAP_ROUTE119',
 'MAP_ROUTE120', 'MAP_ROUTE121',
 'MAP_FIERY_PATH', 'MAP_JAGGED_PASS', 'MAP_NEW_MAUVILLE_ENTRANCE',
 'MAP_NEW_MAUVILLE_INSIDE', 'MAP_METEOR_FALLS_1F_1R',
}
EARLY_BONUS_PERCENT = 4
MID_BONUS_PERCENT = 8
LATE_BONUS_PERCENT = 10
LEGENDARY_BONUS_PERCENT = 1


def progression_tier(map_id):
    if map_id in EARLY_MAPS or map_id.startswith('MAP_GRANITE_CAVE'):
        return 0
    if map_id in MID_MAPS:
        return 1
    return 2


def bonus_percent(map_id):
    return (EARLY_BONUS_PERCENT, MID_BONUS_PERCENT, LATE_BONUS_PERCENT)[progression_tier(map_id)]


def read_dex(root):
    dex=(root/'include/constants/pokedex.h').read_text()
    national=dex.split('enum NationalDexOrder',1)[1].split('NATIONAL_DEX_PECHARUNT,',1)[0]
    names=[n for n in re.findall(r'^\s*NATIONAL_DEX_([A-Z0-9_]+),',national,re.M) if n!='NONE']+['PECHARUNT']
    if len(names)!=1025 or len(set(names))!=1025:raise ValueError('Expected exactly 1025 unique canonical National species')
    defined=set(re.findall(r'\bSPECIES_([A-Z0-9_]+)\b',(root/'include/constants/species.h').read_text()))
    if set(names)-defined:raise ValueError('Official species missing from enabled source')
    types={}
    power={}
    parents=defaultdict(set)
    canonical=set(names)
    for gen in range(1,10):
        s=(root/f'src/data/pokemon/species_info/gen_{gen}_families.h').read_text()
        blocks=list(re.finditer(r'^\s*\[SPECIES_([A-Z0-9_]+)\]\s*=\s*\{',s,re.M))
        for i,m in enumerate(blocks):
            n=m.group(1)
            chunk=s[m.end():blocks[i+1].start() if i+1<len(blocks) else len(s)]
            t=re.search(r'\.types\s*=\s*MON_TYPES\(\s*TYPE_([A-Z_]+)',chunk)
            if t:types[n]=t.group(1)
            stats=[re.search(r'\.base'+k+r'\s*=\s*(\d+)\b',chunk)
                   for k in ('HP','Attack','Defense','Speed','SpAttack','SpDefense')]
            if all(stats):
                power[n]=sum(int(v.group(1)) for v in stats)
            if n not in canonical or '.evolutions = EVOLUTION(' not in chunk:
                continue
            # The official species-info EVOLUTION tuples describe the graph.
            # Count only canonical targets: Mega/forms/custom Eeveelutions are
            # intentionally not extra stages of a National Dex species.
            evolution_section=chunk.split('.evolutions = EVOLUTION(',1)[1]
            for dest in re.findall(r'\{\s*EVO_[A-Z0-9_]+\s*,\s*[^,]+,\s*SPECIES_([A-Z0-9_]+)', evolution_section):
                if dest in canonical and dest!=n:
                    parents[dest].add(n)

    @lru_cache(None)
    def depth(n):
        if n not in canonical:
            return 0
        # All normal evolution chains are directed; an unexpected cycle
        # should be fixed upstream rather than creating bogus early encounters.
        return 0 if not parents[n] else 1+max(depth(p) for p in parents[n])

    stages={n:depth(n) for n in names}
    return names,types,power,stages

def available_areas(root):
    d=json.loads((root/'src/data/wild_encounters.json').read_text())
    maps={e['map'] for group in d['wild_encounter_groups'] if group.get('for_maps')
          for e in group.get('encounters',[]) if e.get('land_mons') and e.get('map')}
    def okay(m):
        if m.endswith('_FRLG') or m in {'MAP_ROUTE101','MAP_ROUTE102'}:return False
        if m.startswith('MAP_ROUTE'):
            num=re.match(r'MAP_ROUTE(\d+)',m)
            return bool(num and 103<=int(num.group(1))<=134)
        return m.startswith(('MAP_PETALBURG_WOODS','MAP_GRANITE_CAVE','MAP_RUSTURF_TUNNEL',
          'MAP_FIERY_PATH','MAP_JAGGED_PASS','MAP_NEW_MAUVILLE','MAP_DESERT_UNDERPASS',
          'MAP_MT_PYRE','MAP_METEOR_FALLS','MAP_SHOAL_CAVE_LOW_TIDE',
          'MAP_SKY_PILLAR','MAP_VICTORY_ROAD','MAP_SAFARI_ZONE_','MAP_ARTISAN_CAVE'))
    result=sorted(m for m in maps if okay(m))
    if len(result)<45:raise ValueError(f'Expected 45+ accessible Hoenn land habitat maps, got {len(result)}')
    return result

def map_matches(m,t):
    if t=='WATER':return any(k in m for k in ('ROUTE103','ROUTE104','ROUTE118','ROUTE119','ROUTE123','ROUTE130','SHOAL','METEOR_FALLS','SAFARI_ZONE_SOUTH'))
    if t=='ICE':return 'SHOAL' in m or 'METEOR' in m or 'VICTORY' in m
    if t=='FIRE':return any(k in m for k in ('FIERY','JAGGED','ROUTE111','ROUTE112','ROUTE113','VICTORY'))
    if t=='ELECTRIC':return any(k in m for k in ('MAUVILLE','ROUTE110','ROUTE117','ROUTE118','VICTORY'))
    if t in {'GHOST','DARK','PSYCHIC'}:return any(k in m for k in ('MT_PYRE','ROUTE120','ROUTE121','VICTORY','STEVENS_CAVE'))
    if t=='DRAGON':return any(k in m for k in ('SKY_PILLAR','METEOR_FALLS','VICTORY'))
    if t in {'ROCK','GROUND','STEEL','FIGHTING'}:return any(k in m for k in ('GRANITE','METEOR','VICTORY','DESERT','FIERY','JAGGED','ROUTE111','ROUTE114','MAUVILLE'))
    if t in {'GRASS','BUG','FAIRY'}:return any(k in m for k in ('WOODS','SAFARI','ROUTE104','ROUTE114','ROUTE117','ROUTE119','ROUTE120','ROUTE121','ROUTE123'))
    return any(k in m for k in ('ROUTE','SAFARI','WOODS','GRANITE','SKY_PILLAR'))

def patch(root):
    root=root.resolve()
    if not (root/'Makefile').exists():raise ValueError('Need Emerald Expansion source checkout')
    starter=root/'src/starter_choose.c'
    src=starter.read_text()
    before='#define GRASS_STARTER (IS_FRLG ? SPECIES_BULBASAUR  : SPECIES_EEVEE) // STAGE8K_EEVEE_STARTER: grass-position ball; still Eevee (Normal type)'
    after='#define GRASS_STARTER (IS_FRLG ? SPECIES_BULBASAUR  : SPECIES_TREECKO) // STAGE15_SOLO_DEX: restore Hoenn starters'
    if src.count(before)!=1:raise ValueError('Starter layout changed; refusing unsafe patch')
    # STAGE15_ART_AUDIT: investigate PC preview mismatch reported for Artheon.
    # The full 171-form bundle is reconstructed at build time.
    manifest=Path(__file__).parent/'stage10'/'manifest.json'
    if manifest.exists():
        forms=json.loads(manifest.read_text(encoding='utf-8')).get('forms',[])
        for form in forms:
            if 'ARTHEON' in form.get('name','').upper() or form.get('name','').upper() in ('AERIEON','AERARTHEON'):
                key=form['name'].upper()
                src_info=(root/'src/data/pokemon/species_info.h').read_text()
                hit=re.search(r'\[SPECIES_'+re.escape(key)+r'\]\s*=\s*\{([\s\S]*?)(?=\n    \},)',src_info)
                block=hit.group(1) if hit else ''
                ref=lambda prop:(re.search(r'\.'+prop+r'\s*=\s*([^,\n]+)',block).group(1).strip()
                                 if re.search(r'\.'+prop+r'\s*=\s*([^,\n]+)',block) else None)
                print('STAGE15_ART_AUDIT:',json.dumps({'form':form,'front':ref('frontPic'),'icon':ref('iconSprite'),
                     'iconPalIndex':ref('iconPalIndex'),'back':ref('backPic')},sort_keys=True)[:1500])
    names,types,power,stages=read_dex(root)
    maps=available_areas(root)
    pools=defaultdict(list)

    def min_wild_level(n):
        if n in RARE:
            return 45
        if stages[n]>=2:
            return 34   # final forms after the sixth-badge stretch
        if stages[n]==1:
            return 18   # middle forms, never on the opening routes
        return 1

    def min_area_tier(n):
        if n in RARE or stages[n]>=2 or power.get(n,420)>530:
            return 2
        if stages[n]>=1 or power.get(n,420)>390:
            return 1
        return 0

    for n in names:
        if n=='EEVEE':continue  # Existing Route 102 wild Eevee stays unchanged.
        rare=n in RARE
        if n in STARTERS:
            candidates=[STARTERS[n]]
        elif rare:
            candidates=[m for m in RARE_AREAS if m in maps and progression_tier(m)==2]
        else:
            candidates=[m for m in maps if map_matches(m,types.get(n,'NORMAL'))
                        and progression_tier(m)>=min_area_tier(n)]
        if not candidates:
            # Some biomes (especially Water and Ice) have no eligible late land
            # maps. Keep the species obtainable in a high-level late area
            # rather than silently sending its final evolution to Route 104.
            candidates=[m for m in maps if progression_tier(m)==2
                        and (m.startswith('MAP_VICTORY_ROAD') or
                             m.startswith('MAP_ARTISAN_CAVE'))]
        if not candidates:
            raise ValueError(f'Missing progression-safe habitat for {n}')
        def score(m):
            h=int.from_bytes(hashlib.sha256(f'{n}/{m}'.encode()).digest()[:4],'big')
            return (len(pools[(m,rare)]),h,m)
        m=min(candidates,key=score)
        pools[(m,rare)].append(n)
    total={n for pool in pools.values() for n in pool}
    if total!=set(names)-{'EEVEE'} or max(map(len,pools.values()))>65:
        raise ValueError('Progression-aware solo National Dex coverage/pool capacity failed')
    early_encounters={n for (m,rare),group in pools.items()
                      if progression_tier(m)==0 for n in group}
    if any(stages[n]>0 or power.get(n,420)>390 for n in early_encounters):
        raise ValueError('Evolved or overpowered species assigned to an early map')
    for example in ('AZUMARILL','DECIDUEYE','QUILLADIN'):
        if example in early_encounters:
            raise ValueError(f'{example} still appears on an opening route')
    entries,flat=[],[]
    for m in sorted({m for m,_ in pools}):
        ordinary=pools[(m,False)];legend=pools[(m,True)]
        a=len(flat);flat.extend(ordinary);b=len(flat);flat.extend(legend)
        entries.append(f'    {{MAP_GROUP({m}), MAP_NUM({m}), {a}, {len(ordinary)}, {b}, {len(legend)}, {bonus_percent(m)}}},')
    if len(flat)!=1024:raise ValueError('Incorrect pool count')
    data='\n'.join('    '+', '.join('SPECIES_'+n for n in flat[i:i+6])+',' for i in range(0,len(flat),6))
    mins='\n'.join('    '+', '.join(str(min_wild_level(n)) for n in flat[i:i+20])+',' for i in range(0,len(flat),20))
    c='''
// STAGE15_SOLO_DEX: biome-aware bonus catch pools for 1,024 National species.
// Eevee already appears natively on Route 102. No encounter table is removed.
struct Stage15Habitat { u8 group, num; u16 first, count, rareFirst, rareCount; u8 bonusChance; };
static const u16 sStage15Species[] = {
'''+data+'''
};
static const u8 sStage15MinLevel[] = {
'''+mins+'''
};
static const struct Stage15Habitat sStage15Maps[] = {
'''+ '\n'.join(entries)+'''
};
static bool8 Stage15_TryWildEncounter(enum WildPokemonArea area, enum Species *species, u8 *level)
{
    u32 i;
    if (area != WILD_AREA_LAND) return FALSE;
    for (i=0; i<ARRAY_COUNT(sStage15Maps); i++)
    {
        u32 index;
        const struct Stage15Habitat *p=&sStage15Maps[i];
        if (p->group != gSaveBlock1Ptr->location.mapGroup || p->num != gSaveBlock1Ptr->location.mapNum) continue;
        if (p->rareCount && Random()%100<1)
        {
            index=p->rareFirst + Random()%p->rareCount;
        }
        else if (p->count && Random()%100<p->bonusChance)
        {
            index=p->first + Random()%p->count;
        }
        else
        {
            return FALSE;
        }
        *species=sStage15Species[index];
        if (*level < sStage15MinLevel[index])
            *level=sStage15MinLevel[index];
        return TRUE;
    }
    return FALSE;
}

'''
    target=root/'src/wild_encounter.c';orig=target.read_text()
    anchor='bool8 TryGenerateWildMon(const struct WildPokemonInfo *wildMonInfo, enum WildPokemonArea area, u8 flags)\n{'
    if orig.count(anchor)!=1 or 'STAGE15_SOLO_DEX' in orig:raise ValueError('Unknown original wild encounter source')
    orig=orig.replace(anchor,c+anchor,1)
    a=orig.index(anchor);b=orig.index('static u16 GenerateFishingWildMon(',a)
    block=orig[a:b]
    call='    CreateWildMon(wildMonInfo->wildPokemon[wildMonIndex].species, level);'
    if block.count(call)!=1:raise ValueError('Wild encounter call changed')
    block=block.replace(call,'    enum Species wildSpecies = wildMonInfo->wildPokemon[wildMonIndex].species;\n    Stage15_TryWildEncounter(area, &wildSpecies, &level);\n    CreateWildMon(wildSpecies, level);',1)
    orig=orig[:a]+block+orig[b:]
    starter.write_text(src.replace(before,after,1))
    target.write_text(orig)
    report={'national_dex_species':1025,'bonus_species':len(flat),'wild_eevee':'MAP_ROUTE102',
       'restored_starters':['TREECKO','TORCHIC','MUDKIP'],'bonus_map_count':len(entries),
       'ordinary_encounter_chance_percent_by_tier':{'early':4,'mid':8,'late':10},
       'rare_encounter_chance_percent':1,
       'minimum_levels':{n:min_wild_level(n) for n in flat},
       'evolution_stage':{n:stages[n] for n in flat},
       'habitats':{m:{'tier':progression_tier(m),'bonus_chance_percent':bonus_percent(m),
                      'common':pools[(m,False)],'rare':pools[(m,True)]}
                   for m in sorted({m for m,_ in pools})}}
    (Path(__file__).parent/'stage15_solo_dex_report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(f'Stage15: restored Treecko / Torchic / Mudkip; Eevee remains wild Route 102.')
    print(f'Stage15: {len(flat)} additional species placed across {len(entries)} progression-safe Hoenn land habitats.')
    print('Stage15: early bonus 4%, mid 8%, late 10%; rare 1%; evolved species get minimum wild levels.')
    print('Stage15: all 1,025 National entries have an encounter path; no early final evolutions.')
    print('Stage15: original wild tables, all 171 Eevee forms, and saves unchanged.')

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('checkout',type=Path)
    patch(ap.parse_args().checkout)
