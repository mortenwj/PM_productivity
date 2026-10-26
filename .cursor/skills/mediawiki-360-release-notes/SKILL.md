---
name: mediawiki-360-release-notes
description: >-
  Updates Public 360° release pages on MediaWiki (e.g. "6.12 release information")
  from Azure DevOps scope, with consistent structure, prose style, and safe edit
  workflow. Covers Process Platform / Flow, IFAR, module sections, and technical
  notes. Use when authoring or refreshing 360° Online release wiki pages, release
  information, GA module text, or comparing ADO 6.12-tagged work to the wiki.
---

# MediaWiki — 360° Online release pages

Complements **`paf-pilot-release-notes`** (weekly pilot Markdown). This skill is for the **internal/customer release wiki** on [Release Information](https://wiki.software-innovation.com/wiki/Release_information) and version pages such as **`6.12 release information`**.

## When to use

- User asks to update **release notes**, **release information**, or a **6.xx** wiki page.
- Process Platform (or another team) needs **GA**, **News and improvements**, **pilots**, or **technical notes** aligned with ADO.
- After a release cut: gap analysis (ADO vs published wiki) before editing.

## Hard rules (style)

1. **English only** on the Public 360° wiki (see MediaWiki MCP editing guidelines).
2. **No Azure DevOps IDs in customer-facing bullets** for fixes, highlights, or improvements — match other modules (e.g. eSigning). IDs may appear in **internal owner lines** only if the user explicitly wants them; default is **no owner/ID lines**.
3. **No NVE / pilot-only customer claims** unless the user approves wording and placement (usually *Coming soon* or pilot sections).
4. **Do not publish** until the user approves proposed text (unless they say “apply”, “publish”, or “implement”).
5. **Internal links:** `[[Page Title]]`, not full wiki URLs.
6. **Minimize scope:** one module/team per edit when possible; do not rewrite unrelated sections.

## Page anatomy (typical major release)

| Section | Use for |
|---------|---------|
| `=New module=` | First GA of a **product module** (e.g. 360° Flow) |
| `=News and improvements in existing module(s)=` | GA modules already sold; corrections and incremental features (e.g. IFAR) |
| `=New features and improvements in the core product=` | Core BL / cross-cutting product |
| `=Coming soon (Ongoing Pilots)=` | Not GA; pilot disclaimer |
| `=Technical notes=` | Implementers, on-prem, registry/migration (not marketing copy) |

**360° Flow:** Prefer a single **`== 360° Flow - Now Generally Available ==`** under *New module* with **Highlights in 6.12**, **Bug fixes**, **Important notes**, **Learn More** — not a second duplicate Flow block.

## Workflow

Copy and track:

```
Release wiki update:
- [ ] 1. Locate page (search + get_page_info + get_sections)
- [ ] 2. Scope ADO (WIQL + get_batch)
- [ ] 3. Map items → wiki section (GA / News / core / pilot / technical)
- [ ] 4. Draft wikitext (no ADO ids in bullets; user decisions noted)
- [ ] 5. User approval
- [ ] 6. Publish (safe edit method)
- [ ] 7. Verify (checklist + optional script)
```

### 1. Locate the wiki page

- Hub: **`Release Information`**
- Version page: **`{version} release information`** (e.g. `6.12 release information`)
- Tools: `user-mediawiki` — `mediawiki_search`, `mediawiki_get_page`, `mediawiki_get_sections`, `mediawiki_search_in_page`

### 2. Scope Azure DevOps

- Project **`360`**, tools: `user-azure-devops` — `wit_query` (action **`wiql`**), `wit_work_item` ( **`get_batch`** ).
- **Process Platform (typical):**
  - Area: `360\Core-Process-platform`, tags **`6.12`** or **`6.12 RV`**, `State <> Removed`
  - Also: tag **`Process Platform`** + **`6.12`** / **`6.12 RV`** (often RV fixes, IFAR, email dialog)
  - IFAR/eInnsyn: title contains IFAR / innsyn / access request + release tag (confirm **area/owner** before attributing to PP)
- Classify each item: **Closed/Resolved** (candidate for published notes) vs **Active/New/Rejected** (Important notes, pilot, or omit).
- Record **user decisions**: GA vs pilot, all customers vs market, fold into Flow GA vs separate News section.

WIQL examples: [reference.md](reference.md).

### 3. Gap analysis

- For each scoped item: **theme** → target wiki section; **already covered?** (search_in_page by keyword, not only by ID).
- Deliverable before edit: short table **Covered / Gap / Proposed action** for the user.

### 4. Draft wikitext

- Use templates in [reference.md](reference.md).
- **Highlights:** bold lead-in (`'''Background processes''' — …`), sub-bullets only when needed.
- **Bug fixes:** customer-safe titles; drop internal test names (e.g. “Pandora”) in published text.
- **Feature toggles:** include official toggle names when GA (e.g. `FT:EnableBackgroundProcesses`) if delivery confirms.

### 5. Approval

- Present proposed blocks in chat or preview.
- For MCP: `mediawiki_find_replace` with **`preview=true`** first when using find/replace.

### 6. Publish (safe editing)

| Change size | Method |
|-------------|--------|
| Small, unique string | `mediawiki_find_replace` (`preview=false` after approval) |
| Whole section replace | Full-page edit via API **or** replace bounded block with regex (fetch wikitext with `action=parse`, edit locally, `action=edit`) |
| Rebuild after corruption | Restore from last good revision + re-apply approved blocks |

**Avoid:** `mediawiki_edit_page` with **`section=`** when content includes `==` headings — it can **duplicate or delete** sibling sections. Prefer **full-page** replace or **`find_replace`** with unique anchors.

**Edit summary:** One clear sentence (what section, why).

### 7. Verify

After publish:

- [ ] Exactly **one** `== 360° Flow - Now Generally Available ==` (if Flow is GA this release)
- [ ] `=News and improvements in existing module(s)=` present and populated if expected
- [ ] No unintended duplicate `==` headings (search_in_page)
- [ ] New prose has **no** `(#…)` / `[#…]` in Flow/News fix bullets (unless user waived)
- [ ] User-requested exclusions (e.g. no NVE) absent from new text

Optional local check (paste wikitext or extract via API):

```powershell
Get-Content path\to\page.wikitext -Raw | uv run python .cursor/skills/mediawiki-360-release-notes/scripts/verify_release_wikitext.py
```

## Related skills and repo

| Resource | Role |
|----------|------|
| `paf-pilot-release-notes` | Weekly pilot ADO → Markdown (not MediaWiki) |
| `pm-ado-work-item-authoring` | Backlog item quality |
| `projects/process-platform/pilot/PAF_pilot_weekly_report_SPEC.md` | Pilot scope/time rules |

## Additional material

- Section templates and WIQL: [reference.md](reference.md)
