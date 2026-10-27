# PM_productivity — Claude Code / Desktop

Private PM workspace: **skills** (`.cursor/skills/`), **toolkit** scripts, **docs**, and **projects** (Process Platform, search, process-builder).

## Bootstrap

```powershell
winget install astral-sh.uv --accept-package-agreements --scope user  # once
.\toolkit\scripts\bootstrap-python.ps1   # or: uv sync
```

Run Python **only** via:

```powershell
uv run python <script> [args...]
```

See [DAILY_WORKFLOW.md](DAILY_WORKFLOW.md) and [PROJECT_SETUP.md](PROJECT_SETUP.md).

## Skills

- **In repo:** `.cursor/skills/` (morning report, module health, tender, mediawiki release notes, ADO quality, …).
- **Install for Claude Code:** copy skill folders to `%USERPROFILE%\.claude\skills\`, or read `SKILL.md` from this repo when invoked.
- **Team shared (lmwtfy, PFR gates, feature-scoping):** [pm-ai-workbench](https://github.com/te-industry-public360/pm-ai-workbench) → `skills/claude-code/`.

## MCP (configure in Claude, same as Cursor)

Typical servers: **Azure DevOps**, **MediaWiki**, **Ratatoskr** (360 Online help), **GitHub**, **ProductPlan**. Tool names and caps: `.cursor/skills/shared/evidence/sources-and-tools.md`.

Default ADO project/team in prompts: **360**, **Core-Process-platform** (override when needed).

## Paths

| Output | Path |
|--------|------|
| Morning report | `outputs/morning/morning_report.md` |
| Module health | `outputs/portfolio/module_health_YYYY-MM-DD.md` |
| lmwtfy answers | `docs/lmwtfy-answers/` |
| Tender library index | `docs/tender-reference/INDEX.md` (source/extracted stay local) |

## Not in git

- Secrets: `config.json`, `.env`
- Generated **outputs/** (except README / `.gitkeep`)
- Tender **source/** and **extracted/** under `docs/tender-reference/`
- BMad: `_bmad/`, `.agents/` (reinstall locally)

## Repo layout

Documented in [README.md](README.md).
