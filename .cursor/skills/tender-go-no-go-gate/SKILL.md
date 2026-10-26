---
name: tender-go-no-go-gate
description: >-
  Builds management-ready tender go/no-go input from ADO PFR portfolios, tender-tool
  gaps, effort bands (months/FTE), and Public 360° roadmap alignment (A/B/C/D).
  Produces Cursor canvases, markdown brief, and PDF exports. Use when preparing a
  tender decision gate, DG/CPTO briefing, bid/no-bid portfolio analysis, or repeating
  the UIM commitment heatmap pattern for another customer tender.
allowed-tools: Read Write Edit Bash Grep Glob
category:
  - productivity
  - analysis
---

# Tender go/no-go gate

Repeatable workflow distilled from the **UIM ESDH 2026** analysis. Goal: **management decision input** (complexity, magnitude, timeline, team size, roadmap conflict) — not deep per-PFR cap-check unless the gate chooses to bid.

Reference implementation: `docs/tender-reference/UIM-management-gate-brief.md`, `canvases/uim-*.canvas.tsx`.

Detailed templates and rubrics: **[reference.md](reference.md)**.

---

## When to use

- User asks for go/no-go, decision gate, DG brief, CPTO portfolio view, or “repeat UIM analysis for [tender]”
- A tender has (or will have) an **ADO parent Feature** linking commitment **PFR Features**
- Award/build/go-live dates are known or assumed

**Not in scope by default:** full tender-tool row-by-row mapping (~300+ requirements), item-level cap-check, pricing, legal review.

---

## Intake (ask or infer)

| Input | Example (UIM) |
|-------|----------------|
| Tender slug | `uim` |
| Customer / tender name | UIM ESDH 2026 |
| ADO parent Feature ID | 433876 |
| Tender tool path | `docs/tender-reference/source/UIM ESDH Tender tool.xlsx` |
| Extracted tender text | `docs/tender-reference/extracted/<file>.txt` |
| Award target | ~Nov 2026 |
| Build complete | 1 Sep 2027 |
| Go-live | Oct 2027 |
| Roadmap source | User PPT path and/or ProductPlan + wiki |
| Portfolio owner / cluster leads | For sign-off column |

Compute **build window months** = calendar months from award to build complete (UIM used **10**).

---

## Workflow checklist

Copy and track:

```
- [ ] 1. ADO portfolio verified (parent + Related Features)
- [ ] 2. Tender-tool gap profile on portfolio PFRs
- [ ] 3. Clusters + conservative effort bands (months)
- [ ] 4. Team size implied (avg + peak FTE)
- [ ] 5. Roadmap alignment A/B/C/D per PFR
- [ ] 6. Canvases updated (management gate + heatmap)
- [ ] 7. Markdown brief + PDF export
- [ ] 8. Hygiene + open actions listed
```

---

## Step 1 — ADO portfolio

**MCP:** `user-azure-devops` → `wit_work_item` (`action: get`, `expand: Relations`).

1. Load parent Feature; collect all **Related** child Features (not hierarchy unless user specifies).
2. Record `LAST_ADO_CHECK` timestamp in artifacts.
3. Hygiene: set **Impacted Module** on every PFR (not `0 - Not applicable` on children).
4. Link orphan tender PFRs to parent with `wit_work_item_link_write` (`action: link`, `type: related`) when user agrees.
5. Note duplicates / overlaps (e.g. K-17 pair, MK-20 pair) for hygiene section.

**Out of scope:** older customer-tagged upgrade Features not Related to parent.

---

## Step 2 — Gap profile

Sources (in order):

1. Tender tool internal ratings (Met / Partial / Not met / Draft) from extracted xlsx txt
2. Light product evidence (Ratatoskr, wiki, code) only where needed for gate blockers
3. **TBD** for new PFRs not yet rated in tender tool

Aggregate counts for UsageBar: Not met · Partial · Draft · In flight · TBD.

Flag **bid blockers** explicitly (minimum requirements with Not met + high product risk).

---

## Step 3 — Clusters and effort

Group PFRs into **8± clusters** (adjust per tender):

| Cluster | Typical content |
|---------|-----------------|
| Platform spine | Customer entities, meta-model, config export |
| Search / FFUI / UI | Search, listviews, personalization, MK-77 |
| Integrations | Office, mail clients, Outlook |
| Dispatch / partner | Physical mail, Strålfors |
| Logging / audit | MK-20 family |
| Admin / workflow / security | Web-admin, workflow reports |
| API / activities | SIF, NG API |
| Point fixes | Small S items |

**Effort rules:**

- Express **net portfolio effort in months**, not person-months as a single number without context
- Include test, integration, contingency — state that explicitly
- **Avoid double-counting** overlapping PFRs and existing programs (FFUI pilot, Search Experience)
- Apply **conservative bands**; uplift FFUI/search when user says estimates feel low
- Derive FTE: `net months ÷ build window months` → avg band; peak band higher when platform + FFUI parallel

Document **XL/L/M/S** at portfolio level (not item estimates in gate phase).

---

## Step 4 — Roadmap alignment (Jenny rubric)

Map **each PFR** to exactly one status. Source: user **Public 360° roadmap PPT** (extract with `toolkit/scripts/extract_pptx_text.py`) and/or ProductPlan.

