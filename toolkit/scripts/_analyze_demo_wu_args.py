"""One-off: analyze WorkunitArguments in English Flow demo process model."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PM = ROOT / "projects/process-platform/flow/manuscripts/Demo setup/Handle application with right of appeal (English).json"
data = json.loads(PM.read_text(encoding="utf-8"))

def parse_arguments(wa: str) -> list[dict]:
    out = []
    for m in re.finditer(
        r'<argument[^>]*name="([^"]+)"[^>]*category="([^"]*)"[^>]*>([^<]*)</argument>',
        wa,
    ):
        out.append({"name": m.group(1), "category": m.group(2), "value": m.group(3)})
    return out


by_wu: dict[str, list] = {}
for stage in data["ProcessModelData"]["StageConfigs"]:
    for sp in stage.get("StageProcessConfigs", []):
        props = sp["Properties"]
        wu = props.get("WorkunitId", "")
        wa = props.get("WorkunitArguments", "")
        if wu not in by_wu:
            by_wu[wu] = {"processes": [], "arg_names": set()}
        by_wu[wu]["processes"].append(props.get("DisplayName"))
        for a in parse_arguments(wa):
            by_wu[wu]["arg_names"].add(a["name"])

print(f"Work units used: {len(by_wu)}")
for wu, info in sorted(by_wu.items(), key=lambda x: x[1]["processes"][0]):
    email = sorted(n for n in info["arg_names"] if "Email" in n or "ShowRecipients" in n or "ShowAttatch" in n)
    print(f"\n{info['processes'][0]} ({len(info['processes'])} config(s))")
    print(f"  WU: {wu}")
    if email:
        print(f"  Email args: {email}")
    print(f"  Has EmailMessageTemplateRecno: {any('EmailMessageTemplateRecno' in n for n in info['arg_names'])}")
