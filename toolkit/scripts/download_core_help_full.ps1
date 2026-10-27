# Full clone of core-help - preserves complete folder structure
# Result: core-help/Source/ENU/... (and everything else in the repo)

$repoUrl = "https://github.com/te-industry-public360/core-help.git"
$outputDir = "core-help"

if (Test-Path $outputDir) {
    Write-Host "Folder $outputDir already exists. Remove it first or choose another name." -ForegroundColor Yellow
    exit 1
}

Write-Host "Cloning full repository..." -ForegroundColor Cyan
git clone $repoUrl $outputDir

if ($LASTEXITCODE -eq 0) {
    Write-Host "Done! Full structure at: $outputDir" -ForegroundColor Green
    Write-Host "Source/ENU is at: $outputDir/Source/ENU" -ForegroundColor Gray
} else {
    Write-Host "Clone failed. If private: run 'gh auth login' or use a personal access token." -ForegroundColor Red
}
