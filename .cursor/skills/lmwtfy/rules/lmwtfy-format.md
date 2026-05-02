# LMWTFY Output Format

Rules for formatting lmwtfy answer files.

## Formatting Rules

**No tables.** They break on copy-paste and render inconsistently across viewers.

**No em-dashes.** Use periods, commas, or semicolons instead.

**Use bullet lists, numbered lists, and bold text** for structure.

**Full links, never wrapped.** Always include complete URLs as plain text, never as markdown links `[text](url)`. Wrapped links render badly when copy-pasting markdown to MS Teams or email.

**Direct GitHub links for source code.** When referencing source files, use full GitHub URLs (for example `https://github.com/te-industry-public360/core-bl/blob/master/Source/path/to/File.cs`), not local file paths.

**Simple language.** Write for colleagues who may not be deep in the specific area. Avoid jargon when a plain word works. Be direct.

**Clarity over completeness.** A clear answer to the core question beats an exhaustive document nobody reads. Put the answer up front, supporting evidence below.

**Documentation assessment (required in every answer file).** After **Findings**, include a **Documentation assessment** section. Use the same three statuses and calibration as **`../../shared/evidence/evidence-playbook.md`** §8: base status on **verified** wiki/help (and other official prose you verified per playbook **§4**), not on code alone and not on search snippets (**leads**). Status is **orthogonal** to answer **confidence** (playbook §5): for example, behaviour can be **High** confidence from code while official help is still **missing_documentation**. When status is **partially_documented** or **missing_documentation**, add **Suggested documentation changes** as bullets (which page or help topic to add or extend, and what to cover).

**No effort estimates.** Estimation is the delivery org's job, not the product team's. If relevant, link to wiki pages about the estimation/delivery process so the colleague can follow the right methodology.

**Always include links in the answer.** Every finding should trace back to a source:

- Wiki pages (full URL): `https://wiki.software-innovation.com/wiki/Page_Name`
- Source code (direct GitHub links to file + line): `https://github.com/te-industry-public360/core-bl/blob/master/Source/path/File.cs#L42`
- Official third-party docs when the answer involves external standards or systems (Noark5, eFormidling, DigDir, OAuth specs, etc.). Link to the authoritative source, not blog posts or summaries.

## File Location

Save every answer under **`./docs/lmwtfy-answers/`** in the PM productivity project unless the user specifies another folder for that run.

```
./docs/lmwtfy-answers/[Descriptive Title].md
```

Use a descriptive title that captures the question, not the person asking. Examples:

- `SLU EventHandler Migration Guidance.md`
- `SIF RabbitMQ Event Queue Limitations.md`
- `Custom Fields via SIF API.md`
- `360 Online OnPrem vs Cloud Differences.md`

## File Template

```markdown
# [Title]

[1-3 sentence summary answering the core question]

---

## Original Question

> [Paste the full original question text here, including any links the colleague provided]

## Context

[Who asked, what they're trying to do, why it matters]

## Findings

[Main content with evidence and links]

## Documentation assessment

- **Status:** well_documented | partially_documented | missing_documentation
- **Explanation:** [1–3 sentences; tie to verified wiki/help URLs from References where applicable]
- **Suggested documentation changes:** [Bullets only when status is partially_documented or missing_documentation: concrete wiki page, help topic, or section to add or update]

## Risks and Limitations

[If applicable]

## References

- https://wiki.software-innovation.com/index.php?title=...
- https://github.com/te-industry-public360/...
- https://tieto-si.visualstudio.com/360/_workitems/edit/...
```
