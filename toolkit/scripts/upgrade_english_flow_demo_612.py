"""
Patch English Flow demo process model for 6.12 work unit registry (ms_6.12.0).

Changes:
- FinalProcessing (E1A5B6C7…): insert EmailMessageTemplateRecno1; normalize create-email category.
- MajorDeficiencyLetter: reorder SendExpiryReminder before DeadlineDays (registry order).

Does not change demo behaviour values except structural/registry alignment.
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

EMAIL_TEMPLATE_ARG = (
    '<argument comment="Choose email message template (optional). Leave empty for no preset template." '
    'type="String" name="EmailMessageTemplateRecno1" editable="True" keyfieldvalue="Recno" '
    'descriptionfieldvalue="Name" origin="SIRIUS//code table: Email message" hidden="False" '
    'category="create email1" categorylocalizationid="007A3375-51FB-4F05-98E5-A8CE57F0EB73" '
    'namelocalizationid="9CEDA612-36D1-4596-95C5-28570EA282B6" '
    'commentlocalizationid="70A05D31-CB49-48FF-B7C6-16019E43636F">#null#</argument>'
)

FINAL_PROCESSING_WU = "E1A5B6C7-D8F9-4012-9E3F-4B6C8D0A2E4F"
MAJOR_DEF_WU = "9E7A8B38-C249-4CD8-A95C-0EDD06ADB727"


def patch_final_processing_email(wa: str) -> str:
    if "EmailMessageTemplateRecno1" in wa:
        out = wa
    else:
        marker = 'name="EmailActivityTitle1"'
        idx = wa.find(marker)
        if idx == -1:
            raise ValueError("EmailActivityTitle1 not found in FinalProcessing WorkunitArguments")
        close = wa.find("</argument>", idx)
        if close == -1:
            raise ValueError("Could not locate end of EmailActivityTitle1 argument")
        insert_at = close + len("</argument>")
        out = wa[:insert_at] + EMAIL_TEMPLATE_ARG + wa[insert_at:]

    out = out.replace('category="Create email 1"', 'category="create email1"')
    # Empty string = MissingArgumentValue at runtime for codetable string args; use #null#.
    out = re.sub(
        r'(<argument[^>]*name="EmailMessageTemplateRecno1"[^>]*>)\s*(</argument>)',
        r"\1#null#\2",
        out,
    )
    return out


def reorder_major_deficiency(wa: str) -> str:
    if "SendExpiryReminder" not in wa or "DeadlineDays" not in wa:
        return wa
    d_block = re.search(
        r'(<argument[^>]*name="DeadlineDays"[^>]*>.*?</argument>)', wa, flags=re.DOTALL
    )
    s_block = re.search(
        r'(<argument[^>]*name="SendExpiryReminder"[^>]*>.*?</argument>)', wa, flags=re.DOTALL
    )
    if not d_block or not s_block or d_block.start() > s_block.start():
        return wa
    pair_old = d_block.group(1) + s_block.group(1)
    pair_new = s_block.group(1) + d_block.group(1)
    if pair_old not in wa:
        return wa
    return wa.replace(pair_old, pair_new, 1)


def main() -> None:
    data = json.loads(DEMO_JSON.read_text(encoding="utf-8"))
    patched_fp = 0
    patched_md = 0
    for stage in data["ProcessModelData"]["StageConfigs"]:
        for sp in stage.get("StageProcessConfigs", []):
            props = sp["Properties"]
            wu = props.get("WorkunitId", "").upper()
            wa = props.get("WorkunitArguments") or ""
            if wu == FINAL_PROCESSING_WU.upper():
                props["WorkunitArguments"] = patch_final_processing_email(wa)
                patched_fp += 1
            elif wu == MAJOR_DEF_WU.upper():
                new_wa = reorder_major_deficiency(wa)
                if new_wa != wa:
                    props["WorkunitArguments"] = new_wa
                    patched_md += 1

    data["Version"] = max(int(data.get("Version", 0)), 7)
    DEMO_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Patched FinalProcessing configs: {patched_fp}")
    print(f"Patched MajorDeficiency configs: {patched_md}")
    print(f"Process model Version set to: {data['Version']}")


if __name__ == "__main__":
    main()
