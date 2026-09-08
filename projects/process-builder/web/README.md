# Process Builder — web app

Branded React UI for 360° Flow process authoring (ADO #400794). UX based on [processmaker-gamma.vercel.app](https://processmaker-gamma.vercel.app/); styling uses **Tietoevry Brand Kit for AI Agents**.

## Brand kit

Tokens and assets:

- `../brand-kit/brand-tokens.json` — machine-readable colors and paths
- `public/assets/tieto-logo-blue.svg` — header logotype (blue on light; do not recolor)
- `public/favicon.svg` — Tieto favicon

Full kit path on this machine: `C:\Users\MortenJensen\Brand Kit for Ai Agents`

Install **Tieto Sans** from the kit for correct typography (`Tieto Sans Typedace/TTF`). Until installed, the app falls back to Segoe UI / system-ui.

## Run locally

```powershell
cd projects/process-builder/web
npm install
npm run dev
```

Open http://localhost:5175

## v1 scope (current)

- Sidebar process list (localStorage)
- Six activity accordions matching skill palette
- Behandlingsform + metadata (Argumenter / Egenskaper tabs)
- Export process definition as JSON
- **Generate `.wu` + `.xaml`** — same structure as `flowworkunit-new-process` skill (templates.md / reference.md)

**Next:** Write generated files to `projects/process-builder/output/` via a local script or File System Access API.

## Output folder (planned)

Generated artifacts will land under:

`projects/process-builder/output/<process-name>/`

Manual copy from there to core-bl or customer instance per brief.
