#!/usr/bin/env python3
"""Generate a Flow process model draft (JSON) for experiment scenarios."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCENARIOS_DIR = ROOT / "scenarios"
FIXTURES_DIR = ROOT / "fixtures"
RUNS_DIR = ROOT / "runs"
PROMPTS_DIR = ROOT / "prompts"


def load_scenario(scenario_id: str) -> dict:
    path = SCENARIOS_DIR / f"{scenario_id}.json"
    if not path.exists():
        available = sorted(p.stem for p in SCENARIOS_DIR.glob("*.json"))
        raise SystemExit(
            f"Unknown scenario '{scenario_id}'. Available: {', '.join(available) or '(none)'}"
        )
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_system_prompt() -> str:
    return (PROMPTS_DIR / "system.md").read_text(encoding="utf-8")


def validate_draft(draft: dict) -> list[str]:
    """Lightweight structural validation (no jsonschema dependency)."""
    errors: list[str] = []

    if not isinstance(draft, dict):
        return ["Root must be a JSON object"]

    for key in ("processModel", "metadata"):
        if key not in draft:
            errors.append(f"Missing required key: {key}")

    pm = draft.get("processModel")
    if not isinstance(pm, dict):
        errors.append("processModel must be an object")
        return errors

    stages = pm.get("stages")
    if not isinstance(stages, list) or not stages:
        errors.append("processModel.stages must be a non-empty array")
        return errors

    orders = []
    for i, stage in enumerate(stages):
        prefix = f"stages[{i}]"
        if not isinstance(stage, dict):
            errors.append(f"{prefix} must be an object")
            continue
        for req in ("id", "name", "order", "activities"):
            if req not in stage:
                errors.append(f"{prefix} missing '{req}'")
        activities = stage.get("activities")
        if not isinstance(activities, list) or not activities:
            errors.append(f"{prefix}.activities must be a non-empty array")
        order = stage.get("order")
        if isinstance(order, int):
            orders.append(order)

    if orders and orders != sorted(orders):
        errors.append("Stage order values must be ascending")

    meta = draft.get("metadata")
    if isinstance(meta, dict):
        for req in ("scenarioId", "sourcePrompt"):
            if req not in meta:
                errors.append(f"metadata missing '{req}'")

    return errors


def run_dry_run(scenario: dict) -> dict:
    fixture_name = f"{scenario['id']}.dry-run.json"
    fixture_path = FIXTURES_DIR / fixture_name
    if not fixture_path.exists():
        raise SystemExit(f"Dry-run fixture not found: {fixture_path}")

    with fixture_path.open(encoding="utf-8") as f:
        draft = json.load(f)

    draft.setdefault("metadata", {})
    draft["metadata"]["scenarioId"] = scenario.get("scenarioId", scenario["id"])
    draft["metadata"]["sourcePrompt"] = scenario.get("prompt", "")
    draft["metadata"]["generatedAt"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    draft["metadata"]["mode"] = "dry-run"
    return draft


def run_live(scenario: dict, system_prompt: str) -> dict:
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL")
    model = os.environ.get("OPENAI_MODEL", "gpt-4o")

    if not api_key:
        raise SystemExit(
            "OPENAI_API_KEY is not set. Use --dry-run or configure .env (see README.md)."
        )

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise SystemExit(
            "openai package required for live mode. From repo root run: uv sync"
        ) from exc

    client_kwargs: dict = {"api_key": api_key}
    if base_url:
        client_kwargs["base_url"] = base_url

    client = OpenAI(**client_kwargs)

    user_message = (
        f"Scenario ID: {scenario.get('scenarioId', scenario['id'])}\n\n"
        f"Process intent:\n{scenario['prompt']}\n\n"
        f"Minimum structure checklist:\n"
        + "\n".join(f"- {item}" for item in scenario.get("minimumStructure", []))
    )

    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content
    if not content:
        raise SystemExit("OpenAI returned empty content")

    try:
        draft = json.loads(content)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"OpenAI response is not valid JSON: {exc}") from exc

    draft.setdefault("metadata", {})
    draft["metadata"].setdefault("scenarioId", scenario.get("scenarioId", scenario["id"]))
    draft["metadata"].setdefault("sourcePrompt", scenario.get("prompt", ""))
    draft["metadata"]["generatedAt"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    draft["metadata"]["mode"] = "live"
    return draft


def write_output(draft: dict, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(draft, f, indent=2, ensure_ascii=False)
        f.write("\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Flow process model draft JSON (AI-assisted process model creator spike)."
    )
    parser.add_argument(
        "--scenario",
        required=True,
        help="Scenario id matching scenarios/<id>.json (e.g. s1-permit)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output JSON path (default: runs/<scenario-id>.json)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Use fixture output instead of calling OpenAI",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    scenario = load_scenario(args.scenario)
    output_path = args.output or (RUNS_DIR / f"{args.scenario}.json")

    use_dry_run = args.dry_run or not os.environ.get("OPENAI_API_KEY")
    if use_dry_run:
        if not args.dry_run and not os.environ.get("OPENAI_API_KEY"):
            print("OPENAI_API_KEY not set — using dry-run fixture.", file=sys.stderr)
        draft = run_dry_run(scenario)
    else:
        draft = run_live(scenario, load_system_prompt())

    errors = validate_draft(draft)
    if errors:
        print("Draft failed validation:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    write_output(draft, output_path)
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
