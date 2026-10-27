---
artifact: feature-spec
source-skill: grill-me
created: 2026-05-26
confidence: high
phases-completed: [1, 2, 3, 4, 5, 6, 7]
acceptance-criteria-count: 7
---

# Feature Spec: 360° Hosted Processes

## Vision

**Hosted Processes** are standardized, Tieto-maintained operational processes delivered on a **subscription** model on top of Public 360°. Customers with **Public 360° only** (no separate Flow capacity purchase required) can enter a **Hosted Processes framework agreement**, then **self-service** browse a **catalog of templates**, **activate** a process (with a **per-process subscription**), complete **bounded configuration**, and **go live** when ready — running cases **end-to-end** including eService intake where the template requires it.

**Primary buyers:** Fagleder / process owner (**B**) and ledelse / standardiseringsprogram (**C**) — process outcome plus org-wide standardisation.

**Today without Hosted:** Mostly manual case handling in P360 (**A**) and spreadsheets/email/outside tools (**C**); bespoke Process Engine (**B**) is uncommon.

**60-second demo:** Catalog in 360 → pick template → **Activate** → basic configuration → show end-to-end readiness (eService, process model, production go-live path).

**Commercial (v1):** Assisted **framework agreement** to enter the program; **self-service** activation UI once entitled; **each activation** = **annual hosted process subscription**; does **not** consume configurable Flow production-process capacity.

## Constraints

### In scope (v1)

- Catalog of **≥5** hosted process templates at pilot/v1 launch (per customer or global catalog — confirm delivery model in O2).
- **Self-service** activate → configure → **draft** → explicit **Go live**.
- Configuration surface only:
  - Names and labels
  - Document archive / category
  - Dispatch channels
  - Template-defined **step selection** (e.g. approval before dispatch)
- Prerequisites enforced with **blocking checklist** before activation/go-live completes.
- **Tieto-managed** template updates on a schedule; **new cases** get new version; **in-flight** cases stay on start version.
- **Deactivation:** no new cases; in-flight run to completion.

### Out of scope (hard boundaries)

- **No** customer-specific process development inside the subscription.
- **No** changes to process logic beyond template **configuration** markers.
- **No** full Process Framework self-service modeling for hosted tenants (upgrade path to configurable Flow is separate).
- **No** counting activated hosted processes toward **Flow capacity** (`FLOW-CAP-*`) entitlement.

### Commercial constraints

- Customer must sign **Hosted Processes framework agreement** before catalog/activate is available.
- Each **Activate** requires an active **per-process hosted subscription** (annual).
- Out-of-envelope requests (early phases): **product change request** → expand core template/config **or** default to change pack/T&M / upgrade to configurable Flow.

### Consistency

- Align with [`360_Flow_Commercial_Spec_v1.md`](360_Flow_Commercial_Spec_v1.md) §8 (separate commercial line; hosted-only meter).
- Product term **Hosted Process** per [`360_Flow_PRD_Reconstruction_Unredacted_v4.md`](360_Flow_PRD_Reconstruction_Unredacted_v4.md) (commercial/service layer on Flow runtime included via P360).

## Acceptance Criteria

