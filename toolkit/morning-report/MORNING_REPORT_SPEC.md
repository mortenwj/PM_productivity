# Morning Report – Spec and structure

This document describes how the morning report is generated so you (or the agent) can produce it consistently. Say **"Good morning"** in Cursor to generate the report.

---

## Time window

- **Last 2 workdays** – Used **only** for **§3 Process Platform team – recent activity** (3.1–3.4) and **GitHub** (§3.3): work items changed, team comments, sprint “closed in window”, and commits/PRs. Workdays = weekdays (Mon–Fri); exclude weekends. Cutoff = start of the day that is 2 workdays ago (e.g. if today is Tuesday, cutoff = start of Friday).
- **§1 Requires your attention** – **No filters** (see dedicated rules below): no date window, no state/type pruning, no row caps, no “sample” or “highlights” subset. **Page every API response** until each source is exhausted; only then may you note a **tooling** failure (not an intentional trim).

---

## Section order

1. **Requires your attention** – **Show everything** from the sources below—**no** filters, caps, or samples. Includes:  
   - **(a) @mentioned me — awaiting my reply** – After you have the **full** candidate union and **full** comment history per item (see below), list **every** work item where someone else @mentioned you and you have **not** posted any comment **after** that mention (algorithm below). That rule is **classification** for this sub-table only, not a reason to shrink the feeds.  
   - **(b) Assigned / activity** – **Complete** outputs for **Assigned to me** and **My activity**: every work item ID each feed returns, with links/titles/states (tables or equivalent). Same semantics as the ADO web UI. **No** §3 cutoff and **no** shortening for length.
2. **Your assigned work** – Assigned to me (active, new/recent, sample). Not completed.
3. **Process Platform team – recent activity**  
   - 3.1 Work items changed (last 2 workdays) – Current iteration only; table: ID, Title, State, Changed (date), Assigned to. Sorted by Changed desc.  
   - 3.2 Recent comments (last 2 workdays) – Latest comment per work item, only if that comment is within last 2 workdays. Item link, author, date, short snippet (1–2 lines).  
   - 3.3 **Development activities (last 2 workdays)** – Code commits and pull requests from GitHub. Same time window as work items (last 2 workdays). See data sources below.  
   - 3.4 Sprint snapshot – Counts by state (New, Active, Resolved, Closed) for current iteration; **closed in last 2 workdays** count.
4. **Current iteration (PP-20)** – Span, days left, link to board.
5. **Team capacity** – Current iteration capacity (optional).
6. **Notes** – Your follow-ups and reminders.

---

## §1 — Exhaustive retrieval (mandatory)

1. **`wit_my_work_items`:** For **`myactivity`** and **`assignedtome`**, use the largest allowed `top` and **repeat** using whatever continuation the REST/MCP exposes (`hasMore`, `$skip`, `continuationToken`, next page—follow ADO docs for that endpoint) until **no** further work items are returned.  
2. **`wit_get_query_results_by_id`:** If `attention_query_id` is set, page the same way until the query result set is **fully** retrieved.  
3. **`wit_list_work_item_comments`:** For §1 mention classification, load **all** comments for each candidate ID (pager or repeated calls), not a partial first page—otherwise “awaiting reply” can be wrong.  
4. **Report:** Do **not** omit §1 rows to keep the file short; long markdown tables in one `morning_report.md` are expected.

---

## @mentioned me — awaiting my reply (definition)

**Goal:** List **every** work item in the candidate union where the **latest @mention of the report user** (from someone else) has **no follow-up comment authored by the report user** after that mention’s `createdDate`. **No** age or row cap—if the condition holds after a full comment load, the row appears. **(b)** must still list **all** feed rows so nothing is dropped from the report; **(a)** is this derived sub-table only, not a substitute for the full feeds.

**Identity (report user):**

1. Call `core_get_identity_ids` with the authenticated user’s email / `uniqueName` (e.g. `morten.jensen@tieto.com`) and take the returned **`id`** (GUID). Use this to match `mentions[].artifactId` and `mentions[].targetId` (case-insensitive string compare).

### Prefer standard DevOps queries (candidate work items)

Use the **same sources as the Azure DevOps web client** where the MCP exposes them—**before** ad‑hoc WIQL or hand-picked ID lists.

1. **`wit_my_work_items` (`myactivity`)** – **My activity**. Page until empty (see **§1 — Exhaustive retrieval**).  
2. **`wit_my_work_items` (`assignedtome`)** – **Assigned to me**. Page until empty.  
3. **Optional saved query:** If `morning_report.attention_query_id` is set, **`wit_get_query_results_by_id`** — page until empty; merge IDs into the candidate union (dedupe by ID only for mention scan, not for dropping rows from (b)). Use **`wit_get_query`** only to resolve or document the query when helpful.

**Union** the IDs from (1)–(3), then for **each** candidate run the **per work item** steps below. Only if no predefined/saved path exists should you invent WIQL solely to build candidates.

**Per work item:**

