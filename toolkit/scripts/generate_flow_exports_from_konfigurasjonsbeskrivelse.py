#!/usr/bin/env python3
"""Generate 360° Flow process model + checklist JSON from consultant Excel (Konfigurasjonsbeskrivelse)."""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path

import openpyxl

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from fill_konfigurasjonsbeskrivelse_flow_demo import (  # noqa: E402
    CHECKPOINT_ANSWER_LABELS,
    CONCURRENCY_NO,
    DOC_CAT_NAMES,
    MILESTONE_LABEL_ALIASES,
    MILESTONE_STATUS_FROM_DESC,
    MILESTONE_STATUS_NO,
    PROCESS_STATUS_FROM_DESC,
    PROCESS_STATUS_NO,
    TIME_CALC,
    WU_TO_PROSESSDEF,
)

PROSESSDEF_TO_WU = {v: k for k, v in WU_TO_PROSESSDEF.items()}

REPO = Path(__file__).resolve().parents[2]
DEFAULT_PM = REPO / "projects/process-platform/flow/manuscripts/Demo setup/Behandle søknad m_klagerett.json"
DEFAULT_CL = (
    REPO
    / "projects/process-platform/flow/manuscripts/Demo setup/Sjekkliste_for_søknadsbehandling_med_klagerett_fcba25b7-4d74-49ba-92c0-a03909c51d02.json"
)

CONCURRENCY_REV = {v: k for k, v in CONCURRENCY_NO.items()}
MILESTONE_STATUS_REV = {**{v: k for k, v in MILESTONE_STATUS_NO.items()}, **MILESTONE_STATUS_FROM_DESC}
PROCESS_STATUS_REV = {**{v: k for k, v in PROCESS_STATUS_NO.items()}, **PROCESS_STATUS_FROM_DESC}
CHECKPOINT_ANSWER_REV = {v: k for k, v in CHECKPOINT_ANSWER_LABELS.items()}
TIME_CALC_REV = {v: k for k, v in TIME_CALC.items()}
DOC_CAT_REV = {v: k for k, v in DOC_CAT_NAMES.items()}
MILESTONE_LABEL_REV = {v: k for k, v in MILESTONE_LABEL_ALIASES.items()}


def _sheet(wb, name_prefix: str):
    for n in wb.sheetnames:
        if n.startswith(name_prefix):
            return wb[n]
    raise KeyError(f"No sheet starting with {name_prefix!r}")


def _cell(row: tuple, idx: int) -> object:
    return row[idx] if idx < len(row) else None


def _norm(s: object) -> str | None:
    if s is None:
        return None
    t = str(s).strip()
    return t or None


def _ja_nei(val: object) -> bool | None:
    t = _norm(val)
    if t is None:
        return None
    low = t.lower()
    if low == "ja":
        return True
    if low == "nei":
        return False
    return None


def _automation_key(aid: object) -> str | None:
    t = _norm(aid)
    if not t:
        return None
    return t.lower()


def milestone_lookup(pm: dict) -> dict[str, int]:
    out: dict[str, int] = {}
    for stage in pm["ProcessModelData"]["StageConfigs"]:
        for ms in stage.get("StageMileStoneConfigs") or []:
            p = ms.get("Properties") or {}
            recno = p.get("MilestoneTypeRecno")
            if recno is None:
                continue
            for label in (p.get("MilestoneTypeDesc"), p.get("Title")):
                if label:
                    clean = str(label).lstrip("*").strip()
                    out[clean] = int(recno)
    for alias, canonical in MILESTONE_LABEL_REV.items():
        if canonical in out and alias not in out:
            out[alias] = out[canonical]
    return out


def parse_doc_categories(text: object) -> list[int] | None:
    t = _norm(text)
    if not t:
        return None
    if "Tilleggsinformasjon - mindre mangel" in t and "vesentlig" in t:
        return [433, 434]
    recnos: list[int] = []
    for part in re.split(r",\s*", t):
        part = part.strip()
        if part in DOC_CAT_REV:
            r = DOC_CAT_REV[part]
            if r not in recnos:
                recnos.append(r)
    return recnos or None


