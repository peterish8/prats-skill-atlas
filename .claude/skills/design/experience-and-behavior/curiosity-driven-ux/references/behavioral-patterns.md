# Behavioral mechanisms extracted from Polaris

Source snapshot: 2026-09-17, commit `390fc6ff1c168e5b14229207c557974ad3f094a1`. Source paths record provenance; this reference is usable without access to that repository.

## What the code does, and what we infer

The observed behavior column describes implementation. The hypothesized benefit is design reasoning to test, not a causal finding.

| Mechanism | Observed behavior | Hypothesized benefit | Adaptation / failure mode |
| --- | --- | --- | --- |
| Bounded invitation | Short survey promise; begin story or go straight to task | Lower uncertainty about effort | Use an honest estimate; do not add a branded intro to every repeat visit |
| Belonging | “Never held one? It's built for you”; novice answers and neutral interest option | Reduce fear of not qualifying | Use the audience's real vocabulary; avoid assuming expertise |
| Concrete purpose | Who → spark → vision → CS connection | Make the task meaningful | Keep it skippable; story is not evidence for all claims it makes |
| Demonstration | Goal bars swap; notation matches cube turns | Explain the idea with a visible relationship | Clearly label illustrations and targets |
| Small actions | Eight steps; text only for contact, cohort/choice taps | Lower effort per decision | Do not fragment a bulk workflow into unnecessary screens |
| Agency | Skip, Back, review edits, pause, reveal-now | Let the person control pace and correctness | These controls must be discoverable, not merely present in source |
| Action ownership | Selected control launches bits toward the cube while a layer turns | Make action and consequence legible | Avoid rewarding one survey opinion more than another |
| Cumulative construction | Eighteen fixed moves across eight milestones form a nested pattern | Create curiosity about the finished object | The result is milestone-driven, not computed from answer preference |
| Competence preview | A real algorithm cycles with highlighted notation | Make a complex skill seem understandable | A demonstration is not the user's earned skill |
| Visible progress | Question count, glossy fill, “a pattern is forming”; full fill after submit success | Clarify destination while giving it character | No fabricated steps or premature “saved” state |
| Reversibility | Past answers visible; steps' cube moves play only once | Make participation safer and correction easy | Keep current data and played-effects ledger separate |
| Ownership | Personal first name, badge pattern choice, live patterned cube | Give the completed result personal relevance | Personalization must improve value; do not collect extra data for ornament |
| Exploration | Eight-pattern wheel, tap to spin, visible arrows | Offer a bounded playful action after required work | Gesture-only discoverability excludes people; keep alternatives |
| Optional expression | Save badge, share, finish, replay | Let users carry or revisit the result voluntarily | Sharing is not a gate; cancellation is neutral |
| Narrative closure | Finale connects learn/compete/grow/personal contribution back to the vision | Give the journey a coherent end | Longer finales need a short/direct route when the product is used often |
| Continuity after detours | Tab draft, history sync, restored cube, clear submission states | Reduce frustration from interruptions | Storage policy and privacy are product-specific |

## Why this feels gamified without a game economy

The frontend uses responsive material, visible construction, milestone progression, object manipulation and a completion gift. The game-like quality comes from the action's consequence, not from a leaderboard of respondents or a currency.

Three layers contribute different things:

```text
Task value:       I expressed a real preference that helps plan the club.
Interaction:      My tap visibly turns the cube and advances the journey.
Completion:       I can keep, customize or share a result that feels mine.
```

Copy the relationship across those layers. Adding a progress bar and confetti to a confusing task does not create the same experience.

The pattern is deliberately deterministic. Every valid answer gets the same construction milestone. Neutral and declining choices still complete the journey and receive the gift. This is an important property of honest research and welcoming onboarding.

## Curiosity with a real payoff

Choose one understandable unresolved question that the task can answer:

- What pattern will my steps reveal?
- What does my learning path connect to next?
- How do these songs sound together?
- Which itinerary fits these constraints?

