# ADO Epic (draft) — IFAR file-first processing workspace

**Copy into Azure DevOps** as Epic work item. Adjust area path, iteration, and tags before save.  
**Product:** 360° Information Act Request · **125877** · module **IFAR**  
**Status:** Draft · 2026-10-22  
**Authoring context:** [brief.md](./brief.md), [.decision-log.md](./.decision-log.md), PFR corpus in `reference-pfr/`

---

## Epic title

**IFAR — FIB file-first in-case processing workspace (Process files)**

---

## Description

### Problem

Case handlers processing access requests (innsyn / IFAR) work at **file granularity** (read, decide grant/deny/partial, redact, assemble response), but the primary in-case UI is **BIF** and **document/metadata-centric**. That mismatch drives weak situational awareness, excessive navigation, unclear “what next?”, and poor fit for email/manual intake — where most customer volume sits.

Qualitative customer feedback and **53 IFAR-tagged Product First Requests** reinforce: need case-level **file lists**, scalable processing, clearer legal outcomes, redaction safety, and assisted reuse of prior grants — without replacing the entire IFAR module in one release.

### Proposed outcome

Deliver a **FIB-based “Process files” workspace** inside the access request case:

- File queue as primary surface (status, filters, document grouping)
- **Inline preview** via existing FIB **`FileViewer`** (Accusoft when configured)
- **Assisted decisions** — rules-based suggestions from structured prior IFAR outcomes (file + document bulk with exceptions)
- Stable **case ↔ access request ↔ file work** wayfinding
- **Redaction mode** handoff (extend FileViewer params; optional Archive Inspector findings — partner track)
- Graceful handoff to **existing** produce/dispatch response flows when queue is complete

**Platform:** All **new UI on FIB**. BIF may remain as optional **classic fallback** during rollout only.

### Success signals

- Material reduction in navigation depth to set a file decision (vs. current BIF flow)
- Lower median time to clear undecided files for typical cases (~10–50 files)
- Meaningful adoption of suggestions where history exists; near-zero critical wrong-match incidents
- Handler qualitative confidence: “I can see what to do next”

### Out of epic (explicit)

- Full IFAR module rewrite; intake/email automation; produce/dispatch policy UI; Innsynsoversikt web part defaults; statistics/deadlines; partsinnsyn; ML/black-box decision engines

---

## Acceptance criteria (epic level)

1. **FIB entry:** Handler can open **Process files** from an access request case on FIB with feature enabled; optional toggle to classic BIF view documented for rollout.
2. **File queue:** All requested files visible with decision state, filters (e.g. undecided, has suggestion), and document grouping aligned with wireframes `01–03`.
3. **Inline preview:** Selecting a file updates in-place preview via FIB `FileViewer` without full-page navigation for typical case sizes.
4. **Decisions:** Handler can set file-level outcomes including distinction of **rejected vs not assessed** where product supports it (PFR **437295**).
5. **Suggestions:** When prior structured outcomes exist, system shows recommendation + short reasoning; handler must **accept, edit, or reject**; acceptance is auditable.
6. **Document bulk:** “Apply to all files on this document” when rules allow; clear exception UX when histories diverge or versions differ (PFR **179398**).
7. **Completion:** When no undecided files remain, clear **next step** to existing response/dispatch IFAR flow (not reimplemented in this epic).
8. **Performance:** Stepping through ~10–50 files in one session is usable (preview load + focus); extreme cases defer to Access Request Report (PFR **267711** context).
9. **Documentation:** PRD/architecture references code pointers (`FileViewer`, `ifar-views`, spikes) and open decisions (match key, ArIn v1 vs v1.1).

---

## Suggested child Features (for ADO breakdown)

| Feature (draft title) | Intent | PFR anchors |
|----------------------|--------|-------------|
| FIB Process files shell & navigation | Tab/route, breadcrumb, case header stats, BIF fallback toggle | **300599**, **178371** |
| File queue & filters | Undecided/all/suggestion/sensitive filters; document groups | **300599**, **254123** (size fast-follow) |
| Inline FileViewer integration | Reuse `@si/360-view-components` FileViewer; keyboard next/prev | Spike: redaction params |
| Decision panel & outcomes | Grant/deny/partial, paragraphs, rejected vs not assessed | **437295** |
| Prior-outcome suggestions (rules v1) | File + document-level suggest; accept/edit/reject audit | **73721**, **64936**, **179398** |
| Document bulk apply & exceptions | 2-of-3 match pattern; disable when unsafe | **179398** |
| Redaction mode (v1) | Detour from queue; save/return; unsaved warning | **97210**, **368994** |
| Archive Inspector indicators (partner) | Row badge + findings panel in redaction | ArIn spike |
| Technical spikes (timeboxed) | FileViewer `enableRedaction`; ArIn batch API for case files | — |

---

## Related work / dependencies

- **te-industry-public360:** `apps/ifar-views`, `FileViewer.tsx`, `FilePreviewManager.cs`
- **Spikes:** `spike-ifar-fileviewer-redaction-params.md`, `spike-archive-inspector-ifar-file-summary.md`
- **UX:** `EXPERIENCE.md`, wireframes `01–05`

---

## Tags (suggested)

`IFAR`; `FIB`; `file-first`; `PFR-aligned`; `125877`; `handler-UX`

---

## HTML description (optional paste block)

```html
<p><strong>Problem:</strong> File-granular IFAR work through BIF document-centric UI — poor overview and high navigation cost.</p>
<p><strong>Solution:</strong> FIB Process files workspace — queue, inline FileViewer, rules-based suggestions, document bulk, handoff to existing dispatch.</p>
<p><strong>Constraints:</strong> FIB-only new UI; v1 not intake/dispatch/web part; suggestions rules-based not ML.</p>
<p><strong>Artifacts:</strong> PM_productivity brief pack + wireframes + PFR reference.</p>
```
