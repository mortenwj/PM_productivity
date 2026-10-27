---
name: IFAR file-first processing workspace
status: draft
sources:
  - docs/product/briefs/ifar-file-first-processing-workspace/brief.md
  - docs/product/briefs/ifar-file-first-processing-workspace/addendum.md
  - te-industry-public360/docs/bmad/ifar-pfr-research.md
updated: 2026-09-30
---

# IFAR file-first processing workspace — Experience spine

> Behavioral and IA contract for the in-case IFAR processing UI. Visual identity is deferred to `DESIGN.md` (inherits Public 360° Online patterns where possible). This document owns *how it works*.

## Foundation

| Attribute | Choice |
|-----------|--------|
| Form factor | **Desktop-first web** inside Public 360° (access request case) |
| Primary user | Case handler (saksbehandler) processing innsyn/IFAR |
| Typical load | **~10–50 files** per case; inline workspace is the default path |
| Preview | FIB **`FileViewer`** (`@si/360-view-components`) — Accusoft via `GetFilePreviewInfo` (**verified**); IFAR **redaction params** — [spike](./spike-ifar-fileviewer-redaction-params.md) |
| Front-end stack | **FIB only** for new UI — no new BIF implementation |
| Legacy coexistence | v1 may ship with toggle to **classic BIF** in-case view during transition; FIB is default target |

Handlers stay in **one primary surface** (“Process files”) reachable from the case without losing wayfinding back to **case summary** and **registered request (innsynskrav)**.

## Information Architecture

### v1 surfaces (in scope)

| Surface | Entry | Purpose |
|---------|--------|---------|
| **Case shell** | Open access request case | Thin header: title, deadline, requester, responsible unit, case status |
| **Process files** (default for handlers) | Case tab / primary action “Process files” | File queue + inline preview + decisions + suggestions |
| **Request detail** | Link from case header | Registered request text, channels, dates — read-focused |
| **Case summary** | Link from header breadcrumb | Metadata, activities, dispatch — unchanged or lightly linked |
| **Redaction mode** | From preview toolbar when decision requires redaction | Full viewer redaction affordances; return to queue on save |

### Explicitly not v1 (linked out)

| Need | Where today / later |
|------|---------------------|
| Leader department overview | Innsynsoversikt web part (fast-follow) |
| Handler’s open cases across cases | My work / web part preset (fast-follow) |
| Very large requests | Access Request Report flow (handoff from Process files) |

### Layout model (desktop)

```text
┌─ Breadcrumb: Case › Innsynskrav › Process files ─────────────────────────┐
│ Case header: deadline · requester · 14 undecided · Next: Review files   │
├───────────────────────────┬──────────────────────────────────────────────┤
│ FILE QUEUE (primary)      │ PREVIEW (Accusoft)                           │
│ Filters · doc groups      │                                              │
│                           ├──────────────────────────────────────────────┤
│                           │ DECISION + SUGGESTION                        │
│                           │ Outcome · paragraph · remark · Accept/Edit   │
└───────────────────────────┴──────────────────────────────────────────────┘
```

On narrow viewports: queue stacks above preview+decisions; keyboard navigation remains required.

## Voice and Tone

Microcopy for Norwegian public-sector casework. Calm, precise, legally aware — not chatty, not gamified.

| Do | Don't |
|----|--------|
| “14 files without a decision” | “You're almost there!” |
| “Suggested: Full grant — same as case 2023/891 (15 Jun 2023)” | “AI recommends grant” |
| “Review required — newer file version since last decision” | “Warning!” |
| “Apply to all 3 files on this document” | “Bulk magic” |
| “You decide; the suggestion is based on prior processing” (once, in help) | Imply automation removes legal responsibility |

Use **innsyn / innsynskrav / sak** where the product language is Norwegian; English admin strings may appear in EN tenants — mirror locale.

## Component Patterns

Behavioral rules only; visual specs live in `DESIGN.md` when defined.

