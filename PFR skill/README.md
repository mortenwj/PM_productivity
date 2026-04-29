# PFR skill (repo folder)

This folder holds **artifacts and specs** for improving the **Product First Request (PFR)** process for Public 360°.

## Primary focus: AI-assisted capability check

The main direction is **automatic (AI-assisted) screening** so every PFR Feature gets a **Standard capability check** before PM time: determine whether the need is *already supported*, *configurable*, *partially supported*, or a *true product gap*, with **evidence** and **confidence**.

- **Gate enforcement location:** Azure DevOps (Feature on the Product First Requests board).  
- **Concept and rules:** `pfr_problem2_capability_knowledge_gap.md`  
- **How Cursor agents should run the check:** project skill **`.cursor/skills/pfr-ai-capability-check/SKILL.md`**

## Other files in this folder

| File | Role |
|------|------|
| `wiki_investigation_product_first_request.md` | Wiki process summary (MediaWiki). |
| `ado_pfr_sample_40_analysis.md` | Sample ADO analysis (40 Features). |
| `.gitkeep` | Keeps empty paths in git if needed. |

Problem 1 (request **quality** and consistency) is out of scope for the **first** iteration of this skill; capability discovery comes first.
