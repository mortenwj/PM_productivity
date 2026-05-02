# Context Assembly

Reusable context packet that the **lmwtfy** skill loads before doing research.

## product-context

**Canonical definition:** the **`profile:code-first-research`** packet lives in the shared layer:

- **[`shared/evidence/profiles/code-first-research.md`](../../shared/evidence/profiles/code-first-research.md)** — source order, `gh` patterns, Ratatoskr / ADO / wiki steps, extract list, conflict resolution (**code wins**).

Supporting mechanics (read as needed for the same run):

- **[`shared/evidence/README.md`](../../shared/evidence/README.md)** — index and precedence note  
- **[`shared/evidence/evidence-playbook.md`](../../shared/evidence/evidence-playbook.md)** — claims, evidence types, confidence, stop rules, conflicts  
- **[`shared/evidence/budgets.md`](../../shared/evidence/budgets.md)** — default call caps for wiki, help, ADO, code  
- **[`shared/evidence/ratatoskr-preflight.md`](../../shared/evidence/ratatoskr-preflight.md)** — DNS / preflight / fallbacks  
- **[`shared/evidence/sources-and-tools.md`](../../shared/evidence/sources-and-tools.md)** — MCP hygiene, repos  
- **[`shared/evidence/verification-and-leads.md`](../../shared/evidence/verification-and-leads.md)** — leads vs verified reads  

## How the skill references this packet

The **`lmwtfy`** `SKILL.md` refers to **`profile:code-first-research`** by name. Skills can load the packet **partially** (for example, skip DevOps if the question has no work item reference).

## Rules

- The packet is documentation, not code. The agent reads the packet definition and follows it. There is no runtime framework.
- When shared retrieval docs change (new source, extraction logic), update **`../../shared/evidence/`** and keep this file’s links current.
