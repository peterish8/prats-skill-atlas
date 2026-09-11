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

$roots = [ordered]@{
    Claude = Join-Path $repoRoot '.claude\skills'
    Codex = Join-Path $repoRoot '.codex\skills'
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
                presentIn = @()
                paths = [ordered]@{}
            }
        }
        $records[$skillDir.Name].presentIn += $rootName
        $records[$skillDir.Name].paths[$rootName] = ($skillFile.Substring($repoRoot.Length + 1) -replace '\\', '/')
    }
}

$skills = @($records.Values | Sort-Object category, name | ForEach-Object {
    [pscustomobject]@{
        name = $_.name
        category = $_.category
        subcategory = $_.subcategory
        presentIn = @($_.presentIn | Sort-Object)
        paths = $_.paths
    }
})

$json = [ordered]@{
    repository = 'prats-skill-forge'
    runtimeRoots = @('.claude/skills', '.codex/skills', '.agents/skills')
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
        $lines += "- `$($skill.name)` — $rootsText"
    }
    $lines += ''

    $categoryLines = @("# $title", '', "Skills in this category: $($group.Count)", '', '| Skill | Available in |', '| --- | --- |')
    foreach ($skill in $group.Group) {
        $categoryLines += "| `$($skill.name)` | $($skill.presentIn -join ', ') |"
    }
    $safeFile = ($title -replace '/', '--') + '.md'
    Set-Content -LiteralPath (Join-Path $categoryDir $safeFile) -Value ($categoryLines -join [Environment]::NewLine) -Encoding utf8
}
$catalogMarkdown = (($lines -join [Environment]::NewLine).TrimEnd() + [Environment]::NewLine)
Set-Content -LiteralPath (Join-Path $catalogDir 'skills.md') -Value $catalogMarkdown -Encoding utf8 -NoNewline

Write-Host "Generated catalog for $($skills.Count) unique skill packages."
