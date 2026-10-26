# Compliance matrix

Build on day one of the bid. Update when the buyer issues amendments. **Never delete a requirement** — flag gaps instead.

---

## Standard columns

| Column | Purpose |
|--------|---------|
| **Req ID** | Buyer's requirement identifier |
| **Source** | RFP section / page / annex |
| **Requirement text** | Verbatim or faithful extract |
| **Type** | Submission / Technical / Security / Legal / Commercial / Process |
| **Mandatory** | Y (skal/must/shall) / N (bør/should) / Pass-fail |
| **Compliance** | Met / Partial / Alternative / Gap / N/A / Unknown |
| **Owner** | Role or name (Proposal lead, Security SME, Legal, …) |
| **Status** | Not started / Draft / In review / Approved |
| **Response location** | Section, table cell, annex ID |
| **Evidence** | Certificate, help topic, wiki, prior answer path |
| **Win theme** | T1–T5 (optional link) |
| **Notes** | Gaps, Q&A to buyer, dependencies |

---

## Starter template (markdown)

```markdown
# Compliance matrix — [Tender name]

**Buyer:** [name]
**Due:** [date]
**Version:** RFP v[x] + amendments [list]
**Last updated:** [date]

## Win themes

| ID | Theme | Evaluation criterion |
|----|-------|---------------------|
| T1 | [one sentence] | [criterion] |
| T2 | | |
| T3 | | |

## Requirements

| Req ID | Source | Mandatory | Compliance | Owner | Status | Response location | Evidence | Theme | Notes |
|--------|--------|-----------|------------|-------|--------|-------------------|----------|-------|-------|
| 1.1 | Kap 1 | Y | Met | | | Kravtabell 1.1 | | T1 | |
| 1.2 | Kap 1 | Y | | | | | | | |
```

---

## Extraction rules

Treat as **mandatory** when the text includes:

| Norwegian | English |
|-----------|---------|
| skal, må, skal være | shall, must, will (obligation) |
| ikke tillatt, forbudt | shall not, must not |
| vedlegges, dokumenteres | must be attached, documented |

Treat as **desirable** when:

| Norwegian | English |
|-----------|---------|
| bør, kan, ønskelig | should, may, desirable |

**Pass/fail items** (missing attachment, wrong format, unsigned form) get their own rows — they are not "just admin."

---

## Compliance status definitions

| Status | Meaning | Response strategy |
|--------|---------|-------------------|
| **Met** | Fully satisfied today with evidence | Standard affirmative answer |
| **Partial** | Some elements met | State what is met; explain gap; mitigation or roadmap |
| **Alternative** | Different approach, equivalent outcome | Justify equivalence; cite precedent if allowed |
| **Gap** | Not met; no acceptable alternative | Frank disclosure; bid/no-bid input; question to buyer |
| **N/A** | Requirement does not apply to our offer | One-sentence justification |
| **Unknown** | Evidence not yet gathered | Owner + deadline; do not draft final text |

---

## Gap summary (append to matrix)

After first pass, produce:

```markdown
## Gap summary

| Req ID | Severity | Description | Bid impact | Action |
|--------|----------|-------------|------------|--------|
| | Disqualifying / High / Medium / Low | | | Q&A / Legal / No-bid |

## Statistics

- Total requirements: [n]
- Mandatory: [n] — Met: [n], Partial: [n], Gap: [n]
- Open unknowns: [n]
```

---

## Go / no-go scorecard (optional)

Use when user asks for bid qualification. Score 1–5 per criterion; weight by importance.

| Criterion | Weight | Score | Notes |
|-----------|--------|-------|-------|
| Strategic fit | | | |
| Win probability | | | |
| Compliance risk (gaps) | | | |
| Resource / effort | | | |
| Commercial attractiveness | | | |

**Threshold:** User or bid team sets cut-off. Skill does not auto no-bid — presents analysis only.

---

## Amendment handling

When buyer issues change:

1. Add rows for new requirements.
2. Mark changed rows with `Amendment [n]` in Notes.
3. Re-check Response location and Evidence for affected rows.
4. Do not remove old requirement text — strike through and note replacement if useful for audit trail.
