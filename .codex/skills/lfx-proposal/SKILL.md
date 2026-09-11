---
name: lfx-proposal
description: Shape grounded, evidence-based LFX and open-source mentorship proposals from verified contributor and project information.
---

# lfx-human-proposal-style

A Claude Code skill for shaping mentorship and open-source proposals in a grounded, human, technical, and proposal-ready style.

> Scope: this skill controls layout, structure, tone, pacing, evidence style, and proposal flow.
> It does not invent project facts, PRs, metrics, links, mentor names, or technical claims.

---

## purpose

Use this skill when the user wants a proposal that feels like a real contributor wrote it after actually working in the codebase.

The target style is:

- human but not casual to the point of being careless
- technical but not robotic
- confident but not arrogant
- specific but not overloaded
- structured like a serious mentorship proposal
- grounded in actual contributions and codebase understanding
- written in a natural first-person voice
- built around evidence, not generic motivation

The proposal should feel like this:

- the applicant knows the project
- the applicant has touched the code
- the applicant understands the problem
- the applicant can explain the implementation clearly
- the plan is realistic for 12 weeks
- risks are acknowledged honestly
- the tone sounds like a human developer, not a grant bot

---

## when to use

Use this skill for:

- LFX mentorship proposals
- Google Summer of Code style proposals
- open source internship proposals
- project implementation plans
- fellowship proposals
- technical mentorship applications
- contributor readiness documents
- project-specific proposal PDFs or markdown drafts

Do not use this skill for:

- generic resumes
- cover letters
- marketing landing pages
- academic research statements
- cold emails
- social posts
- inline content generation without user-provided facts

---

## core rule

The proposal must be built from the user's real information.

Never fabricate:

- pull requests
- merged status
- issue numbers
- mentors
- repository architecture
- code paths
- benchmarks
- timelines already agreed by maintainers
- technical limitations
- prior discussions
- Slack messages
- acceptance odds
- contribution counts
- personal background

If information is missing, leave a clear placeholder or ask for it.

Good placeholder:

```md
[Add 2 to 3 specific PRs here, with what you fixed and why each matters for this project.]
```

Bad placeholder:

```md
I have contributed many important fixes and understand the system deeply.
```

---

## user input expected

Before writing a proposal in this style, collect or infer the following:

### required project details

- program name
- term or cycle
- project title
- organization name
- repository URL
- issue URL or project idea link
- mentor names, if available
- expected duration
- project goal in one sentence

### required applicant details

- name
- GitHub username
- email
- university or school
- year or current status
- timezone or location
- LinkedIn or portfolio, if available

### required contribution details

- merged PRs
- open PRs
- important PRs
- tests written
- bugs fixed
- architecture areas explored
- code files touched
- maintainer interactions

### required technical context

- current system behavior
- project gap
- why the gap matters
- current limitations
- proposed architecture
- files to modify
- testing strategy
- risk areas
- fallback plan

---

## output formats

The skill can produce:

- markdown proposal draft
- structured outline
- PDF-ready markdown
- review checklist
- section-by-section rewrite
- skeleton with placeholders
- Claude Code prompt for proposal generation

Default output should be markdown.

---

## golden style principles

1. Start with real context, not motivational fluff.
2. Use first person where personal experience matters.
3. Use direct sentences.
4. Prefer evidence over adjectives.
5. Make technical depth readable.
6. Use concrete codebase details.
7. Explain why each contribution matters for the proposed project.
8. Show mistakes and learning when useful.
9. Keep claims grounded.
10. Use headings that sound clear, not corporate.
11. Use tables only when they improve scanning.
12. Use bullets for deliverables, not for every paragraph.
13. Use code snippets only when they prove architecture understanding.
14. Use milestones after each phase.
15. Include risks and backup plans.
16. Close with availability and commitment.
17. Avoid fake polish.
18. Avoid generic passion paragraphs.
19. Avoid buzzword stacking.
20. Avoid overclaiming expertise.

---

## tone profile

The tone should sound like a strong contributor explaining the proposal to maintainers.

Target voice:

- simple
- honest
- specific
- slightly conversational
- technically grounded
- calm
- confident
- readable

It should not sound like:

- an AI-generated essay
- a university assignment
- a corporate strategy memo
- a startup pitch
- a motivational speech
- a keyword-stuffed resume

---

## human-like writing commands

When generating or rewriting, apply these commands strictly:

