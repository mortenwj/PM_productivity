# Create .venv and install dependencies via uv (source of truth: pyproject.toml).
$ErrorActionPreference = 'Stop'

$root = Resolve-Path (Join-Path $PSScriptRoot '..\..')
Set-Location $root

$userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
if ($userPath) {
    $env:PATH = "$userPath;$env:PATH"
}

$uv = Get-Command uv -ErrorAction SilentlyContinue
if (-not $uv) {
    Write-Host "uv not found. Install with:"
    Write-Host "  winget install astral-sh.uv --accept-package-agreements --scope user"
    Write-Error "uv is required for Python setup in this repo."
}

Write-Host "Running uv sync (Python 3.12, dependencies from pyproject.toml) ..."
& uv sync

Write-Host ""
& uv run python --version
Write-Host "Done. Run scripts with: uv run python <script.py>"
Write-Host "Example: uv run python projects/process-platform/flow/ai-model-creator-spike/generate_draft.py --scenario s1-permit --dry-run"
