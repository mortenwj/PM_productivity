# Day 1 — Flow pilot: status & learnings

**Title:** 360° Flow pilot — status & learnings  
**When:** Day 1 (before BRE session — exact slot TBD on main workshop schedule)  
**Suggested duration:** 60–75 min  
**Lead:** Morten (product narrative) + delivery/engineering voices for NVE and runtime  
**Audience:** Process Platform team (internal)

---

## Session goal

Give the team a **shared, honest picture** of the Flow pilot — what we set out to prove, what is **shipped in 6.10**, what **NVE** is teaching us, and what we still need to decide — so the later **BRE session** can treat Flow as a known sibling pillar.

**Outputs:** Validated learnings list · NVE status clarity · agreed refresh actions · inputs captured for wiki/ADO

---

## Timing

| Block | Duration | Focus |
|-------|----------|--------|
| **A — Reframing & status** | 20 min | Three-layer Flow story, capability snapshot, DevOps, NVE programme |
| **B — NVE learnings (presented)** | 15 min | Product framing, P&B platform depth, meetings — §5.G1–G3 |
| **C — Workshop discussion** | 25 min | Team input — ProcessView gaps, delivery surprises, actions |
| **Close** | 5 min | Capture owners; handoff to BRE session |

---

## Block A — What the pilot is (~15 min)

### Slide 1 — Title

**360° Flow pilot — status & learnings**

Internal alignment — not customer-facing sales.

### Slide 2 — Flow in the Process Framework

| Component | Question |
|-----------|----------|
| Process models | **What** the process looks like |
| **360° Flow / Process Engine** | **How** it runs |
| Business Rules Engine | **When** actions are allowed or required |

Flow = **governed operational execution** — ProcessView, progress plans, activities, milestones — **not** generic BPM.

### Slide 3 — Pilot model

From [Process_Framework_Pilot_One_Pager.md](../process-models/Process_Framework_Pilot_One_Pager.md):

- **One** end-to-end process · **Tieto-led** delivery · **No** self-service modeling
- **6.10** controlled pilot · primary programme **NVE** (#411612)
- Commercial: **2 processes**, **shipped building blocks only** ([Commercial Spec](./360_Flow_Commercial_Spec_v1.md))

*Speaker note:* Hosted Processes and pricing validation are explicitly out of scope.

---

## Block B — Status (~25 min)

### Slide 4 — What is shipped (pilot-primary)

**Strong today**

- Process models + PMC admin
- Progress plans, activities, runtime orchestration
- Milestones, stages, subprocess dialogs
- **ProcessView** as case-worker surface
- Reusable building blocks (.wu, toolbox activities)

**Partial / watch**

- Document flow dialogs (dual routing legacy + React)
- Localization (#420545 Active, #420676 New)
- Send email / meeting — code exists; ADO Features may still say New

**Not for pilot promises**

- Worklists, portfolio overview, AI modeling, BPMN modeler

*Detail:* [Flow_Pilot_Status_And_Learnings.md](./Flow_Pilot_Status_And_Learnings.md) §3

### Slide 5 — DevOps program

| Epic | State | Focus |
|------|-------|-------|
| #414623 PAF umbrella | New | Empty description — needs narrative |
| #411614 Core Platform | **Active** | Engine, performance, triggers |
| #414328 Standard Artifacts | New | Reusable definitions & templates |
| #414727 UX | New | ProcessView, admin, overview config |
| #411612 **NVE Pilot** | New | Real delivery, tag 6.10 |

Feature [#413948](https://dev.azure.com/tieto-si/360/_workitems/edit/413948) — NVE process definitions before go-live.

### Slide 6 — NVE & demo assets

**Ask in room:** Where is NVE on the go-live path?

Supporting material:

- Demo tenant setup + multilingual assets ([360_Flow_Demo_Setup_DRAFT.md](./360_Flow_Demo_Setup_DRAFT.md))
- Standard process patterns in repo (NVE Processes, deficiency letters)
- Weekly report last in repo: **2026-04-21** — refresh needed

---

## Block C — Learnings (~20 min)

Walk [Flow_Pilot_Status_And_Learnings.md](./Flow_Pilot_Status_And_Learnings.md) **§5.G1–G3** — presented slides, not re-read verbatim.

**Do not pre-fill §5.G4** — defer ProcessView complexity to Block C.

---

## Block C — Workshop discussion (~25 min)

### Slide — Gaps to explore together

Facilitate on **assistance**, **dynamic controls**, and **other items** from NVE/delivery. Capture severity: blocker / important / defer.

### Slide — Team input

Open floor: consultant, engineering, product. Scribe appends to `Flow_Pilot_Status_And_Learnings.md` §5.G after session.

### Slide — Actions

Owner · date · DevOps link for each action assigned in room.

---

## Close (~5 min)

### Slide — Actions

| Action | Owner | Date |
|--------|-------|------|
| Refresh weekly ADO report | | |
| NVE status paragraph for wiki/ADO | | |
| Fill epic #414623 description | | |
| Append workshop learnings to status doc | | |

Point team to `projects/process-platform/flow/Flow_Pilot_Status_And_Learnings.md`.

---

## Facilitation

| Role | Who |
|------|-----|
| Pilot intent, commercial, program | Morten |
| Runtime / capability truth | Engineering (Bjørn or delegate) |
| NVE delivery status | Delivery lead in room |
| Scribe for learnings | Assign in room |

**Handoff to BRE session:** BRE deck slide 3 should reference this session as the Flow inventory baseline.

---

## Deck build

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "projects/process-platform/flow/build_flow_pilot_deck.ps1"
```

Output: [Flow_Pilot_Workshop.pptx](./Flow_Pilot_Workshop.pptx)
