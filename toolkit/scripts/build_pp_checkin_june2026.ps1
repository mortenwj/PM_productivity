# Build Process Platform June 2026 monthly check-in deck
$ErrorActionPreference = 'Stop'

$template = "C:\Users\MortenJensen\Brand Kit for Ai Agents\PPT template\Tieto presentation Template - Tieto Sans dynamic 2.pptx"
$output   = "C:\test\Process Platform check-in June 2026.pptx"
$work     = Join-Path $env:TEMP ("pp_checkin_" + [guid]::NewGuid().ToString() + ".pptx")

if (-not (Test-Path $template)) { throw "Template not found: $template" }
if (-not (Test-Path (Split-Path $output -Parent))) { New-Item -ItemType Directory -Path (Split-Path $output -Parent) -Force | Out-Null }

Copy-Item $template $work -Force
Set-ItemProperty -Path $work -Name IsReadOnly -Value $false

function Get-PlaceholderType($shape) {
    try { return [int]$shape.PlaceholderFormat.Type } catch { return -1 }
}

function Get-TextShapes($slide) {
    $shapes = @()
    foreach ($shape in $slide.Shapes) {
        if ($shape.HasTextFrame) { $shapes += $shape }
    }
    return $shapes
}

function Set-ShapeText($shape, [string]$text) {
    if ([string]::IsNullOrWhiteSpace($text)) { return }
    $shape.TextFrame.TextRange.Text = $text
}

function Set-CoverSlide($slide, [string]$title, [string]$subtitle, [string]$line3) {
    $titleSet = $false; $subtitleSet = $false; $line3Set = $false
    foreach ($shape in (Get-TextShapes $slide)) {
        switch (Get-PlaceholderType $shape) {
            3 { if (-not $titleSet) { Set-ShapeText $shape $title; $titleSet = $true } }
            4 { if (-not $subtitleSet) { Set-ShapeText $shape $subtitle; $subtitleSet = $true } }
            2 { if (-not $line3Set) { Set-ShapeText $shape $line3; $line3Set = $true } }
        }
    }
}

function Set-ContentSlide($slide, [string]$title, [string]$body) {
    $titleSet = $false; $bodySet = $false
    foreach ($shape in (Get-TextShapes $slide)) {
        $phType = Get-PlaceholderType $shape
        if (($phType -eq 1 -or $phType -eq 3) -and -not $titleSet) {
            Set-ShapeText $shape $title; $titleSet = $true; continue
        }
        if (($phType -eq 2 -or $phType -eq 7) -and -not $bodySet) {
            Set-ShapeText $shape $body; $bodySet = $true
        }
    }
    if (-not $titleSet -or -not $bodySet) {
        throw "Could not fill slide placeholders (title=$titleSet body=$bodySet) title=[$title]"
    }
}

function Set-TwoColumnSlide($slide, [string]$title, [string]$left, [string]$right) {
    $titleSet = $false
    $cols = New-Object System.Collections.Generic.List[object]
    foreach ($shape in (Get-TextShapes $slide)) {
        $phType = Get-PlaceholderType $shape
        if ($phType -eq 1 -and -not $titleSet) { Set-ShapeText $shape $title; $titleSet = $true; continue }
        if ($phType -eq 2) { [void]$cols.Add($shape) }
    }
    if ($cols.Count -lt 2) { throw "Two-column layout missing body placeholders for [$title]" }
    Set-ShapeText $cols[0] $left
    Set-ShapeText $cols[1] $right
}

function Set-ChapterSlide($slide, [string]$title, [string]$subtitle) {
    foreach ($shape in (Get-TextShapes $slide)) {
        if ((Get-PlaceholderType $shape) -eq 1) {
            if ($subtitle) { Set-ShapeText $shape ($title + "`r`n`r`n" + $subtitle) }
            else { Set-ShapeText $shape $title }
            return
        }
    }
}

function Add-Slide($pres, $spec) {
    $layout = $null
    foreach ($l in $pres.SlideMaster.CustomLayouts) {
        if ($l.Name -eq $spec.Layout) { $layout = $l; break }
    }
    if (-not $layout) { throw "Layout not found: $($spec.Layout)" }
    $slide = $pres.Slides.AddSlide($pres.Slides.Count + 1, $layout)
    switch ($spec.Kind) {
        'cover' { Set-CoverSlide $slide $spec.Title $spec.Subtitle $spec.Line3 }
        'two-column' { Set-TwoColumnSlide $slide $spec.Title $spec.BodyLeft $spec.BodyRight }
        'chapter' { Set-ChapterSlide $slide $spec.Title $spec.Body }
        default { Set-ContentSlide $slide $spec.Title $spec.Body }
    }
}

