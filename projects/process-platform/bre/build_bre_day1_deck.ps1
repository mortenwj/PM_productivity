# Build BRE Day 1 deck from Tieto brand template (tieto-brand skill)
# Note: "Content 2" is title-only in this template — use "Content 3" for body text.
$ErrorActionPreference = 'Stop'

$template = "C:\Users\MortenJensen\Brand Kit for Ai Agents\PPT template\Tieto presentation Template - Tieto Sans dynamic 2.pptx"
$output   = Join-Path $PSScriptRoot "BRE_Day1_Workshop.pptx"
$work     = Join-Path $env:TEMP ("bre_day1_" + [guid]::NewGuid().ToString() + ".pptx")

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
            2 {
                if (-not $line3Set) { Set-ShapeText $shape $line3; $line3Set = $true }
            }
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
        $notesSlide = $slide.NotesPage
        foreach ($shape in $notesSlide.Shapes) {
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

    $idx = $pres.Slides.Count + 1
    $slide = $pres.Slides.AddSlide($idx, $layout)

    switch ($spec.Kind) {
        'cover' {
            Set-CoverSlide $slide $spec.Title $spec.Subtitle $spec.Line3
        }
        'two-column' {
            Set-TwoColumnSlide $slide $spec.Title $spec.BodyLeft $spec.BodyRight
        }
        'chapter' {
            Set-ChapterSlide $slide $spec.Title $spec.Body
        }
        default {
            Set-ContentSlide $slide $spec.Title $spec.Body
        }
    }

    if ($spec.Notes) { Set-SlideNotes $slide $spec.Notes }
}

$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = -1
$pres = $pp.Presentations.Open($work, $false, $false, $false)

while ($pres.Slides.Count -gt 0) {
    $pres.Slides.Item(1).Delete()
}

