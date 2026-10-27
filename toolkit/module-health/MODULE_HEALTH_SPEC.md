# Module Health Scorecard — Spec

Authoritative spec for the **Module Health Scorecard**: portfolio view of **bug load** and **PFR demand** per ImpactedModule. **Revenue is optional** (deferred until live financial data is available).

Say **"module health scorecard"** (or **"module health"**) in Cursor to generate the report.

---

## Purpose

Help Public 360 PMs answer:

- Which modules have **elevated bug volume** or **P1 attention**?
- Where is **open PFR demand** concentrated (count and customer breadth)?
- Which modules are **under combined pressure** (bugs + PFRs)?

When revenue is re-enabled (`--with-revenue`), also: investment vs. maintenance trade-offs.

Scores are **indicative** for portfolio discussion — not capacity or financial truth.

---

## Default scope

| Setting | Default | Override examples |
|--------|---------|-------------------|
| ADO project | `360` | — |
| Product team filter | none (all teams) | `--team "Process Platform"` |
| Module filter | none (all modules) | `--module "Dispatch"` |
| Bug window | Last **90 days** (created) | `scoring_config.json` → `windows_days.bugs` |
| PFR scope | **Open** (New, Active, Pending) | — |
| Revenue | **Off** | `--with-revenue` + `--revenue-excel` |
| Output | `outputs/portfolio/module_health_YYYY-MM-DD.md` | `--output` |

---

## Execution order

1. **Load taxonomy** — `toolkit/module-health/module_taxonomy.json` (module → product team, aliases).
2. **ADO — Bugs (90d)** — WIQL via Azure DevOps MCP; page until complete; batch-get fields if WIQL returns IDs only.
3. **ADO — Open PFRs** — WIQL; page until complete.
4. **Save scratch JSON** (recommended) — `outputs/scratch/module_health_bugs.json`, `module_health_pfrs.json`.
5. **Build scorecard** — `build_scorecard.py` (no revenue by default) or MCP.
6. **Write output** — save markdown; give user a 2–4 sentence summary in chat.

**Revenue (optional, later):** add `--with-revenue` when Excel or Power BI integration is ready.

---

## WIQL templates

Project: **360**. Use `wit_query` with `action: "wiql"`. **Page** with increasing `$skip` or repeat until no new IDs (MCP `top` default 50 — increase to 200 when supported).

### Bugs — last 90 days

```sql
SELECT [System.Id], [System.Title], [System.State],
       [Custom.ImpactedModule], [Microsoft.VSTS.Common.Priority],
       [System.CreatedDate]
FROM WorkItems
WHERE [System.TeamProject] = '360'
  AND [System.WorkItemType] = 'Bug'
  AND [System.CreatedDate] >= @Today - 90
  AND [Custom.ImpactedModule] <> ''
  AND [Custom.ImpactedModule] <> '0 - Not applicable'
ORDER BY [System.CreatedDate] DESC
```

### Open Product First Requests

```sql
SELECT [System.Id], [System.Title], [System.State],
       [Custom.ImpactedModule], [Custom.Customername],
       [System.CreatedDate]
FROM WorkItems
WHERE [System.TeamProject] = '360'
  AND [System.AreaPath] UNDER '360\Product First Requests'
  AND [System.State] IN ('New', 'Active', 'Pending')
  AND [Custom.ImpactedModule] <> ''
  AND [Custom.ImpactedModule] <> '0 - Not applicable'
ORDER BY [System.CreatedDate] DESC
```

After WIQL returns IDs only, batch-get with `wit_get_work_items_batch_by_ids` (≤200 IDs per call):

`System.Id`, `System.Title`, `System.State`, `Custom.ImpactedModule`, `Microsoft.VSTS.Common.Priority`, `Custom.Customername`

If `Custom.Customername` returns **TF51535**, retry without it and note in report **Data notes**.

---

## Scoring model

Config: `toolkit/module-health/scoring_config.json`

### Default — ADO only

| Dimension | Weight | Logic |
|-----------|--------|--------|
| Bug burden | 55% | `100 - min(100, bugs×2 + p1×10)` |
| PFR backlog | 45% | `100 - min(100, open_pfrs×3)` |

**Bands:** Healthy ≥75 · Watch ≥55 · At Risk ≥35 · Review &lt;35

**Insight rules:** quality hotspot, PFR demand, combined pressure, P1 attention — see `insights_ado_only` in config.

### Optional — with revenue (`--with-revenue`)

| Dimension | Weight | Logic |
|-----------|--------|--------|
| Revenue rank | 35% | Percentile rank of YTD revenue among modules in scope |
| Revenue growth | 15% | From Excel `Delta YTD PY` when present |
| Bug burden | 25% | Same as above |
| PFR backlog | 25% | Same as above |

Adjust weights with PM agreement; document changes in git.

---

## MCP tools

### Azure DevOps (`user-azure-devops`)

- `wit_query` — `action: "wiql"` for bugs and PFRs
- `wit_get_work_items_batch_by_ids` — field details

### Module portfolio (`module-portfolio`) — optional local server

| Tool | Purpose |
|------|---------|
| `get_module_taxonomy` | Module → team map |
| `get_scoring_config` | Weights and bands |
| `get_revenue_by_module` | Excel → module revenue |
| `build_module_health_scorecard` | Merge JSON payloads → markdown + scores |

Register in Cursor MCP (stdio):

```json
{
  "module-portfolio": {
    "command": "uv",
    "args": ["run", "python", "toolkit/module-health/module_portfolio_mcp.py"],
    "cwd": "C:/Users/MortenJensen/.cursor/projects/PM_productivity"
  }
}
```

---

## CLI (offline / CI)

```powershell
uv run python toolkit/module-health/build_scorecard.py --dry-run
uv run python toolkit/module-health/build_scorecard.py `
  --bugs outputs/scratch/module_health_bugs.json `
  --pfrs outputs/scratch/module_health_pfrs.json `
  --team "Process Platform" `
  --output outputs/portfolio/module_health_2026-08-04.md
```

---

## Output quality

- Title with **report date** and **scope** (team / module filters).
- **Summary table** — all modules in scope, sorted by health score.
- **Insights** — only modules with triggered rules.
- **Dimension detail** — transparent sub-scores.
- **Data notes** — missing Excel, TF51535 fields, partial ADO paging failures.

---

## Do not rely on

- **`build_scorecard.py` alone** for live ADO — it merges JSON snapshots; the agent must fetch ADO via MCP first (unless user supplies JSON files).

---

## Related assets

| Asset | Path |
|-------|------|
| Skill | `.cursor/skills/module-health/SKILL.md` |
| Scoring reference | `.cursor/skills/module-health/references/scoring-model.md` |
| WIQL reference | `.cursor/skills/module-health/references/wiql-templates.md` |
| Revenue leaderboard | `toolkit/scripts/generate_revenue_leaderboard.py` |
| Module taxonomy source | wiki Module overview / Product Teams |
