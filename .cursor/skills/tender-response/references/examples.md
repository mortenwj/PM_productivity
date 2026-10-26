# Tender response examples in this repo

**Always grep `docs/tender-reference/extracted/` recursively** and check [`docs/tender-reference/INDEX.md`](../../../../docs/tender-reference/INDEX.md) for the current file list.

---

## By tender folder

| Folder | Key extracted paths | Use for |
|--------|---------------------|---------|
| **`NND/`** | `NND/02.01-…-kravtabell.txt` | **Primary NO** — `Svar på krav X.Y`, Fordeler, U/B/K |
| **`HSØ/`** | `HSØ/02.00-…-beskrivelse av Tjenesten.txt` | Tjenestebeskrivelse narrative |
| **`KUM-SLKS/`** | `KUM-SLKS/Bilag 3 - Kravspecifikation.txt`, `…Processtyring (1).txt` | Danish KK krav + processtyring / Management Reporting API |
| **`(root)`** | `KK Tender tool.txt` | KK matrix — ReqID, owners, planned answer doc names |
| **`Nationalbanken/`** | `Nationalbanken/Bilag 3.i …txt`, etc. | PDF bid material — implementation, security |

---

## Repo drafts (secondary)

| File | Pattern |
|------|---------|
| `docs/product/Krav_2.24_Svar_Forslag.md` | Ugradert/Gradert split; security scenarios |
| `docs/product/Risikostyring_Anbudssvar.md` | Parent + numbered sub-krav (3.5.11x) |
| `docs/product/RFP_Leverandørens_svar_utdrag.txt` | Partial extract; prefer `NND/02.01-…txt` |

---

## Attachment rule

KK matrix **«Link to answer document»** (e.g. `Bilag 2 - 5.2.18.1 - …docx`) is often **planned**, not on disk. Only cite *«vedlagte»* when the file appears in `INDEX.md` under `source/`.
