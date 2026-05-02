---
name: grill-me
description: >-
  Generates complete feature specs by interrogating product vision and
  requirements through structured questioning. Produces a spec document
  covering constraints, acceptance criteria, edge cases, and variant
  directions before any code gets written. Use when user says "grill me",
  "spec interview", "interrogate me on this feature", "write a spec", or
  "spec this". Do NOT use for general triage (use /triage-requests) or
  technical scoping (use /feature-scoping).
allowed-tools: Read Write Edit AskUserQuestion Glob Grep
context: fork
category:
  - productivity
  - development
metadata:
  author: olgasafonova
  version: 1.0.0
---

# Grill Me: Spec Interview

Turn a rough vision into a complete feature specification through structured interrogation. The conversation is the value. The document is the artifact.

## Pipeline Position

```
feature-scoping (optional upstream) --> grill-me --> edge-cases (downstream)
```

Accepts input from:
1. A vision statement (what they want to build)
2. An optional file reference (existing scoping brief, requirements doc, DevOps item dump)
3. Optional variant directions (different interaction models or approaches)

## Input Parsing

The user provides everything after `/grill-me` on the command line.

If a file reference is included (e.g., `@docs/scoping.md` or a path), read it first and use it as context. Do not ask the user to repeat information already in the file.

If no vision statement is provided, ask: "What are you trying to build? One sentence."

## Interview Process

Work through these phases one at a time. Ask 2-3 questions per phase, wait for answers, then move to the next phase. Never dump all questions at once.

### Phase 1: Vision Clarification

- Who specifically uses this? What's their workflow today without it?
- What's the single most important thing this must do?
- How would you demo this to a stakeholder in 60 seconds?

### Phase 2: Constraints

- What must this NOT do? Where are the scope boundaries?
- Are there performance, data volume, or scale requirements?
- What existing patterns, systems, or conventions must it be consistent with?

### Phase 3: Acceptance Criteria

Based on their answers, propose 4-6 acceptance criteria. Then ask:

- Do these capture what "done" means for you?
- What's missing from this list?
- Which one is the most critical; the one you'd ship with if you could only pick one?

Use AskUserQuestion for the priority ranking.

### GATE: Testable Criteria

Every acceptance criterion must be testable. If any contains "works correctly", "is fast", "is better", "is improved", or similar unmeasurable language, push back: "How would you verify that? What specific, observable behavior?" Replace vague terms with measurable outcomes: response times in milliseconds, error rates as percentages, specific user-visible states, or exact data transformations.

### Phase 4: Edge Cases and Error States

Surface scenarios the user hasn't considered:

- What happens with no data? (empty states)
- What happens with extreme data? (100 items, 0 items, very long text, missing fields)
- What happens when something fails? (API errors, timeouts, stale data, partial writes)
- Are there permission, access, or multi-user considerations?
- What happens with bad input? (duplicates, out-of-range values, concurrent edits)

Be direct and challenging. These questions should surface real gaps, not softball.

### Phase 5: Variant Directions (if provided)

For each variant direction the user specified:

- Describe the interaction model in one sentence
- Ask: "What's the strongest argument FOR this approach for your users?"
- Ask: "What's the biggest risk or downside?"
- Ask: "What's your gut verdict; build, skip, or explore further?"

Use AskUserQuestion for the verdict on each variant.

If no variants were provided, ask: "Is there more than one way to approach this? Sometimes building 2-3 variants and comparing beats debating which to build."

### Phase 6: Test Plan

Propose a test plan covering:

- Visual verification (key states a human should eyeball)
- Functional verification (core user flows to validate)
- Edge case verification (empty states, error states, boundary conditions from Phase 4)

Ask if anything is missing.

### Phase 7: Generate Spec

Compile everything into the final spec:

```markdown
# Feature Spec: {Feature Name}

## Vision
{Refined vision statement incorporating interview answers}

## Constraints
{Scope boundaries, technical constraints, what this must NOT do}

## Acceptance Criteria
{Numbered list, ordered by priority. Most critical first.}

## Edge Cases and Error States
{Each scenario with expected behavior}

## Variant Directions
{For each: description, strongest argument, biggest risk, verdict}

## Test Plan
### Visual verification
- [ ] ...
### Functional verification
- [ ] ...
### Edge case verification
- [ ] ...

## Technical Reference
{Link to scoping brief if one exists, or note that /feature-scoping should run next}
```

## Save Location

Ask the user where to save. Suggest a default based on context:

- If in a project repo with a `docs/` folder: `docs/{feature-name}-spec.md`
- If working from an Obsidian vault: save under the vault's `Projects/` directory
- If unclear, ask.

## Rules

