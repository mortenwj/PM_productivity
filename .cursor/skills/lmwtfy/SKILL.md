---
name: lmwtfy
description: >-
  Research and answer technical questions from colleagues about Public 360°,
  SIF, and related systems. Searches GitHub source code, 360 Online help
  center, Azure DevOps, and wiki. Saves verified answers to a local folder
  and proposes wiki entries for knowledge gaps. Use when user says "lmwtfy",
  "wiki that", "colleague question", "answer question", or needs to research
  a product/technical question for someone.
allowed-tools: Read Write Edit Bash Grep Glob WebFetch WebSearch
context: fork
category:
  - productivity
  - research
metadata:
  author: olgasafonova
  version: 2.2.1
---

# LetMeWikiThatForYou: Colleague Question Research

Research and answer technical questions from colleagues about Public 360°, SIF API, integrations, and related systems. Produces verified, high-confidence answers backed by source code, help center documentation, and wiki. Saves answers under the **output directory** below for reuse.

## Cursor (PM productivity project)

**Default output directory:** `./docs/lmwtfy-answers/` (create the folder when you write the first file if it does not exist).

### Shared evidence-retrieval layer (default retrieval)

**Default:** Treat **`shared/evidence/`** plus **`profile:code-first-research`** as the **baseline** retrieval path: load the shared index and playbooks first, then run the profile’s four-source order and mechanics. **Do not** invent a second, undocumented verification standard; **what counts as verified, a lead, inferred, confidence, and conflicts** stays **`shared/evidence/evidence-playbook.md`** (with **`verification-and-leads.md`** for ledger hygiene). **Do not** paste a parallel copy of those rules into chat; link and apply them.

**Load once per run (before touching GitHub, help, ADO, or wiki):**

1. [`shared/evidence/README.md`](../shared/evidence/README.md) — index; confirms **`lmwtfy`** uses **`profile:code-first-research`**.  
2. [`shared/evidence/evidence-playbook.md`](../shared/evidence/evidence-playbook.md) — **claim**, **evidence**, verified / lead / inferred, **confidence**, stop rules, conflicts, **§8 documentation coverage** (read before Steps 1–4, before the evidence ledger, and before writing **Documentation assessment** in the answer).  
3. [`shared/evidence/budgets.md`](../shared/evidence/budgets.md) — default caps (wiki pages, help topics read, ADO `top`, code searches / files).  
4. [`shared/evidence/sources-and-tools.md`](../shared/evidence/sources-and-tools.md) — MCP descriptors, server ids, `gh` / Grep / WebFetch, key repos.  
5. [`shared/evidence/verification-and-leads.md`](../shared/evidence/verification-and-leads.md) — leads vs verified reads; ledger fields.  
6. [`shared/evidence/ratatoskr-preflight.md`](../shared/evidence/ratatoskr-preflight.md) — before relying on Ratatoskr body text.

**Default execution path (code-first, four sources):**

- **[`shared/evidence/profiles/code-first-research.md`](../shared/evidence/profiles/code-first-research.md)** — **§** load order (1 GitHub → 2 Ratatoskr → 3 ADO if relevant → 4 wiki), conflict rule (**code wins**), extract list, and the concrete steps/commands for each source. **This file remains the normative definition of the default *what* and *how*;** extensions (below) are **additive** and must be **declared**, not a silent alternate workflow.

**Ratatoskr tool names and call order** (parameters): **`rules/ratatoskr-mcp-tools.md`**.

If an MCP server is not configured, skip that source per the profile, record it in the evidence ledger, and continue where the profile allows. Do not invent tool names.

**Controlled extensions beyond the default profile**

You **may** go beyond the default four-source pass **when** at least one applies: the colleague’s question is **ambiguous** after Step 0, **verified** material from the default pass is **insufficient** to answer safely, or **deeper investigation** is clearly needed (for example follow-on repo, extra wiki scope, external standard, bounded WebSearch). **Still:** complete a sensible **default** pass first unless the question obviously does not need it (then state why in the ledger).

**Rule for any deviation**

1. **Declare it in the evidence ledger** before or when you present the ledger (dedicated rows or a short **Profile extension** block): **what** you did beyond the profile, **why** (tie to ambiguity / insufficiency / depth), and **Verified how** for each new source (same bar as **`evidence-playbook.md`** §4; no snippet-only “verification”).  
2. **Same verification rules** as the playbook for every claim you keep: extended retrieval does **not** relax leads vs verified or confidence calibration.  
3. **Stay bounded:** prefer extra reads within the same corpora and `budgets.md` before opening wide net; if you exceed default caps, say so in the ledger and temper confidence or caveats accordingly.  
4. **No chaos:** do not reorder the **default** profile into wiki-first or skip code for product-behaviour questions unless the **user explicitly** asks for that one-off; extensions are **after** the default path or justified skip, not a replacement taxonomy.