def apply_process_model_from_excel(pm: dict, wb) -> None:
    ws_pm = wb["Prosessmodell"]
    title = _norm(ws_pm.cell(row=6, column=2).value)
    admin_notes = _norm(ws_pm.cell(row=6, column=4).value)
    if title:
        pm["Title"] = title
        props = pm["ProcessModelData"]["Properties"]
        props["Title"] = title
        if admin_notes:
            props["AdminNotes"] = admin_notes

    ms_label_to_recno = milestone_lookup(pm)

    ws_faser = wb["Saksbehandlingsfaser"]
    stages_by_title: dict[str, dict] = {
        (s.get("Properties") or {}).get("Title"): s
        for s in pm["ProcessModelData"]["StageConfigs"]
    }
    for row in ws_faser.iter_rows(min_row=6, values_only=True):
        stage_title = _norm(row[2])
        if not stage_title or stage_title not in stages_by_title:
            continue
        stage = stages_by_title[stage_title]
        sp = stage["Properties"]
        if row[4] is not None:
            sp["Description"] = _norm(row[4])
        if row[5] is not None:
            sp["AdminNotes"] = _norm(row[5])
        if row[6] is not None:
            sp["CalculationDays"] = int(row[6])
        if row[7] is not None:
            sp["SortId"] = int(row[7])
        if row[8]:
            sp["AutomationID"] = str(row[8]).strip()
        conc = CONCURRENCY_REV.get(_norm(row[9]) or "")
        if conc is not None:
            sp["Concurrency"] = conc
        for col, key in ((13, "InitiateAsPlannedUpcoming"), (14, "AllowManualAdd"), (15, "AutoGenerate")):
            flag = _ja_nei(row[col - 1])
            if flag is not None:
                sp[key] = flag

    ws_ms = _sheet(wb, "Milep")
    ms_by_aid: dict[str, dict] = {}
    for stage in pm["ProcessModelData"]["StageConfigs"]:
        for ms in stage.get("StageMileStoneConfigs") or []:
            p = ms.get("Properties") or {}
            key = _automation_key(p.get("AutomationID"))
            if key:
                ms_by_aid[key] = ms

    for row in ws_ms.iter_rows(min_row=6, values_only=True):
        aid = _automation_key(row[9])
        if not aid:
            continue
        ms = ms_by_aid.get(aid)
        if not ms:
            continue
        p = ms["Properties"]
        if row[3]:
            p["MilestoneTypeDesc"] = str(row[3]).lstrip("*").strip()
        if row[4]:
            p["Title"] = _norm(row[4])
        if row[5] is not None:
            p["Description"] = _norm(row[5])
        if row[6] is not None:
            p["AdminNotes"] = _norm(row[6])
        if row[7] is not None:
            p["CalculationDays"] = int(row[7])
        if row[8] is not None:
            p["SortId"] = int(row[8])
        status_label = _norm(row[10])
        if status_label and status_label in MILESTONE_STATUS_REV:
            p["MilestoneStatusRecno"] = MILESTONE_STATUS_REV[status_label]
        conc = CONCURRENCY_REV.get(_norm(row[11]) or "")
        if conc is not None:
            p["Concurrency"] = conc
        cats = parse_doc_categories(row[12])
        if cats is not None:
            p["DocumentCategoryRecnos"] = cats
        for col, key in (
            (14, "IsGlobal"),
            (15, "AutoGenerate"),
            (16, "ShouldRecalculate"),
            (17, "IsStartMilestone"),
            (18, "AllowManualAdd"),
        ):
            flag = _ja_nei(row[col - 1])
            if flag is not None:
                p[key] = flag
        tc = TIME_CALC_REV.get(_norm(row[18]) or "")
        if tc is not None:
            p["TimeCalculationBehaviorString"] = str(tc)

    ws_proc = wb["Prosesser"]
    proc_by_stage_wu: dict[tuple[str, str], dict] = {}
    proc_by_stage_aid: dict[tuple[str, str], dict] = {}
    proc_by_stage_sort: dict[tuple[str, int], dict] = {}
    for stage in pm["ProcessModelData"]["StageConfigs"]:
        stage_title = (stage.get("Properties") or {}).get("Title") or ""
        for proc in stage.get("StageProcessConfigs") or []:
            p = proc.get("Properties") or {}
            wu = (p.get("WorkunitId") or "").upper()
            if wu:
                proc_by_stage_wu[(stage_title, wu)] = proc
            aid = _automation_key(p.get("AutomationID"))
            if aid:
                proc_by_stage_aid[(stage_title, aid)] = proc
            sort_id = p.get("SortId")
            if sort_id is not None:
                proc_by_stage_sort[(stage_title, int(sort_id))] = proc

    for row in ws_proc.iter_rows(min_row=6, values_only=True):
        stage_title = _norm(row[2])
        if not stage_title:
            continue
        pdef = _norm(row[5])
        wu = PROSESSDEF_TO_WU.get(pdef or "")
        proc = None
        if wu:
            proc = proc_by_stage_wu.get((stage_title, wu.upper()))
        if proc is None:
            aid = _automation_key(row[12])
            if aid:
                proc = proc_by_stage_aid.get((stage_title, aid))
        if proc is None and row[11] is not None:
            proc = proc_by_stage_sort.get((stage_title, int(row[11])))
        if not proc:
            continue
        p = proc["Properties"]
        display = _norm(row[3])
        if display:
            p["DisplayName"] = display
        if row[7] is not None:
            p["Description"] = _norm(row[7])
        if row[8] is not None:
            p["AdminNotes"] = _norm(row[8])
        conc = CONCURRENCY_REV.get(_norm(row[9]) or "")
        if conc is not None:
            p["Concurrency"] = conc
        target = _norm(row[10])
        if target:
            p["TargetMilestoneTypeDescription"] = target
            recno = ms_label_to_recno.get(target)
            if recno is not None:
                p["TargetMilestoneTypeRecno"] = recno
        if row[11] is not None:
            p["SortId"] = int(row[11])
        status_label = _norm(row[6])
        if status_label and status_label in PROCESS_STATUS_REV:
            p["ProcessStatusRecno"] = PROCESS_STATUS_REV[status_label]
            p["ProcessStatusDescription"] = {
                "Planlagt": "Planned",
                "Aktiv": "Active",
                "Avsluttet": "Closed",
            }.get(status_label, p.get("ProcessStatusDescription"))
        for col, key in (
            (14, "ShowAsUpcomingProcess"),
            (15, "AllowManualAdd"),
            (16, "AutoGenerate"),
            (17, "ShowActivePassiveButton"),
            (18, "ShowClosePhaseButton"),
        ):
            flag = _ja_nei(row[col - 1])
            if flag is not None:
                p[key] = flag
        cancel = _ja_nei(row[20])
        if cancel is not None:
            p["PreventProcessCancellation"] = cancel


