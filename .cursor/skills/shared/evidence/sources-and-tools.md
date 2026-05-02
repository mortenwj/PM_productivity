# Sources and tools

**Purpose:** Align **which systems** to query and **how** to invoke tools safely across skills.

**Semantics:** **[`evidence-playbook.md`](evidence-playbook.md)** is authoritative for **claim**, **evidence**, **verified**, **lead**, **confidence**, and related terms. This file only covers **systems and commands**.

---

## MCP hygiene

**Before calling any MCP tool:** read its JSON descriptor under `mcps/<server>/tools/<tool>.json` in this workspace (when present), then invoke with `call_mcp_tool` using the server id and tool name from the descriptor.

If a server is not configured, skip that source and record the skip in the run notes (map to PFR `limitations` / ledger or lmwtfy ledger per **`evidence-playbook.md`**). **Do not invent tool names.**

---

## Cursor MCP servers (typical)

| Source | Server id (when enabled) | Typical tools |
|---------|--------------------------|---------------|
| Wiki | `user-mediawiki` | `mediawiki_search`, `mediawiki_get_page`, `mediawiki_search_in_page`, `mediawiki_edit_page`, … |
| 360 Online help | `user-ratatoskr` | See `.cursor/skills/lmwtfy/rules/ratatoskr-mcp-tools.md` for canonical names (`list_sections`, `search_topics`, `read_topic`, …). Before each call, read `mcps/user-ratatoskr/tools/<tool>.json` when that folder exists. |
| Azure DevOps | `user-azure-devops` | Match names in that server’s descriptors (work item read, search, WIQL, batch). |

---

## GitHub / local code

- **Prefer `gh` in the terminal** when available; otherwise use **WebFetch** for raw GitHub URLs or the repo browser.
- **Workspace search:** use the Cursor **Grep** tool or `rg` (do not assume a Unix `grep` binary on Windows).

Turning a **hit** into **verified** evidence (read file, stable link) is defined in **`evidence-playbook.md`** §3–§4 and [`verification-and-leads.md`](verification-and-leads.md).

**Key repositories** (lmwtfy defaults; adjust if the question names another repo):

- `te-industry-public360/core-bl` — Core business logic, SIF API contracts  
- `te-industry-public360/cie-*` — Customer-specific implementations  
- `te-industry-public360/core-*` — Other core components  

Example structured code search:

```bash
gh api search/code -X GET -f q="[search term] org:te-industry-public360" \
  --jq '.items[] | {path: .path, repo: .repository.full_name}'
```

Example repo-scoped search (CLI):

```bash
gh search code "SearchTerm" --repo te-industry-public360/core-bl --limit 10
```

Read file content (pattern):

```bash
gh api repos/{owner}/{repo}/contents/{path} --jq '.content' | base64 -d
```

Browse directory / tree (patterns above) for navigation, then complete **verification** per **`evidence-playbook.md`** §4.

---

## Help center sections (Ratatoskr)

- **Release Information** (~340 topics): release notes for 360° Online, Plan & Build, Collect, eManager, OpenGov  
- **360° Administrator (English)** (~630 topics): full admin documentation  
- **360° Administrator (Norsk)** (~530 topics): admin docs in Norwegian  

---

**File:** `shared/evidence/sources-and-tools.md`
