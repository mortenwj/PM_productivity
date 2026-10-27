# -*- coding: utf-8 -*-
"""Emit markdown tables for §1 from wit_get_work_items_batch_by_ids JSON dumps."""
import json
import pathlib
import re
import sys

BASE = "https://tieto-si.visualstudio.com/360/_workitems/edit"
def esc(s):
    if s is None:
        return ""
    return (
        str(s)
        .replace("|", "\\|")
        .replace("\n", " ")
        .replace("\r", "")[:200]
    )


def row(wi):
    f = wi.get("fields", {})
    aid = f.get("System.Id")
    title = esc(f.get("System.Title", ""))
    state = esc(f.get("System.State", ""))
    changed = esc(f.get("System.ChangedDate", ""))
    assign = f.get("System.AssignedTo")
    if isinstance(assign, dict):
        assign = assign.get("displayName", str(assign))
    assign = esc(assign)
    return f"| [{aid}]({BASE}/{aid}) | {title} | {state} | {changed} | {assign} |"


def emit_table(out, title, work_items, sort_key=None):
    items = list(work_items)
    if sort_key:
        items.sort(key=sort_key)
    out.write(f"### {title}\n\n")
    out.write(f"*Rows: **{len(items)}** (feed `hasMore: false` this run.)*\n\n")
    out.write("| ID | Title | State | Changed (UTC) | Assigned to |\n")
    out.write("|----|-------|-------|-----------------|---------------|\n")
    for wi in items:
        out.write(row(wi) + "\n")
    out.write("\n")


def main():
    assigned_path = pathlib.Path(sys.argv[1])
    myactivity_path = pathlib.Path(sys.argv[2])
    out_path = pathlib.Path(sys.argv[3])
    feed_ids_path = pathlib.Path(sys.argv[4]) if len(sys.argv) > 4 else None
    assigned_raw = json.loads(assigned_path.read_text(encoding="utf-8"))
    my_raw = json.loads(myactivity_path.read_text(encoding="utf-8"))
    by_id = {x["id"]: x for x in assigned_raw}
    if feed_ids_path and feed_ids_path.is_file():
        raw = feed_ids_path.read_text(encoding="utf-8").strip()
        feed_ids = [int(x.strip()) for x in raw.split(",") if x.strip()]
        if len(feed_ids) > 100:
            feed_ids = feed_ids[:100]
        assigned_rows = [by_id[i] for i in feed_ids if i in by_id]
    else:
        assigned_rows = sorted(by_id.values(), key=lambda x: x.get("fields", {}).get("System.Id", 0))
    with out_path.open("w", encoding="utf-8") as out:
        emit_table(out, "Assigned to me (all)", assigned_rows)
        emit_table(out, "My activity (all)", my_raw, sort_key=lambda x: x.get("id", 0))


if __name__ == "__main__":
    main()
