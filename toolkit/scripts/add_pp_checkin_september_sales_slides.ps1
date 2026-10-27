# Insert Sales enablement slides into September section of check-in deck.
# Source: Sales feedback (Tone / Sales, Sep 2026) -> 360_Flow_Implementation_Package_2Process_SalesKit_DRAFT.md Part H
$ErrorActionPreference = 'Stop'

$source = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_updated.pptx'
$output = $source
$work   = Join-Path $env:TEMP ("pp_checkin_sales_" + [guid]::NewGuid().ToString() + ".pptx")
$insertAfterSlide = 10   # after "September focus..."; before issues / next steps

if (-not (Test-Path $source)) { throw "Deck not found: $source" }

Copy-Item $source $work -Force
Set-ItemProperty -Path $work -Name IsReadOnly -Value $false

function Get-PlaceholderType($shape) {
    try { return [int]$shape.PlaceholderFormat.Type } catch { return -1 }
}
function Get-TextShapes($slide) {
    $shapes = @()
    foreach ($shape in $slide.Shapes) { if ($shape.HasTextFrame) { $shapes += $shape } }
    return $shapes
}
function Set-ShapeText($shape, [string]$text) {
    if ($null -eq $text) { return }
    $shape.TextFrame.TextRange.Text = $text
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
    if (-not $titleSet -or -not $bodySet) { throw "Could not fill slide [$title]" }
}
function Set-TwoColumnSlide($slide, [string]$title, [string]$left, [string]$right) {
    $titleSet = $false
    $cols = New-Object System.Collections.Generic.List[object]
    foreach ($shape in (Get-TextShapes $slide)) {
        $phType = Get-PlaceholderType $shape
        if ($phType -eq 1 -and -not $titleSet) { Set-ShapeText $shape $title; $titleSet = $true; continue }
        if ($phType -eq 2) { [void]$cols.Add($shape) }
    }
    if ($cols.Count -lt 2) { throw "Two-column layout missing for [$title]" }
    Set-ShapeText $cols[0] $left
    Set-ShapeText $cols[1] $right
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
    if ($spec.Kind -eq 'two-column') {
        Set-TwoColumnSlide $slide $spec.Title $spec.BodyLeft $spec.BodyRight
    } else {
        Set-ContentSlide $slide $spec.Title $spec.Body
    }
}

$salesSlides = @(
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
        Kind = 'two-column'
        Layout = 'Two columns 1'
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
)

$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = -1
$pres = $pp.Presentations.Open($work, $false, $false, $false)

$insertAt = $insertAfterSlide + 1
foreach ($spec in $salesSlides) {
    Add-SlideAt $pres $insertAt $spec
    $insertAt++
}

try {
    $pres.SaveAs($output, 24)
    $saved = $output
} catch {
    $fallback = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_updated_sales.pptx'
    $pres.SaveAs($fallback, 24)
    $saved = $fallback
}

$total = $pres.Slides.Count
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
Write-Output "Total slides: $total (inserted $($salesSlides.Count) sales slides after slide $insertAfterSlide)"
