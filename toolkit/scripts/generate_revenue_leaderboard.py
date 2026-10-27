#!/usr/bin/env python3
"""
Generate a product revenue leaderboard by product team.

Uses:
- External Revenue, EUR.xlsx for product revenue (YTD)
- Module ownership mapping (aligned with wiki Module overview / Product Teams)

Outputs:
- revenue_leaderboard.html - Interactive report with drilldowns (Team -> Module -> Product)
- revenue_leaderboard.md - Static markdown summary

Note: Module-to-team mapping from product_first_request_process_analysis.
Validate at wiki.software-innovation.com Module overview / Product Teams.
"""

import json
import sys
import pandas as pd
from pathlib import Path
from collections import defaultdict

# Product name (from Excel) -> Module (wiki/ImpactedModule naming)
# Aligns with wiki module pages and ImpactedModule dropdown
PRODUCT_TO_MODULE = {
    # Core products
    "WebCruiter": "WebCruiter",
    "eArchive Historic search": "eArchive",
    "360° eEiendom": "eEiendom",
    "Consulting Customized": "Consulting",
    "Business 360°": "Business 360°",
    "360° Online Public": "Public 360°",
    "360° Scanning": "Scanning",
    "360° Integrasjon mot Folkeregisterert (NO)": "Integrations",
    "360° Board and Council": "Board meeting",
    "360° OpenGov Cases and Documents": "Public link",
    "360° eSigning Connect": "eSignature",
    "360° Contract Management": "Contract Management",
    "360° File Viewer": "Fileviewer",
    "360° eManager": "eManager",
    "Local hosting": "Local hosting",
    "360° Restricted mode": "Restricted Mode",
    "360° Integration with Sharepoint": "Integrations",
    "360° Mimir": "Mimir",
    "360° eServices Connect": "eServices",
    "360° eLearning": "eLearning",
    "eDoc Consulting": "Consulting",
    "P360° Lead offerings": "Public 360°",
    "360° Dispatch": "Dispatch",
    "360° eWorker": "eWorker",
    "360° AD Sync Service": "Usersync",
    "360° Format Converter": "Format converter",
    "Public 360°": "Public 360°",
    "360° PDF Signing": "Personal Digital Signing",
    "360° Archive Format Validator": "File validation",
    "360° Import Center": "File center",
    "360° Dispatch adapter: Deltagon": "Dispatch",
    "360° Integration with Folkeregisteret": "Integrations",
    "360° Dispatch DKAL Adaptor (DK)": "Dispatch",
    "360° Dispatch Adapter: Digipost": "Dispatch",
    "360° Integration with eFormidling (NO)": "Integrations",
    "360°Dispatch Adapter: Svar ut (NO)": "Dispatch",
    "360°Ekspedering adapter: DPI (NO)": "Dispatch",
    "360° Integration: SvarInn (NO)": "Integrations",
    "360° Integrasjon mot Enhetsregisteret (NO)": "Integrations",
    "360°Cadastre integration": "Integrations",
    "360° Enhetsregisteret - Update (NO)": "Integrations",
    "360° Folkeregisteret - Update (NO)": "Integrations",
    "360° Integration with Det Centrale Virksomhedsregister (DK)": "Integrations",
    "360° Integration with Det Centrale Personregister (DK)": "Integrations",
    "360°Meeting Management": "Board meeting",
    "360° eMeeting": "Board meeting",
    "360° Decision Tracking": "Decision tracking",
    "360° eMeetings Prepare": "Board meeting",
    "360° eMeetings Live": "Board meeting",
    "360° PDF Stamping": "Doc production",
    "360°  Information Act Requests": "IFAR",
    "360°  OpenGov Meetings": "Public link",
    "360° Public Journal": "Public link",
    "360° eInnsyn export": "eArchive",
    "360°  Sign": "eSignature",
    "360° Policy Documents": "Policy Documents",
    "360° Integration with NgDP": "Integrations",
    "360° Dispatch adapter: Mina meddelande": "Dispatch",
    "Server rent fee": "Infrastructure",
    "360° Additional Production Database": "Database",
    "360° Non-production environments": "Infrastructure",
    "360° Sharepoint Connect": "Integrations",
    "360° Third Party Integration Tools": "Integrations",
    "Others 3rd party": "Integrations",
    "360° Template Connect": "Template filters",
    "360° Integration with MS Office Apps": "Integrations",
    "360° Integration with MS Teams": "Teams Integration",
    "360° Integration with Webcruiter": "Integrations",
    "360° AutoSaver": "Document",
    "360° Process Engine": "Process Engine",
    "360° Process libary: Startskudd": "Process Engine",
    "360° Process libary: EveryOne": "Process Engine",
    "360° Process libary: Landbruksdirektoratet": "Process Engine",
    "360° Archive inspector": "eArchive",
    "360° Process library: Email archiving": "Process Engine",
    "360° eServices Platform": "eServices",
    "360° eArchive": "eArchive",
    "Doculive Historic Search": "eArchive",
    "Plan & Build 360°": "Plan&Build",
    "360° OpenGov Cases": "Public link",
    "360° Plansak": "Plan&Build",
    "360° Integrations with Finance system": "Integrations",
    "360° Matrikkelføring": "Plan&Build",
    "Consulting": "Consulting",
    "Consulting Application Management": "Consulting",
    "Customized Solution": "Consulting",
    "PixEdit": "Document",
    "360° Collect": "Collect",
    "360° RDF Portal": "Public link",
    "eDoc 360°": "eArchive",
}

