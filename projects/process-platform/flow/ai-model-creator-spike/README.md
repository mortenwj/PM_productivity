# AI-assisted process model creator — internal experiment spike

Offline tooling for scenario **S1** (permit-style linear process). Produces Flow-native JSON drafts for human review per `_bmad-output/specs/spec-ai-assisted-process-model-creator/`.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) (repo uses `pyproject.toml` at root — not local `pip install`)
- For **live mode**: internal OpenAI endpoint credentials

From the **repository root**:

```powershell
uv sync
copy projects/process-platform/flow/ai-model-creator-spike/.env.example projects/process-platform/flow/ai-model-creator-spike/.env
# Edit .env with OPENAI_API_KEY, OPENAI_BASE_URL, OPENAI_MODEL
```

## Run S1

**Dry-run** (no API — uses `fixtures/s1-permit.dry-run.json`):

```powershell
uv run python projects/process-platform/flow/ai-model-creator-spike/generate_draft.py --scenario s1-permit --dry-run
```

Or:

```powershell
.\toolkit\scripts\run-ai-spike.ps1 --scenario s1-permit --dry-run
```

Output: `projects/process-platform/flow/ai-model-creator-spike/runs/s1-permit.json`

**Live** (internal OpenAI):

```powershell
uv run python projects/process-platform/flow/ai-model-creator-spike/generate_draft.py --scenario s1-permit
```

## Evaluate

Score output using `_bmad-output/specs/spec-ai-assisted-process-model-creator/evaluation-criteria.md`. This spike does not auto-score.

## Layout

| Path | Purpose |
|------|---------|
| `schema/flow-process-model-draft.schema.json` | JSON IR contract |
| `prompts/system.md` | Flow-native system prompt (live mode) |
| `scenarios/s1-permit.json` | S1 input bundle |
| `fixtures/s1-permit.dry-run.json` | Reference output for offline demo |
| `runs/` | Generated drafts (gitignored) |

## Related specs

- Experiment contract: `_bmad-output/specs/spec-ai-assisted-process-model-creator/SPEC.md`
- Implementation spec: `_bmad-output/implementation-artifacts/spec-s1-json-spike.md`
