#!/usr/bin/env python3
"""Generate Nationalbanken Intern Revision Flow checklist + process model JSON exports."""

from __future__ import annotations

import argparse
import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MANUSCRIPTS = REPO_ROOT / "projects" / "process-platform" / "flow" / "manuscripts" / "Demo setup"

PM_SOURCE = MANUSCRIPTS / "Behandle ansøgning m. klageret (Danish).json"
CL_SOURCE = MANUSCRIPTS / "Tjekliste for ansøgningsbehandling med klageret (Danish).json"
SPEC_SOURCE = Path(r"C:\Users\MortenJensen\Downloads\public-360-flow-internal-revision-spec.md")

OUT_DIR = REPO_ROOT / "outputs" / "customer-meetings" / "nationalbanken-intern-revision"
DOWNLOADS = Path(r"C:\Users\MortenJensen\Downloads")

PROCESS_TITLE = "Intern revision — godkendelse af dokument"
STAGE2_TITLE = "Ny godkendelsescyklus (re-godkendelse)"
CHECKLIST_NAME = "Tjekliste for intern revision (Nationalbanken demo)"
CHECKLIST_FILENAME = "Tjekliste_for_intern_revision_Nationalbanken.json"
PM_FILENAME = "Intern revision godkendelse af dokument (Nationalbanken demo).json"

KNOWN_KLAGERET_CHECKLIST_UID = "9d82684e-cf2e-4eba-a37a-182b9d914d6c"
KNOWN_SSI_CHECKLIST_UID = "7e4a2b91-8c3d-4f5e-a6b1-2d9e8f0c4a73"

WU_DOCUMENT_REVIEW_APPROVAL = "89e0ed8c-7391-4202-9f4d-d9d2d631c37a"
WU_FOLLOWUP_MILESTONES = "E1A5B6C7-D8F9-4012-9E3F-4B6C8D0A2E4F"
WU_INTERN_REVISION_TEST = "0176cc78-602a-4271-b521-f2e4df5d046a"

UUID_RE = re.compile(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.I
)
# Opening tag: allow `>` inside quoted attribute values (e.g. comment="(true/false)").
_WU_OPEN_TAG = r'(?:[^>"\']|"[^"]*")*'


def patch_wu_arguments(
    xml: str, updates: dict[str, str], *, optional: set[str] | None = None
) -> str:
    if not xml or not updates:
        return xml
    optional = optional or set()
    for name, value in updates.items():
        pat = re.compile(
            rf'(<argument\b{_WU_OPEN_TAG}\sname="{re.escape(name)}"{_WU_OPEN_TAG}>)([^<]*)(</argument>)',
            re.I,
        )
        xml, n = pat.subn(rf"\1{value}\3", xml, count=1)
        if n != 1 and name not in optional:
            raise ValueError(f"Expected exactly one <argument name=\"{name}\">; patched {n}")
    return xml


TEXT_REPLACEMENTS = [
    ("Behandle ansøgning m. klageret", PROCESS_TITLE),
    ("Klagebehandling", STAGE2_TITLE),
    ("Ansøgning modtaget", "Start intern revision"),
    ("Kontroller ansøgning", "Parallel kvalitetssikring (gennemgang)"),
    (
        "Anmodning om supplerende dokumentation - Væsentlig mangel",
        "Afvent — ikke anvendt (intern revision)",
    ),
    (
        "Automatisk bekræftelse af modtaget ansøgning",
        "Start godkendelse efter gennemgang (fase 1 — initiator)",
    ),
    ("Afgørelse truffet", "Formel godkendelse"),
    ("Afslut sagsbehandling", "Godkendt PDF og afslut workflow"),
    ("Skriv brev - Ansøgning modtaget", "Registrer kildedokument og deltagere"),
    ("Skriv brev - Afgørelse", "Formel godkendelse af kildedokument"),
    ("Registrer/opdater dato for modtaget ansøgning", "Registrer kildeversion ved workflow-start"),
]


def new_uid() -> str:
    return str(uuid.uuid4())


def blocked_checklist_uids() -> set[str]:
    blocked = {
        KNOWN_KLAGERET_CHECKLIST_UID.lower(),
        KNOWN_SSI_CHECKLIST_UID.lower(),
    }
    if CL_SOURCE.is_file():
        try:
            src = json.loads(CL_SOURCE.read_text(encoding="utf-8"))
            if src.get("UID"):
                blocked.add(str(src["UID"]).lower())
        except json.JSONDecodeError:
            pass
    return blocked


