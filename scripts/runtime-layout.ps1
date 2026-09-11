function Get-RuntimeSkillDirectories {
    param([Parameter(Mandatory)][string]$Root)

    if (-not (Test-Path -LiteralPath $Root)) { return }
    foreach ($categoryDir in Get-ChildItem -Directory -LiteralPath $Root) {
        foreach ($subcategoryDir in Get-ChildItem -Directory -LiteralPath $categoryDir.FullName) {
            foreach ($skillDir in Get-ChildItem -Directory -LiteralPath $subcategoryDir.FullName) {
                if (Test-Path -LiteralPath (Join-Path $skillDir.FullName 'SKILL.md')) {
                    [pscustomobject]@{
                        Directory = $skillDir
                        Category = $categoryDir.Name
                        Subcategory = $subcategoryDir.Name
                    }
                }
            }
        }
    }
}
