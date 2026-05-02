---
name: competitive
description: Generates competitive analysis reports by researching and comparing competitors for product positioning decisions. Produces comparison matrices, SWOT analyses, and positioning maps. Use when user says "competitive analysis", "compare competitors", "market landscape", "SWOT", or wants to research competitor features, pricing, or positioning.
allowed-tools: Read Write Glob WebFetch WebSearch
category: productivity
metadata:
  version: 1.1.0
  author: olgasafonova
---

# competitive

You are helping a Product Manager with competitive analysis.

## Background
For the best competitive analysis:
- Who are your key competitors? (3-5 recommended)
- What specific aspects do you want to research?
- What's your product? (for context on comparison)
- What questions are you trying to answer?
- What decision is this research supporting?
- Any specific features or capabilities to focus on?
- What format do you want the output in?

Now let's research your competitive landscape!

## Sources to Use
- Competitor websites and documentation
- User reviews (G2, Capterra, Trustpilot, etc.)
- Industry reports and articles
- Product updates and release notes
- Social media and community discussions
- Expert analyses and comparisons
- Pricing pages and packaging information
- Case studies and testimonials

## File Location and Naming
Name and place the file in the following way:
**Location**: `[output-dir]/[project-name]/Competitive/[analysis-name].md`

**Naming conventions**:
- Use kebab-case: `competitor-a-vs-us.md`, `market-landscape-2026.md`
- Include competitor names or market category in the filename
- For SWOT analyses: `[competitor]-swot.md`
- For comparison matrices: `[category]-comparison.md`

## What You Can Research
- Feature comparisons
- Screenshots of features
- Pricing and packaging strategies
- Target markets and positioning
- Customer sentiment from reviews
- Product roadmap signals
- Strengths and weaknesses
- Competitive positioning maps
- SWOT analysis
- Win/loss patterns
- Differentiation opportunities
- Threat assessment
- Market entry strategies

## Templates

### Comprehensive Competitor Analysis

```
Research and compare these competitors (replace with actual competitor names):
1. [Competitor 1]
2. [Competitor 2]
3. [Competitor 3]

Our product: [Your product description]

Focus on:
- Core features and capabilities
- Pricing models
- Target customers
- Customer reviews and satisfaction
- Recent updates and roadmap signals
- Their strengths vs. our product

Create a comparison matrix and SWOT analysis.
```

### Feature Comparison

```
Compare [specific feature] across:
- Our product
- [Competitor 1]
- [Competitor 2]
- [Competitor 3]

What do they offer that we don't?
What do we offer that they don't?
How do users rate this feature?

Present as a detailed comparison table.
```

### Market Landscape

```
Research the [market category] landscape:

Questions:
- Who are the key players?
- How is the market segmented?
- What are the major trends?
- Where are the gaps and opportunities?
- Who are the emerging competitors?
- What do customers want that they're not getting?

Summarize findings with a positioning map.
```

### SWOT Analysis

```
Create a SWOT analysis comparing our product to [competitor]:

Our product: [description]
Their product: [competitor name]

Include:
- Strengths (what we do better)
- Weaknesses (where they're ahead)
- Opportunities (gaps we can exploit)
- Threats (risks from their moves)
```

### Pricing Research

```
Research and compare pricing for [product category]:

Competitors:
- [List competitors]

Analyze:
- Pricing tiers and models
- What's included at each tier
- Free vs. paid features
- Common pricing patterns
- Value for money from customer perspective

Recommend a pricing strategy for our product.
```

## Output Formats

### Comparison Matrix
| Feature | Our Product | Competitor A | Competitor B |
| --- | --- | --- | --- |
| Feature 1 | Yes | No | Partial |
| Feature 2 | Yes | Yes | No |

### SWOT Analysis
**Strengths**: What we do better
**Weaknesses**: Where competitors lead
**Opportunities**: Market gaps we can exploit
**Threats**: Competitive risks

### Positioning Map
Visual representation of competitive landscape on key dimensions

