# Profile: code-first-research

**Id:** `profile:code-first-research`  
**Used by:** **`lmwtfy`** (colleague question research).  
**Packet name:** `product-context` (same content as historically in `rules/context-assembly.md`).

**Evidence semantics:** **[`../evidence-playbook.md`](../evidence-playbook.md)** is authoritative for **claim**, **evidence**, **verified**, **lead**, **inferred**, **confidence**, **when to stop**, and **conflicts**. This profile defines **load order and tools only**; do not redefine those terms here.

**Also read:** [`../README.md`](../README.md), [`../budgets.md`](../budgets.md), [`../sources-and-tools.md`](../sources-and-tools.md), [`../ratatoskr-preflight.md`](../ratatoskr-preflight.md), [`../verification-and-leads.md`](../verification-and-leads.md). Tool names: `.cursor/skills/lmwtfy/rules/ratatoskr-mcp-tools.md`.

**Bounded retrieval (`lmwtfy`):** Apply default caps in [`../budgets.md`](../budgets.md) unless the user explicitly expands the budget. Skipped sources belong in the evidence ledger with reason (per **`evidence-playbook.md`**).

---

## Source reliability order

**Load order (unchanged):** 1 GitHub → 2 Ratatoskr → 3 ADO (if relevant) → 4 Wiki.

**Conflict rule (unchanged):** When **verified** sources disagree on shipped behaviour, **implementation (code) wins** over help text; note the discrepancy in the ledger and answer. Full wording: **`evidence-playbook.md`** §7; tier alignment for PFR-style work: **`pfr-ai-capability-check/references/pfr_evidence_sources_credibility.md`**.

---

## Load order (attempt all four in this sequence)

Skills may **skip** a source when irrelevant (e.g. no work item reference → skip DevOps).

### 1. GitHub / source code

Search source code **first**. Use `gh` CLI when available; patterns:

```bash
# Prefer gh api for structured data; WebFetch for documentation pages
gh api search/code -X GET -f q="[search term] org:te-industry-public360" \
  --jq '.items[] | {path: .path, repo: .repository.full_name}'
```

```bash
# Search across a repo
gh search code "SearchTerm" --repo te-industry-public360/core-bl --limit 10

# Read specific files
gh api repos/{owner}/{repo}/contents/{path} --jq '.content' | base64 -d

# Browse directory
gh api repos/{owner}/{repo}/contents/{path} --jq '.[].name'

# Recursive tree
gh api "repos/{owner}/{repo}/git/trees/{branch}?recursive=1" --jq '.tree[] | select(.path | startswith("some/path")) | .path'
```

Key repositories:

- `te-industry-public360/core-bl` — Core business logic, SIF API contracts  
- `te-industry-public360/cie-*` — Customer-specific implementations  
- `te-industry-public360/core-*` — Other core components  

### 2. 360 Online help (`user-ratatoskr`)

Search the 360 Online help center for customer-facing documentation (1500+ topics). Use **`user-ratatoskr`**; see **`ratatoskr-mcp-tools.md`** for exact tool names. Before each call, read `mcps/user-ratatoskr/tools/<tool>.json` when that folder exists.

**Preflight:** follow [`../ratatoskr-preflight.md`](../ratatoskr-preflight.md). If help fetch fails after preflight, record in the evidence ledger, apply fallbacks there, and **continue**; do not block the whole answer on help center alone.

Help center sections:

- **Release Information** (~340 topics): release notes for 360° Online, Plan & Build, Collect, eManager, OpenGov  
- **360° Administrator (English)** (~630 topics): full admin documentation  
- **360° Administrator (Norsk)** (~530 topics): admin docs in Norwegian  

### 3. Azure DevOps (if relevant)

Search Azure DevOps when the question relates to specific work items, bugs, feature requests, or customer implementations.

Use **`user-azure-devops`**; pick tools from descriptors (search vs get-by-id). If the Cursor setup only has one org/project, say that in the ledger; do not assume a second org unless configured.

### 4. Wiki (`user-mediawiki`)

Search the Public 360° wiki for internal product documentation and broader context.

- Use `mediawiki_search` for broad topic discovery  
- Use `mediawiki_get_page` to read specific pages  
- Use `mediawiki_search_in_page` to find specific content within a known page  
- Record page URLs for every piece of information found  

---

## Extract (what to pull into notes / ledger)

Fields to capture map to **`evidence-playbook.md`** §2. Practically:

- Source code file paths and relevant lines (as GitHub URLs, not local paths)  
- Help center topic URLs and key findings  
- DevOps work item status, assignees, and acceptance criteria  
- Wiki page URLs and supplementary context  

---

## How lmwtfy references this profile

The **`lmwtfy`** `SKILL.md` points here for **research order** and conflict handling. Question decomposition, evidence ledger presentation, answer file format, and wiki publication loop stay in **`lmwtfy/rules/`**.

---

## Rules

- This packet is **documentation**, not code. The agent reads the packet and follows it; there is no runtime framework.  
- When the packet changes (new source, extraction logic), skills that link here should be updated if their steps diverge.

---

**File:** `shared/evidence/profiles/code-first-research.md`
