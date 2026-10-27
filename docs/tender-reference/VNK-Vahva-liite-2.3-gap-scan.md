# VNK-Vahva — Liite 2.3 domain-by-domain gap scan

**Tender:** VN Asia (Valtioneuvoston kanslia / Valtori) · **Liite 2.3** toiminnalliset vaatimukset  
**Date:** 4 Sep 2026  
**Method:** Section-level assessment (A–P) against Public 360° standard product, Finnish subsetup patterns, registered ADO PFRs, and Innovation Board deck. **Not** a row-by-row cap-check — indicative bands for gate planning.  
**Scale:** Met · Mostly met · Partial · Significant gap · Not met (Pakollinen rows weighted higher than Vertailtava).

---

## Executive summary

| Metric | Value |
|--------|-------|
| Total requirements | **487** |
| Pakollinen (bid rejection if “Ei”) | **416** |
| Vertailtava (scoring) | **68** |
| Unknown / unclassified type | **3** |
| Domains assessed | **16** (A–P) |
| **Indicative Pakollinen posture** | **~45% Met/Mostly met · ~40% Partial · ~15% Significant gap/Not met** |
| Registered PFRs covering Liite 2.3 | **9** (~2% of rows) |
| **Highest-risk domains (Pakollinen)** | **A, C, F, K, P** (+ **O** single mandatory) |
| Domains with ADO PFR | **B, E, H (narrow), I, partial F** |

**Headline:** Standard Public 360° likely covers **core ESDH** (documents, versions, basic workflow, search baseline, contacts, retention concepts) at **Met/Mostly met** for a large share of rows. The bid risk concentrates in **Finnish-specific governance** (TOS/SÄHKE2, hävitys, publication), **multi-organisation government model**, **eIDAS advanced signing**, **Suomi.fi**, **API-first depth**, **offline**, and **process/rules engine** depth — most of which have **no PFR** today.

---

## Rating legend

| Rating | Meaning for Pakollinen rows |
|--------|----------------------------|
| **Met** | Credible “Kyllä” on standard product + FI subsetup without product change |
| **Mostly met** | >70% of section met; gaps are config, partner, or narrow product deltas |
| **Partial** | Material gaps; mix of config + product; several “Ei” risks if answered honestly |
| **Significant gap** | Domain needs substantial product investment or explicit phased delivery |
| **Not met** | No credible path without new program / partner |

---

## Domain scan matrix

| Sec | Domain (FI) | Reqs | Pak | Vert | Overall | Est. Pakollinen mix (M / P / G) | ADO PFR | Bid risk |
|-----|-------------|------|-----|------|---------|----------------------------------|---------|----------|
| **A** | Asianhallinta | 36 | 32 | 4 | **Partial** | 55% / 30% / 15% | — | **High** |
| **B** | Asiakirja & dokumentti | 89 | 75 | 14 | **Mostly met** | 65% / 28% / 7% | 433271, 433354, 433356 | Medium |
| **C** | Hyväksyminen & allekirjoitus | 27 | 24 | 3 | **Significant gap** | 40% / 35% / 25% | — | **High** |
| **D** | Työnkulut | 16 | 14 | 2 | **Mostly met** | 60% / 35% / 5% | — | Medium |
| **E** | Toimeksiannot & jakelut | 65 | 55 | 10 | **Partial** | 50% / 40% / 10% | 430271, 432904, 430291, 433271 | Medium–High |
| **F** | Metatiedot / TOS | 111 | 95 | 16 | **Significant gap** | 35% / 45% / 20% | 430281 | **High** |
| **G** | Arkistointi | 9 | 8 | 1 | **Partial** | 45% / 45% / 10% | — | Medium |
| **H** | Seulonta & hävitys | 13 | 11 | 2 | **Partial** | 50% / 40% / 10% | 433356 (narrow) | Medium |
| **I** | Haku | 50 | 42 | 8 | **Partial** | 55% / 38% / 7% | 434693 | Medium |
| **J** | Raportointi & tilastot | 15 | 12 | 3 | **Partial** | 45% / 45% / 10% | — | Medium |
| **K** | Julkaisu | 17 | 14 | 3 | **Significant gap** | 40% / 40% / 20% | — | **High** |
| **L** | Virtuaalikansiot | 4 | 4 | 0 | **Mostly met** | 75% / 25% / 0% | — | Low |
| **M** | Hallintapalvelut | 20 | 17 | 3 | **Partial** | 55% / 40% / 5% | — | Medium |
| **N** | Mobiili | 6 | 5 | 1 | **Partial** | 35% / 50% / 15% | — | Medium |
| **O** | Offline | 1 | 1 | 0 | **Not met** | 0% / 0% / 100% | — | Medium |
| **P** | Prosessimoottori | 8 | 8 | 0 | **Significant gap** | 30% / 50% / 20% | — | **High** |

