# Upload 360 Flow demo assets to wiki (as ZIP — wiki allows zip, not json/dotm).
$ErrorActionPreference = 'Stop'
$mcp = Get-Content 'C:\Users\MortenJensen\.cursor\mcp.json' -Raw | ConvertFrom-Json
$apiUrl = $mcp.mcpServers.mediawiki.env.MEDIAWIKI_URL
$user = $mcp.mcpServers.mediawiki.env.MEDIAWIKI_USERNAME
$pass = $mcp.mcpServers.mediawiki.env.MEDIAWIKI_PASSWORD
$base = $PSScriptRoot
$staging = Join-Path $env:TEMP '360flow-demo-wiki-upload'
if (Test-Path $staging) { Remove-Item $staging -Recurse -Force }
New-Item -ItemType Directory -Path $staging | Out-Null

function Copy-DemoFile([string]$Pattern, [string]$DestDir) {
    $item = Get-ChildItem -LiteralPath $base -File | Where-Object { $_.Name -like $Pattern } | Select-Object -First 1
    if (-not $item) { throw "Missing file for pattern: $Pattern" }
    $dest = Join-Path $DestDir $item.Name
    Copy-Item -LiteralPath $item.FullName -Destination $dest -Force
    return $item.Name
}

$pmDir = Join-Path $staging 'process-models'
$clDir = Join-Path $staging 'checklists'
$tmDir = Join-Path $staging 'document-templates'
New-Item -ItemType Directory -Path $pmDir, $clDir, $tmDir | Out-Null

Copy-DemoFile 'Handle application with right of appeal (English).json' $pmDir | Out-Null
Copy-DemoFile 'Behandle ans*gning m. klageret (Danish).json' $pmDir | Out-Null
Copy-DemoFile 'Behandle s*knad m_klagerett.json' $pmDir | Out-Null
Copy-DemoFile 'Behandla ans*kan med *verklagander*tt (Swedish).json' $pmDir | Out-Null
Copy-DemoFile 'K*sittele hakemus valitusoikeudella (Finnish).json' $pmDir | Out-Null
Copy-DemoFile 'Checklist for application processing with right of appeal (English).json' $clDir | Out-Null
Copy-DemoFile 'Tjekliste for ans*gningsbehandling med klageret (Danish).json' $clDir | Out-Null
Copy-DemoFile 'Sjekkliste_for*s*knadsbehandling_med_klagerett*.json' $clDir | Out-Null
Copy-DemoFile 'Checklista f*r ans*kningsbehandling med *verklagander*tt (Swedish).json' $clDir | Out-Null
Copy-DemoFile 'Tarkistuslista hakemuksen k*sittelyyn valitusoikeudella (Finnish).json' $clDir | Out-Null
Copy-DemoFile 'prosess_mangelbrev.dotm' $tmDir | Out-Null
Copy-DemoFile 'process_deficiency_letter.dotm' $tmDir | Out-Null
Copy-DemoFile 'proces_mangelbrev.dotm' $tmDir | Out-Null
Copy-DemoFile 'process_bristbrev.dotm' $tmDir | Out-Null
Copy-DemoFile 'prosessi_puutekirje.dotm' $tmDir | Out-Null
Copy-DemoFile 'prosess_vedtak.dotm' $tmDir | Out-Null
Copy-DemoFile 'process_decision.dotm' $tmDir | Out-Null
Copy-DemoFile 'proces_vedtagelse.dotm' $tmDir | Out-Null
Copy-DemoFile 'process_beslut.dotm' $tmDir | Out-Null
Copy-DemoFile 'prosessi_paatos.dotm' $tmDir | Out-Null

$zips = @(
    @{ Wiki = '360 Flow demo - process models.zip'; Path = Join-Path $env:TEMP '360 Flow demo - process models.zip'; Source = $pmDir }
    @{ Wiki = '360 Flow demo - checklists.zip'; Path = Join-Path $env:TEMP '360 Flow demo - checklists.zip'; Source = $clDir }
    @{ Wiki = '360 Flow demo - document templates.zip'; Path = Join-Path $env:TEMP '360 Flow demo - document templates.zip'; Source = $tmDir }
)
foreach ($z in $zips) {
    if (Test-Path $z.Path) { Remove-Item $z.Path -Force }
    Compress-Archive -Path (Join-Path $z.Source '*') -DestinationPath $z.Path -Force
}

$cookieJar = Join-Path $env:TEMP 'mw-upload-cookies.txt'
if (Test-Path $cookieJar) { Remove-Item $cookieJar -Force }
$desc = "[[Category:360°]]`nDemo asset for [[360° Flow - Demo setup]]. Internal pilot only. Extract ZIP before import."

$tokJson = curl.exe -sS -c $cookieJar -b $cookieJar ($apiUrl + '?action=query&meta=tokens&type=login&format=json')
$loginToken = ($tokJson | ConvertFrom-Json).query.tokens.logintoken
$loginJson = curl.exe -sS -c $cookieJar -b $cookieJar -X POST $apiUrl `
    --data-urlencode "action=login" `
    --data-urlencode "lgname=$user" `
    --data-urlencode "lgpassword=$pass" `
    --data-urlencode "lgtoken=$loginToken" `
    --data-urlencode "format=json"
$login = $loginJson | ConvertFrom-Json
if ($login.login.result -ne 'Success') { throw "Login failed: $($login.login.result)" }

$csrfJson = curl.exe -sS -c $cookieJar -b $cookieJar ($apiUrl + '?action=query&meta=tokens&type=csrf&format=json')
$csrf = ($csrfJson | ConvertFrom-Json).query.tokens.csrftoken

$results = @()
foreach ($z in $zips) {
    Write-Host "Uploading: $($z.Wiki)"
    $curlOut = curl.exe -sS -b $cookieJar -c $cookieJar $apiUrl `
        -F "action=upload" `
        -F "filename=$($z.Wiki)" `
        -F "file=@$($z.Path)" `
        -F "token=$csrf" `
        -F "format=json" `
        -F "ignorewarnings=1" `
        -F "comment=360 Flow demo setup assets" `
        -F "text=$desc"
    $resp = $curlOut | ConvertFrom-Json
    if ($resp.error) {
        if ($resp.error.code -eq 'fileexists-no-change') {
            Write-Host "  OK (unchanged on wiki)"
            $results += [pscustomobject]@{ Wiki = $z.Wiki; Url = "(unchanged)" }
            continue
        }
        throw "Upload failed for $($z.Wiki): $($curlOut)"
    }
    $uploadResult = $resp.upload.result
    if ($uploadResult -ne 'Success' -and $uploadResult -ne 'Warning') {
        throw "Upload failed for $($z.Wiki): $($curlOut)"
    }
    $url = $null
    if ($resp.upload.imageinfo) { $url = $resp.upload.imageinfo[0].descriptionurl }
    $results += [pscustomobject]@{ Wiki = $z.Wiki; Url = $(if ($url) { $url } else { $uploadResult }) }
    Write-Host "  OK"
}
$results | Format-Table -AutoSize
Write-Host "Uploaded $($results.Count) ZIP packages."