# Module -> Product Team (from wiki Product Teams)
# Source: product_first_request_process_analysis.md Key Teams
MODULE_TO_TEAM = {
    "IFAR": "Transparency",
    "Dispatch": "Core BL and eArchive",
    "Access matrix": "Core BL and eArchive",
    "Access Group": "Core BL and eArchive",
    "Document": "Core UI",
    "Doc production": "Core BL and eArchive",
    "File Operations": "Core BL and eArchive",
    "eArchive": "Core BL and eArchive",
    "Workflow": "Process Platform",
    "SIF": "Core Integration",
    "Plan&Build": "Plan & Build",
    "Process Engine": "Process Platform",
    "Board meeting": "Decision Support",
    "UI-UX": "Core UI",
    "Webparts": "Core UI",
    "Search": "Core UI",
    "Contact": "Core UI",
    "Reports": "Decision Support",
    "Charts": "Decision Support",
    "Mimir": "AI & Insights",
    "eSignature": "Core BL and eArchive",
    "Personal Digital Signing": "Core BL and eArchive",
    "Fileviewer": "Core BL and eArchive",
    "File center": "Core BL and eArchive",
    "Format converter": "Core BL and eArchive",
    "File validation": "Core BL and eArchive",
    "Public link": "Transparency",
    "Restricted Mode": "Core BL and eArchive",
    "Decision tracking": "Decision Support",
    "Contract Management": "Decision Support",
    "eManager": "Decision Support",
    "eServices": "Engage & Collect",
    "Integrations": "Core Integration",
    "Teams Integration": "Core Integration",
    "Template filters": "Core UI",
    "Usersync": "Core Integration",
    "Collect": "Engage & Collect",
    "Public 360°": "Transparency",
    "Business 360°": "Transparency",
    "Scanning": "Core BL and eArchive",
    "WebCruiter": "Transparency",
    "eEiendom": "Plan & Build",
    "Policy Documents": "Transparency",
    "eLearning": "Transparency",
    "eWorker": "Core BL and eArchive",
    "Consulting": "Other",
    "Local hosting": "Other",
    "Infrastructure": "Tech Platform Team",
    "Database": "Tech Platform Team",
}


def extract_product_name(full_name: str) -> str:
    """Extract product name from 'A0xxxx Product Name' format."""
    if not isinstance(full_name, str):
        return ""
    parts = full_name.strip().split(None, 1)
    return parts[1] if len(parts) > 1 else full_name


def load_revenue_data(excel_path: str) -> tuple[pd.DataFrame, str]:
    """
    Load revenue from Excel. Auto-detect format.
    Returns (df, revenue_col) where revenue_col is the column name for totals.
    """
    df_raw = pd.read_excel(excel_path, sheet_name="Export", header=None)
    # Row 0 has headers (dates or metric names)
    row0 = [str(h).strip().lower() for h in df_raw.iloc[0]]
    last_col_header = row0[-1] if row0 else ""

    df = df_raw.iloc[2:].copy()

    if "total" in last_col_header or (len(df_raw.columns) > 10):
        # data.xlsx format: Product in col 0, Total in last col
        df.columns = [f"col_{i}" for i in range(len(df.columns))]
        df = df.rename(columns={df.columns[0]: "Product", df.columns[-1]: "YTD"})
        return df, "YTD"

    # External Revenue format: fixed columns
    df.columns = [
        "Product", "Reporting month", "Prior year", "Delta",
        "Prior month", "Delta prior month", "YTD", "YTD PY", "Delta YTD PY", "PY FY"
    ][: len(df.columns)]
    return df, "YTD"


