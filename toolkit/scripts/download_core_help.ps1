# Download Source/ENU from te-industry-public360/core-help
# Preserves folder structure locally

$repoUrl = "https://github.com/te-industry-public360/core-help.git"
$targetPath = "Source/ENU"
$outputDir = "core-help-Source-ENU"

Write-Host "Cloning repository with sparse checkout (Source/ENU only)..." -ForegroundColor Cyan

# Create temp directory for clone
$tempDir = Join-Path $env:TEMP "core-help-clone"
if (Test-Path $tempDir) { Remove-Item -Recurse -Force $tempDir }

# Clone with sparse checkout - only fetches the specified folder
git clone --filter=blob:none --sparse $repoUrl $tempDir
if ($LASTEXITCODE -ne 0) {
    Write-Host "Clone failed. If repo is private, ensure you're authenticated (e.g. gh auth login)" -ForegroundColor Red
    exit 1
}

Push-Location $tempDir
git sparse-checkout set $targetPath
Pop-Location

# Copy to desired location in current project
$sourcePath = Join-Path $tempDir $targetPath
if (Test-Path $sourcePath) {
    if (Test-Path $outputDir) { Remove-Item -Recurse -Force $outputDir }
    Copy-Item -Recurse $sourcePath $outputDir
    Write-Host "Done! Files saved to: $outputDir" -ForegroundColor Green
} else {
    Write-Host "Path $targetPath not found in repo" -ForegroundColor Red
}

# Cleanup
Remove-Item -Recurse -Force $tempDir -ErrorAction SilentlyContinue
