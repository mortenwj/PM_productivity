# Profile: tender-evidence

**Id:** `profile:tender-evidence`  
**Used by:** `tender-response` (RFP / anbud requirement answers).

**Evidence semantics:** **[`../evidence-playbook.md`](../evidence-playbook.md)** is authoritative for **claim**, **evidence**, **verified**, **lead**, **inferred**, **confidence**, **when to stop**, and **conflicts**. This profile defines **load order, krav routing, and tender-specific conflict handling** only.

**Also read:** [`../README.md`](../README.md), [`../budgets.md`](../budgets.md), [`../sources-and-tools.md`](../sources-and-tools.md), [`../ratatoskr-preflight.md`](../ratatoskr-preflight.md), [`../verification-and-leads.md`](../verification-and-leads.md), [`../mediawiki_extract.md`](../mediawiki_extract.md).

**Ratatoskr tool order:** [`../../../tender-response/references/ratatoskr-mcp-tools.md`](../../../tender-response/references/ratatoskr-mcp-tools.md) (or `~/.cursor/skills/lmwtfy/rules/ratatoskr-mcp-tools.md`).

**Bounded retrieval:** Apply caps in [`../budgets.md`](../budgets.md) unless the user expands the budget. Skipped MCP servers → record in the tender evidence ledger with reason.

---

## How this differs from `code-first-research` (lmwtfy)

| Aspect | lmwtfy (`code-first-research`) | tender (`tender-evidence`) |
|--------|-------------------------------|----------------------------|
| **Primary goal** | Answer colleague's technical question | Draft evaluator-facing compliance text |
| **Load order** | Code → Help → ADO → Wiki | Prior answers → Wiki → Help → ADO → Code |
| **Conflict rule** | Code wins on shipped behaviour | Code wins on **truth**; cite **help/wiki** in tender prose when customer-facing |
| **Output** | Answer file + optional wiki loop | Requirement response + evidence ledger row |
| **Overclaim risk** | Wrong answer to colleague | Disqualification / audit exposure |

Do **not** use lmwtfy's code-first order for tender drafting unless the user explicitly requests a one-off "prove in code first" pass (declare in ledger).

---

## Stage 0 — Local prior art (always first)

Before any MCP call — **both substages are mandatory**:

### 0a — Tender reference library (primary)

**Path:** `docs/tender-reference/extracted/` (recursive; see [`INDEX.md`](../../../docs/tender-reference/INDEX.md)).

1. **Grep** `docs/tender-reference/extracted/` **recursively** for requirement ID (`Svar på krav 1.7`, `5.2.18.1`, etc.) and topic keywords.
2. Consult **`docs/tender-reference/INDEX.md`** to select the right tender folder (`NND/`, `KUM-SLKS/`, …).
2. **Read** matching sections from hit `.txt` files (full paragraphs, not search snippets).
3. Record in tender evidence ledger: `Source: docs/tender-reference/extracted/<file>.txt`.

If `extracted/` is missing, run `uv run python toolkit/scripts/extract_tender_reference.py` after populating `docs/tender-reference/source/`.

### 0b — Repo drafts and context

1. **Grep** `docs/product/` for requirement ID, keywords, and topic.
2. Read `docs/product/context/master-context.md` when framing product capabilities.
3. Read matching files from [`../../../tender-response/references/examples.md`](../../../tender-response/references/examples.md).

**Stop stage 0 early** only when prior approved text exists in **0a or 0b** **and** the user confirms reuse; still run verification spot-checks on facts that may have changed (versions, SLAs, certifications).

---

## Krav-type routing

Pick the **primary track** after parsing the requirement. Run the full waterfall for that track; add stages from other tracks when the krav spans types (e.g. security + product capability).

| Krav type | Signals | Waterfall emphasis |
|-----------|---------|-------------------|
| **Product capability** | funksjonalitet, støtter, konfigurasjon, integrasjon, NOARK, arkiv | Ratatoskr (admin-en/no) → Wiki module/release → Code if ambiguous |
| **Security / ops** | sikkerhet, backup, DR, TLS, tilgang, audit, SaaS, B/K | Wiki security/ops → `docs/tender-reference/` → `docs/product/` security tenders → Ratatoskr admin → Code for specific controls |
| **Process / delivery** | prosess, endring, risiko, test, oppgradering, SLA | Wiki process pages → `docs/tender-reference/` → `docs/product/` process tenders → ADO only for commitment dates |
| **Certification / compliance** | godkjenning, NOARK, ISO, GDPR, vedlegg | Wiki + `docs/product/` + linked PDFs via Ratatoskr `get_linked_files` / `read_pdf` |
| **Roadmap / future** | skal leveres, planlagt, versjon | ADO (state = closed for "shipped") → never claim from open/new items without Partial + date |

