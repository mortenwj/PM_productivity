# Install — tender-response bundle

## Contents

| Path in zip | Install target |
|-------------|----------------|
| `.cursor/skills/tender-response/` | `%USERPROFILE%\.cursor\skills\tender-response\` **or** `<workspace>\.cursor\skills\tender-response\` |
| `.cursor/skills/shared/` | `%USERPROFILE%\.cursor\skills\shared\` **or** `<workspace>\.cursor\skills\shared\` |
| `docs/tender-reference/extracted/` | `<workspace>\docs\tender-reference\extracted\` |
| `docs/tender-reference/INDEX.md` | `<workspace>\docs\tender-reference\INDEX.md` |
| `docs/tender-reference/README.md` | `<workspace>\docs\tender-reference\README.md` |

**Recommended workspace:** clone or open **PM_productivity**, merge these paths into that repo root so skill paths match (`docs/tender-reference/...`).

Personal skills alone work for the skill text; **prior-art grep (Stage 0a)** requires `docs/tender-reference/extracted/` inside the **same workspace** you use for tender chat.

## MCP (optional but expected for evidence)

Configure Cursor MCP as you would for PM work:

- **user-mediawiki** — process, security, releases
- **user-ratatoskr** — help.360online.com product/admin
- **user-azure-devops** — shipped vs planned

See `.cursor/skills/shared/evidence/sources-and-tools.md` after install.

## Use in chat

Mention **tender-response**, or tender / anbud / kravbesvarelse / compliance matrix. Read **`SHARING-POLICY-SSA-L-AND-PRIOR-BIDS.md`** before using extracts.

## Refresh extracts (maintainers only)

Originals live in `docs/tender-reference/source/` (not shipped in this zip). Regenerate extracts on a machine that has `source/`:

```powershell
uv run python toolkit/scripts/extract_tender_reference.py
```
