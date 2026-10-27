# POC learnings — Process Builder web app

**Captured:** 2026-09-08  
**Branch:** `feature/process-builder-poc`  
**Code:** `projects/process-builder/web/`

## What we built

- **React + Vite** web POC with Tietoevry brand kit
- **Three-pane authoring:** component palette → ordered canvas → argument inspector
- **11 activity types** from `flowworkunit-new-process` skill (not the v0 prototype’s six accordions)
- **Process metadata:** template scope, profile (progress-plan / background), naming scheme, feature toggles, phase deadline/warning
- **Generator:** `.wu` + `.xaml` download aligned to skill `templates.md` / `reference.md`
- **English UI** (Norwegian v0 reference retired for POC)
- **localStorage** persistence for saved process definitions

## UX decisions (supersede v0 prototype)

| v0 prototype | POC decision | Rationale |
|--------------|--------------|-----------|
| Accordion per activity type | **Drag-and-drop ordered list** | Matches skill discovery Q3 — order is sacred |
| Argumenter / Egenskaper tabs | **Metadata form + inspector on selection** | Simpler; same information surface |
| Six activity types | **Eleven types** incl. ShareWith, ClientAction, ProcessTask, DocumentReminder | Skill palette is authoritative |
| Norwegian + EN toggle | **English only** | Pilot/dogfood language for v1 |
| Flat list in sidebar | **Palette expands; saved processes collapse below** | All palette items visible without scroll |

## Generator — implemented vs deferred

| Area | Status |
|------|--------|
| Progress-plan shell (Assign, GetCurrentStageId, PhaseContainer) | ✅ |
| All 11 palette types → phase XML / wizard WaitTask | ✅ |
| Bool args + direct `[…]` bindings (no `CBool`, no `SendAutomatically`) | ✅ |
| Email/meeting nested milestones, subprocess `StageRecno` | ✅ |
| DocumentReminder → `WaitTask` on preceding wizard | ✅ (simple) |
| Feature toggles block in `.wu` | ✅ |
| Naming schemes (suffixed NVE, PAF single, hearing-style) | ✅ |
| Background process XAML (templates §17) | ❌ UI only; generation blocked |
| Localization GUIDs (`NVECustomLocalizationFile.js`) | ❌ omitted in v1 |
| Full document-reminder stack (expiry docs, ProcessDataHandler) | ❌ |
| OpenUrl via work-unit picker (§18) | ❌ manual URL only |
| Write to `output/` folder (vs browser download) | ❌ planned |
| Golden-file / PEToolkit automated tests | ❌ planned |

## Skill as product contract

The Cursor skill `flowworkunit-new-process` is not internal-only documentation — it is the **generation contract** for Process Builder. When the skill changes, these app files must sync:

- `web/src/types/components.ts` — palette + argument fields
- `web/src/lib/generator/context.ts` — indexing, DocumentReminder pairing
- `web/src/lib/generator/wu.ts` — `.wu` arguments
- `web/src/lib/generator/xaml.ts` — phase activities + `x:Members` parity

## Dogfood readiness

POC is sufficient for **internal spec validation** and **manual PEToolkit open** tests. Not yet sufficient for customer pilot without: output folder workflow, localization IDs, and scenario-based regression tests.

## Relationship to AI model creator spike

| Track | Output | User |
|-------|--------|------|
| **Process Builder** (this POC) | `.wu` + `.xaml` | Customer process owner |
| **AI-assisted process model creator** | JSON process model | Consultant experiment |

Parallel tracks; Process Builder does not use LLM generation in v1.
