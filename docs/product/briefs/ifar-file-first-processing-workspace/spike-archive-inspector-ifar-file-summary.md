---
title: Spike — Archive Inspector file sensitivity for IFAR Process files
status: draft
created: 2026-09-30
audience: Archive Inspector / AI (si-bl-ai-build), IFAR, FIB File Viewer
parent: ifar-file-first-processing-workspace brief
timebox: 5–10 engineering days (suggest)
---

# Spike brief: File sensitivity summary for IFAR access-request files

## Context

We are designing a **FIB-based, file-first IFAR processing workspace** (see [brief.md](./brief.md)). Product intent:

1. **File queue:** icon or short explanation when Archive Inspector has detected personal/sensitive information on a file.
2. **Redaction mode:** when the caseworker opens redaction, surface **findings** and guide them to problematic areas (same mental model as **Sensitivity review** for unregistered documents).

This spike determines whether we can **reuse existing AI/Inspector data and APIs** for **registered files on an access-request case**, or what minimal backend work is required before UI starts.

## What exists today (confirmed in codebase)

| Asset | Location / behaviour |
|-------|----------------------|
| FIB Sensitivity review UI | `core-360-react-views/apps/ai-views` → `DocRegistration.tsx` (`SensitivityReportPage`) |
| Findings list + viewer navigation | `FindingsTable.tsx`, `searchTextInPDF` → Accusoft/PDF highlight by matched **text** |
| File viewer (FIB) | `packages/360-view-components/FileViewer.tsx` — passes `searchString`, `enableSelectTextTool` to Accusoft preview URL |
| AI client API | `SI.Client.Api.AI` / `AIDataServiceHandler`, models e.g. `FileInfoResultModel`, `UnregisterDocumentDetailsModel` (`IsDocFileSensitive`, `Tags`, `ScanStatus`) |
| IFAR FIB | `apps/ifar-views` — **no** Archive Inspector integration today |
| Persistence | Wiki *Archive Inspector analyzes* — `aifs_filesensitive`, `aisd_aisensitivedetails`, tags, `aifs_isreviewed` |

**Not in repo today:** IFAR case file list enriched with Inspector tags.

**Verified (see [spike-ifar-fileviewer-redaction-params.md](./spike-ifar-fileviewer-redaction-params.md)):** FIB **`FileViewer`** already embeds Accusoft; gap is **`enableRedaction`** (and IFAR) query params on the wrapper, not a new viewer host.

## Spike goal

**Primary question:** Can the IFAR Process files queue show, per file, a **reliable sensitivity summary** (scan status + tag types/counts) for all files attached to an access-request case?

**Secondary questions:**

1. Are those files **already scanned** by regular/full Archive Inspector jobs, or only unregistered-document / registration flows?
2. If not scanned, can we **trigger analysis** from IFAR context (which job/API, latency, licensing)?
3. Can we fetch findings in **one batch call** for N file recnos (typical case ~10–50 files)?
4. For redaction mode: can Accusoft preview accept **`enableRedaction` + `searchString`** together for IFAR files? *(Tracked in [spike-ifar-fileviewer-redaction-params.md](./spike-ifar-fileviewer-redaction-params.md) — out of this spike unless blocked.)*
5. When a caseworker redacts from IFAR, should Inspector **`reviewed`** state update (audit/compliance)?

## Out of scope for this spike

- Building the full IFAR Process files UI.
- One-click “apply all redactions” from AI coordinates (separate epic; likely needs geometry not used in current `ai-views` flow).
- Replacing Archive Inspector models or training new detectors.

## Proposed spike tasks

### 1. Data path (AI / backend) — owner: AI team

- [ ] Pick a **test access-request case** in dev (NO cloud) with known sensitive content in attached files.
- [ ] Trace whether **`aifs_filesensitive` / tags** exist for those `df_recno` values after normal operations.
- [ ] Document which **scan types** populate findings (regular analysis, full analysis, doc registration only, on-demand).
- [ ] List **existing procedures** (or gaps) equivalent to:
  - `GetFilesForUnregisteredDocuments` / `GetUnregisteredDocumentDetails`
  - but for **registered files on a case** or **IFAR request document set**.
- [ ] If gap: sketch **minimal new API** e.g. `GetFileSensitivitySummariesForFiles(int[] fileRecnos)` returning per file:
  - `ScanStatus`, `HasFindings`, `TagSummary[]` (code, description, count), optional `IsReviewed`
  - Optional detail endpoint for redaction panel: same shape as `FileContentTags` / `FileTitleTags` on `FileInfoResultModel`.

### 2. Scan trigger (if needed) — owner: AI team

- [ ] If case files are often **not analyzed**, identify approved way to **queue scan** from IFAR (reuse `UpdateScanStatus` / scan preprocessing — see release note on UpdateScanStatus API fix Aug 2026).
- [ ] Define UX constraints: max wait time, polling pattern (reuse `useStatusPolling` from `ai-views`?).

### 3. Integration sketch — owner: PM + AI + IFAR

*(FIB FileViewer / Accusoft / redaction params: [spike-ifar-fileviewer-redaction-params.md](./spike-ifar-fileviewer-redaction-params.md).)*

- [ ] Confirm **module gate**: `Subsetup.Archive_Inspector` (same as `DocRegistration.tsx`).
- [ ] Confirm **license/market** messaging when module off (Norway-first).
- [ ] Agree **reviewed-state** rule when user completes redaction from IFAR.

## Success criteria (spike done)

| Criterion | Pass |
|-----------|------|
| Written **answer** to primary question with evidence (DB row, API response, or explicit gap) | Required |
| **Sample JSON** (or procedure names) for batch file summary on one real IFAR case | Required |
| **File Viewer** note: redaction + highlight feasible Y/N | See fileviewer spike (parallel) |
| **Effort estimate** for net-new API (if any) and for UI composition (reuse FindingsTable) | Required |
| **Recommendation**: v1 include row indicators Y/N; redaction panel same release or +1 | Required |

## Deliverables

1. Short **spike report** (Confluence or markdown in repo) linked from this file.
2. **ADO items** (if created): API, FileViewer params, IFAR UI composition (separate from this spike).

## Suggested participants

- Archive Inspector / **AI** backend (`si-bl-ai-build`)
- **IFAR** product/dev (`ifar-views`)
- **FIB** / **360-view-components** (FileViewer)
- PM: Morten Jensen

## References

- [addendum.md](./addendum.md) — section *Archive Inspector × IFAR file workspace*
- [EXPERIENCE.md](./EXPERIENCE.md) — Flow 3 redaction; wireframe `05-redaction-mode.html`
- Wiki: [360° Archive Inspector](https://wiki.software-innovation.com/wiki/360%C2%B0_Archive_Inspector)
- Admin: [360° Archive inspector](https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/360archiveinspector.htm) — Review sensitive data; Sensitivity review on registration
- Code entry: `core-360-react-views/apps/ai-views/src/DocRegistration/DocRegistration.tsx`

## Timebox

**5–10 engineering days** total across AI + File Viewer (parallel). If primary question is “no data for registered IFAR files without new scan job”, stop early and size the API/job work instead of prototyping UI.