def build_leaderboard(excel_path: str = "External Revenue, EUR.xlsx") -> dict:
    """Build revenue leaderboard by product team (Team -> Module -> Product)."""
    df, revenue_col = load_revenue_data(excel_path)

    # team -> { modules -> { products } }
    team_data = defaultdict(lambda: defaultdict(lambda: {"total": 0, "products": []}))
    unmapped_products = []

    for _, row in df.iterrows():
        product_full = str(row["Product"]).strip()
        if not product_full or not product_full.startswith("A0"):
            continue

        product_name = extract_product_name(product_full)
        ytd = row[revenue_col]
        if pd.isna(ytd) or ytd < 0:
            ytd = 0
        else:
            ytd = float(ytd)

        if ytd == 0 and product_full != "A01040 Consulting Customized":
            continue

        module = PRODUCT_TO_MODULE.get(product_name)
        if not module:
            for key, mod in PRODUCT_TO_MODULE.items():
                if key in product_name or product_name in key:
                    module = mod
                    break

        if not module:
            unmapped_products.append((product_name, ytd))
            continue

        team = MODULE_TO_TEAM.get(module, "Other")
        team_data[team][module]["total"] += ytd
        team_data[team][module]["products"].append({
            "product": product_name,
            "ytd_eur": ytd,
        })

    # Convert to serializable structure
    by_team = {}
    for team, modules in team_data.items():
        by_team[team] = {
            "total": sum(m["total"] for m in modules.values()),
            "modules": {
                mod: {
                    "total": info["total"],
                    "products": sorted(info["products"], key=lambda p: p["ytd_eur"], reverse=True),
                }
                for mod, info in modules.items()
            },
        }

    return {
        "by_team": by_team,
        "unmapped": unmapped_products,
    }


def format_eur(value: float) -> str:
    """Format as EUR with thousands separator."""
    return f"{value:,.0f}"


def write_leaderboard_md(data: dict, output_path: str, source_file: str = "") -> None:
    """Write leaderboard to Markdown file."""
    source = source_file or "External Revenue, EUR.xlsx"
    lines = [
        "# Product Revenue Leaderboard by Product Team",
        "",
        f"**Source:** {source} (YTD/Total revenue)",
        "**Grouping:** Product teams (wiki Module overview / Product Teams)",
        "",
        "---",
        "",
        "## Leaderboard (YTD Revenue)",
        "",
        "| Rank | Product Team | Revenue (EUR) | Share |",
        "|------|--------------|---------------|-------|",
    ]

    by_team = data["by_team"]
    total_revenue = sum(v["total"] for v in by_team.values())
    sorted_teams = sorted(
        by_team.items(),
        key=lambda x: x[1]["total"],
        reverse=True,
    )

    for rank, (team, info) in enumerate(sorted_teams, 1):
        rev = info["total"]
        pct = (rev / total_revenue * 100) if total_revenue else 0
        lines.append(f"| {rank} | {team} | {format_eur(rev)} | {pct:.1f}% |")

    lines.extend(["", "---", "", "## Detail by Team", ""])

    for team, info in sorted_teams:
        lines.append(f"### {team}")
        lines.append("")
        lines.append("| Module | Product | YTD (EUR) |")
        lines.append("|--------|---------|-----------|")
        for mod, mod_info in sorted(info["modules"].items(), key=lambda x: x[1]["total"], reverse=True):
            for p in mod_info["products"]:
                lines.append(f"| {mod} | {p['product']} | {format_eur(p['ytd_eur'])} |")
        lines.append("")

    if data["unmapped"]:
        lines.extend(["---", "", "## Unmapped Products", ""])
        for name, ytd in sorted(data["unmapped"], key=lambda x: x[1], reverse=True):
            lines.append(f"- {name}: {format_eur(ytd)} EUR")

    Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"Written: {output_path}")


