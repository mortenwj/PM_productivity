# Daily workflow – stay on top as PM

Use this from **Cursor** with **Azure DevOps** and **GitHub** MCP tools so you rarely need to leave the editor.

---

## 1. Start the day: morning report

**In Cursor**, ask the agent to generate your morning report, for example:

- *"Good morning"*
- *"Generate my morning report"*
- *"Morning report for Core-Process-platform"*

The agent will use Azure DevOps MCP to:

- Get your **assigned work items** (and optionally “my activity”)
- List **current iteration** and **team capacity**
- Highlight items that **need your attention** (e.g. where you’re mentioned in comments)
- **Process Platform team – recent activity (last 2 workdays):** work items changed, recent comments, sprint snapshot
- Save a markdown file: `outputs/morning/morning_report.md`

Open that file in this repo to see:

- **Requires attention** – items you should act on first
- **Your assigned work** – active, new, and other assigned items
- **Process Platform team – recent activity** – items changed in 48h, recent comments, sprint snapshot
- **Current iteration** – team scope and days left
- **Notes** – follow-ups and reminders

Report structure and time window (last 2 workdays): see [toolkit/morning-report/MORNING_REPORT_SPEC.md](toolkit/morning-report/MORNING_REPORT_SPEC.md).

---

## 2. Azure DevOps – quick checks without leaving Cursor

You can ask the agent to run MCP actions such as:

| Goal | Example prompt |
|------|----------------|
| My work | *"List my work items assigned to me in 360"* |
| Backlog | *"Show backlog for Core-Process-platform"* |
| Iteration work | *"Work items for current iteration in 360"* |
| One item | *"Get work item 165592 in project 360"* |
| Comments | *"List comments on work item 165592"* |
| Add comment | *"Add a comment to work item 165592: …"* |
| Update state | *"Update work item 165592 to Active"* |
| Capacity | *"Team capacity for current iteration"* |

Default project/team in your setup: **360**, **Core-Process-platform**. Say the project/team name if you use others.

---

## 3. GitHub – issues and PRs

Use the GitHub MCP from the same Cursor workspace:

| Goal | Example prompt |
|------|----------------|
| My issues | *"List my open issues in mortenwj/pm-productivity"* |
| Open PRs | *"List open pull requests in [org/repo]"* |
| One PR | *"Get PR #3 in mortenwj/pm-productivity"* |
| PR checks | *"Status checks for PR #3 in mortenwj/pm-productivity"* |
| Create issue | *"Create an issue in mortenwj/pm-productivity: title and body"* |
| Search | *"Search issues in [repo] with label bug"* |

Keep a short list of **key repos** (e.g. this one, main product repos) and ask for status by name.

---

## 4. Suggested daily flow

1. **Open Cursor** in this PM productivity folder.
2. **Generate morning report** – *"Good morning"* → read `outputs/morning/morning_report.md`.
3. **Triage “Requires attention”** – resolve, comment, or reassign in DevOps (via prompts).
4. **Scan your assigned work** – decide what to do today; update state or add comments via prompts.
5. **Check GitHub** – *"Open PRs in [repo]"* / *"My issues in [repo]"* for repos you care about.
6. **Use this repo** for notes, RFP text, and analyses; commit and push when you’re ready.

---

## 5. One place for everything

- **This repo**: All PM artifacts (reports, notes, scripts, docs).
- **Cursor**: Single window for writing, running scripts, and calling DevOps + GitHub via MCP.
- **Morning report**: Single place to see “what needs me today” from Azure DevOps.

Adjust project/team names and repo list to match your real projects; the same workflow applies.
