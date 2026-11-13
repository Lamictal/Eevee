#!/usr/bin/env python3
"""Generate level-up move tables from the exact generated Emerald ROM source."""
import argparse, json, re
from pathlib import Path
from collections import defaultdict

ENTRY = re.compile(r'(?m)^    \[SPECIES_([A-Z0-9_]+)\]\s*=\s*\{')
DEF = re.compile(r'(?m)^\s*static const struct LevelUpMove\s+(s[A-Za-z0-9_]+)\[\]\s*=\s*\{')
MOVE = re.compile(r'\bLEVEL_UP_MOVE\s*\(\s*(\d+)\s*,\s*(MOVE_[A-Z0-9_]+)\s*\)')

def pointers(root):
    files=sorted((root/'src/data/pokemon/species_info').glob('gen_*_families.h'))
    files.append(root/'src/data/pokemon/species_info.h')
    found=defaultdict(list)
    for file in files:
        text=file.read_text(encoding='utf8')
        blocks=list(ENTRY.finditer(text))
        for i,m in enumerate(blocks):
            end=blocks[i+1].start() if i+1<len(blocks) else len(text)
            body=text[m.end():end]
            close=re.search(r'(?m)^    \},?\s*$',body)
            if close:body=body[:close.start()]
            ptr=re.findall(r'\.levelUpLearnset\s*=\s*([A-Za-z0-9_]+)',body)
            found[m.group(1)].append((file.name,ptr))
    return found

def defs(root):
    found=defaultdict(list)
    config=(root/'include/config/pokemon.h').read_text(encoding='utf8')
    selected=re.search(r'(?m)^#define\\s+P_LVL_UP_LEARNSETS\\s+(GEN_LATEST|GEN_[1-9])\\b',config)
    if not selected:
        raise ValueError('Cannot identify active level-up learnset generation from build config')
    generation=9 if selected.group(1)=='GEN_LATEST' else int(selected.group(1).split('_')[1])
    file=root/f'src/data/pokemon/level_up_learnsets/gen_{generation}.h'
    if not file.is_file():
        raise ValueError('Active generation learnset file not found: '+str(file))
    print(f'Active level-up configuration: {selected.group(1)} -> gen_{generation}.h')
    files=[file]
    for file in files:
        text=file.read_text(encoding='utf8')
        matches=list(DEF.finditer(text))
        for i,m in enumerate(matches):
            body=text[m.end():matches[i+1].start() if i+1<len(matches) else len(text)]
            end=re.search(r'\n\s*\};',body)
            if end is None:raise ValueError('No closing learnset brace: '+m.group(1))
            body=body[:end.start()]
            moves=[(int(a),b) for a,b in MOVE.findall(body)]
            if not moves or len(moves)!=len(re.findall(r'\bLEVEL_UP_MOVE\s*\(',body)):
                raise ValueError('Unexpected move list in '+m.group(1))
            if '#if ' in body or '#elif ' in body or '#else' in body:
                raise ValueError('Conditional move list needs preprocessor evaluation: '+m.group(1))
            found[m.group(1)].append((file.name,moves))
    return found

def pretty(symbol):
    exceptions={'FEINT_ATTACK':'Feint Attack','HI_JUMP_KICK':'Hi Jump Kick',
                'DOUBLE_EDGE':'Double-Edge','X_SCISSOR':'X-Scissor',
                'U_TURN':'U-turn','V_CREATE':'V-create','WILL_O_WISP':'Will-O-Wisp'}
    word=symbol.removeprefix('MOVE_')
    return exceptions.get(word,word.replace('_',' ').title())

