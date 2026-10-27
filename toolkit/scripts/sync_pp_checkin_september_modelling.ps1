# Align September synthesis slides with user-added web process modelling slides (13-14).
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot '_pp_checkin_table_helpers.ps1')

$deck = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_updated.pptx'
if (-not (Test-Path $deck)) { throw "Deck not found: $deck" }
$work = Join-Path $env:TEMP ("pp_checkin_mod_" + [guid]::NewGuid().ToString() + ".pptx")
Copy-Item $deck $work -Force
Set-ItemProperty -Path $work -Name IsReadOnly -Value $false

function Find-SlideByTitleFragment($pres, [string]$fragment) {
    for ($i = 1; $i -le $pres.Slides.Count; $i++) {
        $slide = $pres.Slides.Item($i)
        foreach ($shape in (Get-TextShapes $slide)) {
            $phType = Get-PlaceholderType $shape
            if ($phType -eq 1 -or $phType -eq 3) {
                $t = $shape.TextFrame.TextRange.Text
                if ($t -like "*$fragment*") { return $slide }
            }
        }
    }
    return $null
}

function Set-TwoColumnByTitle($slide, [string]$title, [string]$left, [string]$right) {
    $titleSet = $false
    $cols = New-Object System.Collections.Generic.List[object]
    foreach ($shape in (Get-TextShapes $slide)) {
        $phType = Get-PlaceholderType $shape
        if (($phType -eq 1 -or $phType -eq 3) -and -not $titleSet) {
            Set-ShapeText $shape $title; $titleSet = $true; continue
        }
        if ($phType -eq 2) { [void]$cols.Add($shape) }
    }
    if ($cols.Count -lt 2) { throw "Two-column layout missing for [$title]" }
    Set-ShapeText $cols[0] $left
    Set-ShapeText $cols[1] $right
}

function Set-ContentByTitle($slide, [string]$title, [string]$body) {
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
    if (-not $titleSet -or -not $bodySet) { throw "Could not fill content slide [$title]" }
}

$focusTitle = 'September focus and progress since August'
$focusLeft = @"
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
$focusRight = @"
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

$nextTitle = 'September  -  recommended next steps'
$nextBody = @"
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

$issuesTitle = 'September  -  issues and decisions'
$headers = @('Issue', 'Crit', 'Suggestion', 'Decision')
$rows = @(
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

$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = -1
$pres = $pp.Presentations.Open($work, $false, $false, $false)

$sFocus = Find-SlideByTitleFragment $pres 'September focus and progress'
$sNext = Find-SlideByTitleFragment $pres 'recommended next steps'
$sIssues = Find-SlideByTitleFragment $pres 'issues and decisions'
if (-not $sFocus) { throw 'Focus slide not found' }
if (-not $sNext) { throw 'Next steps slide not found' }
if (-not $sIssues) { throw 'Issues slide not found' }

Set-TwoColumnByTitle $sFocus $focusTitle $focusLeft $focusRight
Set-ContentByTitle $sNext $nextTitle $nextBody
Set-TableSlide $sIssues $issuesTitle $headers $rows

try {
    $pres.SaveAs($deck, 24)
    $saved = $deck
} catch {
    $fallback = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_updated_modelling.pptx'
    $pres.SaveAs($fallback, 24)
    $saved = $fallback
}

$pres.Close()
$pp.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pres) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pp) | Out-Null
[GC]::Collect()
[GC]::WaitForPendingFinalizers()
Remove-Item $work -Force -ErrorAction SilentlyContinue

Write-Output "Saved: $saved"
Write-Output "Updated: focus (slide $($sFocus.SlideIndex)), next steps ($($sNext.SlideIndex)), issues table ($($sIssues.SlideIndex))"
