# DEPRECATED: overwrote May/March slides. Use add_pp_checkin_august_section.ps1 instead.
# Update Process Platform August 2026 monthly check-in deck (in-place content refresh)
$ErrorActionPreference = 'Stop'

$source = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_aug.pptx'
$output = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_aug_updated.pptx'
$work   = Join-Path $env:TEMP ("pp_checkin_update_" + [guid]::NewGuid().ToString() + ".pptx")

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

function Set-SlideTitle($slide, [string]$title) {
    foreach ($shape in (Get-TextShapes $slide)) {
        $phType = Get-PlaceholderType $shape
        if ($phType -eq 1 -or $phType -eq 3) {
            Set-ShapeText $shape $title
            return $true
        }
    }
    return $false
}

function Set-SlideBody($slide, [string]$body) {
    $shapes = Get-TextShapes $slide
    $bodyShape = $null
    $maxLen = -1
    foreach ($shape in $shapes) {
        $phType = Get-PlaceholderType $shape
        if ($phType -in 1, 3) { continue }
        $len = 0
        try { $len = $shape.TextFrame.TextRange.Text.Length } catch {}
        if ($len -gt $maxLen) { $maxLen = $len; $bodyShape = $shape }
    }
    if (-not $bodyShape) {
        foreach ($shape in $shapes) {
            if ((Get-PlaceholderType $shape) -notin 1, 3) { $bodyShape = $shape; break }
        }
    }
    if (-not $bodyShape) { return $false }
    foreach ($shape in $shapes) {
        if ($shape -ne $bodyShape -and (Get-PlaceholderType $shape) -notin 1, 3) {
            Set-ShapeText $shape ''
        }
    }
    Set-ShapeText $bodyShape $body
    return $true
}

function Replace-AllTextOnSlide($slide, [string]$newText) {
    $shapes = Get-TextShapes $slide
    if ($shapes.Count -eq 0) { return $false }
    $primary = $shapes | Sort-Object { try { $_.TextFrame.TextRange.Text.Length } catch { 0 } } -Descending | Select-Object -First 1
    Set-ShapeText $primary $newText
    foreach ($shape in $shapes) {
        if ($shape -ne $primary) { Set-ShapeText $shape '' }
    }
    return $true
}

function Set-SlideContent($slide, [string]$title, [string]$body) {
    if ($title) { Set-SlideTitle $slide $title | Out-Null }
    if ($body) {
        if (-not (Set-SlideBody $slide $body)) {
            Replace-AllTextOnSlide $slide $body | Out-Null
        }
    }
}