**Searching past answers (lmwtfy-only, not part of shared four-source profile):** Use the workspace **Grep** tool or `rg` against `./docs/lmwtfy-answers/` instead of assuming a Unix `grep` binary.

## Trigger Phrases

- "lmwtfy [question]"
- "colleague question about..."
- "answer question from..."
- "wiki that for me"
- "research this for [name]"

## Step 0: Question Decomposition

Before researching, restate the question and break it into verifiable parts.

1. **Restate in plain language** - One sentence: what is the colleague actually asking?
2. **List the specific claims to verify** - Turn the question into yes/no checkpoints. Example: "Can SIF handle concurrent writes?" becomes:
   - Does SIF API support concurrent requests?
   - Is there locking or queuing?
   - What happens on conflict?
3. **Show the decomposition** - Present it to the user: "Here's what I think they're asking and what I need to check. Correct before I dig in?"

This prevents answering the wrong question or missing a sub-question buried in the original phrasing.

## Steps 1–4: Corpus retrieval (default profile, optional extension)

After Step 0 (and user correction if any), run **`profile:code-first-research`** as defined in [`shared/evidence/profiles/code-first-research.md`](../shared/evidence/profiles/code-first-research.md), respecting [`shared/evidence/budgets.md`](../shared/evidence/budgets.md) and [`shared/evidence/verification-and-leads.md`](../shared/evidence/verification-and-leads.md). That pass is the **required baseline** unless you document a justified skip in the ledger (rare).

- **§1 GitHub / source code** — first; use commands and repo list from the profile + `sources-and-tools.md`.  
- **§2 Ratatoskr** — follow `ratatoskr-preflight.md` first; then `ratatoskr-mcp-tools.md` for tool order.  
- **§3 Azure DevOps** — only when the question references work items, releases, or backlog; tools from ADO descriptors per `sources-and-tools.md`.  
- **§4 Wiki** — last among the four; search/read steps and URL recording per the profile.

**Conflict resolution** is defined in the profile (**code wins**); note discrepancies in the ledger and answer.

**Then (optional):** If the **Controlled extensions** rules in the shared-layer section apply, perform additional retrieval and **record every extension** in the evidence ledger with **Verified how** per **`evidence-playbook.md`**. Do **not** substitute wiki-first or another wholesale reorder as the silent default; a **user-requested** one-off order change is allowed and must also be **declared** in the ledger, with the same verification bar for every source you cite.

## Step 5: Existing Answers

Check if a similar question was already answered under **`./docs/lmwtfy-answers/`** using the workspace **Grep** tool or `rg` (do not rely on `grep` on Windows).

## Step 6: Evidence Ledger

Present this ledger to the user BEFORE writing the answer file.

For each factual claim you plan to include, fill one row:

**Claim:** [the specific statement you will write]
**Source:** [GitHub file:line URL / help center topic URL / DevOps work item / wiki URL / "UNVERIFIED"]
**Verified how:** [read the full file | read the help topic | read the wiki section | traced code path from X to Y | searched but found nothing]

Use the ledger row template and verification rules in **`shared/evidence/verification-and-leads.md`**, aligned with **`shared/evidence/evidence-playbook.md`** (verified vs lead vs inferred; confidence levels). UNVERIFIED claims must be verified, downgraded to low confidence, or removed.

If you used **Controlled extensions** (extra sources, extra passes, justified skip of the default profile, or user-requested order change), the ledger must include that disclosure **before** you ask for approval: what extended beyond the default profile, why, and how each cited line meets **`evidence-playbook.md`** §4.

After presenting the ledger, ask: **"Evidence checks out? OK to write the answer?"**

## Step 7: Write the Answer

Only after the user approves the evidence ledger, write the answer file.

Follow the output format, file template, and formatting rules in `rules/lmwtfy-format.md`.

Include **Documentation assessment** (required) after **Findings**: **Status** (`well_documented` | `partially_documented` | `missing_documentation`), **Explanation** (short, evidence-based), and **Suggested documentation changes** (bullets when status is partial or missing; concrete wiki/help additions). Calibrate **only** from **verified** official wiki/help (and similar prose you actually read per playbook **§4**), not from code alone and not from **leads**; definitions and orthogonality to **confidence**: **`shared/evidence/evidence-playbook.md`** §8 and §5.

When your findings contradict the colleague's assumptions, follow the framing guidance in `rules/lmwtfy-framing.md`.

