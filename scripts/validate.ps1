[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$rootNames = @('.claude\skills', '.codex\skills', '.grok\skills', '.agents\skills')
. (Join-Path $PSScriptRoot 'runtime-layout.ps1')
$total = 0

foreach ($relativeRoot in $rootNames) {
    $root = Join-Path $repoRoot $relativeRoot
    if (-not (Test-Path -LiteralPath $root)) { throw "Missing runtime root: $relativeRoot" }
    $flatSkills = @(Get-ChildItem -Directory -LiteralPath $root | Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') })
    if ($flatSkills.Count -gt 0) { throw "Flat skill packages remain in ${relativeRoot}: $($flatSkills.Name -join ', ')" }
    $entries = @(Get-RuntimeSkillDirectories -Root $root)
    if ($entries.Count -eq 0) { throw "No categorized skill packages found in ${relativeRoot}" }
    foreach ($entry in $entries) {
        $content = Get-Content -Raw -LiteralPath (Join-Path $entry.Directory.FullName 'SKILL.md')
        if ([string]::IsNullOrWhiteSpace($content)) { throw "Empty SKILL.md: $($entry.Directory.FullName)" }
    }
    $total += $entries.Count
    Write-Host "$relativeRoot`: $($entries.Count) valid categorized skill packages"
}

if (-not (Test-Path -LiteralPath (Join-Path $repoRoot 'catalog\skills.json'))) { throw 'Missing generated catalog/skills.json' }
if (-not (Test-Path -LiteralPath (Join-Path $repoRoot 'catalog\skills.md'))) { throw 'Missing generated catalog/skills.md' }
Write-Host "Validation passed: $total runtime package entries checked."
