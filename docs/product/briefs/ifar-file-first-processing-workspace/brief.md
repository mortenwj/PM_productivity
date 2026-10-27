---
title: IFAR file-first processing workspace
status: draft
created: 2026-09-29
updated: 2026-09-30
product: Public 360° — 360° Information Act Request (IFAR / access request)
module_product_number: 125877
author: Morten Jensen (with BMad product-brief facilitation)
---

# Product Brief: IFAR file-first processing workspace

## Executive Summary

Case handlers processing access requests (innsyn / IFAR) in Public 360° today work through a BIF-based experience that emphasizes **documents and case metadata**, while the real work happens at **file level**: read content, decide grant/deny/partial, redact, and assemble the response. Handlers report excessive clicking, weak overview, and unclear “what do I do next?” — especially for manually registered and email-driven requests, which dominate customer volume.

We propose a **new in-case processing workspace**: a file-first queue with **inline preview** (default: existing Accusoft File Viewer), keyboard-friendly navigation across tens of files per case, and **assisted decisions** that suggest outcomes at **file** and **document** granularity with explicit reasoning drawn from prior IFAR history (for example, prior full grant on the same document).

Version 1 focuses on the **inside-the-case** handler journey for typical cases (mostly tens of files, rarely above ~50). Leader queues, intake redesign, alternate closure paths, and partsinnsyn remain related but separate tracks. Success is measured by faster case processing, fewer navigation steps, and handler trust in suggestions — not by replacing the entire IFAR module at once.

**Platform constraint:** Public 360° has two front-end stacks — **BIF** (legacy) and **FIB** (modern). This initiative **must ship on FIB**. Replacing BIF UX with another BIF surface would increase UI inconsistency and long-term maintenance cost; the file-first workspace is an opportunity to **move IFAR casework onto FIB**, not to add a third pattern.

## The Problem

### Core mismatch

IFAR decisions are **file-granular**; the current overview surfaces **documents and metadata**. Handlers must often **open one file at a time** in separate flows to scan content and set decisions. That creates:

- Poor **situational awareness** (what is undecided, what is blocked, what is ready for response).
- High **interaction cost** (many detail views, easy to get lost between “case”, “request”, and document trees).
- **Unclear workflow** for everyday case managers — the experience feels built for **document management** specialists and journal-centric assumptions, not department case handlers.

### Customer evidence (Norwegian public-sector feedback)

A customer consolidated pain across the innsynsmodulen, including: confusing case navigation; habit clash (handlers used to normal document casework but forced into case-centric IFAR shells); heavy manual/email intake; large requests; requests not tied to a single document; cases without registered requests (no alert); need to close as “answered in another system”; sensitive/HR/training content and access control; partsinnsyn; weak **Innsynsoversikt** web part for leaders (filters not persisted); handler visibility of open work; default responsible unit for distribution; limited notification options; overall fit for central document management rather than distributed casework.

See `addendum.md` for the verbatim feedback list and theme mapping.

### Product First Request (PFR) evidence — Azure DevOps

Structured demand from **53 IFAR-tagged PFR Features** (plus 23 adjacent title matches), scanned 2026-09-30. Narrative: `te-industry-public360/docs/bmad/ifar-pfr-research.md`; row index: `ifar-pfr-index.csv`.

**Themes that reinforce the file-first workspace (in-case processing):**

| PFR theme | Count (IFAR corpus) | How the proposal responds |
|-----------|--------------------:|---------------------------|
| `document_volume` | 9 | File queue as the case “document/file list” (**300599** AST); scale path via reports (**178371**, **267711** 100-doc report cap) |
| `decisions_legal` | 10 | Per-file + document-bulk decisions; suggestion from prior grants (**179398** — paragraph-per-file unsustainable at 400+ files); clarify outcomes (**437295** Rejected vs Not assessed) |
| `redaction` | 7 | Redaction mode + Archive Inspector findings; unsaved redaction warning (**97210**); decision messaging (**368994**) |
| `automation_repeat` | 9 | Prior-grant suggestions (**64936**, **73721** history) — rules-based v1, not full auto-dispatch |

**Themes validated as separate tracks (still IFAR, not v1 wedge UI):**

| PFR theme | Count | Track |
|-----------|------:|--------|
| `dispatch_delivery` | 15 | Response/dispatch flows, hide produce-and-dispatch (**407246** / **408393**), email size (**208709**) |
| `intake_email` | 10 | Registration, requester contact (**177814**), dates (**177823**), responsible defaults (**177289**, **151982**) |
| `innsynsoversikt_ui` | 5 | Web part defaults (**271358**), picker UX (**189202**, **149838**) |
| `reporting_stats` | 10 | Statistics, fees/file counts (**269202**, **443449**), templates |
| `deadlines_calendar` | 6 | Provisional reply (**352837**), workdays/holidays (**211718**, **352850**) |

