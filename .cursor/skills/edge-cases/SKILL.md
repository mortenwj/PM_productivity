---
name: edge-cases
description: Generates edge case and error state analysis for features before development. Produces a checklist covering input validation, data states, system states, permissions, and user flows. Use when user says "edge cases", "error states", "what could go wrong", or wants to review a feature for failure modes before building it.
allowed-tools: Read Write Glob
category: development
compatibility: claude-code
metadata:
  version: 1.0.0
  author: olgasafonova
---

# edge-cases

You are an expert helping identify edge cases and error states.

## File Location and Naming

**Location**: `[output-dir]/[project-name]/Edge-Cases/[feature-name]-edge-cases.md`

**Naming conventions**:
- Use kebab-case: `checkout-flow-edge-cases.md`, `user-authentication-edge-cases.md`
- Include "-edge-cases" suffix for clarity

## Your Task

Proactively identify edge cases, error states, and system state combinations during the design phase-before development begins.

## What You'll Identify

### Input Validation Edge Cases
- Empty inputs (required fields left blank)
- Special characters and unicode
- Extremely long inputs (beyond limits)
- Invalid formats (email, phone, date)
- Negative numbers where positive expected
- Zero values
- Maximum/minimum boundaries
- Whitespace-only inputs
- SQL injection attempts
- XSS payloads

### Data State Edge Cases
- **Empty States**: No data exists yet
  - First-time user (no history)
  - Filtered results return nothing
  - Search with no matches
  - All items deleted

- **Extreme Data States**:
  - Single item vs. thousands of items
  - Very long text vs. very short
  - Large files (at limit)
  - Deep hierarchical nesting

### System State Edge Cases
- Loading states (initial, pagination, refresh)
- Offline/connectivity issues
- Slow network (3G, spotty WiFi)
- Timeout scenarios
- Partial failures (3 of 5 API calls succeed, 2 fail)
- Session expiration mid-task
- Concurrent edits by multiple users
- Cache invalidation

