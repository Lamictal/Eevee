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

def read_dex(root):
    dex=(root/'include/constants/pokedex.h').read_text()
    national=dex.split('enum NationalDexOrder',1)[1].split('NATIONAL_DEX_PECHARUNT,',1)[0]
    names=[n for n in re.findall(r'^\s*NATIONAL_DEX_([A-Z0-9_]+),',national,re.M) if n!='NONE']+['PECHARUNT']
    if len(names)!=1025 or len(set(names))!=1025:raise ValueError('Expected exactly 1025 unique canonical National species')
    defined=set(re.findall(r'\bSPECIES_([A-Z0-9_]+)\b',(root/'include/constants/species.h').read_text()))
    if set(names)-defined:raise ValueError('Official species missing from enabled source')
    types={}
    for gen in range(1,10):
        s=(root/f'src/data/pokemon/species_info/gen_{gen}_families.h').read_text()
        blocks=list(re.finditer(r'^\s*\[SPECIES_([A-Z0-9_]+)\]\s*=\s*\{',s,re.M))
        for i,m in enumerate(blocks):
            chunk=s[m.end():blocks[i+1].start() if i+1<len(blocks) else len(s)]
            t=re.search(r'\.types\s*=\s*MON_TYPES\(\s*TYPE_([A-Z_]+)',chunk)
            if t:types[m.group(1)]=t.group(1)
    return names,types

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
    names,types=read_dex(root)
    maps=available_areas(root)
    pools=defaultdict(list)
    for n in names:
        if n=='EEVEE':continue  # Existing Route 102 wild Eevee stays unchanged.
        rare=n in RARE
        if n in STARTERS:candidates=[STARTERS[n]]
        elif rare:candidates=[m for m in RARE_AREAS if m in maps]
        else:candidates=[m for m in maps if map_matches(m,types.get(n,'NORMAL'))]
        if not candidates:raise ValueError(f'Missing habitat: {n}')
        # Spread species deterministically; never crowd out native encounters.
        def score(m):
            h=int.from_bytes(hashlib.sha256(f'{n}/{m}'.encode()).digest()[:4],'big')
            return (len(pools[(m,rare)]),h,m)
        m=min(candidates,key=score)
        pools[(m,rare)].append(n)
    total={n for pool in pools.values() for n in pool}
    if total!=set(names)-{'EEVEE'} or max(map(len,pools.values()))>50:
        raise ValueError('Solo National Dex coverage/pool capacity failed')
    entries,flat=[],[]
    for m in sorted({m for m,_ in pools}):
        ordinary=pools[(m,False)];legend=pools[(m,True)]
        a=len(flat);flat.extend(ordinary);b=len(flat);flat.extend(legend)
        entries.append(f'    {{MAP_GROUP({m}), MAP_NUM({m}), {a}, {len(ordinary)}, {b}, {len(legend)}}},')
    if len(flat)!=1024:raise ValueError('Incorrect pool count')
    data='\n'.join('    '+', '.join('SPECIES_'+n for n in flat[i:i+6])+',' for i in range(0,len(flat),6))
    c='''
// STAGE15_SOLO_DEX: biome-aware bonus catch pools for 1,024 National species.
// Eevee already appears natively on Route 102. No encounter table is removed.
struct Stage15Habitat { u8 group, num; u16 first, count, rareFirst, rareCount; };
static const u16 sStage15Species[] = {
'''+data+'''
};
static const struct Stage15Habitat sStage15Maps[] = {
'''+ '\n'.join(entries)+'''
};
static bool8 Stage15_TryWildEncounter(enum WildPokemonArea area, enum Species *species)
{
    u32 i;
    if (area != WILD_AREA_LAND) return FALSE;
    for (i=0; i<ARRAY_COUNT(sStage15Maps); i++)
    {
        const struct Stage15Habitat *p=&sStage15Maps[i];
        if (p->group != gSaveBlock1Ptr->location.mapGroup || p->num != gSaveBlock1Ptr->location.mapNum) continue;
        if (p->rareCount && Random()%100<3)
        {
            *species=sStage15Species[p->rareFirst + Random()%p->rareCount];
            return TRUE;
        }
        if (p->count && Random()%100<12)
        {
            *species=sStage15Species[p->first + Random()%p->count];
            return TRUE;
        }
        return FALSE;
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
    block=block.replace(call,'    enum Species wildSpecies = wildMonInfo->wildPokemon[wildMonIndex].species;\n    Stage15_TryWildEncounter(area, &wildSpecies);\n    CreateWildMon(wildSpecies, level);',1)
    orig=orig[:a]+block+orig[b:]
    starter.write_text(src.replace(before,after,1))
    target.write_text(orig)
    report={'national_dex_species':1025,'bonus_species':len(flat),'wild_eevee':'MAP_ROUTE102',
       'restored_starters':['TREECKO','TORCHIC','MUDKIP'],'bonus_map_count':len(entries),
       'ordinary_encounter_chance_percent':12,'rare_encounter_chance_percent':3,
       'habitats':{m:{'common':pools[(m,False)],'rare':pools[(m,True)]} for m,_ in sorted(pools)}}
    (Path(__file__).parent/'stage15_solo_dex_report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(f'Stage15: restored Treecko / Torchic / Mudkip; Eevee remains wild Route 102.')
    print(f'Stage15: {len(flat)} additional species placed across {len(entries)} Hoenn land habitats; all 1,025 National entries directly encounterable.')
    print('Stage15: original wild tables, evolution mechanics, all 171 Eevee forms, and saves unchanged.')

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('checkout',type=Path)
    patch(ap.parse_args().checkout)
