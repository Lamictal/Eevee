#!/usr/bin/env python3
"""Publish a generated learnset Markdown page back to the development branch.

Writes docs only; never uploads ROMs or changes game source. Requires the
workflow's limited GITHUB_TOKEN contents:write permission and a successful build.
"""
import base64
import json
import os
from pathlib import Path
import re
import time
import urllib.error
import urllib.parse
import urllib.request

URL = "https://api.github.com"
TARGET = "EEVEE_LEVEL_UP_MOVES.md"
BRANCH = "stage8e-cloud-prototype"

def request(method,url,payload=None):
    token=os.environ['GITHUB_TOKEN']
    data=json.dumps(payload).encode('utf8') if payload is not None else None
    req=urllib.request.Request(url,method=method,data=data,headers={
        'Authorization':'Bearer '+token,
        'Accept':'application/vnd.github+json',
        'Content-Type':'application/json',
        'X-GitHub-Api-Version':'2022-11-28',
        'User-Agent':'eevee-learnset-doc-publisher'})
    with urllib.request.urlopen(req,timeout=30) as response:
        return json.load(response)

def main():
    repo=os.environ['GITHUB_REPOSITORY']
    run=os.environ['GITHUB_RUN_ID']
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repo) or not run.isdigit():
        raise ValueError('Bad GitHub repository or build run')
    source=Path(TARGET)
    if not source.is_file():raise ValueError('The generated guide was not found')
    guide=source.read_text(encoding='utf8')
    if '172 entries (Eevee + 171 forms)' not in guide:
        raise ValueError('Guide coverage marker missing')
    guide=guide.replace(
        '# Eevee and all 171 Eeveelutions: level-up moves',
        '# Eevee and all 171 Eeveelutions: level-up moves\n\n'
        + '<!-- generated-by-run='+run+' -->\n\n'
        + 'Compiled source build: https://github.com/'+repo+'/actions/runs/'+run,
        1)
    path=urllib.parse.quote(TARGET,safe='')
    base=f'{URL}/repos/{repo}/contents/{path}'
    data=base64.b64encode(guide.encode('utf8')).decode('ascii')
    for attempt in range(5):
        sha=None
        try:
            current=request('GET',base+'?ref='+BRANCH)
            sha=current['sha']
            old=base64.b64decode(current['content']).decode('utf8')
            prev=re.search(r'generated-by-run=(\d+)',old)
            if prev and int(prev.group(1))>int(run):
                print('Skipped older build guide',run,'because',prev.group(1),'is newer')
                return
            if old==guide:
                print('Learnset guide already up to date')
                return
        except urllib.error.HTTPError as exc:
            if exc.code!=404:raise
        payload={'message':'docs: refresh level-up moves of Eevee and all 171 forms (run '+run+')',
                 'content':data,'branch':BRANCH}
        if sha:payload['sha']=sha
        try:
            result=request('PUT',base,payload)
            print('Published',TARGET,'at',result['commit']['sha'][:12])
            return
        except urllib.error.HTTPError as exc:
            if exc.code not in (409,422) or attempt==4:raise
            time.sleep(2)
    raise RuntimeError('Could not publish the generated guide')

if __name__=='__main__':
    main()
