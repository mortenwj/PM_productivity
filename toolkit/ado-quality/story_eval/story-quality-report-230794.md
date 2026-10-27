# User story quality report

**Evaluated (UTC):** `2026-03-30T14:59:20.490685+00:00`

## Scope

| | |
|---|---|
| Team | Core-Process-platform |
| Iteration | PP - 22 - 16.03.2026 - 03.04.2026 |
| Work item types | User Story |
| Stories evaluated | 1 |
| Filter (work item IDs) | 230794 |

## Evaluation notes

- Automated heuristic scoring from System.Description, Microsoft.VSTS.Common.AcceptanceCriteria, System.Parent, Microsoft.VSTS.Common.Risk, and Custom.Riskdescription.
- Risk classification uses Microsoft.VSTS.Common.Risk (1–3). Risk description uses Custom.Riskdescription when risk is 1 or 2.

## Aggregate summary

| Metric | Value |
|--------|-------|
| Count | 1 |
| Avg final score | 91.6 |
| Non-compliant | 0 |

### Top systemic issues

- Unset or invalid Microsoft.VSTS.Common.Risk; populate Risk (1–3) and Risk description when risk is 1–2.
- Many standard stories deviate from strict As a / I want / so that and Gherkin AC; see per-item issues.

### Quick wins

- Add Given/When/Then to Acceptance Criteria field for stories with bullets-only AC.
- Shorten or split very large descriptions that look like multi-sprint specs.

## Story summary

| ID | Title | Score | Status | Parent Feature/Epic | Format | AC | Risk | Parent |
|---:|---|---:|:---|:---:|:---:|:---:|:---:|:---:|
| [230794](https://dev.azure.com/tieto-si/360/_workitems/edit/230794) | PE Designer Component - Create a Milestone | 91.6 | Compliant | Yes | 100 | 100 | 100 | 100 |

## Non-compliant detail (issues)
