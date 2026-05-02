# LMWTFY Answer Framing

How to deliver findings that contradict what a colleague believes, without triggering defensiveness.

## Sidestep, don't block

Build on their assumption, then redirect with evidence. Use "and" instead of "but."

- **They think a feature exists, it doesn't:**
  "That's a reasonable expectation for a records management system. And in Public 360, the SIF API handles this differently: [your finding with link]."

- **They proposed an approach that won't work:**
  "That approach makes sense for [their context]. And looking at the source code, [specific class/method] actually requires [correct approach]. Here's what would work: [alternative]."

- **They cited outdated information:**
  "That was accurate in [version/timeframe]. And as of [current version], the behavior changed: [finding with link to commit or wiki]."

## Anchor in evidence, not authority

Frame corrections as findings, not opinions. Let the source code and wiki do the heavy lifting.

- "The source code shows..." (link to file + line)
- "According to the wiki page on [topic]..." (full URL)
- "The commit history suggests this changed in [version]..." (link)

Never: "I believe..." or "In my experience..." in a lmwtfy answer. The whole point of this skill is that every claim traces to a source. Let the sources deliver the bad news.

## When to apply this

Add framing guidance to the answer file when ALL of these are true:

- The colleague stated or implied a specific belief in their question
- Your research contradicts that belief
- The answer will be shared directly (not just filed away)

Keep the framing brief; one sentence of redirection before the evidence. The answer itself stays factual; the framing just softens the entry point.
