# 360° Flow — First delivery project (2 processes)

**Document type:** Delivery / service description (internal + customer-facing source)  
**Status:** DRAFT — time and effort **TBD** pending Delivery calibration (NVE pilot actuals)  
**Version:** 0.2  
**Date:** 2026-09-17  
**Owner:** Product + Delivery (Flow)  
**Package SKU:** `FLOW-IMPL-2PROC`  
**Related module:** **P00285** (360° Flow)  
**Commercial rules:** [`360_Flow_Commercial_Spec_v1.md`](360_Flow_Commercial_Spec_v1.md) · [`360_Flow_Implementation_Package_2Process_SalesKit_DRAFT.md`](360_Flow_Implementation_Package_2Process_SalesKit_DRAFT.md)  
**Contract:** [`360_Flow_Entitlement_and_Metering_Contract_Addendum_DRAFT.md`](360_Flow_Entitlement_and_Metering_Contract_Addendum_DRAFT.md)

---

## 1. Purpose

This document describes **how the first 360° Flow delivery project is run** when a customer purchases the **Implementation Package (2 Processes)**:

- **What** we deliver and **how** the project is executed  
- **Typical duration** and **effort envelope** (planning estimates — to be confirmed by Delivery)  
- **Conditions** that must be met before and during the project  

It is the delivery counterpart to the **module product sheet** ([`360_Flow_Product_Sheet_ENG.md`](360_Flow_Product_Sheet_ENG.md) / **P00285**).

---

## 2. What this delivery project is

| Element | Description |
|---------|-------------|
| **Offer** | Fixed-scope **implementation project** for **two** end-to-end processes on 360° Flow |
| **Delivery model** | **Tieto-led** — we design, configure, test, and go-live; customer validates and accepts |
| **Building blocks** | **Shipped Flow catalogue only** — no custom work units or bespoke components in base package |
| **Outcome** | Two **active process models** in **production** (published, with cases per go-live plan), configuration documentation, handover, and **customer enablement** to configure **further processes** on shipped building blocks |
| **Platform capacity** | Under the **introductory pilot offer**, platform entitlement for **two active process models** is bundled with this delivery contract when signed by **31 December 2026** (see commercial spec §11.4) |
| **Enablement goal** | By project end, nominated customer administrators can **configure the next processes themselves** (within catalogue boundaries), not only operate cases on the two delivered processes |

**Not included in this project type:** custom work units / bespoke components, third process without separate order, Enterprise-only capabilities, Hosted Processes, unlimited 1:1 coaching beyond the three training sessions.

---

## 3. Conditions for starting (entry criteria)

The project **starts at M0** only when **all** of the following are in place:

| # | Condition | Owner |
|---|-----------|-------|
| C1 | Signed **delivery contract / SOW** for `FLOW-IMPL-2PROC` | Customer + Tieto Sales |
| C2 | Valid **Public 360°** subscription; tenant on **6.12 or newer** (or agreed minimum) | Customer IT |
| C3 | **360° Flow** pilot enablement on agreed environments (production + non-production as scoped) | Tieto Deployment / Customer IT |
| C4 | **Two process owners** (or one owner + deputy) named with authority to approve design and UAT | Customer |
| C5 | **Key users** identified for workshops and UAT | Customer |
| C6 | Access for Tieto: environments, admin accounts, project collaboration (Teams/360° as agreed) | Customer IT |
| C7 | **Process scope** documented at kick-off: two logical processes, case types, building-block fit confirmed | Tieto + Customer |
| C8 | No dependency on **custom development** outside catalogue without signed change order | Both |
| C9 | **Training participants** nominated (typically process owners + 2–4 future administrators) for all **three** sessions | Customer |

**Sales guardrail:** Do not start delivery without **C1**. Do not promise go-live dates before **C3** and design approval (**M1/M2**).

---

## 4. How the project is run

