"""Build hierarchical Aktiviteter rows (consultant Excel layout) from work unit argument XML."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from collections import OrderedDict
from typing import Callable, Iterator

# Norwegian document category labels (tenant / consultant example)
DOC_CAT_LABELS: dict[int, str] = {
    433: "Tilleggsinformasjon - mindre mangel",
    434: "Tilleggsinformasjon - vesentlig mangel",
    437: "Mangelbrev - mindre mangel",
    438: "Mangelbrev - vesentlig mangel",
    99002: "Vedtaksbrev",
    99024: "Klage",
    99012: "Søknad",
    111: "Dokument ut",
}

ARCHIVE_LABELS = {"2": "Saksdokument", "1": "Journalsak"}
CASE_ROLE_LABELS = {"50011": "Søker"}
TEMPLATE_LABELS = {"50109": "Mangelbrev", "50134": "Brev"}

ARG_LABEL: dict[str, str] = {
    "DocumentActivityTitle1": "Aktivitetstittel - Nytt dokument",
    "DocumentActivityTitle2": "Aktivitetstittel - Nytt dokument",
    "OutboundArchive1": "Dokumentarkiv",
    "OutboundArchive2": "Dokumentarkiv",
    "OutboundArchive3": "Dokumentarkiv",
    "DocumentArchive": "Dokumentarkiv",
    "DocumentArchiveId": "Dokumentarkiv",
    "OutboundCategory1": "Dokumentkategori",
    "OutboundCategory2": "Dokumentkategori",
    "DocumentCategory": "Dokumentkategori",
    "DocumentCategoryId": "Dokumentkategori",
    "CaseRole1": "Kontakt-Saksrolle",
    "CaseRole2": "Kontakt-Saksrolle",
    "CaseContactRole": "Kontakt-Saksrolle",
    "CaseContactRoleId": "Kontakt-Saksrolle",
    "CaseRoleCC1": "Kontakt-Saksrolle kopi",
    "CaseRoleCC2": "Kontakt-Saksrolle kopi",
    "CaseContactRoleCC": "Kontakt-Saksrolle kopi",
    "DocumentTitle1": "Dokumenttittel",
    "DocumentTitle2": "Dokumenttittel",
    "DocumentTitle": "Dokumenttittel",
    "DocumentTemplateId1": "Mal",
    "DocumentTemplateId2": "Mal",
    "DocumentTemplate": "Mal",
    "DocumentTemplateId": "Mal",
    "CreateReview1": "Send til gjennomgang",
    "CreateApproval1": "Send til godkjenning",
    "CreateDispatch1": "Klar for ekspedering",
    "SendExpiryReminder": "Send påminnelse om at fristen utløper",
    "DeadlineDays": "Send påminnelse etter # dager",
    "Expired_DocumentArchive": "Arkiv for påminnelsesdokument",
    "Expired_DocumentCategory": "Kategori på påminnelsesdokument",
    "Expired_DocumentTitle": "Tittel på påminnelsesdokument",
    "Expired_DocumentTemplate": "Mal for påminnelsesdokument",
    "AutoDispatchReminderDocument": "Ekspeder påminnelsesdokument automatisk",
    "SendFinalWarning": "Send siste varsel",
    "FinalWarningDays": "Send siste varsel etter # dager",
    "Final_DocumentArchive": "Dokumentarkiv for siste varsel",
    "Final_DocumentCategory": "Dokumentkategori for siste varsel",
    "Final_DocumentTitle": "Dokumenttittel for siste varsel",
    "Final_DocumentTemplate": "Dokumentmal for siste varsel",
    "AutoDispatchFinalWarningDocument": "Ekspeder siste varsel automatisk",
    "DispatchChannelId": "Ekspederingskanal",
    "DispatchDocument": "Klar for ekspedering",
    "CheckpointActivityTitle1": "Aktivitetstittel - Sjekkpunkt",
    "EmailActivityTitle1": "Tittel på e-postaktivitet",
    "EmailMessageTemplateRecno1": "E-postmal",
    "SubProcessActivityTitle1": "Aktivitetstittel - Delprosess",
    "SubProcessAutomationId1": "Automatisering-ID for delprosess",
    "MilestoneActivityTitle1": "Aktivitetstittel - Milepæl",
    "MilestoneAutomationId1": "Automatisering-ID for milepæl",
}

SKIP_ARG_NAMES = frozenset({"ProgressPlanId"})
SKIP_ARG_PREFIXES = ("Show",)

# Category (XML) -> component title in Argumenter / Prosessdefinisjoner
CATEGORY_COMPONENT: dict[str, str] = {
    "CreateDocument": "Opprett dokument",
    "CreateSecondDocument": "Opprett dokument",
    "CreateThirdDocument": "Opprett dokument",
    "CreateFourthDocument": "Opprett dokument",
    "Document creation": "Opprett dokument",
    "Major Deficiency Letter": "Brev om vesentlig mangel",
    "create email1": "Opprett e-post",
    "Checkpoint": "Sjekkpunkt",
    "FirstCheckpoint": "Sjekkpunkt",
    "SecondCheckpoint": "Sjekkpunkt",
    "Subprocess 1": "Delprosess",
    "Milestone 1": "Milepæl",
    "Milestone": "Milepæl",
    "DispatchHandling": "Opprett dokument",
}

# Preferred component order per prosessdefinisjon name
COMPONENT_ORDER: dict[str, list[str]] = {
    "MajorDeficiencyLetter": ["Brev om vesentlig mangel"],
    "Autosend Application Receipt to applicant": ["Opprett dokument"],
    "Final processing": ["Sjekkpunkt", "Opprett dokument", "Opprett e-post", "Delprosess", "Milepæl"],
    "Document Creation Process with Review, approval, dispatch and Milestone": ["Opprett dokument"],
    "create single document": ["Opprett dokument"],
}

# Field order within standard Opprett dokument
CREATE_DOC_FIELD_ORDER = [
    "Aktivitetstittel - Nytt dokument",
    "Dokumentarkiv",
    "Dokumentkategori",
    "Kontakt-Saksrolle",
    "Kontakt-Saksrolle kopi",
    "Dokumenttittel",
    "Mal",
    "Send til gjennomgang",
    "Send til godkjenning",
    "Klar for ekspedering",
    "Ekspederingskanal",
]

MAJOR_DEF_FIELD_ORDER = CREATE_DOC_FIELD_ORDER + [
    "Send påminnelse om at fristen utløper",
    "Send påminnelse etter # dager",
    "Arkiv for påminnelsesdokument",
    "Kategori på påminnelsesdokument",
    "Tittel på påminnelsesdokument",
    "Mal for påminnelsesdokument",
    "Ekspeder påminnelsesdokument automatisk",
    "Send siste varsel",
    "Send siste varsel etter # dager",
    "Dokumentarkiv for siste varsel",
    "Dokumentkategori for siste varsel",
    "Dokumenttittel for siste varsel",
    "Dokumentmal for siste varsel",
    "Ekspeder siste varsel automatisk",
]


def _is_empty_value(val: str) -> bool:
    if not val:
        return True
    upper = val.strip().upper()
    return upper in ("NA", "N/A", "#NULL#", "NAN", "NONE")


def _format_bool(val: str) -> str:
    return "Ja" if val.strip().lower() == "true" else "Nei"


def _format_value(name: str, val: str, arg_type: str) -> str | None:
    if _is_empty_value(val):
        return None
    if arg_type == "Bool" or val.lower() in ("true", "false"):
        return _format_bool(val)
    if name.endswith("Archive1") or name.endswith("Archive2") or "Archive" in name:
        return ARCHIVE_LABELS.get(val, val)
    if "Category" in name or name in ("OutboundCategory1", "DocumentCategoryId"):
        try:
            return DOC_CAT_LABELS.get(int(val), val)
        except ValueError:
            return val
    if "Template" in name:
        return TEMPLATE_LABELS.get(val, val if not val.isdigit() else val)
    if name.startswith("CaseRole") or "ContactRole" in name:
        if val in ("-99", "#null#"):
            return None
        return CASE_ROLE_LABELS.get(val, val)
    return val


def _parse_args(xml_str: str | None) -> list[dict]:
    if not xml_str:
        return []
    try:
        root = ET.fromstring(xml_str)
    except ET.ParseError:
        return []
    rows = []
    for arg in root.findall(".//argument"):
        if (arg.get("hidden") or "").lower() == "true":
            continue
        name = arg.get("name") or ""
        rows.append(
            {
                "category": arg.get("category") or "General",
                "name": name,
                "type": arg.get("type") or "String",
                "value": (arg.text or "").strip(),
            }
        )
    return rows


def _show_flag(args: list[dict], prefix: str) -> bool:
    for a in args:
        if a["name"].startswith(prefix) and a["value"].lower() == "true":
            return True
    return False


def _category_active(category: str, args: list[dict]) -> bool:
    if category == "Major Deficiency Letter":
        return _show_flag(args, "ShowDocumentDialogue")
    if category in ("CreateDocument", "Document creation"):
        if _show_flag(args, "ShowDocumentDialogue"):
            return True
        return any(
            a["name"] in ("DocumentTitle", "DocumentTitle1", "DocumentArchiveId")
            and not _is_empty_value(a["value"])
            for a in args
        )
    if category == "DispatchHandling":
        return any(not _is_empty_value(a["value"]) for a in args if not a["name"].startswith("Show"))
    if category in ("Checkpoint", "FirstCheckpoint", "SecondCheckpoint"):
        return _show_flag(args, "ShowCheckpointDialogue")
    if category == "create email1":
        return _show_flag(args, "ShowEmailDialogue")
    if category == "Subprocess 1":
        return _show_flag(args, "ShowSubProcessDialogue")
    if category in ("Milestone 1", "Milestone"):
        return _show_flag(args, "ShowMilestoneDialogue")
    return False


def _component_for_category(category: str, prosessdef: str) -> str | None:
    if category in CATEGORY_COMPONENT:
        return CATEGORY_COMPONENT[category]
    if prosessdef == "MajorDeficiencyLetter" and "Deficiency" in category:
        return "Brev om vesentlig mangel"
    return None


def _field_order_for_component(component: str, prosessdef: str) -> list[str] | None:
    if component == "Brev om vesentlig mangel":
        return MAJOR_DEF_FIELD_ORDER
    if component == "Opprett dokument":
        return CREATE_DOC_FIELD_ORDER
    return None


def iter_activity_rows(
    prosessdef: str,
    xml_str: str | None,
    *,
    automation_by_id: dict[str, str] | None = None,
) -> Iterator[tuple[str | None, str | None, str | None]]:
    """Yield (component, field_label, value) — only one of component/field set per row."""
    args = _parse_args(xml_str)
    if not args:
        return
    by_cat: OrderedDict[str, list[dict]] = OrderedDict()
    for a in args:
        by_cat.setdefault(a["category"], []).append(a)

    active: dict[str, list[dict]] = {}
    for cat, cat_args in by_cat.items():
        if cat == "General":
            continue
        if not _category_active(cat, cat_args):
            continue
        comp = _component_for_category(cat, prosessdef)
        if not comp:
            continue
        active.setdefault(comp, []).extend(cat_args)

    order = COMPONENT_ORDER.get(prosessdef, [])
    components = [c for c in order if c in active]
    for c in active:
        if c not in components:
            components.append(c)

    for comp in components:
        cat_args = active[comp]
        if not any(
            ARG_LABEL.get(a["name"]) and not a["name"].startswith(SKIP_ARG_PREFIXES)
            for a in cat_args
        ):
            continue
        yield (comp, None, None)
        fields: dict[str, str | None] = {}
        for a in cat_args:
            if a["name"] in SKIP_ARG_NAMES or a["name"].startswith(SKIP_ARG_PREFIXES):
                continue
            label = ARG_LABEL.get(a["name"])
            if not label:
                continue
            formatted = _format_value(a["name"], a["value"], a["type"])
            if formatted is None and label not in (
                "Kontakt-Saksrolle kopi",
                "E-postmal",
                "Ekspederingskanal",
            ):
                continue
            if a["name"] == "SubProcessAutomationId1" and automation_by_id and a["value"]:
                aid = a["value"].lower()
                formatted = automation_by_id.get(aid, a["value"])
            fields[label] = formatted

        field_order = _field_order_for_component(comp, prosessdef)
        if field_order:
            labels = [f for f in field_order if f in fields]
            labels.extend([f for f in fields if f not in labels])
        else:
            labels = list(fields.keys())

        for label in labels:
            yield (None, label, fields.get(label))


def write_aktiviteter_sheet(
    ws,
    pm: dict,
    *,
    wu_to_prosessdef: dict[str, str],
    process_sort_key: Callable[[dict, dict], tuple],
) -> int:
    """Fill Aktiviteter from row 10; return row count written."""
    pmc_title = pm["ProcessModelData"]["Properties"].get("Title") or pm.get("Title")
    stages = pm["ProcessModelData"]["StageConfigs"]

    ws.cell(row=4, column=2, value=f"Prosessmodell 1: {pmc_title}")
    for idx, stage in enumerate(stages[:4], start=1):
        st = (stage.get("Properties") or {}).get("Title")
        if st:
            ws.cell(row=4 + idx, column=3, value=f"Fase {idx}: {st}")

    # Header row 9 already in template
    automation_by_id: dict[str, str] = {}
    for stage in stages:
        for proc in stage.get("StageProcessConfigs") or []:
            p = proc.get("Properties") or {}
            aid = (p.get("AutomationID") or "").lower()
            if aid:
                automation_by_id[aid] = p.get("DisplayName") or aid

    processes: list[tuple[dict, dict]] = []
    for stage in stages:
        for proc in stage.get("StageProcessConfigs") or []:
            processes.append((stage, proc))
    processes.sort(key=lambda sp: process_sort_key(sp[0], sp[1]))

    row = 10
    current_pmc: str | None = None
    current_phase: str | None = None

    for stage, proc in processes:
        p = proc.get("Properties") or {}
        stage_title = (stage.get("Properties") or {}).get("Title") or ""
        wu = (p.get("WorkunitId") or "").upper()
        prosessdef = wu_to_prosessdef.get(wu) or wu_to_prosessdef.get(wu.lower()) or ""
        proc_name = p.get("DisplayName") or ""
        if stage_title == "Klagebehandling" and wu.startswith("6F8C2A1B"):
            proc_name = "Mottatt klage"

        if current_pmc != pmc_title:
            ws.cell(row=row, column=2, value=pmc_title)
            current_pmc = pmc_title
            current_phase = None
            row += 1

        if current_phase != stage_title:
            ws.cell(row=row, column=3, value=stage_title)
            current_phase = stage_title
            row += 1

        ws.cell(row=row, column=4, value=proc_name)
        row += 1

        for comp, field, val in iter_activity_rows(
            prosessdef, p.get("WorkunitArguments"), automation_by_id=automation_by_id
        ):
            if comp:
                ws.cell(row=row, column=5, value=comp)
            if field:
                ws.cell(row=row, column=6, value=field)
                if val is not None:
                    ws.cell(row=row, column=7, value=val)
            row += 1

    return row - 10
