[CmdletBinding()]
param(
    [switch]$All,
    [switch]$Claude,
    [switch]$Codex,
    [switch]$Grok,
    [switch]$Antigravity,
    [switch]$Agents,
    [string]$Manifest,
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
. (Join-Path $repoRoot 'scripts\runtime-layout.ps1')

if ($Manifest -and ($All -or $Claude -or $Codex -or $Grok -or $Antigravity -or $Agents)) {
    throw 'Use -Manifest by itself; do not combine it with runtime switches.'
}

$selectedNames = $null
$selectedSkills = $null
$manifestData = $null
if ($Manifest) {
    $manifestPath = (Resolve-Path -LiteralPath $Manifest).Path
    $manifestData = Get-Content -Raw -LiteralPath $manifestPath | ConvertFrom-Json
    if ($manifestData.schemaVersion -ne 1) { throw 'Unsupported selection manifest schemaVersion. Expected 1.' }
    $selectedSkills = @($manifestData.skills | ForEach-Object {
        if ($_ -is [string]) {
            [pscustomobject]@{ Name = [string]$_; Targets = @() }
        } else {
            [pscustomobject]@{ Name = [string]$_.name; Targets = @($_.targets | ForEach-Object { [string]$_ }) }
        }
    } | Where-Object { -not [string]::IsNullOrWhiteSpace($_.Name) })
    $selectedNames = @($selectedSkills.Name | Select-Object -Unique)
    if ($selectedNames.Count -eq 0) { throw 'Selection manifest contains no skills.' }
    $requestedTargets = @($manifestData.targets | ForEach-Object { [string]$_ } | Select-Object -Unique)
    if ($requestedTargets.Count -eq 0) { throw 'Selection manifest contains no targets.' }
} else {
    if (-not ($All -or $Claude -or $Codex -or $Grok -or $Antigravity -or $Agents)) {
        $All = $true
    }
    $requestedTargets = @()
    if ($All -or $Claude) { $requestedTargets += 'Claude' }
    if ($All -or $Codex) { $requestedTargets += 'Codex' }
    if ($All -or $Grok) { $requestedTargets += 'Grok' }
    if ($All -or $Antigravity) { $requestedTargets += 'Antigravity' }
    if ($All -or $Agents) { $requestedTargets += 'Agents' }
}

$targetDefinitions = @{
    Claude = @{ Name = 'Claude'; Source = Join-Path $repoRoot '.claude\skills'; Target = Join-Path $HOME '.claude\skills' }
    Codex = @{ Name = 'Codex'; Source = Join-Path $repoRoot '.codex\skills'; Target = Join-Path $HOME '.codex\skills' }
    Grok = @{ Name = 'Grok'; Source = Join-Path $repoRoot '.grok\skills'; Target = Join-Path $HOME '.grok\skills' }
    Antigravity = @{ Name = 'Antigravity'; Source = Join-Path $repoRoot '.antigravity\skills'; Target = Join-Path $HOME '.gemini\config\skills' }
    Agents = @{ Name = 'Agents'; Source = Join-Path $repoRoot '.agents\skills'; Target = Join-Path $HOME '.agents\skills' }
}
$targets = @()
foreach ($targetName in $requestedTargets) {
    if (-not $targetDefinitions.ContainsKey($targetName)) { throw "Unknown target runtime: $targetName" }
    $targets += $targetDefinitions[$targetName]
}

foreach ($entry in $targets) {
    $available = @{}
    foreach ($skillEntry in @(Get-RuntimeSkillDirectories -Root $entry.Source)) {
        $available[$skillEntry.Directory.Name] = $skillEntry.Directory
    }
    $installNames = if ($selectedNames) { $selectedNames } else { @($available.Keys | Sort-Object) }
    if ($selectedSkills) {
        $installNames = @($selectedSkills | Where-Object {
            ($_.Targets.Count -eq 0) -or ($_.Targets -contains $entry.Name)
        } | Select-Object -ExpandProperty Name -Unique)
    }
    $installed = 0
    $missing = @()
    foreach ($skillName in $installNames) {
        if (-not $available.ContainsKey($skillName)) {
            $missing += $skillName
            continue
        }
        $destination = Join-Path $entry.Target $skillName
        if (-not $DryRun) {
            New-Item -ItemType Directory -Force -Path $entry.Target | Out-Null
            Copy-Item -LiteralPath $available[$skillName].FullName -Destination $destination -Recurse -Force
        }
        $installed++
    }
    $modeLabel = if ($DryRun) { 'would install' } else { 'installed' }
    Write-Host ("{0}: {1} {2} skill packages into {3}" -f $entry.Name, $modeLabel, $installed, $entry.Target)
    if ($missing.Count -gt 0) {
        Write-Warning ("{0}: unavailable in this runtime tree: {1}" -f $entry.Name, ($missing -join ', '))
    }
}

$completion = if ($DryRun) { 'Dry run complete. No files were changed.' } else { 'Installation complete. Existing unrelated skill packages were not deleted.' }
Write-Host $completion
