#!/usr/bin/env python3
"""Generate SSI markedsdialog Flow checklist + process model JSON exports."""

from __future__ import annotations

import argparse
import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

PM_SOURCE = Path(
    r"C:\Users\MortenJensen\Downloads\Behandle ansøgning m. klageret (v4).json"
)
CL_SOURCE = Path(
    r"C:\Users\MortenJensen\Downloads\Tjekliste_for_ansøgningsbehandling_med_klageret_7822ee6c-1fbe-4aca-a457-2c0f9740e34e.json"
)

OUT_DIR = Path(__file__).resolve().parents[2] / "outputs" / "customer-meetings" / "ssi-flow"
DOWNLOADS = Path(r"C:\Users\MortenJensen\Downloads")

PROCESS_TITLE = "Behandle rettighedsanmodning (PKU/destruktion)"
STAGE2_TITLE = "Efterfølgende destruktionsbekræftelse"
CHECKLIST_NAME = "Tjekliste for rettighedsanmodning (PKU/destruktion, barn under 15)"
CHECKLIST_FILENAME = "Tjekliste_for_rettighedsanmodning_PKU_destruktion.json"
PM_FILENAME = "Behandle rettighedsanmodning PKU destruktion (SSI demo).json"

# Import i Public 360° matcher eksisterende tjekliste på UID (ikke Recno i JSON).
# Samme UID → update → samme Recno i databasen (overskriver definitionen).
KNOWN_KLAGERET_CHECKLIST_UID = "9d82684e-cf2e-4eba-a37a-182b9d914d6c"

UUID_RE = re.compile(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.I
)

# Longer phrases first
TEXT_REPLACEMENTS = [
    ("Behandle ansøgning m. klageret", PROCESS_TITLE),
    ("Automatisk bekræftelse af modtaget ansøgning", "Automatisk kvittering for modtaget henvendelse"),
    (
        "Anmodning om supplerende dokumentation - Væsentlig mangel",
        "Afvent samtykke eller manglende oplysninger",
    ),
    (
        "Supplerende dokumentation anmodet - væsentlig mangel",
        "Samtykke/manglende oplysninger anmodet",
    ),
    (
        "Anmodning om supplerende dokumentation - Væsentlig mangel",
        "Anmodning om samtykke eller manglende oplysninger",
    ),
    ("Skriv brev - Væsentlig mangel", "Skriv brev - Anmodning om samtykke/manglende oplysninger"),
    ("Påmindelse - Væsentlig mangel", "Påmindelse - manglende samtykke/oplysninger"),
    ("Kontroller ansøgning", "Kontroller identitet og forældremyndighed"),
    (
        "Skriv e-mail - Indhent oplysninger - mindre mangel",
        "Skriv e-mail - Intern høring MS/PKU og destruktionsanmodning",
    ),
    (
        "Anmodning om supplerende dokumentation - Væsentlig mangel",
        "Afvent samtykke eller manglende oplysninger",
    ),
    ("Registrer/opdater dato for modtaget ansøgning", "Registrer modtagelsesdato for henvendelse"),
    ("Registrer dato - Ansøgning komplet", "Registrer dato - Sag oplyst"),
    ("Skriv brev - Ansøgning modtaget", "Skriv brev - Henvendelse modtaget"),
    ("Kvittering for ansøgning", "Kvittering for henvendelse"),
    ("Komplet ansøgning", "Sag oplyst (klar til afgørelse)"),
    ("Klagebehandling", STAGE2_TITLE),
    ("Skriv brev - Klage modtaget", "Skriv brev - Destruktionsbekræftelse registreret"),
    ("Klage modtaget", "Destruktionsbekræftelse modtaget"),
    ("Ansøgning modtaget", "Henvendelse modtaget"),
]


def new_uid() -> str:
    return str(uuid.uuid4())


def blocked_checklist_uids() -> set[str]:
    blocked = {KNOWN_KLAGERET_CHECKLIST_UID.lower()}
    if CL_SOURCE.is_file():
        try:
            src = json.loads(CL_SOURCE.read_text(encoding="utf-8"))
            if src.get("UID"):
                blocked.add(str(src["UID"]).lower())
        except json.JSONDecodeError:
            pass
    return blocked