### 4.1 Overview

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ 1. Initiate  │──▶│ 2. Design    │──▶│ 3. Build &   │──▶│ 4. Test &    │──▶│ 5. Go-live & │
│    & plan    │   │  (2 proc.)   │   │  configure   │   │  accept      │   │  handover    │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
     M0                  M1, M2              M3                  M4                  M5
```

### 4.2 Roles

| Role | Party | Responsibility |
|------|-------|----------------|
| **Project manager** | Tieto | Plan, steering, status, milestone gates, change control |
| **Process consultant** | Tieto | Workshops, design, configuration, test support, as-built documentation |
| **Deployment / technical** | Tieto (as needed) | Flow enablement, environment checks |
| **Process owner (×2 or shared)** | Customer | Domain rules, decisions, design sign-off, UAT sign-off |
| **Key users** | Customer | Workshops, UAT execution |
| **IT contact** | Customer | Access, integrations within scope, production go-live approval |

### 4.3 Phase detail

#### Phase 1 — Initiate & plan (→ **M0**)

| Activity | Tieto | Customer |
|----------|-------|----------|
| Kick-off, confirm two processes and success criteria | ● | ● |
| RACI, communication plan, project plan | ● | Review |
| Environment plan (dev/test/prod) | ● | ● |
| Confirm building-block fit per process; escalate gaps | ● | ● |
| Agree UAT approach and acceptance criteria template | ● | ● |

**Gate M0:** Project plan and scope **approved** by customer project sponsor.

---

### 4.4 Customer enablement training (3 sessions — included)

Training is **part of the fixed package**, not an add-on. It runs **in parallel** with delivery so that, by **M5**, the customer can configure **additional processes** on **shipped building blocks** (phases, milestones, checklists, standard patterns). Tieto still leads delivery of the **two contracted processes**; training transfers repeatable configuration skills.

| Session | When (typical) | Duration | Content | Customer outcome |
|---------|----------------|----------|---------|------------------|
| **1 — Introduction to 360° Flow** | After **M0** (early Phase 2) | **3 hours** | 360° Flow framework; **process models**; **checklists**; **milestones**; **automation logic**; **portfolio management** (scope per release) | Shared vocabulary and mental model for the project |
| **2 — Process mapping** | Before **M1** (Phase 2) | **TBD** hours *(planning: ~3)* | Collaborative **diagramming** workshop — map the **first process** to implement (pure mapping exercise, not system configuration) | Approved input for Process 1 design; customer practices mapping |
| **3 — Checklist implementation** | Phase 3 (after **M1**, during build of Process 1) | **TBD** hours *(planning: ~4)* | Deep dive on Process 1 from session 2; **set up the first checklist** in the system **with** the customer (hands-on) | Customer can implement checklists on shipped patterns with reduced dependency on Tieto |

**Participants:** process owners, key users, and nominated **administrators** who will own the next processes (C9).

**Boundaries:** Training covers **governed configuration within shipped building blocks** — not custom work units, not Enterprise-only portfolio features unless explicitly in scope, not a substitute for ordering capacity/implementation for process 3+.

**Deliverable:** Brief training completion note (sessions held, attendees, topics covered) at **M5**.

---

#### Phase 2 — Design (→ **M1**, **M2**)

| Activity | Tieto | Customer |
|----------|-------|----------|
| **Training session 1** (introduction) | Deliver | Attend |
| **Training session 2** (process mapping — Process 1) | Facilitate | Co-create diagram |
| As-is / to-be workshops **per process** (may follow session 2 output) | Facilitate | Participate, provide regulations and local rules |
| Process model design (phases, milestones, checklists, activities) | Propose | Validate |
| Integration points (max **one simple** per process if in scope) | Propose | Confirm |
| Design document / sign-off pack | ● | Approve per process |

**Gate M1:** Process **1** design **approved** (written).  
**Gate M2:** Process **2** design **approved** (written).

Design for process 2 may overlap with early build of process 1 where dependencies allow.

---

#### Phase 3 — Build & configure (→ **M3** internal)

| Activity | Tieto | Customer |
|----------|-------|----------|
| Configure process models, checklists, milestones, dialogs | ● | Clarifications (target: within **2 business days**) |
| **Training session 3** (checklist implementation — Process 1) | Facilitate hands-on | **Co-configure** first checklist |
| System test (Tieto) | ● | — |
| Defect fix for in-scope configuration | ● | — |

**Gate M3:** Configuration **complete** and ready for UAT (internal Tieto gate; customer informed).

---

#### Phase 4 — Test & accept (→ **M4**)

| Activity | Tieto | Customer |
|----------|-------|----------|
| UAT plan and test cases (agreed at kick-off) | Support | **Execute** UAT |
| UAT support and in-scope defect fix | ● | Retest |
| Written acceptance **per process** | — | ● |

**Gate M4:** **Written UAT acceptance** for **both** processes; no **critical** open defects (severity defined in SOW).

---

#### Phase 5 — Go-live & handover (→ **M5**)

| Activity | Tieto | Customer |
|----------|-------|----------|
| Production activation (publish models per agreed plan) | ● | Approve go-live |
| Handover documentation (as-built configuration) | ● | Receive |
| Training completion note; confirm enablement goal met | ● | Acknowledge |
| Name operations / support contact | — | ● |

**Gate M5:** Go-live **approved**; handover **complete**.

**Post-go-live:** Hypercare per SOW (**TBD** — e.g. 30 days configuration defect fix). Platform support follows standard Public 360° agreement. Process **changes** after handover = consultancy / change request.

---

## 5. Time estimate

> **Status:** **Planning model only.** Delivery must replace **TBD** with calibrated figures from **NVE pilot** and consultant capacity. Do not quote externally until **D-HOURS** is locked (sales kit Part I).

### 5.1 Elapsed calendar time (indicative)

Assumes customer meets participation targets and **one** non-production environment for build/UAT before production go-live.

| Phase | Indicative duration | Notes |
|-------|---------------------|-------|
| 1. Initiate & plan | **2–3 weeks** | Depends on access and sponsor availability |
| 2. Design (2 processes) | **4–6 weeks** | Often sequential workshops; M1 then M2 |
| 3. Build & configure | **4–6 weeks** | Partial overlap with late design possible |
| 4. Test & accept | **2–4 weeks** | Customer UAT calendar often drives length |
| 5. Go-live & handover | **1–2 weeks** | |
| **Total (typical)** | **~12–16 weeks** | **Planning range** — adjust after NVE actuals |

**Factors that extend timeline:** customer delay > agreed response window, scope change, extra integrations, unavailable process owners, complex regulatory sign-off.

### 5.2 Effort envelope (Tieto — TBD)

Fixed-price package assumes effort **not exceeding** the envelope below unless change order.

| Activity area | Indicative effort | Owner | Status |
|---------------|-------------------|-------|--------|
| Project management | **TBD** days | Tieto PM | ☐ Calibrate |
| Process design workshops (2 processes) | **TBD** sessions × **TBD** hours | Process consultant | ☐ Calibrate |
| Configuration & system test | **TBD** days | Process consultant | ☐ Calibrate |
| UAT support | **TBD** days | Process consultant | ☐ Calibrate |
| Go-live & handover | **TBD** days | Process consultant + PM | ☐ Calibrate |
| Deployment / enablement | **TBD** days | Deployment | ☐ Calibrate |
| **Customer enablement training** (3 sessions) | **10 hours** included *(3 + ~3 + ~4 planning; confirm S2/S3)* | Process consultant | ☐ Confirm durations |
| **Total envelope** | **TBD** person-days | | ☐ **D-HOURS** |

*Customer effort:* plan for **three training sessions**, **workshop participation** for design/UAT, **UAT** (typically **1–2 weeks** calendar per process depending on complexity), and timely sign-offs.

### 5.3 Payment milestones (linked to delivery)

Align with SOW — default proposal in sales kit Part E:

| Trigger | % of implementation fee |
|---------|-------------------------|
| Signed delivery contract | 30% |
| M4 — UAT accepted (both processes) | 40% |
| M5 — Go-live and handover | 30% |

---

## 6. Scope and change conditions

### 6.1 Included in the fixed package

See sales kit **Part C**. Summary:

- Two processes, shipped building blocks, design through go-live, PM, as-built documentation, **three enablement training sessions** (§4.4), standard integrations within pre-agreed simple integration cap.

### 6.2 Out of scope without change order

- Custom work units, third process, extra environments, **training beyond the three included sessions** (e.g. floor-walking, train-the-trainer at scale), Enterprise features, material scope change after M1/M2.

### 6.3 Change control

| Change type | Handling |
|-------------|----------|
| Clarifications within approved design | Included |
| New integration, process, or catalogue gap | **Change request** — price and timeline impact |
| Customer delay beyond **TBD** agreed days | Timeline shift; possible standby charges per SOW |

---

## 7. Customer obligations (ongoing)

| Obligation | Detail |
|------------|--------|
| **Availability** | Process owners and key users for workshops and UAT windows |
| **Decisions** | Design and go-live approvals within **TBD** business days unless otherwise agreed |
| **Domain correctness** | Customer responsible for legal/regulatory content of process logic |
| **Capacity ordering** | Inform Tieto before go-live if a **third** active process model is planned (capacity + implementation order) |
| **Operations** | Case handling on live processes after handover |
| **Further processes** | Use skills from training to configure **next** processes on shipped blocks; order **capacity** (and implementation support if needed) before production go-live of process 3+ |

---

## 8. Assumptions and risks

| ID | Assumption / risk | Mitigation |
|----|-------------------|------------|
| A1 | Both processes can be built from **shipped building blocks** | Confirm at kick-off; escalate before contract if not |
| A2 | Customer has **one** production and **one** test environment suitable for Flow | In entry criteria C3 |
| A3 | Portfolio / manager worklists may be **limited** in pilot release | Set expectations in design; do not promise GA portfolio |
| A4 | No technical block on exceeding 2-process entitlement in pilot | Contract + delivery discipline at go-live (R5) |
| A5 | NVE learnings may adjust effort envelope | Revise §5.2 when Delivery signs off |

---

## 9. Deliverables checklist

| Deliverable | When |
|-------------|------|
| Approved project plan | M0 |
| Approved design per process | M1, M2 |
| Configured processes in test/UAT | Before M4 |
| UAT acceptance record | M4 |
| Production-active processes (per plan) | M5 |
| As-built configuration documentation | M5 |
| All **three training sessions** completed | Before M5 (session 3 before/during Process 1 build) |
| Handover completed; enablement goal acknowledged | M5 |

---

## 10. Next steps to finalize this document

| # | Action | Owner |
|---|--------|-------|
| 1 | Replace §5.2 **TBD** with NVE-based person-day envelope | Delivery |
| 2 | Confirm §5.1 calendar range or narrow to single quoted duration | Delivery + PMO |
| 3 | Set customer response / approval **TBD** days in §6–7 | Legal + Delivery |
| 4 | Convert to **service sheet** PPT/PDF (Enablement template) | Enablement |
| 5 | Publish **Implementation guidelines** wiki page (SPOC) | Consultancy |
| 6 | Link from sales kit Part B as canonical delivery description | Product |

---

## Revision history

| Version | Date | Changes |
|---------|------|---------|
| 0.1 DRAFT | 2026-09-17 | Initial delivery project description — run model, time framework, conditions |
| 0.2 DRAFT | 2026-09-17 | Three included enablement sessions; goal = customer can configure next processes on shipped blocks |
