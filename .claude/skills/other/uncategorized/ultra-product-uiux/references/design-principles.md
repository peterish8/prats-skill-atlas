# Design principles

Start with the decision the screen must support. Name the user, their intent, what they need to know first, the safest useful next action, and the uncertainty that could stop them.

Use hierarchy deliberately: position, scale, weight, contrast, spacing, grouping, density, and motion are tools—not decoration. A primary action should be obvious because nearby elements are quieter, not because every element is loud.

Establish one visual language before implementation:

- color roles: canvas, surface, elevated surface, text, muted text, border, primary action, status;
- type roles: display, heading, body, label, numeric/data, code where needed;
- a small spacing and radius scale;
- a consistent shadow/elevation rule;
- one icon family and stroke logic;
- a defined treatment for illustrations and images.

Avoid accidental mixtures: sharp and soft geometry without a rule, filled and outlined icon families, unrelated accents, competing button treatments, arbitrary gradients, and effects that impair readability. Use distinction through thoughtful proportions, rhythm, copy, and interaction details.

Design the complete state space. A beautiful populated state is incomplete if loading, empty, error, permission-denied, success, long-content, and narrow-screen states are confusing.

## Decision hierarchy

Use this order when a screen feels busy:

1. Preserve the user’s task and current context.
2. Make the next safe action unmistakable.
3. Put the facts needed to decide near that action.
4. Move detail, secondary actions, and explanation behind progressive disclosure.
5. Remove decorative weight before adding visual effects.

For each large region, write one sentence that starts with “This exists so the user can…”. If it does not support an action, decision, orientation, trust signal, or recovery path, remove it or make it subordinate.

## Content and component resilience

| Situation | Expected treatment |
| --- | --- |
| Long title or name | Wrap naturally, preserve identity, and avoid overlapping controls. |
| Missing image | Use a neutral fallback that keeps the layout and subject identifiable. |
| Zero or empty data | Explain what is absent and how to create or change it. |
| Slow result | Reserve layout space and show what is loading, not a generic spinner alone. |
| Failure | Name the failed action, preserve user input where safe, and offer a concrete retry/recovery. |
| Sensitive action | State consequence, reversible options, and confirmation requirements before committing. |
