# Business Rules Engine (BRE) — documentation inventory

**Purpose:** Collect and synthesize everything we know about BRE — what it is, what it is meant to solve, current status, and how it fits into Public 360° and the Process Framework.

**Owner:** Process Platform team  
**Started:** June 2026  
**Status:** Inventory + **source code pilot assessment** (2026-06-08)

---

## Documents in this folder

| Document | Description |
|----------|-------------|
| [BRE_Day1_Session_Plan.md](./BRE_Day1_Session_Plan.md) | **Day 1 workshop** — 90 min agenda, slide outline, speaker notes |
| [BRE_Inventory.md](./BRE_Inventory.md) | **Start here** — synthesized overview |
| [BRE_Pilot_Readiness_Assessment.md](./BRE_Pilot_Readiness_Assessment.md) | **Code-based pilot verdict** — what works, blockers, MVP slice |
| [BRE_Architecture.md](./BRE_Architecture.md) | Architecture diagram and component map (as implemented) |
| [BRE_Reverse_Engineered_PRD.md](./BRE_Reverse_Engineered_PRD.md) | Product spec inferred from code — not aspirational docs |
| [BRE_Code_Risk_Assessment.md](./BRE_Code_Risk_Assessment.md) | Technical risks ranked for pilot go/no-go |
| [sources/ado-work-items.md](./sources/ado-work-items.md) | Azure DevOps epic, features, scenario-linked items |
| [sources/productplan-roadmap.md](./sources/productplan-roadmap.md) | ProductPlan BRE bars and reconciliation notes |
| [sources/codebase-pilot-assessment.md](./sources/codebase-pilot-assessment.md) | Detailed file-level code scan |
| [sources/codebase.md](./sources/codebase.md) | Short codebase index |
| [sources/onedrive-materials.md](./sources/onedrive-materials.md) | OneDrive folder contents and extracts |
| [sources/scenarios-register.md](./sources/scenarios-register.md) | Customer scenarios from scope sheet |
| [sources/risk-register-summary.md](./sources/risk-register-summary.md) | OneDrive commercial/organizational risks |
| [sources/wiki-and-product.md](./sources/wiki-and-product.md) | Live wiki pages, Flow PRD, commercial notes |
| [sources/oslo-workshop-deck.md](./sources/oslo-workshop-deck.md) | Oslo BRE workshop slide summary |
| [**information-package/**](./information-package/README.md) | **PRD evidence bundle** (sources + ADO + code; assembled 2026-06-16) |

---

## Source locations (originals)

| Source | Location |
|--------|----------|
| **OneDrive** | `C:\Users\MortenJensen\OneDrive - Tieto\Technology & Development - Public 360 - Business Rules Engine` |
| **Azure DevOps** | Epic [#11122](https://dev.azure.com/tieto-si/360/_workitems/edit/11122) |
| **Codebase** | `core-bl/Source/si-bl-process-platform-build/SI.Biz.Core.ProcessPlatform.RulesEngine/` |
| **MediaWiki** | [Flexibility initiatives](https://wiki.software-innovation.com/wiki/Flexibility_initiatives) |
| **ProductPlan** | [Process Platform](https://app.productplan.com/ZFvmHNxV) |
| **Prototype UI** | https://business-rules-360.lovable.app/ |

---

## Gaps / next steps

- [ ] Fix runtime blockers (ContextEntity + IsEnabled filtering) before pilot
- [ ] Extend RuntimeTests to prove ValidationMessage e2e
- [ ] Sign pilot scope: validation-only, Case OnUpdate, single-decision models
- [ ] Unpark/update ProductPlan BRE bar
- [ ] Copenhagen workshop: align team on ~55% pilot readiness vs epic 2026 target
