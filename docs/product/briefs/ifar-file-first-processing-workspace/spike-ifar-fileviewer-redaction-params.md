---
title: Spike — FIB FileViewer redaction params for IFAR Process files
status: draft
created: 2026-09-30
audience: Core UI / IFAR (ifar-views), File Viewer
parent: ifar-file-first-processing-workspace brief
timebox: 2–3 engineering days (suggest)
related: spike-archive-inspector-ifar-file-summary.md
---

# Spike brief: FIB FileViewer + IFAR redaction (narrow)

## Verified (2026-09-30) — no spike needed for “embed Accusoft in FIB”

Accusoft is **already embedded in FIB** via shared component **`FileViewer`** (`core-360-react-views/packages/360-view-components/src/FileViewer/FileViewer.tsx`):

- Loads preview through FIB **`GetFilePreviewInfo`** → `FilePreviewManager.GenerateAccusoftUrl` → iframe (`si-fib-fileviewer-iframe`).
- When `FilePreviewOptions.AccuSoft`, appends **`searchString`**, **`isdoccommitted`**, **`enableselecttexttool`** to preview URL.
- **In production use:** Archive Inspector sensitivity review (`apps/ai-views/DocRegistration.tsx`), case detail file panel (`case-components/.../FilePreview.tsx`), OpenGov `FilesTab`, generic `FilePreviewComponent`.

**IFAR Process files should compose this component** (same pattern as case `FilePreview` + `ai-views`), not build a new viewer host.

## Remaining gap (this spike)

FIB **`IFileViewerParams`** does **not** yet expose **`enableRedaction`** (and related IFAR flags). Legacy IFAR/BIF URLs add query params manually, e.g. `enableRedaction=true/false` in `ifar-views` file-list dialogs.

| Task | Owner | Done when |
|------|--------|-----------|
| Confirm Accusoft URL supports **`enableRedaction` + `searchString`** together for IFAR-licensed files | File Viewer / Core UI | Documented param combo + test file on dev |
| Extend **`IFileViewerParams`** + `FileViewer.tsx` to append **`enableRedaction`** (and any required `enable360` etc.) when AccuSoft | Core UI | PR or spike branch |
| Verify **permissions** (`CanUserPerformRedaction`) match IFAR rules in inline mode | IFAR + Core UI | Y/N with notes |
| **Performance smoke:** switch among 20–30 IFAR case files without iframe leak / unacceptable reload | IFAR UI | Subjective pass + any metrics |
| **Keyboard focus:** queue → iframe → decision panel (a11y smoke) | IFAR UI | Known issues logged |

## Out of scope

- New preview server or non-Accusoft embed.
- Full Process files UI build.
- Archive Inspector APIs (see [spike-archive-inspector-ifar-file-summary.md](./spike-archive-inspector-ifar-file-summary.md)).

## Success criteria

- Written confirmation that IFAR workspace can use **`FileViewer`** with **redaction enabled** and optional **finding highlight** (`searchString`).
- Effort estimate to merge param extension (if not done in spike).

## References (repo)

- `packages/360-view-components/src/FileViewer/FileViewer.tsx`
- `core-bl/.../File/Manager/FilePreviewManager.cs` — `GenerateAccusoftUrl`
- `packages/fib-bl-api/.../FilePreviewOptions.ts` — `AccuSoft = 2`
- `apps/ifar-views/.../ColumnRenderers.tsx` — legacy `enableRedaction=false` URL pattern