- Write like a real developer wrote this after working in the repo.
- Use natural first-person phrasing where appropriate.
- Do not use em dashes.
- Do not use over-polished LinkedIn language.
- Do not use phrases like passionate about, excited to leverage, robust solution, cutting-edge, seamless, transformative, or deeply passionate.
- Use contractions when they sound natural.
- Prefer short and medium sentences.
- Break long technical explanations into smaller paragraphs.
- Use specific nouns instead of vague nouns.
- Explain technical points like you are talking to a maintainer who knows the project.
- Use plain English before heavy terminology.
- Do not sound like a brochure.
- Do not force perfect symmetry between sections.
- Let some paragraphs feel human and slightly uneven.
- Use active voice.
- Do not say I believe unless it adds honesty.
- Do not say I am confident without proving why.
- Use concrete examples from PRs, files, bugs, and tests.
- Do not exaggerate.
- Do not invent emotional struggle.
- Mention debugging difficulty only if the user provided it or it is grounded in facts.
- Do not include fake humility.
- Do not include generic gratitude paragraphs.
- Keep capitalization normal, not hype style.
- Prefer I worked on, I traced, I fixed, I tested, I learned.
- Never write as if the applicant already completed the proposed project.
- Do not use filler transitions like furthermore, moreover, additionally too often.
- Use phrases like here’s the gap, this is the part I want to fix, the tricky part is, the plan is.
- Allow simple sentences like That’s the gap.
- Use technical confidence through specificity.
- Make every paragraph do a job.

---

## forbidden phrases

- `passionate about technology`
- `leverage my skills`
- `robust and scalable solution`
- `seamless integration`
- `cutting-edge technologies`
- `game-changing`
- `transformative impact`
- `synergize`
- `utilize my expertise`
- `deeply fascinated by`
- `ever since childhood`
- `I am the perfect fit`
- `I guarantee success`
- `world-class`
- `revolutionary`
- `highly motivated individual`
- `strong foundation in computer science`
- `keen interest in open source`
- `I would be honored`
- `I will work tirelessly`
- `this opportunity aligns perfectly with my career goals`
- `my diverse skill set`
- `end-to-end holistic solution`
- `industry-standard best practices`
- `state-of-the-art`
- `next-generation`

---

## preferred phrases

- `I found the project while...`
- `The architecture caught my attention because...`
- `I started with...`
- `When I saw this project idea, it felt like a natural next step.`
- `Here’s the actual gap.`
- `The tricky part is...`
- `This matters because...`
- `I already ran into a similar problem in...`
- `That PR matters here because...`
- `The plan is to...`
- `If this part gets blocked, I’ll...`
- `By the end of this phase...`
- `The goal is not to replace everything, but to...`
- `This keeps the existing behavior unchanged.`
- `I want to make this useful for future contributors too.`
- `That’s the gap I want to fill.`
- `This is where the integration logic comes in.`

---

## document structure

Use this structure unless the user asks for a different one.

### cover page

Program, project title, mentors, GitHub issue, applicant contact details.

### how i found the project

A short origin story tied to codebase or issue discovery.

### why i want to work on this

Explain the real gap and why it matters to users or maintainers.

### why i am a good fit

Summarize contributions, codebase familiarity, and work habits.

### 3 prs that show i can do this

A table connecting past PRs to the proposed project.

### all my work

A compact contribution history table.

### what i know

Skills tied to actual work, not generic skill listing.

### the plan

A 12-week implementation plan.

### what is the problem

Plain explanation of the current limitation.

### architecture context

How the current system works.

### technical design

Step-by-step design with code-path references.

### files i will work on

Concrete file or directory list.

### week-by-week breakdown

Phases, weeks, deliverables, tests, milestones.

### testing strategy

Test tools, test types, examples.

### timeline summary

Compact table of phases, weeks, tests, deliverables.

### target metrics

Measurable goals.

### what could go wrong

Risk table with mitigation.

### availability

Timezone, weekly hours, communication plan.

### closing

Brief, grounded final note.

---

## cover page rules

The cover page should be simple and proposal-like.

Include:

- program name
- term
- project title
- mentor names
- GitHub issue or project link
- name and contact information
- GitHub username
- email
- university
- year
- LinkedIn or portfolio

Do not include motivational paragraphs on the cover page.

Keep it clean.

Example structure:

```md
# LFX Mentorship 2026 Spring Term

## Project Title

Mentors: [mentor names]
GitHub Issue: [org/repo#issue]

## Name and Contact Information

Name: [name]
GitHub: [username]
Email: [email]
University: [university]
Current Year: [year]
LinkedIn: [link]
```

---

## section: how i found the project

Purpose:

- show natural discovery
- show the project genuinely caught the applicant’s attention
- connect discovery to later contributions

Structure:

1. Where the applicant found the project.
2. What architectural detail caught attention.
3. What the applicant started with.
4. Why this specific mentorship idea became a natural next step.

Style rules:

- 2 to 4 paragraphs
- first person
- no grand claims
- mention real architecture only
- mention real PRs only if provided

Template:

