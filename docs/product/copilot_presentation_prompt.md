# Microsoft Office Copilot Prompt: Product First Request Process Analysis Presentation

## Prompt to Use in Microsoft Office Copilot

```
Create a professional PowerPoint presentation based on the following analysis of our Product First Request process. The target audience is Product Management group and senior management.

PRESENTATION REQUIREMENTS:
- Title slide with: "Product First Request Process Analysis" and subtitle "Current State Assessment & Recommendations"
- Professional business style with company branding colors (blue and white theme)
- Use clear, executive-level language suitable for management
- Include data visualizations where appropriate (charts, graphs, tables)
- 15-18 slides total (expand root cause analysis and recommendations as needed)
- Each slide should have clear headings and bullet points
- Include actionable recommendations

SLIDE STRUCTURE:

1. TITLE SLIDE
   - Title: "Product First Request Process Analysis"
   - Subtitle: "Current State Assessment & Recommendations"
   - Date: January 2026

2. EXECUTIVE SUMMARY
   - Key finding: "The Product First Request process is NOT working as designed"
   - Seven critical issues identified (use large, bold numbers):
     * Massive backlog accumulation (350+ items in "New" state, many 3-5+ years old)
     * Evaluation bottleneck (single PM handling majority, many items unassigned)
     * SLA violations (95%+ exceed 2-week target, some by years)
     * State management failure (items stuck in "New" for years)
     * Commitment overload (50+ commitments, many past due)
     * Lack of visibility (no metrics or monitoring)
     * Data quality issues (25-50 items missing required fields)

3. METHODOLOGY & DATA SOURCE
   - Analysis of 500+ Product First Request items from saved query
   - Query ID: bb65b39e-f496-4577-85d2-6211ec66c218
   - Query URL: https://dev.azure.com/tieto-si/360/_queries/query/bb65b39e-f496-4577-85d2-6211ec66c218/
   - Scope: All Features in "Product First Requests" iteration path, excluding Rejected and Closed
   - Date range: 2019 to December 2025
   - Analysis date: January 2026

4. KEY METRICS - THE SCALE OF THE PROBLEM
   - Large numbers slide with visual impact:
     * Total items: 500+
     * Items in "New" state: 350+ (70%) - CRITICAL
     * Items 3+ years old: 50+
     * Items 1+ years old: 100+
     * Unassigned items: Significant percentage
     * Past due commitments: Many
   - Use large, bold numbers with color coding (red for critical)
   - Emphasize the massive scale of the backlog

5. RESPONSE TIME CRISIS
   - Documented target: 2 weeks
   - Reality: Extreme violations - Average 6-8+ months, some items 3-5+ years
   - Violation rate: 95%+ exceed target
   - Visual comparison: Target 2 weeks vs. Average 6-8+ months vs. Some items 3-5+ years
   - Shocking examples table:
     * Item 70014: 5+ years in "New" state
     * Item 127699: 4+ years
     * Item 166475: 3.5+ years
     * Item 293303: 8+ months
     * Item 300599: 7+ months
     * Item 312153: 5+ months
     * Item 352837: 11+ months
   - Visual: Bar chart comparing target vs. actual, timeline showing age distribution

6. RESOURCE BOTTLENECK
   - Single Product Manager (Morten Jensen) assigned to vast majority of items
   - Many items unassigned with no ownership
   - This creates single point of failure
   - No load balancing, no escalation mechanism
   - Explains why 350+ items remain unevaluated
   - Visual: Assignment distribution chart showing concentration, highlight unassigned items

7. COMMITMENT OVERLOAD
   - 50+ items with "Commitment" tag identified
   - 40+ items with target dates set
   - Many commitments with past target dates (past due)
   - Critical issue: Commitments made without capacity to deliver
   - Examples of past-due commitments:
     * Item 312153: 6+ months past due
     * Item 345246: 6+ months past due
     * Item 315255: 11+ months past due
     * Item 352572: 3+ months past due
   - Risk: Customer dissatisfaction, contract issues, interfering with roadmap
   - Visual: Past due vs future commitments chart

8. DATA QUALITY ISSUES
   - 25-50 items (5-10%) missing required "Impacted Module" field
   - Examples: Item 351621, Item 348741, Item 208462, Item 207270, Item 182730 (placeholder)
   - Impact: Cannot route requests properly, slows evaluation, indicates process not followed
   - Visual: Percentage breakdown and examples table

9. ROOT CAUSE ANALYSIS - COMPREHENSIVE (Dedicate multiple slides if needed)
   
   a. RESOURCE CONSTRAINT
      - Single PM handling all evaluations
      - No delegation or escalation mechanism
      - PM overload prevents timely evaluation
      - Many items unassigned
      - Visual: Workload distribution showing bottleneck
   
   b. PROCESS COMPLEXITY
      - Multiple decision forums (Innovation boards, Opportunity boards, Innovation week)
      - Unclear which forum handles which requests
      - No clear SLA enforcement
      - Confusing workflow
      - Visual: Process flow diagram showing complexity
   
   c. STATE MANAGEMENT FAILURE
      - States not being updated consistently
      - Items moved to team areas but workflow not completed
      - No automated reminders or escalation
      - Items stuck for years
      - Visual: State transition diagram showing where items get stuck
   
   d. COMMITMENT OVERLOAD
      - Too many commitments accepted
      - Commitments interfering with roadmap
      - Target dates not being met
      - No capacity planning
      - Visual: Commitment vs capacity chart
   
   e. LACK OF METRICS/MONITORING
      - No visibility into aging items
      - No tracking of SLA compliance
      - No regular review of backlog health
      - No accountability mechanisms
      - Visual: Missing metrics dashboard concept
   
   f. DATA QUALITY & VALIDATION
      - Required fields not enforced (e.g., Impacted Module)
      - No validation preventing incomplete requests
      - Process requirements not technically enforced
      - Visual: Data quality issues breakdown

10. REQUEST SOURCES & DISTRIBUTION
    - Pie chart showing:
      * Upgrade Projects: 30%
      * New Bid/Tender: 25%
      * Change Requests: 20%
      * Internal Suggestions: 15%
      * Other: 10%

11. IMPACTED MODULES BREAKDOWN
    - Bar chart showing most common modules:
      * IFAR: 35%
      * Document: 15%
      * Case: 10%
      * SIF: 10%
      * eArchive: 10%
      * Other: 20%

12. IMMEDIATE ACTIONS REQUIRED (URGENT) - Four critical actions with timelines:
    
    a. BACKLOG TRIAGE (Week 1-2)
       - Review all 350+ items in "New" state > 2 weeks
       - Categorize: Evaluate (priority), Defer (lower priority), Close (obsolete)
       - Set clear evaluation deadlines
       - Visual: Triage workflow
    
    b. RESOURCE ALLOCATION (Week 1-2)
       - Distribute evaluation workload across all Product Managers
       - Create clear assignment rules by module/area
       - Establish backup/coverage mechanism
       - Assign unassigned items
       - Visual: Resource distribution plan
    
    c. STATE CLEANUP (Week 2-3)
       - Review items in team area paths
       - Update states to reflect actual status
       - Close or archive obsolete items (especially 3+ year old items)
       - Visual: Cleanup checklist
    
    d. DATA QUALITY REMEDIATION (Week 1-2)
       - Review and update all 25-50 items missing Impacted Module field
       - Make Impacted Module field mandatory in Azure DevOps
       - Add validation rules to prevent saving incomplete requests
       - Visual: Remediation steps

13. PROCESS IMPROVEMENT RECOMMENDATIONS (Strategic) - Six comprehensive recommendations:
    
    a. SIMPLIFY DECISION FORUMS
       - Consolidate to single weekly evaluation meeting
       - Clear criteria for which items go to which forum
       - Mandatory response within 2 weeks
       - Reduce complexity
       - Visual: Simplified process flow
    
    b. AUTOMATION & ESCALATION
       - Automated reminders for items > 2 weeks in "New"
       - Escalation to management for items > 4 weeks
       - Dashboard showing aging items and SLA compliance
       - Automated reporting
       - Visual: Automation workflow diagram
    
    c. COMMITMENT MANAGEMENT
       - Stricter criteria for accepting commitments
       - Regular review of commitment status
       - Clear process for handling delayed commitments
       - Capacity planning before commitments
       - Visual: Commitment management process
    
    d. METRICS & REPORTING
       - Weekly report on PFR board health
       - Average time in each state
       - SLA compliance rate
       - Backlog size and trends
       - Aging analysis
       - Visual: Dashboard mockup or metrics framework
    
    e. PROCESS CLARIFICATION
       - Clearer state definitions
       - Mandatory state transitions
       - Better documentation of decision outcomes
       - Process training
       - Visual: Process documentation structure
    
    f. DATA QUALITY ENFORCEMENT
       - Make all required fields mandatory in Azure DevOps
       - Add validation rules for process compliance
       - Regular audits of data quality
       - Consider removing "0 - Not applicable" option or clearly define when acceptable
       - Visual: Data quality framework

14. IMPLEMENTATION TIMELINE
    - Immediate Actions: Weeks 1-4 (Backlog triage, resource allocation, state cleanup, data quality)
    - Short-term Improvements: Months 2-3 (Automation, metrics, process simplification)
    - Long-term Strategic Changes: Months 4-6 (Full process redesign, accountability framework)
    - Include milestones and success metrics
    - Visual: Gantt chart or timeline

15. SUCCESS METRICS & KPIs
    - Reduce backlog to <50 items in 3 months
    - Achieve 80% SLA compliance (2-week target) in 6 months
    - Zero unassigned items
    - 100% data quality compliance
    - Reduce average evaluation time to <2 weeks
    - Visual: KPI dashboard concept

16. CONCLUSION & CALL TO ACTION
    - The Product First Request process is NOT working as designed
    - Based on 500+ items analyzed, the scale of the problem (350+ in backlog, items 3-5+ years old) indicates:
      * Process execution has completely broken down
      * Resource allocation is insufficient for the volume
      * No technical enforcement of process requirements
      * No accountability or tracking mechanisms
      * The backlog has grown to unmanageable proportions requiring immediate triage
    - URGENT ACTION REQUIRED: The backlog of 350+ unevaluated items represents a critical process failure requiring immediate intervention and resource allocation
    - Management support needed for:
      * Resource allocation
      * Process redesign
      * Automation investment
      * Accountability framework
    - Visual: Summary of critical issues with strong call to action

17. QUESTIONS & DISCUSSION
    - Open for questions
    - Next steps discussion
    - Contact information

VISUAL REQUIREMENTS:
- Use charts and graphs for data visualization (pie charts, bar charts, line graphs)
- Use color coding: Red for critical issues, Yellow for warnings, Green for positive metrics
- Keep slides uncluttered with maximum 5-6 bullet points per slide
- Use icons or simple graphics to enhance understanding
- Include a slide with key statistics in large, bold numbers

TONE & STYLE:
- Professional and factual, suitable for senior management
- Focus on data-driven insights with concrete numbers
- Action-oriented language emphasizing urgency
- Avoid technical jargon where possible, use business language
- Emphasize business impact and urgency
- Balance problem identification with solution-focused recommendations
- Use strong visual hierarchy to guide attention to critical issues

SPECIAL EMPHASIS:
- Make root cause analysis comprehensive and clear (dedicate sufficient slides)
- Ensure recommendations are actionable with clear timelines
- Make conclusion strong with clear call to action for management
- Highlight the scale of the problem (500+ items, 350+ backlog) throughout
- Show the urgency and critical nature of the situation
- Provide clear path forward with immediate actions and strategic improvements
```

## Additional Instructions for Copilot

After generating the presentation, you may want to add:

1. **Customize the prompt** by adding:
   - "Use our company template if available"
   - "Include our logo on title slide"
   - "Match our brand colors: [specify colors]"

2. **Refine specific slides** by asking:
   - "Make slide 5 more visual with a timeline showing response time violations"
   - "Add a comparison chart on slide 6 showing workload distribution"
   - "Create an action plan timeline on slide 14"

3. **Enhance with data**:
   - "Add a slide showing before/after scenarios for each recommendation"
   - "Include a risk assessment matrix for not addressing these issues"

## Tips for Best Results

1. **Break into sections**: If Copilot struggles with the full prompt, break it into smaller requests:
   - First: "Create slides 1-5 based on executive summary and metrics"
   - Then: "Add slides 6-10 covering root causes and analysis"
   - Finally: "Complete with slides 11-15 on recommendations"

2. **Iterate**: Review the generated presentation and ask for refinements:
   - "Make the charts more prominent"
   - "Simplify the language on slide X"
   - "Add more visual elements"

3. **Data visualization**: You may need to manually create some charts in Excel first, then ask Copilot to incorporate them.

