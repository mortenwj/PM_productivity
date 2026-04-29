# PFR problem 2: “We already support that” (knowledge and discovery)

**Intent:** Tackle this *before* broad quality fixes on request text.  
**Context:** Public 360° is large; consultants and customers often ask for X when the product already delivers X (or a close equivalent) via another module, flow, setting, or supported configuration pattern.

*(You wrote “PDR”; this note follows the Product First Request / PFR naming used elsewhere.)*

---

## Problem statement

| Symptom | Effect |
|--------|--------|
| Request describes a **desired UI or workflow**, not the **underlying need** | PM and R&D spend time on items that should never enter the “new functionality” funnel. |
| **Unknown standard path** | Noise on the PFR board, slower answers, frustration (“you said no, but we needed Y”). |
| **Custom-first habit** | Reinvents what configuration or a different case/document model already allows—works against Product First strategy. |

This is **not** mainly a template problem; it is a **discovery, routing, and verification** problem.

---

## Strategic goal

Before a Feature is treated as a **product gap**, the organization should produce a **short, explicit “standard capability check”** outcome:

1. **Already supported** — document *where* (module, setting, pattern, wiki/release note) and how the user achieves the outcome.  
2. **Achievable without new core code** — configuration / case model / integration / extension point; still document the pattern.  
3. **Partially supported** — what exists + what is genuinely missing (then a narrow PFR makes sense).  
4. **Not supported** — justified PFR with clear gap vs standard.

The wiki’s first activity already points here (“understand request”, configuration possibilities, module overviews, prior board items, PM advice)—but **today it is not enforced as a visible gate or record** before the DevOps item becomes the system of record.

---

## Practical interventions (ordered by leverage)

### 1. Make the gate visible and mandatory (lightweight)

Add a **single required step before “Report request”** (or immediately when creating the Feature):

- **Owner:** Solution consultant (functional) or Technical Consulting (technical), per existing RACI on [[Product first - Request new functionality]].  
- **Output:** A short section in the work item (or CIM ticket) titled e.g. **“Standard capability check”** with:  
  - **Outcome** (one of the four bullets above)  
  - **Evidence** (links: wiki page, release note, module doc, similar customer, test env screenshot)  
  - **Who** performed the check and **when**

If the outcome is (1) or (2), the process should **stop or redirect** (close with rationale, or convert to documentation/training task)—not continue as an open “new functionality” request unless leadership explicitly wants a UX improvement PFR.

### 2. Curated “same need, different place” patterns

Maintain a **small, living pattern library** (wiki or internal doc—not a dump of every feature):

- **Themes:** access / IFAR / P&B stages / eArchive / search / integrations / cloud vs on-prem.  
- **Each pattern:** symptom → standard approach → “when not applicable” → link to deeper doc.

This gives consultants a **fast path** before PM time. It complements [[Configuration Possibilities in 360°]] and module overviews by answering *“I want behaviour B”* in product language.

### 3. Triage ownership and SLAs for *discovery* only

- **First 48–72 hours:** not “full PM evaluation,” but **capability routing**—is this likely standard, config, or product?  
- **Escalation:** to the right PM from [[Product teams]] when the triager is stuck (wiki already encourages PM contact for uncertainty).

Reduces the second problem without pretending every item gets deep architecture immediately.

### 4. Instrumentation (simple metrics)

Track over a quarter:

- PFRs **withdrawn or closed** as “already supported / configuration”  
- **Time to first triage note** with evidence link  
- Repeat topics (same `Custom.ImpactedModule` + similar title)—candidate for pattern library entries

If these numbers move, the second problem is shrinking even if request *text* quality is still uneven.

### 5. Optional DevOps hygiene (later)

When you are ready for tooling: a tag or custom field such as **“Capability check: Complete”** with values *Standard / Config / Partial / Gap* makes reporting easier. Not required to start; narrative in Description is enough.

---

## Dependencies and risks

| Risk | Mitigation |
|------|------------|
| Triagers become a bottleneck | Time-box the check; escalate; expand pool (TC + senior consultants). |
| “False negatives” (marked supported but customer rejects) | Involve customer-facing role in sign-off for high-stakes customers; link to customer plan where relevant. |
| Pattern library rots | Owner (e.g. Head of Transformation / process owner from wiki governance) + quarterly refresh from top PFR themes. |

---

## Relation to problem 1 (quality)

Improving templates **does not** fix “unknown standard path.” Fixing problem 2 **reduces load** on PMs and clarifies which items truly need richer narratives—so work on problem 1 becomes more focused later.

---

## Next step (for you)

Decide **where the gate lives** operationally:

- **A)** Only on the Azure DevOps Feature (after creation), or  
- **B)** In **CIM/ServiceNow before** the internal Feature exists (stronger for v2.0 consultant path), or  
- **C)** Both, with a copy-paste summary into DevOps.

Once you pick A/B/C, the same “Standard capability check” block can be pasted into wiki process text and CIM templates in a follow-up change.

---

**File:** `PFR skill/pfr_problem2_capability_knowledge_gap.md`  
**Last updated:** 2026-04-29
