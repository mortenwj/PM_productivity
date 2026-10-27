"""Assess NAV endringsønsker spreadsheet against ADO/release evidence."""
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / "outputs/pfr/nav_endringonsker_parsed.json"
OUT = REPO / "outputs/pfr/nav_endringonsker_assessment_2026-09-09.csv"

ASSESS = {
    336166: {
        "status": "Fully implemented",
        "when": "6.4 (shipped Feb 2025)",
        "evidence": "Release notes Feb 2025; ADO child 336596 closed Dec 2024; tag 6.4",
        "customer_message": "Search for unregistered contacts on case level is standard from 6.4.",
    },
    335602: {
        "status": "Fully implemented",
        "when": "Aug 2025 (360° Online)",
        "evidence": "PFR Already implemented; core 364592; CIM Fikset August 2025",
        "customer_message": "Searchable org.unit in Distribution for other units webpart was delivered.",
    },
    351566: {
        "status": "Fully implemented",
        "when": "Mar 2025",
        "evidence": "Core 354664 Teams AutoSync multiple folder bindings closed Mar 2025",
        "customer_message": "Teams automatic sync can bind multiple folders/chats to one case.",
    },
    354222: {
        "status": "Partially implemented",
        "when": "6.4–6.5 (2025) + Aug 2025 for distribution units",
        "evidence": "IFAR quicksearch 6.4/6.5; distribution units via 335602/364592; groups still open",
        "customer_message": "Type-in/search in webparts: IFAR fixed 6.4/6.5; distribution-for-units Aug 2025; distribution groups still planned.",
    },
    335012: {
        "status": "Partially implemented",
        "when": "Ongoing 2024–2026",
        "evidence": "Accessibility epic 244281 Active; CIM Fixed on specific items",
        "customer_message": "Several NAV accessibility findings addressed under ongoing accessibility program.",
    },
    350612: {
        "status": "Partially implemented",
        "when": "Jan 2024–Feb 2026 (Extended stand-in)",
        "evidence": "Extended stand-in release notes 2024–2026; NAV-specific refinements still open",
        "customer_message": "Major stand-in expansion delivered since 5.13/6.x; additional NAV stand-in asks remain backlog.",
    },
    395352: {
        "status": "Partially implemented",
        "when": "Jan 2024–Feb 2026",
        "evidence": "Same extended stand-in program as 350612",
        "customer_message": "Expanded stand-in capability shipped incrementally; several NAV refinements still open.",
    },
    400608: {
        "status": "Partially implemented",
        "when": "2025–2026",
        "evidence": "Stand-in/webpart display count improvements theme",
        "customer_message": "Part of stand-in/webpart improvement stream.",
    },
    347815: {
        "status": "Planned / in development",
        "when": "Target 6.11 (2026)",
        "evidence": "Core 373813 Active; tagged 6.11 May 2026",
        "customer_message": "Infotorg Folkeregister parity with FIKS in development for 6.11.",
    },
    373813: {
        "status": "Planned / in development",
        "when": "Target 6.11 (2026)",
        "evidence": "Active Infotorg adapter; covers 347815 and CS0038567",
        "customer_message": "Folkeregister search improvements for Infotorg planned in 6.11.",
    },
    352215: {
        "status": "Planned / in development",
        "when": "Target 6.11 (2026)",
        "evidence": "CIM Planned 6.11; FIKS may satisfy part of need",
        "customer_message": "Direct register lookup for recipients planned in 6.11.",
    },
    350615: {
        "status": "Planned / in development",
        "when": "Target 6.11 (2026)",
        "evidence": "Duplicate of 352215",
        "customer_message": "Same register-recipient simplification as 352215.",
    },
    351531: {
        "status": "Planned / in development",
        "when": "Roadmap (not released)",
        "evidence": "Core duplicate 395458 still New",
        "customer_message": "To-date on manually granted access rights on roadmap, not yet released.",
    },
    344327: {
        "status": "Planned / in development",
        "when": "In development",
        "evidence": "Linked core 93761 React Files list",
        "customer_message": "Main file vs attachment visibility comes with new React Files view.",
    },
    351211: {
        "status": "Planned / in development",
        "when": "Roadmap",
        "evidence": "Related 348593 eFormidling2 Active",
        "customer_message": "Dispatch channel filtering on roadmap; related work ongoing.",
    },
    203857: {
        "status": "Not implemented (closed out of scope)",
        "when": "Closed Jan 2026 without delivery",
        "evidence": "ADO comment: generic Modify file split not planned for 2026",
        "customer_message": "Not being implemented; alternative public-read/eInnsyn path pursued.",
    },
    358729: {
        "status": "Not implemented (by design)",
        "when": "Rejected 2025",
        "evidence": "Conclusion By Design",
        "customer_message": "Intentional product design.",
    },
    354146: {
        "status": "Not implemented (duplicate)",
        "when": "Closed 2025",
        "evidence": "Duplicate Office WebApps UI request",
        "customer_message": "Duplicate — not a separate delivery.",
    },
}

