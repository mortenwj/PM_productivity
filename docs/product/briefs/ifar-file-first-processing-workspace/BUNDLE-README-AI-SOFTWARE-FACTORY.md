# AI software factory — input pack (IFAR file-first workspace)

**Unzip and start with this file.**

**Product:** Public 360° — **360° Information Act Request (IFAR)** · **125877**  
**Initiative:** FIB **file-first** in-case processing workspace  
**Pack date:** 2026-10-22  

**Regenerate zip (from PM_productivity repo root):** run wireframe pack then `uv run python docs/product/briefs/_pack_factory_input.py`

---

## Folder layout

| Path | Contents |
|------|----------|
| `workspace/` | Full initiative: brief, decisions, addendum, experience, design, spikes, wireframes |
| `reference-pfr/` | PFR research narrative + CSV (53 IFAR-tagged Features) |
| `reference-module-wiki-draft/` | Optional wiki module page draft (broader IFAR context) |
| `reference-handoff/` | Agent transcript excerpts + ADO epic draft |
| `reference-wireframes/` | `ifar-file-first-wireframes.zip` (HTML wireframes only) |

---

## Reading order

1. `workspace/brief.md` — problem, solution, scope  
2. `workspace/.decision-log.md` — decisions + open questions  
3. `workspace/addendum.md` — customer feedback, PFR ADO IDs, Archive Inspector  
4. `workspace/EXPERIENCE.md` — flows and IA  
5. `workspace/wireframes/index.html` — open in browser (screens 01–05)  
6. `workspace/spike-*.md` — technical spikes  
7. `workspace/CODE-POINTERS.md` — `te-industry-public360` code paths  
8. `reference-pfr/ifar-pfr-research.md` — PFR themes  
9. `reference-handoff/agent-transcript-excerpts.md` — user intent timeline from Cursor session  
10. `reference-handoff/ado-epic-draft.md` — paste-ready Azure DevOps Epic (also in `workspace/ado-epic-draft.md`)  
11. `reference-wireframes/ifar-file-first-wireframes.zip` — shareable wireframes-only bundle  

Also in `workspace/`: `AI-SOFTWARE-FACTORY-INPUT.md` (same guidance with in-folder links).

---

## Problem (short)

File-level IFAR work is forced through **BIF** document/case UI → poor overview, high click cost, weak reuse of prior grants.

## Solution (short)

**FIB** Process files: queue + **FileViewer** (Accusoft) + suggestions + document bulk → hand off to existing response/dispatch.

## Factory guardrails

- **New UI on FIB only** (BIF = optional classic fallback during rollout).  
- **v1 wedge** = in-case Process files; not intake, dispatch hide, or Innsynsoversikt unless reprioritized.  
- **Suggestions v1** = rules + prior structured outcomes, not ML.  
- **Open:** match key for suggestions, ArIn v1 vs v1.1, FIB route/toggle.

---

## Suggested agent prompt

> Continue IFAR file-first processing workspace (125877). Read this README, then `workspace/brief.md`, `workspace/.decision-log.md`, and `workspace/EXPERIENCE.md`. Honor FIB-only and v1 scope. Use wireframes as UX baseline. Deliver PRD + plan; specify or execute `workspace/spike-*.md`. Code repo: `te-industry-public360` per `workspace/CODE-POINTERS.md`.

---

## Provenance

Built in **PM_productivity** (`docs/product/briefs/ifar-file-first-processing-workspace/`). PFR from **te-industry-public360** `docs/bmad/`.
