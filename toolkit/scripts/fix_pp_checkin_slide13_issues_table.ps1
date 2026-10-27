# Convert September "issues and decisions" slide body to a real PowerPoint table.
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot '_pp_checkin_table_helpers.ps1')

$deck = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_updated.pptx'
$titleMatch = 'September  -  issues and decisions'
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

if (-not (Test-Path $deck)) { throw "Deck not found: $deck" }
$work = Join-Path $env:TEMP ("pp_checkin_tbl_" + [guid]::NewGuid().ToString() + ".pptx")
Copy-Item $deck $work -Force
Set-ItemProperty -Path $work -Name IsReadOnly -Value $false

$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = -1
$pres = $pp.Presentations.Open($work, $false, $false, $false)

$target = $null
for ($i = 1; $i -le $pres.Slides.Count; $i++) {
    $slide = $pres.Slides.Item($i)
    foreach ($shape in (Get-TextShapes $slide)) {
        $phType = Get-PlaceholderType $shape
        if ($phType -eq 1 -or $phType -eq 3) {
            if ($shape.TextFrame.TextRange.Text -like "*$titleMatch*") {
                $target = $slide
                break
            }
        }
    }
    if ($target) { break }
}
if (-not $target) { throw "Slide not found: [$titleMatch]" }

Set-TableSlide $target $titleMatch $headers $rows

try {
    $pres.SaveAs($deck, 24)
    $saved = $deck
} catch {
    $fallback = 'C:\Users\MortenJensen\Downloads\Process Platform check-in 2026_updated_table.pptx'
    $pres.SaveAs($fallback, 24)
    $saved = $fallback
}

$slideNum = $target.SlideIndex
$pres.Close()
$pp.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pres) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pp) | Out-Null
[GC]::Collect()
[GC]::WaitForPendingFinalizers()
Remove-Item $work -Force -ErrorAction SilentlyContinue

Write-Output "Saved: $saved (slide $slideNum table applied)"
