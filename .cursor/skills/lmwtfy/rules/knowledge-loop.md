# Self-Improving Knowledge Loop

Pattern for producing verified knowledge that feeds back into the team wiki. After saving research locally, check if it should be published to the team wiki. This prevents the same questions from being answered repeatedly.

## The Loop

```
Research complete → Save locally → Check wiki → Gap? → Propose entry → Approve → Publish
```

## When to Trigger

Run this check when ALL of these are true:

- The skill just produced a verified, high-confidence answer
- The topic is general enough to help more than one person
- The answer references wiki pages or source code (not just customer-specific context)

Do NOT trigger when:

- The answer is customer-specific or contains sensitive data
- Confidence is low or medium (unverified answers don't belong on the wiki)
- The question is about a one-off bug or transient issue
- The user explicitly asked for a private/personal note only

## Step 1: Check Wiki Coverage

After saving the local answer, search and read the wiki using the **shared evidence-retrieval layer** only — **§4 Wiki (`user-mediawiki`)** in [`shared/evidence/profiles/code-first-research.md`](../../shared/evidence/profiles/code-first-research.md), plus MCP hygiene and caps in [`shared/evidence/sources-and-tools.md`](../../shared/evidence/sources-and-tools.md) and [`shared/evidence/budgets.md`](../../shared/evidence/budgets.md). Read MCP tool schemas before calling (see `sources-and-tools.md`).

Classify the result:

- **Well covered** - wiki has a page that answers this question adequately. Stop here.
- **Partially covered** - wiki has a related page but misses this specific aspect. Propose an edit to the existing page.
- **Not covered** - no wiki page addresses this topic. Propose a new page.

## Step 2: Propose Entry

Draft the wiki content following these rules:

- Write in English (wiki requirement)
- Use wikitext formatting, not markdown (`mediawiki_convert_markdown` can help)
- Use internal wiki links: `[[Page Title]]`, never full URLs for wiki pages
- Keep it concise; link to source code and other wiki pages for depth
- Add to an appropriate category: `[[Category:SIF]]`, `[[Category:Integration]]`, etc.
- Include a "See also" section with related wiki pages

Structure for a new page:

```
== Summary ==
[1-3 sentences answering the core question]

== Details ==
[Key findings, structured with subsections if needed]

== References ==
* [GitHub links, external docs]

== See also ==
* [[Related Wiki Page]]

[[Category:Appropriate Category]]
```

Structure for an edit to an existing page:

- Add a new section or update an existing section
- Don't restructure the whole page; make a focused addition
- Note what was added in the edit summary

## Step 3: Ask for Approval

Present the proposal to the user:

1. State whether this is a **new page** or an **edit to an existing page**
2. If editing, show the page title and link
3. Show the full proposed content
4. Ask: "Publish this to the wiki? (yes / edit first / skip)"

## Step 4: Publish

If approved:

- New page: `mediawiki_edit_page` with the full content
- Existing page edit: `mediawiki_edit_page` appending/updating the section
- Always use `preview=true` first, then confirm, then publish
- Include a clear edit summary: "Added [topic] based on colleague research"

After publishing, tell the user the page URL.