$updates = @{
    1 = @{
        Title = 'Process Platform'
        Subtitle = "Monthly check-in`r`nAugust 2026`r`n`r`nInternal - Business Monitoring"
    }
    2 = @{
        ReplaceAll = $true
        Body = @"
Process Platform team - August status

Objective #1: Deliver stable, scalable 360 Flow (PAF)
Objective #2: Stabilize IFAR and prepare handover
Objective #3: Extend process modelling (web-based, rule-driven)

Status: O1 on track (6.10 pilot live, NVE Active) | O2 ongoing | O3 ramping

OKR confidence
  Flow: Medium-High
  IFAR: Low-Medium
  Modelling: Medium

Focus this month
  NVE process delivery (#413948 Active)
  6.11 GA scope lock (Collect, worklists, docs)
  Web modelling MVP (Sumit, Anna, Bjorn)
  Copenhagen follow-up (AST, KK, Nationalbanken)

Focus issues
  IFAR bug inflow (50+ open bugs; IFAR module Review)
  Portfolio/worklist gap vs NVE expectation
  Build pipeline / delivery velocity

Health metrics (Aug 2026)
  Sprint PP-29 ends 28 Aug (4 days left)
  Module health: IFAR Review | Workflow At Risk | PE Watch

Problems to solve
  1. NVE go-live readiness (maps, portfolio, process definitions)
  2. IFAR handover + protect Flow delivery capacity
"@
    }
    6 = @{ Chapter = 'August' }
    11 = @{
        Title = '6.10 / 6.11 focus'
        Body = @"
Prioritize (6.11 GA path)
  Runtime stability and NVE production readiness
  NVE process definitions and acceptance testing
  Lifecycle consistency, reusable flow blocks
  Portfolio surfaces (worklists, desktops)
  Localization, documentation, Collect integration

Deprioritize
  Broad feature expansion, advanced AI ambitions
  Large-scale modelling ambitions, broad UX redesign

Decision principles
  Stability over flexibility | Performance over new capability
  Intelligence layer on foundation - not 6.11 GA promise
"@
    }
    12 = @{
        Title = 'Current operational risks - August 2026'
        Body = @"
AREA | RISK
IFAR inflow | Capacity drain (1-2 devs constantly)
NVE go-live | Maps, portfolio depth, process velocity
Process development velocity | Sprint PP-29 pressure
Worklists/desktops | Emerging - not operationally mature
Modelling complexity | Still implementation-centric (VS binding)
Build pipeline | Long build times delay pilot feedback
AI oversell | Copenhagen constraints: domestic cloud, governance, accuracy

Takeaway: Runtime feasibility is proven. Risk is operational maturity, simplification, and protecting delivery capacity while closing NVE gaps.
"@
    }
    13 = @{ Chapter = 'Customer discovery' ; Subtitle = 'Copenhagen 10 June 2026' }
    14 = @{
        Title = 'PAF / Flow status - August 2026'
        Body = @"
6.10 pilot: runtime operational on ProcessView, milestones, stages, progress plans

Programme (ADO)
  NVE Pilot #411612 - Active | Process defs #413948 - Active
  Core Platform #411614 - Active | UX #414727 - Active
  Standard Artifacts #414328 - Active

Since June
  Copenhagen discovery: AST, KK, Nationalbanken - intelligence on foundation
  NVE reframing: execution + visualization + portfolio = one story
  Desktops/webparts feature #416409 closed; worklists #411634 still New

Path to GA (6.11-6.12)
  NVE feedback, Collect integration, monitoring, templates, localization
  Web modelling MVP | BRE entity-event MVP stretch
"@
    }
    15 = @{
        ReplaceAll = $true
        Title = 'Customer activities - August 2026'
        Body = @"
Nr | Customer | Status | Follow-up
1 | NVE | Pilot Active | Process delivery, go-live planning
2 | Datatilsynet | Demo done | Awaiting response
3 | SIKT | Demo booked Feb | Follow up Q3
4 | Avinor | Demo booked Feb | Follow up Q3
5 | Thon gruppen | Demo Mar | Follow up
6 | UIM / WS Processtøtte DK | Demo Jan | Pipeline
7 | Chalmers, Norec, Drammen, NAV | Demo done | Nurture
8 | Copenhagen (AST, KK, NB) | Discovery Jun | AST rules, NB publication, KK examples
9 | Botkyrka, NND, Svenska Kyrkan | Planned/tender | Sales pipeline

Commercial model slides unchanged (Single / Multi / Full Platform)
"@
    }
    18 = @{
        Title = 'Internal training needs'
        Body = @"
Increasing org pressure to deliver Flow implementations without core engineering

Needs
  Flow consultant enablement (ProcessView, building blocks, NVE patterns)
  Copenhagen insight pack for sales and delivery
  Clear escalation when portfolio/modelling gaps block customer promise

Blocker: team capacity - IFAR and bug inflow limit training investment
"@
    }
    22 = @{
        Title = 'Next items on roadmap - August 2026'
        Body = @"
Item | Timeline | Status
Flow GA (6.11-6.12) | Q3-Q4 | Scope lock in progress
Web-based process modelling | Q3-Q4 | Team ramping; bpmn.io foundation
Business Rules Engine | Q3-Q4 | MVP stretch 6.11; eDoc caseclose scenario
Agentic AI on foundation | 2026+ | Position only - domestic cloud first
IFAR handover | Q3 | Transparency team; eDoc journal notes
"@
    }
    23 = @{
        Title = 'Issue list - August 2026'
        Body = @"
Issue | Crit | Suggestion
Open bugs 50+ (threshold 5) | 4 | IFAR handover; triage discipline
NVE go-live gaps (maps, portfolio, processes) | 4 | Acceptance test plan; 6.11 backlog priority
IFAR capacity drain (1-2 devs) | 4 | Handover to Transparency; protect Flow sprint
Process dev velocity vs GA timeline | 3 | Senior backup; clarify NVE assignments
Web modelling team ramp | 3 | MVP scope lock (8 components)
Collect integration for 6.11 | 3 | Coordinate Integration Team
Copenhagen follow-up | 3 | AST rules, NB publication workflow, KK examples
Documentation / GA readiness | 3 | Module page, help, enablement
"@
    }
}

$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = -1
$pres = $pp.Presentations.Open($work, $false, $false, $false)

foreach ($slideNum in ($updates.Keys | Sort-Object)) {
    $spec = $updates[$slideNum]
    $slide = $pres.Slides.Item([int]$slideNum)

    if ($spec.Subtitle -and -not $spec.Body -and -not $spec.Title) {
        Replace-AllTextOnSlide $slide $spec.Subtitle | Out-Null
    }
    if ($spec.Chapter) {
        $text = $spec.Chapter
        if ($spec.Subtitle) { $text += "`r`n`r`n$($spec.Subtitle)" }
        Replace-AllTextOnSlide $slide $text | Out-Null
        continue
    }
    if ($spec.ReplaceAll -and $spec.Body) {
        Replace-AllTextOnSlide $slide $spec.Body | Out-Null
        continue
    }
    if ($spec.Title -or $spec.Body) {
        Set-SlideContent $slide $spec.Title $spec.Body
    }
    if ($spec.Subtitle -and $slideNum -eq 1) {
        foreach ($shape in (Get-TextShapes $slide)) {
            if ((Get-PlaceholderType $shape) -eq 4) {
                Set-ShapeText $shape $spec.Subtitle
                break
            }
        }
    }
}

try {
    $pres.SaveAs($output, 24)
    $saved = $output
} catch {
    $fallback = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_aug_updated_regen.pptx'
    $pres.SaveAs($fallback, 24)
    $saved = $fallback
    Write-Warning "Could not overwrite output. Saved to: $fallback"
}

$pres.Close()
$pp.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pres) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pp) | Out-Null
[GC]::Collect()
[GC]::WaitForPendingFinalizers()
Remove-Item $work -Force -ErrorAction SilentlyContinue

Write-Output "Updated deck saved: $saved"
