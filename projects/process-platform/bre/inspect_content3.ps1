$ErrorActionPreference = 'Stop'
$template = 'C:\Users\MortenJensen\Brand Kit for Ai Agents\PPT template\Tieto presentation Template - Tieto Sans dynamic 2.pptx'
$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = -1
$pres = $pp.Presentations.Open($template, $true, $false, $false)
foreach ($layoutName in @('Content 3', 'Content 4', 'Agenda')) {
    Write-Output "=== $layoutName ==="
    foreach ($layout in $pres.SlideMaster.CustomLayouts) {
        if ($layout.Name -ne $layoutName) { continue }
        foreach ($shape in $layout.Shapes) {
            if (-not $shape.HasTextFrame) { continue }
            $phType = 'none'
            try { $phType = $shape.PlaceholderFormat.Type } catch {}
            $txt = ($shape.TextFrame.TextRange.Text -replace "`r?`n", ' | ').Substring(0, [Math]::Min(50, $shape.TextFrame.TextRange.Text.Length))
            Write-Output "  $($shape.Name) PhType=$phType [$txt]"
        }
        break
    }
}
$pres.Close()
$pp.Quit()
