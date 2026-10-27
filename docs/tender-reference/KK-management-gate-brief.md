# Københavns Kommune (KK) Plan & Build — management go/no-go brief

**Purpose:** Input for decision gate on continued KK tender work and bid/no-bid.  
**Scope:** ADO query returns **27** work items: foundation epic [#434005](https://dev.azure.com/tieto-si/360/_workitems/edit/434005) + **25** tender PFR Features + placeholder [#429990](https://dev.azure.com/tieto-si/360/_workitems/edit/429990) (excluded from gate). [Query 6d4459e7](https://dev.azure.com/tieto-si/360/_queries/query-edit/6d4459e7-42f4-431d-9e54-68566fed49aa/).  
**Sources:** KK Tender tool (`Timeline` sheet: award and go-live **ukendt**; supplier proposes plan via 4.1.1 / Bilag 1 §5.1), DevOps portfolio, Public 360° roadmap PPT (Q1 2026–Q2 2027), Copenhagen customer discovery (Jun 2026), Epic #434005 estimation table.  
**Last ADO verification:** 18 Aug 2026, 11:22 CET.

---

## Implementation timeline (tender facts)

**There is no fixed go-live date in the tender.** The internal Timeline sheet lists **Award decision: ukendt** and **Go-live: ukendt**.

| What | Tender says |
|------|-------------|
| **Overtagelsesdag** | Milestone in Bilag 1 (Overtagelsesprøve, hypercare, roll-back plan) — **date set by supplier** in detailed implementation plan (Bilag 1 §5.1) |
| **Implementation plan** | Supplier describes in bid — **4.1.1 Implementeringsplan (15% evaluation weight)** |
| **Delay / penalties** | Measured against **supplier's proposed timeline** in Bilag 1 §5.1 (e.g. >20 working days slip on Overtagelsesdag or Driftsprøve) |
| **Driftsprøve** | 30 calendar days after Overtagelsesprøve (B1-15) |
| **Freeze periods** | No go-live activities in **all of July**, **24 Dec–1 Jan**, or Danish public holidays (B1-17) |
| **IT risk approval** | Koncern IT review up to **3 months** — can shift plan if not supplier-caused (Q&A confirms) |

**Internal planning assumption only** (not a tender commitment): if award lands ~Q4 2026, a **~10-month** implementation window is a reasonable bid-planning band — subject to freeze periods and Koncern IT lead time.

---

## ADO query portfolio (27 items)

| Layer | Count | IDs |
|-------|-------|-----|
| **Foundation epic** | 1 | [#434005](https://dev.azure.com/tieto-si/360/_workitems/edit/434005) — PnB Baseline, 200 days |
| **Tender PFR delta** | 25 | 434352, 434878, 434881, 435480–435493, 435495–435499, 435501–435503 |
| **Placeholder (excluded)** | 1 | [#429990](https://dev.azure.com/tieto-si/360/_workitems/edit/429990) — Suggestion for Improvement |
| **Query total** | **27** | |

All 25 tender PFRs are mapped in commitment clusters below. Previously **#435503** (AI Assist option) was missing from the Integration spine cluster — now included (7 PFRs in that cluster).

---

### Q1 — Do we want to open the Danish market?

KK (Københavns Kommune) is the anchor beachhead: largest Danish municipality, ~90 TB, strict GDPR/AI governance, existing eDoc customer. A **yes** commits to a Danish compliance surface (BOM, FilArkiv, servicemål, Digital Post, grunddata, SIEM). A **no** means decline or minimal bid; continue eDoc migration only ([#376382](https://dev.azure.com/tieto-si/360/_workitems/edit/376382) for Ringkøbing-Skjern).

Release planning for Plan & Build in Denmark ([#434336](https://dev.azure.com/tieto-si/360/_workitems/edit/434336)) is **awaiting LT decision by end August 2026**.

### Q2 — Do we migrate Plan & Build into a Public 360° module (360 Flow + fee + GIS + BOM)?

This is **Approach 1** in epic [#434005](https://dev.azure.com/tieto-si/360/_workitems/edit/434005): *P360 with P&B in same setup* — merge P&B from separate product into Public 360°, using **360 Flow** for process modelling, and folding in **fee calculation**, **map/GIS integrations**, BOM, FilArkiv, and Danish case types.

| | Approach 1 (strategic) | Approach 2 (narrow) |
|--|------------------------|---------------------|
| Architecture | P360 with P&B in same setup | P&B subset deployed on P360 DAN |
| **Estimate** | **200 man-days** | 141 man-days |

**A yes on Q2 approves epic #434005** (~200 man-days ≈ 1 FTE × 10 months dev-focused; test/contingency may sit outside). **A no** keeps eDoc/Flow-heavy bid or Approach 2 — harder to meet KK's full byggesags scope.

### Q3 — Given yes/yes, which tender PFR gaps are in the bid baseline?

Only after Q1+Q2: resolve tactical blockers among the **25 query PFRs** (SIEM, tagging, servicemål polish, etc.). These are **on top of** the foundation epic, not a substitute for it.

---

## Foundation investment — Epic #434005

**Title:** Copenhagen Bid - Master Commitment Danish Plan & Build Foundation  
**State:** New · **Tags:** Commitment; Copenhagen Bid · **Child:** [#434006](https://dev.azure.com/tieto-si/360/_workitems/edit/434006) (servicemål/deadlines) · **Related:** [#434009](https://dev.azure.com/tieto-si/360/_workitems/edit/434009) (time registration)

**Approach 1 breakdown (200 man-days):**

| Block | Days | Contents |
|-------|------|----------|
| Integrations | 77 | BOM (15), **fee (8)**, BBR (10), FilArkiv (10), GIS conflict (15), GIS neighbor (15), GIS localization (4) |
| Process models | 40 | 360 Flow process modelling basis |
| UI & database | 53 | P&B case types — BIF + FIB + DB |
| Testing | 30 | Six case-type families (building, supervision, illegality, complaint, estate dividing, request) |
| **Total** | **200** | Plus BIF/subsetup/BL cleanup (sitemaps, transfer jobs, archive admin) |

Several KK PFRs map to foundation scope (BOM, FilArkiv, servicemål, GIS/conflict, fee). Others — especially SIEM ([#435501](https://dev.azure.com/tieto-si/360/_workitems/edit/435501)), log integrity ([#435493](https://dev.azure.com/tieto-si/360/_workitems/edit/435493)), tagging ([#435480](https://dev.azure.com/tieto-si/360/_workitems/edit/435480)) — are **tender delta**, not in the 200-day table.

---

## Executive summary

| Metric | Value |
|--------|-------|
| **Foundation epic** | [#434005](https://dev.azure.com/tieto-si/360/_workitems/edit/434005) — **200 man-days** (Approach 1) |
| ADO query items | **27** (25 PFR delta + #434005 + #429990 placeholder) |
| Tender PFR delta | **25** Features |
| PFR net effort (conservative) | **30–55 months** — **tender delta only**; does **not** include foundation 200 man-days (multi-team; overlap-adjusted within PFRs) |
| Rough total (before PFR/foundation dedupe) | **~40–65 person-months** scoped work, delivered in parallel |
| Implementation timeline | **Supplier-proposed** — no fixed go-live in tender (Timeline: **ukendt**) |
| Internal planning band | **~10 months** from award (assumption only; excludes Jul freeze + IT risk buffer) |
| Team size implied | **3–6 FTE average**, **6–10 FTE peak** (foundation + PFR delta in parallel) |
| Tender-tool gap profile | 3 Not met · 3 Partial · 2 In flight · 17 TBD |
| Roadmap alignment (PFRs) | **A 5 · B 6 · C 11 · D 3** |

**Primary gate questions:** (1) Open Danish market? (2) Approve P&B → P360 module merge ([#434005](https://dev.azure.com/tieto-si/360/_workitems/edit/434005), 200 days, Approach 1)?

**Tactical bid blockers (Q3, if yes/yes):** SIEM LogPoint ([#435501](https://dev.azure.com/tieto-si/360/_workitems/edit/435501)), log integrity ([#435493](https://dev.azure.com/tieto-si/360/_workitems/edit/435493)), tagging module ([#435480](https://dev.azure.com/tieto-si/360/_workitems/edit/435480)).

---

## Roadmap alignment vs KK delivery

**Source:** Public 360° roadmap (PPT, Q1 2026–Q2 2027) mapped against **supplier-proposed Overtagelsesdag** in our bid plan (no fixed customer date). Cluster-owner validation **pending**.

| Status | PFRs | Meaning | DG implication |
|--------|------|---------|----------------|
| **A — On roadmap, aligns with KK delivery** | 5 | Existing roadmap item(s) that align well with a credible bid timeline | Reference existing roadmap in bid narrative |
| **B — On roadmap, needs acceleration** | 6 | Existing roadmap item(s) that must be delivered faster than currently targeted | Core investment conflict — pulls BRE, search, Flow/servicemål forward |
| **C — Off roadmap, strategically relevant** | 11 | New scope not on the roadmap but strategically relevant if we bid | Net-new product bets beyond current roadmap |
| **D — Off roadmap, low priority** | 3 | New scope not on the roadmap and would otherwise not be prioritized | Small or hygiene items; low standalone priority |

### Roadmap alignment share

| Category | PFRs |
|----------|------|
| Aligns with roadmap timing | 5 |
| Needs acceleration | 6 |
| Strategically relevant off-roadmap | 11 |
| Low priority off-roadmap | 3 |

**Headline for DG:** KK is not “deliver planned roadmap on time.” ~24% needs acceleration (B); ~44% is strategically relevant but not on the roadmap (C). Copenhagen discovery (Jun 2026) reinforces AI governance and metadata quality as strategic — aligns with option PFR **435503** but not yet rated in tender tool.

### PFR-level roadmap mapping

| ID | Title | Roadmap | Roadmap reference |
|----|-------|---------|-------------------|
| 434352 | Data delimitation of cases | A — Aligns | Access matrix / dataafgrænsning |
| 434878 | 5.2.11.2 Servicemålstid start/stop | D — Low priority | — (config/milestone) |
| 434881 | 5.2.11.3 Sagsbehandlingstid ikke-BOM | D — Low priority | — (config/milestone) |
| 435480 | 5.2.1.1 Tagging, structuring, sorting | C — Strategic | — |
| 435481 | 5.2.1.2 Conflict resolution | C — Strategic | — |
| 435482 | 5.2.1.3 Flexible journalisation | B — Accelerate | Plan & Build / BOM integration |
| 435483 | 5.2.4.3 Search, sorting, filtering, export | B — Accelerate | Refactor search experience |
| 435484 | 5.2.8.4 / 5.2.12.1 / 5.2.13.2 Process control | C — Strategic | — |
| 435485 | 5.2.8.5 Handling received information | C — Strategic | — |
| 435486 | B2-03 BRE write-back to BOM | A — Aligns | Business Rules Engine |
| 435487 | 5.2.9.1 / 5.2.9.4 BOM search criteria | B — Accelerate | Plan & Build / BOM integration |
| 435488 | 5.2.13.1 Case templates | B — Accelerate | Hosted Processes / Flow |
| 435489 | FilArkiv archive transfer (P&B) | C — Strategic | Archive automation |
| 435490 | B2-12 Danish servicemål deadline model | B — Accelerate | Plan & Build 360 / Flow |
| 435491 | B2-14 Time registration on cases | C — Strategic | — |
| 435492 | 5.3.4.2 Error texts and messages | D — Low priority | — |
| 435493 | 5.3.7.2.6 Log integrity / manual deletion | C — Strategic | — |
| 435495 | B2-18 Integration landscape | C — Strategic | — |
| 435496 | 5.3.8.2.2.1 Master data from registers | A — Aligns | NG Integration API / grunddata |
| 435497 | 5.3.8.2.3 Deep link integrations | A — Aligns | NG Integration API |
| 435498 | 5.3.8.2.7.1.2 Remote print SF1601 | C — Strategic | — |
| 435499 | 5.3.8.2.7.1.4 MeMo Digital Post actions | A — Aligns | Digital Post (in flight) |
| 435501 | B2-20 / SIEM LogPoint delivery | C — Strategic | — |
| 435502 | 5.4.1.1 Debtor system (option) | C — Strategic | — |
| 435503 | 5.4.2.1 AI Assist integration (option) | B — Accelerate | Agentic case management / AI |

---

## Decision paths

### A — Strategic yes (market + product merge)
**Yes to Q1 and Q2:** Approve epic **#434005** (200 man-days, Approach 1 — P&B as P360 module on Flow). Bid KK with foundation + managed PFR delta. Accept **30–55 months** tender PFR effort on top of foundation. Propose a **credible implementation plan** (4.1.1) and staff **3–6 FTE average (6–10 FTE peak)** for the bid timeline. Proceed with release planning ([#434336](https://dev.azure.com/tieto-si/360/_workitems/edit/434336)). Resolve SIEM/tagging via build, partner, or Q&A narrow.

### B — Market yes, product narrow
**Yes to Q1, no or partial on Q2:** Bid with Approach 2 (141 days) or eDoc/Flow-heavy story without full P&B merge. Challenge MK blockers (SIEM, tagging) via ordregiver Q&A. Weaker on full byggesag portfolio; cap FilArkiv and time-registration at delivery-plan responses.

### C — No-bid or low-effort
**No to Q1:** Decline KK or minimal compliance. Defer Danish P&B module; continue eDoc migration track ([#376382](https://dev.azure.com/tieto-si/360/_workitems/edit/376382)) only.

---

## Commitment clusters

| Cluster | Features | Size | Effort (months) | Risk | Gate question |
|---------|----------|------|-----------------|------|---------------|
| Case UX / search / tagging | 5 | L + M | 12–22 | High | Is 435480 (tagging) in scope or out via Q&A? |
| Process control & templates | 2 | M + L | 6–12 | Medium | Case overview + templates: config vs product? |
| BOM + BRE integration | 2 | L | 10–16 | High | B2-03 write-back: BRE pilot ready for KK? |
| Servicemål / deadlines | 3 | XL | 12–20 | High | Danish deadline model at Overtagelsesdag — Flow commit? |
| Time registration | 1 | L | 4–8 | Medium | eDoc reuse or net-new for B2-14? |
| FilArkiv archive | 1 | L | 6–12 | Medium | Merge project scope for P&B → FilArkiv? |
| Integration spine | 7 | XL + L + M | 18–32 | High | Nine grunddata registers all at Overtagelsesdag? Options 435502/435503 in baseline? |
| Security / logging / SIEM | 3 | L | 6–12 | High | LogPoint + log deletion: build, partner, or no-bid? |
| Point fix | 1 | S | <1 | Low | Baseline include |

**PFR IDs by cluster**

- Case UX / search: 435480, 435481, 435482, 435483, 435485
- Process control: 435484, 435488
- BOM + BRE: 435486, 435487
- Servicemål: 434878, 434881, 435490
- Time registration: 435491
- FilArkiv: 435489
- Integration spine: 435495, 435496, 435497, 435498, 435499, 435502, 435503
- Security / SIEM: 434352, 435493, 435501
- Point fix: 435492

---

## Team size vs bid timeline

**Tender:** No fixed Overtagelsesdag — we propose the date in Bilag 1 §5.1. Penalties bind to **our proposed plan**, not a customer-imposed go-live.

**Internal planning band:** ~10 calendar months from award (assumption only). Account for **full July freeze**, **Koncern IT risk review (up to 3 months)**, and **30-day Driftsprøve** after Overtagelsesprøve when drafting the bid timeline.

**Effort math (conservative):** 30–55 months PFR delta ÷ ~10-month planning band ≈ **3–6 FTE sustained average**. Integration spine and servicemål run in parallel → **6–10 FTE peak**.

| Product team | Features | Indicative FTE (10 mo window) | XL Features |
|--------------|----------|-------------------------------|-------------|
| Plan & Build / Process Platform | 8 | **3–5 FTE** | 2 |
| Core Integration | 7 | 2–4 FTE | 1 |
| Core UI / Search | 4 | 1–3 FTE | 0 |
| Tech Platform / CloudOps | 3 | 1–2 FTE | 0 |
| Core BL / Archive | 2 | 1–2 FTE | 0 |
| Options (AI, debtor) | 2 | 0.5–1 FTE | 0 |

Bands overlap across teams — not additive headcount.

---

## Tender-tool gap profile (portfolio PFRs)

| Gap | Count | Notable PFRs |
|-----|-------|--------------|
| Not met | 3 | 435480 (tagging), 435493 (log integrity), 435501 (SIEM) |
| Partial | 3 | 435482 (journalisation/BOM), 435489 (FilArkiv), 435490 (servicemål) |
| In flight | 2 | 434352 (data delimitation), 435499 (MeMo) |
| TBD | 17 | Most IK/MK items not yet rated in tender tool |

**Bid blockers (MK minimum + Not met):** 435493, 435501. **High product risk:** 435480 (internal risk sheet: “unable to meet”).

---

## Hygiene and open actions

- [ ] **LT decision** on Danish market + P&B module by end Aug 2026 ([#434336](https://dev.azure.com/tieto-si/360/_workitems/edit/434336))
- [ ] Link all 25 query PFRs as **Related** to foundation epic **#434005**
- [ ] Set **Impacted Module** on all 25 PFRs (currently unset)
- [ ] Rate 17 TBD PFRs in KK Tender tool (esp. 435484, 435495, 435496)
- [ ] Dedupe servicemål overlap: 434878/434881 vs consolidated 435490 vs child #434006
- [ ] Cluster leads validate roadmap A/B/C/D column
- [ ] CloudOps sign-off on SIEM LogPoint feasibility or Q&A narrow wording

---

## Recommended 60-minute gate agenda

1. **Q1 — Danish market:** in or out (10 min)
2. **Q2 — P&B → P360 module:** approve #434005 / 200 days Approach 1 (15 min)
3. **Q3 — Tender PFR delta:** SIEM, tagging, servicemål blockers (10 min)
4. Roadmap conflict — what gets reprioritised (10 min)
5. Team capacity vs **proposed bid timeline** (10 min)
6. Decision path A / B / C (5 min)

---

## Related artifacts

- **Foundation epic:** [#434005](https://dev.azure.com/tieto-si/360/_workitems/edit/434005) · Release planning [#434336](https://dev.azure.com/tieto-si/360/_workitems/edit/434336) · eDoc parallel [#376382](https://dev.azure.com/tieto-si/360/_workitems/edit/376382)
- Canvases: `canvases/kk-management-gate.canvas.tsx`, `canvases/kk-commitment-heatmap.canvas.tsx`
- PDFs: `docs/tender-reference/export/kk-management-gate.pdf`, `kk-commitment-heatmap.pdf`
- Tender tool: `KK Tender tool.xlsx` (Timeline sheet — go-live **ukendt**)
- Customer context: `toolkit/scripts/_copenhagen_meetings_extract.txt`
- PFR query: [6d4459e7-42f4-431d-9e54-68566fed49aa](https://dev.azure.com/tieto-si/360/_queries/query-edit/6d4459e7-42f4-431d-9e54-68566fed49aa/)