$slides = @(
    @{
        Kind     = 'cover'
        Layout   = 'Cover page 1'
        Title    = 'Business Rules Engine'
        Subtitle = 'Status, commitments and role in the platform'
        Line3    = 'Process Platform workshop - Day 1 - Internal alignment'
        Notes    = 'Today we align internally on BRE. Not a customer session; not a sales pitch.'
    }
    @{
        Layout = 'Agenda'
        Title  = 'Agenda (90 min)'
        Body   = @"
Block A - What and why (30 min)
  Platform role, customer problems, rule model, three example cases

Block B - Status and next steps (55 min)
  Code reality (Bjorn), DevOps, commitments, platform role, pilot proposal

Close (5 min)
  Capture actions and owners
"@
        Notes = 'Morten leads Part A; Bjorn owns technical status in Part B.'
    }
    @{
        Layout = 'Content 3'
        Title  = 'Where BRE sits in the platform'
        Body   = @"
Process Framework - three questions

Process models          WHAT the process looks like
Process Engine / Flow   HOW it runs
Business Rules Engine   WHEN actions are allowed or required

BRE is the governance layer:
  Validations and constraints today
  Automation when runtime catches up
  Without bespoke code per customer

Sibling pillar to Flow and Process Engine - not a replacement.
"@
        Notes = 'Link to Flow inventory from earlier Day 1 if already covered.'
    }
    @{
        Layout = 'Content 3'
        Title  = 'Why customers care'
        Body   = @"
Public-sector organisations need standardisation AND local adaptation.

Today much of that lives in:
  Custom event code and consultant one-offs
  Opaque configuration that breaks on upgrade
  Repeated patterns rebuilt per customer
    close-case checks, auto-close, field rules, tender-specific logic

BRE aims to make operational rules:
  Explicit and configurable (DMN-based)
  Versionable and auditable
  Inside the product - not scattered in scripts

Honest expectation: admin/consultant skill still needed early on.
"@
    }
    @{
        Kind      = 'two-column'
        Layout    = 'Two columns 1'
        Title     = 'Every rule: Trigger - Condition - Action'
        BodyLeft  = @"
WHEN (Trigger)
  Case updated, document created
  Document status change
  Schedule / job (future)
  Invoked from UI or integration (future)

IF (Condition)
  Case type and status
  Field values and mandatory data
  Document state and counts
  Process step / dependency (future)
"@
        BodyRight = @"
WHAT (Action)
  Block with validation message (works today)
  Update data / close case (not in runtime)
  Notify users (not in runtime)
  Trigger process / RunProcess (stub)

Reuse Oslo deck slide 12 visual if available in room.
"@
    }
    @{
        Layout = 'Content 3'
        Title  = 'Example 1: Close-case validation (First wave)'
        Body   = @"
Problem
  Cases closed with working documents still active
  Missing mandatory fields on close
  Cancelled while documents still in progress

Rule pattern
  Trigger: Event on case status change
  Condition: Document state, mandatory fields, case type rules
  Action: Raise error (ValidationMessage) - blocks the operation

Customers: Tullverket, Regeringskansliet, IMR, Svenska kyrkan
DevOps #219865 - First wave scenario, multiple commitments

This pattern works in code today (ValidationMessage).
"@
        Notes = 'Reuse Oslo slide 13 if projected alongside.'
    }
    @{
        Layout = 'Content 3'
        Title  = 'Example 2: Auto-close ready cases'
        Body   = @"
Problem
  Large share of cases sit in "ready from case handler" but never close
  Manual follow-up cost and backlog

Rule pattern
  Trigger: Scheduled job (daily / periodic)
  Condition: Status = ready, documents in correct state, no blockers
  Action: Update data - close case automatically

Customer: Aurskog-Holand - DevOps #311335

Important for Block B
  Automation / Update-data actions are NOT in runtime yet
  Sets up honest status discussion - do not oversell
"@
        Notes = 'Reuse Oslo slide 14. Flag gap before status section.'
    }
    @{
        Layout = 'Content 3'
        Title  = 'Example 3: Empty cases - void only'
        Body   = @"
Problem
  Cases without documents should not be closed normally - only voided

Rule pattern
  Trigger: Event on case close attempt
  Condition: Document count = 0 (or equivalent)
  Action: Raise error - direct user to void instead

Customer: Regeringskansliet Klaradia - DevOps #239187

Backup example if time
  Helsedirektoratet #312153 - due date on incoming doc (Commitment, overdue)
"@
    }
    @{
        Kind   = 'chapter'
        Layout = 'Chapter 1'
        Title  = 'Status and next steps'
        Body   = 'What we have built - DevOps - Commitments - Pilot proposal'
    }
    @{
        Layout = 'Content 3'
        Title  = 'What we have built (core-bl)'
        Body   = @"
Strong today
  DMN meta model and bridge to decision tables
  Publish lifecycle (draft to published)
  Admin APIs: list, save, publish rule sets

Partial / wired with gaps
  Event runtime on Case and Document CRUD
  ValidationMessage - blocks operation with user-facing message

Not implemented
  RunProcess and data-update actions
  Scheduled jobs / Manual triggers (meta only)
  Plugin execution path
  ContextEntity filter at runtime
  IsEnabled not enforced on evaluation

Admin UI in separate repo. Feature flag BusinessRuleEngineEnabled OFF by default (6.6+).

Detail: BRE_Pilot_Readiness_Assessment.md, BRE_Architecture.md
"@
        Notes = 'Bjorn leads this slide (~10 min). Whiteboard OK for runtime gaps.'
    }
    @{
        Layout = 'Content 3'
        Title  = 'DevOps - Epic #11122'
        Body   = @"
DMN Business Rules Engine
  Owner: Bjorn
  Epic target: 2026-12-30
  State: New (framework under active development)

Active now (4 features)
  Data model
  Input resolution
  Validations
  Built-in queries and actions

Backlog (New)
  Meta events, Admin UX, Publishing workflow
  Rules library, Statistics, integration polish

Child work items tie to customer scenarios - see sources/ado-work-items.md
"@
    }
    @{
        Layout = 'Content 3'
        Title  = 'Commitments drive the real timeline'
        Body   = @"
Planning assumption: Commitment-tagged customer items matter more than epic date alone.

Overdue
  #312153 Helsedirektoratet - due date on incoming document

Feb 2026 (in description, no target date field)
  #231319 Svenska Kyrkan - cleanup on case close

Jun 2027
  #422713 Danish tender K - auto-close documents on case close

Sep 2027 (IVO tender)
  #420587, #420590, #420282 - mandatory fields, dependencies, cleanup

Anchor for full scenario coverage: mid-late 2027
Epic 2026 = pilot and foundation, not tender-grade automation
"@
    }
    @{
        Layout = 'Content 3'
        Title  = 'Role in the platform'
        Body   = @"
Process Platform stack

Flow / Process Engine
  Structure and execution of work

Business Rules Engine
  When things are allowed, required, or blocked

FFUI
  Field-level UI rules - related, separate engine today

AI / agentic (hypothesis)
  Needs rules and structure as guardrails

Day 2 customer dialog is process support broadly - BRE is one thread, not the headline.
Connects to Day 1 AI/rules session later - do not pre-empt Day 2 agenda.
"@
    }
    @{
        Layout = 'Content 3'
        Title  = 'Proposed pilot v1'
        Body   = @"
Realistic with code today plus small engineering fixes

Scope
  Event trigger: Case OnUpdate only
  Action: ValidationMessage only
  Scenarios: close-case validation, void-only empty cases
  1 tenant, flag on, 1-2 rule sets, single-decision models

Engineering first (before pilot)
  ContextEntity filtering at runtime
  IsEnabled enforcement
  End-to-end test that asserts rule outcome

Not in pilot v1
  Auto-close jobs, RunProcess, plugin actions, FFUI rules
"@
    }
    @{
        Layout = 'Content 3'
        Title  = 'Discussion and next steps'
        Body   = @"
Decisions to capture (15 min discussion)

1. Agree pilot slice above?
2. Who owns runtime blocker fixes?
3. Admin UX - webadmin repo status, demo path?
4. Reconcile epic Dec 2026 vs commitments Jun-Sep 2027
5. ProductPlan BRE bar - unpark and update?

Actions slide
  Owner, date, DevOps link for each action

Reference after session: projects/process-platform/bre/ inventory
"@
    }
    @{
        Layout = 'Conclusion 1'
        Title  = 'Thank you'
        Body   = @"
Questions?

projects/process-platform/bre/ - full inventory for the team
"@
    }
)

foreach ($s in $slides) {
    Add-Slide $pres $s
}

$pres.SaveAs($output, 24)
$pres.Close()
$pp.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pres) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pp) | Out-Null
[GC]::Collect()
[GC]::WaitForPendingFinalizers()
Remove-Item $work -Force -ErrorAction SilentlyContinue

Write-Output "Created: $output ($($slides.Count) slides)"
