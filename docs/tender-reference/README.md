# Tender reference library

Canonical **prior bid responses** for the `tender-response` skill. The agent must search here **before** drafting any requirement answer.

**Sensitive:** Real SSA-L / kravtabell material. Do not commit to a public repo unless your policy allows it (see [Refresh](#refresh) and `.gitignore`).

---

## Layout

| Path | Purpose |
|------|---------|
| [`source/`](source/) | Original `.docx` / `.xlsx` / `.pdf` — organised by tender (`NND/`, `KUM-SLKS/`, …) |
| [`extracted/`](extracted/) | Plain-text extracts (mirrors `source/` layout) for **Grep** |
| [`INDEX.md`](INDEX.md) | **Auto-generated** catalogue — run extract script after changes |

---

## Index

After any change to `source/`, regenerate:

```powershell
uv run python toolkit/scripts/extract_tender_reference.py
```

This updates `extracted/`, removes stale extracts, and rewrites **`INDEX.md`** (+ `extracted/_index.json`).

**Search scope:** Grep `docs/tender-reference/extracted/` recursively (not only the repo root of `extracted/`).

---

## Tender folders (current)

| Folder | Contents |
|--------|----------|
| **`(root)`** | `KK Tender tool.xlsx`, granskning krav map |
| **`FHM/`** | Forsvarshistorisk Museum — konkurransegrunnlag del III, ansvarsmatrise, tjenestebeskrivelse, **Bilag 3 etableringsplan**, **fremdriftsplan m/ estimater** |
| **`NND/`** | Norwegian `02.01-…` kravtabell, arbeidsflyt/granskning arbeidsdokument |
| **`HSØ/`** | SSA-L tjenestebeskrivelse (`02.00-…`) |
| **`KUM-SLKS/`** | Danish KK cluster — kravspecifikation, processtyring, tidsplan, priser |
| **`Nationalbanken/`** | PDF bilag — løsningsbeskrivelser, implementering, sikkerhed |

See **[`INDEX.md`](INDEX.md)** for the full file list with sizes and extract status.

---

## Files (legacy quick reference)

| Source | Use when drafting |
|--------|-------------------|
| `FHM/Konkurransegrunnlag del III …v2.docx` | **FHM buyer** — åpen anbudskonkurranse, kravspesifikasjon basis |
| `FHM/Ansvarsmatrise&Svar på kravspesifikasjon_FHM.xlsx` | **FHM** — ansvarsmatrise + svar på krav |
| `FHM/02.01-…-Utfyllende beskrivelse av Tjenesten.docx` | **FHM supplier** — Bilag 2 vedlegg, tjenestebeskrivelse |
| `NND/02.01-…-kravtabell.docx` | **Primary NO (NND)** — full kravtabell answers |
| `KUM-SLKS/Bilag 3 - Kravspecifikation.docx` | Danish kravspecifikation cluster |
| `KUM-SLKS/Bilag 3 - 11.8 - … Processtyring.docx` | Processtyring / 360° Flow / Management Reporting API |
| `KK Tender tool.xlsx` | KK compliance matrix (ReqID, owners, answer doc links) |

---

## Agent workflow (mandatory)

On every **Respond**, **Gap analysis**, or **Review** with factual claims:

1. **Grep** `docs/tender-reference/extracted/` **recursively** for the requirement ID (e.g. `krav 2.24`, `Svar på krav 1.7`, `5.2.18.1`).
2. Check **[`INDEX.md`](INDEX.md)** to pick the right tender folder (`NND/`, `KUM-SLKS/`, …).
2. **Grep** for topic keywords if ID unknown.
3. **Read** the matching paragraph(s) from the hit file(s) — not snippet-only.
4. **Adapt** tone and structure from prior art; **verify** facts against wiki / Ratatoskr / code per `profile:tender-evidence`.
5. Record prior-art path in the **tender evidence ledger** (`Source: docs/tender-reference/extracted/…`).

Then continue with `docs/product/` drafts and MCP sources as in the skill.

---

## Refresh

After adding or updating files in `source/`:

```powershell
uv run python toolkit/scripts/extract_tender_reference.py
```

---

## Populating on a new machine

1. Copy your `bid responses` folder contents into `docs/tender-reference/source/`.
2. Run the extract command above.
3. Confirm `extracted/*.txt` exist before using `tender-response`.
