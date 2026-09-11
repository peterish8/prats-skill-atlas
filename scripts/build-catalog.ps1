[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$catalogDir = Join-Path $repoRoot 'catalog'
New-Item -ItemType Directory -Force -Path $catalogDir | Out-Null
$categoryDir = Join-Path $catalogDir 'categories'
New-Item -ItemType Directory -Force -Path $categoryDir | Out-Null
. (Join-Path $PSScriptRoot 'runtime-layout.ps1')
. (Join-Path $PSScriptRoot 'category-rules.ps1')

function Get-SkillDescription {
    param([Parameter(Mandatory)][string]$SkillFile)

    $descriptionLine = Get-Content -LiteralPath $SkillFile | Where-Object { $_ -match '^description:\s*' } | Select-Object -First 1
    if (-not $descriptionLine) { return '' }
    return (($descriptionLine -replace '^description:\s*', '').Trim().Trim('"', "'"))
}

$roots = [ordered]@{
    Claude = Join-Path $repoRoot '.claude\skills'
    Codex = Join-Path $repoRoot '.codex\skills'
    Grok = Join-Path $repoRoot '.grok\skills'
    Agents = Join-Path $repoRoot '.agents\skills'
}

$records = @{}
foreach ($rootName in $roots.Keys) {
    foreach ($entry in Get-RuntimeSkillDirectories -Root $roots[$rootName]) {
        $skillDir = $entry.Directory
        $skillFile = Join-Path $skillDir.FullName 'SKILL.md'
        if (-not $records.ContainsKey($skillDir.Name)) {
            $records[$skillDir.Name] = [ordered]@{
                name = $skillDir.Name
                category = $entry.Category
                subcategory = $entry.Subcategory
                description = (Get-SkillDescription -SkillFile $skillFile)
                presentIn = @()
                paths = [ordered]@{}
            }
        }
        $records[$skillDir.Name].presentIn += $rootName
        $records[$skillDir.Name].paths[$rootName] = ($skillFile.Substring($repoRoot.Length + 1) -replace '\\', '/')
    }
}

$skills = @($records.Values | Sort-Object { $_['category'] }, { $_['name'] } | ForEach-Object {
    $record = $_
    [pscustomobject]@{
        name = [string]$record['name']
        category = [string]$record['category']
        subcategory = [string]$record['subcategory']
        description = [string]$record['description']
        presentIn = @($record['presentIn'] | Sort-Object)
        paths = $record['paths']
    }
})

$json = [ordered]@{
    repository = 'prats-skill-atlas'
    runtimeRoots = @('.claude/skills', '.codex/skills', '.grok/skills', '.agents/skills')
    skillCount = $skills.Count
    skills = $skills
} | ConvertTo-Json -Depth 8
Set-Content -LiteralPath (Join-Path $catalogDir 'skills.json') -Value $json -Encoding utf8

$lines = @('# Skill index', '', "Unique skill packages: $($skills.Count)", '')
foreach ($group in ($skills | Group-Object category, subcategory | Sort-Object Name)) {
    $title = ($group.Name -replace ', ', '/')
    $lines += "## $title"
    $lines += ''
    foreach ($skill in $group.Group) {
        $rootsText = ($skill.presentIn -join ', ')
        $description = (($skill.description -replace '\s+', ' ').Trim() -replace '\|', '\\|')
        $suffix = if ($description) { " | $description" } else { '' }
        $lines += ('- ' + [char]96 + $skill.name + [char]96 + ' - ' + $rootsText + $suffix)
    }
    $lines += ''

    $categoryLines = @("# $title", '', "Skills in this category: $($group.Count)", '', '| Skill | Available in | Description |', '| --- | --- | --- |')
    foreach ($skill in $group.Group) {
        $description = (($skill.description -replace '\s+', ' ').Trim() -replace '\|', '\\|')
        $categoryLines += ('| ' + [char]96 + $skill.name + [char]96 + ' | ' + ($skill.presentIn -join ', ') + ' | ' + $description + ' |')
    }
    $safeFile = ($title -replace '/', '--') + '.md'
    Set-Content -LiteralPath (Join-Path $categoryDir $safeFile) -Value ($categoryLines -join [Environment]::NewLine) -Encoding utf8
}
$catalogMarkdown = (($lines -join [Environment]::NewLine).TrimEnd() + [Environment]::NewLine)
Set-Content -LiteralPath (Join-Path $catalogDir 'skills.md') -Value $catalogMarkdown -Encoding utf8 -NoNewline

Write-Host "Generated catalog for $($skills.Count) unique skill packages."
