# Tender go/no-go gate — reference

## PFR row schema (heatmap canvas)

```typescript
type PfrRow = {
  id: number;
  ref: string;           // tender req id, e.g. EK-6, MK-77
  title: string;
  cluster: string;
  module: string;        // Impacted Module
  magnitude: "XL" | "L" | "M" | "S";
  gap: "Not met" | "Partial" | "Draft needed" | "TBD" | "In flight";
  risk: "High" | "Medium" | "Low";
  phase: "Gate decision" | "Q&A / clarify" | "Build if bid";
  owner: string;
  roadmap: RoadmapAlign;
  roadmapRef: string;    // PPT initiative name or "—"
  note?: string;
};

type RoadmapAlign =
  | "A — Aligns"
  | "B — Accelerate"
  | "C — Strategic"
  | "D — Low priority";
```

## Roadmap summary table (management canvas)

Use **full headlines** in the Status column (not abbreviated):

| Status | PFRs | Meaning | DG implication |
|--------|------|---------|----------------|
| **A — On roadmap, aligns with UIM delivery** | n | Existing roadmap item(s) that align well timewise with expected delivery | Reference existing roadmap in bid narrative |
| **B — On roadmap, needs acceleration** | n | Existing roadmap item(s) that must be delivered faster than currently targeted | Core investment conflict |
| **C — Off roadmap, strategically relevant** | n | New scope not on the roadmap but strategically relevant if we bid | Net-new product bets |
| **D — Off roadmap, low priority** | n | New scope not on the roadmap and would otherwise not be prioritized | Small or hygiene items |

Replace “UIM delivery” with `{build complete month/year}` for other tenders.

### Mapping heuristics (Public 360° PPT)

Common PPT initiative names → typical alignment:

| PPT / strategic initiative | Often maps to |
|----------------------------|---------------|
| Full Flex UI cont. | B (scope wider than tender PFR) |
| 360° Søkeassistent / Refactor search experience | B |
| Config migration tool | B (export/import may exceed) |
| Business Rules Engine | A or B |
| NG Integration API / 360° API Gateway | A |
| Office alternatives / New Outlook Support | A or B |
| Customer entities / platform spine | B or C |
| MK-77 unbounded results | C (architecture change) |
| Dispatch / Strålfors / logging MK-20 | C |
| Duplicate-contact S fixes | D |

Always validate with cluster lead; mark **pending** in artifacts.

---

## Magnitude bands (portfolio level, conservative)

| Tier | Indicative band | Notes |
|------|-----------------|-------|
| XL | Multi-team platform; cluster totals often 25–45 months net | Overlap-adjusted |
| L | 4–8 months | |
| M | 2–5 months | |
| S | <1 month | |

FFUI/search clusters: bias **high** when tender includes listviews, personalization, and Search Experience overlap.

---

## FTE derivation

```
avg_FTE_low  = net_months_low  / build_window_months
avg_FTE_high = net_months_high / build_window_months
peak_FTE     = avg_high + parallel-program uplift (platform + FFUI)
```

State explicitly: bands overlap across teams — not additive headcount.

---

## Decision paths (wording template)

**A — Strategic bid:** Commit to [platform spine / key XL cluster]. Accept [net months] and staff [avg FTE] ([peak FTE]) through build complete [date]. Requires multi-team program and executive sponsorship.

**B — Bid with Q&A scope narrow:** Submit but challenge [blockers] via ordregiver Q&A. Cap XL items at partial/delivery-plan responses.

**C — No-bid or low-effort:** Decline or minimal compliance if [primary gate question] cannot be credibly committed by award gate.

---

## Canvas chart rules

1. **Roadmap share:** table + `horizontal` BarChart only
2. Categories: `A · Aligns`, `B · Accelerate`, `C · Strategic`, `D · Low priority`
3. Height ≥ 220px for four horizontal bars
4. Do **not** put roadmap vertical bar chart inside a 3-column grid middle column
5. Row tone by roadmap: A=success, B=warning, C=danger, D=neutral

---

## ADO MCP quick reference

```text
wit_work_item          action: get, id, project: 360, expand: Relations
wit_work_item_link_write  action: link, updates: [{ id, linkToId, type: related, comment }]
```

Project: `360`, parent area: `Product First Requests`.

---

## Roadmap PPT extract

```powershell
uv run python toolkit/scripts/extract_pptx_text.py "C:\path\to\roadmap.pptx" "docs/tender-reference/extracted/roadmap-slug.txt"
```

Slide 4–5 of Public 360° roadmap typically list initiative names and Q1 2026–Q2 2027 horizon.

---

## PDF export adaptation

Copy `toolkit/scripts/export_uim_canvas_pdfs.py` → `{slug}_export_gate_pdfs.py` or parameterize:

- `BRIEF_MD` path
- `PFR_ROWS` dict list (include `roadmap`, `roadmap_ref`)
- Output stems: `{slug}-management-gate`, `{slug}-commitment-heatmap`
- `is_table_separator()` for markdown tables (fix header row + last row before blank line)

---

## Brief markdown sections (order)

1. Title + purpose + scope + sources + last ADO check
2. Executive summary table
3. New Features (if any)
4. Roadmap alignment vs delivery (summary table + share table + PFR mapping table)
5. Decision paths
6. Commitment clusters
7. Team size vs build deadline
8. Product team demand
9. Cluster light scans
10. Timeline and risk context
11. Recommended agenda
12. Related artifacts
13. Open actions

---

## Hygiene follow-ups (template)

- Dedupe overlapping PFR pairs (document IDs)
- Clarify FFUI/search overlap across PFR IDs
- Rate TBD PFRs in tender tool
- Link orphan Features to parent
- Cluster leads validate roadmap A/B/C/D column
