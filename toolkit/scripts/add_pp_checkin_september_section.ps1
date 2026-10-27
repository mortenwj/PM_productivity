# Add September 2026 section to Process Platform check-in deck.
# Inserts September before August (latest first). Preserves August, May, March unchanged.
$ErrorActionPreference = 'Stop'

$source = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026.pptx'
$output = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_updated.pptx'
$work   = Join-Path $env:TEMP ("pp_checkin_sep_section_" + [guid]::NewGuid().ToString() + ".pptx")
$insertAfterSlide = 5   # after IFAR intro; before August (latest month first)

if (-not (Test-Path $source)) { throw "Source deck not found: $source" }

Copy-Item $source $work -Force
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
    if ($null -eq $text) { return }
    $shape.TextFrame.TextRange.Text = $text
}

function Set-CoverSubtitle($slide, [string]$subtitle) {
    foreach ($shape in (Get-TextShapes $slide)) {
        if ((Get-PlaceholderType $shape) -eq 4) {
            Set-ShapeText $shape $subtitle
            return
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

function Set-TableCellText {
    param($Cell, [Parameter(Mandatory)][string]$Text)
    $tr = $Cell.Shape.TextFrame.TextRange
    $tr.Text = $Text
    $tr.ParagraphFormat.Bullet.Type = 0   # ppBulletNone
    $tr.ParagraphFormat.SpaceAfter = 0
    $tr.ParagraphFormat.SpaceBefore = 0
}
function Set-TableSlide($slide, [string]$title, [string[]]$headers, [object[]]$rows) {
    $titleSet = $false
    $bodyLeft = 36; $bodyTop = 100; $bodyWidth = 648; $bodyHeight = 320
    foreach ($shape in @($slide.Shapes)) {
        if ($shape.HasTable) { $shape.Delete() }
    }
    foreach ($shape in $slide.Shapes) {
        if ($shape.HasTable) { continue }
        $phType = Get-PlaceholderType $shape
        if (($phType -eq 1 -or $phType -eq 3) -and -not $titleSet) {
            Set-ShapeText $shape $title
            $titleSet = $true
            continue
        }
        if ($phType -eq 2 -or $phType -eq 7) {
            $bodyLeft = $shape.Left
            $bodyTop = $shape.Top
            $bodyWidth = $shape.Width
            $bodyHeight = $shape.Height
            Set-ShapeText $shape ''
            try { $shape.Visible = 0 } catch { }
        }
    }
    if (-not $titleSet) { throw "Could not set table slide title [$title]" }

    $numRows = 1 + $rows.Count
    $numCols = $headers.Count
    $tableShape = $slide.Shapes.AddTable($numRows, $numCols, $bodyLeft, $bodyTop, $bodyWidth, $bodyHeight)
    $table = $tableShape.Table
    for ($c = 1; $c -le $numCols; $c++) {
        Set-TableCellText -Cell $table.Cell(1, $c) -Text $headers[$c - 1]
        $table.Cell(1, $c).Shape.TextFrame.TextRange.Font.Bold = -1
    }
    for ($r = 0; $r -lt $rows.Count; $r++) {
        $row = @($rows[$r])
        for ($c = 1; $c -le $numCols; $c++) {
            $cellText = [string]$row[$c - 1]
            Set-TableCellText -Cell $table.Cell($r + 2, $c) -Text $cellText
        }
    }
    try {
        $total = $bodyWidth
        $table.Columns.Item(1).Width = $total * 0.34
        $table.Columns.Item(2).Width = $total * 0.08
        $table.Columns.Item(3).Width = $total * 0.34
        $table.Columns.Item(4).Width = $total * 0.24
    } catch { }
    try { $tableShape.Table.ApplyStyle('Medium Style 2 - Accent 1') } catch { }
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
    $set = $false
    foreach ($shape in (Get-TextShapes $slide)) {
        if ((Get-PlaceholderType $shape) -eq 1) {
            if ($subtitle) { Set-ShapeText $shape ($title + "`r`n`r`n" + $subtitle) }
            else { Set-ShapeText $shape $title }
            $set = $true
            return
        }
    }
    if (-not $set) { Replace-LargestTextShape $slide ($title + $(if ($subtitle) { "`r`n`r`n$subtitle" } else { '' })) }
}

function Replace-LargestTextShape($slide, [string]$text) {
    $shapes = Get-TextShapes $slide
    if ($shapes.Count -eq 0) { throw 'No text shapes on slide' }
    $primary = $shapes | Sort-Object { try { $_.TextFrame.TextRange.Text.Length } catch { 0 } } -Descending | Select-Object -First 1
    Set-ShapeText $primary $text
}

function Get-Layout($pres, [string]$name) {
    foreach ($l in $pres.SlideMaster.CustomLayouts) {
        if ($l.Name -eq $name) { return $l }
    }
    throw "Layout not found: $name"
}

function Add-SlideAt($pres, [int]$index, $spec) {
    $layout = Get-Layout $pres $spec.Layout
    $slide = $pres.Slides.AddSlide($index, $layout)
    switch ($spec.Kind) {
        'two-column' { Set-TwoColumnSlide $slide $spec.Title $spec.BodyLeft $spec.BodyRight }
        'chapter'    { Set-ChapterSlide $slide $spec.Title $spec.Subtitle }
        'table'      { Set-TableSlide $slide $spec.Title $spec.Headers $spec.Rows }
        default      { Set-ContentSlide $slide $spec.Title $spec.Body }
    }
    return $slide
}

# Sources: Andreas status 11.09.2026 + ADO pull 14.09.2026 (PP-30, epics)
$septemberSlides = @(
    @{
        Kind = 'chapter'; Layout = 'Chapter 1'
        Title = 'September 2026'
        Subtitle = 'Monthly check-in  -  discussion topics (input: Andreas, 11 Sep)'
    }
    @{
        Layout = 'Content 3'; Title = 'Team status  -  September 2026'
        Body = @"
Delivery team (Andreas, 11 Sep)
  Strong focus  -  all members working on common features
  Past sprint less IFAR-heavy; critical issues hotfixed to supported versions
  Proposal after 6.12: quality sprint  -  customer bugs first, polish shipped functionality

Health metrics
  Customer bugs: 11 open (threshold 5)  -  all in this or upcoming sprint
  Expect ~8 bugs entering next sprint (starts 21 Sep)
  Sprint PP-30 ends 18 Sep (4 days left)  -  142 backlog items in ADO

OKR pulse (unchanged objectives)
  Flow / GA: Medium  -  enablers in progress, several GA items open
  IFAR: Medium  -  improved sprint, handover still relevant
  Web modelling: Medium  -  feature #419789 New

Team ask: align priorities for next 3-6 months (customer feedback + commitments)
"@
    }
    @{
        Layout = 'Content 3'; Title = 'Flow GA enablers  -  status (11 Sep)'
        Body = @"
Ongoing
  Workunit registry
  NVE pilot feedback (gap: Ask for assistance still missing)

Delivered / partial
  Collect path: case create with model base UID applies published process version
  Monitoring and statistics  -  basic in place
  Background processes  -  completed (minor bugs in progress)
  Triggering  -  simple milestone trigger on document category

Not completed / early
  End-user and admin documentation
  Process model capabilities (GA scope)
  Full triggering system
  Refresh (async)  -  early testing; needs PnB / Oslo customer feedback
  Process model templates  -  not started
  Localization  -  POC; significant gaps remain
"@
    }
    @{
        Layout = 'Content 3'; Title = 'Programme snapshot  -  ADO (14 Sep)'
        Body = @"
Flow / PAF epics
  NVE Pilot #411612  -  Active (Bjorn)
  NVE process definitions #413948  -  Active
  Core Platform #411614  -  Active
  UX #414727  -  Active
  Standard Artifacts #414328  -  Active
  PAF umbrella #414623  -  New (description still thin)

Adjacent backlog
  Worklists / desktops #411634  -  New
  Web-based process modeling #419789  -  New

Current iteration: PP-30 (31 Aug - 18 Sep 2026)
"@
    }
    @{
        Kind = 'two-column'; Layout = 'Two columns 1'; Title = 'September focus and progress since August'
        BodyLeft = @"
Discuss today
  3-6 month priority stack (team + leadership)
  Flow GA gaps vs NVE and customer promises
  Web process designer (slides 13-14) - approve vibe-first experiment?
  Post-6.12 quality sprint  -  approve in principle?
  Close customer bugs before sprint turnover (21 Sep)
  Owners for documentation and GA enablers

Risks to flag
  GA documentation and templates not started
  NVE Ask for assistance missing
  Async refresh without customer validation
  AI designer prototype not production-ready (governance before merge)
  Legacy vs new execution path - compatibility decisions open
"@
        BodyRight = @"
Improved since August check-in
  IFAR load down this sprint
  Customer bugs tracked and sprint-assigned (11 vs crisis narrative)
  Collect integration milestone  -  model UID on case create
  Background processes largely complete
  Web modelling: prototype + WU Registry direction tangible (#419789)
  Team alignment on shared features

Still true
  Runtime strong; operational / GA maturity in progress
  Designer UI still a shell; much domain work already in master
  Worklists portfolio track needs explicit priority
"@
    }
    @{
        Layout = 'Content 3'
        Title = 'Sales enablement - what Sales asked for (Sep 2026)'
        Body = @"
Source: Tone / Sales feedback (captured in Flow 2-process Implementation Package draft)

Sales needs a sellable package, not only a technical pilot:
  Product / service sheet with clear scope and delivery
  Price for 2-process implementation (TBD catalogue)
  Included vs add-ons (2 processes, shipped building blocks only)
  Delivery model, milestones, and progress gates
  Assistance, training, and handover materials
  Support / hypercare after go-live
  Contract proposal: roles, acceptance, payment, change control
  Invoicing model for process 3+ (active process model metering)
  Clarity: customer self-admin vs Tieto assistance
  Ownership: models, checklists, rules, configuration

Commercial guardrails Sales must quote:
  2 production processes included only with signed delivery contract
  Limited offer: contracts signed by 31 Dec 2026
  No standalone platform entitlement without implementation package
"@
    }
    @{
        Kind = 'two-column'; Layout = 'Two columns 1'
        Title = 'Sales enablement - product response and gaps'
        BodyLeft = @"
In progress (draft v0.5)
  Implementation Package SalesKit + product sheet EN v1.0
  Commercial spec: hybrid model, 2-process pilot entitlement
  Delivery phases M0-M5, RACI, included vs add-ons tables
  Active process model definition + monitoring story
  Entitlement / contract addendum drafts

Still open before external pilot quote
  Catalogue SKUs (FLOW-IMPL-2PROC, FLOW-CAP-INCL-2) - Enablement
  List prices and quote template - Enablement / Finance
  Wiki module page 360 Flow - Product (draft exists)
  One-page production process definition - Product
  Legal sign-off on contract package - Legal
  Sales training + playbook sync - Enablement
"@
        BodyRight = @"
Ask leadership / check-in
  Approve pilot commercial model (2 proc, shipped blocks)
  Confirm Enablement owns SKUs + CRM fields before first quote
  Product publishes production process definition
  Align GA documentation with what Sales promises

Team link to delivery
  NVE pilot = reference implementation for sales story
  Ask for assistance gap affects customer promise - prioritize?
  Post-6.12 quality sprint supports sales credibility (stable product)

Reference (repo):
  flow/360_Flow_Implementation_Package_2Process_SalesKit_DRAFT.md
  flow/360_Flow_Enablement_Sales_Decision_Deck.md
"@
    }
    @{
        Layout = 'Content 3'
        Title = 'AI prototype exposed a simpler path to web-based process modelling'
        Body = @"
Starting point. Tone's interaction concept plus a Cursor/BMAD experiment produced a standalone Tailwind designer with drag-and-drop, inline editing and WU/XAML output.

What AI changed. A working shell emerged in hours - making the previously impractical direction tangible.

What it did not prove. Prototype only: not through production, accessibility or quality gates.

Bjorn's extension. Work Unit Registry as common store for process types, templates and published versions.

Designer scope. Assemble simple sequential Flow from reusable components; configure titles, automation IDs, arguments and groups.

Safe evolution. Models pin a Work Unit version; draft and publish - no automatic update of running models.

Current state. UI still a shell; many domain-layer elements from the demo are already in master.

Sources: weekly demo 11 Sep 2026; Teams 9-10 Sep. Demo 18 Sep upcoming.
"@
    }
    @{
        Layout = 'Content 3'
        Title = 'Push forward with vibe first - but make production readiness explicit'
        Body = @"
Prototype to learn - not to ship. Demo, change, approve, then harden.

Start narrow. NVE-ready sequential activities first; branching when scenarios require it.

Stabilize the contract. Versioned Work Units; never mutate running processes in place.

Separate old and new. Isolate new execution path; convert only understood scenarios.

Proposed experiment. Designer in internal/test; one NVE golden path: create, configure, publish, use, upgrade.

Govern generated code. Human owner, PR review, tests, security and a11y before merge.

Compatibility decision. Architecture group: plans, state machines, PnB global plans, Docker/Linux constraints.

Capture learning. Specs and ADRs beside code; 18 Sep demo decides production hardening scope.
"@
    }
    @{
        Layout = 'Content 3'; Title = 'September  -  recommended next steps'
        Body = @"
This month
  Run team priority workshop (3-6 months)  -  Andreas lead
  Close or re-plan customer bugs before sprint PP-31
  NVE assistance feature  -  product decision and ADO slice
  Assign documentation / GA enabler DRI per open GA line
  PnB / Oslo feedback session on async refresh
  Web designer: internal/test env + NVE golden path (create, publish, use, upgrade)
  Name owner for AI-generated UI; PR review, tests, security and a11y before merge
  Use 18 Sep demo to decide what advances to production hardening

After 6.12 (proposal)
  Quality sprint: customer bugs first, stabilize and polish delivered Flow functionality

Architecture / learning
  Small group: Plan and Build plans, state machines, Docker/Linux custom-process constraints
  Capture specs and ADRs beside code (per Bjorn 10-11 Sep strategy)

Reporting
  Refresh pilot weekly ADO report
  Update ProductPlan from September priorities
"@
    }
    @{
        Kind = 'table'; Layout = 'Content 3'; Title = 'September  -  issues and decisions'
        Headers = @('Issue', 'Crit', 'Suggestion', 'Decision')
        Rows = @(
            ,@('Flow GA documentation', '4', 'Assign owners; minimum GA set', 'Who leads?')
            ,@('NVE Ask for assistance', '4', 'Scope + target release', 'In 6.12 or patch?')
            ,@('GA enablers open (templates, localization, triggering)', '4', 'Rank for 3-6 month plan', 'Workshop output')
            ,@('Web designer experiment', '4', 'Approve internal golden-path pilot (slide 14)', 'Go / defer?')
            ,@('AI-generated UI governance', '4', 'Named owner + quality gates before merge', 'Who owns?')
            ,@('Modelling vs legacy execution', '3', 'Architecture session on compatibility constraints', 'Schedule?')
            ,@('Customer bugs (11)', '3', 'Burn down before 21 Sep', 'Accept quality sprint?')
            ,@('Async refresh validation', '3', 'Engage PnB / Oslo', 'Customer contact?')
            ,@('3-6 month priorities', '4', 'Team session this month', 'Calendar workshop?')
        )
    }
)

$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = -1
$pres = $pp.Presentations.Open($work, $false, $false, $false)

Set-CoverSubtitle $pres.Slides.Item(1) "Monthly check-in`r`nSeptember 2026`r`n`r`nInternal - Business Monitoring"

$insertAt = $insertAfterSlide + 1
foreach ($spec in $septemberSlides) {
    Add-SlideAt $pres $insertAt $spec | Out-Null
    $insertAt++
}

try {
    $pres.SaveAs($output, 24)
    $saved = $output
} catch {
    $fallback = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_updated_regen.pptx'
    $pres.SaveAs($fallback, 24)
    $saved = $fallback
    Write-Warning "Could not save to output path. Saved to: $fallback"
}

$totalSlides = $pres.Slides.Count
$augustStart = $insertAfterSlide + $septemberSlides.Count + 1
$mayStart = $augustStart + 6   # August section is 6 slides in base deck
$pres.Close()
$pp.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pres) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pp) | Out-Null
[GC]::Collect()
[GC]::WaitForPendingFinalizers()
Remove-Item $work -Force -ErrorAction SilentlyContinue

$fixScript = Join-Path $PSScriptRoot 'fix_pp_checkin_pptx_encoding.py'
if (Test-Path $fixScript) {
    $repoRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
    Push-Location $repoRoot
    try { uv run python $fixScript $saved | Write-Host } finally { Pop-Location }
}

Write-Output "Saved: $saved"
Write-Output "Total slides: $totalSlides (added $($septemberSlides.Count) September slides after slide $insertAfterSlide)"
Write-Output "August section starts at slide $augustStart"
Write-Output "May section starts at slide $mayStart"

