#!/usr/bin/env python3
"""Maintain the easy-download link on GitHub after each successful alpha build.

Called by the *same* trusted workflow that uploads the ROM artifact. Uses the
scoped GitHub Actions token (contents:write) and edits only marked blocks.
Never uploads a ROM, creates a release, or broadens repo visibility.

Failure to update pages fails this publish step, so it is visible in Actions.
"""
import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HOST = "https://api.github.com"
START = "<!-- EEVEE_LATEST_BUILD_START -->"
END = "<!-- EEVEE_LATEST_BUILD_END -->"

def call(method, url, payload=None):
    token=os.environ.get("GITHUB_TOKEN","")
    if not token:
        raise RuntimeError("GITHUB_TOKEN not supplied")
    data=None if payload is None else json.dumps(payload).encode("utf8")
    req=urllib.request.Request(
        url,
        data=data,
        headers={
          "Authorization": f"Bearer {token}",
          "Accept": "application/vnd.github+json",
          "X-GitHub-Api-Version": "2022-11-28",
          "Content-Type": "application/json",
          "User-Agent": "eevee-build-link-updater"
        },
        method=method)
    with urllib.request.urlopen(req,timeout=30) as response:
        return json.load(response)

def fetch_artifact(repository, run_id):
    url=f"{HOST}/repos/{repository}/actions/runs/{run_id}/artifacts?per_page=100"
    # Github Actions artifact availability may lag upload-artifact by a few seconds.
    for attempt in range(6):
        result=call("GET",url)
        choices=[x for x in result.get("artifacts",[])
                 if x.get("name","").startswith("Eevee-All171-")
                 and not x.get("expired",False)]
        if len(choices)==1:
            return choices[0]
        if attempt<5:
            time.sleep(3)
    raise RuntimeError("Expected exactly one non-expired all-171 ROM artifact")

def update_page(repo,branch,path,new_block,run_id):
    url=f"{HOST}/repos/{repo}/contents/{urllib.parse.quote(path,safe='/')}?ref={urllib.parse.quote(branch,safe='')}"
    for attempt in range(4):
        f=call("GET",url)
        content=base64.b64decode(f["content"]).decode("utf8")
        if content.count(START)!=1 or content.count(END)!=1:
            raise RuntimeError(f"{branch}/{path} needs exactly one latest-build marker pair")
        start=content.index(START)
        end=content.index(END,start)
        old_block=content[start:end+len(END)]
        older=re.search(r"data-build-run=(\d+)",old_block)
        if older and int(older.group(1))>int(run_id):
            print(f"Skipped stale run for {branch}/{path}: existing run {older.group(1)} is newer")
            return
        updated=content[:start]+new_block+content[end+len(END):]
        if updated==content:
            print(f"Up to date: {branch}/{path}")
            return
        endpoint=url.split("?ref=")[0]
        payload={
            "message":f"docs: refresh latest Eevee alpha download link (run {run_id})",
            "content":base64.b64encode(updated.encode("utf8")).decode("ascii"),
            "sha":f["sha"],
            "branch":branch
        }
        try:
            result=call("PUT",endpoint,payload)
            print(f"Updated {branch}/{path} -> {result['commit']['sha'][:12]}")
            return
        except urllib.error.HTTPError as ex:
            if ex.code!=409 or attempt==3:
                raise
    raise RuntimeError(f"GitHub content update conflict on {branch}/{path}")

def main():
    repo=os.environ["GITHUB_REPOSITORY"]
    run_id=os.environ["GITHUB_RUN_ID"]
    label=os.environ.get("EEVEE_BUILD_LABEL","171-form Eevee alpha").strip()
    if not re.fullmatch(r"[A-Za-z0-9_./-]+/[A-Za-z0-9_.-]+",repo):
        raise ValueError("Invalid GitHub repo")
    if not run_id.isdigit():
        raise ValueError("Invalid run ID")
    artifact=fetch_artifact(repo,run_id)
    link=f"https://github.com/{repo}/actions/runs/{run_id}/artifacts/{artifact['id']}"
    run=f"https://github.com/{repo}/actions/runs/{run_id}"
    safe_label=label.replace("|","/").replace("\n"," ")
    base=f"{START}\n<!-- data-build-run={run_id} -->\n"
    foot=f"\n{END}"
    main_block=(
      base+
      f"### [VIEW THE LATEST DEVELOPMENT BUILD]({run})\n\n"
      f"**{safe_label}** · [Build details]({run})\n\n"
      "**Not a public patch release:** the build page contains a temporary GitHub "
      "Actions artifact for testing. Sign-in may be required. "
      "See [the download guide](DOWNLOAD.md)."
      +foot
    )
    download_block=(
      base+
      f"**[VIEW THE LATEST TEMPORARY DEVELOPMENT BUILD]({run})**\n\n"
      f"**{safe_label}** · [Successful build details]({run})\n\n"
      "On the build page open **Artifacts** for the ZIP if GitHub permits access. "
      "Artifacts expire after 14 days; this is not a permanent public patch release."
      +foot
    )
    dev_block=(
      base+
      f"> **Latest development build:** [{safe_label}]({run}). "
      "Find its alpha ZIP under **Artifacts**; temporary artifact, "
      "not a cleared public patch release."
      +foot
    )
    for branch,path,block in [
        ("main","README.md",main_block),
        ("main","DOWNLOAD.md",download_block),
        ("stage8e-cloud-prototype","README.md",dev_block)
    ]:
        update_page(repo,branch,path,block,run_id)
    print("All marked download links synchronized. No ROM uploaded to GitHub releases.")

if __name__=="__main__":
    main()
