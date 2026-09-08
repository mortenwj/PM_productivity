# Current state — Flow process authoring (2026-09-08)

Captured during BMAD discovery. Source: core-bl analysis + `flowworkunit-new-process` skill.

## What exists today

### Standard processes (product team)

- **Repo:** `core-bl/Source/si-bl-process-platform-build/WorkUnits/FlowWorkUnits/StandardProcesses/`
- Paired **`.wu` + `.xaml`** per process; shipped to `workunits/PAF/` on build
- Categories: NVE Processes, deficiency letters, templates, shared components

### Customer processes

- **Not in repo** — deployed per instance under `workunits/custom/`
- Emerging **WorkUnitRegistry** zip import path (assembler still incomplete)

### Authoring toolchain

| Layer | Tool | Who uses it |
|-------|------|-------------|
| Workflow design | Visual Studio + **ProcessEngineToolKit** NuGet (WWF designer) | Consultants (advanced), product team |
| Work unit metadata | `.wu` XML (arguments, categories, GUID, feature toggles) | Same |
| Process configuration | **PMC** in 360° Administrator (stages, stapc, argument XML) | Implementation / tenant admins |
| AI assist (internal) | Cursor skill `flowworkunit-new-process` | Product team via Cursor |

### Cursor skill (`flowworkunit-new-process`)

Encodes the **domain model** for creating valid process pairs:

1. **Discovery interview** — folder, names, **ordered activity list** (MilestoneDialog, DocumentFlowWizard, SendEmailDialog, etc.), feature toggles
2. **Templates** — XAML shell, phase activities, `.wu` skeleton (`templates.md`, `reference.md`, `examples.md`)
3. **Hard rules** — argument parity between `.wu` and `x:Members`, bool binding conventions, localization GUIDs, no invented activity sequences

The skill is effectively a **structured authoring contract** — not just code generation.

## Pain points (evident)

1. **VS + NuGet required** — consultants must open `FlowWorkUnits.sln`, use `packages.config`, ProcessEngineToolKit
2. **Split surfaces** — XAML in VS; PMC wiring in Administrator; no unified designer
3. **Argument duplication** — every `.wu` arg mirrored in XAML `x:Members`
4. **Manual project maintenance** — `.vbproj` entries, localization catalogs
5. **No web/self-service path** — admin UI configures args but does not design workflows

## Hypothesis (from product owner)

Use the **skill's discovery model + templates** as the foundation for a **web application** so consultants and customers can create processes without Visual Studio.
