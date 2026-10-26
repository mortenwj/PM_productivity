# Tender response templates

Use the template that matches the buyer's mandated format. Adapt section titles to the RFP; do not add sections the buyer did not ask for.

---

## A. Norwegian narrative (DFO / standard kravtabell — free text)

Use when the cell allows structured prose (see `docs/tender-reference/extracted/02.01-…-kravtabell.txt` or `docs/product/RFP_Leverandørens_svar_utdrag.txt`).

```markdown
## Svar på krav [ID]

**Kundens krav:** [Quote or faithful paraphrase of requirement]

**Leverandørens besvarelse:**

[Direct compliance — one sentence answering how the requirement is met.]

### [Sub-part or theme 1 — mirror buyer heading if present]
[Concrete capability, process step, or control. Name product modules/tools.]

### [Sub-part or theme 2]
[...]

**Dokumentasjon / vedlegg:** [Attachment ID and title, e.g. 02.0x – 1.4 - NOARK godkjenningsbrev]
```

### Variant with "Fordeler" (when RFP template includes benefit blocks)

```markdown
**Oppsummering**
[2–3 sentences: compliance + differentiation tied to win theme]

**Fordeler for kunden**
- [Outcome-oriented benefit — not feature list]
- [Max 4–6 bullets]

**Beskrivelse av hvordan kravet oppfylles**
[Technical/process detail; evidence; metrics]
```

---

## B. Norwegian Ugradert / Gradert split

Use when one krav has separate cells for security platforms.

```markdown
## Leverandørens besvarelse Ugradert

### 1) [Buyer sub-heading]
[Supplier-operated SaaS: controls, geo-redundancy, ops routines, SLAs]

### 2) [Buyer scenario if any]
[...]

---

## Leverandørens besvarelse Gradert

### 1) [Same sub-heading]
[Same product design; customer-operated infra; supplier documentation/support role]

### 2) [Buyer scenario if any]
[Insider threat / admin — shared product controls + customer governance]
```

Reference: `docs/product/Krav_2.24_Svar_Forslag.md`.

---

## C. English narrative (international / EU-style)

```markdown
## Response to Requirement [ID]

**Requirement:** [Verbatim or faithful paraphrase]

**Compliance:** [Full | Partial — see note below]

**Response:**

[Opening sentence: direct compliance statement.]

### [Sub-requirement a]
[Evidence-backed description]

### [Sub-requirement b]
[...]

**Supporting documentation:** [Annex / certificate / help reference]
```

For Partial compliance, add immediately after Compliance line:

```markdown
**Note:** [What is met today; what is partial; alternative approach or customer action; timeline if roadmap.]
```

---

## D. Compact table cell (character-limited)

Structure as dense paragraphs, no extra headings:

1. Compliance sentence (≤40 words).
2. How met (product + process).
3. Evidence pointer (attachment ID only if space tight).

Avoid bullets in very tight cells unless the buyer uses them.

---

## E. Sub-requirement mapping (3.5.11x style)

When the buyer lists numbered sub-krav under one parent:

```markdown
## Svar på krav nr. [parent]

**Kundens krav:** [Parent requirement]

**Leverandørens besvarelse:**
[Short intro tying process together]

---

## Svar på krav nr. [child]

**Kundens krav:** [Child text verbatim]

**Leverandørens besvarelse:**

### [Aspect 1 from child requirement]
[...]

### [Aspect 2]
[...]
```

Reference: `docs/product/Risikostyring_Anbudssvar.md`.

---

## F. Internal draft marker (remove before submission)

During drafting, append for reviewer traceability:

```markdown
---
**Internal — remove before submit**
| Claim | Evidence | Confidence |
|-------|----------|------------|
| [statement] | [source] | High/Med/Low |
---
```

---

## Opening sentence patterns

**Full compliance (NO):**
- "Skytjenesten oppfyller krav [ID] gjennom …"
- "Leverandøren har etablert prosess for … som omfatter …"

**Full compliance (EN):**
- "The Service meets Requirement [ID] by …"
- "The Supplier maintains a documented process for …"

**Partial (honest):**
- "Kravet oppfylles delvis: [met part]. For [gap] gjelder følgende alternativ / kundens ansvar: …"
- "Requirement [ID] is partially met. [X] is delivered today; [Y] is addressed through [alternative/customer responsibility]."

**Configuration vs custom:**
- "Kundespesifikke behov løses gjennom konfigurasjon i standardproduktet, uten custom code utenfor produktutviklingsprosessen."

---

## Attachment reference format

Match buyer convention when known. Default:

```
[Section] – [Krav ID] - [Supplier] - Bilag [n] - [Document title]
```

Example from repo: `02.0x – 1.4 -Tietoevry-Bilag 2-Vedlegg Public 360 NOARK godkjenningsbrev med vedlegg`