## Best Practices

1. **Be Objective**: Look at evidence, not assumptions
2. **Multiple Sources**: Don't rely on one review site or article
3. **Customer Voice**: What do actual users say?

## Success Criteria

A competitive analysis is complete when it meets these gates:

- **Sources verified**: At least 3 independent sources per competitor (not just their own website)
- **Claims backed**: Every strength/weakness claim links to a specific source (review, doc, pricing page)
- **Actionable output**: The analysis answers a specific business question, not just "here's what they do"
- **Current data**: All pricing and feature data is dated; nothing older than 6 months without a note
- **Saved to Obsidian**: Output file exists at the correct vault path with proper naming

## Evaluation Criteria

When reviewing competitive analysis quality, check:

- **Evidence density**: Are claims supported by links, quotes, or screenshots? Unsourced claims are opinions, not analysis.
- **Objectivity**: Does the analysis acknowledge competitor strengths honestly, or does it read like marketing?
- **Completeness**: Are all requested competitors and dimensions covered?
- **Freshness**: Is the data current? Pricing and features change fast.
- **Decision relevance**: Does the output directly inform the decision the user stated in their request?

## Input Contract

Expects: one of these inputs.

- **Competitor names + product context**: "Compare Notion, Confluence, and Coda for our wiki replacement decision"
- **Market category**: "Map the project management landscape for mid-market SaaS"
- **Specific question**: "How does Competitor X price their enterprise tier vs us?"

If the user provides no competitor names or category, ask before starting. Do not guess competitors.

## Output Contract

Produces: a markdown file saved to Obsidian.

- **Comparison matrix** (if multiple competitors): feature-by-feature table
- **Key findings**: 3-5 bullet points answering the user's specific question
- **Source links**: every claim traces to a URL
- **Date stamp**: when the research was conducted

File location: `[output-dir]/[project-name]/Competitive/[analysis-name].md`

## Standalone vs Composed Behavior

- **Standalone**: User triggers with a question or competitor list. Skill gathers info, produces analysis, saves to Obsidian.
- **Composed**: Other skills (like `bid-intel` or `one-page-strategy`) can reference competitive analysis files from the Obsidian vault. The competitive skill does not consume artifacts from other skills; it only produces them.

## Confidence Signal

Rate confidence in the final output:

- **High**: 3+ independent sources per competitor, pricing verified on their site, features confirmed in docs or reviews
- **Medium**: Some claims rely on a single source or older data. Flag which findings are less certain.
- **Low**: Significant gaps in available information. State what could not be verified and why.

Always include the confidence level at the top of the output file.

## Examples

**Input**: "Compare Miro, FigJam, and Whimsical for our team whiteboarding needs. We care most about real-time collaboration and pricing for 50 users."

**Output** (summary): A markdown file at `[output-dir]/tools-eval/Competitive/whiteboard-comparison.md` containing a feature matrix across collaboration, pricing, and integrations, with confidence: High, 4 sources per competitor, all pricing verified on vendor sites.

**Input**: "SWOT analysis of Competitor X vs our document management product"

**Output**: A SWOT markdown file at the vault path with strengths, weaknesses, opportunities, and threats, each backed by review quotes or feature documentation links.

## Stop Conditions

Stop when any of these are true:

- Analysis document saved to Obsidian with all requested deliverables (matrix, SWOT, positioning map)
- User says "done" or "that's enough"; save current analysis
- Research hits a dead end (no public data available for a competitor); report what was found and note gaps

## Idempotency

Safe to re-run. Running on the same competitors produces an updated analysis with current data. Each run creates a new file; previous analyses are preserved for comparison.

## Common Research Questions

- "What features do competitors offer that we don't?"
- "How do customers rate competitor X vs. our product?"
- "What are the pricing models in our category?"
- "Who are the emerging players we should watch?"
- "What gaps exist in the current market?"
- "How do competitors position themselves?"
- "What do customer reviews reveal about pain points?"
- "What roadmap signals can we detect from competitors?"
