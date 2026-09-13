# Sprint, worker, and result contracts

Use contracts for non-trivial delegated work. Keep them proportional; a bounded ticket should not become a specification novel.

## Sprint contract

```text
OBJECTIVE
SCOPE
ACCEPTANCE CRITERIA
VERIFICATION
BOUNDARIES
NON-GOALS
DEPENDENCIES
STOP / ESCALATION CONDITIONS
```

Constrain outcomes and invariants more strongly than implementation style. Classify user-supplied numerical targets as hard requirements or engineering goals; never silently promote an invented threshold.

## Worker ticket

```text
TASK ID / OWNER
OBJECTIVE
RELEVANT BACKGROUND
ALLOWED SCOPE — repository, worktree, files, services
MODIFICATION — read-only or write-enabled
CONSTRAINTS / NON-GOALS
DEPENDENCIES
ACCEPTANCE CRITERIA
VERIFICATION TO RUN
OUTPUT FORMAT
BUDGET / DEADLINE
ESCALATE WHEN
```

Give the smallest sufficient context. Explicitly say whether commits, pushes, network access, production access, or destructive actions are allowed; never infer those permissions from delegation.

## Implementation result

```text
STATUS
WORKTREE / COMMIT
FILES CHANGED
WHAT CHANGED
TEST COMMANDS
TEST RESULTS / ARTIFACTS
UNRESOLVED RISKS
ASSUMPTIONS
```

## Investigation result

```text
STATUS
FINDING
EVIDENCE
FILES / SYMBOLS / SOURCES
ROOT-CAUSE HYPOTHESIS
RECOMMENDED NEXT STEP
CONFIDENCE
```

Large evidence belongs in a file or artifact. Return its path and a decision-relevant summary instead of flooding the lead's context.

## Ownership rules

Track task ID, owner, status, dependencies, scope, verification, and artifact or commit. Only one modifying owner may hold a scope at a time. Read-only overlap is allowed when deliberate independent verification is worth the cost.