UID_FILE = OUT_DIR / "INTERN_REVISION_CHECKLIST_UID.txt"
CHECKLIST_RECNO_FILE = OUT_DIR / "INTERN_REVISION_CHECKLIST_DEFINITION_RECNO.txt"


def read_checklist_definition_recno(cli_override: int | None = None) -> int | None:
    if cli_override is not None:
        return cli_override
    if not CHECKLIST_RECNO_FILE.is_file():
        return None
    for line in CHECKLIST_RECNO_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        return int(line)
    return None


def assert_uid_not_blocked(uid: str) -> str:
    uid = uid.strip().upper()
    if uid.lower() in blocked_checklist_uids():
        raise SystemExit(
            f"Refusing blocked/template checklist UID: {uid}\n"
            "Det ville overskrive klageret- eller SSI-demo-tjeklisten ved import.\n"
            f"Brug den dedikerede UID i {UID_FILE.name}."
        )
    return uid


def checklist_uid(*, force_new: bool = False) -> str:
    blocked = blocked_checklist_uids()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if force_new:
        uid = str(uuid.uuid4()).upper()
        while uid.lower() in blocked:
            uid = str(uuid.uuid4()).upper()
        UID_FILE.write_text(uid + "\n", encoding="utf-8")
        return uid

    if UID_FILE.is_file():
        return assert_uid_not_blocked(UID_FILE.read_text(encoding="utf-8"))

    uid = str(uuid.uuid4()).upper()
    while uid.lower() in blocked:
        uid = str(uuid.uuid4()).upper()
    UID_FILE.write_text(uid + "\n", encoding="utf-8")
    return uid


def finalize_checklist_for_import(
    checklist: dict,
    *,
    uid: str,
    generated_at: str,
) -> None:
    checklist.pop("Recno", None)
    checklist["UID"] = assert_uid_not_blocked(uid)
    checklist["ToModifiedBy"] = None

    base_desc = checklist.get("Description") or ""
    if "Genereret" not in base_desc:
        checklist["Description"] = (
            f"{base_desc} Nationalbanken intern revision (fase 1 semi-manuel). "
            f"Sidst genereret {generated_at}."
        ).strip()


def apply_text_replacements(text: str) -> str:
    for old, new in TEXT_REPLACEMENTS:
        text = text.replace(old, new)
    return text


def sync_workunit_id(xml: str, wu_id: str) -> str:
    if not xml:
        return xml

    def repl(m: re.Match[str]) -> str:
        return f'{m.group(1)}{wu_id}{m.group(2)}'

    return re.sub(
        r'(<workUnit id=")[^"]+(")',
        repl,
        xml,
        count=1,
        flags=re.I,
    )


def find_stage_process_xml(pm: dict, display_name: str) -> str | None:
    for stage in pm.get("ProcessModelData", {}).get("StageConfigs", []):
        for sp in stage.get("StageProcessConfigs", []):
            if sp.get("Properties", {}).get("DisplayName") == display_name:
                return sp.get("Properties", {}).get("WorkunitArguments")
    return None


def apply_title_replacements_to_pm(pm: dict) -> None:
    """Rename visible labels only — never stringify-replace inside WorkunitArguments."""

    def walk_titles(obj):
        if isinstance(obj, dict):
            for key in ("Title", "DisplayName", "Description", "AdminNotes"):
                if key in obj and isinstance(obj[key], str):
                    obj[key] = apply_text_replacements(obj[key])
            for v in obj.values():
                walk_titles(v)
        elif isinstance(obj, list):
            for item in obj:
                walk_titles(item)

    walk_titles(pm)
    pm["Title"] = apply_text_replacements(pm.get("Title") or PROCESS_TITLE)


def checkpoint(
    cid: str,
    name: str,
    *,
    sort_id: int,
    index: int,
    milestone: int | None = None,
    description: str | None = None,
    answer_option: int = 1,
    outcome: dict | None = None,
) -> dict:
    return {
        "Recno": None,
        "CheckpointId": cid,
        "Name": name,
        "Description": description,
        "MilestoneType": milestone,
        "Theme": None,
        "CheckpointAnswerOption": answer_option,
        "Outcome": outcome,
        "Links": [],
        "SortId": sort_id,
        "Rule": None,
        "IsSubitem": None,
        "HasSubItems": None,
        "Index": index,
        "ParentIndex": None,
        "ToChecklistInstance": None,
        "ChecklistSubitems": [],
    }


