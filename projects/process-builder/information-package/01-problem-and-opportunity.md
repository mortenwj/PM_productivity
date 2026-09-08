# Problem and opportunity — Process Builder

## The problem (draft)

360 Flow customers who need **custom processes** today depend on implementation consultants or advanced internal staff. Authoring requires:

- Visual Studio with ProcessEngineToolKit
- Paired `.wu` and `.xaml` files with strict argument parity
- Separate PMC configuration in 360° Administrator

Most **customer process builders** cannot realistically own this toolchain. They wait on consultants, pay for change requests, or run with processes that do not fit their case handling — while the product team has already codified safe authoring patterns in an internal Cursor skill (`flowworkunit-new-process`).

## The opportunity

Productize that skill as a **customer-facing web application**: guided discovery (ordered activities, toggles, validation) → generated WU/XAML → deploy to the customer's instance. Start with the **80%** of processes that follow linear phase-activity patterns the skill already supports.

## Primary audience

**Customer process builders** — tenant staff who configure how cases move through stages, not implementation consultants (consultants may still assist, but are not the v1 design center).

## v1 output (confirmed)

| In v1 | Later |
|-------|-------|
| Generate `.wu` + `.xaml` (A) | Full process model modeling (stages, milestones, PMC graph) |
| Deploy to customer instance (B) | Branching/state-machine complexity beyond skill palette |
| Activity types from skill today | Shared components, advanced subprocess edge cases |

## Success signal (hypothesis — to validate)

A customer process builder can create and deploy a new linear Flow process **without Visual Studio or a consultant**, and attach it in their environment within one working session.