SSI_UID_FILE = OUT_DIR / "SSI_CHECKLIST_UID.txt"
SSI_CHECKLIST_RECNO_FILE = OUT_DIR / "SSI_CHECKLIST_DEFINITION_RECNO.txt"


def read_checklist_definition_recno(cli_override: int | None = None) -> int | None:
    if cli_override is not None:
        return cli_override
    if not SSI_CHECKLIST_RECNO_FILE.is_file():
        return None
    for line in SSI_CHECKLIST_RECNO_FILE.read_text(encoding="utf-8").splitlines():
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
            "Det ville overskrive klageret-demo-tjeklisten ved import.\n"
            f"Brug den dedikerede SSI-UID i {SSI_UID_FILE.name}."
        )
    return uid


def ssi_checklist_uid(*, force_new: bool = False) -> str:
    """
    Stabil UID for SSI-tjeklisten: samme ved hver generering → import opdaterer
    kun denne definition. Adskilt fra klageret-skabelonens UID.
    """
    blocked = blocked_checklist_uids()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if force_new:
        uid = str(uuid.uuid4()).upper()
        while uid.lower() in blocked:
            uid = str(uuid.uuid4()).upper()
        SSI_UID_FILE.write_text(uid + "\n", encoding="utf-8")
        return uid

    if SSI_UID_FILE.is_file():
        return assert_uid_not_blocked(SSI_UID_FILE.read_text(encoding="utf-8"))

    uid = str(uuid.uuid4()).upper()
    while uid.lower() in blocked:
        uid = str(uuid.uuid4()).upper()
    SSI_UID_FILE.write_text(uid + "\n", encoding="utf-8")
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
        checklist["Description"] = f"{base_desc} Sidst genereret {generated_at}.".strip()