Ordered by priority (interview: **AC1 catalog** is non-negotiable #1).

1. **AC1 — Catalog (priority #1):** An entitled tenant displays **≥5** hosted process templates in Public 360°, each with name, description, and **prerequisites** (modules, eService, archive, etc.). *Verify:* count ≥5; prerequisite list visible before Activate.

2. **AC2 — Entitlement gate:** Without a **Hosted Processes framework agreement**, the catalog/activate UI is **not available**. With agreement but **no** per-process subscription for template X, **Activate** on X is **blocked** with clear messaging. *Verify:* role tests for entitled vs non-entitled tenant.

3. **AC3 — Activate and configure:** Authorized admin can **Activate** an entitled template, complete configuration **only** within the allowed fields (names, labels, archive/category, dispatch channels, template-defined step toggles), and save as **draft** without Tieto development. *Verify:* configuration UI matches allow-list; no model editor exposed.

4. **AC4 — Go live:** Admin can move a configured process from **draft** to **Go live** only when the **prerequisite checklist** is green; after go-live, **new cases** may enter the process. *Verify:* draft blocks case start; go-live enables; checklist blocks when prerequisite missing.

5. **AC5 — End-to-end execution:** Within **30 minutes** of go-live (test environment), a new case completes the template’s golden path including **eService** intake (if required), process model progression, and ProcessView-visible stages. *Verify:* scripted test case per template.

6. **AC6 — Metering:** Each live hosted process is recorded on **hosted subscription** entitlement only; activating/hosting does **not** decrement configurable Flow **production process** count. *Verify:* CRM/entitlement report or admin entitlement view.

7. **AC7 — Managed updates:** Tieto publishes template version **N+1**; on rollout date, **new cases** use **N+1**; cases started on **N** remain on **N** until closed. Release notes published per rollout. *Verify:* two-case test across rollout boundary.

## Edge Cases and Error States

| Scenario | Expected behavior |
|----------|-------------------|
| **Missing prerequisites** | Block activation/go-live; show checklist (Q11 **A**). |
| **Configure outside envelope** | Early phase: product change request; if not core → change pack/T&M or Flow upgrade (Q12). |
| **Draft vs live** | No new cases on process until **Go live** (Q9 **A**). |
| **Template update with live cases** | New cases on new version; in-flight pinned to start version (Q10 **A**). |
| **Deactivate / subscription ends** | No new cases; in-flight complete on current version (Q13 **A**). |
| **No framework agreement** | Catalog hidden or read-only with “contact sales”; no Activate. |
| **Activate without subscription line** | Block with link to order/add subscription SKU. |
| **Empty catalog (&lt;5 templates)** | Fail AC1; not shippable for stated v1 pilot bar (Q17 **C**). |
| **Compliance-critical update** | Managed rollout per policy; limited opt-out window (Q8 **A**). |
| **Customer on configurable Flow only** | Hosted catalog additive; hosted activation still uses hosted SKU, not capacity slot. |

## Variant Directions

### Self-service UI vs assisted commercial entry

| | |
|--|--|
| **Model** | Self-service catalog/activate/configure; **assisted** only for **framework agreement** and per-process SKU (Q14–15). |
| **Strongest argument** | Low delivery cost at scale; matches fagleder demo; contract captures program commitment. |
| **Biggest risk** | Subscription/entitlement plumbing not ready → gating breaks or manual workarounds. |
| **Verdict** | **Build** — product self-service; commercial assisted entry. |

### Per-process subscription vs bundle-only

| | |
|--|--|
| **Model** | **Per activated process** annual line (Q16 **A**). |
| **Strongest argument** | Revenue follows adoption; clear expansion. |
| **Biggest risk** | Procurement friction per process; needs simple order path. |
| **Verdict** | **Build** for v1. |

## Test Plan

### Visual verification

- [ ] Catalog shows **≥5** templates with prerequisites readable without Activate.
- [ ] Activate flow shows **draft** vs **go live** states distinctly.
- [ ] Configuration UI exposes **only** allowed fields (no process model editor).
- [ ] Prerequisite checklist visible and turns green/red correctly.
- [ ] Blocked states: no framework agreement, no per-process SKU.

### Functional verification

- [ ] Sign framework agreement (test tenant) → catalog appears.
- [ ] Add per-process subscription → Activate enabled for that template.
- [ ] Configure + **Go live** → start case → complete golden path including eService (template-dependent).
- [ ] Deactivate → cannot start new case; existing case completes.
- [ ] Entitlement: hosted process does not reduce Flow capacity counter.

### Edge case verification

- [ ] Go live blocked with red checklist; fix prerequisite → go live succeeds.
- [ ] Template rollout: old case on vN, new case on vN+1 after rollout date.
- [ ] Out-of-config request documented as product change request path (process test with PM).

## Technical Reference

| Document | Use |
|----------|-----|
| [`360_Flow_Commercial_Spec_v1.md`](360_Flow_Commercial_Spec_v1.md) §8 | SKU placeholders, no double-count, pilot billing |
| [`360_Flow_PRD_Reconstruction_Unredacted_v4.md`](360_Flow_PRD_Reconstruction_Unredacted_v4.md) | Hosted Process as service layer; runtime boundaries |
| Forankring Alternativ 2 (`process models/extracted_text/Forankring v.0.1 …`) | Delivery and subscription rationale |
| **Open:** `/feature-scoping` for sprint breakdown, subscription framework (O7), template authoring pipeline |

### Open items (from interview)

| ID | Item | Owner |
|----|------|-------|
| O1 | Framework agreement SKU + legal text | Enablement / Legal |
| O2 | Global vs per-customer catalog for pilot | Product / Delivery |
| O3 | Template authoring & versioning toolchain | Engineering |
| O4 | Product change request workflow for out-of-envelope | Product |
| O5 | Opt-out policy duration for managed rollout | Product / Support |

---

**Confidence: high** — All grill-me phases completed with substantive answers; acceptance criteria are measurable; demo vs commercial entry reconciled (self-service product, assisted framework contract).

*This spec will evolve. Run `/grill-me` on this file to pressure-test after pilot learnings.*