def build_checklist(*, force_new_uid: bool = False) -> dict:
    template = json.loads(CL_SOURCE.read_text(encoding="utf-8"))
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    cl_uid = checklist_uid(force_new=force_new_uid)

    version_mismatch_outcome = {
        "OutcomeValue": 2,
        "OutcomeType": 6,
        "OutcomeText": {
            "ContentType": "Text",
            "Title": "Kildeversion afviger",
            "Description": "Kontrolleret version matcher ikke workflow — genstart eller eskalér.",
            "TitleNewNorwegian": None,
            "DescriptionNewNorwegian": None,
        },
    }

    points = [
        checkpoint(
            "1",
            "Kildedokument er valgt og workflow er startet",
            sort_id=1,
            index=0,
            milestone=99001,
            description="FR-001: kildeversion registreres ved start.",
        ),
        checkpoint(
            "2",
            "Mindst én reviewer og præcis én approver er valgt",
            sort_id=2,
            index=1,
            milestone=99001,
        ),
        checkpoint(
            "3",
            "Kildeversion under gennemgang er identificeret (FR-003)",
            sort_id=3,
            index=2,
            milestone=99001,
            outcome=version_mismatch_outcome,
        ),
        checkpoint(
            "4",
            "Parallel gennemgang: alle review-opgaver afsluttet (FR-002, FR-005)",
            sort_id=4,
            index=3,
            milestone=99003,
        ),
        checkpoint(
            "5",
            "Initiator har manuelt startet godkendelsesfasen (fase 1)",
            sort_id=5,
            index=4,
            milestone=99003,
            description="FR-005 fase 1: notifikation + manuel overgang.",
        ),
        checkpoint(
            "6",
            "Formel godkendelse gennemført (godkendt eller afvist)",
            sort_id=6,
            index=5,
            milestone=217,
        ),
        checkpoint(
            "7",
            "Ved afvisning: ingen godkendt PDF genereret (FR-008)",
            sort_id=7,
            index=6,
            milestone=217,
            answer_option=2,
        ),
        checkpoint(
            "8",
            "Ved godkendelse: initiator har startet PDF-konvertering (fase 1)",
            sort_id=8,
            index=7,
            milestone=217,
        ),
        checkpoint(
            "9",
            "PDF konverteret fra godkendt kildeversion (FR-009)",
            sort_id=9,
            index=8,
            milestone=217,
        ),
        checkpoint(
            "10",
            "Godkendelsesmetadata stemplet på PDF (FR-010)",
            sort_id=10,
            index=9,
            milestone=217,
        ),
        checkpoint(
            "11",
            "Godkendt PDF gemt og linket; kildedokument bevaret (FR-011, FR-012)",
            sort_id=11,
            index=10,
            milestone=218,
        ),
        checkpoint(
            "12",
            "Audit trail og workflow-status = Completed (FR-013)",
            sort_id=12,
            index=11,
            milestone=218,
        ),
        checkpoint(
            "13",
            "Tidligere godkendte PDF'er bevares ved re-godkendelse (FR-014)",
            sort_id=13,
            index=12,
            milestone=218,
            answer_option=2,
        ),
    ]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.00")
    checklist = {
        "Name": CHECKLIST_NAME,
        "Description": "Demo — intern revision med gennemgang, godkendelse og godkendt PDF.",
        "FromDate": None,
        "ToDate": None,
        "IsAllCaseType": template.get("IsAllCaseType", -1),
        "ToCaseType": template.get("ToCaseType"),
        "DiBKServiceUrlFragment": None,
        "ToChecklistScope": template.get("ToChecklistScope", 2),
        "ToApplicationType": template.get("ToApplicationType", -99999991),
        "IsLocked": template.get("IsLocked", -99999991),
        "IsUsedByProject": template.get("IsUsedByProject", -99999991),
        "ModifiedDate": now,
        "CheckPoints": points,
    }
    finalize_checklist_for_import(checklist, uid=cl_uid, generated_at=generated_at)
    return checklist


def collect_workunit_ids(obj) -> set[str]:
    ids: set[str] = set()

    def walk(o):
        if isinstance(o, dict):
            wu = o.get("WorkunitId")
            if isinstance(wu, str):
                ids.add(wu.lower())
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for i in o:
                walk(i)

    walk(obj)
    return ids


