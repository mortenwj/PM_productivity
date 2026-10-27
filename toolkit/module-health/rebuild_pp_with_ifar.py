#!/usr/bin/env python3
"""Merge Process Platform + IFAR ADO snapshots and rebuild scorecard."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "toolkit" / "module-health"))
from build_scorecard import build  # noqa: E402

IFAR_PFRS = [
    {"id": 74050, "fields": {"Custom.ImpactedModule": "IFAR"}},
    {"id": 146088, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "POLITIHØGSKOLEN PUBLIC360"}},
    {"id": 149838, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "BANE NOR"}},
    {"id": 151440, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "NORDRE FOLLO KOMMUNE PUBLIC360"}},
    {"id": 151815, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "KONKURRANSETILSYNET PUBLIC360"}},
    {"id": 174530, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "KONKURRANSETILSYNET PUBLIC360"}},
    {"id": 175370, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "BANE NOR SF PUBLIC360"}},
    {"id": 175810, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "GRAN KOMMUNE PUBLIC360"}},
    {"id": 177289, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Arbetsmiljöverket"}},
    {"id": 177814, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Arbetsmiljöverket"}},
    {"id": 177823, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Arbetsmiljöverket"}},
    {"id": 178371, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Arbetsmiljöverket"}},
    {"id": 179028, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "LINDESNES KOMMUNE PUBLIC360"}},
    {"id": 179194, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "FLEKKEFJORD KOMMUNE PUBLIC360"}},
    {"id": 179398, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "TOLLETATEN PUBLIC360"}},
    {"id": 189202, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Dirmin "}},
    {"id": 208709, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Strålsäkerhetsmyndigheten"}},
    {"id": 211718, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "UM/MFA DK"}},
    {"id": 254123, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Arbetsmiljöverket"}},
    {"id": 255184, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Arbetsmiljöverket"}},
    {"id": 267690, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "UM / MFA DK"}},
    {"id": 267711, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "UM"}},
    {"id": 269202, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Arbetsmiljöverket"}},
    {"id": 269922, "fields": {"Custom.ImpactedModule": "IFAR"}},
    {"id": 271358, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "DSS"}},
    {"id": 293303, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "UM"}},
    {"id": 300599, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "AST"}},
    {"id": 352837, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Nav, FMA"}},
    {"id": 352850, "fields": {"Custom.ImpactedModule": "IFAR"}},
    {"id": 368994, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "DIO/DSS"}},
    {"id": 402494, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "UDENRIGSMINISTERIET "}},
    {"id": 407246, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Statens vegvesen, Forsvarsmateriell"}},
    {"id": 408393, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Statens vegvesen, Forsvarsmateriell"}},
    {"id": 425386, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "Oslo kommune"}},
    {"id": 430142, "fields": {"Custom.ImpactedModule": "IFAR", "Custom.Customername": "SIDA"}},
]

IFAR_BUGS = [
    {"id": 422547, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
    {"id": 424183, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 2}},
    {"id": 424423, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
    {"id": 425019, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
    {"id": 425048, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
    {"id": 427829, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
    {"id": 428534, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
    {"id": 430505, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 2}},
    {"id": 431168, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 1}},
    {"id": 431307, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
    {"id": 431338, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
    {"id": 431343, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
    {"id": 431360, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
    {"id": 431481, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 2}},
    {"id": 431774, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
    {"id": 431895, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
    {"id": 432225, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
    {"id": 432562, "fields": {"Custom.ImpactedModule": "IFAR", "Microsoft.VSTS.Common.Priority": 3}},
]

scratch = ROOT / "outputs" / "scratch"
bugs = json.loads((scratch / "module_health_bugs_pp.json").read_text()) + IFAR_BUGS
pfrs = json.loads((scratch / "module_health_pfrs_pp.json").read_text()) + IFAR_PFRS
bugs_path = scratch / "module_health_bugs_pp_with_ifar.json"
pfrs_path = scratch / "module_health_pfrs_pp_with_ifar.json"
bugs_path.write_text(json.dumps(bugs, indent=2), encoding="utf-8")
pfrs_path.write_text(json.dumps(pfrs, indent=2), encoding="utf-8")

out = ROOT / "outputs" / "portfolio" / "module_health_2026-08-05_process-platform.md"
result = build(
    excel_path=None,
    bugs_path=bugs_path,
    pfrs_path=pfrs_path,
    team_filter="Process Platform",
    module_filter=None,
    output_path=out,
    include_revenue=False,
)
print(json.dumps(result, indent=2))
