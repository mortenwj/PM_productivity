"""
Export Microsoft Teams channel messages (and replies) via Microsoft Graph for analysis in Cursor.

Setup (one-time):
  1. Azure Portal → App registrations → New registration (single-tenant or multi).
  2. Authentication → enable "Allow public client flows" (for device code).
  3. API permissions → Microsoft Graph → Delegated:
       ChannelMessage.Read.All, User.Read
     → Grant admin consent if your tenant requires it for ChannelMessage.Read.All.
  4. Copy Application (client) ID and Directory (tenant) ID.

Usage:
  set TEAMS_TENANT_ID=...
  set TEAMS_CLIENT_ID=...
  python fetch_teams_channel_messages.py --list-teams
  python fetch_teams_channel_messages.py --list-channels TEAM_ID
  python fetch_teams_channel_messages.py --team-id TEAM_ID --channel-id CHANNEL_ID --out teams_export.json

First run opens a browser/device-code sign-in; token is cached in ~/.msal_token_cache_teams.json
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import httpx
import msal

GRAPH = "https://graph.microsoft.com/v1.0"
CACHE_PATH = Path.home() / ".msal_token_cache_teams.json"
SCOPES = ["https://graph.microsoft.com/ChannelMessage.Read.All", "https://graph.microsoft.com/User.Read"]


class _HTMLToText(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._chunks: list[str] = []

    def handle_data(self, data: str) -> None:
        self._chunks.append(data)

    def get_text(self) -> str:
        raw = "".join(self._chunks)
        raw = html.unescape(raw)
        raw = re.sub(r"\s+", " ", raw).strip()
        return raw


def body_to_text(body: dict[str, Any] | None) -> str:
    if not body:
        return ""
    content = body.get("content") or ""
    ctype = (body.get("contentType") or "html").lower()
    if ctype == "text":
        return content.strip()
    p = _HTMLToText()
    try:
        p.feed(content)
        p.close()
        return p.get_text()
    except Exception:
        return re.sub(r"<[^>]+>", " ", content)


def display_name(from_obj: dict[str, Any] | None) -> str:
    if not from_obj:
        return ""
    user = from_obj.get("user") or {}
    if user.get("displayName"):
        return user["displayName"]
    if user.get("id"):
        return user["id"]
    app = from_obj.get("application") or {}
    if app.get("displayName"):
        return app["displayName"]
    return ""


def load_cache() -> msal.SerializableTokenCache:
    cache = msal.SerializableTokenCache()
    if CACHE_PATH.is_file():
        cache.deserialize(CACHE_PATH.read_text(encoding="utf-8"))
    return cache


def save_cache(cache: msal.SerializableTokenCache) -> None:
    if cache.has_state_changed:
        CACHE_PATH.write_text(cache.serialize(), encoding="utf-8")


def get_token(tenant_id: str, client_id: str) -> str:
    cache = load_cache()
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
    save_cache(cache)
    if "access_token" not in result:
        raise SystemExit(result.get("error_description") or json.dumps(result))
    return result["access_token"]


def graph_get(client: httpx.Client, url: str) -> dict[str, Any]:
    r = client.get(url, follow_redirects=True)
    if r.status_code == 429:
        retry = int(r.headers.get("Retry-After", "5"))
        time.sleep(retry)
        r = client.get(url, follow_redirects=True)
    r.raise_for_status()
    return r.json()


def graph_get_all(client: httpx.Client, first_url: str, max_items: int | None) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    url: str | None = first_url
    while url:
        data = graph_get(client, url)
        batch = data.get("value") or []
        items.extend(batch)
        if max_items is not None and len(items) >= max_items:
            return items[:max_items]
        url = data.get("@odata.nextLink")
    return items


def list_teams(client: httpx.Client) -> None:
    url = f"{GRAPH}/me/joinedTeams"
    teams = graph_get_all(client, url, None)
    for t in teams:
        print(f"{t.get('id')}\t{t.get('displayName')}")


def list_channels(client: httpx.Client, team_id: str) -> None:
    url = f"{GRAPH}/teams/{team_id}/channels"
    chans = graph_get_all(client, url, None)
    for c in chans:
        print(f"{c.get('id')}\t{c.get('displayName')}\tmembershipType={c.get('membershipType')}")


def normalize_message(m: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": m.get("id"),
        "createdDateTime": m.get("createdDateTime"),
        "lastModifiedDateTime": m.get("lastModifiedDateTime"),
        "from_display": display_name(m.get("from")),
        "body_text": body_to_text(m.get("body")),
        "replyCount": m.get("replyCount", 0),
        "importance": m.get("importance"),
        "messageType": m.get("messageType"),
    }


def fetch_replies(
    client: httpx.Client, team_id: str, channel_id: str, message_id: str
) -> list[dict[str, Any]]:
    url = f"{GRAPH}/teams/{team_id}/channels/{channel_id}/messages/{message_id}/replies"
    raw = graph_get_all(client, url, None)
    return [normalize_message(r) for r in raw]


def export_channel(
    client: httpx.Client,
    team_id: str,
    channel_id: str,
    max_messages: int | None,
    include_replies: bool,
) -> dict[str, Any]:
    url = f"{GRAPH}/teams/{team_id}/channels/{channel_id}/messages?$top=50"
    raw = graph_get_all(client, url, max_messages)
    out_messages: list[dict[str, Any]] = []
    for m in raw:
        base = normalize_message(m)
        if include_replies and (m.get("replyCount") or 0) > 0:
            mid = m.get("id")
            if mid:
                try:
                    base["replies"] = fetch_replies(client, team_id, channel_id, mid)
                except httpx.HTTPStatusError as e:
                    base["replies_error"] = str(e)
        out_messages.append(base)
    return {
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "team_id": team_id,
        "channel_id": channel_id,
        "message_count": len(out_messages),
        "messages": out_messages,
    }


def main() -> None:
    p = argparse.ArgumentParser(description="Export Teams channel messages via Microsoft Graph.")
    p.add_argument("--list-teams", action="store_true", help="Print teams the signed-in user has joined.")
    p.add_argument("--list-channels", metavar="TEAM_ID", help="Print channels for a team.")
    p.add_argument("--team-id", help="Team (group) ID.")
    p.add_argument("--channel-id", help="Channel ID.")
    p.add_argument("--out", type=Path, default=Path("teams_channel_export.json"), help="Output JSON path.")
    p.add_argument("--max-messages", type=int, default=None, help="Stop after N top-level messages.")
    p.add_argument("--no-replies", action="store_true", help="Skip fetching reply threads.")
    args = p.parse_args()

    tenant = os.environ.get("TEAMS_TENANT_ID")
    client_id = os.environ.get("TEAMS_CLIENT_ID")
    if not tenant or not client_id:
        print("Set TEAMS_TENANT_ID and TEAMS_CLIENT_ID.", file=sys.stderr)
        raise SystemExit(1)

    token = get_token(tenant, client_id)
    headers = {"Authorization": f"Bearer {token}"}
    with httpx.Client(headers=headers, timeout=60.0) as client:
        if args.list_teams:
            list_teams(client)
            return
        if args.list_channels:
            list_channels(client, args.list_channels)
            return
        if not args.team_id or not args.channel_id:
            print("Provide --team-id and --channel-id, or use --list-teams / --list-channels.", file=sys.stderr)
            raise SystemExit(1)
        payload = export_channel(
            client,
            args.team_id,
            args.channel_id,
            args.max_messages,
            include_replies=not args.no_replies,
        )
    args.out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.out} ({payload['message_count']} messages).", file=sys.stderr)


if __name__ == "__main__":
    main()
