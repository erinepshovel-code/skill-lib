#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "skills.json"
REQUIRED = ["## Trigger", "## Non-trigger", "## Sources of truth", "## Workflow", "## Boundaries", "## Output", "## Validation", "## hmmm"]

def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    failures = []
    names = set()
    for entry in data["skills"]:
        name = entry["name"]
        if name in names:
            failures.append(f"duplicate skill name: {name}")
        names.add(name)
        path = ROOT / entry["path"]
        if not path.exists():
            failures.append(f"missing: {entry['path']}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\nname:"):
            failures.append(f"bad frontmatter start: {entry['path']}")
        for section in REQUIRED:
            if section not in text:
                failures.append(f"{entry['path']}: missing {section}")
    registered = {str((ROOT / e["path"]).relative_to(ROOT)) for e in data["skills"]}
    present = {str(p.relative_to(ROOT)) for p in ROOT.glob("*/SKILL.md")}
    for orphan in sorted(present - registered):
        failures.append(f"unregistered skill: {orphan}")
    if failures:
        print("FAIL")
        for f in failures:
            print("-", f)
        return 1
    print(f"PASS: {len(names)} skills registered and structurally complete")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
