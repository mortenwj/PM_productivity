# Flow portfolio & reporting — prototype scope

Clickable prototype for **manager desktops**, **worklists**, and **reporting** in the 360° Flow story.

## Problem we are exploring

NVE and pilot learnings show customers expect Flow to cover **execution** (ProcessView) and **portfolio** (manager prioritisation) as one narrative — not two products stitched together.

| Gap (from pilot) | Prototype focus |
|----------------|-----------------|
| Worklists / manager queues (#411634) | Prioritised case list by phase, deadline, assignee |
| Process-centric desktops (#414651) | Desktop shell with Flow-relevant widgets |
| "More than webparts shown" | Richer filtering, follow-ups, reporting |

**Source docs:** [`../Flow_Pilot_Status_And_Learnings.md`](../Flow_Pilot_Status_And_Learnings.md), [`../360_Flow_Module_Page_DRAFT.md`](../360_Flow_Module_Page_DRAFT.md)

## Prototype screens (v0)

1. **Worklist** — manager queue: overdue, due this week, blocked; filter by process model and phase.
2. **Portfolio** — cross-case grid with phase status, deadlines, assignee; open case detail.
3. **Reporting** — snapshot metrics: volume by phase, overdue trend, avg days in phase (mock data).

## Out of scope (for now)

- Real Public 360° / Plan&Build integration
- ProcessView case-worker UI (separate surface)
- Auth, permissions, persistence
- Production design system compliance

## Open questions to resolve in iteration

- Desktop layout: single worklist vs configurable widget board?
- Reporting: operational (manager) vs governance (program) views?
- Relationship to existing Plan&Build webparts — extend vs replace?
- Which filters and follow-up actions matter most for NVE?
