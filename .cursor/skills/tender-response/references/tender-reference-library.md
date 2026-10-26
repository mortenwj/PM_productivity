# Tender reference library (skill index)

**Canonical path:** `docs/tender-reference/`

| Resource | Purpose |
|----------|---------|
| [`INDEX.md`](../../../../docs/tender-reference/INDEX.md) | **Auto-generated** file catalogue (run extract after source changes) |
| [`README.md`](../../../../docs/tender-reference/README.md) | Layout and workflow |

---

## Mandatory Stage 0a (before MCP)

| Step | Action |
|------|--------|
| 1 | Read **`docs/tender-reference/INDEX.md`** if tender folder is unknown |
| 2 | **Grep** `docs/tender-reference/extracted/` **recursively** for `Svar på krav [ID]`, `krav [ID]`, `5.2.18.1`, or topic keywords |
| 3 | **Read** full matching sections from hit `.txt` files (path includes tender folder) |
| 4 | Note reuse vs drift in tender evidence ledger |

Only after Stage 0a: grep `docs/product/`, then wiki / Ratatoskr / ADO / code.

---

## Tender folder quick map

| Folder | Primary use |
|--------|-------------|
| **`(root)`** | `KK Tender tool.txt` — KK matrix; granskning krav dependencies |
| **`FHM/`** | Forsvarshistorisk Museum — `Konkurransegrunnlag del III…txt`, `Ansvarsmatrise&Svar…txt`, `02.01-…Utfyllende beskrivelse av Tjenesten.txt` |
| **`NND/`** | Norwegian `02.01-…kravtabell.txt` — full SSA-L style answers |
| **`HSØ/`** | `02.00-…beskrivelse av Tjenesten.txt` — service description |
| **`KUM-SLKS/`** | Danish KK — `Bilag 3 - Kravspecifikation.txt`, processtyring, tidsplan |
| **`Nationalbanken/`** | PDF extracts — implementation, security, solution descriptions |

---

## Attachment existence rule

Only cite **«vedlagte Bilag …»** when the file exists under `docs/tender-reference/source/` (see `INDEX.md`) or the user confirms it is in the submission package. KK matrix **«Link to answer document»** names are often **planned** (`Not Started`) — not existing files.

---

## Regenerate index and extracts

```powershell
uv run python toolkit/scripts/extract_tender_reference.py
```

Produces: `extracted/` (mirrors `source/`), `INDEX.md`, `extracted/_index.json`.
