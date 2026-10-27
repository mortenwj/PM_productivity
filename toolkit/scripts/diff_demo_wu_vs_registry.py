"""Compare demo process model WorkunitArguments to 6.12 .wu registry definitions."""
from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEMO = REPO / "projects/process-platform/flow/manuscripts/Demo setup/Handle application with right of appeal (English).json"
WU_ROOT = Path(r"c:\Users\MortenJensen\source\repos\te-industry-public360\core-bl\Source\si-bl-process-platform-build\WorkUnits\FlowWorkUnits")

WU_MAP = {
    "E1A5B6C7-D8F9-4012-9E3F-4B6C8D0A2E4F": WU_ROOT / "StandardProcesses/NVE Processes/FinalProcessing.wu",
    "89e0ed8c-7391-4202-9f4d-d9d2d631c37a": WU_ROOT / "StandardProcesses/NVE Processes/HearingProcess.wu",
    "9E7A8B38-C249-4CD8-A95C-0EDD06ADB727": WU_ROOT / "StandardProcesses/MajorDeficiencyLetter/MajorDeficiencyLetter.wu",
    "10C6E5A9-C167-459B-B556-A0973A5E31A4": WU_ROOT / "StandardProcesses/AutoReceipt.wu",
    "6F8C2A1B-4E7D-4C9A-A3F1-2B5D8E9C0A1F": WU_ROOT / "StandardProcesses/CreateSingleDocument.wu",
}


def parse_demo_args(wa: str) -> list[str]:
    return re.findall(r'name="([^"]+)"', wa)


def parse_wu_args(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    root = ET.fromstring(text)
    ns = {"x": "http://www.w3.org/2001/XMLSchema-instance"}
    # workUnit has default ns sometimes - strip
    names = []
    for arg in root.iter():
        if arg.tag.endswith("argument") and "name" in arg.attrib:
            names.append(arg.attrib["name"])
    return names


def main() -> None:
    data = json.loads(DEMO.read_text(encoding="utf-8"))
    seen: set[tuple[str, str]] = set()
    for stage in data["ProcessModelData"]["StageConfigs"]:
        for sp in stage.get("StageProcessConfigs", []):
            props = sp["Properties"]
            wu = props["WorkunitId"].upper()
            wu_key = props["WorkunitId"]
            # normalize lookup
            lookup = None
            for k, v in WU_MAP.items():
                if k.upper() == wu:
                    lookup = (k, v)
                    break
            if not lookup:
                print(f"Unknown WU: {wu_key} ({props.get('DisplayName')})")
                continue
            key = (lookup[0], props.get("DisplayName"))
            if key in seen:
                continue
            seen.add(key)
            demo_names = parse_demo_args(props.get("WorkunitArguments", ""))
            reg_names = parse_wu_args(lookup[1])
            demo_set, reg_set = set(demo_names), set(reg_names)
            missing = [n for n in reg_names if n not in demo_set]
            extra = [n for n in demo_names if n not in reg_set]
            print(f"\n=== {props.get('DisplayName')} ===")
            print(f"Registry: {lookup[1].name}")
            if missing:
                print(f"  MISSING in demo ({len(missing)}): {missing}")
            if extra:
                print(f"  EXTRA in demo ({len(extra)}): {extra}")
            if not missing and not extra:
                print("  Arg names match registry.")
            # order check (first mismatch only)
            for i, (a, b) in enumerate(zip(demo_names, reg_names)):
                if a != b:
                    print(f"  Order diff at index {i}: demo={a} registry={b}")
                    break
            else:
                if len(demo_names) == len(reg_names):
                    print("  Order matches.")


if __name__ == "__main__":
    main()
