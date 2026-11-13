#!/usr/bin/env python3
"""Publish the generated encounter-rate guide on both public documentation branches.

Uses the Actions contents:write token after a successful ROM source build.
Never uploads save files or ROM binaries. Older concurrent builds cannot
overwrite a newer published page.
"""
import base64
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

PAGE = "ENCOUNTERS.md"
BRANCHES = ("main", "stage8e-cloud-prototype")
API = "https://api.github.com"

def request(method,url,data=None):
    token=os.environ["GITHUB_TOKEN"]
    req=urllib.request.Request(url,method=method,
        data=json.dumps(data).encode("utf8") if data is not None else None,
        headers={
            "Authorization":"Bearer "+token,
            "Accept":"application/vnd.github+json",
            "Content-Type":"application/json",
            "X-GitHub-Api-Version":"2022-11-28",
            "User-Agent":"eevee-encounter-guide-publisher"
        })
    with urllib.request.urlopen(req,timeout=40) as r:
        return json.load(r)

def publish(repo, branch, run, content):
    endpoint=API+"/repos/"+repo+"/contents/"+urllib.parse.quote(PAGE,safe="")
    encoded=base64.b64encode(content.encode("utf8")).decode("ascii")
    for attempt in range(6):
        sha=None
        try:
            existing=request("GET",endpoint+"?ref="+urllib.parse.quote(branch,safe=""))
            sha=existing["sha"]
            previous=base64.b64decode(existing["content"]).decode("utf8")
            previous_run=re.search(r"generated-by-run=(\d+)",previous)
            if previous_run and int(previous_run.group(1))>int(run):
                print(f"Skipping older run {run} for {branch}; newer run {previous_run.group(1)} published")
                return
            if previous==content:
                print(f"Unchanged: {branch}/{PAGE}")
                return
        except urllib.error.HTTPError as e:
            if e.code!=404:
                raise
        payload={
            "message":"docs: update area-by-area wild encounter chances (build "+run+")",
            "content":encoded,
            "branch":branch,
        }
        if sha:
            payload["sha"]=sha
        try:
            result=request("PUT",endpoint,payload)
            print(f"Published {branch}/{PAGE}: {result['commit']['sha'][:12]}")
            return
        except urllib.error.HTTPError as e:
            if e.code not in (409,422) or attempt==5:
                raise
            time.sleep(2)
    raise RuntimeError("Could not publish the encounter guide")

def main():
    repo=os.environ["GITHUB_REPOSITORY"]
    run=os.environ["GITHUB_RUN_ID"]
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+",repo) or not run.isdigit():
        raise ValueError("Invalid repository or workflow run")
    guide=Path(PAGE).read_text(encoding="utf8")
    if "# Pokémon Eevee: complete wild encounter rates by area" not in guide:
        raise ValueError("Encounter guide headline missing")
    if "**Coverage:**" not in guide or "## Route 104" not in guide or "## Route 102" not in guide:
        raise ValueError("Encounter guide coverage or early-route examples missing")
    guide=guide.replace(
        "# Pokémon Eevee: complete wild encounter rates by area",
        "# Pokémon Eevee: complete wild encounter rates by area\n\n"
        + "<!-- generated-by-run="+run+" -->\n\n"
        + "Source build: https://github.com/"+repo+"/actions/runs/"+run,
        1
    )
    for branch in BRANCHES:
        publish(repo,branch,run,guide)

if __name__=="__main__":
    main()
