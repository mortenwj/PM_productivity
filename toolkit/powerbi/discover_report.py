#!/usr/bin/env python3
"""
Discover Power BI report metadata, dataset data sources, and model tables.

One-time auth via device code (MSAL). Writes agent-readable JSON to outputs/scratch/.

  uv run python toolkit/powerbi/discover_report.py
  uv run python toolkit/powerbi/discover_report.py --config config.json

See toolkit/powerbi/POWERBI_SETUP.md for Azure app registration steps.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx
import msal

PBI = "https://api.powerbi.com/v1.0/myorg"
CACHE_PATH = Path.home() / ".msal_token_cache_powerbi.json"
SCOPES = [
    "https://analysis.windows.net/powerbi/api/Dataset.Read.All",
    "https://analysis.windows.net/powerbi/api/Report.Read.All",
]

# Microsoft public client — no custom app registration in Azure Portal required.
# User signs in with device code; works when tenant allows user consent for Power BI.
AZURE_CLI_CLIENT_ID = "04b07795-8ddb-461a-bbee-02f9e1bf7b46"

_REPO = Path(__file__).resolve().parents[2]
_DEFAULT_OUT = _REPO / "outputs" / "scratch" / "powerbi_discovery.json"


def _resolve_client_id(raw: str | None) -> str:
    if not raw or raw.strip().lower() in ("azure-cli", "default", "public"):
        return AZURE_CLI_CLIENT_ID
    return raw.strip()


def _load_config(path: Path | None) -> dict[str, Any]:
    cfg: dict[str, Any] = {}
    if path and path.is_file():
        cfg = json.loads(path.read_text(encoding="utf-8"))
    pbi = cfg.get("powerbi") or {}
    client_raw = os.environ.get("POWERBI_CLIENT_ID") or pbi.get("client_id")
    return {
        "tenant_id": os.environ.get("POWERBI_TENANT_ID") or pbi.get("tenant_id"),
        "client_id": _resolve_client_id(client_raw),
        "workspace_id": os.environ.get("POWERBI_WORKSPACE_ID") or pbi.get("workspace_id"),
        "report_id": os.environ.get("POWERBI_REPORT_ID") or pbi.get("report_id"),
    }


def _require(cfg: dict[str, Any], key: str) -> str:
    val = cfg.get(key)
    if not val and key != "client_id":
        raise SystemExit(
            f"Missing {key}. Set in config.json → powerbi, or env POWERBI_{key.upper()}.\n"
            "See toolkit/powerbi/POWERBI_SETUP.md"
        )
    if key == "client_id":
        return cfg.get("client_id") or AZURE_CLI_CLIENT_ID
    return str(val)


def _token_cache() -> msal.SerializableTokenCache:
    cache = msal.SerializableTokenCache()
    if CACHE_PATH.is_file():
        cache.deserialize(CACHE_PATH.read_text(encoding="utf-8"))
    return cache


def _save_cache(cache: msal.SerializableTokenCache) -> None:
    if cache.has_state_changed:
        CACHE_PATH.write_text(cache.serialize(), encoding="utf-8")


def get_access_token(tenant_id: str, client_id: str) -> str:
    cache = _token_cache()
    app = msal.PublicClientApplication(
        client_id=client_id,
        authority=f"https://login.microsoftonline.com/{tenant_id}",
        token_cache=cache,
    )
    accounts = app.get_accounts()
    result = None
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
    if not result:
        flow = app.initiate_device_flow(scopes=SCOPES)
        if "user_code" not in flow:
            raise SystemExit(f"Device flow failed: {flow}")
        print(flow["message"], file=sys.stderr)
        result = app.acquire_token_by_device_flow(flow)
    _save_cache(cache)
    if "access_token" not in result:
        raise SystemExit(result.get("error_description") or json.dumps(result))
    return result["access_token"]


def pbi_get(client: httpx.Client, path: str) -> dict[str, Any]:
    url = f"{PBI}{path}" if path.startswith("/") else path
    r = client.get(url, follow_redirects=True)
    if r.status_code == 429:
        time.sleep(int(r.headers.get("Retry-After", "5")))
        r = client.get(url, follow_redirects=True)
    if r.status_code == 404:
        return {"error": "not_found", "status": 404, "path": path}
    r.raise_for_status()
    return r.json()


def pbi_post(client: httpx.Client, path: str, body: dict[str, Any]) -> dict[str, Any]:
    url = f"{PBI}{path}"
    r = client.post(url, json=body, follow_redirects=True)
    if r.status_code == 429:
        time.sleep(int(r.headers.get("Retry-After", "5")))
        r = client.post(url, json=body, follow_redirects=True)
    if r.status_code >= 400:
        try:
            err = r.json()
        except Exception:
            err = {"message": r.text[:500]}
        return {"error": err, "status": r.status_code, "path": path}
    return r.json()


def execute_dax(client: httpx.Client, workspace_id: str, dataset_id: str, query: str) -> dict[str, Any]:
    return pbi_post(
        client,
        f"/groups/{workspace_id}/datasets/{dataset_id}/executeQueries",
        {"queries": [{"query": query}], "serializerSettings": {"includeNulls": True}},
    )


def discover(client: httpx.Client, workspace_id: str, report_id: str) -> dict[str, Any]:
    out: dict[str, Any] = {
        "discovered_at": datetime.now(timezone.utc).isoformat(),
        "workspace_id": workspace_id,
        "report_id": report_id,
        "report": None,
        "dataset": None,
        "datasources": None,
        "report_pages": None,
        "tables_info": None,
        "columns_sample": None,
        "errors": [],
    }

    report = pbi_get(client, f"/groups/{workspace_id}/reports/{report_id}")
    if report.get("error"):
        out["errors"].append({"step": "report", **report})
        return out
    out["report"] = {
        "id": report.get("id"),
        "name": report.get("name"),
        "datasetId": report.get("datasetId"),
        "webUrl": report.get("webUrl"),
        "embedUrl": report.get("embedUrl"),
    }

    dataset_id = report.get("datasetId")
    if not dataset_id:
        out["errors"].append({"step": "dataset", "message": "Report has no datasetId"})
        return out

    ds = pbi_get(client, f"/groups/{workspace_id}/datasets/{dataset_id}")
    if not ds.get("error"):
        out["dataset"] = {
            "id": ds.get("id"),
            "name": ds.get("name"),
            "configuredBy": ds.get("configuredBy"),
            "isRefreshable": ds.get("isRefreshable"),
            "isEffectiveIdentityRequired": ds.get("isEffectiveIdentityRequired"),
            "targetStorageMode": ds.get("targetStorageMode"),
        }
    else:
        out["errors"].append({"step": "dataset", **ds})

    src = pbi_get(client, f"/groups/{workspace_id}/datasets/{dataset_id}/datasources")
    if not src.get("error"):
        out["datasources"] = [
            {
                "datasourceType": d.get("datasourceType"),
                "connectionDetails": d.get("connectionDetails"),
                "gatewayId": d.get("gatewayId"),
                "datasourceId": d.get("datasourceId"),
            }
            for d in (src.get("value") or [])
        ]
    else:
        out["errors"].append({"step": "datasources", **src})

    pages = pbi_get(client, f"/groups/{workspace_id}/reports/{report_id}/pages")
    if not pages.get("error"):
        out["report_pages"] = [
            {"name": p.get("name"), "displayName": p.get("displayName"), "order": p.get("order")}
            for p in (pages.get("value") or [])
        ]
    else:
        out["errors"].append({"step": "report_pages", **pages})

    tables_result = execute_dax(client, workspace_id, dataset_id, "EVALUATE INFO.TABLES()")
    if tables_result.get("error"):
        out["errors"].append({"step": "INFO.TABLES", **tables_result})
    else:
        out["tables_info"] = tables_result

    # Sample column metadata for first few tables (if INFO.COLUMNS works)
    columns_result = execute_dax(
        client, workspace_id, dataset_id, "EVALUATE TOPN(200, INFO.COLUMNS())"
    )
    if columns_result.get("error"):
        out["errors"].append({"step": "INFO.COLUMNS", **columns_result})
    else:
        out["columns_sample"] = columns_result

    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Discover Power BI report and dataset metadata")
    parser.add_argument("--config", type=Path, default=_REPO / "config.json")
    parser.add_argument("--output", type=Path, default=_DEFAULT_OUT)
    args = parser.parse_args()

    cfg = _load_config(args.config if args.config.is_file() else None)
    tenant_id = _require(cfg, "tenant_id")
    client_id = _require(cfg, "client_id")
    workspace_id = _require(cfg, "workspace_id")
    report_id = _require(cfg, "report_id")

    token = get_access_token(tenant_id, client_id)
    headers = {"Authorization": f"Bearer {token}"}

    with httpx.Client(headers=headers, timeout=120.0) as client:
        result = discover(client, workspace_id, report_id)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, default=str), encoding="utf-8")

    ds_count = len(result.get("datasources") or [])
    page_count = len(result.get("report_pages") or [])
    err_count = len(result.get("errors") or [])
    print(f"Wrote {args.output}")
    print(f"  Report: {result.get('report', {}).get('name')}")
    print(f"  Dataset: {result.get('dataset', {}).get('name')}")
    print(f"  Data sources: {ds_count} | Pages: {page_count} | Errors: {err_count}")
    if err_count:
        print("  Check errors[] in JSON — often executeQueries tenant setting or Build permission.", file=sys.stderr)


if __name__ == "__main__":
    main()