```md
I found [project] while [real discovery path]. The [architecture/component] caught my attention because [specific reason]. It looked like the kind of system where I could learn by actually contributing, not just reading docs.

I started with [small contribution type], then moved into [bigger contribution type]. When I saw the mentorship idea for [project idea], it felt like a natural next step because I had already worked around [related subsystem].
```

---

## section: why i want to work on this

Purpose:

- explain the real pain point
- show why the project matters
- show applicant motivation through technical friction

Structure:

1. Name the pain clearly.
2. Give a concrete example of the friction.
3. Explain why users or contributors care.
4. Connect applicant interest to the codebase.

Style rules:

- human opening is allowed
- avoid generic passion
- do not overdo emotional language
- use one concrete example

Good opening patterns:

```md
Here’s the thing: [current system] works, but [specific limitation].
```

```md
I’ve already run into this problem while working on [PR/subsystem].
```

```md
The gap is not that [project] lacks tests/features completely. The gap is that there is nothing in between [existing option A] and [existing option B].
```

---

## section: why i am a good fit

Purpose:

- summarize credibility
- connect applicant history to project execution
- give maintainers confidence

Rules:

- include identity briefly
- include contribution count if verified
- include merged/open PRs if verified
- include codebase areas touched
- include work habit only if specific

Avoid:

- I am the best candidate
- I am extremely passionate
- I have always loved open source

Template:

```md
I’m [name], [brief background]. I’ve spent the last [time period] working in [project/repo], mostly around [subsystems]. So far, I’ve [verified contribution summary].

The main reason I think I’m a good fit is that this project sits close to the code I’ve already worked on: [specific connection]. I’m not starting from zero here.
```

---

## section: 3 prs that show i can do this

This is one of the most important sections.

Use a table.

Columns:

- PR
- What I did
- Why it matters for this project

Rules:

- choose only 3 strong PRs
- each PR must connect directly to project work
- explain the debugging or implementation briefly
- say why it matters in practical terms
- avoid listing PRs without interpretation

Table template:

```md
| PR | What I did | Why it matters for this project |
|---|---|---|
| #[number]: [short title] | [2 to 4 sentences about the real work] | [direct link to proposed project responsibility] |
| #[number]: [short title] | [2 to 4 sentences about the real work] | [direct link to proposed project responsibility] |
| #[number]: [short title] | [2 to 4 sentences about the real work] | [direct link to proposed project responsibility] |
```

Good connection examples:

- A controller bug fix proves ability to reason about reconciliation loops.
- A test framework PR proves ability to build reusable test utilities.
- A race condition fix proves ability to handle concurrency risks.
- A webhook fix proves ability to understand request lifecycle.
- A cache bug fix proves ability to test state consistency.

---

## section: contribution history

Purpose:

- make the proposal feel evidence-heavy
- show consistency
- let maintainers scan work quickly

Use tables.

Recommended split:

- merged PRs
- open PRs
- draft PRs or PoCs

Columns:

- PR
- Description
- Status

Rules:

- keep descriptions short
- use exact statuses
- do not inflate status
- mention release cherry-picks only if verified

---

## section: what i know

Purpose:

- list technical skills through actual project use

Format:

- bullet list
- each skill gets one sentence

Bad:

```md
- Kubernetes: advanced
```

Good:

```md
- Kubernetes internals: Controllers, informers, CRDs, and reconciliation loops. I learned most of this by fixing bugs in [project].
```

Rules:

- do not include every technology the applicant knows
- only include skills relevant to the proposal
- connect skills to contribution evidence

---

## section: the plan

Use a clean title.

Good titles:

- `The Plan — 12 Weeks`
- `Project Proposal: 12-Week Implementation Plan`
- `Week-by-Week Breakdown`

Avoid:

- `Comprehensive Strategic Roadmap`
- `Implementation Paradigm`
- `Execution Blueprint for Transformative Delivery`

---

## problem statement rules

The problem statement should be plain and specific.

Structure:

1. What exists now.
2. What is missing.
3. Why users or contributors suffer.
4. What the proposed project changes.

Use a small table if there is a comparison.

Example table:

```md
| What users want | What they get now |
|---|---|
| [desired workflow] | [current limitation] |
| [desired workflow] | [current limitation] |
```

Rules:

- make the gap obvious
- do not start with abstract definitions
- do not over-explain the entire project
- keep the problem close to the mentorship idea

---

## architecture context rules

Purpose:

- prove the applicant understands the current system

Include:

- major components
- relevant controllers
- relevant files
- current data flow
- important edge cases
- why the design is tricky

Style:

- explain in plain English first
- then include code paths or snippets
- do not dump huge code
- code snippets should be short and purposeful

Good pattern:

```md
The important part is [subsystem]. It currently does [behavior]. I traced this while working on [PR/subsystem], and the tricky bit is [edge case].
```

Then optionally:

```md
Relevant files:
- `pkg/...`
- `cmd/...`
- `apis/...`
```

---

## code snippet rules

Use code snippets only when they show real architecture understanding.

Allowed snippets:

- simplified pseudocode
- actual code path excerpt provided by user
- new API struct proposal
- controller reconciliation sketch
- validation logic sketch
- test example names

Rules:

- keep snippets under 40 lines when possible
- add a sentence before and after each snippet
- do not include code just to look technical
- do not invent exact code if not sure
- label pseudocode as pseudocode
- preserve project style when user provides real code

Bad:

```md
Here is a huge 150-line implementation.
```

Good:

```md
The controller logic can stay small. The main job is to read the external scaling intent, validate it against project state, then update the custom resource only when safe.
```

---

## technical design section

This section should be step-based.

Recommended structure:

```md
## Technical Design

### Step 1: [CRD/API change]
[Explain what changes and why.]

### Step 2: [Controller or core logic]
[Explain the control flow.]

### Step 3: [Validation/safety]
[Explain edge cases and safeguards.]

### Step 4: [Tests/observability/docs]
[Explain how users and maintainers verify behavior.]
```

Rules:

- use step titles
- keep each step tied to a file or component
- explain why the step exists
- avoid making a giant unordered list

---

## files i will work on

Purpose:

- show that the plan is concrete

Format:

```md
Files I’ll work on:

- `path/to/file.go`
- `path/to/new_file.go`
- `docs/path.md`
- `test/path/...`
```

Rules:

- distinguish new files from modified files if useful
- do not invent paths
- if paths are uncertain, write `[likely path]`

---

## week-by-week plan

Use 4 phases for a 12-week project.

Default structure:

- Phase 1: foundation
- Phase 2: core implementation
- Phase 3: advanced integration
- Phase 4: hardening, docs, CI

Each phase should include:

- goal
- weeks
- bullet deliverables
- milestone
- approximate test count if relevant

Template:

```md
### Phase 1 — [Name] (Weeks 1–3)

Goal: [one sentence]

- [deliverable]
- [deliverable]
- [deliverable]

Milestone: [clear success condition]
```

Rules:

- do not make every week equally detailed unless needed
- add sub-week details where complexity matters
- make milestones measurable
- keep phase names simple

---

## milestone rules

Milestones should be concrete.

Good:

- `make test-integration passes locally without a cluster.`
- `Basic HPA scaling works with validation enabled.`
- `Full validation pipeline blocks unsafe scale-downs.`
- `CI job runs the new suite with coverage reporting.`

Bad:

- `Project foundation completed.`
- `System improved significantly.`
- `Architecture becomes robust.`

---

## testing strategy

Always include testing.

Recommended content:

- test framework
- unit tests
- integration tests
- envtest or local API server if relevant
- mock strategy
- race tests if concurrency exists
- example test names
- CI integration

Example format:

```md
Testing strategy:

- Use [tool] for [purpose].
- Run [command] locally and in CI.
- Add tests for [edge case].
- Use `go test -race` where concurrency is involved.

Example tests:

- `Test[Component]Blocks[UnsafeCase]`
- `Test[Component]Allows[SafeCase]`
- `Test[Component]Handles[FailureCase]`
```

---

## timeline summary table

Use a compact table near the end.

Template:

```md
| Phase | Weeks | Tests | Key Deliverable |
|---|---:|---:|---|
| 1 — Foundation | 1–3 | [count] | [deliverable] |
| 2 — Core Logic | 4–6 | [count] | [deliverable] |
| 3 — Advanced Integration | 7–9 | [count] | [deliverable] |
| 4 — Hardening | 10–12 | [count] | [deliverable] |
| Total | 12 | [count] | [final outcome] |
```

Rules:

- use realistic numbers
- avoid fake precision
- do not promise impossible coverage

---

## target metrics

Purpose:

- show success can be measured

Use bullets.

Examples:

- CI time
- controller latency
- test count
- coverage for new code paths
- startup time
- per-test overhead
- response time
- migration count

Rules:

- use metrics only when meaningful
- do not invent benchmarks
- mark estimates as targets
- compare against current state only if verified

---

## risk section

Use the heading:

`What Could Go Wrong`

or

`Risks & Mitigation`

Use a table.

Columns:

- Risk
- Impact
- How I’ll handle it

Template:

```md
| Risk | Impact | How I’ll handle it |
|---|---|---|
| [risk] | [impact] | [specific fallback] |
```

Rules:

- include real technical risks
- do not include fake risks like I might work too hard
- include fallback paths
- say when something becomes a stretch goal

Good risk examples:
