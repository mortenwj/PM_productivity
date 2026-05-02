---
name: feature-scoping
description: >-
  Generates scoped feature documents for sprint execution using territory
  classification and risk scenarios. Produces sprint cards with acceptance
  criteria and risk assessments. Use when user says "scope this feature",
  "sprint planning", "feature scoping", "estimate this", or provides a DevOps
  work item to scope. Do NOT use for general triage (use /triage-requests) or
  edge case analysis (use /edge-cases).
allowed-tools: Read Write Edit Bash Grep Glob mcp__azure-devops__wit_get_work_item mcp__azure-devops__wit_get_work_items_batch_by_ids mcp__azure-devops__wit_create_work_item mcp__azure-devops__wit_add_work_item_comment
context: fork
category:
  - productivity
  - development
---

# Feature Scoping

Scope features for sprint planning by classifying known vs. unknown territory and presenting risk scenarios instead of flat time estimates.

## Pipeline Position

```
triage-requests (optional upstream) --> feature-scoping --> edge-cases (downstream)
```

This skill accepts input from three sources:
1. An Azure DevOps work item ID (fetched automatically)
2. A triage output file from `/triage-requests` (read from Obsidian)
3. Raw text (pasted feature request, Teams message, email)

## Phase 0: Political Context

Before any analysis, ask the user:

1. **Who initiated this request?** (PM, customer escalation, internal engineering, leadership)
2. **What is the implied or stated deadline?** (sprint boundary, customer promise, release date, or "no deadline")
3. **Is there a linked Azure DevOps work item?** (If yes, fetch it via `mcp__azure-devops__wit_get_work_item`. If no, the request is informal.)

### GATE 1: Political Context Anchor

**Block condition:** Requestor is "unknown" AND deadline is "unknown" AND no DevOps item linked.

**Action:** "I need at least one anchor: who asked for this, when it's needed, or a DevOps item number. Which can you provide?"

If the user says "I don't know the deadline," treat it as "next sprint" and flag this assumption explicitly in the output document.

**Exit criteria:** At least one context anchor is confirmed (who, when, or work item ID). Gate 1 passed.

## Phase 1: Request Decomposition

Break the request into atomic verifiable questions. Each question must be specific enough to answer with evidence.

If a DevOps work item exists, extract: title, description, acceptance criteria (if any), tags, and comments.

If the input is raw text, parse it into structured claims about what the feature should do.

**Decomposition format:**

For each atomic question:
- Restate in plain language: what specifically needs to happen?
- Identify the technical domain: API, UI, infrastructure, integration, data model?
- Flag knowledge gaps: what do we not yet know?

Show the full decomposition to the user before proceeding: "Here's how I'm reading this feature. Correct?"

### GATE 2: Specificity Check

**Block condition:** Any atomic question contains "improve", "support", "better", or "system" without a concrete measurable qualifier.

**Action:** "The question '[vague text]' is not specific enough to classify or estimate. What exact behavior should change?"

Rewrite the question with the user's input and re-present.

**Exit criteria:** All atomic questions have concrete measurable qualifiers. User confirmed the decomposition. Gate 2 passed.

## Phase 2: Territory Classification

Read `references/territory-patterns.md` for the known territory catalog.

For each atomic question from Phase 1, classify it:

### Known Territory (High Confidence)
The implementation pattern exists in the portfolio. A reference file path can be cited. The work is predictable.

**Estimation:** Effort size (S/M/L). Duration is implicit from the pattern.

### Adjacent Territory (Medium Confidence)
A partial precedent exists but needs adaptation. The general approach is clear; specific details are not.

**Estimation:** Effort range (e.g., M-L). Flag which part is uncertain.

### Unknown Territory (Low Confidence)
No precedent in the portfolio. External API with untested behavior. New architectural pattern. First-time integration.

**Estimation:** Do not estimate. Define a timeboxed spike task instead.

Present the territory map to the user as a table. The user can challenge any classification.

### GATE 3: Unknown Territory Spike Requirement

**Block condition:** Any item classified as Unknown Territory AND the user chooses full scope (Option A in Phase 3) AND no spike task is defined.

**Action:** "Unknown territory must have a timeboxed spike. What's the timebox? (Recommended: 1 day maximum.)"

**Exit criteria:** Every atomic question has a territory classification (Known, Adjacent, or Unknown). User reviewed and accepted the territory map. Gate 3 passed for any Unknown items.

## Phase 3: Risk Scenarios

Present two scenarios for the full feature:

### Happy Path
Everything goes as expected. Dependencies cooperate. Known territory executes cleanly. State the expected effort and duration for the known components.

