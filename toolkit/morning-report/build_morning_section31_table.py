# -*- coding: utf-8 -*-
import json
import pathlib
import sys

BASE = "https://tieto-si.visualstudio.com/360/_workitems/edit"


def esc(s):
    if s is None:
        return ""
    return str(s).replace("|", "\\|").replace("\n", " ")[:120]


def main():
    path = pathlib.Path(sys.argv[1])
    out = pathlib.Path(sys.argv[2])
    limit = int(sys.argv[3])
    data = json.loads(path.read_text(encoding="utf-8"))
    data.sort(key=lambda x: x["fields"].get("System.ChangedDate", ""), reverse=True)
    lines = []
    lines.append("| ID | Title | State | Changed (UTC) | Assigned to |")
    lines.append("|----|-------|-------|----------------|---------------|")
    for wi in data[:limit]:
        f = wi["fields"]
        aid = f.get("System.Id")
        assign = f.get("System.AssignedTo")
        if isinstance(assign, dict):
            assign = assign.get("displayName", "")
        lines.append(
            f"| [{aid}]({BASE}/{aid}) | {esc(f.get('System.Title'))} | {esc(f.get('System.State'))} | {esc(f.get('System.ChangedDate'))} | {esc(assign)} |"
        )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