| Status | Meaning |
|--------|---------|
| **A — Aligns** | On roadmap; timing fits build complete |
| **B — Accelerate** | On roadmap; scope or schedule insufficient for tender |
| **C — Strategic** | Off roadmap; strategically relevant if we bid |
| **D — Low priority** | Off roadmap; unlikely prioritized without tender |

Add columns: `roadmap`, `roadmapRef` (PPT bar name or `—`).

**DG headline:** tender is rarely “deliver planned roadmap on time”; count B + C.

Cluster leads validate before DG; mark **pending** in artifacts.

---

## Step 5 — Canvases (required)

Read **`~/.cursor/skills-cursor/canvas/SKILL.md`** before editing.

**Location:** `PM_productivity/canvases/` (needs `tsconfig.json` + canvas infra). Sync copies to other workspace `canvases/` if user uses multi-root.

### `{slug}-management-gate.canvas.tsx`

- Stats: PFR count, net effort months, avg FTE, award, build complete / go-live
- Callouts: team size vs deadline, ADO check, primary gate question, secondary blockers
- Decision paths A / B / C (strategic bid, Q&A narrow, no-bid)
- Gap UsageBar + **Roadmap alignment** card (UsageBar + table with full A–D headlines)
- Cluster table + light scans for owner sign-off
- Team rollup (Impacted Module → product team FTE bands)
- **Roadmap alignment share:** full-width section with **table first**, then **`horizontal` BarChart** with categories `A · Aligns`, `B · Accelerate`, `C · Strategic`, `D · Low priority` — **never** use vertical bar chart for four categories in a narrow column (labels get dropped)

### `{slug}-commitment-heatmap.canvas.tsx`

- `PFR_ROWS` with gap, risk, phase, owner, **roadmap**, **roadmapRef**
- Filters: cluster + roadmap status
- Roadmap UsageBar + horizontal bar chart
- Sort: magnitude XL first, then gap severity

Embed all data inline; no fetch.

---

## Step 6 — Markdown brief + PDF

**Path:** `docs/tender-reference/{TENDER}-management-gate-brief.md`

Sections: executive summary (incl. roadmap A/B/C/D counts), new PFRs, roadmap alignment table + **Roadmap alignment share** table, decision paths, clusters, team size, cluster scans, agenda (include **roadmap conflict** slot), related artifacts, open actions.

**PDF export:** adapt `toolkit/scripts/export_uim_canvas_pdfs.py` for the new slug (PFR_ROWS + brief path), or generalize script. Run:

```powershell
uv run python toolkit/scripts/export_uim_canvas_pdfs.py
```

**Markdown → HTML table rules** (if using simple converter): skip separator rows with `is_table_separator()`; do not treat blank lines after rows as skipping the row itself.

Outputs: `docs/tender-reference/export/{slug}-management-gate.pdf`, `{slug}-commitment-heatmap.pdf`

---

## Step 7 — Gate meeting pack

**60-minute agenda template:**

1. Platform spine in/out (15 min)
2. Bid blockers (10 min)
3. **Roadmap conflict** — what gets reprioritised if we bid (10 min)
4. Team capacity vs build window (10 min)
5. Decision path A / B / C (15 min)
6. Next artifacts (5 min)

Deliverables for CPTO/DG: PDFs or published canvases + one-paragraph headline (effort, FTE, B+C share, primary gate question).

---

## Starting a new tender (file naming)

Replace `uim` / `UIM` with `{slug}` / `{TENDER}`:

| Artifact | Pattern |
|----------|---------|
| Brief | `docs/tender-reference/{TENDER}-management-gate-brief.md` |
| Gate canvas | `canvases/{slug}-management-gate.canvas.tsx` |
| Heatmap canvas | `canvases/{slug}-commitment-heatmap.canvas.tsx` |
| Export PDFs | `docs/tender-reference/export/{slug}-*.pdf` |
| Roadmap extract | `docs/tender-reference/extracted/{roadmap-file}.txt` |

Copy UIM canvases as templates; rename constants (`PARENT_ID`, `PORTFOLIO_COUNT`, dates, clusters, `PFR_ROWS`, `ROADMAP_SUMMARY`).

---

## Quality bar

Before handing to management:

- [ ] Portfolio count in brief matches ADO Related links
- [ ] Roadmap table has **all four** A–D rows with full headlines (not abbreviated)
- [ ] Horizontal roadmap chart shows all four labels
- [ ] Effort/FTE math uses stated build window
- [ ] Overlap / double-count called out for FFUI/search clusters
- [ ] Cluster sign-off still **pending** unless leads confirmed

---

## Related skills

- **`pfr-ai-capability-check`** — deep per-PFR sizing **after** gate chooses to bid
- **`tender-response`** / tender-reference library — bid wording, not this gate
- **`canvas`** — canvas UI rules
- **`feature-scoping`** — earlier discovery; this skill is pre-bid **commitment** portfolio

---

## UIM reference anchors

| Item | Value |
|------|-------|
| Parent ADO | 433876 |
| Portfolio | 27 Features (Aug 2026) |
| Net effort | 45–75 months |
| FTE | 5–8 avg, 9–14 peak |
| Roadmap | A4 · B9 · C11 · D3 |

Use as calibration when estimating band widths for similar ESDH/platform tenders.