def generate(checkout,manifest,output):
    checkout=checkout.resolve()
    forms=json.loads(manifest.read_text(encoding='utf8'))['forms']
    if len(forms)!=171 or len({f['name'].upper() for f in forms})!=171:
        raise ValueError('Require exactly 171 distinct named Eeveelutions in Stage 10 manifest')
    members=[{'name':'Eevee','types':['NORMAL'],'key':'ORIGINAL_EEVEE'}]+forms
    allptr=pointers(checkout)
    alllearn=defs(checkout)
    rows=[]
    for item in members:
        species=item['name'].upper()
        names=allptr.get(species,[])
        if len(names)!=1 or len(names[0][1])!=1:
            raise ValueError('Ambiguous or absent explicit learnset for '+species+': '+str(names))
        ptr=names[0][1][0]
        match=alllearn.get(ptr,[])
        if len(match)!=1:
            raise ValueError('Ambiguous or absent move array for '+species+': '+ptr+' '+str(len(match)))
        file,moves=match[0]
        rows.append((item,ptr,file,moves))
    grouped=defaultdict(list)
    for item,ptr,file,moves in rows:
        grouped[ptr].append(item['name'])
    reused={k:v for k,v in grouped.items() if len(v)>1}
    text=[
        '# Eevee and all 171 Eeveelutions: level-up moves',
        '',
        '> GENERATED FROM THE COMPILED STAGE 15.1 SOURCE, not an external move database.',
        '> This is a level-up reference, NOT a TM, tutor, egg-move or breeding guide.',
        '> Level 1 means starting/relearner moves; evolving does not automatically',
        '> teach every move listed at lower levels. Gameplay verification remains pending.',
        '',
        '**Family coverage:** 172 entries (Eevee + 171 forms). '
          +str(len(grouped))+' distinct learnset arrays; '
          +str(sum(len(v) for v in reused.values()))+' species share an array.',
        '',
        '## How to read this',
        '',
        '- A level 0 entry, where present, means a move learned on evolution.',
        '- Level-up moves are tied to the evolved species. Evolving with a catalyst or',
        '  type item does not itself guarantee a move from earlier levels.',
        '- Custom first evolutions require level 15+ and their catalyst; dual forms',
        '  require level 38+, six Gym Badges and a second-type booster item.',
        '- The schedule below is sourced from the active compiled species pointer.',
        '  If several forms share one learnset pointer, they have the same move levels.',
        '- Move labels are rendered from C move constants; in-game display names',
        '  may have different punctuation. Wild, TM/HM, tutor and egg moves are separate.',
        '',
        '## Shared / provisional learnsets audit',
        ''
    ]
    if reused:
        text.append('The following species reuse the same existing move schedule:')
        text.append('')
        for ptr,names in sorted(reused.items(),key=lambda z:(-len(z[1]),z[0])):
            text.append('- '+ptr+' ('+str(len(names))+'): '+', '.join(names))
    else:
        text.append('All species have distinct named learnsets.')
    text+=['','## Full level-up tables','']
    for item,ptr,file,moves in rows:
        label=item['name']+' ('+'/'.join(t.title() for t in item['types'])+')'
        text+=['### '+label,'','Source: '+file+'; pointer: '+ptr,'',
               '| Level | Move(s) |','|---:|---|']
        buckets=defaultdict(list)
        for lv,move in moves:
            if lv<0 or lv>100:raise ValueError('Unusual level for '+label+': '+str(lv))
            buckets[lv].append(pretty(move))
        for lv,stuff in sorted(buckets.items()):
            txt='Evolution' if lv==0 else '1 (start/relearn)' if lv==1 else str(lv)
            text.append('| '+txt+' | '+', '.join(stuff)+' |')
        text.append('')
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text('\n'.join(text)+'\n',encoding='utf8')
    print(json.dumps({'entries':len(rows),'distinct_learnsets':len(grouped),
        'shared_species':sum(len(v) for v in reused.values()),'bytes':output.stat().st_size,
        'Eevee':rows[0][3][:12],'Aerieon':next((q[3][:12] for q in rows if q[0]['name']=='Aerieon'),None)}))

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--checkout',type=Path,required=True)
    p.add_argument('--manifest',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    generate(a.checkout,a.manifest,a.output)
