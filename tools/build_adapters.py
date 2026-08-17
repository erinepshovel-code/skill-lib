#!/usr/bin/env python3
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REG = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))
OUT = ROOT / "skills"

def render(entry):
    canonical = entry["path"]
    name = entry["name"]
    desc = entry["description"].replace("\n", " ")
    return f"---\nname: {name}\ndescription: {desc}\n---\n\n# generated adapter\n\nCanonical source: `../../{canonical}`.\n\nLoad and follow the canonical root skill. Do not edit this adapter by hand.\n"

def main(check=False):
    failures=[]
    for entry in REG["skills"]:
        path=OUT/entry["name"]/"SKILL.md"
        expected=render(entry)
        if check:
            actual=path.read_text(encoding="utf-8") if path.exists() else None
            if actual != expected:
                failures.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8")
    if failures:
        print("DRIFT")
        for f in failures: print("-", f)
        return 1
    print(("PASS" if check else "WROTE") + f": {len(REG['skills'])} adapters")
    return 0

if __name__ == "__main__":
    import sys
    raise SystemExit(main(check="--check" in sys.argv))