1. `wit_list_work_item_comments` — fetch **all** pages of comments for this work item (no partial thread).  
2. Sort comments by `createdDate` ascending.  
3. Find the **latest** comment where:  
   - `mentions` includes the report user’s GUID (see above), **and**  
   - `createdBy.id` is **not** the report user (ignore self-mentions / you pinging yourself).  
4. If no such comment → item does **not** qualify for this subsection.  
5. If such comment exists at time **T**: check whether **any** comment has `createdDate` **> T** and `createdBy.id` **equals** the report user. If **yes** → you replied; **exclude** the item. If **no** → **include** the item (**awaiting your reply**).

**Report output for each row:** Work item link, title (from batch get), **last @mention** author + date (UTC), one-line snippet from that comment (strip HTML if needed).

---

## Data sources (Azure DevOps MCP)

- **Report user id:** `core_get_identity_ids` (searchFilter = user email / unique name) → use `id` for mention matching.
- **Standard lists (§1):** `wit_my_work_items` (**assignedtome**, **myactivity**, project 360) — page until exhausted; same as **Assigned to me** / **My activity**. Prefer these over custom WIQL for candidate IDs.  
- **Optional saved query (§1):** `wit_get_query_results_by_id` when `morning_report.attention_query_id` is set in `config.json`.  
- **Attention / mention scan:** `wit_list_work_item_comments` on the §1 candidate union; match `comment.mentions` to the report user id. Work item titles via `wit_get_work_items_batch_by_ids`.
- **Team iteration:** `work_list_team_iterations` (project 360, team Core-Process-platform, timeframe current).
- **Iteration work items:** `wit_get_work_items_for_iteration` (same project, team, iteration id).
- **Work item details:** `wit_get_work_items_batch_by_ids` with fields: System.Id, System.Title, System.State, System.ChangedDate, System.WorkItemType, System.AssignedTo.
- **Recent comments:** `wit_list_work_item_comments` for items changed in last 2 workdays; show latest comment if `createdDate` is within last 2 workdays.
- **Capacity:** `work_get_team_capacity` (project, team, iteration id).

### GitHub (development activities)

- **Repos:** Configured in `config.json` under `morning_report.repos` (default: `te-industry-public360/core-bl`).
- **Team filter:** Only include commits and PRs from Process Platform team members. Configure `morning_report.team_github_users` in `config.json` with GitHub login names (e.g. `BjornTieto`). If not configured, show all contributors (shared repo has many non-team contributors).
- **Commits:** `mcp_github_list_commits` (owner, repo, sha=branch, perPage=30). Filter by (a) `commit.author.date` within last 2 workdays (same cutoff as work items), and (b) `author.login` in `team_github_users`.
- **Pull requests:** `mcp_github_list_pull_requests` (owner, repo, state=open, per_page=15). Filter by `user.login` in `team_github_users`. Show only open PRs from team members.

---

## Defaults (current)

| Setting | Value |
|--------|--------|
| Project | 360 |
| Team | Core-Process-platform |
| Time window | Last 2 workdays (**§3 and GitHub only**; **not** §1) |
| §1 Requires your attention | **No filters**; full pagination; full (b) tables; full comments for (a); optional `attention_query_id` |
| GitHub repos | te-industry-public360/core-bl (configurable in config.json) |
| Comment scope | §3.2: latest comment per item only if in last 2 workdays; §1: **all** comments per candidate for mention logic; **no** trimming |
| @mention / no-reply | Prefer `wit_my_work_items` (myactivity ∪ assignedtome) ± `wit_get_query_results_by_id`; then `core_get_identity_ids` + `wit_list_work_item_comments` |
| Team scope | Current iteration only |
| Sprint snapshot | Yes, including "closed in last 2 workdays" |

---

## Output

- **File:** `outputs/morning/morning_report.md` in this repo.
- **Cutoff for last 2 workdays:** Compute for **§3 / GitHub only** (start of the day that is 2 workdays ago, weekdays only). State it in the report header. **§1** uses **no** time or row filters—only the mention/reply **definition** selects rows for sub-table (a); (b) is the **full** feed contents.

---

## GitHub repo configuration

Add `morning_report` to `config.json`:

```json
{
  "morning_report": {
    "repos": [
      {"owner": "te-industry-public360", "repo": "core-bl", "branch": "master"}
    ],
    "team_github_users": ["BjornTieto", "andreas-hjelmborg", "..." ],
    "attention_query_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
  }
}
```

- **attention_query_id (optional):** GUID of a **saved work item query** in Azure DevOps. When set, merge `wit_get_query_results_by_id` results into §1 candidates (standard DevOps query, team-maintained). Omit if unused.
- **repos:** Which repos to include. Default: `te-industry-public360/core-bl` (branch: master).
- **team_github_users:** GitHub login names of Process Platform team members. Only commits and PRs from these users are shown in development activities. The core-bl repo is shared; without this filter, the report would show contributors from other teams. Add the correct GitHub usernames for: Bjørn Kristiansen, Andreas Hjelmborg, Aniket Jagtap, Ashish Chaudhari, Jette Smith, Mudita Sharma, Nikisha Nevase, Sumit Pandey.
