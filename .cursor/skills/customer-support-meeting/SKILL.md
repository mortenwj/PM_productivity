---
name: customer-support-meeting
description: >-
  Analyzes ServiceNow/CIM support case Excel exports for customer meetings:
  filter by PM teams, generate Markdown report from description/comments,
  enrich with Azure DevOps links by support number, flag missing R&D escalation.
  Writes outputs/customer-support/*.md. Use when the user asks for support meeting
  report, supportsak-analyse, kundemøte supportsaker, or pastes the support
  case Excel workflow.
---

# Customer support meeting report

## Before you start

1. Read **`toolkit/customer-support-meeting/SUPPORT_MEETING_SPEC.md`** (authoritative).
2. Ask the user for if missing:
   - Path to Excel export (`.xlsx`)
   - Customer name (for output filename)
   - Their team names in `PM_group_main`
   - ADO project (default `360`) and support-number field if known

## Step 1 – Parse Excel

```powershell
uv run python toolkit/customer-support-meeting/parse_support_export.py --input "<xlsx-path>" --output-json outputs/customer-support/_parsed.json
```

Add `--teams "Team A" "Team B"` when teams are known.

Inspect JSON: columns, team distribution, open/closed counts, case text in `description` / `comments`. **Never use `ai_summary` (column J) for analysis.**

## Step 2 – Draft Markdown report

Write to **`outputs/customer-support/{customer-slug}_{YYYY-MM-DD}_support_meeting.md`**.

Follow structure in the spec:

- Summary table (open/closed per team, modules)
- One chapter per team
- §x.1 closed-case patterns (brief context only)
- §x.2 open cases grouped by theme from F/G text
- `Kommentar/vurdering:` placeholder under each open case
- §x.3 summary table of open cases
- **Prioriterte punkter til møtet**

Use Norwegian section titles if the user works in Norwegian.

## Step 3 – Team QA (interactive)

When the user corrects classification:

1. Before removing a case: quote its report description for forwarding to another PM
2. Remove or move cases; recalculate all counts and tables
3. Remove empty theme sections or rename headings on request

## Step 4 – Azure DevOps enrichment

Use MCP **`wit_query`** with `action: wiql`, `project: 360` (or user override).

Collect CS numbers from open cases. Query support-number field (try `Custom.SupportNumber`, then variants from spec).

Update report:

- Link under each case: `[{id}](https://tieto-si.visualstudio.com/{project}/_workitems/edit/{id})`
- Table DevOps column; `ikke registrert` when no match
- Note DevOps Closed/Resolved but support still open → meeting priority

## Step 5 – R&D escalation flags

For `ikke registrert` cases, analyze F/G. Add ⚠️ when support confirmed reproducible bug / active bug not escalated / repeated escalation without DevOps item.

## Step 6 – Hand off

Tell the user the output path. Remind them to fill `Kommentar/vurdering:` before the meeting.

## Do not

- Rely on AI summary column J for case descriptions
- Skip recount after removing/moving cases
- Invent DevOps IDs — only link confirmed WIQL matches