$slides = @(
    @{
        Kind = 'cover'; Layout = 'Cover page 1'
        Title = 'Process Platform'; Subtitle = 'Monthly check-in - June 2026'
        Line3 = 'Internal - Business Monitoring'
    }
    @{
        Layout = 'Content 3'; Title = 'Process Platform team - June status'
        Body = @"
Objective #1: Deliver stable, scalable 360 Flow (PAF)
Objective #2: Stabilize IFAR and prepare handover
Objective #3: Extend process modelling (web-based, rule-driven)

Status: O1 on track (6.10 pilot to GA path) | O2 ongoing | O3 starting (team ramp-up)

Focus this month
  6.10 Flow pilot - NVE + Copenhagen customer discovery
  GA roadmap draft (6.11 to 6.12)
  Web modelling team setup (Sumit, Anna, Bjorn)

Focus issues: IFAR capacity | portfolio gap vs customer expectation | delivery velocity
"@
    }
    @{
        Kind = 'two-column'; Layout = 'Two columns 1'; Title = 'Team objectives and OKRs 2026'
        BodyLeft = @"
O1: Production-grade Flow
  10+ customers in stable production
  50%+ implementations without core engineering

O2: IFAR handover ready
  Bug inflow under control

O3: Web modelling
  70%+ new models via web UI
  10 customers with own BREs
"@
        BodyRight = @"
OKR confidence (June)
  Flow: Medium-High
  IFAR: Low-Medium
  Modelling: Medium

Problems to solve
  1. Pilot to GA with NVE + Copenhagen learnings
  2. Portfolio/worklist gap vs customer expectation
  3. IFAR competing for same developers
"@
    }
    @{
        Kind = 'chapter'; Layout = 'Chapter 1'; Title = '360 Flow'; Body = '6.10 pilot status and path to GA'
    }
    @{
        Layout = 'Content 3'; Title = 'Flow release status - June 2026'
        Body = @"
6.10 pilot delivered - runtime ahead of portfolio and modelling maturity

Shipped: process models, progress plans, milestones, stages, ProcessView, building blocks
Transitional: document flow (legacy + React), localization (#420676)
Emerging: worklists, process-centric desktops (#411634, #414651)

Takeaway: execution core is real. Gap is operational maturity and GA enablers - not runtime feasibility.

Primary programme: NVE (#411612). Sentiment: positive but cautious.
"@
    }
    @{
        Kind = 'two-column'; Layout = 'Two columns 1'; Title = 'What Flow is - reframed after NVE'
        BodyLeft = @"
Execution
  Process models, activities, milestones, ProcessView

Visualization
  Overview columns: maps, deficiencies, decisions, checklists

Portfolio
  Manager queues, deadlines, phase status, desktops
"@
        BodyRight = @"
We undersold Flow internally
  Customers expect one story: desk to case

NVE signal
  Maps required for go-live
  P and B webparts assumed to be Flow
  Want more filtering, follow-ups, reporting

Direction: common repo for shared P and B + Flow assets
"@
    }
    @{
        Layout = 'Content 3'; Title = '6.10 focus and GA decision principles'
        Body = @"
Prioritize for 6.11+
  Runtime stability and NVE production readiness
  Lifecycle consistency, reusable flow blocks, governance
  NVE pilot feedback, Collect integration, async refresh

Deprioritize
  Broad feature expansion, advanced AI ambitions
  Large-scale modelling ambitions, broad UX redesign

When trade-offs arise: stability over flexibility; performance over new capability
"@
    }
    @{
        Kind = 'chapter'; Layout = 'Chapter 1'; Title = 'Customer discovery'; Body = 'Copenhagen 10 June 2026 - Nationalbanken, KK, Ankestyrelsen'
    }
    @{
        Layout = 'Content 3'; Title = 'Three discovery dialogues - not a pitch'
        Body = @"
Nationalbanken (central bank)
  Flagship: publication and approval workflows
  Wants visibility, traceability, predictability
  Start simple - Internal Audit workflow already works

Kobenhavns Kommune (5.5 yrs on 360, ~90 TB)
  Metadata quality at scale; centralized AI governance
  PE felt too hard - needed developers
  RPA delivers fast value

Ankestyrelsen (~60k cases/yr, 70 handlers)
  30 min manual QA per case; strong PE satisfaction
  #1 ask: AI on domestic cloud
  Building own tooling if we do not move
"@
    }
    @{
        Layout = 'Content 3'; Title = 'Cross-customer pattern'
        Body = @"
One pattern: manual checking and clicking - not deciding

AST: 30 min on every case - just checking documents before real work
AST: 1,100 templates - update one by one when something changes
NB: People work late - approvals in Excel across departments
KK: AI cites wrong legal paragraph - verification eats the savings
AST: Do you get help? - No. We live with it.

Synthesis: customers ready for AI in case work - we own the foundation; window to lead is now
"@
    }
    @{
        Kind = 'two-column'; Layout = 'Two columns 1'; Title = 'What they ask us to build'
        BodyLeft = @"
Automate case handling
  Auto-registration, QA, metadata, assignment

AI journalization and metadata
  Suggest metadata, assist archiving

Email to 360
  Transparent triage vs opaque routing

Publication workflows (NB)
  Multi-step approvals, deadlines, traceability
"@
        BodyRight = @"
AI for case workers
  Summaries, timelines, redaction, similar cases

Search across entities
  Limited today; GDPR constraints

Maps to our pillars
  Flow GA | BRE | Web modelling | Agentic AI | IFAR
"@
    }
    @{
        Layout = 'Content 3'; Title = 'Constraints - non-negotiable gates'
        Body = @"
Domestic-cloud AI - AST #1; NB data must not leave Denmark
Centralized AI governance - KK routes all LLM via one platform, legal sign-off
Accuracy you can trust - wrong legal paragraphs unacceptable
Auditability and equal treatment - full trails, defensible decisions
Accessibility - JAWS, screen readers (AST)
Change management - start one simple process, prove, then scale (NB)
"@
    }
    @{
        Kind = 'two-column'; Layout = 'Two columns 1'; Title = 'Foundation we can point to'
        BodyLeft = @"
SOLID - Foundation
  P360/eDoc case and document management

EXISTS - Automation
  AutoSaver, Process Engine, RPA, email archiving

PARTIAL - Self-service
  eManager, Template Connect - not bulk management
"@
        BodyRight = @"
MISSING - Intelligence
  AI journalization, semantic search, redaction
  Model orchestration, explainability

Flow message for check-in
  6.10 proved runtime execution
  Copenhagen proves next sale is maturity + intelligence on foundation
"@
    }
    @{
        Kind = 'chapter'; Layout = 'Chapter 1'; Title = 'High-level roadmap'; Body = 'Draft - June 2026'
    }
    @{
        Layout = 'Content 3'; Title = 'Roadmap overview - five pillars'
        Body = @"
1) Flow GA (6.11 to 6.12)
   Workunit registry, NVE feedback, Collect integration, monitoring, docs, triggers, refresh, templates, localization, background processes

2) Web-based process modelling (6.12, MVP stretch 6.11)
   Team: Sumit, Anna, Bjorn (architecture). NVE library MVP then GA

3) BRE
   MVP stretch 6.11: DMN on entity event + error + workunits
   GA V1 6.12; GA V2 meta pickers

4) Agentic AI vs Flow - positioning and guardrails

5) IFAR - bugs; eDoc journal notes (MJ + Brian)
"@
    }
    @{
        Kind = 'two-column'; Layout = 'Two columns 1'; Title = 'Flow GA and web modelling'
        BodyLeft = @"
Flow GA (6.11 to 6.12)
  Workunit registry
  NVE feedback (6.11)
  Collect integration - coordinate Integration Team
  Monitoring and statistics
  End-user and admin documentation
  Triggering system, async refresh (6.11)
  Process model templates (6.12)
  Localization, background processes
"@
        BodyRight = @"
Web modelling (6.12)
  MVP: diagram + execute NVE process library
  Represent NVE components, execution engine, storage
  Variables, import/export, code table pickers

GA: BL/oneliner, logging, validation, simulation
  Beyond 8 MVP components

KK validates: PE too hard for business users
"@
    }
    @{
        Kind = 'two-column'; Layout = 'Two columns 1'; Title = 'BRE, Agentic AI, and IFAR'
        BodyLeft = @"
BRE
  Flow = how work runs | BRE = when allowed/blocked
  MVP stretch 6.11: entity event, raise error, execute WU
  GA V1 6.12 + Search Assistant query builder
  GA V2: meta field pickers
  AST: forms automation, will share business rules

Agentic AI vs Flow
  Flow/BRE = structure and guardrails
  Intelligence layer on foundation - not 6.11 GA promise
  Domestic cloud and governance first
"@
        BodyRight = @"
IFAR
  1-2 devs constantly on bugs
  Handover to Transparency team
  eDoc journal notes - MJ coordinates with Brian

Customer link
  AST: heavy IFAR requests (object logs, activity)
  NB: traceability pillar
"@
    }
    @{
        Layout = 'Content 3'; Title = 'Priority sequence and four moves'
        Body = @"
Do first
  AI journalization and metadata (extend intake)
  Intelligent email triage (transparent rules)
  Publication workflow - NB beachhead on Internal Audit pattern

Strategic bets: AI case assistant | domestic cloud + governance | cross-system search
Defer: full self-service config UI

Four moves: (1) domestic cloud + AI governance (2) journalization prototype this quarter
(3) templates + NB publication flow (4) platform API + support
"@
    }
    @{
        Layout = 'Content 3'; Title = 'Current risks - June 2026'
        Body = @"
Disintermediation - AST building around 360 if we do not deliver API and workflows
Black-box automation - KPMG mailbox sorter; need transparent BRE + Flow triggers
Support = renewal - AST dissatisfaction regardless of roadmap
PE reputation - KK: too hard; web modelling + Tieto-led delivery until ready
NVE go-live - maps and portfolio gaps
IFAR capacity drain
AI oversell - constraints before capabilities in customer conversations
"@
    }
    @{
        Layout = 'Content 3'; Title = 'Issue list - June 2026'
        Body = @"
NVE go-live gaps (maps, portfolio) | Crit 4 | Prioritize 6.11 backlog
Process dev velocity vs GA | Crit 4 | Clarify assignments; senior backup
IFAR capacity | Crit 4 | Handover; eDoc journal notes scoped
Web modelling team ramp | Crit 3 | Sumit/Anna/Bjorn; MVP scope lock
Collect integration | Crit 3 | Integration Team coordination for 6.11
Documentation / GA readiness | Crit 3 | Module page, help, enablement
Copenhagen follow-up | Crit 3 | NB beachhead, AST rules review, KK process examples
"@
    }
    @{
        Layout = 'Content 3'; Title = 'Recommended next steps'
        Body = @"
Lock 6.11 Flow GA scope with Integration Team (Collect)
NVE map + overview acceptance test plan
ADO epic descriptions (#414623, #411612)
Web modelling MVP scope sign-off (8 components)
BRE MVP scope - entity event + error + WU execution
IFAR eDoc journal notes - MJ and Brian
Refresh weekly ADO pilot report
ProductPlan roadmap update from this draft
NB publication workflow proposal; AST business rules review
"@
    }
    @{
        Layout = 'Conclusion 1'; Title = 'Thank you'
        Body = @"
Sources: Flow_Pilot_Status_And_Learnings.md
Copenhagen customer meetings 10.06.2026
PP_Customer_Insight_Synthesis_10.06.2026.pptx
"@
    }
)

$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = -1
$pres = $pp.Presentations.Open($work, $false, $false, $false)
while ($pres.Slides.Count -gt 0) { $pres.Slides.Item(1).Delete() }

foreach ($s in $slides) { Add-Slide $pres $s }

try {
    $pres.SaveAs($output, 24)
    $saved = $output
} catch {
    $fallback = "C:\test\Process Platform check-in June 2026_regenerated.pptx"
    $pres.SaveAs($fallback, 24)
    $saved = $fallback
    Write-Warning "Original file in use. Saved to: $fallback"
}

$pres.Close()
$pp.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pres) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pp) | Out-Null
[GC]::Collect()
[GC]::WaitForPendingFinalizers()
Remove-Item $work -Force -ErrorAction SilentlyContinue

Write-Output "Created: $saved ($($slides.Count) slides)"