def write_leaderboard_html(data: dict, output_path: str, source_file: str = "") -> None:
    """Write interactive HTML report with drilldowns."""
    # Build data for JS: teams sorted by revenue
    by_team = data["by_team"]
    total_revenue = sum(v["total"] for v in by_team.values())
    teams_sorted = sorted(
        by_team.items(),
        key=lambda x: x[1]["total"],
        reverse=True,
    )

    html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Product Revenue Leaderboard by Product Team</title>
  <style>
    :root {
      --bg: #0f1419;
      --surface: #1a2332;
      --surface-hover: #243044;
      --text: #e6edf3;
      --text-muted: #8b949e;
      --accent: #58a6ff;
      --accent-dim: #388bfd66;
      --success: #3fb950;
      --border: #30363d;
      --font: 'Segoe UI', system-ui, -apple-system, sans-serif;
    }
    * { box-sizing: border-box; }
    body {
      font-family: var(--font);
      background: var(--bg);
      color: var(--text);
      margin: 0;
      padding: 1.5rem;
      line-height: 1.5;
    }
    h1 { font-size: 1.5rem; margin: 0 0 0.5rem; }
    .subtitle { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.5rem; }
    .controls {
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
      margin-bottom: 1.5rem;
      align-items: center;
    }
    .controls label { display: flex; align-items: center; gap: 0.5rem; }
    select {
      background: var(--surface);
      color: var(--text);
      border: 1px solid var(--border);
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      font-size: 0.9rem;
    }
    .breadcrumb {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 1rem;
      font-size: 0.9rem;
      color: var(--text-muted);
    }
    .breadcrumb a { color: var(--accent); text-decoration: none; }
    .breadcrumb a:hover { text-decoration: underline; }
    .view { min-height: 200px; }
    table {
      width: 100%;
      border-collapse: collapse;
      background: var(--surface);
      border-radius: 8px;
      overflow: hidden;
    }
    th, td { padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid var(--border); }
    th { background: var(--surface-hover); font-weight: 600; color: var(--text-muted); font-size: 0.85rem; }
    tr:hover { background: var(--surface-hover); }
    tr.clickable { cursor: pointer; }
    .bar-cell { min-width: 120px; }
    .bar {
      height: 8px;
      background: var(--accent-dim);
      border-radius: 4px;
      overflow: hidden;
    }
    .bar-fill { height: 100%; background: var(--accent); border-radius: 4px; }
    .num { font-variant-numeric: tabular-nums; text-align: right; }
    .back-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.4rem 0.8rem;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text);
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.9rem;
      margin-bottom: 1rem;
    }
    .back-btn:hover { background: var(--surface-hover); }
    .hidden { display: none !important; }
  </style>
