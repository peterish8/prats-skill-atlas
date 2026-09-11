---
name: routing-agent-tools
description: Use when more than one tool, API, CLI, browser, simulator, or computer-use interface could perform or verify the task.
---

# Choose the execution interface

Choose the interface that gives the best reliability and evidence for this specific operation. When capabilities are equivalent, prefer:

```text
structured native tool -> API or MCP -> CLI -> browser automation -> general computer use
```

This is a preference, not a prohibition. Use the actual UI, browser, simulator, or device when UI behavior, gestures, rendering, or accessibility need validation. Prefer real Git and structured data access over imitating them in a GUI. If an interface fails, switch only after diagnosing whether the problem is transient, authorization-related, environment-specific, or a genuine capability gap.