def find_duplicate_process_display_names(pm: dict) -> list[tuple[str, str, int]]:
    """Return (stage_title, display_name, count) for duplicates within a phase."""
    dupes: list[tuple[str, str, int]] = []
    for stage in pm["ProcessModelData"]["StageConfigs"]:
        stage_title = (stage.get("Properties") or {}).get("Title") or ""
        names: dict[str, int] = {}
        for proc in stage.get("StageProcessConfigs") or []:
            name = (proc.get("Properties") or {}).get("DisplayName")
            if not name:
                continue
            names[name] = names.get(name, 0) + 1
        for name, count in names.items():
            if count > 1:
                dupes.append((stage_title, name, count))
    return dupes


def _iter_checkpoints(checkpoints: list) -> list[dict]:
    out: list[dict] = []
    for cp in checkpoints:
        out.append(cp)
        out.extend(_iter_checkpoints(cp.get("ChecklistSubitems") or []))
    return out


def apply_checklist_from_excel(cl: dict, wb, pm: dict) -> None:
    ms_label_to_recno = milestone_lookup(pm)
    ws = wb["Sjekklister"]
    header_name = _norm(ws.cell(row=6, column=2).value)
    if header_name:
        cl["Name"] = header_name

    excel_rows: dict[str, tuple] = {}
    for row in ws.iter_rows(min_row=7, values_only=True):
        cp_id = _cell(row, 5)
        if cp_id is None:
            continue
        excel_rows[str(cp_id).strip()] = row

    all_cps = _iter_checkpoints(cl.get("CheckPoints") or [])
    by_id = {str(c["CheckpointId"]): c for c in all_cps}

    for cp_id, row in excel_rows.items():
        cp = by_id.get(cp_id)
        if not cp:
            continue
        name = _norm(_cell(row, 6))
        if name:
            cp["Name"] = name
        cp["Description"] = _norm(_cell(row, 8))
        mt_label = _norm(_cell(row, 9))
        if mt_label:
            recno = ms_label_to_recno.get(mt_label)
            if recno is not None:
                cp["MilestoneType"] = recno
            else:
                cp["MilestoneType"] = None
        # Excel col 12 is "Utfall - Respons" (Ja/Nei), not Theme — import requires int|null for Theme.
        ans = CHECKPOINT_ANSWER_REV.get(_norm(_cell(row, 10)) or "")
        if ans:
            cp["CheckpointAnswerOption"] = ans

        # Cols 13–15: Utfallstype, Tittel utfall, Beskrivelse utfall (0-based indices 12–14)
        outcome_title = _norm(_cell(row, 13))
        outcome_desc = _norm(_cell(row, 14))
        outcome_type_label = _norm(_cell(row, 12))
        if outcome_title or outcome_desc or outcome_type_label:
            outcome = cp.get("Outcome") or {
                "OutcomeValue": 2,
                "OutcomeType": 16,
                "OutcomeText": {
                    "ContentType": "Text",
                    "Title": None,
                    "Description": None,
                    "TitleNewNorwegian": None,
                    "DescriptionNewNorwegian": None,
                },
            }
            ot = outcome.get("OutcomeText") or {}
            if outcome_title:
                ot["Title"] = outcome_title
            if outcome_desc:
                ot["Description"] = outcome_desc
            outcome["OutcomeText"] = ot
            cp["Outcome"] = outcome


