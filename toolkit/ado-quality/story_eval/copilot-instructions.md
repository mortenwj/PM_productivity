# Copilot Instructions – User Story Quality Enforcement for Azure DevOps

This repository uses GitHub Copilot together with the Azure DevOps MCP server. Copilot must evaluate and improve the quality of Azure DevOps user stories according to our internal product policy and industry best practices.

Copilot should follow the rules, scoring rubric, and safety guidelines in this document whenever interacting with Azure DevOps work items.

---

## 🎯 Purpose

To ensure every user story in Azure DevOps is:
- Well-structured
- Testable
- Business-value oriented
- Risk-aware
- Aligned with agile delivery standards
- Ready for implementation within a sprint

Copilot must:
1. Retrieve user stories from Azure DevOps using MCP tools
2. Evaluate them using the **scoring rubric**
3. Output a structured **quality report in JSON**
4. Propose improved story and acceptance criteria text where needed
5. Only propose fixes – **never automatically execute updates**

---

## 🔒 Governance & Safety Rules (Non-Negotiable)

- Copilot **must not automatically update or modify Azure DevOps work items**.
- When recommending improvements, Copilot should:
  1. Generate proposed updates as **JSON Patch objects** (for the `wit_update_work_item` tool).
  2. Clearly label all updates as **"Proposed – do not execute unless explicitly approved."**
- Only execute updates when the user explicitly instructs with wording such as:
  **“Apply the patch now”** or **“Execute the patch for work item 12345.”**
- If a story is non-compliant or below threshold, Copilot must recommend changes, not apply them.

- Copilot must always ask the user which saved query they want to evaluate before invoking any saved-query retrieval operation. This is mandatory: do not run `wit_get_query` without explicit user selection of the saved query.

---

## 🔧 Azure DevOps Field Mapping

| Business Concept         | Azure DevOps Field Reference         | Type    | Allowed Values / Notes                                   |
|-------------------------|--------------------------------------|---------|----------------------------------------------------------|
| **Risk Classification** | `Microsoft.VSTS.Common.Risk` (field label **Risk**) | Integer | Must be set to `1`, `2`, or `3` (mandatory). Note: `Common.Risk` is not a valid reference — use the full name. |
| **Risk Description**    | `Custom.Riskdescription` (field label **Risk description**), and/or narrative in Description | Text | Mandatory if Risk = 1 or 2                               |
| **Acceptance Criteria** | `System.Description` and/or custom AC field | Text | Copilot must parse and validate from either location     |
| **Parent Link**         | `System.LinkTypes.Hierarchy-Reverse` | Link    | Must be linked to a Feature or Epic                      |
| **Dependencies**        | `System.LinkTypes.Dependency`        | Link    | Recommended when applicable                              |

---

## 🧭 Story Types & Valid Formats

| Story Type             | Identification                                 | Required Story Format                                                                 |
|------------------------|-------------------------------------------------|----------------------------------------------------------------------------------------|
| **Standard User Story** | Title does **not** start with `[Tech]` or `[Enabler]` | Must follow classic format:<br>**“As a `<role>`, I want `<capability>`, so that `<benefit>`”** |
| **Exception Story**   | Title **starts with** `[Tech]` or `[Enabler]`    | May use technical language, but must still describe outcome and include structured AC |

---

## ✅ Mandatory Rules for Quality Compliance

1. **Story Format** – Classic format is mandatory unless title begins with `[Tech]` or `[Enabler]`.
2. **Acceptance Criteria Format**:
   - Standard stories → **Gherkin format required** (Given / When / Then).
   - `[Tech]` / `[Enabler]` → **Structured bullet format** starting with:
     - “The system must…”
     - “This solution shall…”
3. **Risk Classification (`Risk`)** – Must be 1, 2, or 3 (mandatory).
4. **Risk Description** – Mandatory if Risk = 1 or 2. Must clearly describe risk/impact.
5. **Story Size** – Must be deliverable in one sprint. Epic-sized or vague stories are non-compliant.
6. **Business Value** – Must be clearly expressed in the “so that…” clause.
7. **Parent Link** – Must be linked to a Feature or Epic.
8. **NFR Consideration** – Required only if the story has performance, security, accessibility, availability, or similar impact.
9. **Dependencies** – Recommended when applicable (not mandatory, but evaluated for coaching).

