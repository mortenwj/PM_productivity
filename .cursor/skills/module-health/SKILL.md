---
name: module-health
description: >-
  Generates the Module Health Scorecard per MODULE_HEALTH_SPEC.md: bugs (90d by
  ImpactedModule), open PFRs, composite health score and insight tags. Revenue
  is optional (--with-revenue) when financial data is available. Writes
  outputs/portfolio/module_health_YYYY-MM-DD.md. Use when the user asks for
  module health, portfolio scorecard, module scoring, product health, bug/PFR
  pressure by module, or which modules need attention.
---

# Module Health Scorecard

Portfolio scorecard for Public 360 **ImpactedModule** units: **bug load** and **PFR demand** (revenue optional).

## Before you start

1. Read **`toolkit/module-health/MODULE_HEALTH_SPEC.md`** (WIQL, scoring, MCP mapping, output path).
2. Read **`toolkit/module-health/scoring_config.json`** if the user asks how scores are computed.
3. Use **today's date** in the output filename: `outputs/portfolio/module_health_YYYY-MM-DD.md`.

## Default scope (unless the user overrides)

| Item | Value |
|------|--------|
| ADO project | `360` |
| Product team filter | none (all teams) |
| Module filter | none |
| Bug window | 90 days (created) |
| PFR states | New, Active, Pending |
| Revenue | **Off by default** — use `--with-revenue` only when user has live financial data |
| Output | `outputs/portfolio/module_health_YYYY-MM-DD.md` |

**Common overrides:** `--team "Process Platform"`, `--module "Dispatch"`.

## Execution order

1. **Bugs (90d)** — `wit_query` with `action: "wiql"` using the bugs WIQL from the spec (or `references/wiql-templates.md`). **Page to completion.** If response is IDs-only, `wit_get_work_items_batch_by_ids` with fields: `System.Id`, `System.Title`, `System.State`, `Custom.ImpactedModule`, `Microsoft.VSTS.Common.Priority`.

2. **Open PFRs** — Same pattern with PFR WIQL from spec. Fields include `Custom.Customername` when available.

3. **Save scratch** (recommended):
   - `outputs/scratch/module_health_bugs.json`
   - `outputs/scratch/module_health_pfrs.json`

4. **Build scorecard** — MCP `build_module_health_scorecard` (without revenue) or:
   ```powershell
   uv run python toolkit/module-health/build_scorecard.py `
     --bugs outputs/scratch/module_health_bugs.json `
     --pfrs outputs/scratch/module_health_pfrs.json `
     --team "<team if filtered>" `
     --output outputs/portfolio/module_health_YYYY-MM-DD.md
   ```
   Add `--with-revenue` and `--revenue-excel` only when the user explicitly wants financials included.

5. **Summarize in chat** — 2–4 sentences: scope, modules under most pressure, one actionable insight.

## MCP mapping

| Step | Server | Tool |
|------|--------|------|
| WIQL bugs / PFRs | `user-azure-devops` | `wit_query` (`action: "wiql"`) |
| Work item fields | `user-azure-devops` | `wit_get_work_items_batch_by_ids` |
| Merge / score | `module-portfolio` (optional) | `build_module_health_scorecard` |
| Taxonomy | local file | `module_taxonomy.json` |

## Scoring (default — ADO only)

```
Health = 55% bug burden + 45% PFR backlog
```

Higher score = **healthier** (fewer bugs and open PFRs relative to penalties in config).

Insight tags cover quality hotspots, PFR demand, combined pressure, and P1 attention — see `insights_ado_only` in scoring config.

## Output quality

- Link to saved markdown file.
- Call out **data gaps** (partial WIQL page, missing Customername field).
- Only modules with **bugs and/or PFRs** in scope appear (no revenue-driven module list).
- If user asks about **one module**, use `--module` filter or highlight that row from full run.

## Pipeline fit

```
triage-requests → module-health (context) → feature-scoping
```

Use before scoping when the user needs **module-level bug/PFR context**.

## Do not

- Update ADO work items unless explicitly asked.
- Skip WIQL pagination — under-counting bugs/PFRs invalidates the scorecard.
- Load revenue Excel or Power BI unless the user asks for `--with-revenue`.
