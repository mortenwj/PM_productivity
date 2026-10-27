# 360° Flow — Enablement & Sales decision (5 slides)

**Meeting:** Enablement + Sales · **Goal:** Land pilot commercial model in one session  
**Presenter:** [Name] · **Date:** [Today]  
**Detail after meeting:** [`360_Flow_Commercial_Spec_v1.md`](360_Flow_Commercial_Spec_v1.md)

> **Do not use** the full options deck (`360_Flow_Pricing_Options_Management_Deck.md`) in this meeting — that is analysis archive. Use **this deck** to decide.

---

## Slide 1 — One decision today

**Approve the pilot commercial model for 360° Flow.**

| We are **not** deciding today | We **are** deciding today |
|------------------------------|---------------------------|
| List prices (NOK/EUR) | Model structure for pilot quotes |
| GA segment entitlements (5 vs 10) | **2 processes included** for all pilot customers |
| Hosted Processes catalogue | **Shipped building blocks only** in included tier |
| Full SKU numbers | Who does what before first pilot quote |

**Architecture (already recommended):** **Hybrid** — foundation included in P360, charge for **more processes** and **Enterprise power** later.

---

## Slide 2 — The model (simple)

```
┌─────────────────────────────────────────────────────────┐
│  INCLUDED in Public 360° (pilot)                        │
│  • ProcessView, milestones, stages, standard dialogs    │
│  • Shipped building blocks ONLY                         │
│  • 2 production processes per customer                  │
└─────────────────────────────────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
   Process pack      Enterprise      Implementation
   (process 3+)      (power features) (fixed Playbook
   = revenue         = revenue         packages)
```

**Sales story (unchanged):** Prove → Expand → Mature (Playbook levels 1 / 2 / 3).

**Nordic norm:** Basic case progression is **in the platform** — we do **not** sell “permission to run workflow.”

---

## Slide 3 — Pilot rules (locked for this meeting)

| Rule | Pilot policy |
|------|----------------|
| **Included processes** | **2** per customer — same for kommune and state |
| **What’s free to use** | **Shipped building blocks only** — standard catalogue components |
| **Process 3+** | Process pack / per-process fee (use existing Process Engine bands until new SKUs exist) |
| **Enterprise** | **Not** in pilot base — portfolio, advanced rules, self-service modeling, custom components |
| **Services** | Fixed implementation package per deal (Playbook) |
| **Compliance** | Auditability and basic lifecycle visibility stay **included** — never behind Enterprise |

**Delivery guardrail:** Pilot processes are built from **shipped blocks only** unless customer buys expansion or Enterprise.

---

## Slide 4 — Vote (check boxes in the room)

| # | Decision | Proposed | ☐ Approve |
|---|----------|----------|-----------|
| **1** | **Hybrid** is the commercial architecture for Flow (foundation + capacity + Enterprise) | Yes | |
| **2** | Pilot included entitlement = **2 production processes**, all segments | Yes | |
| **3** | Pilot included scope = **shipped building blocks only** | Yes | |
| **4** | Process **3+** = pack / Process Engine overage (no unlimited processes in pilot) | Yes | |
| **5** | **Enablement** owns SKU placeholders + CRM fields before first external pilot quote | Yes | |
| **6** | **Product** publishes **“production process”** definition before first external pilot quote | Yes | |

**If any “no”:** note objection on slide 5; do not reopen full 3-option debate — escalate to product lead.

---

## Slide 5 — Next steps (owners & dates)

| Owner | Action | By when |
|-------|--------|---------|
| **Enablement** | Pilot SKU shape: `FLOW-CAP-INCL-2`, pack placeholder, implementation package IDs; CRM fields (`flow_process_entitlement`, `flow_pilot`) | [date] |
| **Enablement** | Quote template: 2 processes + building blocks + fixed implementation; footnote on expansion path | [date] |
| **Product** | One-page **production process** definition (what counts as 1 of 2) | [date] |
| **Sales** | Pilot offer one-pager aligned to slide 3; no bespoke / no feature discounting | [date] |
| **Finance** | Confirm Process Engine bands apply for process 3+ until new SKUs live | [date] |

**Success metric for pilot:** **Processes live** — not licences sold.

**Reference:** [`360_Flow_Commercial_Spec_v1.md`](360_Flow_Commercial_Spec_v1.md) §11 (pilot policy)

---

*Internal only. Hosted Processes = separate track — not on this meeting agenda unless time.*