PFR does **not** replace qualitative customer notes; it **prioritizes** backlog alignment. Detail and ADO IDs: `addendum.md` § Product First Requests.

### Status quo cost

Handlers repeat decisions without systematic reuse of **prior grants** on the same material. Product concepts such as **Previous request** / historic decision context exist but are not positioned as **proactive guidance** during processing. Time-to-decision and error risk (inconsistent paragraphs, missed file versions) stay high.

## The Solution

Replace the primary **in-case IFAR processing UI** (BIF-based today) with a dedicated **file-first workspace** embedded in the access request case:

1. **Thin case header** — deadline, requester, status, and a clear **next step** (for example, “14 files undecided”).
2. **File queue (primary surface)** — all requested files visible with decision status, filters, and document grouping.
3. **Inline preview pane** — continuous review: select a file, preview updates in place; next/previous file with minimal or no full-page navigation.
4. **Decision panel** — grant/deny/partial, paragraphs, remarks; integrated with preview and queue state.
5. **Assisted suggestions** — when prior IFAR outcomes exist for the same logical content, show **recommended decision + short reasoning**; handler **accepts, edits, or rejects**; actions are auditable.
6. **Document-level bulk** — when all (or a defined subset of) files on a document share the same defensible prior outcome, offer **apply to all files on this document**, with explicit handling of **exceptions** (mixed history, newer file version, classified/sensitive flags).

For cases that occasionally exceed comfortable inline scale, the workspace should **defer gracefully** to existing **Access Request Report** flows rather than pretending one grid fits every edge case.

**Implementation stack:** **FIB** for all new UI (components, layout, navigation, state). **BIF** remains only as a temporary fallback behind a toggle during rollout if required — not as the target architecture.

**Preview (verified in code):** Reuse FIB **`FileViewer`** from `@si/360-view-components` — it already loads **Accusoft** via `GetFilePreviewInfo` / iframe (same pattern as Archive Inspector sensitivity review and case detail file preview). See [spike-ifar-fileviewer-redaction-params.md](./spike-ifar-fileviewer-redaction-params.md).

**Remaining technical work (narrow spike):** extend `FileViewer` query params for **IFAR redaction** (`enableRedaction` + existing `searchString`), plus performance/focus smoke when stepping through ~10–50 files — **not** a new Accusoft embed.

## What Makes This Different

| Aspect | Today (BIF / document-centric) | Target (FIB / file-first workspace) |
|--------|--------------------------------|-------------------------------------|
| Front-end stack | BIF | **FIB** (aligned with modern Public 360° UI) |
| Primary object | Document / case metadata | **File** (document as group + context) |
| Review pattern | Open one file at a time, many hops | **Scan queue + inline preview** |
| Prior decisions | Buried or passive (columns, separate sections) | **Active suggestions with reasoning** |
| Bulk work | Repetitive per-file clicking | **Document-level apply** where safe |
| Mental model | Document administration | **Case handler processing cockpit** |

This is not claimed as a novel legal engine — the differentiator is **execution**: aligning UI with how IFAR actually works and with how Norwegian customers describe casework, while reusing proven viewer and backend decision APIs where possible.

## Who This Serves

**Primary:** **Saksbehandler** / case handler — processes access requests in their unit, often from email or manual registration, typical case ~10–40 files.

**Secondary (v1 awareness, not primary UI):** Team lead distributing work — needs better queues and filters (customer pain on Innsynsoversikt); addressed in a **follow-on epic**, not v1 wedge.

**Out of primary persona for v1:** Document management central teams-only workflows; citizen requester (portal/eInnsyn intake unchanged in v1 unless explicitly scoped later).

**Success for the handler:** Open case → see all files and status → scan and decide in one place → understand why a suggestion appears → finish undecided queue → proceed to response preparation with confidence.

## Success Criteria

| Metric / signal | Target direction (to refine with baseline) |
|-----------------|---------------------------------------------|
| Navigation depth to set a file decision | Material reduction vs. current BIF flow (task study or instrumented click count) |
| Time to clear undecided files | Lower median for cases in 10–50 file range |
| Suggestion adoption | Meaningful share of **accepted** suggestions where history exists; low override rate due to wrong match |
| Handler confidence | Qualitative: “I can see what to do next” (customer language) |
| Wrong suggestion incidents | Near zero critical errors; version/conflict rules prevent blind bulk apply |
| Technical | Accusoft inline meets redaction + step-through performance for typical case size |

