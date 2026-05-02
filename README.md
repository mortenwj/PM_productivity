# PM_productivity

Personal **product manager productivity** workspace: Cursor agent **skills**, shared evidence playbooks, and tooling around **Azure DevOps**, **GitHub**, and **Public 360°** (wiki, PFR, backlog quality).

**Canonical repository:** [https://github.com/mortenwj/PM_productivity](https://github.com/mortenwj/PM_productivity)  
(This is not the same repo as `mortenwj/pm-productivity` with a hyphen; use the link above when cloning or setting `origin`.)

---

## What is in this repo (tracked)

| Path | Purpose |
|------|--------|
| [`.cursor/skills/`](.cursor/skills/) | Cursor **Agent Skills** (`SKILL.md` per skill): morning report, PFR capability check, lmwtfy research, triage, ADO story/bug quality, shared evidence retrieval, and more. |
| [`.cursor/skills/shared/evidence/`](.cursor/skills/shared/evidence/) | Shared **evidence** layer: budgets, playbooks, profiles (`code-first-research`, `cost-aware-doc-first`), MediaWiki norms ([`mediawiki_extract.md`](.cursor/skills/shared/evidence/mediawiki_extract.md)). |
| [`.gitignore`](.gitignore) | Python, local secrets (`config.json`, `.env`), IDE noise, and `.cursor/skills.zip` (redundant export of the skills folder). |

Open any skill’s `SKILL.md` for trigger phrases and behaviour. The shared evidence [README](.cursor/skills/shared/evidence/README.md) indexes cross-skill retrieval docs.

---

## Using this repo in Cursor

1. Clone [mortenwj/PM_productivity](https://github.com/mortenwj/PM_productivity) and open the folder as your workspace.
2. Ensure **Agent Skills** can see this tree (skills live under `.cursor/skills/` per Cursor conventions).
3. Configure **MCP** as needed for your flows (e.g. Azure DevOps, MediaWiki, Ratatoskr) — see each skill and [`sources-and-tools.md`](.cursor/skills/shared/evidence/sources-and-tools.md) for hygiene and caps.

---

## Local-only and optional material

You may keep **scripts**, **generated reports** (e.g. `morning_report.md`), and **draft docs** in the same folder on disk; many of those paths are **gitignored or not yet committed**. Add and commit them when you want them on GitHub.

If you use a **wiki MCP** or other local servers from this workspace, keep secrets out of Git (see `.gitignore`).

---

## License

No license file is set yet; treat contents as private unless you add one.