</head>
<body>
  <h1>Product Revenue Leaderboard</h1>
  <p class="subtitle">''' + (source_file or "Revenue data") + ''' · Grouped by Product Team</p>

  <div class="controls">
    <label>
      Sort by: <select id="sortBy">
        <option value="revenue">Revenue (desc)</option>
        <option value="name">Name (A–Z)</option>
      </select>
    </label>
    <label>
      View: <select id="viewLevel">
        <option value="team">By Product Team</option>
        <option value="module">By Module (flat)</option>
        <option value="product">By Product (flat)</option>
      </select>
    </label>
  </div>

  <div id="breadcrumb" class="breadcrumb hidden"></div>
  <button id="backBtn" class="back-btn hidden">← Back</button>

  <div id="content" class="view"></div>

  <script>
    const DATA = ''' + json.dumps({
        "teams": [
            {
                "name": team,
                "total": info["total"],
                "share": (info["total"] / total_revenue * 100) if total_revenue else 0,
                "modules": [
                    {
                        "name": mod,
                        "total": mod_info["total"],
                        "products": mod_info["products"],
                    }
                    for mod, mod_info in sorted(info["modules"].items(), key=lambda x: x[1]["total"], reverse=True)
                ],
            }
            for team, info in teams_sorted
        ],
        "totalRevenue": total_revenue,
    }) + ''';
    const fmt = (n) => new Intl.NumberFormat('en-EU', { maximumFractionDigits: 0 }).format(n);

    let drill = { level: 'team', team: null, module: null };

    function render() {
      const content = document.getElementById('content');
      const bc = document.getElementById('breadcrumb');
      const backBtn = document.getElementById('backBtn');
      const viewLevel = document.getElementById('viewLevel').value;

      if (viewLevel === 'team' && !drill.team) {
        renderTeams(content, bc, backBtn);
      } else if (viewLevel === 'team' && drill.team && !drill.module) {
        renderModules(content, bc, backBtn);
      } else if (viewLevel === 'team' && drill.team && drill.module) {
        renderProducts(content, bc, backBtn);
      } else if (viewLevel === 'module') {
        renderModulesFlat(content, bc, backBtn);
      } else if (viewLevel === 'product') {
        renderProductsFlat(content, bc, backBtn);
      }
    }

    function renderTeams(container, bc, backBtn) {
      bc.classList.add('hidden');
      backBtn.classList.add('hidden');
      drill = { level: 'team', team: null, module: null };

      const sortBy = document.getElementById('sortBy').value;
      let teams = [...DATA.teams];
      if (sortBy === 'name') teams.sort((a,b) => a.name.localeCompare(b.name));
      else teams.sort((a,b) => b.total - a.total);

      let html = '<table><thead><tr><th>Rank</th><th>Product Team</th><th class="bar-cell">Share</th><th class="num">YTD (EUR)</th></tr></thead><tbody>';
      teams.forEach((t, i) => {
        const pct = ((t.total / DATA.totalRevenue) * 100).toFixed(1);
        html += `<tr class="clickable" data-team="${escapeAttr(t.name)}">
          <td>${i+1}</td><td>${escapeHtml(t.name)}</td>
          <td class="bar-cell"><div class="bar"><div class="bar-fill" style="width:${pct}%"></div></div></td>
          <td class="num">${fmt(t.total)}</td></tr>`;
      });
      html += '</tbody></table>';
      container.innerHTML = html;
      container.querySelectorAll('tr.clickable').forEach(tr => {
        tr.addEventListener('click', () => { drill.team = tr.dataset.team; render(); });
      });
    }

    function renderModules(container, bc, backBtn) {
      bc.classList.remove('hidden');
      backBtn.classList.remove('hidden');
      bc.innerHTML = `<a href="#" data-action="teams">All Teams</a> › <span>${escapeHtml(drill.team)}</span>`;
      bc.querySelector('a').onclick = (e) => { e.preventDefault(); drill.team = null; render(); };

      const team = DATA.teams.find(t => t.name === drill.team);
      if (!team) { renderTeams(container, bc, backBtn); return; }

      let html = '<table><thead><tr><th>Module</th><th class="bar-cell">Share</th><th class="num">YTD (EUR)</th></tr></thead><tbody>';
      team.modules.forEach(m => {
        const pct = ((m.total / team.total) * 100).toFixed(1);
        html += `<tr class="clickable" data-module="${escapeAttr(m.name)}">
          <td>${escapeHtml(m.name)}</td>
          <td class="bar-cell"><div class="bar"><div class="bar-fill" style="width:${pct}%"></div></div></td>
          <td class="num">${fmt(m.total)}</td></tr>`;
      });
      html += '</tbody></table>';
      container.innerHTML = html;
      container.querySelectorAll('tr.clickable').forEach(tr => {
        tr.addEventListener('click', () => { drill.module = tr.dataset.module; render(); });
      });
    }

    function renderProducts(container, bc, backBtn) {
      bc.classList.remove('hidden');
      backBtn.classList.remove('hidden');
      bc.innerHTML = `<a href="#" data-action="teams">All Teams</a> › <a href="#" data-action="modules">${escapeHtml(drill.team)}</a> › <span>${escapeHtml(drill.module)}</span>`;
      bc.querySelectorAll('a').forEach(a => {
        a.onclick = (e) => { e.preventDefault(); if (a.dataset.action==='teams') { drill.team=null; drill.module=null; } else { drill.module=null; } render(); };
      });

      const team = DATA.teams.find(t => t.name === drill.team);
      const mod = team?.modules.find(m => m.name === drill.module);
      if (!mod) { renderTeams(container, bc, backBtn); return; }

      let html = '<table><thead><tr><th>Product</th><th class="bar-cell">Share</th><th class="num">YTD (EUR)</th></tr></thead><tbody>';
      mod.products.forEach(p => {
        const pct = ((p.ytd_eur / mod.total) * 100).toFixed(1);
        html += `<tr><td>${escapeHtml(p.product)}</td>
          <td class="bar-cell"><div class="bar"><div class="bar-fill" style="width:${pct}%"></div></div></td>
          <td class="num">${fmt(p.ytd_eur)}</td></tr>`;
      });
      html += '</tbody></table>';
      container.innerHTML = html;
    }

    function renderModulesFlat(container, bc, backBtn) {
      bc.classList.add('hidden');
      backBtn.classList.add('hidden');
      const sortBy = document.getElementById('sortBy').value;
      const rows = [];
      DATA.teams.forEach(t => t.modules.forEach(m => rows.push({ team: t.name, module: m.name, total: m.total })));
      if (sortBy === 'name') rows.sort((a,b) => a.module.localeCompare(b.module));
      else rows.sort((a,b) => b.total - a.total);

      let html = '<table><thead><tr><th>Product Team</th><th>Module</th><th class="bar-cell">Share</th><th class="num">YTD (EUR)</th></tr></thead><tbody>';
      rows.forEach(r => {
        const pct = ((r.total / DATA.totalRevenue) * 100).toFixed(1);
        html += `<tr class="clickable" data-team="${escapeAttr(r.team)}" data-module="${escapeAttr(r.module)}">
          <td>${escapeHtml(r.team)}</td><td>${escapeHtml(r.module)}</td>
          <td class="bar-cell"><div class="bar"><div class="bar-fill" style="width:${pct}%"></div></div></td>
          <td class="num">${fmt(r.total)}</td></tr>`;
      });
      html += '</tbody></table>';
      container.innerHTML = html;
      container.querySelectorAll('tr.clickable').forEach(tr => {
        tr.addEventListener('click', () => { drill.team = tr.dataset.team; drill.module = tr.dataset.module; document.getElementById('viewLevel').value = 'team'; render(); });
      });
    }

    function renderProductsFlat(container, bc, backBtn) {
      bc.classList.add('hidden');
      backBtn.classList.add('hidden');
      const sortBy = document.getElementById('sortBy').value;
      const rows = [];
      DATA.teams.forEach(t => t.modules.forEach(m => m.products.forEach(p =>
        rows.push({ team: t.name, module: m.name, product: p.product, total: p.ytd_eur }))));
      if (sortBy === 'name') rows.sort((a,b) => a.product.localeCompare(b.product));
      else rows.sort((a,b) => b.total - a.total);

      let html = '<table><thead><tr><th>Product Team</th><th>Module</th><th>Product</th><th class="bar-cell">Share</th><th class="num">YTD (EUR)</th></tr></thead><tbody>';
      rows.forEach(r => {
        const pct = ((r.total / DATA.totalRevenue) * 100).toFixed(1);
        html += `<tr><td>${escapeHtml(r.team)}</td><td>${escapeHtml(r.module)}</td><td>${escapeHtml(r.product)}</td>
          <td class="bar-cell"><div class="bar"><div class="bar-fill" style="width:${pct}%"></div></div></td>
          <td class="num">${fmt(r.total)}</td></tr>`;
      });
      html += '</tbody></table>';
      container.innerHTML = html;
    }

    function escapeHtml(s) { const d=document.createElement('div'); d.textContent=s; return d.innerHTML; }
    function escapeAttr(s) { return escapeHtml(s).replace(/"/g,'&quot;'); }

    document.getElementById('sortBy').addEventListener('change', render);
    document.getElementById('viewLevel').addEventListener('change', () => { drill = { level: 'team', team: null, module: null }; render(); });
    document.getElementById('backBtn').addEventListener('click', () => {
      if (drill.module) drill.module = null;
      else if (drill.team) drill.team = null;
      render();
    });
    render();
  </script>
</body>
</html>'''
    Path(output_path).write_text(html, encoding="utf-8")
    print(f"Written: {output_path}")


if __name__ == "__main__":
    excel_path = sys.argv[1] if len(sys.argv) > 1 else "External Revenue, EUR.xlsx"
    base = Path(excel_path).stem.replace(" ", "_").replace(",", "")
    out_suffix = f"_{base}" if base not in ("External_Revenue_EUR", "Export") else ""
    md_path = f"revenue_leaderboard{out_suffix}.md"
    html_path = f"revenue_leaderboard{out_suffix}.html"

    data = build_leaderboard(excel_path)
    write_leaderboard_md(data, md_path, source_file=excel_path)
    write_leaderboard_html(data, html_path, source_file=excel_path)
    print(f"\nInput: {excel_path}")
    print(f"Output: {md_path}, {html_path}")
    print("\nTop 5 teams by revenue:")
    for team, info in sorted(data["by_team"].items(), key=lambda x: x[1]["total"], reverse=True)[:5]:
        print(f"  {team}: {format_eur(info['total'])} EUR")
