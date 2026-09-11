[CmdletBinding()]
param(
    [switch]$All,
    [switch]$Claude,
    [switch]$Codex,
    [switch]$Agents
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

if (-not ($All -or $Claude -or $Codex -or $Agents)) {
    $All = $true
}

$targets = @()
if ($All -or $Claude) { $targets += @{ Name = 'Claude'; Source = Join-Path $repoRoot '.claude\skills'; Target = Join-Path $HOME '.claude\skills' } }
if ($All -or $Codex) { $targets += @{ Name = 'Codex'; Source = Join-Path $repoRoot '.codex\skills'; Target = Join-Path $HOME '.codex\skills' } }
if ($All -or $Agents) { $targets += @{ Name = 'Agents'; Source = Join-Path $repoRoot '.agents\skills'; Target = Join-Path $HOME '.agents\skills' } }

foreach ($entry in $targets) {
    New-Item -ItemType Directory -Force -Path $entry.Target | Out-Null
    $skills = @(Get-ChildItem -Directory -LiteralPath $entry.Source | Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') })
    foreach ($skill in $skills) {
        $destination = Join-Path $entry.Target $skill.Name
        Copy-Item -LiteralPath $skill.FullName -Destination $destination -Recurse -Force
    }
    Write-Host ("{0}: installed {1} skill packages into {2}" -f $entry.Name, $skills.Count, $entry.Target)
}

Write-Host 'Installation complete. Existing unrelated skill packages were not deleted.'