### Permission & Access Edge Cases
- Read-only access (can't edit)
- Missing permissions mid-flow
- Shared resource access conflicts
- Role changes during session
- Resource ownership changes
- Trial/free account limitations

### User Flow Edge Cases
- User goes back mid-flow
- User refreshes page
- User opens multiple tabs
- User abandons and returns later
- Deep links to middle of flow
- Flow interruption (phone call, notification)

### Integration Edge Cases
- External API is down
- API returns unexpected data
- Authentication failure
- Rate limiting hit
- Version mismatches
- Slow external service

## Edge Case Review Checklist

**Input Validation:**
- [ ] Empty required fields
- [ ] Invalid formats
- [ ] Out-of-bounds values
- [ ] Special characters
- [ ] Security (injection, XSS)

**Data States:**
- [ ] Empty state (no data)
- [ ] Single item
- [ ] Thousands of items
- [ ] Long text/names
- [ ] Deleted items

**System States:**
- [ ] Loading states
- [ ] Error states
- [ ] Offline/connectivity
- [ ] Slow network
- [ ] Timeouts
- [ ] Partial failures

**User Flow:**
- [ ] Back button
- [ ] Refresh page
- [ ] Multiple tabs
- [ ] Abandon and return
- [ ] Deep links
- [ ] Interruptions

**Permissions:**
- [ ] Read-only access
- [ ] Missing permissions
- [ ] Role changes
- [ ] Account limitations

**Accessibility:**
- [ ] Screen reader support
- [ ] Keyboard navigation
- [ ] Color contrast
- [ ] Focus states
- [ ] Error announcements

**Performance:**
- [ ] Large datasets
- [ ] Slow queries
- [ ] Heavy computations
- [ ] Memory constraints

## Output Format

For each edge case:

```markdown
### Edge Case: [Name]

**Scenario**: [What triggers this]
**Frequency**: [How often will this happen?]
**Impact**: [How bad is it if unhandled?]

**Current Behavior**: [What happens now? Or "Undefined"]
**Desired Behavior**: [How should we handle it?]

**User Experience**:
- Message: [What user sees]
- Actions: [What user can do]
- Recovery: [How to get back on track]

**Engineering Notes**:
- [Technical requirements]
- [Error codes/logging]
```

## Input Contract

Accepts: one of the following.
- A feature name or description (free text): "checkout flow", "user authentication"
- A link to a design doc, spec, or user story
- A pasted requirements block

At minimum, the user must provide:
- **Feature name**: what is being reviewed
- **Happy path**: the intended user flow when everything works

Optional but improves coverage:
- Data model or entities involved
- External system dependencies
- Permission model
- Known risks or concerns

## Output Contract

Produces: a single markdown file saved to the Obsidian vault.

```
[output-dir]/[project-name]/Edge-Cases/[feature-name]-edge-cases.md
```

The file contains:
1. A summary of the feature and happy path
2. A categorized list of edge cases, each using the Output Format template below
3. A completed review checklist with checked/unchecked items based on findings
4. A confidence assessment

## Standalone vs Composed Behavior

**Standalone:** Run directly with `/edge-cases` or trigger words. Produces the full edge case document and saves it.

**Composed:** When called from `/grill-me` or `/feature-scoping`, return the edge case list inline without saving to a file. The calling skill handles file output. Skip the vault save step and return structured findings directly.

## Success Criteria

An edge case review is complete when:
- Every category in the review checklist has been evaluated (checked or marked N/A with reason)
- Each identified edge case has a defined desired behavior, not just a description of the problem
- At least one edge case per active category (input, data state, system state, user flow, permissions) is documented
- No edge case is left with "Undefined" as both current and desired behavior

## Evaluation Criteria

When reviewing a feature for edge cases, evaluate against these dimensions:

- **Coverage**: Did the review address all relevant categories from the checklist? Categories can be marked N/A, but they must be explicitly considered.
- **Specificity**: Are edge cases described with concrete scenarios ("user submits form with 50,000 character name field") rather than vague labels ("long input")?
- **Actionability**: Does each edge case include a desired behavior that engineering can implement without further clarification?
- **Priority accuracy**: Are frequency and impact ratings realistic, not inflated to make every edge case seem critical?
- **Completeness**: Are integration points, permission boundaries, and state transitions covered, not just input validation?

## Confidence Signal

After completing the review, state confidence level:

- **High**: Feature is well-understood, all categories reviewed, external dependencies are documented
- **Medium**: Feature scope is clear but external system behavior is assumed, not verified
- **Low**: Feature description is vague, key integration points are unknown, or the review was based on incomplete information

Include the confidence level at the top of the output file, right after the feature summary.

## Structured Output Format

Each edge case entry follows this structure:

```markdown
### Edge Case: [Descriptive Name]

- **Category**: Input Validation | Data State | System State | User Flow | Permissions | Integration | Accessibility | Performance
- **Scenario**: [Specific trigger condition]
- **Frequency**: Rare | Occasional | Common
- **Impact**: Low | Medium | High | Critical
- **Current Behavior**: [What happens now, or "New feature"]
- **Desired Behavior**: [How the system should handle it]
- **User Message**: [What the user sees]
- **Recovery Path**: [How the user gets back on track]
- **Engineering Notes**: [Technical requirements, error codes, logging]
```

## Examples

### Example Input

```
Feature: Bulk document upload
Happy path: User selects 1-20 PDF files, clicks upload, files are processed and appear in the document list.
Data: PDF files, max 10MB each.
Integrations: S3 storage, virus scanner API.
Permissions: Upload requires "Document Creator" role.
```

### Example Output (single edge case)

```markdown
### Edge Case: Virus scanner timeout on large file

- **Category**: Integration
- **Scenario**: User uploads a 9.8MB PDF. The virus scanner API takes longer than the 30-second timeout to respond.
- **Frequency**: Occasional
- **Impact**: High
- **Current Behavior**: New feature
- **Desired Behavior**: Queue the file for retry. Show the user "Processing - scan in progress" status. Retry scan up to 3 times with exponential backoff. If all retries fail, flag the file for manual review and notify the user.
- **User Message**: "Your file is being scanned. This may take a few minutes for large files."
- **Recovery Path**: User can continue uploading other files. The queued file appears in their upload list with a "Scanning" badge.
- **Engineering Notes**: Implement async scan queue. Log scan timeouts with file size and scanner response time. Alert ops if timeout rate exceeds 5% in a 1-hour window.
```

## Stop Conditions

Stop when any of these are true:

- All checklist categories reviewed and edge case document saved
- User says "done" or "that's enough"; save current analysis
- Feature scope is too broad for a single pass; stop and recommend splitting

## Idempotency

Safe to re-run. Running on the same feature produces an updated edge case document. Previous versions are not overwritten (new file created with current date).

## What to Tell Me

- What feature/flow are you reviewing?
- What's the happy path user flow?
- What data does it work with?
- What external systems does it integrate with?
- What user permissions are involved?
- Any known concerns or risks?
