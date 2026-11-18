#!/usr/bin/env python3
"""mGBA GUI smoke test under Xvfb. Screenshots are evidence, not semantic assertions."""
import argparse, hashlib, json, os, subprocess, time
from pathlib import Path

def run(*args):
    return subprocess.check_output(args, text=True).strip()

def main():
    p=argparse.ArgumentParser()
    p.add_argument("rom",type=Path)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    a.out.mkdir(parents=True,exist_ok=True)
    report={"status":"failed","scope":"boot, window responsiveness, screen changes and scripted input only","screenshots":[]}
    proc=subprocess.Popen(["mgba-qt",str(a.rom.resolve())], stdout=subprocess.DEVNULL,stderr=(a.out/"emulator.log").open("w"))
    try:
        window=None
        for _ in range(30):
            if proc.poll() is not None: raise RuntimeError("Emulator exited during startup")
            try:
                window=run("xdotool","search","--onlyvisible","--pid",str(proc.pid)).splitlines()[-1]
                break
            except (subprocess.CalledProcessError,IndexError): time.sleep(1)
        if not window: raise RuntimeError("No emulator window")
        run("xdotool","windowfocus","--sync",window)
        def capture(name):
            if proc.poll() is not None: raise RuntimeError("Emulator exited")
            path=a.out/(name+".png")
            run("import","-window",window,str(path))
            digest=hashlib.sha256(path.read_bytes()).hexdigest()
            report["screenshots"].append({"file":path.name,"sha256":digest})
            return digest
        time.sleep(3)
        first=capture("boot")
        time.sleep(8)
        second=capture("title_wait")
        run("xdotool","key","--window",window,"Return")
        time.sleep(2)
        third=capture("after_start")
        run("xdotool","key","--window",window,"x")
        time.sleep(3)
        fourth=capture("after_confirm")
        if len({first,second,third,fourth})<2: raise RuntimeError("No visible screen changes")
        report["status"]="passed"
        report["limitations"]="Screenshots do not prove title/menu correctness, gameplay progression or input acceptance."
    except Exception as e:
        report["error"]=str(e)
        raise
    finally:
        proc.terminate()
        try: proc.wait(timeout=5)
        except subprocess.TimeoutExpired: proc.kill(); proc.wait()
        (a.out/"report.json").write_text(json.dumps(report,indent=2)+"\n")

if __name__=="__main__": main()