def collect_remap_uuids(obj) -> set[str]:
    keys = {
        "UID",
        "BaseUID",
        "AutomationID",
        "TriggerStageConfigUid",
        "TriggerStageProcessConfigUid",
        "TemplateUID",
        "TemplateBaseUID",
        "ProgressplanTemplateUid",
    }
    found: set[str] = set()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in keys and isinstance(v, str) and UUID_RE.fullmatch(v):
                    found.add(v.lower())
                walk(v)
        elif isinstance(o, list):
            for i in o:
                walk(i)

    walk(obj)
    return found


def remap_uuids_in_string(s: str, mapping: dict[str, str]) -> str:
    def repl(m):
        key = m.group(0).lower()
        return mapping.get(key, m.group(0))

    return UUID_RE.sub(repl, s)


def null_recnos(obj, *, inside_case_types: bool = False) -> None:
    if isinstance(obj, dict):
        for key, value in obj.items():
            child_in_case_types = inside_case_types or key == "CaseTypes"
            if key == "Recno" and not inside_case_types and obj["Recno"] is not None:
                obj["Recno"] = None
            else:
                null_recnos(value, inside_case_types=child_in_case_types)
    elif isinstance(obj, list):
        for item in obj:
            null_recnos(item, inside_case_types=inside_case_types)


def configure_stage1_processes(stage: dict, *, pm: dict) -> None:
    """Map klageret stage processes to intern revision phase 1 (semi-manual)."""
    approval_wu_xml = find_stage_process_xml(pm, "Afgørelse truffet") or ""
    followup_wu_xml = find_stage_process_xml(pm, "Ansøgning modtaget") or ""

    for sp in stage.get("StageProcessConfigs", []):
        props = sp.get("Properties", {})
        title = props.get("DisplayName") or ""

        if title == "Anmodning om supplerende dokumentation - Væsentlig mangel":
            sp["MarkedForRemoval"] = True
            continue

        if title == "Ansøgning modtaget":
            props["AutoGenerate"] = True
            props["AutoExecute"] = False
            props["AllowManualAdd"] = True
            props["WorkunitId"] = WU_FOLLOWUP_MILESTONES
            xml = sync_workunit_id(props.get("WorkunitArguments") or "", WU_FOLLOWUP_MILESTONES)
            props["WorkunitArguments"] = patch_wu_arguments(
                xml,
                {
                    "ShowDocumentDialogue1": "true",
                    "CreateReview1": "false",
                    "CreateApproval1": "false",
                    "CreateDispatch1": "true",
                    "DocumentActivityTitle1": "Registrer kildedokument og deltagere",
                    "DocumentTitle1": "Kildedokument intern revision",
                },
            )

        elif title == "Kontroller ansøgning":
            props["AutoGenerate"] = True
            props["AutoExecute"] = False
            props["WorkunitId"] = WU_DOCUMENT_REVIEW_APPROVAL
            xml = sync_workunit_id(approval_wu_xml, WU_DOCUMENT_REVIEW_APPROVAL)
            props["WorkunitArguments"] = patch_wu_arguments(
                xml,
                {
                    "ShowDocumentDialogue1": "false",
                    "CreateReview1": "true",
                    "CreateApproval1": "false",
                    "CreateDispatch1": "false",
                    "DocumentActivityTitle1": "Parallel kvalitetssikring (gennemgang)",
                },
            )

        elif title == "Automatisk bekræftelse af modtaget ansøgning":
            props["AutoGenerate"] = False
            props["AutoExecute"] = False
            props["AllowManualAdd"] = True
            props["WorkunitId"] = WU_FOLLOWUP_MILESTONES
            xml = sync_workunit_id(followup_wu_xml, WU_FOLLOWUP_MILESTONES)
            props["WorkunitArguments"] = patch_wu_arguments(
                xml,
                {
                    "ShowCheckpointDialogue1": "false",
                    "ShowMilestoneDialogue1": "true",
                    "MilestoneActivityTitle1": "Gennemgang afsluttet — start godkendelse",
                    "ShowDocumentDialogue1": "false",
                    "ShowEmailDialogue1": "false",
                    "CreateDispatch1": "false",
                },
            )

        elif title == "Afgørelse truffet":
            props["AutoGenerate"] = False
            props["AutoExecute"] = False
            props["AllowManualAdd"] = True
            props["WorkunitId"] = WU_DOCUMENT_REVIEW_APPROVAL
            xml = sync_workunit_id(approval_wu_xml, WU_DOCUMENT_REVIEW_APPROVAL)
            props["WorkunitArguments"] = patch_wu_arguments(
                xml,
                {
                    "ShowDocumentDialogue1": "false",
                    "CreateReview1": "false",
                    "CreateApproval1": "true",
                    "CreateDispatch1": "false",
                    "DocumentActivityTitle1": "Formel godkendelse",
                },
            )

        elif title == "Afslut sagsbehandling":
            props["AutoGenerate"] = False
            props["AutoExecute"] = False
            props["AllowManualAdd"] = True
            props["WorkunitId"] = WU_DOCUMENT_REVIEW_APPROVAL
            xml = sync_workunit_id(approval_wu_xml, WU_DOCUMENT_REVIEW_APPROVAL)
            props["WorkunitArguments"] = patch_wu_arguments(
                xml,
                {
                    "ShowDocumentDialogue1": "true",
                    "CreateReview1": "false",
                    "CreateApproval1": "false",
                    "CreateDispatch1": "false",
                    "DocumentActivityTitle1": "Konverter, stemple og gem godkendt PDF",
                    "DocumentTitle1": "Godkendt PDF",
                },
            )


