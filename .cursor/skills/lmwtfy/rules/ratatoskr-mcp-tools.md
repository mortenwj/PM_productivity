# user-ratatoskr MCP tools (360 Online help center)

**Server id for `call_mcp_tool`:** `user-ratatoskr`

**Descriptors:** Cursor mirrors JSON schemas under `mcps/user-ratatoskr/tools/<tool>.json` when the Ratatoskr MCP server is enabled for the workspace. This project’s `mcps` folder may only contain `user-mediawiki` until Ratatoskr is turned on; tool names below match the published Ratatoskr server (same set as in other local projects, e.g. `empty-window`).

Always read the live descriptor before calling if parameters differ from a short summary here.

## Making Ratatoskr actually return help content

**MCP “online” is not enough.** `list_sections` may succeed while `search_topics` / `read_topic` fail with **`no such host`** for `help.360online.com`. The Ratatoskr **server process** must resolve that hostname the same way your laptop does (often **corporate DNS**, for example a resolver under `*.tieto.com`, sometimes only on **VPN**).

**What fixes it (pick what matches your setup):**

1. Run Cursor and the agent **locally** on a machine where `nslookup help.360online.com` succeeds for the **same network** the MCP runtime uses.
2. Turn on **VPN** (or office network) if internal DNS or split DNS is required for that name.
3. Avoid relying on Ratatoskr from **cloud or isolated** runners unless that environment is given the same DNS and egress; use **`SKILL.md` Step 2 fallbacks** (wiki, WebFetch where public, user paste, re-run locally).

**Preflight:** After `list_sections`, one small **`search_topics`** call proves whether TOC fetch works for this session.

## All tools (alphabetical)

| Tool name | Purpose (short) |
|-----------|-----------------|
| `audit_links` | Audit help-center document links; optional `section_id`; full scan is slow. |
| `check_translations` | EN vs NO admin doc coverage by shared URL paths; no required args. |
| `compare_topic` | Search a **term** across all sections (release + admin-en + admin-no); cross-cutting view. |
| `feature_timeline` | Chronological release-note mentions for a **feature** name. |
| `find_similar_pages` | Similar titles within a section, or EN/NO pairs via `cross_section`; optional `compare_content`, `threshold`. |
| `get_linked_files` | **Required:** `section_id`, `url`. PDFs/ZIPs linked from a topic. |
| `list_sections` | Lists sections (`release`, `admin-en`, `admin-no`, …); **call first** when you need `section_id`. |
| `list_topics` | TOC for a section; optional `section_id`, `filter`. |
| `lookup_config` | Search settings / register fields / code tables by **query** (word-level AND). First call may be slow (index build). |
| `read_image` | **Required:** full HTTPS **url** of an image on help.360online.com (from `read_topic`). |
| `read_pdf` | **Required:** full HTTPS **url** of PDF from `get_linked_files`; needs local `pdftotext` per descriptor. |
| `read_topic` | **Required:** `section_id`, `url` (path from `list_topics` / `search_topics`). Full page as plain text. |
| `search_in_page` | **Required:** `section_id`, `url`, `query`; optional `context_lines`. |
| `search_topics` | **Required:** `query`; optional `search_content`, `section_id`. |
| `topic_diff` | **Required:** `url` (shared path); optional `section_a`, `section_b`, `context_lines`. Default EN vs NO diff. |

## Typical call order for lmwtfy (Step 2)

1. **`list_sections`** if you do not already have valid `section_id` values.
2. **`search_topics`** with `query`; set `search_content: true` when title search is not enough.
3. **`read_topic`** for full verification, or **`search_in_page`** when the page is long and you need a needle.
4. **`feature_timeline`** when the question is “when did X ship / change?”.
5. **`compare_topic`** when the question needs how a term appears across languages and release vs admin.
6. **`lookup_config`** when the colleague asks about a **configuration setting**, register field, or code table (not general product behavior).

Secondary / specialist:

- **`get_linked_files`** then **`read_pdf`** when the answer lives in an attached PDF.
- **`read_image`** for screenshots or diagrams referenced in a topic.
- **`check_translations`**, **`find_similar_pages`**, **`topic_diff`** for documentation-quality or EN/NO drift questions (less common for one-off colleague answers).
- **`audit_links`** for link-health QA (usually out of scope for lmwtfy unless explicitly asked).

## Section IDs (from `list_sections`)

Do not hard-code beyond examples; always prefer **`list_sections`** output. Common values in descriptors: `release`, `admin-en`, `admin-no`.
