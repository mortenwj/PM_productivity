# user-ratatoskr MCP tools (tender-response)

**Server id:** `user-ratatoskr`

**Descriptors:** Use `GetMcpTools` with `server: user-ratatoskr` before calling. When `mcps/user-ratatoskr/tools/` exists in the workspace, read the JSON descriptor for each tool.

**Preflight:** [`../../shared/evidence/ratatoskr-preflight.md`](../../shared/evidence/ratatoskr-preflight.md) — DNS/VPN issues often block help fetches even when MCP is "connected".

**Full reference (shared with lmwtfy):** `~/.cursor/skills/lmwtfy/rules/ratatoskr-mcp-tools.md`

---

## Typical call order for tender research

1. **`list_sections`** — get `section_id` (`release`, `admin-en`, `admin-no`).
2. **`search_topics`** — `query` from krav keywords; `search_content: true` when titles miss.
3. **`read_topic`** — full page for verification (required before claiming capability).
4. **`lookup_config`** — krav names a setting, metadata field, or code table.
5. **`feature_timeline`** — version/date claims ("støttet siden", release history).
6. **`get_linked_files`** + **`read_pdf`** — certifications, NOARK letters, attached specs linked from help.

Use **`admin-no`** for Norwegian tender language alignment; **`admin-en`** for technical precision. Use **`release`** for version-gated statements.

---

## Tool quick reference

| Tool | When for tenders |
|------|------------------|
| `list_sections` | First call when section IDs unknown |
| `search_topics` | Discover topics by krav keywords |
| `read_topic` | Verify capability text before drafting |
| `search_in_page` | Long policy topic; find specific paragraph |
| `lookup_config` | Named configuration / register field in krav |
| `feature_timeline` | Prove or qualify version availability |
| `compare_topic` | EN vs NO admin wording for bilingual bids |
| `get_linked_files` | Find PDF certificates linked from help |
| `read_pdf` | Read certification / compliance PDFs |

---

## Budget

Default: **≤3** `read_topic` calls per requirement unless user expands. See [`../../shared/evidence/budgets.md`](../../shared/evidence/budgets.md).

---

## When Ratatoskr is unavailable

1. Record skip in tender evidence ledger.
2. Fall back: `docs/tender-reference/extracted/` → MediaWiki → `docs/product/` → code → ask user for pasted help excerpt.
3. Temper confidence; do not state **Met** on product capability without another verified source.