def apply_text_replacements(text: str) -> str:
    for old, new in TEXT_REPLACEMENTS:
        text = text.replace(old, new)
    return text


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
    checklist_uid = ssi_checklist_uid(force_new=force_new_uid)

    missing_cpr_outcome = {
        "OutcomeValue": 2,
        "OutcomeType": 6,
        "OutcomeText": {
            "ContentType": "Text",
            "Title": "CPR-nummer mangler",
            "Description": "Indhent CPR-nummer hos borgeren og journaliser opslag.",
            "TitleNewNorwegian": None,
            "DescriptionNewNorwegian": None,
        },
    }
    missing_consent_outcome = {
        "OutcomeValue": 2,
        "OutcomeType": 6,
        "OutcomeText": {
            "ContentType": "Text",
            "Title": "Samtykke fra anden forældremyndighedsindehaver mangler",
            "Description": "Ved fælles forældremyndighed skal samtykke indhentes før destruktion.",
            "TitleNewNorwegian": None,
            "DescriptionNewNorwegian": None,
        },
    }

    points = [
        checkpoint(
            "1",
            "Henvendelsen er modtaget og journalført på sagen",
            sort_id=1,
            index=0,
            milestone=99001,
        ),
        checkpoint(
            "2",
            "Modtagelsesdato hos SSI er registreret",
            sort_id=2,
            index=1,
            milestone=99001,
            description="Brug dato for modtagelse hos SSI ( også ved videresendelse internt).",
        ),
        checkpoint(
            "3",
            "Anmodende forælder og barn under 15 år er registreret som parter",
            sort_id=3,
            index=2,
            milestone=99001,
        ),
        checkpoint(
            "4",
            "Kategori/type af rettighedsanmodning er valgt (indsigt/destruktion/PKU)",
            sort_id=4,
            index=3,
            milestone=99001,
        ),
        checkpoint(
            "5",
            "CPR-nummer er oplyst eller indhentet",
            sort_id=5,
            index=4,
            milestone=99001,
            outcome=missing_cpr_outcome,
        ),
        checkpoint(
            "6",
            "Identitet er verificeret (Digital Post eller CPR-opslag dokumenteret)",
            sort_id=6,
            index=5,
            milestone=99001,
        ),
        checkpoint(
            "7",
            "Forældremyndighed er kontrolleret — relevant CPR-udtræk journaliseret",
            sort_id=7,
            index=6,
            milestone=99001,
        ),
        checkpoint(
            "8",
            "Samtykke fra anden forældremyndighedsindehaver foreligger ved fælles FM",
            sort_id=8,
            index=7,
            milestone=201,
            outcome=missing_consent_outcome,
        ),
        checkpoint(
            "9",
            "Intern høring/destruktionsanmodning til MS/PKU er sendt og journaliseret",
            sort_id=9,
            index=8,
            milestone=99003,
        ),
        checkpoint(
            "10",
            "Svar fra intern høring er modtaget og journaliseret",
            sort_id=10,
            index=9,
            milestone=99003,
        ),
        checkpoint(
            "11",
            "Manglende oplysninger er anmodet om hos borger (hvis relevant)",
            sort_id=11,
            index=10,
            milestone=200,
        ),
        checkpoint(
            "12",
            "Sagen er tilstrækkeligt oplyst før afgørelse (GDPR/forvaltningsret)",
            sort_id=12,
            index=11,
            milestone=99003,
        ),
        checkpoint(
            "13",
            "Personoplysninger behandles i overensstemmelse med GDPR",
            sort_id=13,
            index=12,
            milestone=99003,
            answer_option=2,
        ),
        checkpoint(
            "14",
            "Udkast til afgørelse er udarbejdet",
            sort_id=14,
            index=13,
            milestone=217,
        ),
        checkpoint(
            "15",
            "Afgørelse er godkendt internt",
            sort_id=15,
            index=14,
            milestone=217,
        ),
        checkpoint(
            "16",
            "Afgørelse med bilag er sendt til borger og journaliseret",
            sort_id=16,
            index=15,
            milestone=217,
        ),
        checkpoint(
            "17",
            "Afsendelse via Digital Post/brev er dokumenteret",
            sort_id=17,
            index=16,
            milestone=217,
        ),
        checkpoint(
            "18",
            "Sagen er afsluttet med korrekt status",
            sort_id=18,
            index=17,
            milestone=218,
        ),
        checkpoint(
            "19",
            "Alle relevante dokumenter er arkiveret/journaliseret",
            sort_id=19,
            index=18,
            milestone=218,
        ),
        checkpoint(
            "20",
            "Efterfølgende destruktionsbekræftelse er registreret ved genåbning (hvis modtaget)",
            sort_id=20,
            index=19,
            milestone=218,
        ),
    ]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.00")
    checklist = {
        "Name": CHECKLIST_NAME,
        "Description": "Demo/markedsdialog — DBIS rettighedsanmodning PKU og destruktion (barn under 15).",
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
    finalize_checklist_for_import(
        checklist, uid=checklist_uid, generated_at=generated_at
    )
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
    """Clear entity Recnos for import — but keep codetable Recnos under CaseTypes."""
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


def build_process_model(checklist_uid: str, *, checklist_definition_recno: int | None = None) -> dict:
    pm = json.loads(PM_SOURCE.read_text(encoding="utf-8"))
    pm = json.loads(json.dumps(pm))  # deep copy

    workunit_ids = collect_workunit_ids(pm)
    to_remap = collect_remap_uuids(pm) - workunit_ids
    uid_map = {old: new_uid() for old in to_remap}

    raw = json.dumps(pm, ensure_ascii=False)
    raw = apply_text_replacements(raw)
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
        "Day": 27,
        "Hour": 12,
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
        "SSI markedsdialog demo — rettighedsanmodning PKU/destruktion. "
        f"Tjekliste UID (importér og kobl manuelt): {checklist_uid}"
    )
    props["BaseUID"] = pm["BaseUID"]

    for stage in pmd["StageConfigs"]:
        st_props = stage["Properties"]
        if st_props.get("SortId") == 1:
            st_props["Title"] = PROCESS_TITLE
            st_props["CalculationDays"] = 30
            if checklist_definition_recno is not None:
                st_props["ChecklistDefinition"] = checklist_definition_recno
                st_props["ChecklistDefinitionDesc"] = CHECKLIST_NAME
            else:
                # Uden Recno oprettes ingen tjekliste-instans med checkpunkter på fasen.
                st_props["ChecklistDefinition"] = None
                st_props["ChecklistDefinitionDesc"] = CHECKLIST_NAME
        if st_props.get("SortId") == 2:
            st_props["Title"] = STAGE2_TITLE
            st_props["CalculationDays"] = 14
            st_props["AutoGenerate"] = False

        for ms in stage.get("StageMileStoneConfigs", []):
            if ms.get("Properties", {}).get("Title") == "Klagefrist":
                ms["MarkedForRemoval"] = True

        if stage["Properties"].get("Title") == STAGE2_TITLE:
            for sp in stage.get("StageProcessConfigs", []):
                sp["Properties"]["DisplayName"] = "Registrer destruktionsbekræftelse"

    null_recnos(pm)
    return pm


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate SSI Flow checklist + process model JSON.")
    parser.add_argument(
        "--new-checklist-identity",
        action="store_true",
        help=(
            "Tildel ny stabil SSI-UID (skriver SSI_CHECKLIST_UID.txt). "
            "Kun hvis I bevidst vil starte en helt ny tjekliste-definition i tenant."
        ),
    )
    parser.add_argument(
        "--checklist-definition-recno",
        type=int,
        metavar="RECNO",
        help=(
            "Recno for importeret SSI-tjekliste — sættes på fase 1 i procesmodellen. "
            "Alternativt: skriv Recno i SSI_CHECKLIST_DEFINITION_RECNO.txt"
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
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
        (DOWNLOADS / SSI_UID_FILE.name).write_text(
            checklist["UID"] + "\n", encoding="utf-8"
        )

    readme = OUT_DIR / "README-import.txt"
    readme.write_text(
        f"""SSI Flow demo — import i tenant
================================

SSI-tjekliste — stabil UID (opdater under arbejdet)
---------------------------------------------------
Import matcher på UID. Denne export bruger altid SSI-UID fra {SSI_UID_FILE.name}
(nuværende: {checklist['UID']}) — IKKE klageret-skabelonens UID ({KNOWN_KLAGERET_CHECKLIST_UID}).

• Første import med SSI-UID → ny ChecklistDefinition (påvirker ikke klageret-tjeklisten).
• Senere import med samme SSI-UID → opdaterer kun SSI-tjeklisten.

Milepæle (MilestoneType 99001, 217, …) er uændrede codetable-recnos. Recno udelades i JSON.

1. Importér tjekliste: {CHECKLIST_FILENAME}
2. Importér procesmodel: {PM_FILENAME}
3. Tjekliste på fase 1 (KRÆVES for checkpunkter på sagen):
   • Find Recno i admin efter tjekliste-import
   • Skriv Recno i {SSI_CHECKLIST_RECNO_FILE.name} ELLER --checklist-definition-recno
   • Regenerér procesmodel, importér, publicér
   • Opret NY sag (gamle sager får ikke checkpunkter automatisk)

4. I UI: Nulstil filter (milepæl + status) hvis I kun ser 0/0.

Helt ny SSI-identitet (sjældent):
  uv run python toolkit/scripts/build_ssi_flow_exports.py --new-checklist-identity
""",
        encoding="utf-8",
    )

    print(f"Checklist: {cl_path}")
    print(f"Process model: {pm_path}")
    print(f"SSI checklist UID (stable): {checklist['UID']}")
    print(f"UID source: {SSI_UID_FILE}")
    if cld_recno is not None:
        print(f"Process model fase 1 ChecklistDefinition Recno: {cld_recno}")
    else:
        print(
            "WARNING: ChecklistDefinition not set on process model — "
            f"add Recno via {SSI_CHECKLIST_RECNO_FILE.name} and regenerate"
        )
    if args.new_checklist_identity:
        print("Mode: new SSI identity written — first import creates new definition in tenant")
    else:
        print("Mode: same SSI UID — import updates SSI checklist; does not touch klageret UID")


if __name__ == "__main__":
    main()