def generate(
    xlsx_path: Path,
    *,
    template_pm: Path,
    template_cl: Path,
) -> tuple[dict, dict]:
    pm = copy.deepcopy(json.loads(template_pm.read_text(encoding="utf-8")))
    cl = copy.deepcopy(json.loads(template_cl.read_text(encoding="utf-8")))
    wb = openpyxl.load_workbook(xlsx_path, data_only=True)
    apply_process_model_from_excel(pm, wb)
    apply_checklist_from_excel(cl, wb, pm)
    wb.close()
    dupes = find_duplicate_process_display_names(pm)
    if dupes:
        lines = ", ".join(f"{st!r}: {name!r} (×{n})" for st, name, n in dupes)
        raise SystemExit(
            "Duplicate process DisplayName within a phase (import/save will fail): "
            f"{lines}. Fix Excel or template matching."
        )
    return pm, cl


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Flow process model + checklist JSON from Konfigurasjonsbeskrivelse Excel."
    )
    parser.add_argument("--input", type=Path, required=True, help="Path to .xlsx configuration workbook")
    parser.add_argument(
        "--template-process-model",
        type=Path,
        default=DEFAULT_PM,
        help="JSON export used as technical template (work units, recnos, argument XML)",
    )
    parser.add_argument(
        "--template-checklist",
        type=Path,
        default=DEFAULT_CL,
        help="Checklist JSON used as template for structure and outcome types",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=REPO / "outputs" / "flow" / "from-konfigurasjonsbeskrivelse",
        help="Directory for generated JSON files",
    )
    args = parser.parse_args()

    if not args.input.is_file():
        raise SystemExit(f"Input not found: {args.input}")
    if not args.template_process_model.is_file():
        raise SystemExit(f"Process model template not found: {args.template_process_model}")
    if not args.template_checklist.is_file():
        raise SystemExit(f"Checklist template not found: {args.template_checklist}")

    pm, cl = generate(
        args.input,
        template_pm=args.template_process_model,
        template_cl=args.template_checklist,
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)

    pm_name = pm.get("Title") or "process-model"
    safe_pm = re.sub(r'[<>:"/\\|?*]', "_", pm_name).replace("/", "_") + ".json"
    cl_name = cl.get("Name") or "checklist"
    safe_cl = re.sub(r'[<>:"/\\|?*]', "_", cl_name) + ".json"

    pm_path = args.output_dir / safe_pm
    cl_path = args.output_dir / safe_cl
    pm_path.write_text(json.dumps(pm, ensure_ascii=False, indent=2), encoding="utf-8")
    cl_path.write_text(json.dumps(cl, ensure_ascii=False, indent=2), encoding="utf-8")

    stages = pm["ProcessModelData"]["StageConfigs"]
    n_proc = sum(len(s.get("StageProcessConfigs") or []) for s in stages)
    n_ms = sum(len(s.get("StageMileStoneConfigs") or []) for s in stages)
    n_cp = len(_iter_checkpoints(cl.get("CheckPoints") or []))
    print(f"Wrote process model: {pm_path}")
    print(f"Wrote checklist:     {cl_path}")
    print(f"  Stages: {len(stages)}  Processes: {n_proc}  Milestones: {n_ms}  Checkpoints: {n_cp}")


if __name__ == "__main__":
    main()
