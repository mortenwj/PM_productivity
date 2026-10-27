# PR: Claude portability (`chore/claude-portability` → `main`)

## Summary

- Add **toolkit/**, **pyproject.toml** / **uv.lock**, workflow docs, and **CLAUDE.md** so the repo can be cloned and used from Claude Code with `uv run python …`.
- Add **docs/** (lmwtfy answers, product drafts, tender library including **source/** and **extracted/**, strategy markdown).
- Add **projects/process-platform/**, **projects/search-experience/**, process-builder POC learnings, **canvases/**, **assets/**, and **.cursor/rules/python-environment.mdc**.
- Extend **.gitignore** for generated **outputs/**, root xlsx/zip, Office temps, RFP scratch, canvas node_modules, workunit build **obj/**, and large reference binaries.

## Still local-only (by design)

- `config.json`, `.env`, BMad (`.agents/`, `_bmad/`)
- Full **outputs/** tree (except README / `.gitkeep`)
- Root revenue spreadsheets, `PM_productivity.zip`
- Install team skills from **pm-ai-workbench** (`skills/claude-code/`) and copy `.cursor/skills/` to `~/.claude/skills/` as needed

## Test plan

- [ ] Fresh clone on Windows; `uv sync` from repo root succeeds
- [ ] `uv run python toolkit/morning-report/generate_morning_report.py --help` (or dry-run per spec)
- [ ] Read **CLAUDE.md** and **DAILY_WORKFLOW.md** — paths match repo layout
- [ ] Confirm tender **source/** and **extracted/** are present after clone (private repo only)
- [ ] Configure MCP in Claude; run a read-only ADO or Ratatoskr query

## After merge

```powershell
git checkout main
git pull origin main
uv sync
```

Copy skills to `%USERPROFILE%\.claude\skills\` or rely on in-repo `SKILL.md` paths.