---

## Staged retrieval (default waterfall)

Execute **in order** after stage 0. **Stop early** when [`../evidence-playbook.md`](../evidence-playbook.md) §6 sufficiency is met for the compliance level you plan to claim.

| Stage | Source | Actions | Stop if |
|-------|--------|---------|--------|
| **1** | **MediaWiki** (`user-mediawiki`) | 1–3 `mediawiki_search` → `mediawiki_get_page` for **≤5** pages (release, module, security, delivery process) | Process/certification claims fully supported |
| **2** | **Ratatoskr** (`user-ratatoskr`) | Preflight [`../ratatoskr-preflight.md`](../ratatoskr-preflight.md) → `search_topics` → `read_topic` for **≤3** topics; `lookup_config` for settings questions; `feature_timeline` for "when available" | Customer-visible capability confirmed or denied |
| **3** | **ADO** (`user-azure-devops`) | Only when krav references delivery, commitments, or shipped vs planned; WIQL/top **≤10**; prefer **closed** for "exists today" | Roadmap gap identified with work item id |
| **4** | **Code** (`gh` / Grep) | Scoped read per [`../budgets.md`](../budgets.md); only when stages 1–3 insufficient or contradictory | Implementation confirms/denies specific behaviour |

### MediaWiki tips for tenders

- Prefer **Release Information**, **module overviews**, **security**, **upgrade/delivery** pages.
- Use `mediawiki_search_in_page` on long policy pages.
- Record **wiki URLs** for internal ledger; convert to **attachment titles** in final tender if buyer expects Bilag refs not URLs.

### Ratatoskr tips for tenders

- **admin-no** for Norwegian tender prose alignment; **admin-en** for technical precision.
- **release** section for version-gated claims.
- `lookup_config` when krav names a specific setting, register field, or code table.
- `feature_timeline` before stating "introduced in version X".

### Code tips for tenders

- **Read-only** per [`../sources-and-tools.md`](../sources-and-tools.md).
- Use code to **verify** claims, not as primary citation in evaluator text (unless RFP asks for technical architecture evidence).
- Key repos: `te-industry-public360/core-bl`, `te-industry-public360/core-*`.

---

## Conflict handling (tender-specific)

When verified sources disagree:

1. **Shipped behaviour today:** implementation (**code**) wins per playbook §7.
2. **Customer-facing description:** if help/wiki understate capability that code proves → draft can state capability; cite help if accurate, add wiki/internal ref in ledger.
3. **Help/wiki overstate capability vs code:** tender text follows **code**; compliance = **Partial** or **Gap**; do not copy optimistic help into binding bid text.
4. **Prior tender text vs current sources:** prefer **current verified sources**; flag drift to user before reusing old numbers.

Record every conflict in the tender evidence ledger.

---

## Tender evidence ledger (required before final draft)

For **Respond** and **Gap analysis** modes when any factual product/process claim is made. Present to user: **"Evidence checks out? OK to draft final answer?"**

Per planned claim:

| Field | Content |
|-------|---------|
| **Claim** | Statement intended for tender prose |
| **Compliance use** | Met / Partial / Supporting detail only |
| **Source** | Wiki URL / help topic URL / ADO item / GitHub blob / `docs/product/…` / UNVERIFIED |
| **Verified how** | Per playbook §4 |
| **Cite in tender** | Inline / attachment ref only / internal ledger only |
| **Confidence** | High / Medium / Low |

**UNVERIFIED** claims must be verified, downgraded, marked Partial/Gap, or removed.

Full template: [`../../../tender-response/references/evidence-retrieval.md`](../../../tender-response/references/evidence-retrieval.md).

---

## Rationalizations to reject (tender-specific)

| Rationalization | Why it is wrong |
|-----------------|-----------------|
| "We answered this in a past bid" | Grep `docs/tender-reference/extracted/` first; verify facts against current sources |
| "Help doesn't mention it so we don't support it" | Check code before Gap; help coverage is incomplete |
| "Wiki says we do X" | Read the section; wiki can be stale — cross-check release notes or code |
| "ADO item exists so it's shipped" | Only **closed/done** items support "leveres i dag" |
| "Standard cloud practice covers this" | Public-sector evaluators want **product-specific** proof |
| "Snippet is enough for the ledger" | Full read per [`../verification-and-leads.md`](../verification-and-leads.md) |

---

**File:** `shared/evidence/profiles/tender-evidence.md`
