# Ratatoskr (360 Online help) — preflight and fallbacks

**Purpose:** One canonical description of **network/DNS** behavior and **preflight** steps for `user-ratatoskr`, shared by **lmwtfy** and **PFR** runs.

---

## Network / DNS note

The Ratatoskr server can appear **online** in Cursor while calls that **fetch** `https://help.360online.com` still fail (for example `lookup help.360online.com: no such host`). That happens when the **process running the MCP** does not use the same DNS path as your PC (cloud agent, no VPN, no corporate DNS). Fix is **environmental**: run the agent **locally** on a machine that resolves `help.360online.com` (your `nslookup` via `*.tieto.com` is a good sign), connect **VPN** if required, or ask the user to re-run the research in that setup.

---

## Preflight (every run before relying on help text)

1. Call **`list_sections`** (cheap; may succeed even when full fetch is broken depending on server build).  
2. Call **`search_topics`** with a small `query` (and optional `section_id` such as `admin-en`). If the error mentions **DNS**, **no such host**, **timeout**, or **connection refused** to `help.360online.com`, stop retrying Ratatoskr for this run.

---

## If Ratatoskr cannot fetch topics

- State clearly in the run notes: **360 Online help not reachable from this agent (network/DNS).**  
- **Fallback A:** Ask the user to **repeat in Cursor on a local session** (same repo) with **VPN/corporate network** so the Ratatoskr process shares resolvable DNS for `help.360online.com`.  
- **Fallback B:** Use **`user-mediawiki`**; product pages often link `https://help.360online.com/...` PDFs or paths. Try **WebFetch** on those URLs only if your environment can reach them (public edge may work for some assets; corporate-only hosts will not).  
- **Fallback C:** Ask the user to **paste** the relevant help excerpt or the output of `read_topic` from their machine.

**lmwtfy:** record fallbacks in the evidence ledger; do not block the whole answer on help center alone if other sources can proceed.

---

**File:** `shared/evidence/ratatoskr-preflight.md`
