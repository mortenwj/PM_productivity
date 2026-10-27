"""Repair corrupted MajorDeficiency WorkunitArguments in English demo JSON."""
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
EN = REPO / "projects/process-platform/flow/manuscripts/Demo setup/Handle application with right of appeal (English).json"
SSI = REPO / "outputs/customer-meetings/ssi-flow/Behandle rettighedsanmodning PKU destruktion (SSI demo).json"


def extract_wa(data: dict, wu_prefix: str) -> str:
    for stage in data["ProcessModelData"]["StageConfigs"]:
        for sp in stage.get("StageProcessConfigs", []):
            if sp["Properties"]["WorkunitId"].upper().startswith(wu_prefix.upper()):
                return sp["Properties"]["WorkunitArguments"]
    raise SystemExit(f"WU {wu_prefix} not found")


def get_arg_value(wa: str, name: str) -> str | None:
    m = re.search(rf'name="{re.escape(name)}"[^>]*>([^<]*)</argument>', wa)
    return m.group(1) if m else None


def set_arg_value(wa: str, name: str, value: str) -> str:
    pat = rf'(<argument[^>]*name="{re.escape(name)}"[^>]*>)([^<]*)(</argument>)'

    def repl(m: re.Match[str]) -> str:
        return m.group(1) + value + m.group(3)

    out, n = re.subn(pat, repl, wa, count=1)
    if n != 1:
        raise ValueError(f"Could not set {name}")
    return out


def main() -> None:
    en = json.loads(EN.read_text(encoding="utf-8"))
    broken = extract_wa(en, "9E7A8B38")
    ssi_wa = extract_wa(json.loads(SSI.read_text(encoding="utf-8")), "9E7A8B38")

    # Preserve demo-specific values where still readable from broken export
    preserve = [
        "DocumentActivityTitle1",
        "DocumentArchive",
        "DocumentCategory",
        "DocumentTitle",
        "DocumentTemplate",
        "DeadlineDays",
        "Expired_DocumentArchive",
        "Expired_DocumentTitle",
        "Expired_DocumentTemplate",
        "FinalWarningDays",
        "Final_DocumentArchive",
        "Final_DocumentCategory",
        "Final_DocumentTitle",
        "Final_DocumentTemplate",
        "SendExpiryReminder",
        "SendFinalWarning",
        "AutoDispatchReminderDocument",
        "AutoDispatchFinalWarningDocument",
        "DispatchChannelId",
    ]
    wa = ssi_wa
    for name in preserve:
        val = get_arg_value(broken, name)
        if val is not None:
            wa = set_arg_value(wa, name, val)

    wa = set_arg_value(wa, "Expired_DocumentCategory", "438")

    for stage in en["ProcessModelData"]["StageConfigs"]:
        for sp in stage.get("StageProcessConfigs", []):
            if sp["Properties"]["WorkunitId"].upper().startswith("9E7A8B38"):
                sp["Properties"]["WorkunitArguments"] = wa

    EN.write_text(json.dumps(en, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Repaired MajorDeficiency WorkunitArguments")
    print("Expired_DocumentCategory", get_arg_value(wa, "Expired_DocumentCategory"))
    print("arg count", len(re.findall(r'name="', wa)))


if __name__ == "__main__":
    main()
