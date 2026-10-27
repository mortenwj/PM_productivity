# Publish 360° Flow - Demo setup page from outputs/360_Flow_Demo_Setup_wikitext.txt
$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$wikitextPath = Join-Path $repoRoot 'outputs\360_Flow_Demo_Setup_wikitext.txt'
if (-not (Test-Path $wikitextPath)) {
    throw "Missing wikitext: $wikitextPath (run extract_wiki_draft_wikitext.py first)"
}
$content = Get-Content -LiteralPath $wikitextPath -Raw -Encoding UTF8
$mcp = Get-Content 'C:\Users\MortenJensen\.cursor\mcp.json' -Raw | ConvertFrom-Json
$apiUrl = $mcp.mcpServers.mediawiki.env.MEDIAWIKI_URL
$user = $mcp.mcpServers.mediawiki.env.MEDIAWIKI_USERNAME
$pass = $mcp.mcpServers.mediawiki.env.MEDIAWIKI_PASSWORD
$pageId = 7396
$summary = 'Demo setup: troubleshooting empty Process arguments on Stage-Defined processes (Final processing)'

$cookieJar = Join-Path $env:TEMP 'mw-edit-cookies.txt'
if (Test-Path $cookieJar) { Remove-Item $cookieJar -Force }

$tokJson = curl.exe -sS -c $cookieJar -b $cookieJar ($apiUrl + '?action=query&meta=tokens&type=login&format=json')
$loginToken = ($tokJson | ConvertFrom-Json).query.tokens.logintoken
$loginJson = curl.exe -sS -c $cookieJar -b $cookieJar -X POST $apiUrl `
    --data-urlencode "action=login" `
    --data-urlencode "lgname=$user" `
    --data-urlencode "lgpassword=$pass" `
    --data-urlencode "lgtoken=$loginToken" `
    --data-urlencode "format=json"
if (($loginJson | ConvertFrom-Json).login.result -ne 'Success') { throw "Login failed: $loginJson" }

$csrfJson = curl.exe -sS -c $cookieJar -b $cookieJar ($apiUrl + '?action=query&meta=tokens&type=csrf&format=json')
$csrf = ($csrfJson | ConvertFrom-Json).query.tokens.csrftoken

$bodyFile = Join-Path $env:TEMP '360-flow-demo-setup-wikitext.txt'
[System.IO.File]::WriteAllText($bodyFile, $content, [System.Text.UTF8Encoding]::new($false))

$editJson = curl.exe -sS -b $cookieJar -c $cookieJar -X POST $apiUrl `
    --data-urlencode "action=edit" `
    --data-urlencode "pageid=$pageId" `
    --data-urlencode "summary=$summary" `
    --data-urlencode "format=json" `
    --data-urlencode "token=$csrf" `
    --data-urlencode "text@$bodyFile"

$edit = $editJson | ConvertFrom-Json
if ($edit.error) { throw "Edit failed: $editJson" }
Write-Host "Page updated: $($edit.edit.title) rev $($edit.edit.newrevid)"
Write-Host "https://wiki.software-innovation.com/wiki/360%C2%B0_Flow_-_Demo_setup"
