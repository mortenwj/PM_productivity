$ErrorActionPreference = "Stop"

$kitRoot = "C:\Users\MortenJensen\Brand Kit for Ai Agents"
$template = Join-Path $kitRoot "PPT template\Tieto presentation Template - Tieto Sans dynamic 2.pptx"
$output = Join-Path $PSScriptRoot "360_Flow_Pricing_Options_5slides.pptx"

if (-not (Test-Path $template)) {
    throw "Template not found: $template"
}

Copy-Item -Path $template -Destination $output -Force

function Get-LayoutMap {
    param($Presentation)
    $map = @{}
    foreach ($layout in $Presentation.SlideMaster.CustomLayouts) {
        if (-not $map.ContainsKey($layout.Name)) {
            $map[$layout.Name] = $layout
        }
    }
    return $map
}

function Set-PlaceholderText {
    param(
        [Parameter(Mandatory = $true)]$Slide,
        [int]$PlaceholderType,
        [string]$Text
    )
    foreach ($shape in $Slide.Shapes) {
        if ($shape.HasTextFrame -and $shape.PlaceholderFormat -ne $null) {
            if ([int]$shape.PlaceholderFormat.Type -eq $PlaceholderType) {
                $shape.TextFrame.TextRange.Text = $Text
                return $true
            }
        }
    }
    return $false
}

function Set-TitleAndBody {
    param(
        $Slide,
        [string]$Title,
        [string]$Body
    )
    Set-PlaceholderText -Slide $Slide -PlaceholderType 1 -Text $Title | Out-Null
    if (-not (Set-PlaceholderText -Slide $Slide -PlaceholderType 2 -Text $Body)) {
        Set-PlaceholderText -Slide $Slide -PlaceholderType 7 -Text $Body | Out-Null
    }
}

$slides = @(
    @{
        Layout = 'Cover page 1'
        Title  = '360 Flow - Pricing and packaging decision'
        Body   = "Commercial model for pilot to GA`rManagement approval | June 2026"
        Mode   = 'Cover'
    }
    @{
        Layout = 'Content 2'
        Title  = 'The ask'
        Body   = @(
            'Align on three decisions:'
            '- How we land Flow: fast uptake, Nordic buying norms'
            '- How we capture return on Process Framework R&D'
            '- What goes to Enablement / catalogue (meter, tiers, SKUs)'
            ''
            'Recommendation: Hybrid model (Option 3)'
            'Foundation included in Public 360 | process capacity for scale | Enterprise for power'
            'Playbook levels for sales | Process Engine logic for overage above entitlement'
        ) -join "`r"
    }
    @{
        Layout = 'Two columns 1'
        Title  = 'Three pricing options at a glance'
        Body   = @(
            'OPTION 1 - Process Engine (score 23/35)'
            '- Meter: per active production process'
            '- Land: first process cheap | Expand: more processes'
            '- Strength: familiar meter | Risk: weak alone; BPM-style'
            ''
            'OPTION 2 - Playbook packages (score 30/35)'
            '- Meter: 3 capability levels (single / multi / full platform)'
            '- Land: Single Process Access | Expand: to ~5 processes, then upgrade'
            '- Strength: best sales narrative | Risk: under-monetize past ~5'
            ''
            'OPTION 3 - Hybrid RECOMMENDED (score 32/35)'
            '- Meter: foundation + N processes + packs + Enterprise tier'
            '- Land: foundation + generous included N | Expand: packs + Enterprise'
            '- Strength: land + return; strongest Nordic fit'
        ) -join "`r"
    }
    @{
        Layout = 'Content 2'
        Title  = 'Recommended model - Hybrid (Option 3)'
        Body   = @(
            'A - Foundation: ProcessView, milestones/stages, standard dialogs, progression auditability'
            '   Included in Public 360 / Basic'
            ''
            'B - Capacity: right to run N production processes'
            '   5-10 included (segment TBD) + process packs above entitlement'
            '   Overage aligns with Process Engine per-process bands'
            ''
            'C - Enterprise: portfolio/overview (when GA), advanced rules, scale governance'
            '   Premium tier - operating model, not compliance paywall'
            ''
            'Services: fixed implementation packages (Playbook)'
            'Journey: Prove - Expand - Mature'
        ) -join "`r"
    }
    @{
        Layout = 'End slide 1'
        Title  = 'Decisions and next steps'
        Body   = @(
            'Decisions requested:'
            '1. Approve Hybrid as commercial architecture'
            '2. Included production processes: e.g. 5 (small) / 10 (default)'
            '3. Process Engine: per-process bands for overage only'
            '4. Enterprise boundary locked to GA roadmap'
            '5. Pilot: generous entitlement + fixed implementation'
            '6. Enablement: catalogue + production process definition before GA'
            ''
            'If approved: Enablement SKUs, Product metering definition, Sales training, Finance ARPA, Pilot terms'
            ''
            'Inclusion = land economics | Capacity + Enterprise = return economics'
        ) -join "`r"
    }
)

$ppt = $null
$pres = $null

try {
    $ppt = New-Object -ComObject PowerPoint.Application

    $pres = $ppt.Presentations.Open($output, $false, $false, $false)

    while ($pres.Slides.Count -gt 0) {
        $pres.Slides.Item(1).Delete()
    }

    $layouts = Get-LayoutMap -Presentation $pres

    foreach ($spec in $slides) {
        $layoutName = $spec.Layout
        if (-not $layouts.ContainsKey($layoutName)) {
            throw "Layout not found in template: $layoutName"
        }
        $layout = $layouts[$layoutName]
        $slide = $pres.Slides.AddSlide($pres.Slides.Count + 1, $layout)

        if ($spec.Mode -eq 'Cover') {
            Set-PlaceholderText -Slide $slide -PlaceholderType 1 -Text $spec.Title | Out-Null
            if (-not (Set-PlaceholderText -Slide $slide -PlaceholderType 4 -Text $spec.Body)) {
                Set-PlaceholderText -Slide $slide -PlaceholderType 2 -Text $spec.Body | Out-Null
            }
        }
        else {
            Set-TitleAndBody -Slide $slide -Title $spec.Title -Body $spec.Body
        }
    }

    $pres.Save()
    Write-Output "Created: $output"
    Write-Output "Slides: $($pres.Slides.Count)"
}
finally {
    if ($pres -ne $null) { $pres.Close() | Out-Null }
    if ($ppt -ne $null) { $ppt.Quit() | Out-Null }
    if ($pres -ne $null) {
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($pres) | Out-Null
    }
    if ($ppt -ne $null) {
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($ppt) | Out-Null
    }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