*G = Significant gap + Not met combined for Pakollinen rows.*

---

## Section detail

### A — Asianhallinta (Case management) · 36 reqs · **Partial** · Risk: **High**

**Pakollinen themes**
- Multi-organisation cases (A2–A7): several ministries on one case, equal vs primary responsibility, cross-ministry pending register — **Significant gap** for native multi-tenant org model.
- EU/NATO case segregation (A36) — **Partial** (access groups + case types; needs FI security model).
- Suomi.fi viranomaisviestintä (A15) — **Not met** (no PFR; integration program).
- Open APIs (A12–A14) — **Partial** ([#437273](https://dev.azure.com/tieto-si/360/_workitems/edit/437273)).
- Process-to-process case spawn (A21) — **Partial** (workflow + case templates; chaining depth unclear).
- Auto-registration from integrations (A11) — **Mostly met** with integration layer.

**Met/Mostly met (examples):** create/copy case (A17–A19), relations (A29–A31), case number rules (A24–A26), reopen closed (A22), invalidate not delete (A23).

**Gap if team only tracked RFI PFRs:** entire section largely **unregistered**.

**Gate action:** Decide multi-org as **config + services** vs **product program**; register PFR or Q&A narrow for A2–A7; Suomi.fi PFR mandatory for honest A15.

---

### B — Asiakirja & dokumentin hallinta · 89 reqs · **Mostly met** · Risk: **Medium**

**Largest section by row count.** Core document lifecycle is P360 strength.

| Theme | Refs | Rating | PFR / notes |
|-------|------|--------|-------------|
| Mass import/export/edit | B2, B7–B10, B30, B43 | **Partial** | [#433271](https://dev.azure.com/tieto-si/360/_workitems/edit/433271) |
| Template filter by org/class | B58 | **Partial** | [#433354](https://dev.azure.com/tieto-si/360/_workitems/edit/433354) |
| Draft version disposal | B66 | **Partial** | [#433356](https://dev.azure.com/tieto-si/360/_workitems/edit/433356) |
| M365 save-in / Teams import | B6–B8, B13 | **Mostly met** | Office integration; mass paths gap |
| Structured docs / co-editing | B52–B55, B20–B21 | **Partial** | FFUI / Office co-authoring |
| Versioning (500+ versions) | B61–B62 | **Met** | Standard |
| EU language versions | B85–B88 | **Partial** | Metadata + doc model |
| EU/NATO classification marks | B89 | **Partial** | Security labels |

**Residual Pakollinen risk:** mass paths and template filtering in **FI subsetup** (not document-category-first flow).

---

### C — Hyväksyminen & allekirjoittaminen · 27 reqs · **Significant gap** · Risk: **High**

| Theme | Refs | Rating |
|-------|------|--------|
| Internal approval / endorsement flows | C1–C20 | **Mostly met** |
| Mass signing | C17 | **Partial** |
| **eIDAS advanced electronic signature** | C21, C27 | **Not met / Significant gap** |
| External counterparty signing | C27 | **Not met** without qualified trust service partner |

Internal puolto/hyväksyminen ≠ qualified e-sign. Finnish law reference (617/2009) implies **strong e-ID + advanced signature** — likely partner (e.g. Signicat/Digidentity) + product integration, not config.

**No ADO PFR.** This is a **bid blocker cluster** if answered “Kyllä” without architecture.

---

### D — Työnkulkujen hallinta · 16 reqs · **Mostly met** · Risk: **Medium**

Workflow engine covers approval chains, delegation, substitutes (D13), auto-start from integration (D12), cross-org workflows (D5).

**Partial:** org-spanning workflow visibility, publication hooks in workflow (D9), fine-grained parallel/sequential approver selection (D7–D9) — mostly configuration depth.

Overlaps **P-section** for rules engine (see P).

---

### E — Toimeksiannot & jakelut · 65 reqs · **Partial** · Risk: **Medium–High**

| Theme | Refs | Rating | PFR |
|-------|------|--------|-----|
| Work queues, assignments | E1–E20 | **Mostly met** | — |
| Notifications & alerts | E21–E38 | **Partial** | 432904, 430291 |
| Email metadata in subject/body | E45–E47 | **Partial** | 432904 |
| Secure mail / TL marking | E44–E45 | **Partial** | — |
| Mass dispatch | E48–E49 | **Partial** | 430271, 433271 |
| Outlook calendar sync | E30 | **Partial** | — |
| Distribution lists / keywords | E3–E4, E55–E65 | **Mostly met** | — |

**Dispatch redispatch model** (Innovation Board) maps to E41/E48 area — [#430271](https://dev.azure.com/tieto-si/360/_workitems/edit/430271).

---

### F — Metatiedot / TOS & tiedonohjaus · 111 reqs · **Significant gap** · Risk: **High**

**Largest section.** Finnish TOS (tiedonohjaussuunnitelma) + SÄHKE2 + retention/disposal rules.

| Theme | Refs | Rating | PFR |
|-------|------|--------|-----|
| SÄHKE2 / legal metadata set | F3 | **Partial** | FI subsetup |
| Unlimited / configurable fields | F5, F12–F13 | **Mostly met** | — |
| **FI/SV/EN metadata language** | F2 | **Partial** | [#430281](https://dev.azure.com/tieto-si/360/_workitems/edit/430281) |
| Field length | F20 | **Partial** | 430281 |
| Inheritance case→document | F22, B15 | **Partial** | 430281 |
| **Record-type change / publicity safety** | B50, F21 | **Partial** | 430281 (deck slide 9 — **bid blocker** if silent) |
| Mass metadata edit | F23 | **Partial** | 433271 |
| Hierarchical picklists | F16–F17 | **Partial** | Slide 14 — **no PFR** |
| Conditional mandatory metadata | F21 | **Partial** | Slide 14 — BRE overlap |
| Full TOS lifecycle in product | F7–F111 | **Significant gap** | Retention plans, tehtäväluokka, disposal calc F109 |

**One PFR (#430281) vs 111 rows** — team coverage **<5%** of section surface.

---

### G — Arkistointi · 9 reqs · **Partial** · Risk: **Medium**

- National Archives / pitkäaikaissäilytys (G1, G6) — **Partial** (archive connectors; **SÄHKE2 siirtotiedosto** Finnish-specific).
- Transfer package proposal workflow (G3–G5) — **Partial**.
- Zip auto-extract (G2) — **Mostly met**.
- No PDF-only archive mandate (G9) — **Met**.

Often delivered with **archive partner + integration**, not pure product.

---

### H — Seulonta & hävitys · 13 reqs · **Partial** · Risk: **Medium**

Retention calculation (H1), screening, hävitysesitys workflow (H3–H12) — P360 has disposal/retention but Finnish **hävitysesitys** process may need tailoring.

[#433356](https://dev.azure.com/tieto-si/360/_workitems/edit/433356) covers **draft file version** disposal only (B66 overlap) — not full H-section.

---

### I — Hakutoiminnot · 50 reqs · **Partial** · Risk: **Medium**

Strong baseline search (content + metadata, Boolean, permissions I7, saved searches I21–I23, export I41).

| Gap theme | Refs | Rating | PFR |
|-----------|------|--------|-----|
| Single wildcard convention | I27 | **Partial** | [#434693](https://dev.azure.com/tieto-si/360/_workitems/edit/434693) |
| Cross-org saved search share | I32–I33 | **Partial** | 434693 |
| Third-party search engine attach | I49 | **Mostly met** | Elasticsearch |
| Ontology browse | I46 | **Not met** | Niche |
| Synonym rules | I50 | **Partial** | — |
| FFUI list personalization | I38–I39 | **Partial** | FFUI program |

~42 Pakollinen — majority **Met/Mostly met**; gaps cluster on **wildcard, sharing scope, ontology**.

---

### J — Raportointi & tilastot · 15 reqs · **Partial** · Risk: **Medium**

Ad-hoc report builder (J4, J11), all-metadata reports (J1), org-hierarchical reports (J9–J10), diaariote (J3), visual dashboards (J15).

P360 reporting exists but **self-service report designer** depth and **Finnish diaariote** format may be **Partial**. BI export (J13) — integration path.

---

### K — Julkaisu · 17 reqs · **Significant gap** · Risk: **High**

Publication to intranet/internet/extranet (K1–K6), mass publication (K8), scheduling (K11), structured doc partial publish (K17), TLIV rules (K10).

Publication module exists but Finnish **viranomaisjulkaisu** + TLIV + mass/scheduled publish across security classes is **heavy**. **No PFR.**

---

### L — Virtuaalikansiot · 4 reqs · **Mostly met** · Risk: **Low**

Virtual folders, ACLs, multi-folder membership without copies — aligns with P360 case folders / collection concepts. Config-heavy.

---

### M — Hallintapalvelut · 20 reqs · **Partial** · Risk: **Medium**

| Theme | Rating |
|-------|--------|
| Cross-org ACL (M8) | **Partial** — ties to A-section |
| Metadata-driven access (M9–M11) | **Mostly met** |
| Contact register + API (M12–M16) | **Mostly met** |
| Substitutes (M17) | **Met** |
| Secure workstation restriction (M18) | **Not met** — client/policy, not product |
| UX loading indicators (M20) | **Met** (Vertailtava) |

---

### N — Mobiilikäyttö · 6 reqs · **Partial** · Risk: **Medium**

360 mobile exists; N4 mandates broad mobile workflow (approve, sign, queues, comments). **N3** mobile qualified signing — **Significant gap** (ties to C). TLIV-only mobile restriction (N1) — config.

---

### O — Offline · 1 req · **Not met** · Risk: **Medium**

O1: offline document authoring with templates, metadata, sync — **no standard P360 offline client**. Single Pakollinen row but explicit.

**Options:** Q&A narrow, phased delivery, or partner — not credible “Kyllä” at award without plan.

---

### P — Prosessimoottori · 8 reqs · **Significant gap** · Risk: **High**

BPM depth: subprocesses, parallel, long-running, external resources (P2), **rules engine with simulation & impact analysis** (P6–P7), exception/escalation (P8).

360 Flow + BRE cover **part** but full **toimintasääntömoottori simulointi** reads above current Flow maturity. Overlaps D-section.

**No PFR.** Strategic overlap with Copenhagen Flow investment.

---

## Cross-domain themes (not visible in single section)

| Theme | Sections | Rating | PFR |
|-------|----------|--------|-----|
| **API-first / integrations** | A12–A14, B83, M15, I49 | **Partial** | 437273 |
| **Suomi.fi** | A15 | **Not met** | — |
| **eIDAS / strong sign** | C21, C27, N3 | **Not met** | — |
| **Multi-org government** | A2–A7, M8, D5, I32 | **Significant gap** | — |
| **SÄHKE2 + TOS** | A1, F3, G6 | **Significant gap** | 430281 (slice) |
| **Mass operations** | B, E, F23, K8 | **Partial** | 433271 |
| **Security / TLIV** | B89, K, M18, N1 | **Partial** | Liite 2.6 separate |
| **FFUI / Full Flex documents** | B, I38, slide 14 | **Partial** | Roadmap |

---

## Pakollinen risk heatmap (416 rows — indicative)

| Risk band | Est. Pakollinen rows | % | Domains |
|-----------|---------------------|---|---------|
| Credible **Kyllä** (Met/Mostly met) | ~185–200 | 45–48% | B, D, L, parts of I, M, E |
| **Kyllä with config/services** (Partial) | ~155–170 | 37–41% | A, E, F, G, H, I, J, N |
| **Ei / phased / partner** (Significant/Not met) | ~55–70 | 13–17% | C, F, K, P, O, A15, A2–A7 |

**Vertailtava (68 rows):** lower bid risk — can answer “Ei” without rejection; used for quality points.

---

## Comparison: team PFR coverage vs Liite 2.3

| ADO PFR | Primary sections | Rows touched (approx.) | Section coverage |
|---------|------------------|------------------------|------------------|
| 437273 | A12–A14 | 3+ | API slice only |
| 430281 | F, B50 | 15–25 | << F total (111) |
| 433271 | B, E, F23 | 20–30 | Mass subset |
| 434693 | I27, I32–I33 | 3–5 | << I total (50) |
| 430271, 432904, 430291 | E | 10–15 | << E total (65) |
| 433354 | B58 | 1 | Single req |
| 433356 | B66, H | 2–3 | Narrow |

**Unregistered high-impact sections:** **A** (multi-org), **C** (eIDAS), **K** (publication), **P** (process engine), **O** (offline), **G** (SÄHKE2 archive).

---

## Recommended next steps

1. **Tender tool pass** — Import Liite 2.3 into rated matrix (UIM/KK pattern); validate this scan per row for top-risk domains (A, C, F, K, P).
2. **Create PFRs or explicit Q&A positions** for: Suomi.fi (A15), eIDAS (C21/C27), multi-org (A2–A7), publication baseline (K), process/rules (P6–P8).
3. **PoC scope map** — Map Liite 3.1.1 käyttötapaukset to sections; anything not in PoC must go to Product Backlog (per Liite 3.1).
4. **Cluster owner review** — 2-hour pass: F (Willy), C (signing partner), A (Olga/integration), K (publication), P (Flow/BRE).

---

## Related artifacts

- [VNK-Vahva management gate brief](./VNK-Vahva-management-gate-brief.md)
- Liite 2.3 extract: `extracted/vnk-vahva/aRFQ Liite 2.3 VN Asia toiminnalliset vaatimukset.txt`
- Epic [#436815](https://dev.azure.com/tieto-si/360/_workitems/edit/436815)
