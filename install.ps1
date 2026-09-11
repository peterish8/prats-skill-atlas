[CmdletBinding()]
param(
    [switch]$All,
    [switch]$Claude,
    [switch]$Codex,
    [switch]$Agents
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
. (Join-Path $repoRoot 'scripts\runtime-layout.ps1')

if (-not ($All -or $Claude -or $Codex -or $Agents)) {
    $All = $true
}

$targets = @()
if ($All -or $Claude) { $targets += @{ Name = 'Claude'; Source = Join-Path $repoRoot '.claude\skills'; Target = Join-Path $HOME '.claude\skills' } }
if ($All -or $Codex) { $targets += @{ Name = 'Codex'; Source = Join-Path $repoRoot '.codex\skills'; Target = Join-Path $HOME '.codex\skills' } }
if ($All -or $Agents) { $targets += @{ Name = 'Agents'; Source = Join-Path $repoRoot '.agents\skills'; Target = Join-Path $HOME '.agents\skills' } }

foreach ($entry in $targets) {
    New-Item -ItemType Directory -Force -Path $entry.Target | Out-Null
    $skills = @(Get-RuntimeSkillDirectories -Root $entry.Source)
    foreach ($skillEntry in $skills) {
        $destination = Join-Path $entry.Target $skillEntry.Directory.Name
        Copy-Item -LiteralPath $skillEntry.Directory.FullName -Destination $destination -Recurse -Force
    }
    Write-Host ("{0}: installed {1} skill packages into {2}" -f $entry.Name, $skills.Count, $entry.Target)
}

Write-Host 'Installation complete. Existing unrelated skill packages were not deleted.'
