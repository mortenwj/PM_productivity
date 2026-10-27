"""Split NVE behov.xlsx Status column into DevOps link + ADO state."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font

SOURCE = Path(r"C:\Users\MortenJensen\OneDrive - Tieto\NVE behov.xlsx")
OUTPUT = Path(r"C:\Users\MortenJensen\OneDrive - Tieto\NVE behov - DevOps status.xlsx")
ADO_CACHE = Path(__file__).resolve().parent / "nve_behov_ado_cache.json"
ADO_BASE = "https://dev.azure.com/tieto-si/360/_workitems/edit/{id}"
NO_SPRINT = "Ingen sprint"
DROP_TAIL_COLUMNS = frozenset({"Rett"})
TEAM_BACKLOG_ITERATIONS = frozenset(
    {
        r"360\core\Process-platform",
    }
)

URL_RE = re.compile(
    r"https?://(?:dev\.azure\.com/tieto-si|tieto-si\.visualstudio\.com)/360/_workitems/edit/(\d+)",
    re.I,
)
WI_RE = re.compile(r"(?:User Story|Bug|Feature)\s+(\d+)\b", re.I)


def extract_work_item_id(text: object) -> int | None:
    wid, _, _ = parse_status_cell(text)
    return wid


def collect_ids_from_sheet(rows_in: list[tuple]) -> set[int]:
    if not rows_in or not rows_in[0]:
        return set()
    header = list(rows_in[0])
    link_indices: list[int] = []
    if "DevOps link" in header:
        link_indices.append(header.index("DevOps link"))
    if "Status" in header:
        link_indices.append(header.index("Status"))
    if not link_indices:
        link_indices = [3]
    ids: set[int] = set()
    for row in rows_in[1:]:
        row = list(row)
        for idx in link_indices:
            if len(row) > idx:
                wid = extract_work_item_id(row[idx])
                if wid is not None:
                    ids.add(wid)
                    break
    return ids


def missing_cache_entries(sheet_ids: set[int], ado: dict) -> list[int]:
    missing: list[int] = []
    for wid in sorted(sheet_ids):
        if str(wid) not in ado and wid not in ado:
            missing.append(wid)
    return missing


def load_source(path: Path) -> Path:
    try:
        load_workbook(path, read_only=True).close()
        return path
    except PermissionError:
        import shutil
        import tempfile

        dest = Path(tempfile.gettempdir()) / "NVE_behov_copy.xlsx"
        shutil.copy2(path, dest)
        return dest


def parse_status_cell(text: object) -> tuple[int | None, str | None, str | None]:
    """Return (work_item_id, hyperlink_url, local_note)."""
    if text is None or str(text).strip() == "":
        return None, None, None

    raw = str(text).strip()
    flat = raw.replace("\n", " ")

    wid: int | None = None
    m = URL_RE.search(flat)
    if m:
        wid = int(m.group(1))
    else:
        m2 = WI_RE.search(flat)
        if m2:
            wid = int(m2.group(1))

    link = ADO_BASE.format(id=wid) if wid else None

    lines = [ln.strip() for ln in raw.split("\n") if ln.strip()]
    local_note: str | None = None
    if lines and lines[0].lower().startswith("meldt inn"):
        local_note = lines[0]
    elif wid is None:
        local_note = raw

    return wid, link, local_note


def link_label(wid: int, ado: dict) -> str:
    info = ado.get(str(wid)) or ado.get(wid)
    if not info:
        return str(wid)
    wtype = info.get("type", "Work item")
    title = info.get("title", "")
    return f"{wtype} {wid}: {title}"


def format_sprint(info: dict | None) -> str:
    if not info:
        return NO_SPRINT
    path = (info.get("iteration_path") or "").strip()
    if not path or path == "360":
        return NO_SPRINT
    normalized = path.replace("/", "\\")
    if normalized in TEAM_BACKLOG_ITERATIONS:
        return NO_SPRINT
    return normalized


def format_tags(info: dict | None) -> str:
    if not info:
        return ""
    raw = (info.get("tags") or "").strip()
    if not raw:
        return ""
    parts = [p.strip() for p in raw.split(";") if p.strip()]
    return "; ".join(parts)


def work_item_type(info: dict | None, wid: int | None, link_cell: object) -> str:
    if info and info.get("type"):
        return info["type"]
    if link_cell:
        s = str(link_cell)
        m = re.match(r"^(User Story|Bug|Feature)\s+\d+", s, re.I)
        if m:
            t = m.group(1)
            return "User Story" if t.lower() == "user story" else t.title()
    return ""


def row_identity(tema: object, besk: object, wid: int | None) -> tuple:
    if wid is not None:
        return ("id", wid)
    return (
        "row",
        str(tema or "").strip().casefold(),
        str(besk or "").strip().casefold(),
    )


def load_preserved_output_rows() -> list[tuple]:
    """Rows present in OUTPUT but not rebuildable from SOURCE (manual additions)."""
    if not OUTPUT.is_file():
        return []
    try:
        wb = load_workbook(OUTPUT, read_only=True, data_only=True)
    except PermissionError:
        return []
    ws = wb["In progress"]
    rows = list(ws.iter_rows(values_only=True))
    wb.close()
    if not rows:
        return []
    header = list(rows[0])
    if "DevOps link" not in header:
        return []
    link_idx = header.index("DevOps link")
    tema_idx = header.index("Tema") if "Tema" in header else 0
    besk_idx = header.index("Beskrivelse") if "Beskrivelse" in header else 1
    out: list[tuple] = []
    for row in rows[1:]:
        row = list(row)
        while len(row) < len(header):
            row.append(None)
        wid = extract_work_item_id(row[link_idx])
        out.append((row_identity(row[tema_idx], row[besk_idx], wid), tuple(row)))
    return out


def build(ado: dict[str, dict]) -> None:
    src = load_source(SOURCE)
    wb_in = load_workbook(src, read_only=True, data_only=True)
    ws_in = wb_in["In progress"]
    rows_in = list(ws_in.iter_rows(values_only=True))
    wb_in.close()

    preserved_by_key = {k: row for k, row in load_preserved_output_rows()}

    wb_out = Workbook()
    ws_out = wb_out.active
    ws_out.title = "In progress"

    header_in = list(rows_in[0])
    # Replace single Status column with split columns
    status_idx = header_in.index("Status") if "Status" in header_in else 3
    tail_header = [
        c for c in header_in[status_idx + 1 :] if c not in DROP_TAIL_COLUMNS
    ]
    sprint_idx_in_tail: int | None = None
    if "Sprint" in tail_header:
        sprint_idx_in_tail = tail_header.index("Sprint")
        tail_header.insert(sprint_idx_in_tail + 1, "Tags")
    else:
        tail_header.extend(["Sprint", "Tags"])

    prefix_header = list(header_in[:status_idx])
    if len(prefix_header) >= 2:
        prefix_header = prefix_header[:2] + ["Work item type"] + prefix_header[2:]
    else:
        prefix_header = prefix_header + ["Work item type"]

    new_header = prefix_header + [
        "DevOps link",
        "ADO Status",
    ] + tail_header
    ws_out.append(new_header)
    link_col = new_header.index("DevOps link") + 1
    type_col = new_header.index("Work item type") + 1

    link_font = Font(color="0563C1", underline="single")
    built_keys: set[tuple] = set()

    for row in rows_in[1:]:
        row = list(row)
        while len(row) < len(header_in):
            row.append(None)

        wid, link, _local_note = parse_status_cell(row[status_idx])
        info = None
        ado_state = ""
        if wid is not None:
            info = ado.get(str(wid)) or ado.get(wid)
            if info:
                ado_state = info.get("state", "")
            else:
                ado_state = "(not found in ADO)"

        tail_row = [
            row[status_idx + 1 + i]
            for i, col in enumerate(header_in[status_idx + 1 :])
            if col not in DROP_TAIL_COLUMNS
        ]
        if sprint_idx_in_tail is not None:
            while len(tail_row) <= sprint_idx_in_tail:
                tail_row.append(None)
            tail_row[sprint_idx_in_tail] = format_sprint(info)
            tail_row.insert(sprint_idx_in_tail + 1, format_tags(info))
        else:
            tail_row.extend([format_sprint(info), format_tags(info)])

        prefix_row = list(row[:status_idx])
        if len(prefix_row) >= 2:
            prefix_row = prefix_row[:2] + [work_item_type(info, wid, None)] + prefix_row[2:]
        else:
            prefix_row = prefix_row + [work_item_type(info, wid, None)]

        new_row = prefix_row + [None, ado_state] + tail_row
        ws_out.append(new_row)
        out_row = ws_out.max_row
        built_keys.add(row_identity(row[0], row[1], wid))
        if link:
            cell = ws_out.cell(row=out_row, column=link_col)
            cell.value = link_label(wid, ado)
            cell.hyperlink = link
            cell.font = link_font

    for key, preserved in preserved_by_key.items():
        if key in built_keys:
            continue
        preserved = list(preserved)
        link_idx = new_header.index("DevOps link")
        wid = extract_work_item_id(
            preserved[link_idx] if len(preserved) > link_idx else None
        )
        info = (ado.get(str(wid)) or ado.get(wid)) if wid else None
        # Align preserved row to new_header length
        while len(preserved) < len(new_header):
            preserved.append(None)
        type_idx = new_header.index("Work item type")
        preserved[type_idx] = work_item_type(
            info,
            wid,
            preserved[link_idx] if len(preserved) > link_idx else None,
        )
        if info:
            ado_idx = new_header.index("ADO Status")
            preserved[ado_idx] = info.get("state", "")
            if "Sprint" in new_header:
                preserved[new_header.index("Sprint")] = format_sprint(info)
            if "Tags" in new_header:
                preserved[new_header.index("Tags")] = format_tags(info)
        ws_out.append(preserved[: len(new_header)])
        out_row = ws_out.max_row
        if wid:
            cell = ws_out.cell(row=out_row, column=link_col)
            if not cell.hyperlink:
                cell.value = link_label(wid, ado)
                cell.hyperlink = ADO_BASE.format(id=wid)
                cell.font = link_font
        built_keys.add(key)

    # Empty Done_Resolved sheet like source
    ws_done = wb_out.create_sheet("Done_Resolved")
    if "Done_Resolved" in load_workbook(src, read_only=True).sheetnames:
        wb_in2 = load_workbook(src, read_only=True, data_only=True)
        for r in wb_in2["Done_Resolved"].iter_rows(values_only=True):
            ws_done.append(list(r))
        wb_in2.close()

    wb_out.save(OUTPUT)
    print(f"Wrote {OUTPUT}")
    print(f"Rows: {ws_out.max_row - 1}")


def main() -> int:
    if not ADO_CACHE.is_file():
        print(f"Missing ADO cache: {ADO_CACHE}", file=sys.stderr)
        return 1
    ado = json.loads(ADO_CACHE.read_text(encoding="utf-8"))

    sheet_ids: set[int] = set()
    src = load_source(SOURCE)
    wb_in = load_workbook(src, read_only=True, data_only=True)
    rows_in = list(wb_in["In progress"].iter_rows(values_only=True))
    wb_in.close()
    sheet_ids |= collect_ids_from_sheet(rows_in)
    if OUTPUT.is_file():
        try:
            wb_out = load_workbook(OUTPUT, read_only=True, data_only=True)
            sheet_ids |= collect_ids_from_sheet(
                list(wb_out["In progress"].iter_rows(values_only=True))
            )
            wb_out.close()
        except PermissionError:
            pass
    missing = missing_cache_entries(sheet_ids, ado)
    if missing:
        print(
            "ADO cache is missing work items referenced in the sheet:",
            ", ".join(str(i) for i in missing),
            file=sys.stderr,
        )
        print(
            f"Add them to {ADO_CACHE.name} (fetch via Azure DevOps) and re-run.",
            file=sys.stderr,
        )
        return 1

    build(ado)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
