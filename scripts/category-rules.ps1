function Get-SkillPlacement {
    param([Parameter(Mandatory)][string]$Name)

    if ($Name -match '^gsd-') { return [pscustomobject]@{ Category = 'agent-workflows'; Subcategory = 'gsd' } }
    if ($Name -match '^gstack') { return [pscustomobject]@{ Category = 'agent-workflows'; Subcategory = 'gstack' } }
    if ($Name -match 'agent|grill|grilling|interrogate|handoff|swarm|parallelizing|routing|recovering|verifying|adaptive|classifying|decomposing|executing|context-|summarize-context|principle-|full-output|figure-it-out|^(bro|how|why|recall|reflect|unslop|poteto)$') { return [pscustomobject]@{ Category = 'agent-workflows'; Subcategory = 'coordination' } }
    if ($Name -match 'plan|project-manager|product-manager|product-to-launch|to-prd|to-spec|to-questionnaire|to-tickets|to-issues|milestone|roadmap|scaffold') { return [pscustomobject]@{ Category = 'planning'; Subcategory = 'project-planning' } }
    if ($Name -match 'architect|architecture|codebase-design|improve-codebase|domain-modeling|system-design|ubiquitous-language') { return [pscustomobject]@{ Category = 'architecture'; Subcategory = 'system-design' } }
    if ($Name -match 'security|bug-bounty|authorized|harden|turnstile') { return [pscustomobject]@{ Category = 'security'; Subcategory = 'appsec-and-privacy' } }
    if ($Name -match 'accessibility|qa|test|tdd|debug|diagnos|audit|perf|performance|playwright') { return [pscustomobject]@{ Category = 'testing'; Subcategory = 'qa-and-verification' } }
    if ($Name -match 'expo|react-native|swiftui|jetpack|kotlin|ios|android|mobile') { return [pscustomobject]@{ Category = 'mobile'; Subcategory = 'native-and-cross-platform' } }
    if ($Name -match '^frontend|^nextjs|^react|vercel-react|tailwind|web-|browser|landing-page|ui-|ux-|scroll|json-canvas|building-native-ui|use-dom') { return [pscustomobject]@{ Category = 'frontend'; Subcategory = 'web-ui' } }
    if ($Name -match 'animation|motion|gsap|framer|tactile|micro|industrial|minimalist|stitch|image-to-code|imagegen|visual|brand|taste|design') { return [pscustomobject]@{ Category = 'design'; Subcategory = 'visual-and-motion' } }
    if ($Name -match 'backend|fullstack|api|cloudflare|workers|wrangler|durable|convex|supabase|neon|typescript|native-data-fetching|graphql|database') { return [pscustomobject]@{ Category = 'backend'; Subcategory = 'apis-and-platforms' } }
    if ($Name -match 'git|deploy|vercel|setup|release|circleci|sandbox|ship|upgrade|migrate|workflow-manager') { return [pscustomobject]@{ Category = 'devops'; Subcategory = 'delivery-and-tooling' } }
    if ($Name -match 'firecrawl|seo|research|analytics|editorial|gavel|financial|content|copywriter|data') { return [pscustomobject]@{ Category = 'research-data'; Subcategory = 'research-seo-and-content' } }
    if ($Name -match 'writing|document|docs|markdown|readme|prd|spec|proposal|questionnaire|tickets|issues|article|technical-writing') { return [pscustomobject]@{ Category = 'docs'; Subcategory = 'writing-and-specs' } }
    if ($Name -match 'mcp|figma|canva|google|obsidian|connect|airtable|openai|sora|defuddle') { return [pscustomobject]@{ Category = 'integrations'; Subcategory = 'platform-tools' } }
    if ($Name -match 'legal|sales|customer|klyna|education|school|campus|finance') { return [pscustomobject]@{ Category = 'specialists'; Subcategory = 'domain-workflows' } }
    if ($Name -match 'skill|changelog|behuman|brainstorm|caveman|find-skills|teach|wayfinder|wizard|prototype|review|triage') { return [pscustomobject]@{ Category = 'tools-utilities'; Subcategory = 'general-purpose' } }

    return [pscustomobject]@{ Category = 'other'; Subcategory = 'uncategorized' }
}
