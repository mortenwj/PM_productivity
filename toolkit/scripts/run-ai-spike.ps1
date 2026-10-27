param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Args
)

$ErrorActionPreference = 'Stop'
$root = Resolve-Path (Join-Path $PSScriptRoot '..\..')
Set-Location $root

$userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
if ($userPath) { $env:PATH = "$userPath;$env:PATH" }

$script = Join-Path $root 'projects\process-platform\flow\ai-model-creator-spike\generate_draft.py'
& uv run python $script @Args
