# BRE information package

**Purpose:** Consolidated evidence for PRD work (BMad `bmad-prd`) and team alignment.  
**Product:** 360° Business Rules Engine (BRE)  
**Assembled:** 2026-06-16  
**Owner:** Process Platform team

---

## How to use

| File | Contents |
|------|----------|
| [01-purpose-and-vision.md](./01-purpose-and-vision.md) | What BRE is, problems it solves, platform fit |
| [02-customer-scenarios.md](./02-customer-scenarios.md) | Scenario register + first-wave pilot themes |
| [03-devops-snapshot.md](./03-devops-snapshot.md) | Epic #11122 + key features (live ADO 2026-06-16) |
| [04-wiki-snapshot.md](./04-wiki-snapshot.md) | Wiki positioning (cached 2026-06-08; live refresh failed) |
| [05-codebase-snapshot.md](./05-codebase-snapshot.md) | Implementation reality from `core-bl` |
| [06-pilot-readiness-and-gaps.md](./06-pilot-readiness-and-gaps.md) | Pilot verdict, blockers, commitment timeline |
| [07-prd-input-checklist.md](./07-prd-input-checklist.md) | Open questions before drafting the PRD |
| [manifest.json](./manifest.json) | Source lineage, dates, gaps |

**Upstream docs (detail):** [`../`](../README.md) inventory, reverse-engineered PRD, architecture, and [`../sources/`](../sources/).

---

## Source refresh status (2026-06-16)

| Source | Status |
|--------|--------|
| `bre/sources/*` | Ingested |
| Azure DevOps MCP | **Refreshed** — epic #11122 + sample features |
| MediaWiki MCP | **Failed** (403) — using `sources/wiki-and-product.md` |
| `core-bl` codebase | **Scanned** — RulesEngine assembly confirmed |
