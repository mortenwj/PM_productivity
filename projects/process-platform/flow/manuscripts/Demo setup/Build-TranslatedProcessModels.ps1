# Builds DA, NO, SV, FI process model exports from the English 6.12 master.
$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..\..\..')).Path
Push-Location $repoRoot
try {
    uv run python toolkit/scripts/build_localized_flow_demo_process_models.py
}
finally {
    Pop-Location
}
