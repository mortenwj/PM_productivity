# 360° Flow pilot — status & learnings

**Last updated:** 2026-06-08 (NVE customer learnings — §5.G in progress)  
**Audience:** Process Platform team, workshop Day 1  
**Sources:** PRD reconstruction, commercial spec, pilot one-pager, weekly ADO reports, DevOps (live pull 2026-06-08), demo setup, training manuscripts, **NVE customer sessions (Morten, June 2026)**

---

## 1. Start here

This document is the **workshop-ready synthesis** for the Flow pilot: what we set out to prove, where we are in **6.10**, what we have learned so far, and what still needs team input.


| Question                             | Short answer                                                                                                                  |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **What is Flow?**                    | **Execution + visualization + portfolio** on Public 360° — process models, ProcessView, phase context, manager worklists/desktops — not generic BPM |
| **What is the pilot?**               | **One end-to-end process**, Tieto-led delivery, **shipped building blocks only**, controlled enablement in **6.10**           |
| **Primary programme**                | **NVE pilot** (ADO epic [#411612](https://dev.azure.com/tieto-si/360/_workitems/edit/411612), tag `6.10`)                     |
| **Runtime maturity**                 | **Strong** on ProcessView, milestones, stages, progress plans, configurable overview columns                                  |
| **Operational maturity**             | **Transitional** — manager worklists/desktops **partial**; some portfolio patterns exist via Plan&Build webparts customers already saw |
| **Formal learnings doc before this** | **None** — this file fills that gap from existing material                                                                    |


**Related docs:** [Flow_Day1_Session_Plan.md](./Flow_Day1_Session_Plan.md) · [360_Flow_PRD_Reconstruction_Unredacted_v4.md](./360_Flow_PRD_Reconstruction_Unredacted_v4.md) · [Process_Framework_Pilot_One_Pager.md](../process-models/Process_Framework_Pilot_One_Pager.md)

---

## 2. What the pilot is for

From the [Process Framework pilot one-pager](../process-models/Process_Framework_Pilot_One_Pager.md):

- Validate **Individual Standard** in practice — standardized structure with flexibility where variation is real
- Deliver **one complete end-to-end process** on the Process Framework (Single Process Delivery)
- Test that Tieto can deliver **faster and more predictably** than bespoke work
- Feed proven patterns back as **reusable templates and accelerators**

### Delivery model (locked for pilot)


| Aspect                  | Pilot rule                                                   |
| ----------------------- | ------------------------------------------------------------ |
| Who builds the process  | **Tieto** — design, configuration, rules/automation in scope |
| Customer role           | Domain knowledge, validation                                 |
| Self-service modeling   | **Out of scope**                                             |
| Hosted Processes / SaaS | **Out of scope**                                             |
| Pricing validation      | **Out of scope**                                             |


### Commercial guardrails (locked 2026-05-26)

From [360_Flow_Commercial_Spec_v1.md](./360_Flow_Commercial_Spec_v1.md):

- **2 production processes** included per customer in pilot
- **Shipped building blocks only** + fixed implementation
- Pilot success = **processes live**, not licences sold alone

---

## 3. Product status (6.10)

**Release framing:** Public 360° **6.10** — wiki section *Coming soon (Ongoing Pilots) → 360° Flow (Pilot)*  
**Customer-facing name:** **360° Flow** (internal legacy name **PAF** still in ADO)

### Capability snapshot


| Area                                     | Status                                                    | Pilot relevance                     |
| ---------------------------------------- | --------------------------------------------------------- | ----------------------------------- |
| Process models (bind, activate, PMC)     | **Shipped**                                               | Primary admin + runtime surface     |
| Progress plans & activities              | **Shipped**                                               | Primary case-worker execution       |
| Milestones & stages                      | **Shipped**                                               | Primary lifecycle structure         |
| ProcessView (React)                      | **Shipped**                                               | Case-worker home; configurable columns (map, deficiencies, decisions, checklists, etc.) |
| Process overview / visualization panels  | **Shipped / configurable**                                | NVE responded strongly; ADO #420133 (configurable overview sections)                    |
| Document flow (approval/review/dispatch) | **Partial**                                               | Works; legacy + React routing split |
| Send email / meeting / share dialogs     | **Shipped in BL**; designer Features often **New** in ADO | Do not trust Feature state alone    |
| Rules (DMN at engine level)              | **Shipped internal**                                      | Authoring UX limited; see BRE track |
| Reusable building blocks (.wu, toolbox)  | **Shipped**                                               | NVE + demo assets depend on this    |
| Localization (dialogs, activity lists)   | **Active improvement** (#420545 Active, #420676 New)      | Pilot UX risk                       |
| Worklists (manager queues)               | **Backlog / emerging** (#411634 New)                      | NVE expectation: prioritise work across cases by phase status, deadlines                |
| Portfolio / process-centric desktops     | **Partial** — Plan&Build webparts shown; Flow story broader | Customers assumed P&B webparts = Flow; want **more** than shown                         |
| AI-assisted modeling                     | **Future**                                                | Explicitly out of pilot             |
| BPMN modeler                             | **New backlog** (#419789)                                 | Post-pilot direction                |


**One-line summary:** Flow is **ProcessView-centered execution** plus **visualization on the case** and **portfolio surfaces for managers** — we **undersold** the latter in internal docs; NVE expects **one integrated story** from desk to case.

---

## 3b. What Flow is (reframed after NVE)

Internal positioning shift (**1e: we undersold it**):

| Layer | What it is | NVE signal |
|-------|------------|------------|
| **Execution** | Process models, progress plans, activities, milestones | Core pilot — shipped |
| **Visualization** | ProcessView + configurable overview columns (maps, deficiencies, decisions, checklists, …) | Strong positive reaction in customer sessions |
| **Portfolio** | Manager prioritisation across cases — queues, deadlines, phase status; process-centric desktops/webparts | Expected as part of Flow, not a separate future product |

**One Flow story:** case workers in ProcessView and managers on portfolio/desktops are **one narrative**, not two products stitched together in the sales pitch.

**Positioning risk:** Plan&Build webparts were demonstrated; NVE **assumed they were Flow**. They are related platform assets, but customers wanted **even more** portfolio capability than we showed.

### Plan&Build platform depth *(confirmed 2026-06-08)*

Flow draws on **existing Public 360° / Plan&Build assets**, not a greenfield stack. NVE experiences this as **one platform story** — they do not distinguish Flow vs P&B in the room.

| P&B / platform asset (NVE context) | Role in Flow story |
|-----------------------------------|-------------------|
| Map integration | **Required** for NVE go-live — in ProcessView / overview columns |
| Checklists (phase-linked) | Core phase workspace context |
| Estates / parcels / matrikkel | Registration and case context |
| Case phrases / registration patterns | Case setup and worker guidance |
| Document categories + stage binding | Process document flow |
| Deadlines / phase status | Manager queues and prioritisation |
| Decisions | Overview column + process outcome context |

**“More than webparts shown”:** richer **filtering**, **follow-ups**, and **reporting** on manager/portfolio surfaces — beyond what existing P&B webparts demonstrated.

**Strategic implication (2e):** Move Plan&Build assets that belong in the shared process story into a **common repository** consumed by **both** Flow and Plan&Build — reduce duplication, clarify ownership, and stop ad-hoc “is this Flow or P&B?” confusion in delivery.

---

## 4. DevOps program status

**Umbrella:** [#414623 PAF – Process Automation Framework](https://dev.azure.com/tieto-si/360/_workitems/edit/414623) — **New**, description still empty at pull **2026-06-08**.


| Epic               | ID                                                                   | State (2026-06-08) | Role                                                |
| ------------------ | -------------------------------------------------------------------- | ------------------ | --------------------------------------------------- |
| Core Platform      | [#411614](https://dev.azure.com/tieto-si/360/_workitems/edit/411614) | **Active**         | Engine, meta, triggers, performance                 |
| Standard Artifacts | [#414328](https://dev.azure.com/tieto-si/360/_workitems/edit/414328) | **New**            | Reusable process definitions, templates, categories |
| User Experience    | [#414727](https://dev.azure.com/tieto-si/360/_workitems/edit/414727) | **New**            | ProcessView, admin UI, configurable overview        |
| Productization     | [#411613](https://dev.azure.com/tieto-si/360/_workitems/edit/411613) | **New**            | Packaging / GA path — thin in ADO                   |
| **NVE Pilot**      | [#411612](https://dev.azure.com/tieto-si/360/_workitems/edit/411612) | **New**            | Real-programme delivery, tag `6.10`                 |


**NVE process delivery feature:** [#413948](https://dev.azure.com/tieto-si/360/_workitems/edit/413948) — *NVE Specific process definitions before go-live* — **New**

**Weekly tracking:** [PAF_pilot_weekly_report_SPEC.md](../pilot/PAF_pilot_weekly_report_SPEC.md) + generator under `tools/` — last populated report in repo: **2026-04-21** (refresh recommended before workshop).

---

## 5. Pilot learnings (synthesized)

> **Note:** These are **document-derived learnings**, not a formal retrospective. Validate and extend in the Day 1 session — capture new items in §8.

### A. Delivery & operating model

1. **Implementation-led pilot works as a scope filter** — "shipped building blocks only" forces honest scoping and prevents one-off code masquerading as product.
2. **Tieto-led delivery is the right pilot posture** — self-service modeling would conflate product gaps with delivery skill; defer until runtime + artifact library are stable.
3. **Success metric is operational** — a process **live on cases** with case workers using ProcessView, not feature checklists or ADO closure counts.
4. **Demo assets de-risk enablement** — multilingual NVE-style process models, checklists, and document templates ([360_Flow_Demo_Setup_DRAFT.md](./360_Flow_Demo_Setup_DRAFT.md)) give consultants a repeatable starting point separate from customer-specific NVE work.

### B. Product & runtime

1. **The execution core is real** — process models, progress plans, milestones, stages, and ProcessView are integration-tested and pilot-primary; this is not a slide-ware pilot.
2. **ProcessView is the product surface** — invest narrative and UX feedback here; admin PMC matters but case workers experience Flow through ProcessView.
3. **Dual routing is a support tax** — `UserActionExecuter` resolves document-flow URLs only; other client actions fall through to legacy BIF/engine paths. Pilots need explicit test matrices per dialog type.
4. **Async process model loading changes client expectations** — when `AsyncProcessModelLoading` is on, stages/activities may appear after commit; UI must wait/poll (`useWaitTaskStatus` pattern).
5. **ADO Feature state ≠ shippability** — send email, meeting invite, and related designer Features can be **New** while BL handlers and APIs exist; triangulate with code + tests before promising in a pilot SOW.

### C. Reuse & standardization

1. **Building-block model pays off** — toolbox activities + `.wu` standard processes (e.g. document flow, create subprocess, Share With, CreateSingleDocument) let pilots compose rather than rewrite.
2. **Standard Artifacts epic is the scaling lever** — process definitions, stage templates, document categories, deadline types — pilot deliveries should **feed this library**, not stay customer-private silos.
3. **Localization is on the critical path** — dialog APIs and activity list labels still carry localization-ID debt (#420545, #420676); impacts every multilingual pilot including NVE.
4. **Plan&Build assets are part of the Flow delivery stack** — maps (required for NVE), checklists, estates, decisions, deadlines, etc. are not “someone else’s product” at implementation time; **common-repo consolidation** is the agreed direction.

### D. Program & communication

1. **Epic descriptions matter for alignment** — umbrella #414623 and several child epics still lack narrative in ADO; newcomers cannot infer scope from titles alone.
2. **Weekly stakeholder reports help** — 14-day WIQL rollups by epic (NVE, UX, Artifacts, Core) give a honest activity picture; need refresh cadence through workshop.
3. **Rename PAF → 360° Flow is still mid-flight** — ADO, repo paths, and some docs still say PAF; expect confusion in cross-team conversations until glossary is stable.

### E. Commercial & GA path

1. **Hybrid commercial model decided in draft** — Foundation included, capacity by process count, Enterprise for operating-model power ([360_Flow_Commercial_Spec_v1.md](./360_Flow_Commercial_Spec_v1.md)).
2. **Hosted Processes correctly deferred** — [360_Hosted_Processes_spec.md](./360_Hosted_Processes_spec.md) explicitly waits for pilot learnings; do not sell ahead of evidence.
3. **Wiki module page published** — customer-facing positioning exists (rev 59679); 6.10 pilot section still thinner than PRD; no named customers approved for wiki yet.

### F. Platform sibling (BRE)

1. **Flow and BRE are complementary, not competing** — Flow answers *how work runs*; BRE answers *when actions are allowed/blocked*; pilot conversations should keep that boundary crisp (see [BRE_Inventory.md](../bre/BRE_Inventory.md)).
2. **Rules in Flow today ≠ full BRE product** — engine-level DMN exists; customer-facing rules lifecycle and ValidationMessage-first BRE pilot are a **parallel track**.

### G. NVE customer meetings — product framing *(capture in progress)*

#### G1. Reframing what Flow is *(confirmed 2026-06-08)*

| # | Learning |
|---|----------|
| G1.1 | **Portfolio = manager job** — prioritising work **across many cases** via queues, deadlines, and phase status — not an abstract Enterprise upsell. |
| G1.2 | **Desktops / webparts** — NVE had been shown **Plan&Build webparts** and **assumed they were part of Flow**; they wanted **more** than what was demonstrated. |
| G1.3 | **One Flow story** — ProcessView on the case and portfolio on the desk belong in **one** product narrative end-to-end. |
| G1.4 | **Visualization landed** — ProcessView plus **additional overview columns** (maps, deficiencies, decisions, checklists, etc.) were what customers reacted to — not execution mechanics alone. |
| G1.5 | **We undersold Flow internally** — Flow is not only process modeling and execution; it is also **visualization** and **portfolio management** in customer expectation, with parts already present in the platform story. |

#### G2. Plan&Build platform depth *(confirmed 2026-06-08)*

| # | Learning |
|---|----------|
| G2.1 | **Broad P&B dependency** — maps, estates/matrikkel, checklists, case phrases, document categories, deadlines/phase status, and **decisions** all surfaced in the NVE Flow story — not maps alone. |
| G2.2 | **Maps are go-live required** — map integration in ProcessView/overview is **not** optional for NVE pilot acceptance. |
| G2.3 | **Customer credits the platform** — NVE attributes value to **Public 360° platform** holistically, not “Flow module” vs “Plan&Build module” separately. |
| G2.4 | **Portfolio gap is functional** — “more than webparts” means **filtering**, **follow-ups**, and **more reporting** on manager views — not just prettier ProcessView. |
| G2.5 | **Architecture direction** — migrate P&B assets that belong in the shared process story into a **common repo** shared by Flow and Plan&Build; stop parallel silos that confuse customers and delivery. |

#### G3. NVE meetings — what went well *(confirmed 2026-06-08)*

| # | Learning |
|---|----------|
| G3.1 | **What landed** — **Public 360° platform** story and **Tieto partnership / delivery model** resonated more than a narrow “Flow feature tour”. |
| G3.2 | **Full stakeholder mix** — process owners, case workers, IT, consultants, and leadership were all in the room; no single audience layer dominated. |
| G3.3 | **No single “aha” quote** — positive sentiment was **broad**, not one moment or feature call-out (3c: no). |
| G3.4 | **Sentiment: positive but cautious (B)** — enthusiasm for direction; waiting on gaps (maps, portfolio depth, ProcessView behaviours) before go-live confidence. |
| G3.5 | **Repeat what works** — **discovery format + fast iterations**; include **Process Platform** in customer meetings; **collaborate across product, consultancy, and tech consulting** — not product-only or delivery-only sessions. |

*Sections G4–G6: capture in workshop — ProcessView complexity (assistance, dynamic controls), team input, actions.*

---


| Risk                        | Why it matters                     | Mitigation                                                   |
| --------------------------- | ---------------------------------- | ------------------------------------------------------------ |
| Localization incomplete     | Broken or raw IDs in dialogs/lists | Prioritize #420545/#420676; test in all pilot languages      |
| Legacy + React routing      | Hard-to-diagnose dialog failures   | Per-activity test checklist in pilot test plan               |
| Performance on case open    | Many Stage/Checklist API calls     | Core Platform performance initiative (#397370) — monitor NVE |
| Scope creep via custom WU   | Breaks reuse narrative             | Commercial spec: shipped blocks only                         |
| Empty ADO epic descriptions | Misaligned expectations            | Fill #414623 + #411612 narrative after workshop              |
| Portfolio expectation vs delivery | NVE expects P&B-class webparts **plus more** (filtering, follow-ups, reporting) under Flow | Clarify platform vs Flow-branded scope; roadmap for worklists/desktops (#411634, #414651) |
| Map integration not validated on NVE path | **Required** for go-live | Explicit test plan for maps in ProcessView/overview before acceptance |
| P&B vs Flow asset ownership | Customers see one platform; teams maintain parallel repos | **Common repo** for shared process assets (G2.5) — scope and owner TBD |
| Product-only customer sessions | Gaps surface late; cautious sentiment despite platform fit | **Process Platform in the room** — product + consultancy + tech consulting (G3.5) |


---

## 7. Open questions for the workshop

Capture answers live — these are **not** answered in repo material:

1. **NVE status:** Which process definitions are live vs in build? Blockers to go-live?
2. **Case worker feedback:** What have NVE users actually said about ProcessView?
3. **Consultant feedback:** What was harder than expected in delivery?
4. **Reuse:** Which NVE components are candidates for Standard Artifacts library?
5. **Pilot exit:** What would make us confident to offer a **second** controlled pilot customer?
6. **6.10 sign-off:** Who owns wiki release text + scope sign-off checklist?
7. **ProductPlan / roadmap:** Is the Flow bar still parked/stale vs DevOps reality?

---

## 8. Recommended next steps


| Action                                  | Owner (TBD in session) | Output                                                     |
| --------------------------------------- | ---------------------- | ---------------------------------------------------------- |
| Refresh weekly ADO report               |                        | `pilot_weekly_report_YYYY-MM-DD.md`                        |
| Write NVE pilot status paragraph        |                        | Update §4 + wiki draft                                     |
| Fill epic #414623 description           |                        | ADO                                                        |
| Publish learnings capture from workshop |                        | Append to this doc §5                                      |
| Align BRE session narrative             |                        | Link Flow inventory → BRE deck slide 3                     |
| Define common repo for shared P&B ↔ Flow assets |                        | ADO epic / architecture note                                 |
| Map + overview go-live test plan for NVE        |                        | Pilot acceptance checklist                                   |
| Institutionalise NVE meeting format             |                        | Discovery + fast iterations; cross-functional attendance (G3.5) |
| Regenerate workshop deck                        |                        | `Flow_Pilot_Workshop.pptx` via `build_flow_pilot_deck.ps1`   |


---

## 9. Source index


| Source                  | Path                                                                                                             |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------- |
| PRD / capability matrix | [360_Flow_PRD_Reconstruction_Unredacted_v4.md](./360_Flow_PRD_Reconstruction_Unredacted_v4.md)                   |
| Commercial pilot rules  | [360_Flow_Commercial_Spec_v1.md](./360_Flow_Commercial_Spec_v1.md)                                               |
| Pilot intent one-pager  | [Process_Framework_Pilot_One_Pager.md](../process-models/Process_Framework_Pilot_One_Pager.md)              |
| ADO program tree        | [experiment_release_notes_epic_414623_paf_program.md](../pilot/experiment_release_notes_epic_414623_paf_program.md) |
| Weekly report spec      | [PAF_pilot_weekly_report_SPEC.md](../pilot/PAF_pilot_weekly_report_SPEC.md)                                         |
| Latest weekly report    | [pilot_weekly_report_2026-04-21.md](../pilot/pilot_weekly_report_2026-04-21.md)                                     |
| Demo setup              | [360_Flow_Demo_Setup_DRAFT.md](./360_Flow_Demo_Setup_DRAFT.md)                                                   |
| Training tone           | [manuscripts/01_Flow_introduction_MANUSCRIPT.md](./manuscripts/01_Flow_introduction_MANUSCRIPT.md)               |
| BRE sibling context     | [../bre/BRE_Inventory.md](../bre/BRE_Inventory.md)                                                               |


