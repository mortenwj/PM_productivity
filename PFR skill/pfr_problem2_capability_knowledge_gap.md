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

## Decision: enforce the gate in **Azure DevOps**

The **Product First Request Feature** on the PFR board is the **system of record** for the capability gate. CIM/ServiceNow may still be where the need first appears; the **completed check and evidence live on the Feature** (not only in email or the external ticket).

**Definition of Ready (suggested):** A Feature is not ready for PM “evaluation / conclusion” work until the **Standard capability check** block is present and complete. Items created by automation (e.g. from ServiceNow) should get the block **filled by the accountable role** as the first human edit after creation.

---

## Practical interventions (ordered by leverage)

### 1. Mandatory block on the DevOps Feature (primary enforcement)

On **every** PFR Feature, include a clearly titled section in **Description** (top or directly under the template), for example:

**Standard capability check**

| Subfield | Content |
|----------|--------|
| **Outcome** | One of: Already supported \| Config / extension only \| Partially supported \| Not supported (product gap) |
| **Evidence** | Links or pointers: wiki, release note, module overview, existing PFR, demo env, screenshot |
| **Checked by** | Name (role) |
| **Date** | YYYY-MM-DD |

- **Owner:** Solution consultant (functional) or Technical Consulting (technical), per existing RACI on [[Product first - Request new functionality]].  
- **If outcome is Already supported or Config-only:** close or redirect the Feature with a short **Conclusion** (and customer communication per wiki when the request was customer-driven)—do not leave it open as an undifferentiated “new functionality” item unless you explicitly want a UX/product polish PFR.

Optional: add a work item **tag** for quick filtering, e.g. `CapabilityCheck-Standard`, `CapabilityCheck-Config`, `CapabilityCheck-Partial`, `CapabilityCheck-Gap`, until a custom field exists.

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

### 5. Later: custom field on the Feature type (optional)

When process maturity warrants it, add a dedicated Azure DevOps field (e.g. **Capability check outcome**) for WIQL dashboards. Until then, the **Description block + optional tags** above are enough to enforce and query the gate in DevOps.

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

## Next steps (process rollout)

1. Update the **PFR Feature template** in Azure DevOps so the **Standard capability check** block is part of the default Description (reporters fill it in at creation or immediately after).  
2. Update the **wiki** [[Product first - Request new functionality]] “Report request” activity to state that the gate is **recorded on the DevOps Feature** and is **Definition of Ready** before PM evaluation.  
3. Align board / query views so PMs can filter or sort on “missing capability check” if needed (e.g. empty section or absence of outcome tag).

---

**AI-assisted execution:** The Cursor project skill **`.cursor/skills/pfr-ai-capability-check/SKILL.md`** implements this gate by fetching the Feature from Azure DevOps, grounding on the wiki via MCP, and emitting a paste-ready **Standard capability check** block plus structured JSON. **Evidence tiers (T1–T4)** and credibility rules: `PFR skill/pfr_evidence_sources_credibility.md`. Folder overview: `PFR skill/README.md`.

---

**File:** `PFR skill/pfr_problem2_capability_knowledge_gap.md`  
**Last updated:** 2026-04-29