- Ask questions one phase at a time. Waiting between phases is the whole point.
- Use AskUserQuestion for structured choices (priority ranking, variant verdicts).
- Listen. The spec reflects THEIR vision, refined by your questions. Do not impose preferences or invent requirements they didn't express.
- If the user's answers reveal the feature is actually two features, say so. "This sounds like two separate things. Want to scope them separately?"
- If a file reference contradicts the user's verbal answers, flag the contradiction. Don't silently pick one.
- The spec is a living document. End with: "This spec will evolve. Run /grill-me again on the saved file to pressure-test after you learn more."

## Input Contract

Accepts: one of the following inputs.

- **Vision statement** (required): A sentence or paragraph describing what to build. Provided as text after `/grill-me`.
- **File reference** (optional): A path or `@file` reference to an existing scoping brief, requirements document, or DevOps item dump. Read and used as context; the user is not asked to repeat information from the file.
- **Variant directions** (optional): Named alternative approaches to explore in Phase 5.

If no vision statement is provided, prompt: "What are you trying to build? One sentence."

## Output Contract

Produces: a single markdown file containing the completed feature spec.

**Structure:**

```
# Feature Spec: {Feature Name}
## Vision
## Constraints
## Acceptance Criteria
## Edge Cases and Error States
## Variant Directions
## Test Plan
## Technical Reference
```

**Success criteria (pass/fail):**

- PASS: Every acceptance criterion contains a measurable outcome (numeric threshold, specific state, or observable behavior). No vague language survives the gate.
- PASS: At least 4 acceptance criteria are listed, ordered by priority.
- PASS: Edge cases section covers empty states, extreme data, and failure modes.
- PASS: Test plan has at least one item in each of visual, functional, and edge case verification.
- FAIL: Any acceptance criterion uses unmeasurable language ("works correctly", "is fast", "is better").
- FAIL: Spec is generated without completing all interview phases.
- FAIL: User-provided file context is ignored or user is asked to repeat information from the file.

## Confidence Signal

After generating the spec, report a confidence assessment:

- **High**: All phases completed with substantive user answers. Acceptance criteria are measurable. Edge cases are covered.
- **Medium**: Some phases had thin answers or the user skipped variant exploration. Spec is usable but may need a follow-up round.
- **Low**: User gave minimal input, skipped multiple phases, or acceptance criteria remain vague despite pushback.

State the confidence level and one sentence explaining why at the end of the spec file.

## Structured Output

The final spec file follows this exact structure. Every section heading is required; empty sections get "None identified" rather than being omitted.

```yaml
# metadata block at top of spec file
---
artifact: feature-spec
source-skill: grill-me
created: YYYY-MM-DD
confidence: high | medium | low
phases-completed: [1, 2, 3, 4, 5, 6, 7]
acceptance-criteria-count: N
---
```

## Examples

### Example Input

```
/grill-me I want to build a bulk document import feature for SIF that reads CSV files and creates documents with metadata
```

### Example Output (abbreviated)

```markdown
---
artifact: feature-spec
source-skill: grill-me
created: 2026-04-08
confidence: high
phases-completed: [1, 2, 3, 4, 5, 6, 7]
acceptance-criteria-count: 5
---

# Feature Spec: SIF Bulk Document Import

## Vision
Import documents in bulk from CSV files through the SIF API, mapping CSV columns to document metadata fields. Target users are integration developers who currently create documents one at a time via API calls.

## Acceptance Criteria
1. A CSV file with 100 rows produces 100 documents with all mapped metadata fields populated within 60 seconds.
2. Rows with missing required fields are skipped and logged with row number and field name; processing continues for remaining rows.
3. ...

## Edge Cases and Error States
- Empty CSV (headers only, no data rows): returns success with zero documents created and a warning message.
- CSV with 10,000+ rows: processes in batches of 100; reports progress after each batch.
- ...
```

## Stop Conditions

Stop when any of these are true:

- All 7 phases completed and spec document saved to file
- User says "done", "stop", or "that's enough" at any point; save current state
- User's answers reveal two separate features; stop and ask whether to split before continuing
- No progress after two rounds on the same phase; save draft and suggest revisiting later

## Idempotency

Safe to re-run. Running on an existing spec file re-interrogates and updates it. Running on a new vision produces a new spec. Previous specs are not overwritten.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| User gives one-word answers | Rephrase as specific scenarios: "What if a user has 50 items?" |
| Interview stalls at Phase 3 | Propose acceptance criteria yourself; ask them to edit |
| File reference contradicts verbal answers | Flag it explicitly; ask which is current |
| User wants to skip to building | "The spec takes 10 minutes. A bad build takes hours to undo." |