| Pattern | Role | Behavioral rules |
|---------|------|------------------|
| **Case progress strip** | Header | Shows counts: undecided, decided, needs redaction, blocked (sensitive). One **primary next action** label (e.g. “Continue file review”). |
| **Document group** | Queue | Collapsible row: document title/id, file count, group-level suggestion chip. Actions: **Apply to all** (when eligible), expand/collapse files. |
| **File row** | Queue | Status chip (undecided / granted / denied / partial / needs redaction). **Rejected** vs **not assessed** must be distinguishable (PFR **437295**). Suggestion badge if history exists. Optional later: **file size** column (PFR **254123**). Single click selects + loads preview. |
| **Inline preview** | Right top | Loads selected file; does not navigate away. Toolbar: zoom, page, open redaction if needed. |
| **Suggestion card** | Right bottom | Shows recommended outcome, paragraph, **reasoning** (case id, date, link to prior case read-only). Buttons: **Accept**, **Edit**, **Reject suggestion**. |
| **Decision form** | Right bottom | Same fields as today’s IFAR decision semantics (outcome, paragraph, remark). Pre-filled on Accept; editable on Edit. |
| **Exception banner** | Group or file | When bulk not allowed: “2 of 3 files match prior grant — review *fil-2.pdf* (newer version).” |
| **Handoff card** | Queue footer (edge) | If file count &gt; threshold (TBD, e.g. 50+) or user chooses: “Use Access Request Report for this case” with link/action. |

## State Patterns

| State | Where | Treatment |
|-------|--------|-----------|
| Loading case files | Queue | Skeleton rows matching group + file shape; preview area skeleton. |
| Empty queue | Process files | “No files on this request yet.” Primary: add documents/files (existing case action). |
| All decided | Header + queue | Progress strip complete; primary action → “Preview response” / next IFAR step (existing product flow). |
| No suggestion | Suggestion card | Hidden or minimal: “No prior decision found for this file.” Decision form still available. |
| Suggestion conflict | Document group | No **Apply to all**; list per-file badges; banner explains mismatch. |
| Newer file version | File row + suggestion | Suppress auto-grant suggestion or show “review required”; link to version info if product provides it. |
| Sensitive / classified | File or group | Suggestion/bulk **disabled or gated** (org policy TBD); row shows lock icon; tooltip explains why. |
| Preview error | Preview pane | Inline error + retry; queue selection unchanged. |
| Redaction in progress | Preview | Decision panel shows “Redaction required before grant”; save returns to queue with row state **needs redaction** cleared. |
| Suggestion accepted | File row | Status updates immediately (optimistic with rollback on failure); audit entry written server-side. |
| Legacy view | Case | Toggle or link “Open classic view” if coexistence required. |

## Interaction Primitives

**Goal:** scan **all files** with **limited clicking** — keyboard parity with mouse.

| Input | Action |
|-------|--------|
| `↑` / `↓` | Previous / next **file** in filtered queue |
| `Enter` | Accept current suggestion (if visible and enabled) |
| `E` | Focus decision form (edit) |
| `R` | Reject suggestion (clears prefill, keeps undecided unless user saves) |
| `G` | Toggle filter: **undecided only** |
| `Esc` | Clear preview focus / close nested panel |
| `Ctrl+Enter` / primary button | Save decision and **advance to next undecided file** (user preference, default on) |

**Mouse:** one click selects file; double-click does not open new window. Document group chevron expand/collapse.

**Banned in v1:** decision changes without explicit save; silent auto-apply of suggestions; bulk apply without confirmation when any file in group is not eligible.

## Accessibility Floor

- WCAG 2.2 AA target for the new workspace.
- File queue is a **single-select listbox** or table with row selection announced: file name, decision status, suggestion present.
- Suggestion card content available to screen readers **before** preview iframe where possible (reasoning text not trapped in viewer).
- Keyboard path must complete: select file → read suggestion → accept or edit → save → next file, without pointer.
- Focus order: breadcrumb → header actions → queue → preview (toolbar tab stop) → decision panel.
- Do not rely on color alone for status; text labels on chips.

## Key Flows

### Flow 1 — Process a typical email case (Ingrid, saksbehandler, 28 files)

**Climax:** Ingrid clears the undecided queue in one sitting without losing the case context.

