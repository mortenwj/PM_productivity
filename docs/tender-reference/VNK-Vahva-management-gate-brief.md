# VNK-Vahva (VN Asia) — management go/no-go brief

**Purpose:** Input for decision gate on continued Finnish government tender work (Valtioneuvoston kanslia / Valtori — VN Asia).  
**Scope:** Epic [#436815](https://dev.azure.com/tieto-si/360/_workitems/edit/436815) + **9** VN Asia–tagged commitment Features (8 linked to epic; **#430291** orphan).  
**Sources:** Liite 2.3 toiminnalliset vaatimukset (487 reqs), Liite 2.6 tietoturva, Innovation Board deck (`Bid_InnovationBoardPMSession.pptx`), FI API requirements brief, Neuvottelukutsu, PoC liite 3.1, Public 360° roadmap PPT (Q1 2026–Q2 2027).  
**Last ADO verification:** 4 Sep 2026, 00:10 CET.

---

## Executive summary

| Metric | Value |
|--------|-------|
| Registered commitment Features | **9** (8 on epic + 1 orphan) |
| Tender functional requirements (Liite 2.3) | **487** (416 Pakollinen · 68 Vertailtava) |
| PFR coverage of tender matrix | **~2%** by row count — RFI gaps only |
| Net effort — **registered PFR portfolio** | **55–90 months** (overlap-adjusted; API + metadata dominate) |
| Net effort — **full tender surface** (indicative) | **120–200+ months** if all Pakollinen gaps treated as product commits |
| Build window (planning assumption) | **~18 months** after contract (PoC → Rakentamisvaihe 1; supplier proposes detail) |
| Team size implied (PFR portfolio) | **4–6 FTE average**, **8–12 FTE peak** |
| XL Features | 1 (#437273 API) |
| Portfolio gap profile (RFI evidence) | 0 Not met · **9 Partial** · 0 Draft · 0 In flight · 0 TBD |
| Roadmap alignment (9 PFRs) | **A 1 · B 4 · C 4 · D 0** |
| Procedure | Competitive negotiation — Tietoevry shortlisted (Neuvottelukutsu Mar 2026) |
| PoC gate | PoC success required before Rakentamisvaihe 1; gaps → Product Backlog per Liite 3.1 |

**Primary gate question:** Do we strategically commit to **API-first / new SIF** ([#437273](https://dev.azure.com/tieto-si/360/_workitems/edit/437273)) as the Finnish government integration spine — knowing Liite 2.3 has **416 mandatory** functional requirements and the registered portfolio covers only RFI-era gaps?

**Secondary bid blockers (no PFR yet):** **Suomi.fi** (A15, Pakollinen), **eIDAS advanced signing** (C21/C27), **multi-organisation case model** (A2–A7), **TLIV security matrix** (Liite 2.6).

Without a clear yes/no on API platform + honest PoC gap disclosure, the bid cannot be credible against Fujitsu / Innofactor / Twoday.

---

## Implementation timeline (tender facts)

| What | Tender says |
|------|-------------|
| **Procedure** | Kilpailullinen neuvottelumenettely (hankintalaki 1397/2016 §36) |
| **PoC** | Mandatory gate; missing standard functionality → implementation plan + UI mockup + roadmap (Liite 3.1) |
| **Build phases** | PoC → (decision) → Rakentamisvaihe 1 → further phases per contract |
| **Go-live** | **Supplier proposes** in implementation plan (no fixed date in negotiation pack) |
| **Evaluation** | Price 40–60% · Quality 40–60% (functionality, experts, delivery model) |

**Internal planning assumption only:** PoC ~6 months + Rakentamisvaihe 1 ~12 months = **~18-month** product-delivery band for gate FTE math.

---

## ADO portfolio (epic #436815)

| Layer | Count | IDs |
|-------|-------|-----|
| **Epic** | 1 | [#436815](https://dev.azure.com/tieto-si/360/_workitems/edit/436815) — Finnish bid requirements for autumn |
| **Child Feature** | 1 | [#433354](https://dev.azure.com/tieto-si/360/_workitems/edit/433354) — template filtering |
| **Related Features** | 7 | 430271, 430281, 432904, 433271, 433356, 434693, 437273 |
| **Orphan (VN Asia tag, not on epic)** | 1 | [#430291](https://dev.azure.com/tieto-si/360/_workitems/edit/430291) — email configurability (overlaps #432904) |
| **Portfolio total** | **9** | |

**Innovation Board deck (21 Aug 2026):** covers 8 PFRs; **#437273** added post-session (24 Aug). Slide 14 lists four themes **without PFRs** (see unregistered gaps).

---

## Strategic layering

### Q1 — Do we want the Finnish government market?

VN Asia is the anchor: Valtioneuvoston kanslia + Valtori, TLIV confidentiality, Katakri audit at PoC, EU/NATO case segregation. A **yes** commits to Finnish compliance surface (SÄHKE2, turvallisuusluokitus, Suomi.fi, domestic cloud options). A **no** means decline or minimal negotiation participation.

### Q2 — Do we commit to API-first as the integration spine?

**[#437273](https://dev.azure.com/tieto-si/360/_workitems/edit/437273)** + FI API brief describe REST/JSON API-first, webhooks, async jobs, SIEM-ready audit, Elasticsearch — aligned with Liite 2.3 A12–A14 (Pakollinen) but **far beyond** current SIF scope.

| | Strategic API commit | Config/integration-only bid |
|--|----------------------|-----------------------------|
| **Covers** | A12–A14, external UIs, AI agents, SIEM | Point integrations via existing tools |
| **Estimate** | **35–55 months** (cluster) | Lower product, higher services risk |
| **Risk** | Roadmap collision, multi-team program | “No” on mandatory API depth at final tender |

**A yes on Q2** approves #437273 as a platform program, not a single Feature.

### Q3 — Given yes/yes, which RFI PFR deltas + unregistered gaps are in the bid baseline?

Only after Q1+Q2: resolve the **9 registered PFRs** and decide which **487-row** domains are met by standard product vs require new PFRs (Suomi.fi, eIDAS, multi-org, workflow engine, Liite 2.6 security).

---

## Tender complexity vs registered portfolio

### Liite 2.3 section scale

| Section | Domain | Reqs | Pakollinen (approx.) |
|---------|--------|------|----------------------|
| A | Case management (multi-org, EU/NATO) | 36 | ~32 |
| B | Document management | 89 | ~75 |
| C | Approval & eIDAS signing | 27 | ~24 |
| D | Workflows | 16 | ~14 |
| E | Assignments, dispatch, notifications | 65 | ~55 |
| F | Metadata / TOS | **111** | ~95 |
| G | Archiving | 9 | ~8 |
| H | Screening & disposal | 13 | ~11 |
| I | Search | 50 | ~42 |
| J–P | Reporting, publication, admin, mobile, process engine | 71 | ~60 |
| **Total** | | **487** | **416** |

### Unregistered gaps (high risk — no ADO PFR)

| Theme | Tender refs | Innovation Board | Gap stance |
|-------|-------------|------------------|------------|
| Suomi.fi viranomaisviestintä | A15 Pakollinen | Slide 14 | **No PFR** — integration L |
| eIDAS advanced e-signature | C21, C27 Pakollinen | — | **No PFR** — L/XL |
| Multi-org / ministeriö case model | A2–A7, A36 | Slide 11–13 | **No PFR** — config + product L/XL |
| Hierarchical metadata picklists | F16–F17 | Slide 14 Primary | **No PFR** — M |
| Conditional mandatory metadata | F21, B50 | Slide 14 | Partial via #430281 infosec story |
| Full Flex UI for documents | — | Slide 14 | **No PFR** — ties to FFUI program |
| Security matrix | Liite 2.6 (V1/V2) | — | **Parallel compliance** — not in PFR set |

---

## Roadmap alignment vs VN Asia delivery

**Source:** Public 360° roadmap (PPT, Q1 2026–Q2 2027) vs **~18-month** planning band. Cluster-owner validation **pending**.

| Status | PFRs | Meaning | DG implication |
|--------|------|---------|----------------|
| **A — On roadmap, aligns with delivery** | 1 | Existing roadmap item(s) align with expected delivery | Reference in bid / PoC narrative |
| **B — On roadmap, needs acceleration** | 4 | Must be delivered faster than currently targeted | Core investment conflict |
| **C — Off roadmap, strategically relevant** | 4 | New scope not on roadmap but relevant if we bid | Net-new product bets |
| **D — Off roadmap, low priority** | 0 | Would not otherwise be prioritized | — |

### Roadmap alignment share

| Category | PFRs |
|----------|------|
| Aligns with roadmap timing | 1 |
| Needs acceleration | 4 |
| Strategically relevant off-roadmap | 4 |
| Low priority off-roadmap | 0 |

**Headline for DG:** VN Asia PFR set is **89% B+C** (8/9). The tender itself is mostly standard ESDH — the risk is **under-registration**, not over-commitment on ADO.

### PFR-level roadmap mapping

| ID | Title | Cluster | Size | Gap | Roadmap | Roadmap reference |
|----|-------|---------|------|-----|---------|-------------------|
| 437273 | 360° API requirements | API / integration platform | XL | Partial | C — Strategic | NG Integration API / 360° API Gateway (scope >> roadmap) |
| 430281 | Metadata (language, length, inheritance, infosec) | Metadata / TOS | L | Partial | B — Accelerate | Custom fields / metadata model |
| 433271 | Mass functions | Mass operations | L | Partial | B — Accelerate | Mass update / bulk operations |
| 434693 | Search enhancements, wildcard, sharing | Search / FFUI | L | Partial | B — Accelerate | Refactor search experience |
| 433354 | Template filtering (FI/SV subsetup) | Templates / document UX | M | Partial | B — Accelerate | Full Flex UI cont. / templates |
| 430271 | Enhanced dispatch | Dispatch / notifications | L | Partial | C — Strategic | Dispatch / redispatch |
| 432904 | Enhanced email notifications | Dispatch / notifications | M | Partial | A — Aligns | New Outlook Support / notifications |
| 430291 | Email configurability | Dispatch / notifications | M | Partial | C — Strategic | — (overlap #432904) |
| 433356 | Draft file version disposal | Archiving / disposal | M | Partial | C — Strategic | Retention / disposal |

---

## Decision paths

### A — Strategic bid
Commit to Q1+Q2: API-first platform (#437273) + deliver registered PFR portfolio through PoC and Rakentamisvaihe 1. Accept **55–90 months** net PFR effort; staff **4–6 FTE average (8–12 FTE peak)**. Register missing PFRs for Suomi.fi, eIDAS, multi-org before final tender. Executive sponsorship for metadata (F-section) and security (Liite 2.6).

### B — Bid with Q&A / PoC scope narrow
Participate in negotiation; use PoC to prove standard product on subset of Liite 2.3. Challenge API breadth, eIDAS, and Suomi.fi via ordregiver Q&A. Cap #437273 at phased delivery plan. Merge #430291 into #432904.

### C — No-bid or low-effort
Decline or minimal compliance if API spine and mandatory A15/C21 cannot be credibly committed before final tarjouspyyntö.

---

## Commitment clusters (registered PFRs)

| Cluster | Features | Size | Effort (months) | Risk | Gate question |
|---------|----------|------|---------------|------|---------------|
| API / integration platform | 1 | XL | **35–55** | High | Is #437273 in or out? |
| Metadata / TOS | 1 | L | 12–22 | High | Does #430281 cover F-section or only RFI subset? |
| Mass operations | 1 | L | 8–14 | Medium | Mass metadata + bulk export — product or services? |
| Search / FFUI | 1 | L | 8–14 | Medium | Wildcard unification + cross-org search share |
| Dispatch / notifications | 3 | L+M | 10–18 | Medium | Redispatch model + merge 430291/432904 |
| Templates / document UX | 1 | M | 3–6 | Low | FI subsetup template filter — config sufficient? |
| Archiving / disposal | 1 | M | 4–8 | Medium | Draft disposal generic vs FI customization |
| **Portfolio total** | **9** | | **55–90** | High | Overlap-adjusted; excludes unregistered tender domains |

---

## Tender gap heatmap (domain level — not all have PFRs)

| Domain | Liite 2.3 reqs | ADO PFR | Indicative product gap |
|--------|----------------|---------|------------------------|
| API / integrations | A12–A14 + I/O | #437273 | Partial — XL |
| Metadata / TOS | F (111) | #430281 | Partial — large residual |
| Mass / bulk | B7–B10, E48, C17 | #433271 | Partial |
| Search | I (50) | #434693 | Partial |
| Dispatch / notify | E21–E47 | #430271, #432904, #430291 | Partial |
| Templates | B58 | #433354 | Partial |
| Draft disposal | B66, H | #433356 | Partial |
| Multi-org cases | A (36) | — | **Unregistered** |
| eIDAS signing | C (27) | — | **Unregistered** |
| Suomi.fi | A15 | — | **Unregistered** |
| Security | Liite 2.6 | — | **Unregistered** |
| Workflows / process | D, P | — | **Unregistered** |

---

## Team size rollup (Impacted Module TBD on most PFRs)

| Team | Modules | PFRs | XL | FTE band |
|------|---------|------|-----|----------|
| Core Integration / API | SIF, NG API, webhooks, SIEM | 1 | 1 | 3–5 FTE |
| Core BL / metadata | Custom fields, TOS, inheritance | 2 | 0 | 2–4 FTE |
| Core UI / Search | Search, FFUI, templates | 2 | 0 | 2–3 FTE |
| Dispatch / Office | Dispatch, notifications, Outlook | 3 | 0 | 1–3 FTE |
| Archive / retention | Disposal, draft versions | 1 | 0 | 1–2 FTE |

**Hygiene:** Set **Impacted Module** on all 9 PFRs; link **#430291** to epic; dedupe email PFR pair.

---

## 60-minute gate agenda

1. **Q1 — Finland market** (10 min)
2. **Q2 — API-first commit** (#437273) (15 min)
3. **Tender surface vs 9 PFRs** — Liite 2.3 + unregistered gaps (15 min)
4. **PoC strategy** — what we prove vs backlog (10 min)
5. **Roadmap conflict** — B+C share (5 min)
6. **Decision paths A / B / C** (5 min)

---

## Related artifacts

- **Liite 2.3 domain gap scan:** [VNK-Vahva-liite-2.3-gap-scan.md](./VNK-Vahva-liite-2.3-gap-scan.md)
- Epic: [#436815](https://dev.azure.com/tieto-si/360/_workitems/edit/436815)
- Canvases: `canvases/vnk-vahva-management-gate.canvas.tsx`, `canvases/vnk-vahva-commitment-heatmap.canvas.tsx`
- PDFs: `docs/tender-reference/export/vnk-vahva-management-gate.pdf`, `vnk-vahva-commitment-heatmap.pdf`
- Tender source: `docs/tender-reference/source/vnk-vahva/`
- Extracted text: `docs/tender-reference/extracted/vnk-vahva/`
- Innovation Board deck: `Bid_InnovationBoardPMSession.pptx` (extracted `.txt`)
- API brief: `API-requirements-FI-market.docx`

---

## Open actions

| # | Action | Owner |
|---|--------|-------|
| 1 | Link **#430291** to epic #436815 | Jani / PM |
| 2 | Merge or dedupe **#430291** vs **#432904** | Product |
| 3 | Create PFRs for **Suomi.fi**, **eIDAS**, **multi-org** (or document as config-only) | Finnish bid team |
| 4 | Rate Liite 2.3 in tender tool (currently no team tool — gap vs UIM/KK) | Bid team |
| 5 | Cluster leads validate roadmap A–D column | Jenny / module owners |
| 6 | Security: map Liite 2.6 V1/V2 to product vs services | Security architect |
| 7 | Set Impacted Module on all 9 PFRs | PFR owners |
