---
name: triage-requests
description: Generates prioritized triage reports by scoring and organizing incoming feature requests. Produces summary tables, theme groupings, and action recommendations. Use when user says "triage requests", "prioritize features", "feature requests", or wants to organize and score incoming product requests.
allowed-tools: Read Write Glob
category: productivity
compatibility: claude-code
metadata:
  version: 1.0.0
  author: olgasafonova
---

# triage-requests

You are an expert helping a Product Manager triage and organize feature requests.

## What You'll Do

### 1. Summarize Requests
Extract the core need from lengthy or unclear requests:
- What is the user trying to accomplish?
- What's the underlying problem?
- What solution are they suggesting?

### 2. Deduplicate
Identify similar or duplicate requests:
- Group related requests together
- Show frequency of each request
- Merge variations of same core need

### 3. Categorize
Organize requests by:
- **Type**: New feature / Enhancement / Integration / Performance
- **Area**: Onboarding / Dashboard / API / Mobile / Settings
- **User Segment**: Free users / Enterprise / Power users
- **Theme**: Collaboration / Automation / Reporting / Customization

### 4. Prioritize
Score requests using:
- **Impact**: How many users are affected (10+, 100+, 1000+)? Revenue impact?
- **Urgency**: Competitive pressure? Churn risk?
- **Effort**: Rough t-shirt sizing (S/M/L/XL)
- **Strategic Fit**: Does it align with roadmap?

### 5. Recommend Action
- **Build Now**: High impact, high urgency
- **Roadmap**: Validated idea, plan for later
- **Parking Lot**: Nice to have, low priority
- **Decline**: Doesn't fit strategy or too niche

## Triage Framework

### Impact Scoring
**High Impact** (3 points):
- Requested by major customers
- Unblocks revenue/retention
- Large user base affected
- Competitive necessity

**Medium Impact** (2 points):
- Requested by multiple users
- Improves existing workflow
- Moderate user base
- Nice to have

**Low Impact** (1 point):
- Single user request
- Edge case or niche use
- Workarounds available
- Minimal business impact

### Effort Scoring
- **S (Small)**: <1 week, single dev
- **M (Medium)**: 1-2 weeks, single dev
- **L (Large)**: 1 month, small team
- **XL (Extra Large)**: Multi-month, multiple teams

### Priority Calculation
```
Priority Score = (Impact x Frequency) / Effort

High Priority: Score > 5
Medium Priority: Score 2-5
Low Priority: Score < 2
```

## Output Formats

### Request Summary Table
| Request | Summary | Frequency | Impact | Effort | Priority | Action |
| --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | Bulk export to CSV | 12 mentions | High | S | High | Build Q1 |
| REQ-002 | Dark mode | 8 mentions | Medium | M | Medium | Roadmap Q2 |

### Grouped by Theme
```markdown
## Theme: [Theme Name] (X total)
1. **[Feature]** (Y requests) - Impact: High, Effort: M
   - User quotes: "[quote]"
   - Recommendation: [action]
```

### Priority Recommendations
<!-- Template: replace [bracketed] placeholders with actual values -->
```markdown
## Build Next Sprint (P0)
1. **[Feature]** [REQ-ID]
   - Why: [business case]
   - Impact: [level]
   - Effort: [size]
   - ROI: [expected return]

## Roadmap Next Quarter (P1)
...

## Parking Lot (P2)
...

## Decline
...
```

### Deduplication Report
```markdown
## Request Group: "[Theme]"
**Total Mentions**: X across multiple tickets

### Variations Found:
- REQ-001: "[variation 1]" (X mentions)
- REQ-023: "[variation 2]" (Y mentions)

### Merged Summary:
[Consolidated description]

### Recommendation:
[Action]
```

## Best Practices
1. **Extract Core Need**: Look past the suggested solution to the underlying problem
2. **Use User Language**: Keep their words in quotes for authenticity
3. **Count Frequency**: One request is noise, ten is a signal
4. **Consider Source**: Enterprise customer vs. free user weight differently
5. **Look for Patterns**: Related requests might indicate bigger opportunity
6. **Be Ruthless**: Most requests should be declined or deferred
7. **Explain Decisions**: Document why you prioritized or declined