1. Ingrid opens access request case **2026/1842** created from manual registration after email intake.
2. Case opens; banner shows **“18 files without a decision”** and primary action **Process files**.
3. She enters **Process files**. Queue loads grouped by document (4 documents, 28 files). Preview empty until selection.
4. First document group shows chip: **“Suggested: full grant for all 6 files — case 2024/1203”**. She expands, scans filenames, clicks **Apply to all**. System applies six decisions with shared reasoning; rows update to **Granted**; focus moves to first undecided in next group.
5. She selects **rapport-2025.pdf** (single file). Preview loads inline (Accusoft). Suggestion card: **Full grant**, paragraph prefilled, reasoning cites prior case. She reads two pages in preview, clicks **Accept**, then **Save and next**.
6. **personal-notat.docx** has badge **Review required — newer version since 2024 decision**. No Accept; she sets **Partial grant**, adds remark, saves manually, advances.
7. She uses `↓` to skim remaining files; four more Accept+Save; three manual denies without suggestions.
8. Progress strip shows **0 undecided**. Primary action: **Continue to response** (hands off to existing IFAR response flow).

### Flow 2 — Document bulk blocked by exception (Ingrid, same case)

**Climax:** She understands why bulk failed without mistrusting the product.

1. Document group **VED-44** (3 files) shows **“2 of 3 match prior grant”**.
2. **Apply to all** is disabled; banner names **bilag-3.pdf** (newer version).
3. She grants two files via individual Accept; opens **bilag-3.pdf**, reviews content, decides manually.
4. Group collapses to all decided.

### Flow 3 — Redaction detour (Ingrid)

**Climax:** Redaction does not break the scan loop.

1. File **intern-analyse.pdf** marked **needs redaction** for partial grant.
2. From preview toolbar she opens **Redact** (Accusoft). Completes redaction, saves.
3. Returns to same file row; decision panel unlocked; she sets partial grant + paragraph, **Save and next**.

### Flow 4 — Wayfinding back to request (customer pain: “roter seg bort”)

**Climax:** She never feels lost between sak and innsynskrav.

1. Mid-review, she clicks breadcrumb **Innsynskrav** — read-only request detail slides or navigates without closing case.
2. **Process files** tab remains one click away; queue **preserves filter and last selected file** when returning.

### Flow 5 — Handoff to large-case report (edge)

**Climax:** Product acknowledges scale without forcing the wrong tool.

1. Case with 52 files shows footer **handoff card**.
2. Ingrid chooses **Create Access Request Report** (existing capability); Process files remains available for exceptions afterward.

## Inspiration and Anti-patterns

**Lift from:**

- **Document review / e-discovery** — master-detail queue + inline viewer, keyboard next item.
- **Code review UIs** — suggestion with diff/reasoning, explicit accept.

**Reject:**

- **Wizard-only IFAR** — forcing linear steps for every case (handlers need overview first).
- **Auto-apply all suggestions** — legal accountability stays with handler.
- **Document tree as default** — documents are groups, not the primary navigation tree.
- **Separate window per file** — breaks scan loop; only redaction may use expanded viewer if required by Accusoft.

## Open UX questions (for PRD / spike)

- Exact **auto-advance** default after Save (on/off remembered per user?).
- Threshold for **report handoff** nudge (50 files vs. configurable).
- Coexistence UX: default tab **Process files** vs. classic for existing customers.
- Link pattern to **prior case** from reasoning (new tab vs. slide-over read-only).

## Wireframes

HTML low-fidelity screens (desktop split layout, Norwegian labels): [`wireframes/`](./wireframes/) — start at [`wireframes/index.html`](./wireframes/index.html).

| Screen | Maps to |
|--------|---------|
| `01-process-files-default.html` | Flow 1 — FIB FileViewer, size column, ArIn badge, suggestions, decision outcomes |
| `02-document-exception.html` | Flow 2 — 2 of 3 match, bulk disabled |
| `03-all-decided.html` | Handoff to produce/dispatch (existing IFAR) |
| `04-request-detail.html` | Flow 4 — wayfinding |
| `05-redaction-mode.html` | Flow 3 — redaction + ArIn findings panel, unsaved warning |

## Next steps

- **`bmad-prd`** — bind flows to requirements and API events (audit log fields).
- **`DESIGN.md`** — Public 360° token alignment, density, chip colors (when design pass runs).
- **FileViewer spike** — [redaction params + focus/performance smoke](./spike-ifar-fileviewer-redaction-params.md) (Accusoft-in-FIB already verified).
