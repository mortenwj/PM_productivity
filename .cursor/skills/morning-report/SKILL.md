---
name: morning-report
description: >-
  Generates the Process Platform morning report from Azure DevOps and GitHub
  per MORNING_REPORT_SPEC.md: last-2-workdays for §3 only; §1 Requires your
  attention has no filters—full pagination, full Assigned/My activity tables,
  full comment threads for mention classification, wit_my_work_items plus
  optional saved query. Writes
  morning_report.md at repo root. Use when
  the user says good morning, asks for a morning report, daily standup digest,
  @mention no reply, threads awaiting reply, or Process Platform /
  Core-Process-platform recent activity summary.
---

# Morning report

## Before you start

1. Read **`MORNING_REPORT_SPEC.md`** at the repository root (authoritative: time window, section order, MCP tools, GitHub config).
2. Use **today’s date** as “report date” and compute the **2-workday cutoff** only for **§3** and **GitHub**. **§1** must follow **`§1 — Exhaustive retrieval`** in the spec: **no** filters, samples, or row caps—page MCP/ADO until feeds and comments are complete.

## Default scope (unless the user overrides)

| Item | Value |
|------|--------|
| ADO project | `360` |
| ADO team | `Core-Process-platform` |
| “Recent” window | Last 2 workdays for **§3** + GitHub only; **§1** = no filters (see spec §1 exhaustive block) |
| Output file | `morning_report.md` (repo root; overwrite for the current run) |

GitHub repos and `team_github_users`: read from repo `config.json` key `morning_report` if present; otherwise follow defaults in the spec.

## Execution order (fast path)

Follow **section order** in the spec. Do not reorder sections.

1. **Requires your attention** (two parts, in this order; **show everything** per spec):  
   - **(a) @mentioned me — awaiting my reply** – Full candidate union from **paged** **`wit_my_work_items`** (**myactivity**, **assignedtome**) ± **`wit_get_query_results_by_id`** (`attention_query_id`). **`core_get_identity_ids`** + **`wit_list_work_item_comments`** with **all** comment pages per ID. Output a table of **every** item matching the spec’s mention/no-reply rule (empty table + explanation only if truly zero after full scan).  
   - **(b) Assigned / activity** – Two **complete** tables (or equivalent): **every** row from **Assigned to me** and **every** row from **My activity** (ID, Title, State, Changed as available), plus ADO links to those views. No samples, no §3 cutoff, no truncation for file size.
2. **Your assigned work** – Active / new / recent sample; not completed; link IDs to ADO.
3. **Process Platform team – recent activity**  
   - 3.1 Work items changed (current iteration only; table: ID, Title, State, Changed, Assigned to; sort Changed desc).  
   - 3.2 Recent comments (latest per item only if comment in window).  
   - 3.3 Development activities – commits + open PRs per spec; filter by `team_github_users` when configured.  
   - 3.4 Sprint snapshot – counts by state; **closed in last 2 workdays** count.
4. **Current iteration** – Name, span, days left, link to board (use live iteration from `work_list_team_iterations`; do not hardcode sprint names from old samples).
5. **Team capacity** – Optional; include if MCP returns data without extra friction.
6. **Notes** – Short follow-ups for the user to fill or leave a placeholder.

## MCP mapping

Use the tool names and purposes listed in **`MORNING_REPORT_SPEC.md`** (Azure DevOps + GitHub). For §1, **prefer** `wit_my_work_items` + optional **`wit_get_query_results_by_id`** over ad-hoc WIQL; **always** paginate to completion. Prefer batch/detail calls over redundant round-trips. If paging is impossible with the tools available, document that in **Notes** as a gap—not as an intentional partial report.

## Output quality

- Put a **title line** with report date and a **one-line window summary** for **§3** (cutoff date in UTC); state that **§1** is **unfiltered** and exhaustive per spec.
- Under **Requires your attention**: **###** for **@mentioned me — awaiting my reply** (full results table); **###** for **Assigned to me (all)** and **My activity (all)** with **complete** tables per spec—not shortened lists.
- Use **markdown tables** for 3.1 where practical; keep snippets to 1–2 lines for 3.2.
- Link work items with standard ADO edit URLs.

## Do not rely on

- **`generate_morning_report.py`** – informational only in this repo; it does not fetch ADO/GitHub data. Real generation is via MCP per the spec (or a separate `good_morning_report` MCP if the user has it configured).

## After writing

- Save **`morning_report.md`** at repo root.
- Give the user a **2–4 sentence** verbal summary in chat pointing to the file.
