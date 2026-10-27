# Code pointers — IFAR file-first workspace

Repository: **`te-industry-public360`** (paths below relative to repo root). Verified during brief work 2026-09-30.

## FIB FileViewer (inline preview)

| Area | Path |
|------|------|
| React component | `core-360-react-views/packages/360-view-components/src/FileViewer/FileViewer.tsx` |
| Preview API usage | `GetFilePreviewInfo`, iframe for **AccuSoft** (`FilePreviewOptions.AccuSoft`), query params e.g. `searchString`, `enableSelectTextTool` |
| Backend URL generation | `core-bl/.../FilePreviewManager.cs` — `GenerateAccusoftUrl` |

**Spike:** extend params for IFAR redaction (`enableRedaction`, highlight/search) — see `spike-ifar-fileviewer-redaction-params.md`.

## IFAR React (FIB)

| Area | Path |
|------|------|
| IFAR views app | `apps/ifar-views` |
| Note | Some flows use `enableRedaction=false` today — align with Process files redaction mode |

## Archive Inspector (reuse patterns)

| Area | Path |
|------|------|
| FIB sensitivity UI reference | `apps/ai-views/src/DocRegistration/DocRegistration.tsx` (FindingsTable + highlight) |
| Integration | **No IFAR ↔ ArIn integration in code today** — see `spike-archive-inspector-ifar-file-summary.md` |

## Other consumers of FileViewer / preview

- `case-components/FilePreview.tsx`  
- `ai-views` (Archive Inspector flows)

## PFR source (also in zip `reference-pfr/`)

- `docs/bmad/ifar-pfr-research.md`  
- `docs/bmad/ifar-pfr-index.csv`
