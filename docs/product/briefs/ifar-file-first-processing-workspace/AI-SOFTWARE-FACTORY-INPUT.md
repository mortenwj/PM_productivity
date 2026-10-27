# AI software factory — input pack (IFAR file-first workspace)

**Purpose:** Onboarding bundle for an AI software factory to continue product and delivery work started in Cursor (PM_productivity), without losing decisions, evidence, or scope boundaries.

**Product:** Public 360° — **360° Information Act Request (IFAR / access request)** · product **125877**  
**Initiative:** Replace BIF-centric in-case processing with a **FIB file-first workspace** (queue + inline FileViewer + assisted decisions + redaction path).  
**Pack assembled:** 2026-10-22 (includes `ado-epic-draft.md`, `reference-handoff/agent-transcript-excerpts.md`, wireframes zip)  
**Brief status:** Draft (last updated 2026-09-30)

---

## Start here (reading order)

| Order | Artifact | Why |
|------:|----------|-----|
| 1 | [`brief.md`](./brief.md) | Problem, solution, scope v1 / fast-follow / out of scope, success criteria |
| 2 | [`.decision-log.md`](./.decision-log.md) | Accepted decisions + **open** items (match key, rollout, ArIn v1 vs v1.1) |
| 3 | [`addendum.md`](./addendum.md) | Verbatim customer feedback (NO), theme map, PFR ADO traceability, Archive Inspector × IFAR |
| 4 | [`EXPERIENCE.md`](./EXPERIENCE.md) | Persona **Ingrid**, IA, five flows, FIB FileViewer + ArIn intent |
| 5 | [`wireframes/index.html`](./wireframes/index.html) | Low-fi HTML screens 01–05 (open in browser) |
| 6 | Spikes | [`spike-ifar-fileviewer-redaction-params.md`](./spike-ifar-fileviewer-redaction-params.md) (2–3 d), [`spike-archive-inspector-ifar-file-summary.md`](./spike-archive-inspector-ifar-file-summary.md) (5–10 d) |
| 7 | [`reference-pfr/`](../reference-pfr/) *(in zip)* | 53 IFAR-tagged PFR Features — narrative + CSV index |
| 8 | [`CODE-POINTERS.md`](./CODE-POINTERS.md) | Verified code locations in `te-industry-public360` |

Optional background: [`reference-module-wiki-draft/360_Information_Act_Request_DRAFT.md`](../reference-module-wiki-draft/) — wiki module page draft (not scoped to this wedge).

---

## Problem statement (one paragraph)

IFAR decisions are **file-granular**, but the dominant in-case UI is **BIF** and **document/metadata-centric**. Handlers (especially email/manual intake) report excessive navigation, weak overview of undecided files, and no clear “what next?”. Prior grants exist in the product but are not **proactive suggestions** during processing. Customer feedback and **PFR** demand file lists, scale, redaction safety, clearer legal outcomes (e.g. rejected vs not assessed), and better leader queues — with **document_volume**, **decisions_legal**, and **redaction** as the in-case wedge.

---

## Solution thesis (one paragraph)

Ship a **FIB** “Process files” workspace: file queue (filters, document groups, optional size + Archive Inspector badges), **inline FIB `FileViewer`** (Accusoft already wired), decision panel with **rules-based suggestions** (file + document bulk with exceptions), redaction mode with findings panel (fast-follow), then hand off to **existing** produce/dispatch IFAR flows. **Do not** build new UI on BIF except optional classic toggle during rollout.

---

## v1 wedge vs not v1 (factory guardrails)

**In v1 UI:** Process files workspace, inline preview, suggestions, document bulk, wayfinding, rejected vs not assessed semantics where supported.

**Fast-follow / partner:** Archive Inspector row + redaction panel, file size column, unsaved redaction warning, Innsynsoversikt persistence, intake/dispatch/stats/deadlines tracks.

**Out of v1:** Full module rewrite, produce/dispatch hide policy UI, email intake automation, partsinnsyn, ML/black-box decisions.

Full tables: `brief.md` § Scope.

---

## Open decisions (must not be assumed closed)

1. **Match key** for prior-outcome suggestions (Recno, file version, archive ID, hash).  
2. **Sensitive/HR** — suppress or gate document-level bulk.  
3. **FIB mount** — tab/route, feature flag, BIF sunset plan.  
4. **ArIn in v1** — brief allows v1.1 unless API spike is fast; wireframes show target UX.  
5. **Innsynsoversikt in v1** — customer pain vs brief fast-follow (**271358**).

See `.decision-log.md` for full audit trail.

---

## Recommended factory next steps

1. **PRD** from brief + EXPERIENCE + PFR IDs in addendum (BMad `bmad-prd` or equivalent).  
2. **Run spikes** — FileViewer `enableRedaction` + IFAR params (short); Archive Inspector batch API for case files (blocking for ArIn UX).  
3. **Architecture** — FIB app entry in `ifar-views`, reuse `@si/360-view-components` FileViewer, backend suggestion/match API design.  
4. **UX** — wireframes 01→05 as acceptance sketches; `DESIGN.md` still placeholder (inherit Public 360° tokens).  
5. **Validation** — customer review of v1 wedge vs web part priority.

---

## Wireframes

- Folder: `wireframes/` (HTML + `wireframe.css`).  
- Also bundled: `ifar-file-first-wireframes.zip` (same content, shareable).  
- Screens: default queue, document exception, all decided, request detail, redaction + ArIn panel.

---

## Provenance

- Authored/facilitated in **PM_productivity** under `docs/product/briefs/ifar-file-first-processing-workspace/`.  
- PFR corpus canonical in **te-industry-public360** `docs/bmad/` (copied into this zip under `reference-pfr/`).  
- Code verification references **te-industry-public360** (see `CODE-POINTERS.md`).

---

## Suggested prompt for the factory agent

> You are continuing the IFAR **file-first processing workspace** for Public 360° (125877). Read `AI-SOFTWARE-FACTORY-INPUT.md`, then `brief.md`, `.decision-log.md`, and `EXPERIENCE.md`. Respect **FIB-only** new UI and v1 scope boundaries. Use wireframes as UX source of truth. Produce a PRD and implementation plan; run or specify the two spikes in `spike-*.md`. Do not expand scope to intake, dispatch, or Innsynsoversikt without explicit reprioritization.