Show enough of the destination to orient the user. Reveal the result when it is ready. Required pricing, risks, eligibility or consent should not become a mystery. Avoid arbitrary unlocks or a meaningless score just to prolong the journey.

Use anticipation in the scene rather than withholding useful controls. In Polaris, the thank-you and badge action arrive while the celebration plays; opening the badge settles the spectacle instead of forcing it to finish.

## Effort and attention budgets

At each beat, count the decisions, amount of reading, typing and waiting. Prefer fewer than a fixed quota of animations. The source uses short staggered words, constant dock controls and one question at a time, but the implementation's 360ms choice hold and 600ms arrival guard are not proof of a fast journey.

For repeated work, compress the transition and reduce cinematic introductions. Keep visual ownership through a quick state change. For occasional discovery, allow richer object movement. For complex decisions, reduce movement and preserve comparison. These are task-fit judgments, not a universal engagement formula.

## Recovery is part of the appeal

The implementation retains answers locally before submission and restores them after reload; privacy notice navigation can return to the saved task. History entries track scenes and edit origin. A submit UUID is reused for retries, and completion appears after successful persistence. Replay does not submit again.

The portable contracts are:

```text
back/edit       → earlier data stays visible, no repeated construction
reload/detour   → restore according to the app's permitted draft policy
duplicate tap  → one accepted action, no invisible next answer
submit failure → preserve work and show a specific retry route
late success   → associate result with the request that owns it
replay         → visual presentation only
share abort    → result stays available without a failure celebration
```

Do not carry over this survey's retention window, stored identifiers or auto-retry policy to another domain without its product contract.

## Behavior to validate

Use a short representative task, such as “finish this setup, change one answer, then find your result.” Observe quietly before asking for impressions. Include a first-time user, someone wanting to skip, and someone using the static/reduced-motion path. This is a qualitative check, not a statistically valid experiment.

| Question | Evidence to look for | Possible correction |
| --- | --- | --- |
| Does the user understand what is happening? | Can explain the task and object change without prompting | Make relationship and labels clearer |
| Is effort actually low? | Reading/typing/waiting do not interrupt the task; no missed choices | Reduce input and serial delays |
| Is curiosity useful? | Person knows why to continue and the result satisfies the expectation | Clarify destination or improve result value |
| Is control apparent? | Finds Skip, Back, edit, pause and Finish unaided | Improve placement and wording |
| Is exploration voluntary? | Uses spin/picker/replay when desired and can leave promptly | Separate optional play from required flow |
| Is the result credible? | Distinguishes goals from facts and persistence from decoration | Correct copy and success contracts |
| Is the motion comfortable? | Can complete without physical travel and without missing content | Simplify movement and remove long reveal delays |

If the app already has approved measurement, compare task completion, errors, time, correction success and optional exploration before and after. Replay rate alone is ambiguous: it can reflect enjoyment, confusion or a hidden next action. Do not add tracking just to apply this skill. No numeric improvement, retention or addiction claim is supported by this source extraction.

## Provenance map

- `src/components/experience/experience.tsx`: narrative beats, scene transitions, step ledger, replay, navigation, persistence and optional motion control.
- `src/components/experience/survey-docks.tsx`: inputs, conditional batches, choices, review, error copy and explicit submission.
- `src/lib/survey.ts`: eight-step model, welcome/neutral/decline options and pattern contribution.
- `src/lib/journey-store.ts`: tab persistence and history state model.
- `src/components/experience/badge.tsx`: personal result, pattern wheel, spin hint, save/share/finish states.
- `src/lib/submit.ts`, `src/lib/share-badge.ts`: persistence result and share fallback semantics.
- `src/app/privacy/page.tsx`: local draft and locally generated badge explanations.

Research terms such as goal-gradient, competence, curiosity and ownership can be useful lenses, but this skill does not rely on an empirical claim about them. Describe the actual mechanism and test its fit.
