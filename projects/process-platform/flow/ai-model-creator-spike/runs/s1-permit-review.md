# S1 review — permit application (dry-run)

**Artifact:** `runs/s1-permit.json`  
**Mode:** dry-run (fixture — not live OpenAI)  
**Reviewers:** Morten (product) + _consultant TBD_  
**Date:** 2026-06-17

## Minimum structure checklist (from scenarios.md)

| Requirement | Met? | Evidence |
|-------------|------|----------|
| Stages Intake → Assessment → Decision → Closure | Yes | Four stages, `order` 1–4 |
| Milestones on transitions | Yes | Each stage has ≥1 milestone; transitions named |
| Activities: completeness, technical assessment, decision recording, notification | Yes | `act-completeness-check`, `act-technical-assessment`, `act-decision-recording`, `act-notify-applicant` |
| Deadline notes (assessment, decision) | Yes | `annotations` with `type: deadline` on both stages |

## Scoring (1–5)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Structural plausibility | **5** | Linear permit lifecycle matches how a consultant would whiteboard; receive → assess → decide → notify → close is coherent. |
| Flow semantic alignment | **4** | Uses Process Model / Stage / Milestone / Activity; `buildingBlockRef: notification-pattern` is Flow-ish but generic; no Progress Plan instance (correctly scoped out in description). |
| Consultant edit effort | **4** | **Light edit** — structure is usable; would need PMC bindings, Work Unit refs, and concrete building-block IDs from SharedComponents/StandardProcesses. |
| Grounding / hallucination | **4** | No invented activity types; `notification-pattern` is plausible but not tied to a real `.wu` / GUID. |
| Latency & completeness | **5** | Complete JSON; dry-run instant (live TBD). |

**Average:** 4.4 — **PASS** (threshold ≥ 3.0, no dimension at 1)

## Consultant gap note

1. **Correct as-is:** Stage order, activity names, milestone transitions, deadline annotations, separation of assessment vs decision.
2. **Must change:** Map activities to Work Units or template refs; replace `notification-pattern` with a real SharedComponents name/GUID; add PMC-relevant stage keys if this were imported; notification arguably belongs partly in closure stage depending on delivery convention.
3. **Effort:** **light edit** (structure) + **medium** if mapping to deployable XML/XAML.
4. **Failure mode tag:** `grounding` (building blocks not resolved to repo assets)

## Verdict (S1 dry-run only)

**Proceed to live S1** — fixture proves the JSON IR is reviewable and meets minimum structure. Experiment still needs live OpenAI output scored the same way.

## Your adjustments

- Product scores confirmed: **yes** (2026-06-17)
- Consultant review: pending
- Live S1 run scored: pending

**Note on notification placement:** `act-notify-applicant` sits under stage `decision` (order 3), not `closure` (order 4). Closure only has `act-close-case`. This is a modeling choice, not a JSON bug — consultants may prefer notify in Closure; current draft groups notify with decision recording.
