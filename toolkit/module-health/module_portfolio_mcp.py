#!/usr/bin/env python3
"""
Module Portfolio MCP server — revenue, taxonomy, and health scoring tools.

Register in Cursor MCP settings (stdio):

  {
    "mcpServers": {
      "module-portfolio": {
        "command": "uv",
        "args": ["run", "python", "toolkit/module-health/module_portfolio_mcp.py"],
        "cwd": "<repo-root>"
      }
    }
  }
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

_PKG = Path(__file__).resolve().parent
if str(_PKG) not in sys.path:
    sys.path.insert(0, str(_PKG))

from ado_aggregator import aggregate_bugs, aggregate_pfrs, merge_module_stats  # noqa: E402
from report import render_scorecard  # noqa: E402
from revenue_loader import build_module_revenue, load_scoring_config, load_taxonomy  # noqa: E402
from scoring import score_modules  # noqa: E402

server = Server("module-portfolio")


def _repo_root() -> Path:
    return _PKG.parent.parent


def _default_excel() -> Path:
    return _repo_root() / "External Revenue, EUR.xlsx"


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="get_module_taxonomy",
            description="Return module-to-team mapping and ImpactedModule aliases for Public 360 portfolio scoring.",
            inputSchema={"type": "object", "properties": {}, "additionalProperties": False},
        ),
        Tool(
            name="get_scoring_config",
            description="Return health score weights, band thresholds, and insight rules.",
            inputSchema={"type": "object", "properties": {}, "additionalProperties": False},
        ),
        Tool(
            name="get_revenue_by_module",
            description="Load YTD revenue aggregated by ImpactedModule from External Revenue Excel.",
            inputSchema={
                "type": "object",
                "properties": {
                    "excel_path": {
                        "type": "string",
                        "description": "Optional path to revenue Excel. Defaults to repo External Revenue, EUR.xlsx.",
                    }
                },
                "additionalProperties": False,
            },
        ),
        Tool(
            name="build_module_health_scorecard",
            description=(
                "Merge ADO bug/PFR work item JSON with revenue data; return markdown scorecard and scored rows."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "bugs_json": {
                        "type": "string",
                        "description": "JSON string: list of Bug work items (fields include Custom.ImpactedModule).",
                    },
                    "pfrs_json": {
                        "type": "string",
                        "description": "JSON string: list of open PFR work items.",
                    },
                    "team_filter": {"type": "string", "description": "Optional product team name filter."},
                    "module_filter": {"type": "string", "description": "Optional single module filter."},
                    "include_revenue": {
                        "type": "boolean",
                        "description": "Include revenue in scoring (default false). Requires excel_path.",
                    },
                    "excel_path": {"type": "string", "description": "Optional revenue Excel path (only if include_revenue)."},
                },
                "required": ["bugs_json", "pfrs_json"],
                "additionalProperties": False,
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    if name == "get_module_taxonomy":
        return [TextContent(type="text", text=json.dumps(load_taxonomy(), indent=2))]

    if name == "get_scoring_config":
        return [TextContent(type="text", text=json.dumps(load_scoring_config(), indent=2))]

    if name == "get_revenue_by_module":
        excel = Path(arguments.get("excel_path") or _default_excel())
        if not excel.exists():
            return [TextContent(type="text", text=json.dumps({"error": f"Excel not found: {excel}"}))]
        data = build_module_revenue(excel)
        return [TextContent(type="text", text=json.dumps(data, indent=2))]

    if name == "build_module_health_scorecard":
        bugs = json.loads(arguments["bugs_json"])
        pfrs = json.loads(arguments["pfrs_json"])
        team_filter = arguments.get("team_filter")
        module_filter = arguments.get("module_filter")
        include_revenue = bool(arguments.get("include_revenue", False))
        revenue_by_module: dict = {}
        unmapped = 0
        revenue_source = ""

        if include_revenue:
            excel = Path(arguments.get("excel_path") or _default_excel())
            if excel.exists():
                revenue_data = build_module_revenue(excel)
                revenue_by_module = revenue_data["by_module"]
                unmapped = len(revenue_data.get("unmapped_products", []))
                revenue_source = str(excel)
            include_revenue = bool(revenue_by_module)

        rows = merge_module_stats(
            revenue_by_module,
            aggregate_bugs(bugs),
            aggregate_pfrs(pfrs),
            team_filter=team_filter,
            module_filter=module_filter,
        )
        scored = score_modules(rows, include_revenue=include_revenue)
        markdown = render_scorecard(
            scored,
            team_filter=team_filter,
            module_filter=module_filter,
            include_revenue=include_revenue,
            revenue_source=revenue_source,
            unmapped_count=unmapped,
            ado_notes=[] if include_revenue else ["Revenue excluded — ADO-only scoring."],
        )
        payload = {"markdown": markdown, "modules": scored, "module_count": len(scored)}
        return [TextContent(type="text", text=json.dumps(payload, indent=2))]

    return [TextContent(type="text", text=json.dumps({"error": f"Unknown tool: {name}"}))]


async def main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
