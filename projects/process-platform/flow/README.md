# 360° Flow — documentation index

**Purpose:** Product definition, commercial packaging, pilot status, and workshop materials for **360° Flow** (Process Automation Framework / PAF).

---

## Workshop (Day 1)

| Document | Description |
|----------|-------------|
| [Flow_Pilot_Status_And_Learnings.md](./Flow_Pilot_Status_And_Learnings.md) | **Start here** — pilot status, synthesized learnings, open questions |
| [Flow_Day1_Session_Plan.md](./Flow_Day1_Session_Plan.md) | 60–75 min agenda, slide outline, facilitation |
| [Flow_Pilot_Workshop.pptx](./Flow_Pilot_Workshop.pptx) | Branded deck (regenerate via script below) |
| [build_flow_pilot_deck.ps1](./build_flow_pilot_deck.ps1) | PowerShell deck builder (Tieto template) |

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "projects/process-platform/flow/build_flow_pilot_deck.ps1"
```

**Sibling session:** [BRE Day 1](../bre/BRE_Day1_Session_Plan.md) — assumes Flow inventory covered earlier.

---

## Product & commercial

| Document | Description |
|----------|-------------|
| [360_Flow_PRD_Reconstruction_Unredacted_v4.md](./360_Flow_PRD_Reconstruction_Unredacted_v4.md) | PRD reconstruction + capability matrix |
| [360_Flow_Commercial_Spec_v1.md](./360_Flow_Commercial_Spec_v1.md) | Pilot commercial rules (2 processes, shipped blocks) |
| [360_Flow_Module_Page_DRAFT.md](./360_Flow_Module_Page_DRAFT.md) | Wiki module page draft |
| [360_Flow_Product_Sheet_ENG.md](./360_Flow_Product_Sheet_ENG.md) | Module product sheet copy (ENG) — **P00285** |
| [360_Flow_Product_Sheet_ENG.pptx](./360_Flow_Product_Sheet_ENG.pptx) | **Module product data sheet (ENG)** — Enablement template |
| `build_flow_product_sheet.py` | Regenerate module `.pptx` |
| [360_Flow_Implementation_Package_Product_Sheet_ENG.md](./360_Flow_Implementation_Package_Product_Sheet_ENG.md) | Implementation *service* sheet copy (separate SKU) |
| [360_Flow_Implementation_Package_Product_Sheet_ENG.pptx](./360_Flow_Implementation_Package_Product_Sheet_ENG.pptx) | *(Outdated)* implementation package — regenerate from module copy when approved |
| [360_Flow_Implementation_Package_2Process_SalesKit_DRAFT.md](./360_Flow_Implementation_Package_2Process_SalesKit_DRAFT.md) | Sales kit / commercial PRD (delivery + contract) |
| [360_Flow_Implementation_Delivery_Project_Description_DRAFT.md](./360_Flow_Implementation_Delivery_Project_Description_DRAFT.md) | **First delivery project** — run model, time estimate, conditions |
| [360_Flow_6.10_Release_Note_DRAFT.md](./360_Flow_6.10_Release_Note_DRAFT.md) | 6.10 pilot release note draft |
| [Process_Framework_Pilot_One_Pager.md](../process-models/Process_Framework_Pilot_One_Pager.md) | Pilot intent one-pager |

---

## DevOps tracking

| Document | Description |
|----------|-------------|
| [experiment_release_notes_epic_414623_paf_program.md](../pilot/experiment_release_notes_epic_414623_paf_program.md) | PAF program epic tree |
| [PAF_pilot_weekly_report_SPEC.md](../pilot/PAF_pilot_weekly_report_SPEC.md) | Weekly stakeholder report spec |
| [pilot_weekly_report_2026-04-21.md](../pilot/pilot_weekly_report_2026-04-21.md) | Latest populated weekly report in repo |

---

## Prototypes

| Path | Description |
|------|-------------|
| [portfolio-desktops-prototype/](./portfolio-desktops-prototype/README.md) | Clickable Vite prototype — manager worklists, portfolio desktop, reporting |

```powershell
cd projects/process-platform/flow/portfolio-desktops-prototype
npm install
npm run dev
```

---

## Enablement

| Document | Description |
|----------|-------------|
| [360_Flow_Demo_Setup_DRAFT.md](./360_Flow_Demo_Setup_DRAFT.md) | Demo tenant setup (wiki source; live: [360° Flow - Demo setup](https://wiki.software-innovation.com/wiki/360%C2%B0_Flow_-_Demo_setup)) |
| [manuscripts/Demo setup/360_Flow_Standard_Demo_MANUSCRIPT.md](./manuscripts/Demo%20setup/360_Flow_Standard_Demo_MANUSCRIPT.md) | Standard demo presenter script (v1) |
| [manuscripts/01_Flow_introduction_MANUSCRIPT.md](./manuscripts/01_Flow_introduction_MANUSCRIPT.md) | Training video script |
