#!/usr/bin/env python3
"""mGBA GUI smoke test under Xvfb. Screenshots are evidence, not semantic assertions."""
import argparse, hashlib, json, os, subprocess, time, tempfile
from PIL import Image
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
    config=tempfile.TemporaryDirectory()
    cfg=Path(config.name)/"mgba"
    cfg.mkdir()
    (cfg/"config.ini").write_text("[ports.qt]\ndisplayDriver=0\naudioDriver=0\nvolume=0\nmute=1\n")
    env=dict(os.environ, XDG_CONFIG_HOME=config.name, QT_OPENGL="software", LIBGL_ALWAYS_SOFTWARE="1", SDL_AUDIODRIVER="dummy", QT_XCB_GL_INTEGRATION="none")
    proc=subprocess.Popen(["mgba-qt",str(a.rom.resolve())], env=env, stdout=subprocess.DEVNULL,stderr=(a.out/"emulator.log").open("w"))
    try:
        window=None
        for _ in range(30):
            if proc.poll() is not None: raise RuntimeError("Emulator exited during startup")
            try:
                windows=run("xdotool","search","--onlyvisible","--pid",str(proc.pid)).splitlines()
                def area(w):
                    g=run("xdotool","getwindowgeometry","--shell",w)
                    d=dict(line.split("=",1) for line in g.splitlines() if "=" in line)
                    return int(d.get("WIDTH",0))*int(d.get("HEIGHT",0))
                window=max(windows,key=area)
                if area(window)<240*160: raise IndexError("window too small")
                break
            except (subprocess.CalledProcessError,IndexError): time.sleep(1)
        if not window: raise RuntimeError("No emulator window")
        run("xdotool","windowfocus","--sync",window)
        def capture(name):
            if proc.poll() is not None: raise RuntimeError("Emulator exited")
            path=a.out/(name+".png")
            run("import","-window",window,str(path))
            with Image.open(path) as im:
                pixels=im.convert("RGB")
                digest=hashlib.sha256(pixels.tobytes()).hexdigest()
            run("import","-window","root",str(a.out/(name+"_desktop.png")))
            report["screenshots"].append({"file":path.name,"sha256":digest})
            return digest
        time.sleep(3)
        first=capture("boot")
        time.sleep(15)
        second=capture("title_wait")
        run("xdotool","key","Return")
        time.sleep(2)
        third=capture("after_start")
        run("xdotool","key","x")
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
        config.cleanup()
        (a.out/"report.json").write_text(json.dumps(report,indent=2)+"\n")

if __name__=="__main__": main()