Business: improved customer satisfaction on IFAR UX, reduced training burden, stronger competitive story vs. “module feels built only for dokumentforvaltning”.

## Scope

### In scope (v1)

- New **in-case processing workspace** for access request cases (handler persona), implemented in **FIB**.
- **File list** with status, filtering (for example undecided, has suggestion), document grouping — addresses missing case-level file/document overview (**300599**, **178371**).
- **Inline preview** via FIB **`FileViewer`** (Accusoft when backend returns `FilePreviewOptions.AccuSoft`; pending redaction-params spike).
- **File-level** decision suggestions with reasoning from structured prior IFAR outcomes (**73721**, **64936** direction; rules not auto-dispatch in v1).
- **Document-level** “apply to all files on this document” when rules allow; exception UX when not (**179398**).
- Stable navigation among **case ↔ request ↔ file work** (address “roter seg bort”).
- Audit-friendly logging of accepted/rejected suggestions.
- **Decision semantics** in UI copy/controls: distinguish **rejected** vs **not assessed** where product supports it (**437295**).

### Partner / fast-follow (same initiative, separate deliverables)

- **360° Archive Inspector** integration: sensitivity indicator on file rows; findings panel in redaction mode (reuse FIB `ai-views` patterns). See `addendum.md` (Archive Inspector × IFAR).
- **File queue columns:** file **size** (and related metadata) in IFAR case view (**254123**, **208709**).
- **Redaction UX:** warn on close without save (**97210**); messaging on decision re-evaluation (**368994**).
- Persist **Innsynsoversikt** defaults on server (**271358** PFR); picker UX (**189202**); “my open” preset (**149838** context).
- Close path: **besvart i annet system** / dismiss without full dispatch.
- Case created **without registered request** — validation and notification.
- Richer notification schedules beyond once-before / daily-after expiry.

### Out of scope (v1)

- Full replacement of all IFAR touchpoints (intake scanners, GEMI, eArchive-specific UI, AutoIFAR admin).
- **Dispatch / produce-and-dispatch** policy UI (**407246**, **408393**) — configuration or separate flow; workspace hands off to existing response step.
- **Email intake automation** (**177814**, **177823**, **177289**, **430142** AutoIFAR on manual cases).
- **Statistics / all-units reporting** (**443449**), **deadline calendar** rules (**352837**, **211718**, **352850**), **FIN dispatch** tender items (**352872**).
- **Partsinnsyn** and alternate case-type workarounds.
- Deep redesign of sensitive/HR copy and access model (may constrain bulk suggest rules but not fully solved in v1).
- ML/black-box recommendations — v1 is **rules + prior case data**, not generative AI decisions.

### Open product decisions (pre-PRD)

- **Match key** for “same as last time” (document Recno, file version, archive key, etc.) — see `.decision-log.md`.
- Feature toggle / rollout strategy (pilot customers, **FIB default** with optional classic BIF fallback during transition).
- FIB integration pattern (case tab, route, web part host) and API surface to IFAR/back end.
- **Spike outcome:** [FileViewer redaction params](./spike-ifar-fileviewer-redaction-params.md) — Accusoft-in-FIB **verified**; confirm `enableRedaction` + highlight for IFAR.

## Vision

If v1 succeeds, IFAR in Public 360° becomes a **handler-centric processing product** on **FIB**: file queue and assisted decisions are the default; leader and intake surfaces reuse the same file/status model on FIB where applicable; suggestions incorporate version drift, classification, and org policy; **BIF IFAR processing views retire** for casework. Long term, the module fits **distributed public-sector casework** (email-heavy, not journal-only) without forcing every customer through document-management mental models.

## Next steps (BMad)

1. **`bmad-prd`** — requirements, non-functional, rollout, match-key rules, audit/compliance copy.
2. **`EXPERIENCE.md`** — key flows and IA (draft); **`DESIGN.md`** — visual pass when ready.
3. **Technical spikes** — [FileViewer redaction params](./spike-ifar-fileviewer-redaction-params.md) (short); [Archive Inspector file summary](./spike-archive-inspector-ifar-file-summary.md) (primary unknown).
4. **Customer validation** — review brief with source customer; confirm v1 wedge vs. web part pain.

Related artifacts: `.decision-log.md`, `addendum.md`, `EXPERIENCE.md`, `DESIGN.md`, `spike-ifar-fileviewer-redaction-params.md`, `spike-archive-inspector-ifar-file-summary.md`.