def build_process_model(
    checklist_uid: str, *, checklist_definition_recno: int | None = None
) -> dict:
    pm = json.loads(PM_SOURCE.read_text(encoding="utf-8"))
    pm = json.loads(json.dumps(pm))

    workunit_ids = collect_workunit_ids(pm)
    to_remap = collect_remap_uuids(pm) - workunit_ids
    uid_map = {old: new_uid() for old in to_remap}

    raw = json.dumps(pm, ensure_ascii=False)
    raw = remap_uuids_in_string(raw, uid_map)
    pm = json.loads(raw)

    pm["Title"] = PROCESS_TITLE
    pm["Recno"] = None
    pm["Version"] = 1
    pm["UID"] = new_uid()
    pm["BaseUID"] = new_uid()
    pm["FromDate"] = None
    pm["ToDate"] = None
    pm["IsDataChanged"] = True
    pm["IsUnsavedItem"] = False
    pm["TemplateState"] = 0
    pm["CreatedDate"] = {
        "Year": 2026,
        "Month": 9,
        "Day": 30,
        "Hour": 10,
        "Minute": 0,
        "Second": 0,
        "Millisecond": 0,
    }

    pmd = pm["ProcessModelData"]
    pmd["Recno"] = None
    pmd["UID"] = pm["UID"]
    pmd["Versions"] = []

    props = pmd["Properties"]
    props["Title"] = PROCESS_TITLE
    props["VersionNumber"] = 1
    props["AdminNotes"] = (
        "Nationalbanken demo — intern revision (spec v1.0, fase 1 semi-manuel). "
        f"Tjekliste UID: {checklist_uid}. "
        f"Test-workunit Intern revision (core-bl): {WU_INTERN_REVISION_TEST}. "
        "Open decisions: PDF-lagring, stempel-layout, kilde-låsning."
    )
    props["BaseUID"] = pm["BaseUID"]

    for stage in pmd["StageConfigs"]:
        st_props = stage["Properties"]
        if st_props.get("SortId") == 1:
            st_props["Title"] = PROCESS_TITLE
            st_props["CalculationDays"] = 21
            if checklist_definition_recno is not None:
                st_props["ChecklistDefinition"] = checklist_definition_recno
                st_props["ChecklistDefinitionDesc"] = CHECKLIST_NAME
            else:
                st_props["ChecklistDefinition"] = None
                st_props["ChecklistDefinitionDesc"] = CHECKLIST_NAME
            configure_stage1_processes(stage, pm=pm)

        if st_props.get("SortId") == 2:
            st_props["Title"] = STAGE2_TITLE
            st_props["CalculationDays"] = 14
            st_props["AutoGenerate"] = False

        for ms in stage.get("StageMileStoneConfigs", []):
            if ms.get("Properties", {}).get("Title") == "Klagefrist":
                ms["MarkedForRemoval"] = True

        if st_props.get("SortId") == 2:
            for sp in stage.get("StageProcessConfigs", []):
                sp["Properties"]["DisplayName"] = "Start ny godkendelsescyklus"

    apply_title_replacements_to_pm(pm)
    pm["Title"] = PROCESS_TITLE
    pmd["Properties"]["Title"] = PROCESS_TITLE

    null_recnos(pm)
    return pm


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Intern Revision Flow checklist + process model JSON."
    )
    parser.add_argument(
        "--new-checklist-identity",
        action="store_true",
        help=f"Tildel ny stabil UID (skriver {UID_FILE.name}).",
    )
    parser.add_argument(
        "--checklist-definition-recno",
        type=int,
        metavar="RECNO",
        help=(
            "Recno for importeret tjekliste — sættes på fase 1. "
            f"Alternativt: {CHECKLIST_RECNO_FILE.name}"
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if SPEC_SOURCE.is_file():
        spec_dest = OUT_DIR / SPEC_SOURCE.name
        if not spec_dest.exists() or spec_dest.read_bytes() != SPEC_SOURCE.read_bytes():
            spec_dest.write_text(SPEC_SOURCE.read_text(encoding="utf-8"), encoding="utf-8")

    checklist = build_checklist(force_new_uid=args.new_checklist_identity)
    cld_recno = read_checklist_definition_recno(args.checklist_definition_recno)
    process = build_process_model(checklist["UID"], checklist_definition_recno=cld_recno)

    cl_path = OUT_DIR / CHECKLIST_FILENAME
    pm_path = OUT_DIR / PM_FILENAME
    cl_path.write_text(json.dumps(checklist, ensure_ascii=False, indent=2), encoding="utf-8")
    pm_path.write_text(json.dumps(process, ensure_ascii=False, indent=2), encoding="utf-8")

    if DOWNLOADS.is_dir():
        (DOWNLOADS / CHECKLIST_FILENAME).write_text(
            cl_path.read_text(encoding="utf-8"), encoding="utf-8"
        )
        (DOWNLOADS / PM_FILENAME).write_text(pm_path.read_text(encoding="utf-8"), encoding="utf-8")
        (DOWNLOADS / UID_FILE.name).write_text(checklist["UID"] + "\n", encoding="utf-8")
        if SPEC_SOURCE.is_file():
            (DOWNLOADS / SPEC_SOURCE.name).write_text(
                SPEC_SOURCE.read_text(encoding="utf-8"), encoding="utf-8"
            )

    readme = OUT_DIR / "README-import.txt"
    readme.write_text(
        f"""Intern revision Flow demo — import i tenant (Nationalbanken)
============================================================

Tjekliste — stabil UID
----------------------
Import matcher på UID. Export bruger UID fra {UID_FILE.name}
(nuværende: {checklist['UID']}) — adskilt fra klageret ({KNOWN_KLAGERET_CHECKLIST_UID})
og SSI-demo ({KNOWN_SSI_CHECKLIST_UID}).

Spec: {SPEC_SOURCE.name} (kopi i denne mappe).

Fase 1 (semi-manuel) i procesmodellen
--------------------------------------
1. Start intern revision — kildedokument og deltagere
2. Parallel kvalitetssikring — Document Flow Review (reviewers)
3. Initiator starter manuelt: Start godkendelse efter gennemgang
4. Formel godkendelse — Document Flow Approval (én approver)
5. Initiator starter manuelt: Konverter, stemple og gem godkendt PDF

Fase 2 (automatisk kæde) er bevidst ikke modelleret her — se spec §13.2.

Import
------
1. Importér tjekliste: {CHECKLIST_FILENAME}
2. Importér procesmodel: {PM_FILENAME}
3. Kobl tjekliste på fase 1:
   • Find Recno i admin efter tjekliste-import
   • Skriv Recno i {CHECKLIST_RECNO_FILE.name} ELLER --checklist-definition-recno
   • Regenerér og importér procesmodel igen, publicér
   • Opret ny sag til test

Helt ny tjekliste-identitet (sjældent):
  uv run python toolkit/scripts/build_intern_revision_flow_exports.py --new-checklist-identity
""",
        encoding="utf-8",
    )

    print(f"Checklist: {cl_path}")
    print(f"Process model: {pm_path}")
    print(f"Checklist UID (stable): {checklist['UID']}")
    print(f"UID source: {UID_FILE}")
    if cld_recno is not None:
        print(f"Process model fase 1 ChecklistDefinition Recno: {cld_recno}")
    else:
        print(
            "WARNING: ChecklistDefinition not set — "
            f"add Recno via {CHECKLIST_RECNO_FILE.name} and regenerate"
        )


if __name__ == "__main__":
    main()
