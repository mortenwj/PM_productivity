# Build Flow pilot status & learnings deck (tieto-brand skill)
# Content 3 for body text — Content 2 is title-only in this template.
$ErrorActionPreference = 'Stop'

$template = "C:\Users\MortenJensen\Brand Kit for Ai Agents\PPT template\Tieto presentation Template - Tieto Sans dynamic 2.pptx"
$output   = Join-Path $PSScriptRoot "Flow_Pilot_Workshop.pptx"
$work     = Join-Path $env:TEMP ("flow_pilot_" + [guid]::NewGuid().ToString() + ".pptx")

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
    $titleSet = $false
    $subtitleSet = $false
    $line3Set = $false
    foreach ($shape in (Get-TextShapes $slide)) {
        switch (Get-PlaceholderType $shape) {
            3 { if (-not $titleSet) { Set-ShapeText $shape $title; $titleSet = $true } }
            4 { if (-not $subtitleSet) { Set-ShapeText $shape $subtitle; $subtitleSet = $true } }
            2 { if (-not $line3Set) { Set-ShapeText $shape $line3; $line3Set = $true } }
        }
    }
}

function Set-ContentSlide($slide, [string]$title, [string]$body) {
    $titleSet = $false
    $bodySet = $false
    foreach ($shape in (Get-TextShapes $slide)) {
        $phType = Get-PlaceholderType $shape
        if (($phType -eq 1 -or $phType -eq 3) -and -not $titleSet) {
            Set-ShapeText $shape $title
            $titleSet = $true
            continue
        }
        if (($phType -eq 2 -or $phType -eq 7) -and -not $bodySet) {
            Set-ShapeText $shape $body
            $bodySet = $true
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
        if ($phType -eq 1 -and -not $titleSet) {
            Set-ShapeText $shape $title
            $titleSet = $true
            continue
        }
        if ($phType -eq 2) { [void]$cols.Add($shape) }
    }
    if ($cols.Count -lt 2) { throw "Two-column layout missing body placeholders for [$title]" }
    Set-ShapeText $cols[0] $left
    Set-ShapeText $cols[1] $right
}

function Set-ChapterSlide($slide, [string]$title, [string]$subtitle) {
    foreach ($shape in (Get-TextShapes $slide)) {
        if ((Get-PlaceholderType $shape) -eq 1) {
            if ($subtitle) {
                Set-ShapeText $shape ($title + "`r`n`r`n" + $subtitle)
            } else {
                Set-ShapeText $shape $title
            }
            return
        }
    }
}

function Set-SlideNotes($slide, [string]$notes) {
    if ([string]::IsNullOrWhiteSpace($notes)) { return }
    try {
        foreach ($shape in $slide.NotesPage.Shapes) {
            if ($shape.HasTextFrame) {
                $shape.TextFrame.TextRange.Text = $notes
                return
            }
        }
    } catch {}
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
    if ($spec.Notes) { Set-SlideNotes $slide $spec.Notes }
}

$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = -1
$pres = $pp.Presentations.Open($work, $false, $false, $false)
while ($pres.Slides.Count -gt 0) { $pres.Slides.Item(1).Delete() }

$slides = @(
    @{
        Kind     = 'cover'
        Layout   = 'Cover page 1'
        Title    = '360 Flow pilot'
        Subtitle = 'Status and learnings'
        Line3    = 'Process Platform workshop - Day 1 - Internal alignment'
        Notes    = 'Present captured NVE learnings; workshop block is for team input and open gaps.'
    }
    @{
        Layout = 'Agenda'
        Title  = 'Agenda (60-75 min)'
        Body   = @"
Present (35 min)
  Reframing Flow, status, NVE learnings captured so far

Workshop discussion (25 min)
  Gaps we did not fully scope, team input, actions

Close (5 min)
  Capture owners - handoff to BRE session
"@
    }
    @{
        Kind      = 'two-column'
        Layout    = 'Two columns 1'
        Title     = 'Flow is three layers - one story'
        BodyLeft  = @"
Execution
  Process models, progress plans, activities, milestones

Visualization
  ProcessView + overview columns
  Maps, deficiencies, decisions, checklists

Portfolio
  Manager queues across cases
  Deadlines, phase status, desktops/webparts
"@
        BodyRight = @"
Learning: we undersold Flow internally

  Not only modeling + execution
  Also visualization + portfolio management

One Flow story
  Desk to case - managers and case workers

Sibling: BRE = when actions allowed (later session)
"@
    }
    @{
        Layout = 'Content 3'
        Title  = 'Pilot model and NVE programme'
        Body   = @"
Pilot: one end-to-end process, Tieto-led, 6.10 controlled enablement
Primary: NVE (#411612, tag 6.10) - #413948 process definitions

Commercial: 2 processes, shipped building blocks only
Success = processes live on cases

Sentiment after NVE meetings: positive but cautious
  Waiting on gaps before go-live confidence
"@
    }
    @{
        Kind   = 'chapter'
        Layout = 'Chapter 1'
        Title  = 'Status'
        Body   = 'Shipped - partial - DevOps'
    }
    @{
        Kind      = 'two-column'
        Layout    = 'Two columns 1'
        Title     = 'Capability snapshot'
        BodyLeft  = @"
Shipped
  Process models, progress plans, ProcessView
  Configurable overview columns
  Milestones, stages, building blocks

Partial
  Manager worklists / desktops (#411634, #414651)
  Document flow routing, localization
  Portfolio: filtering, follow-ups, reporting
"@
        BodyRight = @"
Plan and Build depth (NVE)
  Maps - required for go-live
  Checklists, estates, case phrases
  Document categories, deadlines, decisions

Direction: common repo for shared P and B + Flow assets
"@
    }
    @{
        Layout = 'Content 3'
        Title  = 'DevOps program'
        Body   = @"
#414623 PAF umbrella - New (description empty)
#411614 Core Platform - Active
#414328 Standard Artifacts - New
#414727 UX - New (ProcessView, overview #420133)
#411612 NVE Pilot - New

Refresh weekly report (last in repo: 2026-04-21)
"@
    }
    @{
        Kind   = 'chapter'
        Layout = 'Chapter 1'
        Title  = 'NVE learnings captured'
        Body   = 'Product framing - platform - meetings'
    }
    @{
        Layout = 'Content 3'
        Title  = 'Product framing (NVE)'
        Body   = @"
Portfolio = managers prioritising across cases
  Queues, deadlines, phase status

P and B webparts were shown - NVE assumed they are Flow
  They want more: filtering, follow-ups, reporting

ProcessView + columns landed
  Maps, deficiencies, decisions, checklists

Customer sees Public 360 platform - not Flow vs P and B modules
"@
    }
    @{
        Layout = 'Content 3'
        Title  = 'Meetings - what worked'
        Body   = @"
What landed
  Public 360 platform story
  Tieto partnership and delivery model

Full stakeholder mix in the room

Repeat this format
  Discovery + fast iterations
  Process Platform in customer meetings
  Product + consultancy + tech consulting together
"@
        Notes = 'No single aha moment - broad positive tone. Sentiment B: cautious on gaps.'
    }
    @{
        Kind   = 'chapter'
        Layout = 'Chapter 1'
        Title  = 'Workshop discussion'
        Body   = 'Team input - gaps - actions'
    }
    @{
        Layout = 'Content 3'
        Title  = 'Gaps to explore together'
        Body   = @"
NVE surfaced complexity we had not fully scoped

Discuss in room - capture severity (blocker / important / defer)

ProcessView - ask for assistance behaviour
ProcessView - dynamic controls by user action
Other items from delivery or customer meetings?

Where does each live: ProcessView, BRE, FFUI, config, custom WU?
"@
        Notes = 'Facilitator: flip chart or DevOps. Do not pre-decide in this deck.'
    }
    @{
        Layout = 'Content 3'
        Title  = 'Team input - your learnings'
        Body   = @"
Add from the room:

Consultant / delivery - what was harder than expected?
Engineering - what surprised you in NVE or demo?
Product - what do we undersell or oversell?

NVE go-live: what is live vs in build?
What belongs in Standard Artifacts vs customer-specific?

Second pilot - what would we refuse to promise?
"@
        Notes = 'Open discussion 15-20 min. Scribe captures bullets for Flow_Pilot_Status_And_Learnings.md'
    }
    @{
        Layout = 'Content 3'
        Title  = 'Actions - capture in room'
        Body   = @"
Owner | Action | Date | DevOps link

Examples to assign:
  Refresh weekly ADO report
  Map + overview NVE acceptance test plan
  Common repo for shared P and B + Flow assets
  Fill epic #414623 description
  Update learnings doc after workshop

"@
        Notes = 'Leave body sparse for live capture or use flip chart.'
    }
    @{
        Layout = 'Conclusion 1'
        Title  = 'Thank you'
        Body   = @"
Next: BRE session

Living doc: projects/process-platform/flow/Flow_Pilot_Status_And_Learnings.md
"@
    }
)

foreach ($s in $slides) { Add-Slide $pres $s }

try {
    $pres.SaveAs($output, 24)
    $saved = $output
} catch {
    $fallback = [System.IO.Path]::Combine(
        [System.IO.Path]::GetDirectoryName($output),
        [System.IO.Path]::GetFileNameWithoutExtension($output) + '_regenerated.pptx'
    )
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
