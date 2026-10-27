$ErrorActionPreference = 'Stop'
$template = 'C:\Users\MortenJensen\Brand Kit for Ai Agents\PPT template\Tieto presentation Template - Tieto Sans dynamic 2.pptx'
$pp = New-Object -ComObject PowerPoint.Application
$pp.Visible = -1
$pres = $pp.Presentations.Open($template, $true, $false, $false)

foreach ($layoutName in @('Content 2', 'Two columns 1', 'Cover page 1', 'Chapter 1', 'Conclusion 1')) {
    Write-Output "=== Layout: $layoutName ==="
    foreach ($layout in $pres.SlideMaster.CustomLayouts) {
        if ($layout.Name -ne $layoutName) { continue }
        $i = 0
        foreach ($shape in $layout.Shapes) {
            $i++
            $hasText = $shape.HasTextFrame
            $phType = 'n/a'
            $phIdx = 'n/a'
            $isPh = $false
            try {
                $isPh = $shape.PlaceholderFormat.Type -ge 0
                $phType = $shape.PlaceholderFormat.Type
                $phIdx = $shape.PlaceholderFormat.Idx
            } catch {}
            $txt = ''
            if ($hasText) {
                $raw = $shape.TextFrame.TextRange.Text
                if ($raw.Length -gt 80) { $txt = $raw.Substring(0, 80) + '...' } else { $txt = $raw }
                $txt = ($txt -replace "`r", '' -replace "`n", ' | ')
            }
            Write-Output "  Shape $i Name=[$($shape.Name)] HasText=$hasText IsPh=$isPh PhType=$phType PhIdx=$phIdx Text=[$txt]"
        }
        break
    }
}

$pres.Close()
$pp.Quit()
