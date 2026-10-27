# Addendum — IFAR file-first processing workspace

Detail that supports PRD and UX but does not belong in the executive brief.

## Product First Requests (ADO)

**Source (canonical in product repo):**

- Narrative: `te-industry-public360/docs/bmad/ifar-pfr-research.md`
- Index: `te-industry-public360/docs/bmad/ifar-pfr-index.csv`

**Corpus:** 53 PFR Features with `ImpactedModule = IFAR`; 36 still `New`; 23 adjacent title/keyword matches in CSV.

### PFR theme frequency → initiative mapping

| Theme | IFAR PFR rows | File-first v1 | Other track |
|-------|--------------:|---------------|-------------|
| `document_volume` | 9 | Queue overview, report handoff | eArchive add-from-search (**188808** adjacent) |
| `decisions_legal` | 10 | Suggestions, bulk-by-document, outcome labels | Terminology (**151691**) |
| `redaction` | 7 | Redaction mode + ArIn (v1.1) | Public variant PDF (**425386**) |
| `automation_repeat` | 9 | Prior-grant suggest only | AutoIFAR manual (**430142**), auto-dispatch (**64936**) |
| `dispatch_delivery` | 15 | Hand off to response | Hide produce/dispatch (**407246**), email registration (**402494**) |
| `intake_email` | 10 | — | Drag-drop requester (**177814**), dates (**177823**), RFA default (**151982**) |
| `innsynsoversikt_ui` | 5 | — | Server defaults (**271358**), React tab (**149838**) |
| `reporting_stats` | 10 | — | All units (**443449**), report titles (**267690**) |
| `deadlines_calendar` | 6 | — | Provisional reply (**352837**), workdays (**211718**) |
| `earchive_integration` | 6 | — | Import (**79828**), prior Acos history (**73721** — data for suggestions) |

### Representative PFR IDs — file-first workspace

