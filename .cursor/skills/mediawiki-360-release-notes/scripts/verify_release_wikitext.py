"""Quick checks on release page wikitext (stdin or file path). No network."""
from __future__ import annotations

import re
import sys
from pathlib import Path

FLOW_HEADING = "== 360° Flow - Now Generally Available =="
NEWS_HEADING = "=News and improvements in existing module(s)="
ADO_IN_PARENS = re.compile(r"\(\[#\d+\]")


def main() -> int:
    if len(sys.argv) > 1:
        text = Path(sys.argv[1]).read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()

    errors: list[str] = []
    warnings: list[str] = []

    flow_count = text.count(FLOW_HEADING)
    if flow_count != 1:
        errors.append(f"Expected 1 Flow GA heading, found {flow_count}")

    if NEWS_HEADING not in text:
        warnings.append("News and improvements section heading not found")

    # Customer-facing bands: New module through start of core product (rough)
    start = text.find("=New module=")
    end = text.find("=New features and improvements in the core product=")
    if start != -1 and end != -1:
        band = text[start:end]
        ado_hits = ADO_IN_PARENS.findall(band)
        if ado_hits:
            errors.append(
                f"ADO id markers in New module/News band: {len(ado_hits)} "
                "(e.g. ([#123456])); remove for consistency"
            )

    if re.search(r"\bNVE PAF\b|\bNVE MLP\b", text):
        warnings.append("Text contains NVE PAF/MLP — confirm intentional")

    if "=Technical notes=\nTBA" in text:
        warnings.append("Technical notes still TBA")

    for w in warnings:
        print("WARN:", w)
    for e in errors:
        print("ERROR:", e)

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