---

## ⚖ Scoring Rubric & Weights (Final Score = 0–100)

| Dimension                  | Weight  |
|---------------------------|---------|
| Story Format              | 15%     |
| Acceptance Criteria Format| 12.5%   |
| Acceptance Testability    | 12.5%   |
| Risk Classification       | 10%     |
| Risk Description          | 5%      |
| Story Size                | 15%     |
| Business Value            | 15%     |
| NFR Consideration         | 5%      |
| Parent Link               | 5%      |
| Dependencies              | *Coaching only – not included in compliance score* |

**Compliance Rule:**  
If any mandatory dimension scores **0**, set:
```
"complianceStatus": "Non-Compliant"
```
Even if weighted FinalScore > 0.

---

## 🚀 Approved Usage Prompts

```markdown
### 🔷 Evaluate current sprint
Use ADO tools to retrieve all User Stories in iteration `{IterationPath}`. Evaluate using the policy in this file and return the JSON structure defined above.

### 🔷 Evaluate a saved query
Run `wit_get_query` on `{QueryPath}`, retrieve work items, and evaluate each using the rubric defined here.

Note: Copilot must **always ask the user to confirm which saved query** to evaluate before running `wit_get_query`.

### 🔷 Suggest improvements
For each Non-Compliant story, provide a rewritten story and acceptance criteria that fully meet this quality policy.

### 🔷 Generate update proposals
Provide `wit_update_work_item` JSON patch proposals to correct the Risk field, parent link, or acceptance criteria. Do not execute unless I explicitly approve.

### 🔷 Generate the report
Save the evaluation JSON as story-eval.json at the repo root.
Run:
"C:\Program Files\PowerShell\7\pwsh.exe" -File .\tools\reports\StoryQualityReport.ps1 -InputJsonPath .\story-eval.json
Return the generated filename and the first 50 lines so I can preview the report.
```

---

## 📚 Additional Guidance for Copilot’s Reasoning

```markdown
- Use INVEST principles to assess story quality.
- Apply IEEE 29148 standards for clarity and testability.
- Flag ambiguity such as: “optimize,” “improve,” “and/or,” “etc.”
- Detect oversized stories by:
  - Multiple outcomes or personas
  - Excessive unrelated acceptance criteria
- Ensure Risk = 1 or 2 always has a meaningful description.
- Detect if NFRs are relevant (external user, performance impact, security-sensitive data, public accessibility, etc.).
- Dependencies should be suggested if another story or technical prerequisite is implied.
```

---

## 📤 Required JSON Output Schema (Final Output Format – Must Be Used After Applying All Rules Above)

```json
{
  "evaluatedAt": "<ISO datetime>",
  "stories": [
    {
      "id": 0,
      "title": "",
      "type": "User Story | Tech | Enabler",
      "hasParentFeatureOrEpic": true,
      "riskClassification": 1,
      "riskDescriptionPresent": true,
      "dimensions": {
        "storyFormat": 0,
        "acFormat": 0,
        "acTestability": 0,
        "riskClassification": 0,
        "riskDescription": 0,
        "storySize": 0,
        "businessValue": 0,
        "nfrConsideration": 0,
        "parentLink": 0,
        "dependencies": 0
      },
      "finalScore": 0,
      "complianceStatus": "Compliant",
      "issues": ["..."],
      "rewriteSuggestions": {
        "story": "As a <role>...",
        "acceptanceCriteria": "GIVEN ... WHEN ... THEN ..."
      }
    }
  ],
  "aggregateSummary": {
    "count": 0,
    "avgFinalScore": 0,
    "nonCompliantCount": 0,
    "topSystemicIssues": ["..."],
    "quickWins": ["..."]
  }
}
```

---

**End of Instructions**
