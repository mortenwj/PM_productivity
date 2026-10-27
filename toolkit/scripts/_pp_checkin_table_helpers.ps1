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
    if (-not $shape.HasTextFrame) { return }
    try { $shape.TextFrame.TextRange.Text = $text } catch { }
}
function Set-TableCellText {
    param($Cell, [Parameter(Mandatory)][string]$Text)
    $tr = $Cell.Shape.TextFrame.TextRange
    $tr.Text = $Text
    $tr.ParagraphFormat.Bullet.Type = 0
    $tr.ParagraphFormat.SpaceAfter = 0
    $tr.ParagraphFormat.SpaceBefore = 0
}
function Set-TableSlide($slide, [string]$title, [string[]]$headers, [object[]]$rows) {
    $titleSet = $false
    $bodyLeft = 36; $bodyTop = 100; $bodyWidth = 648; $bodyHeight = 320
    foreach ($shape in @($slide.Shapes)) {
        if ($shape.HasTable) { $shape.Delete() }
    }
    foreach ($shape in $slide.Shapes) {
        if ($shape.HasTable) { continue }
        $phType = Get-PlaceholderType $shape
        if (($phType -eq 1 -or $phType -eq 3) -and -not $titleSet) {
            Set-ShapeText $shape $title
            $titleSet = $true
            continue
        }
        if ($phType -eq 2 -or $phType -eq 7) {
            $bodyLeft = $shape.Left
            $bodyTop = $shape.Top
            $bodyWidth = $shape.Width
            $bodyHeight = $shape.Height
            Set-ShapeText $shape ''
            try { $shape.Visible = 0 } catch { }
        }
    }
    if (-not $titleSet) { throw "Could not set table slide title [$title]" }

    $numRows = 1 + $rows.Count
    $numCols = $headers.Count
    $tableShape = $slide.Shapes.AddTable($numRows, $numCols, $bodyLeft, $bodyTop, $bodyWidth, $bodyHeight)
    $table = $tableShape.Table
    for ($c = 1; $c -le $numCols; $c++) {
        Set-TableCellText -Cell $table.Cell(1, $c) -Text $headers[$c - 1]
        $table.Cell(1, $c).Shape.TextFrame.TextRange.Font.Bold = -1
    }
    for ($r = 0; $r -lt $rows.Count; $r++) {
        $row = @($rows[$r])
        for ($c = 1; $c -le $numCols; $c++) {
            $cellText = [string]$row[$c - 1]
            Set-TableCellText -Cell $table.Cell($r + 2, $c) -Text $cellText
        }
    }
    # Column widths: Issue widest; Crit narrow
    try {
        $total = $bodyWidth
        $table.Columns.Item(1).Width = $total * 0.34
        $table.Columns.Item(2).Width = $total * 0.08
        $table.Columns.Item(3).Width = $total * 0.34
        $table.Columns.Item(4).Width = $total * 0.24
    } catch { }
    try { $tableShape.Table.ApplyStyle('Medium Style 2 - Accent 1') } catch { }
}
