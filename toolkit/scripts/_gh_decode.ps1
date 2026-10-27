$apiPath = $args[0]
$repo = if ($args.Count -ge 2 -and $args[1]) { $args[1] } else { 'te-industry-public360/core-bl' }
$j = gh api "repos/$repo/contents/$apiPath" | ConvertFrom-Json
$b64 = $j.content -replace "`r`n", '' -replace "`n", ''
[Console]::Out.Write([Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($b64)))