CS_ASSESS = {
    "CS0026755": {
        "status": "Already supported (configuration)",
        "when": "Available via Full Flex UI",
        "evidence": "CIM: ivaretatt gjennom Full Flex UI",
        "customer_message": "Mandatory fields per case type configurable in Full Flex UI today.",
    },
    "CS0057279": {
        "status": "Resolved (customer/integration)",
        "when": "Marked Løst in CIM",
        "evidence": "SIF access group inheritance from case to integrated documents",
        "customer_message": "Resolved in NAV/SIF integration — verify with integration team.",
    },
    "CS0011998": {
        "status": "Resolved (customer)",
        "when": "Marked Løst in CIM",
        "evidence": "CIM Closed/Løst",
        "customer_message": "Marked resolved — confirm scope with case owner.",
    },
    "CS0005990": {
        "status": "Resolved (customer)",
        "when": "CIM Closed",
        "evidence": "Notification when document sent to distribution unit",
        "customer_message": "Closed in CIM — verify product vs process resolution.",
    },
    "CS0038567": {
        "status": "Planned / in development",
        "when": "Target 6.11 (2026)",
        "evidence": "Maps to 373813; CIM Her er det en fiks",
        "customer_message": "Folkeregister search improvements planned with Infotorg adapter in 6.11.",
    },
}

DEFAULT = {
    "status": "Not yet implemented",
    "when": "",
    "evidence": "No matching release or closed core implementation found",
    "customer_message": "Still open product gap or awaiting prioritization.",
}


def parse_devops(val) -> list[int]:
    if val is None:
        return []
    if isinstance(val, (int, float)) and val == val:
        return [int(val)]
    s = str(val).strip()
    if s.upper() in ("N/A", "TESTSak".upper(), "TEST", ""):
        return []
    return [int(x) for x in re.findall(r"\d{5,6}", s)]


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    rows = []
    for item in data:
        if item.get("Number") in (None, "Fra prosjekt"):
            continue
        desc = (item.get("Short description") or "").lower()
        if "test" in desc and desc.strip() in ("endringsønske: test", "endringsonske: test"):
            continue

        cs = str(item.get("Number") or "")
        ids = parse_devops(item.get("DevOps #"))
        assess = None
        for i in ids:
            if i in ASSESS:
                assess = ASSESS[i]
                break
        if assess is None and cs in CS_ASSESS:
            assess = CS_ASSESS[cs]
        if assess is None:
            assess = DEFAULT

        arguable = assess["status"].startswith(
            ("Fully", "Partially", "Already", "Resolved", "Planned")
        )
        rows.append(
            {
                "CS_Number": cs,
                "DevOps_IDs": ";".join(str(i) for i in ids) if ids else str(item.get("DevOps #") or ""),
                "Short_description": (item.get("Short description") or "").replace("\n", " ").strip(),
                "Contact": (item.get("Contact") or "").strip(),
                "Status_DevOps": item.get("Status Devops") or "",
                "Status_CIM": item.get("Status CIM") or "",
                "CIM_Kommentar": item.get("Kommentar") or "",
                "Implementation_Status": assess["status"],
                "When_Delivered_or_Target": assess["when"],
                "Evidence": assess["evidence"],
                "Customer_Talking_Point": assess["customer_message"],
                "Arguable_for_NAV": "Yes" if arguable else "No",
            }
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    c = Counter(r["Implementation_Status"] for r in rows)
    print(f"Rows: {len(rows)}")
    for k, v in c.most_common():
        print(f"  {k}: {v}")
    print(f"Arguable Yes: {sum(1 for r in rows if r['Arguable_for_NAV']=='Yes')}")
    print(f"Written {OUT}")


if __name__ == "__main__":
    main()
