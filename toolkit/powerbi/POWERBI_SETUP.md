# Power BI access for PM_productivity

Enable the Cursor agent to read your Power BI **report metadata**, **dataset data sources**, **model tables**, and **sample revenue rows** — without scraping the Power BI web UI.

## How it works

Power BI does not expose report data to anonymous URLs. Access is via the **Power BI REST API** using **your** Microsoft login (delegated) or a **service principal** (team automation).

```
You (once)                    Agent (ongoing)
─────────                     ───────────────
Azure app registration   →    reads config.json
Device-code sign-in      →    runs discover_report.py
Token cached locally     →    reads outputs/scratch/powerbi_discovery.json
                              builds module-health scorecard from live DAX
```

After one-time setup, say in Cursor: *"Run Power BI discovery"* or *"Module health with live Power BI revenue"*.

---

## Step 1 — Authentication (pick one path)

### Path A — No Azure Portal access (try this first)

Many tenants allow sign-in using **Microsoft’s public Azure CLI app** — you do **not** need to create an app registration.

1. Copy `config.example.json` → `config.json`
2. Leave `powerbi.client_id` as **`azure-cli`** (or omit it — that is the default)
3. Run discovery (Step 4 below)

If device login works and discovery succeeds, you are done with setup.

If login fails with *“Need admin approval”* or *“invalid client”*, use Path B or C.

### Path B — Ask IT / Azure admin (~5 min for them)

Send this request to your **Azure AD admin** or **Power BI workspace owner**:

> Please create an app registration (or reuse an existing internal tooling app) with:
> - **Allow public client flows**: Yes  
> - **Delegated permissions** (Power BI Service): `Dataset.Read.All`, `Report.Read.All`  
> - **Admin consent** granted  
>  
> Add my account (`you@tieto.com`) as a user of the app if required.  
> Return: **Tenant ID**, **Client ID**  
>  
> Purpose: read-only API access to Power BI report `2693f2f6-4104-48c6-b741-95959d135323` in workspace `813e80d7-5ba4-4629-a456-30255b5085c4` for PM portfolio reporting (Module Health Scorecard).

Put the returned Client ID in `config.json` → `powerbi.client_id`.

### Path C — No API access at all (manual export)

If IT cannot help, you can still feed the scorecard without any Azure setup:

1. Open the Power BI report in the browser  
2. On the **revenue by product/module** visual → **⋯** → **Export data** → **Summarized** or **Underlying data** (Excel)  
3. Save to `outputs/scratch/powerbi_revenue_export.xlsx`  
4. In Cursor: *“Module health scorecard using powerbi_revenue_export.xlsx”*

Refresh the export when you need up-to-date numbers (weekly/monthly). The agent maps columns once you export a sample.

---

## Step 1 (detail) — Azure app registration (Path B only)

Skip this section if Path A or C works for you.

Use an existing app or create a new one in [Azure Portal → App registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade).

### Authentication

1. **Authentication** → **Advanced settings**
2. Enable **Allow public client flows** → Yes  
   (Required for device-code login from a script, same as Teams export.)

### API permissions (Delegated)

Add **Power BI Service** (not Microsoft Graph):

| Permission | Why |
|------------|-----|
| `Dataset.Read.All` | Read dataset + execute DAX queries |
| `Report.Read.All` | Read report metadata and pages |

Then **Grant admin consent** if your tenant requires it (some tenants allow user consent for Dataset.Read).

### Copy these values

| Setting | Your value (from report URL) |
|---------|------------------------------|
| **Tenant ID** | `cbede638-a3d9-459f-8f4e-24ced73b4e5e` |
| **Client ID** | From app registration → Application (client) ID |
| **Workspace ID** | `813e80d7-5ba4-4629-a456-30255b5085c4` |
| **Report ID** | `2693f2f6-4104-48c6-b741-95959d135323` |

---

## Step 2 — Tenant admin settings (may already be on)

A Power BI **admin** must enable (Admin portal → Tenant settings):

| Setting | Location | Needed for |
|---------|----------|------------|
| **Dataset Execute Queries REST API** | Integration settings | Running DAX from API |
| **Allow service principals to use Power BI APIs** | Developer settings | Only if using service principal |

Delegated (your login) usually works when **Dataset Execute Queries REST API** is enabled and you have access to the workspace.

---

## Step 3 — Config (do not commit secrets)

Copy `config.example.json` → `config.json` and fill in:

```json
"powerbi": {
  "tenant_id": "cbede638-a3d9-459f-8f4e-24ced73b4e5e",
  "client_id": "YOUR-APP-CLIENT-ID",
  "workspace_id": "813e80d7-5ba4-4629-a456-30255b5085c4",
  "report_id": "2693f2f6-4104-48c6-b741-95959d135323"
}
```

Or set environment variables:

```powershell
$env:POWERBI_TENANT_ID = "cbede638-a3d9-459f-8f4e-24ced73b4e5e"
$env:POWERBI_CLIENT_ID = "YOUR-APP-CLIENT-ID"
```

`config.json` is gitignored.

---

## Step 4 — Run discovery (you sign in once)

From repo root:

```powershell
uv run python toolkit/powerbi/discover_report.py
```

First run prints a **device code** — open https://microsoft.com/devicelogin, enter the code, sign in with the account that can open the report.

Output (agent-readable):

| File | Contents |
|------|----------|
| `outputs/scratch/powerbi_discovery.json` | Report, dataset, datasources, tables, errors |
| `outputs/scratch/powerbi_tables_sample.json` | First rows from `INFO.TABLES()` if API allows |

Token cache: `%USERPROFILE%\.msal_token_cache_powerbi.json` (local only, not in git).

Re-run discovery anytime to refresh schema or after model changes.

---

## Step 5 — Use in Cursor

After discovery succeeds, the agent can:

1. Read `outputs/scratch/powerbi_discovery.json` for table/column names and data source types
2. Draft the correct DAX for module/product revenue
3. Wire `revenue_loader.py` to Power BI instead of Excel

Example prompts:

- *"Run Power BI discovery and show me the data sources"*
- *"What tables are in the revenue dataset?"*
- *"Build module health scorecard with live Power BI revenue"*

---

## Option B — Service principal (team / scheduled runs)

For unattended scorecards (no browser login):

1. App registration → **Application** permissions: `Dataset.Read.All`
2. Admin enables **Allow service principals to use Power BI APIs**
3. Add the app to the Power BI **workspace** as Member/Admin
4. Grant the app **Build** permission on the dataset (dataset access, not just workspace)
5. Store `client_secret` in env `POWERBI_CLIENT_SECRET` (never commit)

Contact your Power BI admin if execute-query returns `401` despite workspace access.

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| **AADSTS65002** — *Consent between first party application … must be configured via preauthorization* | Your tenant blocks Microsoft's public Azure CLI app from Power BI API. **Path A will not work.** Use **Path B** (IT creates an app registration) or **Path C** (manual Export data from report). |
| `401 Unauthorized` on executeQueries | Need Build on dataset; or admin tenant setting off |
| `403` on report | Your account needs access to workspace `813e80d7-...` |
| Device flow disabled | Enable public client flows on app registration |
| INFO.TABLES() fails | Discovery still saves datasources; share a screenshot of the revenue visual or export one page to Excel |
| Empty datasources | Dataset may use DirectQuery / composite — metadata still in discovery JSON |

---

## Security notes

- Discovery runs **as you** — same access as opening the report in the browser
- Do not commit `config.json`, client secrets, or token cache
- DAX queries are read-only; discovery script does not modify reports or datasets
