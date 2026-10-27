# Process Framework – Wiki structure recommendation

## Summary

- **Landing page:** Create one **Process Framework** landing page that introduces the concept, value propositions, core components, and consumption models. Link to existing and new subpages where appropriate.
- **Subpages:** Use **one dedicated subpage for Process models** (functional description). **Keep Process Engine and BRE** as they are today (Process Engine already has its own module page; BRE as a section/link until it has a product page). **Do not** create separate subpages for “case templates” as a product; treat them as part of Process Framework / Process models content.

---

## 1. Landing page: Process Framework

**Suggested title:** `Process Framework` or `360° Process Framework` (align with naming of “360° Process Engine”).

**Content (aligned with existing module/product pages):**

- **Key info** – Part of Public 360°, version (6.7/6.8+), availability, Product Manager.
- **Product information** – Short intro, “What it is / What it is not”, **Individual Standard**, value propositions.
- **Core components** – Table with:
  - **Process Models** → link to subpage **Process Framework - Process models**.
  - **Process Engine** → link to existing **[[360° Process Engine]]**.
  - **Business Rules Engine (BRE)** → short text + link to Flexibility initiatives (or future BRE page).
- **Process model templates / case templates** – One short paragraph under Core components or Adoption accelerators (no separate product subpage).
- **Consumption and delivery models** – Brief overview (single process, framework, hosted, full platform).
- **Who this is for** – Target segments.
- **Product documentation** – Links to subpage, Process Engine, release info; placeholders for product sheets.
- **Right column** – Value proposition/selling points, implementation guidelines (when available), relevant links (Module overview, Process Engine, Public 360°, Product teams, SPOCs).

**Rationale:** One landing page gives a single entry point for “what is the Process Framework” and “how do the pieces fit together,” consistent with **Public 360°** and **360° Process Engine** product pages. The wiki already uses this pattern (Key info + Product information + Documentation from other units).

---

## 2. Should each component have its own subpage?

| Component | Recommendation | Reason |
|-----------|----------------|--------|
| **Process Models** | **Yes – one subpage** | There is a lot of functional content (stages, milestones, triggers, concurrency, tentative mode, configuration, publishing). A dedicated **Process Framework - Process models** page keeps the landing page readable and gives implementers/admins one place for “how process models work.” |
| **Process Engine** | **No new subpage – use existing** | **360° Process Engine** already has a full module page (product number, features, value prop, product sheets, technical docs). The Process Framework page should **link** to it as the execution component. Optionally add a short “Process Framework” note on the Process Engine page. |
| **Business Rules Engine (BRE)** | **No dedicated subpage for now** | BRE is referenced in Flexibility initiatives and roadmap; it may not yet have a product number or release. Keep a **section on the Process Framework landing page** and a link to [[Flexibility initiatives]]. When BRE is released and documented as a product, add a **Business Rules Engine** (or 360° BRE) module page and link from the Framework. |
| **Case templates / process model templates** | **No separate subpage** | These are “adoption accelerators” and building blocks (templates for process models and stages), not a separate product. Describe them in the **Process Framework** page (Core components / Adoption accelerators) and in **Process Framework - Process models** (configuration, stage templates). |

---

## 3. Suggested wiki page structure

```
Process Framework                    ← Landing page (concept, value prop, components, consumption)
├── Process Framework - Process models   ← Subpage (functional description: stages, milestones, triggers, config)
├── 360° Process Engine                 ← Existing module page (link from Framework)
├── Flexibility initiatives             ← Existing (link for BRE until BRE has its own page)
└── Public 360°                         ← Existing (parent product)
```

**Categories:** `[[Category:Product information]]`, `[[Category:360°]]` (and any existing product/module categories used by Enablement).

---

## 4. Module overview

On **Module overview**, consider adding an entry for **Process Framework** (or “Process Framework (process models, BRE, Process Engine)” if you want one line) in a suitable section (e.g. “Process library and Archiving by design” or a new “Process Framework” row), with Product Manager and SPOCs as for other modules. That way the Process Framework is discoverable next to 360° Process Engine and Process library modules.

---

## 5. Files created for you

- **Process_Framework_Wiki_Landing_Page.wikitext** – Full MediaWiki source for the Process Framework landing page. Copy into the wiki as the body of the page `Process Framework`.
- **Process_Framework_Process_Models_Subpage.wikitext** – MediaWiki source for the Process models subpage. Create the page `Process Framework - Process models` and paste this content.
- **Process_Framework_Wiki_Recommendation.md** – This recommendation (structure, subpages, Module overview).

After creating the two wiki pages, add the **Process Framework** link from **Public 360°** (e.g. under “Relevant links” or “Add-on modules”) and from **Module overview** as agreed with Enablement.