### Blow-Up Risk
What could derail the sprint? One specific risk per Unknown or Adjacent territory item. Not a laundry list; the single most likely failure mode for each.

### Scope Options

**Option A: Full scope.** All components, accepts risk from Unknown territory. Include spike tasks for unknowns.

**Option B: Reduced scope.** Only Known and Adjacent territory. Ships on time with high confidence. Unknown items deferred to next sprint or converted to spikes.

If the Phase 0 deadline is a fixed customer date, never present Option A if it risks missing that date. Default to Option B and explain why.

The user must choose Option A or Option B before proceeding.

### GATE 4: Explicit Out of Scope

**Block condition:** The "Out of Scope" section in the draft is empty.

**Action:** "What's explicitly out of scope for this sprint? Name at least one thing that was considered and cut."

Scope creep starts with silence. If nothing is out of scope, everything is negotiable mid-sprint.

**Exit criteria:** User chose Option A or Option B. Out-of-scope section has at least one item. Gate 4 passed.

## Phase 4: Output

Write the scoped feature document to Obsidian using the template in `references/output-template.md`.

**File path:** `[output-dir]/[project-name]/Scoping/[YYYY-MM-DD]-[feature-name]-scope.md`

### GATE 5: Testable Acceptance Criteria

**Block condition:** Any acceptance criterion contains "produces expected output", "is fast", "is better", "is improved", or other unmeasurable language.

**Action:** "Criterion '[text]' is not testable. What specific, observable behavior can you verify?"

### DevOps Integration

After writing the Obsidian document, offer (do not auto-execute) to:
1. Create a DevOps work item with the acceptance criteria and territory classification
2. Add a comment to an existing DevOps work item with a link to the scoping document

### Downstream Handoff

At the end of the document, include a pre-filled context block for `/edge-cases`:

```
## Next Steps

Run edge case analysis before development begins:

/edge-cases

Feature: [feature name]
Happy path: [one sentence from "What We're Building"]
Data: [data types the feature works with]
External systems: [APIs and integrations identified in territory map]
Permissions: [user roles from decomposition]
Known risks: [blow-up risks from Phase 3]
```

**Exit criteria:** Scoping document written to Obsidian. All acceptance criteria are testable (Gate 5 passed). User offered DevOps integration. Downstream handoff block included.

## Hard Gates Reference

| Gate | Phase | Block Condition | User Prompt |
|------|-------|----------------|-------------|
| 1 | 0 | All three context anchors unknown | "Need at least one: who, when, or item ID" |
| 2 | 1 | Vague question without measurable qualifier | "What exact behavior should change?" |
| 3 | 2 | Unknown territory without spike task | "What's the spike timebox?" |
| 4 | 3 | Empty out-of-scope section | "Name one thing considered and cut" |
| 5 | 4 | Unmeasurable acceptance criteria | "What observable behavior can you verify?" |

## Writing Style

Follow `rules/writing-style.md`. Keep scoping documents direct and scannable. Use bullet lists and bold labels for structure. No em-dashes. No corporate fluff. Write for engineers and PMs who will skim the document in 2 minutes.

## Input Contract

Accepts: one of the following inputs.

- **Azure DevOps work item ID** (integer): Fetched via `mcp__azure-devops__wit_get_work_item`. Must contain at least a title.
- **Triage output file** (Obsidian path): A markdown file produced by `/triage-requests` with structured feature request data.
- **Raw text** (string): Pasted feature request, Teams message, email, or verbal description.

At least one input is required. If none is provided, ask: "What feature do you want to scope? Paste the request, give me a DevOps item ID, or describe it."

## Output Contract

Produces: a single markdown file saved to Obsidian.

**Path:** `[output-dir]/[project-name]/Scoping/[YYYY-MM-DD]-[feature-name]-scope.md`

**Required sections in the output document:**
- Political context (who, when, linked item)
- Decomposed atomic questions with domain classification
- Territory map table (Known / Adjacent / Unknown per question)
- Risk scenarios (Happy Path and Blow-Up Risk)
- Chosen scope option (A or B)
- Out of scope (at least one item)
- Testable acceptance criteria
- Downstream handoff block for `/edge-cases`

**Optional side effects (user must confirm each):**
- Create a new Azure DevOps work item
- Add a comment to an existing Azure DevOps work item

## Evaluation Criteria

The scoping document is ready when all of these are true:

- Every atomic question has a territory classification backed by evidence (reference file path for Known, partial precedent for Adjacent, explicit gap for Unknown)
- No acceptance criterion uses unmeasurable language ("fast", "better", "improved", "expected output")
- Out-of-scope section names at least one considered-and-cut item
- Unknown territory items have a timeboxed spike defined (if full scope was chosen)
- The downstream handoff block contains enough context for `/edge-cases` to run without follow-up questions
- Political context is explicit: requestor, deadline (or flagged assumption), and linked DevOps item (or "none")

## Success Criteria

A scoping session is successful when:

1. The output document passes all 5 hard gates without rework
2. The territory classification provides clear signal for sprint planning (no items left as "unclear" or "TBD")
3. The chosen scope option matches the deadline constraint (Option B for fixed customer dates, Option A only when timeline allows)

## Stop Conditions

Stop when:

- The scoping document is saved to Obsidian
- The user has been offered (and accepted or declined) DevOps integration
- The downstream handoff block is included in the document

Stop early if:
- The user decides the feature is not worth scoping (too vague, wrong timing, already covered)
- All items classify as Unknown territory and the user opts to run spikes first before scoping
- The user explicitly says "stop" or "that's enough"

## Safety Guardrails

- **Never auto-create DevOps work items.** Always present the proposed item and wait for user confirmation.
- **Never auto-post comments to DevOps.** Show the comment text first; let the user approve.
- **Never modify existing work items** beyond adding comments. No status changes, no reassignment, no field updates.
- **Bash usage is read-only.** This skill uses Bash only for reading files and checking paths. No destructive file operations.
- **Obsidian writes go to the scoping subdirectory only.** Never overwrite files outside `Projects/[project-name]/Scoping/`.

## Rollback and Recovery

If the skill is interrupted or produces incorrect output:

- The Obsidian file can be deleted or edited manually. No side effects beyond the file itself (unless DevOps integration was confirmed and executed).
- If a DevOps work item was created in error, tell the user the item ID so they can close or delete it. Do not attempt to delete work items programmatically.
- Re-running the skill on the same input is safe. It creates a new dated file; it does not overwrite previous scoping documents.

## Idempotency

Safe to re-run. Each execution creates a new file with the current date in the filename. Previous scoping documents for the same feature are preserved, not overwritten. DevOps actions only execute with explicit user confirmation each time.

## Progress Checkpoints

Report progress at these points:

1. **After Phase 0:** "Political context established: [requestor], [deadline], [DevOps item or none]."
2. **After Phase 1:** "Decomposed into [N] atomic questions. Review the breakdown above."
3. **After Phase 2:** "Territory map complete: [X] Known, [Y] Adjacent, [Z] Unknown."
4. **After Phase 3:** "Risk scenarios drafted. Choose Option A (full scope) or Option B (reduced scope)."
5. **After Phase 4:** "Scoping document saved to [file path]."

## DO / DON'T

**DO:**
- Ask for missing context before proceeding; never assume deadline or requestor
- Back territory classifications with evidence (file paths, precedent references)
- Present scope options as genuine choices, not leading questions
- Flag assumptions explicitly in the output document
- Keep the scoping document under 2 pages; link to details instead of inlining everything

**DON'T:**
- Invent acceptance criteria that aren't in the source material
- Estimate Unknown territory; define spikes instead
- Present Option A when a fixed customer deadline makes it risky
- Auto-execute any DevOps write operation without user confirmation
- Combine multiple features into a single scoping document; scope one feature per run

## Known Pitfalls

- **DevOps items often have empty acceptance criteria.** Use the title and description only. Do not invent criteria that aren't in the source.
- **"Unknown" does not mean "defer."** Unknown territory means "spike first." Do not recommend deferral just because a pattern is unfamiliar. Recommend a timeboxed investigation.
- **The deadline governs all tradeoffs.** If the deadline is a fixed customer date, never present an option that risks missing it. Reduce scope to Known territory instead.
- **Political context shapes framing.** A PM-initiated feature has different risk tolerance than a customer escalation. Adjust the risk scenario language accordingly.
- **Do not auto-create DevOps work items.** Always offer to create; let the user confirm. Work items created without review become noise.
- **Territory classification is not permanent.** Adjacent territory becomes Known after one successful implementation. Update `references/territory-patterns.md` after the sprint.

## MCP Tools Used

<!-- Azure DevOps tools are MCP-provided via the azure-devops MCP server, not standard registry tools -->
- **azure-devops** (`wit_get_work_item`, `wit_get_work_items_batch_by_ids`, `wit_create_work_item`, `wit_add_work_item_comment`) - Fetch and optionally create/update work items
- **Read/Write/Grep/Glob** - Read territory catalog, write output to Obsidian, search for existing scoping documents
