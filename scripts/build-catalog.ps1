[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$catalogDir = Join-Path $repoRoot 'catalog'
New-Item -ItemType Directory -Force -Path $catalogDir | Out-Null
$categoryDir = Join-Path $catalogDir 'categories'
New-Item -ItemType Directory -Force -Path $categoryDir | Out-Null

$roots = [ordered]@{
    Claude = Join-Path $repoRoot '.claude\skills'
    Codex = Join-Path $repoRoot '.codex\skills'
    Agents = Join-Path $repoRoot '.agents\skills'
}

function Get-Category([string]$name) {
    if ($name -match '^(gsd-|gstack|principle-|grill|grilling|interrogate|agent-|adaptive-|classifying-|decomposing-|executing-|parallelizing-|routing-|recovering-|verifying-|context-|summarize-context|handoff|full-output|figure-it-out|how$|why$|bro$|reflect$|recall$|swarm$|unslop$|poteto)') { return 'agent-workflows' }
    if ($name -match 'security|bug-bounty|authorized|harden|turnstile|accessibility|qa|test|tdd|debug|diagnos|audit|perf|performance|playwright') { return 'security-quality' }
    if ($name -match 'expo|react-native|swiftui|jetpack|kotlin|ios|android|mobile') { return 'mobile-native' }
    if ($name -match 'git|deploy|vercel|setup|release|circleci|cloud|sandbox|wrangler|ship|upgrade|migrate') { return 'devops-delivery' }
    if ($name -match 'mcp|figma|canva|google|obsidian|connect|airtable|openai|sora|defuddle|use-dom') { return 'integrations-tools' }
    if ($name -match 'firecrawl|seo|research|analytics|editorial|gavel|financial|content|copywriter|data') { return 'data-research-content' }
    if ($name -match 'writing|document|docs|markdown|readme|prd|spec|proposal|questionnaire|tickets|issues|article|technical-writing') { return 'docs-writing' }
    if ($name -match 'brand|visual|taste|creative|animation|motion|gsap|framer|tactile|micro|industrial|minimalist|stitch|image-to-code|imagegen|high-end-visual|design-(review|consultation|shotgun)|gpt-taste') { return 'design-motion' }
    if ($name -match 'frontend|nextjs|react|tailwind|web-|browser|landing|ui|ux|scroll|json-canvas|vercel-react') { return 'frontend-ui' }
    if ($name -match 'backend|fullstack|api|cloudflare|workers|wrangler|durable|convex|supabase|neon|typescript|native-data-fetching|graphql|database') { return 'backend-platform' }
    return 'other'
}

$records = @{}
foreach ($rootName in $roots.Keys) {
    if (-not (Test-Path -LiteralPath $roots[$rootName])) { continue }
    foreach ($skillDir in Get-ChildItem -Directory -LiteralPath $roots[$rootName]) {
        $skillFile = Join-Path $skillDir.FullName 'SKILL.md'
        if (-not (Test-Path -LiteralPath $skillFile)) { continue }
        if (-not $records.ContainsKey($skillDir.Name)) {
            $records[$skillDir.Name] = [ordered]@{
                name = $skillDir.Name
                category = Get-Category $skillDir.Name
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
foreach ($group in ($skills | Group-Object category | Sort-Object Name)) {
    $lines += "## $($group.Name)"
    $lines += ''
    foreach ($skill in $group.Group) {
        $rootsText = ($skill.presentIn -join ', ')
        $lines += "- `$($skill.name)` — $rootsText"
    }
    $lines += ''

    $categoryLines = @("# $($group.Name)", '', "Skills in this category: $($group.Count)", '', '| Skill | Available in |', '| --- | --- |')
    foreach ($skill in $group.Group) {
        $categoryLines += "| `$($skill.name)` | $($skill.presentIn -join ', ') |"
    }
    Set-Content -LiteralPath (Join-Path $categoryDir "$($group.Name).md") -Value ($categoryLines -join [Environment]::NewLine) -Encoding utf8
}
$catalogMarkdown = (($lines -join [Environment]::NewLine).TrimEnd() + [Environment]::NewLine)
Set-Content -LiteralPath (Join-Path $catalogDir 'skills.md') -Value $catalogMarkdown -Encoding utf8 -NoNewline

Write-Host "Generated catalog for $($skills.Count) unique skill packages."
