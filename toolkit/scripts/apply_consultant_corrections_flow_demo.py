"""
Apply consultant corrections to English Flow demo process model (Behandle søknad m/klagerett).

See: Korrigeringer Prosessmodell Behandle søknad m.docx
"""
from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEMO_JSON = (
    REPO
    / "projects/process-platform/flow/manuscripts/Demo setup/Handle application with right of appeal (English).json"
)

# Standard milestone / document category recnos (6.12 seed, demo tenant)
MILESTONE_ADDITIONAL_DOCUMENTATION_RECEIVED = 203
DOC_CAT_INCOMING_MINOR = 433
DOC_CAT_INCOMING_SIGNIFICANT = 434
DOC_CAT_OUTGOING_MINOR_REQUEST = 437
DOC_CAT_APPEAL = 99024

MILESTONE_AUTOMATION_IDS_RECEIVED = (
    "78be38e9-a39d-4f51-a746-f56479b1abaf",
    "bc5007cc-ff0a-4049-9a18-878357efa296",
)
MILESTONE_MINOR_REQUESTED = "5feeb7e2-ed14-483c-a3b5-bd70944fe55c"
MILESTONE_APPEAL_RECEIVED = "7c058a8b-c00b-4598-b364-4cb1f13cb64d"

AUTO_RECEIPT_WU = "10C6E5A9-C167-459B-B556-A0973A5E31A4"
MAJOR_DEF_WU = "9E7A8B38-C249-4CD8-A95C-0EDD06ADB727"


def patch_milestones(data: dict) -> int:
    n = 0
    for stage in data["ProcessModelData"]["StageConfigs"]:
        for ms in stage.get("StageMileStoneConfigs", []):
            props = ms["Properties"]
            aid = props.get("AutomationID", "")
            if aid in MILESTONE_AUTOMATION_IDS_RECEIVED:
                props["MilestoneTypeRecno"] = MILESTONE_ADDITIONAL_DOCUMENTATION_RECEIVED
                props["MilestoneTypeDesc"] = "Additional documentation received"
                props["DocumentCategoryRecnos"] = [
                    DOC_CAT_INCOMING_MINOR,
                    DOC_CAT_INCOMING_SIGNIFICANT,
                ]
                n += 1
            elif aid == MILESTONE_MINOR_REQUESTED:
                props["DocumentCategoryRecnos"] = [DOC_CAT_OUTGOING_MINOR_REQUEST]
                n += 1
            elif aid == MILESTONE_APPEAL_RECEIVED:
                props["DocumentCategoryRecnos"] = [DOC_CAT_APPEAL]
                n += 1
    return n


def set_argument_value(wa: str, name: str, value: str) -> str:
    pat = rf'(<argument[^>]*name="{re.escape(name)}"[^>]*>)([^<]*)(</argument>)'

    def repl(m: re.Match[str]) -> str:
        return m.group(1) + value + m.group(3)

    out, n = re.subn(pat, repl, wa, count=1)
    return out if n == 1 else wa


def patch_auto_receipt(wa: str) -> str:
    wa = set_argument_value(wa, "DocumentTemplateId", "#null#")
    wa = set_argument_value(wa, "DispatchDocument", "false")
    # Ensure CreateDocument grouping on all args (PMC layout)
    wa = wa.replace('category=""', 'category="CreateDocument"', 1)  # ProgressPlanId only if empty
    wa = re.sub(
        r'(<argument[^>]*name="ProgressPlanId"[^>]*)category=""',
        r'\1category="CreateDocument"',
        wa,
        count=1,
    )
    return wa


def patch_major_deficiency(wa: str) -> str:
    if "Expired_DocumentCategory" not in wa:
        return wa
    # Wrong value was 437 (minor letter); reminder must use significant letter category 438
    return set_argument_value(wa, "Expired_DocumentCategory", "438")


def patch_work_units(data: dict) -> tuple[int, int]:
    auto = major = 0
    for stage in data["ProcessModelData"]["StageConfigs"]:
        for sp in stage.get("StageProcessConfigs", []):
            props = sp["Properties"]
            wu = props.get("WorkunitId", "").upper()
            wa = props.get("WorkunitArguments") or ""
            if wu == AUTO_RECEIPT_WU.upper():
                props["WorkunitArguments"] = patch_auto_receipt(wa)
                auto += 1
            elif wu == MAJOR_DEF_WU.upper():
                props["WorkunitArguments"] = patch_major_deficiency(wa)
                major += 1
    return auto, major


def main() -> None:
    data = json.loads(DEMO_JSON.read_text(encoding="utf-8"))
    ms = patch_milestones(data)
    auto, major = patch_work_units(data)
    data["Version"] = max(int(data.get("Version", 0)), 8)
    DEMO_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Milestones updated: {ms}")
    print(f"AutoReceipt configs: {auto}")
    print(f"MajorDeficiency configs: {major}")
    print(f"Version: {data['Version']}")


if __name__ == "__main__":
    main()
