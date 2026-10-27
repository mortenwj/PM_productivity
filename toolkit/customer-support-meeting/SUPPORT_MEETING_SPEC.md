# Customer support meeting report – Spec

Generate a meeting-ready Markdown report from a ServiceNow/CIM Excel export of support cases, enriched with Azure DevOps work item links.

Say **"support meeting report"** (or name the skill) in Cursor after placing the Excel file in the workspace.

---

## Inputs (from user each run)

| Item | Default / example | Notes |
|------|-------------------|-------|
| Excel export | user-provided path | ServiceNow/CIM export |
| Teams (`PM_group_main`) | user must specify | e.g. `Core UI`, `Transparency` |
| ADO project | `360` | Override if needed |
| ADO org URL | `https://tieto-si.visualstudio.com` | For work item links |
| Support number field | discover per run | Often `Custom.SupportNumber`, `Custom.Supportnumber`, or `Support number` |

---

## Excel column map (expected)

| Letter | Typical name | Use |
|--------|--------------|-----|
| — | Case / CS number column | Identifier; detect by header or `CS\d+` pattern |
| F | description | Primary text for analysis |
| G | comments | Primary text for analysis |
| H | `PM_group_main` | Responsible team filter |
| — | `PM_group_module` | Module breakdown in summary |
| — | Status / state column | Open vs closed filter |
| J | AI summary | **Do not use** for analysis |

If headers differ, the parser script maps by name; fall back to column letters when names match the export convention.

---

## Output

Write **`outputs/customer-support/{customer-slug}_{YYYY-MM-DD}_support_meeting.md`**

Create the directory if missing. Use a slug from the customer name the user provides (e.g. `oslo-kommune`).

---

## Report structure (Markdown)

```markdown
# Support cases – {Customer} – {date}

## Summary

| Team | Open | Closed | Modules (open) |
|------|------|--------|-----------------|
| … | … | … | … |

## 1. {Team 1}

### 1.1 Closed cases – patterns (context)
Short thematic summary from closed cases only.

### 1.2 Open cases by theme

#### {Theme}
**{CS-number}** – {short title}
{Description from F + relevant G excerpts}

DevOps: [{id}]({url}) | *ikke registrert* | ⚠️ burde vært meldt videre til R&D

Kommentar/vurdering:

### 1.3 Open cases table

| CS | Theme | Module | DevOps |
|----|-------|--------|--------|
| … | … | … | … |

## 2. {Team 2}
(same structure)

## Prioriterte punkter til møtet
- Items needing progress clarification
- Unanswered questions
- Cases without DevOps registration
- DevOps Closed but support still open
- ⚠️ Should have been escalated to R&D
```

---

## Execution order

### Step 1 – Parse Excel

Run:

```powershell
uv run python toolkit/customer-support-meeting/parse_support_export.py --input "<path-to-xlsx>" --output-json outputs/customer-support/_parsed.json
```

Optional team filter:

```powershell
uv run python toolkit/customer-support-meeting/parse_support_export.py --input "<path>" --teams "Core UI" "Transparency" --output-json outputs/customer-support/_parsed.json
```

Read the JSON: column map, row counts, team distribution, open/closed split, case list.

### Step 2 – Generate draft report

Using parsed data (columns F/G, not J):

- One chapter per team
- Open cases grouped into logical sub-themes (agent judgment from F/G text)
- Closed cases: brief pattern summary per team (section 1.1 / 2.1)
- Placeholder `Kommentar/vurdering:` under every open case
- End with **Prioriterte punkter til møtet**

### Step 3 – Team assignment QA

User may request:

- Remove misclassified cases (give full description first, then remove and recalc counts)
- Move case to correct team chapter
- Rename/remove empty theme sections
- Recount: verify summary tables match actual case lists

### Step 4 – Azure DevOps lookup

Use **`wit_query`** with `action: wiql`.

1. Collect all CS numbers from open cases in the report.
2. If support field unknown, run a probe WIQL on one known CS number or ask user for field name from DevOps UI.
3. Batch WIQL (max ~200 CS numbers per query; split if needed):

```sql
SELECT [System.Id], [System.Title], [System.State], [Custom.SupportNumber]
FROM WorkItems
WHERE [System.TeamProject] = @project
AND [Custom.SupportNumber] IN ('CS0001234', 'CS0005678')
```

Try field variants if zero results: `Custom.Supportnumber`, `[Support number]`.

4. Work item link format:

`https://tieto-si.visualstudio.com/{project}/_workitems/edit/{id}`

5. Update report:

- DevOps link under each case in §1.2 / §2.2
- DevOps column in §1.3 / §2.3 tables
- `ikke registrert` when no match

**Mismatch flag:** DevOps state Closed/Resolved but support case still open → add to meeting priorities.

### Step 5 – Flag missing R&D escalation

For cases with **no DevOps match**, read F and G. Flag ⚠️ when text indicates:

- Reproducible / confirmed bug in production or test
- Support acknowledges active bug but not escalated
- Repeated escalation or video evidence without DevOps item

Add ⚠️ note under DevOps line and in meeting priorities.

### Step 6 – Finalize

User fills `Kommentar/vurdering:` placeholders. Save final `.md` to outputs path.

---

## MCP tools

| Purpose | Tool |
|---------|------|
| WIQL search by support number | `wit_query` (`action: wiql`, `project`, `wiql`, `top`) |
| Work item details | `wit_work_item` |
| List projects | `core_list_projects` |

---

## Quick prompts (Norwegian – copy/paste)

**Structure check**

```
Les Excel-filen og fortell meg hvilke kolonner som finnes, antall rader, og noen eksempelrader.
```

**Team overview**

```
Vis alle unike verdier i PM_group_main og antall saker per team.
```

**Generate report**

```
Lag en rapport i Markdown for teamene [Team 1] og [Team 2].
Regler: kun åpne saker i detalj; lukkede som kort bakteppe; grupper etter tema;
bruk kolonne F og G, ikke J; placeholder Kommentar/vurdering under hver sak;
avslutt med Prioriterte punkter til møtet.
```

**DevOps enrichment**

```
Søk i DevOps-prosjektet 360 etter work items der Support number matcher disse CS-numrene: [liste]
Oppdater rapporten med lenker og DevOps-kolonne i tabellene.
```

**Escalation QA**

```
For saker uten DevOps-treff: analyser F og G. Flag ⚠️ der feilen er bekreftet men ikke meldt videre til R&D.
```