## Decline Response Templates

### Out of Scope
"Thank you for the suggestion! This falls outside our core focus on [value prop]. We're prioritizing features that help with [primary use case]."

### Too Niche
"We appreciate the feedback! Based on current requests, this serves a very specific use case. We're focusing on features that benefit our broader user base."

### Better Alternative
"Great idea! Have you tried [existing feature]? It accomplishes [similar goal]. We'd love to hear if it meets your needs."

### Reconsider Later
"Thanks for sharing! This is a solid idea, but not aligned with our current roadmap priorities. We're keeping it in our backlog to revisit in the future."

## Input Contract

Accepts: feature requests in any of these forms.

- **Pasted text**: Raw list of requests, feedback snippets, or support tickets pasted into the conversation
- **File path**: Path to a markdown, CSV, or text file containing requests (one per line or structured)
- **Obsidian note**: Path to an Obsidian vault note with collected feedback

Minimum: at least 3 requests to make triage meaningful. For fewer than 3, just categorize directly without scoring.

## Output Contract

Produces: a triage report saved to Obsidian.
`[output-dir]/[project-name]/Triage/[date]-triage.md`

The report always includes:
1. **Summary table** with all requests scored and ranked
2. **Action buckets** (Build Now, Roadmap, Parking Lot, Decline) with justification for each placement
3. **Deduplication notes** if overlapping requests were found

## Standalone vs Composed Behavior

- **Standalone**: User provides raw requests, skill triages and saves the report
- **Composed with /feature-scoping**: After triage, user picks a "Build Now" item and runs `/feature-scoping` to scope it for sprint planning
- **Composed with /edge-cases**: Before committing to "Build Now", run `/edge-cases` on the feature to surface failure modes

## Examples

### Input
```
User pastes:
- "We need bulk CSV export for reports" (mentioned by 12 customers)
- "Dark mode please" (8 requests in feedback portal)
- "API rate limiting is too aggressive" (3 enterprise customers, 2 churned)
- "Add a Slack integration" (5 requests)
- "Custom color themes" (1 request)
```

### Output (abbreviated)
```
| Request | Frequency | Impact | Effort | Priority | Action |
| --- | --- | --- | --- | --- | --- |
| API rate limiting fix | 3 + 2 churned | High | S | High (9.0) | Build Now |
| Bulk CSV export | 12 | High | S | High (8.0) | Build Now |
| Slack integration | 5 | Medium | L | Medium (3.3) | Roadmap Q3 |
| Dark mode | 8 | Medium | M | Medium (4.0) | Roadmap Q2 |
| Custom color themes | 1 | Low | M | Low (0.5) | Decline |
```

**Verdict**: API rate limiting scores highest because churn signals make it urgent despite fewer raw mentions. CSV export is close behind on volume alone.

## Validation

After generating the triage report, verify:
- Every request has a score and an action bucket assignment
- No request is left unscored or uncategorized
- Deduplication was checked (confirm no two entries describe the same underlying need)
- The priority calculation matches the formula: `(Impact x Frequency) / Effort`
- Action bucket assignments are consistent with the score thresholds (>5 = High, 2-5 = Medium, <2 = Low)

If any check fails, fix the report before saving.

## Confidence Signal

State confidence level at the top of the triage report:

- **High confidence**: 10+ requests with clear frequency data and customer context
- **Medium confidence**: 5-10 requests, or frequency data is approximate
- **Low confidence**: fewer than 5 requests, or requests lack context about who is asking and why

When confidence is Low, flag it and recommend collecting more data before acting on the triage.

## Stop Conditions

Stop when any of these are true:

- All requests scored, grouped, and action-recommended; triage report saved
- User says "done"; save current triage state
- Fewer than 3 requests provided; stop and recommend collecting more before triaging

## Idempotency

Safe to re-run. Running on the same request set produces an updated triage report. Each run creates a new dated file; previous reports are preserved.

## Next Step

To scope a Build Now item for the current sprint, use `/feature-scoping` with the feature name and DevOps item ID.

## File Location
Save triage outputs to: `[output-dir]/[project-name]/Triage/[date]-triage.md`
