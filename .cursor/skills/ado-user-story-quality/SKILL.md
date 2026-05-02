---
name: ado-user-story-quality
description: Evaluates Azure DevOps User Stories against the team quality policy (format, acceptance criteria, risk, parent links, scoring rubric), outputs structured JSON, and proposes field updates without applying them. Use when the user asks for story quality review, user story evaluation, sprint story compliance, Definition of Ready checks, or ADO story rubric scoring against story_eval policy.
---

# Azure DevOps user story quality (Cursor)

## Canonical policy

Full rules, rubric weights, and JSON schema text live in the repo:

- `story_eval/copilot-instructions.md`

Follow that document for **mandatory rules**, **scoring weights**, **compliance logic**, and **output shape**. This skill adds **Cursor + MCP-specific** steps only.

## MCP server

Use **`user-azure-devops`** (read MCP tool descriptors under `mcps/user-azure-devops/tools/` before calling tools). There is **no** GitHub Copilot-specific step in Cursor.

## Safety (non-negotiable)

- **Never** call `wit_update_work_item` or `wit_update_work_items_batch` unless the user explicitly approves (e.g. “Apply the patch now”, “Update work item 12345”).
- For improvements, show **`wit_update_work_item`**-style proposals: `{ "id": <number>, "updates": [ { "path": "/fields/...", "value": "..." } ] }` labeled **Proposed – do not execute unless approved**.
- **Saved queries:** **Do not** call `wit_get_query` until the user has **confirmed which query** (path or ID) to use.

## How to retrieve stories (pick one path)

### A) Saved query

1. **Confirm** with the user: project name, and query **path** (e.g. `Shared Queries/...`) or query **GUID**.
2. **`wit_get_query`** — `project`, `query` — returns the query definition (e.g. WIQL). Note the query **`id`** if you need it for step 3.
3. **`wit_get_query_results_by_id`** — **`id`**: the saved query’s **id** (string). Optional: `project`, `team`, `top` (default 50), **`responseType`**: `ids` to reduce payload, then hydrate with batch; or `full` if the API returns enough fields for evaluation.
4. If you only have **IDs**, call **`wit_get_work_items_batch_by_ids`** (see fields below). Chunk IDs if the batch is large (typical limit **200** per batch).

### B) Current sprint / iteration

1. Confirm **project** and **team** with the user if unknown.
2. **`work_list_team_iterations`** — `timeframe`: `current`, plus `project`, `team` — resolve the **iteration** identifier returned by the API.
3. **`wit_get_work_items_for_iteration`** — `project`, `team` (if needed), **`iterationId`** (string from step 2).
4. Hydrate or enrich with **`wit_get_work_items_batch_by_ids`** as needed.

### C) Ad hoc list

- User supplies work item IDs → **`wit_get_work_items_batch_by_ids`** only.

### D) Assigned to me / my activity (narrow scope)

- **`wit_my_work_items`** — `project`, optional `type`: `assignedtome` | `myactivity`, `top`, `includeCompleted` — then filter to User Stories and batch-fetch full fields if required.

## Fields to request (batch)

Pass explicit **`fields`** to `wit_get_work_items_batch_by_ids` (and `wit_get_work_item` when needed), for example:

- `System.Id`, `System.Title`, `System.WorkItemType`, `System.State`
- `System.Description`, `System.Parent`
- `Microsoft.VSTS.Common.AcceptanceCriteria`
- `System.IterationPath`, `System.AreaPath`
- **Risk (verified on project `360`, work item type User Story):**
  - **`Microsoft.VSTS.Common.Risk`** — API reference name for the field labeled **Risk** (not `Common.Risk`; that ref does **not** exist and returns TF51535).
  - **`Custom.Riskdescription`** — separate field **Risk description** (HTML/text). Use for policy checks when risk level requires narrative (per `story_eval/copilot-instructions.md`).
- Unset fields may be **omitted** from batch responses; treat missing Risk as unset.

### If another project/process differs

Call **`wit_get_work_item_type`** with `project` and `workItemType` (e.g. `User Story`) and search the returned field list for **`name`: "Risk"** to read the correct **`referenceName`**.

## Parent links and dependencies

- **`wit_get_work_items_batch_by_ids`** may **not** return **relations**. To verify **Parent → Feature/Epic** or **Dependency** links, use **`wit_get_work_item`** with **`expand`: `relations`** (and `fields` as needed) for stories that require link evidence, or sample critical items if volume is high.
- Relation types are in API `relations[].attributes.name` / URL; map to policy (parent hierarchy vs dependency).

## Evaluation steps

1. Load policy + rubric from `story_eval/copilot-instructions.md`.
2. Retrieve work items via an allowed MCP path above.
3. Score each **User Story** (and Tech/Enabler per title prefix rules) per dimensions and weights in the policy.
4. Emit **one JSON document** matching the **Required JSON Output Schema** in `story_eval/copilot-instructions.md` (`evaluatedAt`, `stories[]`, `aggregateSummary`).
5. If **`complianceStatus`** is **Non-Compliant** (including any mandatory dimension at 0 per policy), list **`issues`** and **`rewriteSuggestions`**.
6. Optionally save JSON to **`story_eval/story-eval.json`** (or user-specified path). If **`tools/reports/StoryQualityReport.ps1`** exists, the user may run it locally; **do not assume** the script exists in this repo.

## Proposed updates shape (MCP)

`wit_update_work_item` expects **`updates`**: array of `{ "path": "/fields/<FieldReferenceName>", "value": "<string>" }` (and optionally `"op"` per tool defaults).

Examples (illustrative only):

- Title: `/fields/System.Title`
- Description (HTML or plain per org): `/fields/System.Description`
- Acceptance criteria: `/fields/Microsoft.VSTS.Common.AcceptanceCriteria`
- Risk level: `/fields/Microsoft.VSTS.Common.Risk` (value must match process; policy expects `1`–`3` where applicable)
- Risk description: `/fields/Custom.Riskdescription`

Always mark proposals in chat as **not executed**.

## When fields or queries fail

- If **`Microsoft.VSTS.Common.Risk`** fails with TF51535, the process template likely differs — use **`wit_get_work_item_type`** to resolve the reference name for the **Risk** field.
- If **`wit_get_query_results_by_id`** returns truncated results, increase **`top`** in reasonable steps or paginate using query/WIQL strategies the user approves.

## Related repo files

- `story_eval/copilot-instructions.md` — full product policy, rubric, JSON schema, sample prompts

### Local evaluation script (no MCP)

`story_eval/run_story_quality_eval.py` scores stories from cached merge JSON or **live from Azure DevOps**:

- **`--fetch`** with one or more **`--id`** — calls the REST **workitemsbatch** API for the latest revision (same field set as batch MCP). Does **not** require `_merged_pp22_batches.json` for those IDs.
- **Authentication:** set **`AZURE_DEVOPS_PAT`** or **`ADO_PAT`** to a PAT with **Work Items (Read)** (organization default **`--organization tieto-si`**, project **`--project 360`**).
- Parent Feature/Epic types: uses `_parent_types_pp22.json` when present, then **hydrates missing parents** via a second batch call when using **`--fetch`**.
