$ErrorActionPreference = 'Stop'
$mcp = Get-Content 'C:\Users\MortenJensen\.cursor\mcp.json' -Raw | ConvertFrom-Json
$apiUrl = $mcp.mcpServers.mediawiki.env.MEDIAWIKI_URL
$user = $mcp.mcpServers.mediawiki.env.MEDIAWIKI_USERNAME
$pass = $mcp.mcpServers.mediawiki.env.MEDIAWIKI_PASSWORD
$pageId = 7396
$title = '360° Flow - Demo setup'
$textPath = Join-Path $PSScriptRoot '_wiki_publish.txt'
$text = Get-Content -LiteralPath $textPath -Raw -Encoding UTF8
$summary = 'Sync demo setup: Decision templates (vedtak), EnableChecklistsP360, updated ZIP'

$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$tok = Invoke-RestMethod -Uri ($apiUrl + '?action=query&meta=tokens&type=login&format=json') -WebSession $session
$loginBody = @{
    action   = 'login'
    lgname   = $user
    lgpassword = $pass
    lgtoken  = $tok.query.tokens.logintoken
    format   = 'json'
}
$login = Invoke-RestMethod -Uri $apiUrl -Method Post -Body $loginBody -WebSession $session
if ($login.login.result -ne 'Success') { throw "Login failed: $($login.login.result)" }

$csrfTok = Invoke-RestMethod -Uri ($apiUrl + '?action=query&meta=tokens&type=csrf&format=json') -WebSession $session
$baseRev = (Invoke-RestMethod -Uri ($apiUrl + "?action=query&pageids=$pageId&prop=revisions&rvprop=ids&format=json") -WebSession $session).query.pages."$pageId".revisions[0].revid
$editBody = @{
    action    = 'edit'
    pageid    = $pageId
    text      = $text
    summary   = $summary
    token     = $csrfTok.query.tokens.csrftoken
    baserevid = $baseRev
    format    = 'json'
}
$edit = Invoke-RestMethod -Uri $apiUrl -Method Post -Body $editBody -WebSession $session
if ($edit.error) { throw ($edit.error | ConvertTo-Json -Compress) }
Write-Host ($edit | ConvertTo-Json -Depth 6 -Compress)
if (-not $edit.edit) { throw 'No edit result' }
Write-Host "Result: $($edit.edit.result) newrev: $($edit.edit.newrevid) oldrev: $($edit.edit.oldrevid)"
