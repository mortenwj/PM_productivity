$ErrorActionPreference = 'Stop'
$output = Join-Path $PSScriptRoot 'BRE_Day1_Workshop.pptx'
$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = -1
$pres = $pp.Presentations.Open($output, $true, $false, $false)
for ($i = 1; $i -le $pres.Slides.Count; $i++) {
    $slide = $pres.Slides.Item($i)
    Write-Output "--- Slide $i ---"
    foreach ($shape in $slide.Shapes) {
        if (-not $shape.HasTextFrame) { continue }
        $txt = $shape.TextFrame.TextRange.Text.Trim()
        if ($txt -and $txt -notmatch '^(December|<#>|$)') {
            $preview = if ($txt.Length -gt 120) { $txt.Substring(0, 120) + '...' } else { $txt }
            Write-Output "  [$($shape.Name)]: $preview"
        }
    }
}
$pres.Close()
$pp.Quit()
