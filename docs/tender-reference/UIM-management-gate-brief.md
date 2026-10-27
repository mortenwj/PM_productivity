# UIM ESDH 2026 — management go/no-go brief

**Purpose:** Input for early-week decision gate on continued tender work.  
**Scope:** 27 commitment Features (Related to [ADO #433876](https://dev.azure.com/tieto-si/360/_workitems/edit/433876)).  
**Sources:** UIM ESDH Tender tool (Jul 2026), DevOps portfolio, Public 360° roadmap PPT (Q1 2026–Q2 2027), light product evidence.  
**Last ADO verification:** 17 Aug 2026, 09:44 CET — **+3 new Features** (435597, 435603, 435606) linked to parent.

---

## Executive summary

| Metric | Value |
|--------|-------|
| Commitment Features | **27** (+3 since 14 Aug 2026) |
| Net effort (conservative) | **45–75 months** (FFUI uplift applied; avoid double-counting Search/FFUI overlap; includes test/integration margin) |
| Build window | **~10 months** (award Nov 2026 → build complete 1 Sep 2027) |
| Team size implied | **5–8 FTE average**, **9–14 FTE peak** (multi-squad program) |
| XL Features | 8 |
| Tender-tool gap profile | 11 Not met · 3 Partial · 2 Draft needed · 1 In flight · 10 TBD |
| Roadmap alignment | **A 4 · B 9 · C 11 · D 3** (vs Public 360° roadmap PPT) |
| Award target | ~Nov 2026 |
| Build complete | **1 Sep 2027** |
| Go-live | **Oct 2027** |

**Primary gate question:** Do we strategically commit to **customer-created entities** (PFR **433895** / EK-6) as a platform program?

**Secondary bid blocker:** **MK-77** unbounded search/list results (PFR **435257**).

Without a clear yes/no on the platform spine, bid narrative and resourcing cannot be credible. ~70–80% of portfolio risk and effort sits in the platform spine + Search/FFUI clusters. **435606** (all listviews / all first-level metadata) materially increases FFUI scope beyond prior estimates.

---

## New Features (17 Aug 2026)

| ID | Title | Ref | Cluster | Module | Size | Gap |
|----|-------|-----|---------|--------|------|-----|
| [435597](https://dev.azure.com/tieto-si/360/_workitems/edit/435597) | Configurable rules and validations | EK-5 | Platform spine | Custom fields | L | TBD |
| [435603](https://dev.azure.com/tieto-si/360/_workitems/edit/435603) | Configurable icons | EK-6 | Platform spine | Custom fields | M | TBD |
| [435606](https://dev.azure.com/tieto-si/360/_workitems/edit/435606) | All listviews configurable with all first-level metadata | MK-66+ / EK-3 | Search / FFUI | Search | XL | TBD |

435597 and 435603 are satellites of **433895** (customer entities). 435606 is related to **433882** and overlaps the FFUI/search personalization cluster.

---

## Roadmap alignment vs UIM delivery

**Source:** Public 360° roadmap (PPT, Q1 2026–Q2 2027) mapped against UIM build complete **1 Sep 2027**. Cluster-owner validation pending.

| Status | PFRs | Meaning | DG implication |
|--------|------|---------|----------------|
| **A — On roadmap, aligns with UIM delivery** | 4 | Existing roadmap item(s) that align well timewise with expected delivery (Sep 2027) | Reference existing roadmap in bid narrative |
| **B — On roadmap, needs acceleration** | 9 | Existing roadmap item(s) that must be delivered faster than currently targeted | Core investment conflict — pulls FFUI/search/platform forward |
| **C — Off roadmap, strategically relevant** | 11 | New scope not on the roadmap but strategically relevant if we bid | Net-new product bets beyond current roadmap |
| **D — Off roadmap, low priority** | 3 | New scope not on the roadmap and would otherwise not be prioritized | Small or hygiene items; low standalone priority |

### Roadmap alignment share

| Category | PFRs |
|----------|------|
| Aligns with roadmap timing | 4 |
| Needs acceleration | 9 |
| Strategically relevant off-roadmap | 11 |
| Low priority off-roadmap | 3 |

**Headline for DG:** UIM is not mostly “deliver planned roadmap on time.” ~33% needs acceleration (B); ~41% is strategically relevant but not on the roadmap (C).

### PFR-level roadmap mapping

| ID | Title | Roadmap | Roadmap reference |
|----|-------|---------|-------------------|
| 433895 | Customer entities platform | B — Accelerate | Full Flex UI cont. |
| 433881 | Retention/deletion on all entities | B — Accelerate | Full Flex UI cont. (433895 satellite) |
| 433883 | Mass update on custom entities | B — Accelerate | Full Flex UI cont. |
| 433887 | Configuration import/export | B — Accelerate | Config migration tool |
| 435597 | Configurable rules and validations | A — Aligns | Business Rules Engine |
| 435603 | Configurable icons | D — Low priority | — |
| 433882 | Full Flex advanced search | B — Accelerate | 360° Søkeassistent + Refactor search experience |
| 433884 | Full Flex detail webparts / columns | B — Accelerate | Full Flex UI cont. |
| 435253 | UI personalization | B — Accelerate | Full Flex UI cont. + search refactor |
| 435606 | All listviews / all metadata | B — Accelerate | Full Flex UI cont. + search refactor |
| 435257 | No limit on search/list results | C — Strategic | — |
| 433877 | Hierarchical case collections | C — Strategic | — |
| 435258 | Activities via API | A — Aligns | NG Integration API / 360° API Gateway |
| 433889 | LibreOffice support | A — Aligns | Office alternatives |
| 433891 | Evolution mail client | B — Accelerate | Office alternatives |
| 435203 | Alternative email clients (duplicate) | D — Low priority | — |
| 433894 | UUID across all logging | C — Strategic | — |
| 435333 | Log separation & traceability | C — Strategic | — |
| 433885 | Workflow history report | C — Strategic | — |
| 433886 | Mask definition via web-admin | C — Strategic | — |
| 433888 | Report: entities no user can access | C — Strategic | — |
| 433892 | Failed dispatch notification | C — Strategic | — |
| 433893 | Split large dispatches | C — Strategic | — |
| 435336 | Remote Print configuration | C — Strategic | — |
| 435338 | Dispatch channel (physical mail) | C — Strategic | — |
| 433880 | Duplicate contact prevention | D — Low priority | — |
| 433890 | Archiving datetime in Outlook | A — Aligns | New Outlook Support cont. |

---

## Decision paths

### A — Strategic bid
Commit to 433895 platform spine and FFUI/search roadmap. Accept **45–75 months** net effort and staff **5–8 FTE average (9–14 FTE peak)** through build complete **1 Sep 2027**. Requires multi-team program and executive sponsorship.

### B — Bid with Q&A scope narrow
Submit but challenge MK-77, entity scope, and integration commitments via ordregiver Q&A. Cap XL items at partial/delivery-plan responses.

### C — No-bid or low-effort
Decline or minimal compliance response if platform spine and MK-77 cannot be credibly committed by Nov 2026 award gate.

---

## Commitment clusters

| Cluster | Features | Size | Effort (months) | Risk | Gate question |
|---------|----------|------|-----------------|------|---------------|
| Platform spine | 6 | XL + L + M | 28–45 | High | Is 433895 in or out? |
| Search / FFUI / UI | 6 | XL + M | **25–40** | High | MK-77 commit without product risk? |
| Integrations | 4 | L + S | 10–16 | Medium | Build, partner, or Q&A narrow? |
| Dispatch / Strålfors | 4 | M | 6–12 | Medium | Physical mail in-house or partner? |
| Logging / audit | 2 | L | 4–8 | Medium | Merge MK-20 Features first |
| Admin / workflow / security | 3 | M | 5–10 | Medium | Min requirements vs evaluation? |
| API / activities | 1 | M | 2–5 | Medium | Close EK-12 (377061) before bid lock? |
| Point fixes | 1 | S | <1 | Low | Baseline include |

**PFR IDs by cluster**

- Platform spine: 433895, 433881, 433883, 433887, 435597, 435603
- Search / FFUI: 433882, 433884, 435253, 435257, 433877, 435606
- Integrations: 433889, 433891, 435203, 433890
- Dispatch: 433892, 433893, 435336, 435338
- Logging: 433894, 435333
- Admin: 433885, 433886, 433888
- API: 435258
- Point fix: 433880

---

## Team size vs build deadline

**Build window:** ~10 calendar months from award (~Nov 2026) to build complete (**1 Sep 2027**). Go-live **Oct 2027** — one month for cutover and stabilisation after build complete.

**Effort math (conservative):** 45–75 months net effort ÷ 10 months ≈ **5–8 FTE sustained average**. Platform spine and Search/FFUI run in parallel → **9–14 FTE peak** across product teams.

| Product team | Features | Indicative FTE (10 mo window) | XL Features |
|--------------|----------|-------------------------------|-------------|
| Core UI | 12 | **6–10 FTE** | 8 |
| Core BL and eArchive | 6 | 2–4 FTE | 1 |
| Core Integration | 5 | 2–3 FTE | 0 |
| Process Platform | 1 | 0.5–1 FTE | 0 |
| Tech Platform Team | 2 | 1–2 FTE | 0 |

FTE bands assume parallel delivery within the build window. Totals overlap across teams — not additive headcount. Estimates include integration, test, and contingency — not dev-only. **FFUI/listview work is the main driver of the uplift from prior 35–60 month estimate.**

**Late start risk:** If XL platform work (433895 cluster) does not begin until after award, the effective window shrinks further and peak FTE must rise above 14, or go-live Oct 2027 is not credible.

---

## Product team demand (Impacted Module)

Impacted Module set on all 27 Features (Aug 14–17, 2026).

| Product team | Features | XL Features | Modules |
|--------------|----------|-------------|---------|
| Core UI | 12 | 8 | Search, UI-UX, Webparts, Contact, Custom fields, UI Configuration, Massupdate, Web admin |
| Core BL and eArchive | 6 | 1 | Dispatch, Access matrix, Disposal and Retention |
| Core Integration | 5 | 0 | Integrations, SIF, Outlook client sidepanel |
| Process Platform | 1 | 0 | Workflow |
| Tech Platform Team | 2 | 0 | Logs |

Core UI carries the bulk of XL load (Search Experience + FFUI + Custom fields + universal listviews).

---

## Cluster light scans (for owner sign-off)

### Platform spine — High risk
- **433895 (EK-6/EK-1):** Draft needed. Hub for customer entities + Udlændingeoverblik. Not a single-module feature.
- **433881 (MK-6):** Partial. Retention/deletion on all entities — depends on entity model breadth.
- **433883 (MK-80):** Not met. Mass update on contacts and custom entities.
- **433887 (K-11/K-12):** Not met. Configuration import/export — FFUI config export not available.
- **435597 (EK-5):** TBD. Configurable rules and validations — evaluation criterion; strategic platform capability.
- **435603 (EK-6):** TBD. Configurable icons — admin UI; low market potential but bid-relevant.

### Search / FFUI — High risk
- **433882, 433884, 435253, 435606:** XL cluster overlapping Search Experience / FFUI pilot. **435606** adds universal listview configurability across all views.
- **435257 (MK-77):** Not met. **Bid blocker** — no limit on search/list result counts.
- **433877 (MK-30):** Not met. Hierarchical case collections — medium, Q&A candidate.

### Integrations — Medium risk
- **433889 (K-16):** Not met. LibreOffice — no product support today.
- **433891 / 435203 (K-17):** Not met + duplicate scope. Evolution / alternative mail clients.
- **433890 (MK-145):** Partial. Outlook archiving datetime — small S fix.

### Dispatch — Medium risk
- **433892 (MK-169):** Not met. Failed dispatch user notification.
- **433893 (K-18):** Not met. Split large dispatches.
- **435336 (MK-165), 435338 (MK-167):** TBD. Remote print + physical mail channel (Strålfors assumptions).

### Logging — Medium risk
- **433894 vs 435333:** Both MK-20 family — merge before commitment wording.

### Admin / workflow — Medium risk
- **433885 (MK-99):** Not met. Automatic workflow history document — manual workaround only today.
- **433886 (MK-120):** TBD. Mask definition via web-admin.
- **433888 (MK-133):** Not met. Report on entities no user can access.

### API — Medium risk
- **435258 (EK-12):** In flight via WI 377061. Lowest gate risk if closed before bid lock.

### Point fix — Low risk
- **433880 (MK-56):** Partial. Duplicate contact prevention (~40h ballpark).

---

## Timeline and risk context

- Award ~Nov 2026 leaves **~10 months** to build complete **1 Sep 2027** (go-live **Oct 2027**).
- **45–75 months** net effort requires **5–8 FTE average**, **9–14 FTE peak** — a multi-squad program, not a single team.
- XL platform work must start **in parallel with bid preparation**, not after award, for a credible response.
- **Overlap risk:** Do not double-count months across 433882, 433884, 435253, **435606** and Search Experience / FFUI program roadmaps.

### Hygiene before bid lock
1. Dedupe MK-20: 433894 vs 435333
2. Dedupe K-17: 433891 vs 435203
3. Clarify EK-3 vs FFUI PFR overlap (435253 vs 433882/433884/**435606**)
4. Rate new PFRs (435597, 435603, 435606) in tender tool where TBD

### Portfolio completeness note
The UIM tender tool contains ~356 requirement rows. The **27 Feature set linked Related to #433876** is the product-first commitment portfolio for this gate — not an exhaustive tender mapping. A full gap scan beyond these items is out of scope for this gate.

**Out of scope (not linked to #433876):** older UIM-tagged upgrade-project Features such as 353751, 360628, 360634, 360656, 361021.

---

## Recommended 60-minute agenda

1. **Platform spine in/out (15 min)** — 433895 + satellites (incl. 435597/435603); Custom fields ownership
2. **Bid blockers (10 min)** — MK-77 (435257); min requirements vs evaluation
3. **Roadmap conflict (10 min)** — 9 PFRs need acceleration (B); 11 off-roadmap but strategic (C). What gets reprioritised?
4. **Team capacity (10 min)** — Can we staff 5–8 FTE average (9–14 FTE peak) to build complete 1 Sep 2027? Core UI 6–10 FTE vs Search Experience / FFUI commitments
5. **Decision path A / B / C (15 min)** — Assign bid narrative and Q&A owner
6. **Next artifacts (5 min)** — Cluster owner sign-off; deep cap-check after gate

---

## Related artifacts

- **Cursor canvases:** `uim-management-gate.canvas.tsx`, `uim-commitment-heatmap.canvas.tsx`
- **Tender source:** `docs/tender-reference/source/UIM ESDH Tender tool.xlsx`
- **ADO parent:** https://dev.azure.com/tieto-si/360/_workitems/edit/433876

---

## Open actions (post-gate if bid continues)

- [ ] Cluster leads validate roadmap alignment column (A/B/C/D) per PFR
- [ ] Cluster leads return sign-off column (commit / Q&A / no-bid per cluster)
- [ ] Deep cap-check on XL PFRs (433895 cluster first; then FFUI cluster incl. 435606)
- [ ] Confirm PFR portfolio completeness vs tender minimum requirements
- [ ] ADO query for live portfolio view in gate meeting