### Confidence Levels

- **High** - Verified in source code + at least one other source (help center, wiki, or DevOps). No hedging needed.
- **Medium** - Found in one source only. Include with caveat: "Verified in [source] only."
- **Low** - Based on general knowledge, not verified. Flag explicitly: "Not verified; needs confirmation from [team/person]."

Before finishing, verify every URL in the answer is real and every claim has a source link.

## Step 8: Wiki Publication Check (Self-Improving Knowledge Loop)

After saving the answer, check if this knowledge should be on the team wiki. Follow the full pattern in `rules/knowledge-loop.md` (wiki search/read for the loop uses the **same shared layer** — profile **§4** plus `sources-and-tools.md` and `budgets.md`, as referenced from that rule file). Quick version:

1. Search wiki per shared **§4** + `knowledge-loop.md` Step 1.
2. **Classify coverage:**
   - Well covered - stop, no action needed
   - Partially covered - propose an edit to the existing page
   - Not covered - propose a new wiki page
3. **Draft wiki content** in wikitext format (not markdown). Keep it concise. Add `[[Category:...]]` tags.
4. **Show the proposal** to the user and ask: "Publish this to the wiki? (yes / edit first / skip)"
5. **If approved:** use **`user-mediawiki`** `mediawiki_edit_page` (or the appropriate edit tool from descriptors) with **`preview=true`** first, then publish after confirmation per wiki MCP safety rules

Skip this step when:
- The answer is customer-specific or contains sensitive/internal data
- Confidence is low or medium
- The user said "skip wiki" or "private only"
- The question is about a one-off bug or transient issue

## Rationalizations to Reject

### Content traps

| Rationalization | Why It's Wrong |
|---|---|
| "This is a standard feature, it must exist" | Public 360° is not a generic product. Standard for competitors does not mean standard here. |
| "The wiki doesn't mention it, so it's not supported" | Wiki coverage is incomplete. Check source code before concluding Nei. |
| "I found a class/method name that matches, so it works" | File names and method signatures prove existence, not behavior. Read the implementation. |
| "SIF probably handles this" | SIF has specific operations. Check the actual API contract, not what seems reasonable. |

### Process traps

| Rationalization | Why It's Wrong |
|---|---|
| "I already found this in a search snippet, no need to read the full file" | See **`shared/evidence/verification-and-leads.md`** — `gh search code` results are fragments; read the actual file. |
| "The wiki page title confirms this" | Wiki page titles can be misleading. Open the page per shared profile **§4** and read the relevant section. |

## What This Skill Is NOT

- Not for bid/tender responses
- Not for writing wiki pages directly (use mediawiki MCP for that)
- Not for standup or weekly status updates

## MCP Tools Used

**Default:** corpus tools **per** [`shared/evidence/sources-and-tools.md`](../shared/evidence/sources-and-tools.md) and **`profile:code-first-research`** (profile **§1–§4**): **gh** / Grep / WebFetch, **`user-ratatoskr`**, **`user-azure-devops`**, **`user-mediawiki`**. **Extensions:** any extra tool or corpus still follows **`sources-and-tools.md`** where it applies and **`evidence-playbook.md`** for verification; declare in the ledger (shared-layer **Controlled extensions**).

## Rules Referenced

- `shared/evidence/README.md` — Shared retrieval index; **`lmwtfy`** → **`profile:code-first-research`**
- `shared/evidence/evidence-playbook.md` — Unified claim / evidence / confidence / conflict vocabulary
- `shared/evidence/budgets.md` — Default caps
- `shared/evidence/profiles/code-first-research.md` — **Normative** code-first load order and per-source steps
- `shared/evidence/sources-and-tools.md` — MCP hygiene, repos, GitHub / workspace search
- `shared/evidence/ratatoskr-preflight.md` — Help center preflight and fallbacks
- `shared/evidence/verification-and-leads.md` — Leads vs verification; ledger alignment
- `rules/context-assembly.md` — Historical `product-context` name; points to shared profile
- `rules/ratatoskr-mcp-tools.md` — **`user-ratatoskr`** tool names and usage order
- `rules/lmwtfy-format.md` — Output template, formatting rules, and file location
- `rules/lmwtfy-framing.md` — How to frame answers that contradict colleague beliefs
- `rules/knowledge-loop.md` — Wiki publication loop (wiki steps via shared **§4**)

## Output Directory

**Default in this repo:** `./docs/lmwtfy-answers/`. You can override per run if the user asks for a different folder; then use that path consistently in Step 5, Step 7, and in `rules/lmwtfy-format.md`.
