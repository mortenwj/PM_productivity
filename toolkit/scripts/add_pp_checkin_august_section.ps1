# Add August 2026 section to Process Platform check-in deck.
# Preserves all existing slides (May + March sections unchanged).
$ErrorActionPreference = 'Stop'

$source = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_aug.pptx'
$output = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_aug_updated.pptx'
$work   = Join-Path $env:TEMP ("pp_checkin_aug_section_" + [guid]::NewGuid().ToString() + ".pptx")
$insertAfterSlide = 5   # after IFAR; before May chapter

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
        default      { Set-ContentSlide $slide $spec.Title $spec.Body }
    }
    return $slide
}

$augustSlides = @(
    @{
        Kind = 'chapter'; Layout = 'Chapter 1'
        Title = 'August 2026'
        Subtitle = 'Monthly check-in â€” discussion topics'
    }
    @{
        Layout = 'Content 3'; Title = 'August status â€” team objectives'
        Body = @"
Objective #1: Deliver stable, scalable 360 Flow (PAF)
Objective #2: Stabilize IFAR and prepare handover
Objective #3: Extend process modelling (web-based, rule-driven)

Status (24 Aug)
  O1 on track â€” 6.10 pilot live; NVE epic Active (#411612)
  O2 ongoing â€” IFAR bug inflow; handover in progress
  O3 ramping â€” web modelling team (Sumit, Anna, Bjorn)

OKR confidence
  Flow: Medium-High | IFAR: Low-Medium | Modelling: Medium

Sprint PP-29 ends 28 Aug (4 days left)
Module health (5 Aug): IFAR Review | Workflow At Risk | PE Watch
Open bugs: 50+ (threshold 5)
"@
    }
    @{
        Layout = 'Content 3'; Title = 'Flow / PAF status â€” August 2026'
        Body = @"
6.10 pilot: runtime operational
  ProcessView, milestones, stages, progress plans, building blocks

Programme (ADO)
  NVE Pilot #411612 â€” Active
  Process definitions #413948 â€” Active
  Core Platform #411614 â€” Active
  UX #414727 â€” Active | Standard Artifacts #414328 â€” Active

Maturity snapshot
  Shipped: runtime execution, ProcessView, lifecycle visibility
  Transitional: document flow (legacy + React)
  Emerging: worklists (#411634 New), portfolio/desktops

NVE reframing (June)
  One story: execution + visualization + portfolio
  Maps required for go-live; portfolio depth beyond P&B webparts shown
"@
    }
    @{
        Kind = 'two-column'; Layout = 'Two columns 1'; Title = '6.11 focus and Copenhagen signals'
        BodyLeft = @"
6.11 GA priorities
  NVE production readiness and acceptance testing
  Runtime stability, reusable flow blocks
  Portfolio surfaces (worklists, desktops)
  Collect integration, localization, documentation

Deprioritize
  Broad feature expansion
  Advanced AI ambitions at GA
  Large-scale modelling, broad UX redesign

Decision principles
  Stability over flexibility
  Performance over new capability
"@
        BodyRight = @"
Copenhagen discovery (10 Jun)
  AST: 60k cases/yr; domestic-cloud AI #1
  KK: PE too hard; centralized AI governance
  NB: publication workflows; start simple

Cross-customer pattern
  Manual checking and clicking â€” not deciding

Positioning
  6.10 proved execution
  Next sale = maturity + intelligence on foundation
  Do not oversell AI at GA
"@
    }
    @{
        Layout = 'Content 3'; Title = 'August risks and issue list'
        Body = @"
Operational risks
  IFAR inflow â€” 1-2 devs constantly on bugs
  NVE go-live â€” maps, portfolio, process velocity
  Build pipeline â€” long cycles delay pilot feedback
  AI oversell â€” domestic cloud and governance first

Issue | Crit | Suggestion | Decision needed
Open bugs 50+ | 4 | IFAR handover; triage discipline |
NVE go-live gaps | 4 | 6.11 backlog; acceptance test plan | Prioritize maps + portfolio?
IFAR capacity drain | 4 | Handover to Transparency | Approve timeline?
Process dev vs GA | 3 | Senior backup; NVE assignments |
Web modelling ramp | 3 | MVP scope lock (8 components) |
Collect integration 6.11 | 3 | Integration Team coordination | Lock scope owner?
Copenhagen follow-up | 3 | AST rules, NB publication flow |
"@
    }
    @{
        Layout = 'Content 3'; Title = 'August â€” recommended next steps'
        Body = @"
This month
  Lock 6.11 Flow GA scope with Integration Team (Collect)
  NVE map + overview acceptance test plan
  ADO epic descriptions (#414623, #411612)
  Web modelling MVP scope sign-off
  BRE MVP scope â€” entity event + error + WU execution
  IFAR eDoc journal notes â€” MJ and Brian
  Refresh weekly ADO pilot report

Sales / customer
  NB publication workflow proposal
  AST business rules review
  ProductPlan roadmap update from August draft
"@
    }
)

$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = -1
$pres = $pp.Presentations.Open($work, $false, $false, $false)

# Cover date only â€” does not touch May/March sections
Set-CoverSubtitle $pres.Slides.Item(1) "Monthly check-in`r`nAugust 2026`r`n`r`nInternal - Business Monitoring"

$insertAt = $insertAfterSlide + 1
foreach ($spec in $augustSlides) {
    Add-SlideAt $pres $insertAt $spec | Out-Null
    $insertAt++
}

try {
    $pres.SaveAs($output, 24)
    $saved = $output
} catch {
    $fallback = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_aug_updated_regen.pptx'
    $pres.SaveAs($fallback, 24)
    $saved = $fallback
    Write-Warning "Could not save to output path. Saved to: $fallback"
}

$totalSlides = $pres.Slides.Count
$pres.Close()
$pp.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pres) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pp) | Out-Null
[GC]::Collect()
[GC]::WaitForPendingFinalizers()
Remove-Item $work -Force -ErrorAction SilentlyContinue

Write-Output "Saved: $saved"
Write-Output "Total slides: $totalSlides (added $($augustSlides.Count) August slides after slide $insertAfterSlide)"
Write-Output "May section starts at slide $($insertAfterSlide + $augustSlides.Count + 1)"

