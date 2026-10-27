# Product team objectives — refresh workbook (2026–2027)

**Purpose:** Team-by-team working document for the objective cycle. **Phase A:** retire or merge what is completed, obsolete, or duplicate. **Phase B:** first stab at **2–3 objectives per team** anchored in the [strategy brief](team-objectives-strategy-brief-2026.md), with explicit pull from **UIM** and **Copenhagen discovery**.

**Status:** Draft for LPM + QCLT — not ProductPlan edits until workshops sign off.  
**Parent:** [Strategy brief](team-objectives-strategy-brief-2026.md) · [Proposal summary](team-objectives-proposal-2026.md) · [Agent appendix](agent-strategy-appendix-d7.md) · **QCLT pack:** [qclt-objectives-alignment-pack-2026.md](qclt-objectives-alignment-pack-2026.md)  
**ProductPlan snapshot:** 44 objectives listed (Sep 2026); team names from ProductPlan teams API.

**How to use**

1. Walk one team section in a workshop; agree **Phase A** actions (archive in ProductPlan after QCLT).
2. Refine **Phase B** titles and draft KRs (not written here — next pass).
3. Record disagreements in the **Open** column; resolve **D1 phasing** (award vs no-award capacity) and **D3** before locking Core UI and Process Platform KRs.

**Phase B — how to read shaped objectives**

Each objective below uses the same skeleton LPMs should refine in workshops:

| Field | Purpose |
|-------|---------|
| **Outcome** | What materially changes for customers, bids, or platform credibility |
| **Draft KRs** | Measurable themes (LPMs add dates, thresholds, evidence) |
| **Depends on / Enables** | Explicit cross-team contracts |
| **AI Software Factory** | Where governed delivery (spec → review → test → ship) applies — see [QCLT pack §6](qclt-objectives-alignment-pack-2026.md) |

Teams may rewrite wording; **keep dependency and factory gates** unless QCLT reconvenes.

**Legend — Phase A actions**

| Action | Meaning |
|--------|---------|
| **Retire** | Archive in ProductPlan; outcome delivered or no longer a team OKR |
| **Merge** | Archive after moving intent into a consolidated objective |
| **Keep** | Stays as-is or becomes a KR under a consolidated objective |
| **Defer** | Archive or pause until bid/program gate (KK, international, etc.) |
| **Re-home** | Wrong team slot today — move ownership then merge |

**Naming:** Existing ProductPlan objectives are referenced by **title**, not numeric ID. Proposed cycle IDs (**CU1**, **CO1**, …) stay as agreed shorthand for new objectives.

---

## Company-wide objectives (Phase A → CO refresh)

| Current objective (ProductPlan) | Phase A | Rationale |
|--------------------------------|---------|-----------|
| Get product ready for further growth | **Replace** | Becomes **CO1 Platform-ready for growth** (UIM, fit-to-standard, spine, merger) — rewrite KRs, do not stack a fourth company theme |
| Improve the Desirability of our Product | **Replace** | Becomes **CO2 Desirable, accessible case handling** (Copenhagen, NAV, NPS) |
| Accelerating AI adoption (proposed) | **Replace** | Becomes **CO3 Governed AI on the case platform** — drop immature placeholder KRs |
| Succeed with eDoc product merger by Q2 2026 | **Keep** | Program overlay; team objectives contribute KRs, not duplicate merger OKRs |
| Develop product capabilities to support continuation of Nordic Public 360° Online migrations and further growth | **Keep / fold** | Fold measurable KRs under **CO1** (online readiness, migration enablers) |
| RDF adaption layer | **Keep / fold** | Company RDF trajectory; **Collect CE2** owns team slice |
| *Improve internal tools used by consultants*; *Refactor IFAR module to React*; archived design system / chat / Management Reporting API objectives (see appendix) | **Archived in ProductPlan** | See [Archived objectives — achievement vs disposition](#archived-objectives--achievement-vs-disposition); do not un-archive — carry forward only where noted |

### Phase B — proposed company objectives (first stab)

| ID | Objective | UIM / Copenhagen hook (draft KR themes) |
|----|-----------|-------------------------------------------|
| **CO1** | **Platform-ready for growth** | D1 spine chartered; config portability **433887** via **CE1** (Collect owner, Core BL supporting); fit-to-standard KR; eDoc merger on track; RDF customer count |
| **CO2** | **Desirable, accessible case handling** | WCAG methodology live; desirability baselined; Flow/PE usability for reference customers (Copenhagen AST/KK) |
| **CO3** | **Governed AI on the case platform** | Governance layer; agent platform MVP; 2 native reference agents; hosting offer **D9b/c** (AI & Insights lead) |

---

## Core UI

**Strategic pull:** UIM **433895** platform spine, MK-77 search/list; Copenhagen WCAG + PE desktops; eDoc UI merge (*eDoc general functionality merge*). Config **433887**: **CE1** (Collect owner; Core BL supporting).

### Phase A — current ProductPlan

| Current objective (ProductPlan) | Action | Rationale |
|-------------------------------|--------|-----------|
| Flexible user interface (FFUI) | **Merge → CU1** | KRs at 0% while UIM implies multi-squad programme — reframe as **platform spine**, not generic FFUI label |
| eDoc general functionality merge | **Merge → CU3** (+ TR2) | Shared program with Transparency; avoid duplicate team OKRs |
| Accessibility support | **Merge → CU2** | Part 1 (NAV go-live Jan 2025) **treat as complete** — retire NAV-specific KR; keep **methodology by design** under CU2 |

### Phase B — shaped objectives (draft for LPM refinement)

**Workshop open:** **D1 phasing** — UIM offer delivered; customer decision pending. **No-bid is off the table.** If **no award**, agree **roadmap phasing** for spine/MK-77 vs merger peak; CU1 **direction** unchanged.

#### CU1 — Credible platform spine and modern case UI (FFUI + BIF→React)

**Outcome:** Customers and evaluators can treat 360° as a **configurable platform** (entities, lists, search, admin-defined behaviour via BRE) with a **credible path off legacy BIF** — not a collection of one-off UI projects.

**Depends on:** **PP2 BRE** (flexibility/EK-5); **Core BL** spine/logging/file services; **CE1** for config portability (Collect owner).

**Enables:** **CO1**, **INT1**, **PP2**; UIM/DSS bid narrative; **CO2** via modern detail UX (**433884**).

| Track | Theme |
|-------|--------|
| **A — Platform spine** | Customer-created entities, list metadata, search/list/mass-update |
| **B — BIF→React (factory)** | Governed modernisation of webparts and detail sections |

**Draft KRs — Track A (spine)**

1. **Spine programme:** Milestone plan for **433895** scope (entities, relationships, admin-extensible model) with bid-aligned “existing vs roadmap” evidence.  
2. **Search & lists:** Deliver phased **MK-77** capability per **D1/D2**; include **search refactoring** that reduces list/report pain (*Operational Reporting* incremental path).  
3. **Integration with flexibility:** Demonstrate end-to-end “admin configures without vendor code” on at least one spine scenario **blocked on PP2 BRE** — dated joint milestone with Process Platform.  
4. **Cross-team enablers:** Named dates for **Core BL** retention/dispatch/logging dependencies; no duplicate config OKR (**CE1** owns **433887**).

**Draft KRs — Track B (AI Software Factory + CU1)**

5. **Factory gate:** No production BIF→React work without signed **acceptance criteria + test strategy**; PR review by named human owner (AI does not self-merge).  
6. **Methodology pilot:** Document **rewrite-in-place vs recreate** outcome on one webpart slice (quality, effort, a11y, maintainability) — default approach for scale.  
7. **Files section pilot:** Production-quality **React Files** on case/document detail (design-system components, Excel export, column model) — evidence pack for factory program.  
8. **Factory metrics (baseline cycle):** Track review hours and rework on pilot slices vs pre-factory baseline; report to factory program owner (no company-wide efficiency % yet).  
9. **Scale (H2):** Prioritised % of BIF surfaces on roadmap with factory playbook + **CU2** WCAG/design-system checks.

**Why one CU1 objective:** Same FFUI/modern-stack outcome; preserves 3-objective cap with **CU2** and **CU3**.

---

#### CU2 — Accessible, desirable case handling by design

**Outcome:** WCAG and UX quality are **predictable in delivery**, not rescue work at go-live — supporting NAV/HSØ, Copenhagen AST/KK/NB, and **CO2**.

**Depends on:** Design QA discipline; **CU1** shipping modern UI through the same gates.

**Enables:** All customer-facing modules; tender WCAG claims; factory **a11y validation** on agent-generated UI.

**Draft KRs**

1. **WCAG operating model:** Definition-of-done for UI includes automated + manual a11y checks; exceptions recorded with remediation date.  
2. **Baseline & trend:** Desirability metrics (e.g. critical-task clicks, load time on reference flows) baselined on NVE/Oslo-class journeys; improvement targets for cycle.  
3. **Reference journeys:** AST/KK/NB-relevant flows reviewed with documented gaps and dated fixes (coordination with **PP1/PP2** PE usability).  
4. **Factory role:** Mandatory a11y gate on **CU1 Track B** outputs; publish checklist for other teams using factory on UI.

---

#### CU3 — eDoc UI ready for merger and Danish growth

**Outcome:** Shared **eDoc general functionality** UI (templates, searches, notifications, journal patterns) is **merge-ready with Transparency** and supports Q2 2026 merger trajectory.

**Depends on:** **TR2**, **INT2**; secondary to **CU1** spine unless merger on critical path.

**Enables:** eDoc company objective; **PNB2** Danish references; **KK** UI expectations.

**Draft KRs**

1. **Merge scope map:** Single cross-team backlog (CU3/TR2) with ownership per capability area — no duplicate merge OKRs.  
2. **Template & FFUI merge:** Milestones for case templates and FFUI parity agreed with Transparency for Online.  
3. **Quality bar:** User-facing merge features pass **CU2** a11y/UX gates before release.  
4. **Factory (optional):** Use factory spec/test assist only for bounded merge slices with regression evidence — not a separate objective.

---

## Process Platform

**Strategic pull:** Flow **6.11 GA**, NVE, Collect–Flow; **Business Rules Engine (BRE)** as the enabler of **admin-configurable flexibility** (UIM **EK-5**, KK write-back, fit-to-standard); Copenhagen **PE usability**. **Platform spine and FFUI flexibility for UIM/Copenhagen depends on BRE delivery** — not a parallel optional track. **IFAR (*Refactor IFAR module to React*):** no team OKR this cycle.

### Phase A — current ProductPlan

| Current objective (ProductPlan) | Action | Rationale |
|-------------------------------|--------|-----------|
| Business Rules Engine | **Merge → PP2 (lead theme)** | *Business Rules Engine* anchor — platform flexibility OKRs start here |
| Web-based process modelling | **Merge → PP2** | Supports Copenhagen **D3**; secondary to BRE |
| Visual representation of process steps | **Merge → PP2** | UIM workflow history / templates; secondary to BRE |
| Refactor IFAR to React (archived) | **Drop as OKR** | Not achieved; remain archived — no **PP3/TR3** handover objective in this refresh |

### Phase B — shaped objectives (draft for LPM refinement)

#### PP1 — Flow and PAF production-grade through 6.11 GA

**Outcome:** **NVE** and reference customers run integrated **case + process** on a **stable, documented** Flow/PAF runtime — Copenhagen can sell an integrated story, not runtime experiments.

**Depends on:** **PNB** webparts/maps; **CE2** Collect–Flow; **CU2** UX on process surfaces.

**Enables:** **CO2**, **PNB2**, **CE2**; AST/KK process–case narrative.

**Draft KRs**

1. **6.11 GA:** Release criteria met (stability, upgrade path, known-issue budget) with NVE sign-off or agreed exception plan.  
2. **Operational readiness:** Runbooks, monitoring, and support model for Flow/PAF in production at reference customers.  
3. **Collect integration:** Dated Collect–Flow scenarios required for NVE/RDF on production path (**CE2** alignment).  
4. **Documentation & enablement:** Implementer/consultant documentation sufficient for Oslo-class go-live (**PNB2**).  
5. **Factory (optional):** AI-assisted test generation or spec refinement for **regression-heavy Flow areas** — bounded slices with human-reviewed tests only.

---

#### PP2 — Business rules and process flexibility customers can own

**Outcome:** Admins configure **validations, rules, and process behaviour** without vendor code — unlocking **CO1 fit-to-standard**, **UIM EK-5**, KK BRE, and **CU1** credibility.

**Depends on:** **CU1** for desktops/webparts that surface rules; honest bid narrative with sales.

**Enables:** **CU1**, **CO1**, UIM/DSS; Copenhagen **D3** (PE maintains models).

**Draft KRs**

1. **BRE delivery:** Milestone plan for UIM/DSS/KK-committed BRE scope with **shared programme view with CU1** — flexibility is **gated** on these dates.  
2. **Bid evidence:** “Existing vs planned” BRE capability pack for UIM/KK evaluations (no overstated KRs).  
3. **Admin-configurable validation:** At least one production reference where business users change rules/validations without deployment project.  
4. **Web process modelling:** Ramp milestone — business users maintain approved model types (Copenhagen PE usability).  
5. **Workflow history & visual steps:** Scoped milestones for UIM/eDoc template needs **after** BRE critical path unless capacity proves parallel safe.  
6. **Factory:** BMAD/BMAT-style **spec discovery** for BRE/PE epics before implementation — spec lead time tracked as factory phase metric.

**Workshop open:** Max **2** Process Platform objectives unless IFAR programme reopens.

**Dependency (explicit):** **CU1** spine credibility **depends on PP2 BRE** dates — one programme board, not competing OKRs.

---

## Core Integrations

**Strategic pull:** UIM/Vahva API-first; **#437273** / agent context; eDoc KOMBIT lift; Copenhagen **435503** / external AI Assist pattern (platform, not duplicate AI strategy).

**Config migration (*Improve internal tools used by consultants*):** If **Core BL** cannot support **CE1** backend commitments, **Core Integrations** may implement backend services — **Collect & Engage remains the named objective owner** in ProductPlan.

### Phase A — current ProductPlan

| Current objective (ProductPlan) | Action | Rationale |
|-------------------------------|--------|-----------|
| API-first integration framework | **Merge → INT1** | Single integration-platform objective |
| KOMBIT integrations lift | **Merge → INT2** | eDoc merger critical path |
| eDoc external API translation | **Merge → INT2** | Same programme as *KOMBIT integrations lift* |
| Increase perceived value of Autosaver | **Park** | **INT3 not in 2026–27 objective set** — archive or pause in ProductPlan when QCLT agrees; revisit when UIM/Copenhagen capacity allows |

### Phase B — shaped objectives (draft for LPM refinement)

**This cycle:** **INT1 + INT2** only. **INT3 / Autosaver** parked.

#### INT1 — Integration platform ready for agents and API-first tenders

**Outcome:** External systems and **customer/partner agents** integrate through a **documented, secured API layer** (SIF direction, **#437273**) — supporting Vahva, FI agent brief, **CO3**, BYO-AI positioning.

**Depends on:** **Core BL** auth, logging, audit; **BL3** for agent identity patterns.

**Enables:** **AI2**, **PNB3**, municipal AI Assist (**435503**).

**Draft KRs**

1. **Platform roadmap:** Published API-first roadmap with agent-relevant **context, actions, events** — aligned with D7 B.  
2. **Reference integration:** At least one production or pilot integration using new platform patterns (Vahva-class or agent context).  
3. **Security & segregation:** Agent/non-human access patterns documented and implemented for one reference scenario (**BL3** alignment).  
4. **Developer experience:** Partner/implementer documentation and sandbox path for KK **435503**-style REST consumers.  
5. **Factory:** OpenAPI/spec and contract tests maintained as factory context assets; generated client stubs only with human review.

---

#### INT2 — eDoc and KOMBIT integrations merger-ready

**Outcome:** Danish **KOMBIT lift**, API translation, and external continuity are **verified** — merger and Danish references do not fail on integration gaps.

**Depends on:** **DS3**, **TR2**, **CU3** programme coordination.

**Enables:** eDoc company objective; Danish market **CO1**.

**Draft KRs**

1. **Portfolio inventory:** All KOMBIT/eDoc integration points with RAG status and owner — shared with merger programme.  
2. **Lift & translate:** Committed interfaces lifted/translated to Online with test evidence before merger gate.  
3. **External API continuity:** Breaking-change policy and customer communication for eDoc external APIs.  
4. **Factory:** Use factory for **integration test packs** and doc generation on high-regression interfaces — not for net-new architecture without architect review.

---

## Core BL and eArchive

**Strategic pull:** UIM MK-7 deletion self-service, dispatch/logging, SIEM (**435501**); online deployment for merger; agent identity (**D7/D9**). **Supports Collect CE1** — config migration **backend** (not a separate ProductPlan team objective on Core BL).

### Phase A — current ProductPlan

| Current objective (ProductPlan) | Action | Rationale |
|-------------------------------|--------|-----------|
| Supporting cont. deployments (TUXIT) | **Merge → BL2** | Shared with QuadCore — one deployment maturity OKR |
| Outlook integration | **Merge → BL2** | Same online/migration theme |
| AI Query Builder | **Defer → AI & Insights** | Not Core BL strategy; avoid duplicate AI OKR on wrong team |
| Consultant config tools (archived, company) | **Fold → CE1** (Collect owns); **Core BL supports** backend | **Core Integrations** alternative backend implementer if needed |

### Phase B — shaped objectives (draft for LPM refinement)

#### BL1 — Spine-grade retention, dispatch, and audit-ready logging

**Outcome:** Platform spine and tenders (**MK-7**, **MK-160**, KK **435501**) are credible on **deletion self-service**, message dispatch, and **SIEM-ready** operational logs.

**Depends on:** **Tech Platform / QuadCore** for monitoring/residency enablers.

**Enables:** **CU1**, **INT1**, **AI1** governance evidence.

**Draft KRs**

1. **Deletion self-service:** Customer-configurable retention/deletion policies without vendor ticket (**MK-7** narrative).  
2. **Dispatch & messaging:** Reliability and observability targets for spine-critical dispatch paths.  
3. **Logging export:** Documented non-proprietary log/analytics export path (**MK-160** / open architecture) with one customer or lab validation.  
4. **SIEM readiness:** KK-class SIEM integration feasibility — commit, partial, or documented Q&A position aligned with gate briefs.

---

#### BL2 — Online deployment and collaboration maturity

**Outcome:** **TUXIT/containerization** and **Outlook** paths support Online growth, UIM integration hosts, and **eDoc merger** deployment — co-owned with QuadCore where infra KRs apply.

**Depends on:** QuadCore/Tech Platform capacity (**TP1**, merge *Supporting cont. deployments (TUXIT)* intent here).

**Enables:** Merger, UIM Online integrations, **CO1** migration story.

**Draft KRs**

1. **Containerization milestones:** Dated TUXIT/Online deployment milestones for merger and UIM host classes — **QuadCore co-KRs** named.  
2. **Outlook integration:** Committed Outlook/Online scenario for migration customers (scope per product).  
3. **Environment promotion:** Test→prod patterns support **CE1** backend commitments (Collect owner unchanged).

---

#### BL3 — Identity and audit for agents and integrations

**Outcome:** Non-human actors (agents, integrations) use **segregated credentials** with audit trails suitable for **CO3** and KK governance.

**Depends on:** **AI1**, **INT1** designs.

**Enables:** Agent platform, tender segregation answers.

**Draft KRs**

1. **Credential model:** Documented pattern for agent/service accounts with least privilege.  
2. **Audit:** Security-relevant agent/integration actions emit auditable events (**AI1** SIEM alignment).  
3. **Reference implementation:** One end-to-end scenario with **INT1** or **AI2** in lab or pilot.

**Supporting commitments (not extra OKRs)**

- **CE1:** Backend for config import/export and test→prod (**Collect** owns objective).  
- **CU1 Track B:** File/spine APIs, performance, brownfield context for BIF pilots — dates in **CU1** plan; **review capacity** for agent-generated BL changes named in factory program.

---

## AI and Insights

**Strategic pull:** CO3; **D7/D8/D9**; Copenhagen summaries/classification/redaction; not parallel strategies on other teams.

### Phase A — current ProductPlan

| Current objective (ProductPlan) | Action | Rationale |
|-------------------------------|--------|-----------|
| AI infrastructure ("Sebastian to suggest text") | **Merge → AI1** | Placeholder — replace with governed infra wording |
| Support AI adoption | **Merge → AI2** | Too generic; folds into agent platform + native agents |
| Continued success with Archive Inspector | **Merge → AI3** | One analytics product line OKR |
| Further scaling of Archive Inspector | **Merge → AI3** | Duplicate ArIn theme |
| Success for Mimir | **Merge → AI3** | Mimir + ArIn under one **insights products** objective |
| Chat in core product (archived) | **Achieved — stay archived** | Delivered via **360 Mimir** release; do not reopen *Chat functionality in core product* |

### Phase B — shaped objectives (draft for LPM refinement)

**Note:** Sebastian / AI & Insights owns **CO3** execution via AI1–AI2; other teams hold **dependencies** only. **Customer AI ≠ AI Software Factory** — factory may accelerate **native agent** delivery where specs/tests are factory-ready.

#### AI1 — Governed AI infrastructure (CO3 foundation)

**Outcome:** Every case-handling AI feature runs through **central routing, model registry, residency rules, and audit** — answering AST/KK/NB domestic-cloud and SIEM expectations.

**Depends on:** **Core BL** logging/audit; **Tech Platform** **TP1/TP2** when D9b applies.

**Enables:** **AI2**, **BL3**, all native agents, honest tender roadmaps.

**Draft KRs**

1. **Governance layer live:** Routing/proxy, classification gates, human-in-the-loop rules for production AI paths.  
2. **Registry & residency:** Supported deployment topologies documented (**D9b/c**); default path for Nordic customers defined.  
3. **Audit & SIEM:** AI operations emit evidence compatible with KK **435501** / centralized governance narrative.  
4. **Offer packaging:** Clear standard vs add-on AI SKUs for bids (KK B2-16 honesty pattern).

---

#### AI2 — Agent platform and reference native agents

**Outcome:** **BYO-AI and native agents** coexist: platform exposes **agent-ready APIs** (**INT1**) plus **2–3 reference agents** (metadata, summary, redaction class) from Copenhagen discovery.

**Depends on:** **INT1**, **CU1** context surfaces, **AI1**, **BL3**.

**Enables:** **PNB3**, Sandnes/NKF/KK patterns; **CO3** MVP.

**Draft KRs**

1. **Agent platform MVP:** Context, permissions, events for at least one municipal partner scenario.  
2. **Reference agents:** Two production-grade native capabilities with governance from **AI1** and measurable user outcome (not feature count).  
3. **Roadmap honesty:** Bid pack “existing vs planned” aligned with ProductPlan KRs.  
4. **Factory:** Native agent **spec + test** artifacts built through factory gates; separate **customer AI** metrics from engineering phase metrics.

---

#### AI3 — Mimir and Archive Inspector growth

**Outcome:** Insight products (**Mimir**, **Archive Inspector**) grow revenue and competitiveness, including chat/archive assist lines from discovery.

**Depends on:** Process Platform for redaction/archive overlap (no IFAR OKR).

**Enables:** Insight revenue; AST archive/analysis assist narrative.

**Draft KRs**

1. **Revenue & retention:** Targets for ArIn/Mimir customer base and NPS or equivalent.  
2. **Competitive parity:** Dated capabilities vs market for archive analysis and Mimir assistant scenarios.  
3. **Platform alignment:** Uses **AI1** governance when touching case/archive AI features.

---

## Transparency

**Strategic pull:** Publishing revenue/satisfaction; eDoc merge. **IFAR handover (TR3):** not in this cycle — see *Refactor IFAR module to React* disposition.

### Phase A — current ProductPlan

| Current objective (ProductPlan) | Action | Rationale |
|-------------------------------|--------|-----------|
| Publishing solutions — satisfaction and revenue | **Keep → TR1** | Still valid market OKR |
| eDoc general functionality merge | **Merge → TR2** | Shared with Core UI CU3 — one merge OKR on Transparency side |

### Phase B — shaped objectives (draft for LPM refinement)

#### TR1 — Publishing solutions customers renew and expand

**Outcome:** Publishing/OpenGov customers show **measurable satisfaction and revenue trajectory** — not maintenance-only mode.

**Depends on:** **Core UI** (**CU2** UX/a11y); **Decision Support** for board/publication workflows.

**Enables:** Danish market; NB publication patterns via **DS1** coordination.

**Draft KRs**

1. **Satisfaction:** Target NPS/CSAT or agreed proxy for publishing customer cohort.  
2. **Revenue:** Product revenue or expansion metric for publishing solutions (define baseline in workshop).  
3. **Reference quality:** At least one public reference journey meeting **CU2** accessibility bar.

---

#### TR2 — eDoc general functionality merged on Online

**Outcome:** Journal, templates, searches, notifications, and shared general functionality are **delivered with Core UI** under one merger programme — Q2 2026 trajectory intact.

**Depends on:** **CU3**, **INT2**; shared backlog with Core UI.

**Enables:** eDoc company objective.

**Draft KRs**

1. **Joint programme plan:** Dated milestones with **CU3** — single source of truth.  
2. **Capability completion:** Defined merge checklist % complete by quarter.  
3. **Customer communication:** Breaking changes and migration notes for Danish eDoc customers.

---

## Decision Support

**Strategic pull:** eManager desirability; Danish eSigning; eDoc meetings on Online.

### Phase A — current ProductPlan

| Current objective (ProductPlan) | Action | Rationale |
|-------------------------------|--------|-----------|
| Board and council manager satisfaction | **Keep → DS1** | Copenhagen NB/board patterns |
| New eManager version | **Merge → DS1** | Same customer outcome |
| Modern document production (no office clients) | **Defer or KR-only** | **0 KRs** — not a healthy OKR; track as roadmap initiative or merge into DS1 if still strategic |
| eDoc meeting functionality on Online | **Keep → DS3** | Merger critical path |
| Roll out eSigning to Danish market | **Keep → DS2** | Dated company commitment |

### Phase B — shaped objectives (draft for LPM refinement)

#### DS1 — Board, council, and eManager customers prefer our UX

**Outcome:** **Board and Council Manager / eManager** meet desirability expectations for **NB, councils, and Copenhagen discovery** — coordinated with **CU2**, not a parallel UX programme.

**Depends on:** **Core UI** a11y/desirability gates.

**Enables:** **TR1** publication workflows; Copenhagen NB patterns.

**Draft KRs**

1. **Desirability baseline:** Critical admin journeys measured (time-on-task, support tickets, or agreed proxy).  
2. **eManager roadmap:** Named releases that close top customer pain from board/council segment.  
3. **Cross-module UX:** Shared patterns with **CU2** for WCAG on DS-owned UI.

---

#### DS2 — eSigning live for Danish market commitments

**Outcome:** **Roll out eSigning to Danish market** company commitment delivered with integrator-ready packaging.

**Depends on:** **Core Integrations** for signing integrations.

**Enables:** **CO1** Danish growth; merger adjacent scenarios.

**Draft KRs**

1. **Market rollout milestones:** Dated availability for committed Danish scenarios.  
2. **Compliance & documentation:** Customer-facing legal/technical documentation complete.  
3. **Support readiness:** Support model and known-issue budget for go-live customers.

---

#### DS3 — eDoc meetings on 360° Online

**Outcome:** **eDoc meeting functionality** required for merger works on Online with integrations intact.

**Depends on:** **INT2**, **TR2**/**CU3** programme.

**Enables:** eDoc company objective Q2 2026.

**Draft KRs**

1. **Feature parity milestone:** Meeting capabilities required for merger signed off with test evidence.  
2. **Integration tests:** End-to-end scenarios with **INT2** KOMBIT/external dependencies.  
3. **Pilot customer:** At least one Danish customer or lab sign-off before general availability.

---

## Plan and Build (Planning Case + P&B + Construction)

**Strategic pull:** Copenhagen reference delivery; Oslo go-live; Sweden fit; optional agent pilot (**D7**, Sandnes/KK).

Teams in ProductPlan: **Planning Case (5105)**, **Plan&Build (5107)**, **Construction cases (5106)** — one **combined** objective set for workshops (max 2–3 across programme).

### Phase A — current ProductPlan

| Current objective (ProductPlan) | Action | Rationale |
|-------------------------------|--------|-----------|
| Succeed with P&B Sweden | **Keep → PNB1** | High risk — still valid |
| Customers experience | **Keep → PNB2** | Aligns CO2/Copenhagen NPS |
| Successful go-live Oslo for P&B | **Keep → PNB2** | Concrete delivery OKR |
| Fee solution discovery | **Defer** | Discovery-only until KK/fee bid commits |
| Integration leader | **Retire or merge → PNB2** | Slogan without distinct KRs; Copenhagen needs **delivery** OKRs, not positioning text |
| eDoc building case on Online | **Program KR** | Track under PNB1/PNB2 + *Succeed with eDoc product merger by Q2 2026* — not a fourth team objective |

### Phase B — shaped objectives (draft for LPM refinement)

#### PNB1 — Plan & Build fit for Sweden

**Outcome:** **P&B Sweden** high-risk commitment progresses with Flow/maps/webparts viable for Swedish regulatory and customer context.

**Depends on:** **PP1** Flow GA; domain product ownership.

**Enables:** Nordic growth **CO1**.

**Draft KRs**

1. **Risk burn-down:** Top Sweden blockers with owners and dates (legal, product, technical).  
2. **Flow/maps readiness:** Scenarios required for Sweden on supported runtime (**PP1** alignment).  
3. **Customer milestone:** Named Swedish customer or pilot gate.

---

#### PNB2 — Reference delivery and bid-competitive P&B experience

**Outcome:** **Oslo go-live** succeeds and P&B is **credible in Copenhagen/KK bids** — integrated Flow + UX + integrations, not siloed module claims.

**Depends on:** **PP1**, **CU1/CU2**, **INT1**; eDoc building case as **program KR** not fourth objective.

**Enables:** **CO2** reference story; KK/Copenhagen sales.

**Draft KRs**

1. **Oslo go-live:** Dated go-live criteria with executive-visible RAG.  
2. **Customer experience:** Bid/demo journey meeting **CU2** thresholds for critical P&B flows.  
3. **Integrated narrative:** Documented AST/KK reference architecture linking Flow, webparts, maps, agents (honest maturity labels).

---

#### PNB3 — PnB agent integration pilot (optional)

**Outcome:** Municipal **agent + PnB** pattern (Sandnes, KK **435503**) proven on **agent platform** — not a second AI strategy.

**Depends on:** **AI2**, **PP1**, **INT1**; D7 approval.

**Enables:** Municipal agent ecosystem **CO3**/BYO-AI.

**Draft KRs**

1. **Pilot charter:** Named municipality/collaborative, scope, success metric.  
2. **Integration evidence:** Agent accesses case/context via **INT1** with **BL3** security.  
3. **Learnings:** Publish pattern for reuse or explicit deferral.

**Workshop open:** **PNB3** only if leadership allocates capacity (**D7**).

---

## Collect and Engage

**Strategic pull:** **Config migration** (folds archived *Improve internal tools used by consultants*); company RDF KR; NVE Collect–Flow. Hard requirement for **UIM** and **HSØ**. **Named ProductPlan owner: Collect & Engage.**

### Config migration programme (ownership model)

| Role | Team | ProductPlan |
|------|------|-------------|
| **Objective owner** (UI/UX + end-to-end accountability) | **Collect & Engage** | **CE1** — single team objective |
| **Supporting** (backend: import/export, test→prod, validation, services/APIs) | **Core BL** (default) | Committed via **CE1** dependencies / Core BL supporting plan — **not** a separate Core BL team OKR |
| **Alternative supporting implementer** | **Core Integrations** | If Core BL capacity or architecture favours integration-layer delivery — **CE1** owner unchanged |

Collect owns customer-facing experience and programme outcome; Core BL (or Integrations) delivers backend scope named in **CE1** KRs and dependency matrix.

### Phase A — current ProductPlan

| Current objective (ProductPlan) | Action | Rationale |
|-------------------------------|--------|-----------|
| New markets outside Nordics (DE/AT/NL) | **Defer** | Not UIM/Copenhagen critical path unless leadership confirms entry |
| Improve internal tools for consultants (archived, company) | **Fold → CE1** | **Collect & Engage** named owner; **Core BL supporting** backend |

### Phase B — shaped objectives (draft for LPM refinement)

**Recommendation:** **CE1 + CE2** this cycle; **CE1** workshop led by Collect LPM with Core BL (supporting) present.

#### CE1 — Customer-operable configuration and migration (owner)

**Outcome:** Customers and consultants **import/export, promote, and validate** 360 configuration (**433887**, HSØ) **without vendor-only tooling** — Collect owns end-to-end outcome.

**Depends on:** **Core BL** backend (default) or **Core Integrations** alternative; **Tech Platform** env promotion.

**Enables:** **CO1**, **CU1**, UIM/HSØ bids.

**Draft KRs**

1. **Portability MVP:** Import/export for agreed configuration scope with documented limitations.  
2. **Test→prod:** Customer or consultant can promote config between environments with audit trail (**CE1** UI + backend).  
3. **UIM/HSØ evidence:** Bid-ready description of existing vs roadmap for config self-service.  
4. **Programme governance:** Single backlog; backend delivery dates from Core BL/INT in **CE1** plan.  
5. **Factory:** Spec-first delivery for config UX flows; regression suite for migration scenarios.

---

#### CE2 — RDF and Collect integrated with Flow

**Outcome:** **RDF adaption layer** trajectory and **Collect–Flow** work support **NVE**, RDF customer count **CO1** KR, and portfolio bids.

**Depends on:** **PP1** Flow GA.

**Enables:** **PNB1/PNB2**, company RDF KR.

**Draft KRs**

1. **Collect–Flow scenarios:** Production-path integration for NVE-required use cases.  
2. **RDF customers:** Contribution to company RDF customer count milestone (baseline in workshop).  
3. **Documentation:** Implementer guidance for RDF+Flow deployments.

---

#### CE3 — International expansion readiness (optional / defer)

**Outcome:** Preparedness for DE/AT/NL only if leadership confirms entry — otherwise defer.

**Draft KRs:** (Define only if **CE3** approved at QCLT.)

---

## Tech Platform / CloudOps / QuadCore

ProductPlan may not have a dedicated product team slot; objectives *Supporting cont. deployments (TUXIT)* sit on Core BL + **QuadCore (5268)**.  
**Meeting pack:** [quadcore-meeting-pack-2026.md](quadcore-meeting-pack-2026.md) · docx: `quadcore-meeting-one-pager-2026.docx`, `quadcore-objectives-alignment-2026.docx`

### Phase A

| Current objective (ProductPlan) | Action | Rationale |
|-------------------------------|--------|-----------|
| TUXIT / containerization | **Re-home** | Intent captured under **BL2**; clarify QuadCore vs Core BL KR ownership with LPM |

### Phase B — shaped program objectives (if no ProductPlan team slot)

#### TP1 — Sovereignty-ready residency and platform monitoring

**Outcome:** Tenants meet **residency and monitoring** expectations for KK, AI hosting, and UIM logging clusters — **QuadCore/Tech Platform** deliverer, **Core BL** coordinates product requirements.

**Enables:** **AI1**, **BL1**, **CO3** D9; KK **435501**.

**Draft KRs**

1. **Residency patterns:** Documented deployment options aligned with **D8/D9** messaging.  
2. **Monitoring/SIEM:** Platform monitoring hooks validated for at least one reference tenant.  
3. **UIM logging cluster:** Capacity plan for **MK-160**-class requirements (~1–2 FTE band validated in QuadCore breakout).

---

#### TP2 — Nordic managed AI inference ops (if D9b)

**Outcome:** Tieto-operated **T2 inference** for native agents is operable with clear lifecycle ownership vs customer-local **T3**.

**Enables:** **CO3**, small/mid kommuner turnkey AI.

**Draft KRs**

1. **Ops model:** Runbooks, SLA, and security boundary documented.  
2. **Pilot runtime:** One native agent path on T2 in lab or pilot customer.  
3. **Cost visibility:** Model/agent cost per outcome tracked for product decisions.

---

## Parked objectives (not in 2026–27 set)

| Current objective (ProductPlan) | Team | Disposition |
|-------------------------------|------|-------------|
| Increase perceived value of Autosaver | Core Integrations | **INT3 parked** — not UIM/Copenhagen critical path; no team OKR; archive or pause in ProductPlan after QCLT sign-off |
| Operational Reporting | Unassigned | Pulled out; partial path via **CU1** search refactoring (see orphan section) |

**QCLT one-liners**

- **INT3:** *Increase perceived value of Autosaver* parked for this cycle; Core Integrations focuses on **INT1** API/agent platform and **INT2** eDoc/KOMBIT for UIM and merger.
- **Operational reporting:** *Operational Reporting* retired from the OKR set; reporting gaps addressed incrementally via the **CU1** search refactoring programme.

---

## Unassigned / orphan objectives

| Current objective (ProductPlan) | Action | Rationale |
|-------------------------------|--------|-----------|
| Operational Reporting | **Pull out of this refresh** — archive or pause in ProductPlan | Not on UIM/Copenhagen critical path. No team OKR this cycle. Need addressed **incrementally** via **search refactoring** programme (align with **CU1** list/search/MK-77 work), not a standalone operational-reporting objective. Distinct from completed *BI / Management Reporting* (Management Reporting API release). |

---

## Cross-team: UIM and Copenhagen on the critical path

| Priority | Theme | Primary objectives |
|----------|-------|-------------------|
| **UIM bid credibility** | Platform spine + search + **config migration (CE1)** + **BRE (PP2 — gates flexibility)** + API + logging | **PP2**, **CU1**, **CE1**, Core BL (support), **INT1**, **CO1** |
| **HSØ / config portability** | Import/export, test→prod, customer-operable config | **CE1** (Collect owner); Core BL supporting backend (**INT** alternative implementer) | — |
| **Copenhagen product bets (D3)** | PE usability, Flow GA story, governed AI patterns, WCAG | **PP1**, **PP2**, **CU2**, **AI2**, **PNB2** |
| **Merger Q2 2026** | eDoc programme | *Succeed with eDoc product merger by Q2 2026*, **CU3**, **TR2**, **INT2**, **DS3**, **BL2** |

---

## Suggested workshop order

1. Core UI (**D1 phasing** — spine direction already agreed)  
2. **Collect & Engage** (**CE1** owner) with **Core BL supporting** (Integrations alternative if needed)  
3. Process Platform  
4. Core Integrations  
5. AI and Insights (with Sebastian)  
6. Plan and Build, Transparency, Decision Support, Core BL (parallel or wave 2)  
7. Company CO1–CO3 rewrite  

---

## Archived objectives — achievement vs disposition

ProductPlan **archived** ≠ **achieved**. QCLT disposition (Sep 2026):

| Archived objective (ProductPlan) | Achieved? | Disposition for 2026–2027 refresh |
|----------------------------------|-----------|-----------------------------------|
| Improve internal tools used by consultants (config import/export, test→prod, access matrix regen, etc.) | **No** | **CE1** on **Collect & Engage** (named owner); **Core BL supporting** backend. Alternative implementer: Core Integrations. Hard requirement for **UIM** and **HSØ**. Do not un-archive *Improve internal tools used by consultants*. |
| Refactor IFAR module to React | **No** | **Drop as OKR this cycle** — stay archived; capacity to Flow, UIM, Copenhagen, merger. No **PP3/TR3** in workbook. |
| Chat functionality in core product | **Yes** | Delivered via **360 Mimir** release. Stay archived; lineage noted under **AI3**. |
| Establish foundational design system | **Yes** | Stay archived; outcomes live in FFUI/design practice — express via **CU2/CO2** if needed, not separate company OKRs. |
| Foster design system adoption and awareness | **Yes** | Same as *Establish foundational design system* — stay archived. |
| BI / Management Reporting (AI & Insights team) | **Yes** | Completed via **Management Reporting API** release. Stay archived. |
| Operational Reporting (Unassigned) | **N/A — pulled out** | Not in 2026–2027 team objective set; partial coverage via **search refactoring** / **CU1**; archive active *Operational Reporting* when QCLT agrees |

---

## Revision log

| Version | Date | Change |
|---------|------|--------|
| 0.1 draft | 2026-09-14 | Team-by-team Phase A retire/merge + Phase B first stab (UIM + Copenhagen) |
| 0.2 draft | 2026-09-14 | Archived-objective dispositions; config migration split **CE1/BL4**; drop IFAR OKR (*Refactor IFAR module to React*); Mimir/design system/Mgmt Reporting API outcomes |
| 0.3 draft | 2026-09-14 | Config migration: Collect **UI/UX (CE1)**; **Core BL backend (BL4)** with **Core Integrations** as alternative owner |
| 0.5 draft | 2026-09-15 | **CU1**: Core UI owner, **Core BL** dependency; detail-view tile rewrite via agentic AI-assisted development |
| 0.6 draft | 2026-09-21 | *Operational Reporting* pulled out of refresh; partial path via **CU1** search refactoring |
| 0.7 draft | 2026-09-21 | **PP2** reframed around **BRE**; platform flexibility gated on BRE delivery; **CU1** depends on **PP2** |
| 0.8 draft | 2026-09-21 | **INT3 / Autosaver (*Increase perceived value of Autosaver*)** parked; Core Integrations **INT1 + INT2** only |
| 0.9 draft | 2026-09-21 | **BIF→React agentic rewrite** in **CU1** (Tracks A/B); Core BL supporting for pilots + CE1; Jarle/Willy initiative |
| 1.0 draft | 2026-09-21 | Refer to existing ProductPlan objectives by **title**, not numeric ID |
| 1.1 draft | 2026-09-21 | UIM offer delivered; **no-bid off table**; **D1** = phasing; Copenhagen = market direction regardless of award |
| 1.2 draft | 2026-09-22 | **Shaped Phase B** objectives with draft KRs + **AI Software Factory** hooks per team |
