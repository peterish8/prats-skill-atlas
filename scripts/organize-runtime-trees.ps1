[CmdletBinding(SupportsShouldProcess)]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
. (Join-Path $PSScriptRoot 'category-rules.ps1')

$roots = @('.claude\skills', '.codex\skills', '.grok\skills', '.agents\skills')
$moved = 0

foreach ($relativeRoot in $roots) {
    $root = Join-Path $repoRoot $relativeRoot
    $flatSkills = @(Get-ChildItem -Directory -LiteralPath $root | Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') })
    foreach ($skill in $flatSkills) {
        $placement = Get-SkillPlacement -Name $skill.Name
        $destinationParent = Join-Path $root (Join-Path $placement.Category $placement.Subcategory)
        $destination = Join-Path $destinationParent $skill.Name
        if (Test-Path -LiteralPath $destination) { throw "Destination already exists: $destination" }
        New-Item -ItemType Directory -Force -Path $destinationParent | Out-Null
        if ($PSCmdlet.ShouldProcess($skill.FullName, "Move to $destination")) {
            Move-Item -LiteralPath $skill.FullName -Destination $destination
            $moved++
        }
    }
}

Write-Host "Organized $moved skill packages."
