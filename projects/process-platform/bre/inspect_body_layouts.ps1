$ErrorActionPreference = 'Stop'
$template = 'C:\Users\MortenJensen\Brand Kit for Ai Agents\PPT template\Tieto presentation Template - Tieto Sans dynamic 2.pptx'
$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = -1
$pres = $pp.Presentations.Open($template, $true, $false, $false)

foreach ($layout in $pres.SlideMaster.CustomLayouts) {
    $bodyPh = @()
    $titlePh = @()
    foreach ($shape in $layout.Shapes) {
        if (-not $shape.HasTextFrame) { continue }
        try {
            $t = $shape.PlaceholderFormat.Type
            if ($t -eq 1 -or $t -eq 3) { $titlePh += $shape.Name }
            if ($t -eq 2 -or $t -eq 7) { $bodyPh += "$($shape.Name):$t" }
        } catch {}
    }
    if ($bodyPh.Count -gt 0) {
        Write-Output "$($layout.Name) | title=$($titlePh -join ',') | body=$($bodyPh -join ',')"
    }
}

$pres.Close()
$pp.Quit()
