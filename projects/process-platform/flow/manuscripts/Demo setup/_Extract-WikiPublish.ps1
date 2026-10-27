$draft = Join-Path (Split-Path $PSScriptRoot -Parent | Split-Path -Parent) '360_Flow_Demo_Setup_DRAFT.md'
$draft = Join-Path (Split-Path $PSScriptRoot -Parent) '360_Flow_Demo_Setup_DRAFT.md'
$text = Get-Content -LiteralPath $draft -Raw -Encoding UTF8
if ($text -notmatch '(?s)```wikitext\r?\n(.*)\r?\n```') { throw 'wikitext block not found' }
$Matches[1] | Set-Content -LiteralPath (Join-Path $PSScriptRoot '_wiki_publish.txt') -Encoding UTF8 -NoNewline
Write-Host 'Extracted' (Join-Path $PSScriptRoot '_wiki_publish.txt')