| ADO | Title (short) | Shapes proposal |
|-----|----------------|-----------------|
| [178371](https://dev.azure.com/tieto-si/360/_workitems/edit/178371) | Many documents on access case | v1 queue + grouping; not one-off BIF navigation |
| [179398](https://dev.azure.com/tieto-si/360/_workitems/edit/179398) | Paragraph per file at 400+ files | Document-level apply + suggestions; report path for extreme size |
| [300599](https://dev.azure.com/tieto-si/360/_workitems/edit/300599) | List documents on case (AST) | File queue is primary case attachment view for processing |
| [437295](https://dev.azure.com/tieto-si/360/_workitems/edit/437295) | Rejected vs Not assessed misuse | Decision panel semantics + training copy |
| [254123](https://dev.azure.com/tieto-si/360/_workitems/edit/254123) | File size in IFAR case | Fast-follow column in queue |
| [267711](https://dev.azure.com/tieto-si/360/_workitems/edit/267711) | 100-doc cap on IFAR report from search | Explicit handoff card in workspace |
| [97210](https://dev.azure.com/tieto-si/360/_workitems/edit/97210) | Warn if redaction not saved | Redaction mode (Flow 3) |
| [271358](https://dev.azure.com/tieto-si/360/_workitems/edit/271358) | Innsynsoversikt server defaults | Confirms fast-follow web part (not v1) |

### PFR limitations (from research doc)

- Many rows lack `Custom.Source`; 16+ thin/empty/stub descriptions (RITM detail external).
- Adjacent corpus ≠ IFAR ownership — use for context only.

## Verbatim customer feedback (Norwegian)

Source: customer consolidation on innsynsmodulen improvements.

1. Mange detaljbilder og generelt forvirrende i innsynssak. Bygd for at kun dokumentforvaltning skal kunne manøvrere i sakstypen.
2. Kontra-intuitivt at saksbehandlere må fokusere på selve saken, ikke dokumenter, som de er vant til. Vi har sett at de lett roter seg bort etter gammel vane, og finner ikke tilbake til sak og innsynskrav.
3. Lite tilpasset manuell registrering av innsyn som kommer på epost andre kanaler. Det er her vi har størst del av innsynskrav. Veldig tungvint med større innsynskrav.
4. Ofte innsyn som ikke er knyttet til et spesifikt dokument.
5. Oppretter innsynssak uten krav (dette trigger ikke varsel).
6. Dårlig egnet for innsynskrav som besvares på annen måte, f.eks. i annet system. Burde hatt en enkel måte å «avskrive» innsynskravet på samt avslutte saken med «besvart på i annet system».
7. Innsyn i sensitive-, -opplærings- og personaldokumenter skaper utfordringer både med tanke på tilgangsstyring og sensitivt innhold som dras inn i innsynssaken.
8. Partsinnsyn — svardokument som skal være sensitiv — vi må bruke gammel rutine med egnet sakstype.
9. Webdelen «Innsynsoversikt» er veldig uoversiktlig og lite tilpasset for at ledere skal ha oversikt over åpne innsynskrav på sin avdeling (valg som settes på visning lagres ikke).
10. Kunne også vært lettere for saksbehandler å se sine åpne innsyn.
11. Skulle vært mulig å velge ansvarlig avdeling som «Default case responsible», slik at leder får til fordeling.
12. Varsel på innsynskrav — skulle vært flere valgmuligheter enn «en gang før utløp» og «hver dag etter utløp».
13. Hele modulen virker veldig tilpasset en offentlig journal uten fulltekstpublisering og at dokumentforvaltning (eller liknende avdeling) håndterer alle innsyn.

## Theme map → initiative

| Theme | Customer items | v1 file-first workspace | Track |
|-------|----------------|-------------------------|--------|
| A. Case shell vs. work objects | 1, 2 | Thin header; file queue; wayfinding to sak/innsynskrav | v1 |
| B. Scale / manual intake | 3 | Inline scan; bulk document apply; report handoff edge | v1 + existing reports |
| C. Request shape | 4, 5 | Not UI-only — intake/validation/notifications | Fast-follow |
| D. Alternate outcomes | 6 | Close/dismiss workflow | Fast-follow |
| E. Sensitive content | 7 | Guardrails on suggest/bulk | Rules in v1; deep fix later |
| F. Partsinnsyn | 8 | — | Later |
| G. Oversikt / my work / default unit | 9, 10, 11 | — | Fast-follow (web part) |
| H. Notifications | 12 | — | Config product |
| I. Product assumption | 13 | Positioning + handler-first UX | v1 narrative |

## Three-layer information model (navigation)

```
Case (deadline, requester, legal frame, status)
  └── Document (grouping, bulk suggest, familiar to handlers)
        └── File (decision, preview, redaction, response inclusion)
```

Brief positions **file** as processing unit and **document** as grouping — resolves apparent tension between “handlers want documents” and “decisions are on files”.

## Document-level suggestion rules (draft for PRD)

| Condition | Document-level action |
|-----------|------------------------|
| All files: same prior outcome on this document | Offer **Apply to all** with shared reasoning |
| Mixed prior outcomes | No bulk; show **N of M match — review exceptions** |
| Any file: newer version since last decision | Flag **review required**; block or warn on bulk |
| Classified/restricted (org policy) | Suppress or gate bulk/suggest per policy TBD |

## Example suggestion reasoning (UX copy)

- File: “Full grant on *vedlegg-1.pdf* in case 2023/891 (15 Jun 2023), paragraph …”
- Document: “Full grant on all files of document ABC-2024/567 in case 2023/891 — except *vedlegg-2.pdf* (newer file version).”

## FIB FileViewer / Accusoft (verified 2026-09-30)

- [x] **Accusoft embedded in FIB** — `360-view-components/FileViewer.tsx` + `GetFilePreviewInfo` / `FilePreviewManager.GenerateAccusoftUrl`.
- [x] **Reference UIs** — `ai-views/DocRegistration.tsx`, `case-components/.../FilePreview.tsx` (list + inline viewer).
- [ ] **IFAR redaction params** on FIB wrapper — see [spike-ifar-fileviewer-redaction-params.md](./spike-ifar-fileviewer-redaction-params.md).
- [ ] Confirm FIB components for queue, chips, split layout match Public 360° design system / FFUI patterns.
- [ ] Step through 30–50 files: acceptable load time and memory (smoke in redaction-params spike).

## Existing product hooks (research notes)

- Module: **360° Information Act Request** (product number 125877).
- Release/wiki mentions **Previous request** section for historic access decisions and paragraphs — candidate data source for v1 suggestions (confirm APIs and match rules in PRD).
- **Access Request Reports** for large requests; setting `requestforaccess.reportoverviewforsmallifarcases` governs report availability.
- **Historical notes** column referenced in customer-facing drafts — not fully verified in admin help; validate in Public 360° end-user help / same build as customer.

## Archive Inspector × IFAR file workspace (investigation 2026-09-30)

### How Archive Inspector works today

| Layer | What it does |
|-------|----------------|
| **Module** | 360° Archive Inspector (product **139187**). Cloud (Azure EU/NO); Norway GA, pilots SE/DK. Requires **360° File Viewer**; optional AFV for text quality. |
| **Detection** | Personal ID (FNR, D-number, DUF), bank accounts, passwords, personal health information — in **metadata and file content** (see wiki *Archive Inspector analyzes* → `aifs_filesensitive`, `aisd_aisensitivedetails`, tag codes). |
| **Admin entry** | Monitoring → **Review sensitive data** (regular/full scan results). Unregistered documents → **Register** → **Sensitivity review** window. |
| **FIB UI (reference)** | `core-360-react-views/apps/ai-views` → **SensitivityReportPage** (`DocRegistration.tsx`): left = document/file sections + **FindingsTable** (tag type, occurrence text, location); right = **FIB FileViewer** (`@si/360-view-components`). |
| **Finding → viewer** | Clicking a **file content** finding sets `searchString` on Accusoft preview and calls **`searchTextInPDF`** (PDF.js `find` / highlight) — **locates** sensitive text; does **not** auto-apply redaction rectangles in this flow. |
| **Flags** | `IsDocFileSensitive`, per-file `ScanStatus`, `FileContentTags` / `FileTitleTags` via **AIDataService** (e.g. unregistered document procedures). |
| **IFAR redaction today** | Accusoft File Viewer with IFAR module; setting **Enable Global Redact** (`file.htm` → IFAR). **ifar-views** (FIB/React) opens viewer with `enableRedaction=false` in some file-pick dialogs — redaction is a **separate** viewer mode, not wired to Archive Inspector findings. |

**Gap:** No code path links **IFAR access-request file processing** to Archive Inspector scan results or findings UI (`ai-views` has no IFAR references; `ifar-views` has no Archive Inspector references).

### Your desired UX (mapped)

1. **File overview** — icon or label when personal/sensitive information **has been detected** on that file (and optionally: not yet reviewed / N findings).
2. **Redaction mode** — when opening file(s) for redaction, **offer to redact** problematic areas (findings-driven).

### Recommended integration (FIB, reuse AI stack)

Build IFAR **Process files** in **FIB** (same as brief) and **compose** existing AI/Inspector patterns — do not rebuild detection in IFAR.

```text
┌─ IFAR Process files (new FIB app / ifar-views extension) ─────────────┐
│ File queue row: [decision chips] [ArIn: 3 findings · FNR, PHI]       │
├───────────────────────────────────────────────────────────────────────┤
│ Preview / Redact: FileViewer(enableRedaction=1) + Findings panel      │
│   · Reuse FindingsTable + navigation (from ai-views)                  │
│   · Optional: "Redact this finding" → jump highlight → user confirms  │
└───────────────────────────────────────────────────────────────────────┘
         ▲                              ▲
         │                              │
   New or extended API              Existing SI.Client.Api.AI /
   (batch by access-request         AIDataService tag model
    file recnos)                    (FileInfoResultModel tags)
```

**Phase 1 — Overview indicators (high value, lower risk)**  
- For each file on the access-request case, load sensitivity **summary** (scan status + tag counts/types), gated on `Subsetup.Archive_Inspector` (same check as `DocRegistration.tsx`).  
- Row UI: icon + tooltip (“Personal ID detected in file content (2 occurrences)”) + filter **Has sensitive findings**.  
- **Data:** Extend AI API with **GetSensitivitySummaryForFiles(fileRecnos[])** or reuse file list models if IFAR case files can be keyed like unregistered flow — **spike with AI team** (scan may be tied to document registration / regular analysis jobs today).  
- If file never scanned: show **Scan now** (call existing scan preprocessing / `UpdateScanStatus` pipeline) with clear latency + license note.

**Phase 2 — Redaction mode + finding-guided review (matches your story)**  
- Extend wireframe **05 Redaction mode**: left = compact queue; center = FileViewer with **`enableRedaction`** (extend FIB `FileViewer` params — today only `searchString` / `enableSelectTextTool` are passed to Accusoft URL).  
- Right or bottom = **FindingsTable** copied or shared from `ai-views` (package extract to `@si/360-view-components` or shared `ai-components`).  
- Click finding → highlight in viewer (existing `searchTextInPDF` pattern) → caseworker applies redaction in Accusoft tools.  
- Copy/disclaimer from Sensitivity review (`ReviewMessage`, transparency note) when showing AI findings in IFAR context.

**Phase 3 — “Apply suggested redactions” (only if product supports geometry)**  
- Current FIB flow suggests **where to look**, not one-click blackout. True **apply all suggestions** needs Accusoft redaction API + **coordinates** from Inspector (confirm with AI/File Viewer teams). Treat as **separate epic** until spike proves data exists.  
- Until then, label UX **“Review and redact findings”**, not “auto-redact”.

### Dependencies and constraints

- **License:** Archive Inspector + AI platform (commercial rule on wiki). Hide ArIn UI when module off.  
- **Market:** Inspector cloud/Norway-first — align with IFAR NO customers; disable or message elsewhere.  
- **Review state:** DB `aifs_isreviewed` — decide whether IFAR redaction counts as “reviewed” for Inspector audit trail (legal/AI governance).  
- **Ownership:** **AI3** (detection, APIs, scan jobs) + **IFAR/Core UI** (FIB workspace) + **File Viewer** (Accusoft params, redaction mode).

### Suggested scope placement

| Item | Suggestion |
|------|------------|
| Sensitivity **icon on file row** | **v1.1** or v1 if API spike is quick |
| Findings panel in **redaction mode** | **v1.1** (same release as redaction workspace) |
| One-click apply all redactions | **Later** — requires product capability proof |
| On-demand scan from IFAR case | **Spike** — may already exist for registered docs via regular analysis |

### PRD / spike questions for AI + File Viewer

1. Can we fetch **FileContentTags** / **ScanStatus** for **registered** files on an IFAR case by `df_recno` list?  
2. Does regular/full scan already cover access-request documents, or only unregistered / journal workflows?  
3. What Accusoft URL flags enable **redaction + searchString** together for IFAR? → [spike-ifar-fileviewer-redaction-params.md](./spike-ifar-fileviewer-redaction-params.md)  
4. Should accepting a finding in IFAR mark it reviewed in Archive Inspector?

## Rejected / parked for now

- **Full module UI rewrite in one release** — rejected; wedge is in-case processing workspace.
- **Generative AI decision text in v1** — parked; rules + prior cases only.
- **Duplicate PII detection inside IFAR** — rejected; integrate Archive Inspector only.
