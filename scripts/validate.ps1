[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$rootNames = @('.claude\skills', '.codex\skills', '.agents\skills')
$total = 0

foreach ($relativeRoot in $rootNames) {
    $root = Join-Path $repoRoot $relativeRoot
    if (-not (Test-Path -LiteralPath $root)) { throw "Missing runtime root: $relativeRoot" }
    $dirs = @(Get-ChildItem -Directory -LiteralPath $root)
    $skillDirs = @($dirs | Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') })
    $invalid = @($dirs | Where-Object { -not (Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md')) })
    if ($invalid.Count -gt 0) { throw "Non-skill direct children found in ${relativeRoot}: $($invalid.Name -join ', ')" }
    foreach ($skill in $skillDirs) {
        $content = Get-Content -Raw -LiteralPath (Join-Path $skill.FullName 'SKILL.md')
        if ([string]::IsNullOrWhiteSpace($content)) { throw "Empty SKILL.md: $($skill.FullName)" }
    }
    $total += $skillDirs.Count
    Write-Host "$relativeRoot`: $($skillDirs.Count) valid skill packages"
}

if (-not (Test-Path -LiteralPath (Join-Path $repoRoot 'catalog\skills.json'))) { throw 'Missing generated catalog/skills.json' }
if (-not (Test-Path -LiteralPath (Join-Path $repoRoot 'catalog\skills.md'))) { throw 'Missing generated catalog/skills.md' }
Write-Host "Validation passed: $total runtime package entries checked."
