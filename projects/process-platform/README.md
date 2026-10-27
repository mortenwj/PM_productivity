# Process Platform project

Cross-pillar documentation and pilot tracking for **360° Process Platform**: **Flow**, **BRE**, weekly pilot reports, workunit analysis, and process models.

---

## Pillars

| Area | Path | Start here |
|------|------|------------|
| **Flow** | [`flow/`](flow/README.md) | Pilot status, Day 1 workshop, commercial specs |
| **BRE** | [`bre/`](bre/README.md) | Business Rules Engine workshop (restore content if missing) |
| **Pilot** | [`pilot/`](pilot/) | Weekly stakeholder reports, release-note experiments, [`PAF_pilot_weekly_report_SPEC.md`](pilot/PAF_pilot_weekly_report_SPEC.md) |
| **Workunits** | [`workunits/`](workunits/) | Workunit analysis corpus + `analyze_workunits.py` |
| **Process models** | [`process-models/`](process-models/) | Framework wiki drafts, extracted model text |
| **Shared** | [`shared/`](shared/) | Cross-pillar notes (small) |

---

## Common commands

```powershell
# Flow pilot deck (requires Tieto PPT template on disk)
powershell -NoProfile -ExecutionPolicy Bypass -File "projects/process-platform/flow/build_flow_pilot_deck.ps1"

# Pilot weekly report (after refreshing JSON batches via MCP or PAT)
py -3 projects/process-platform/pilot/tools/generate_pilot_weekly_report.py
```

---

## Workshop sequence

1. **Flow Day 1** — [`flow/Flow_Day1_Session_Plan.md`](flow/Flow_Day1_Session_Plan.md)
2. **BRE Day 1** — [`bre/BRE_Day1_Session_Plan.md`](bre/BRE_Day1_Session_Plan.md) *(after BRE tree restored)*
