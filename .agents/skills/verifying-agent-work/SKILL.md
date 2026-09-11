---
name: verifying-agent-work
description: Use before claiming a requested implementation, fix, research result, configuration, or UI change is complete.
---

# Verify evidence before completion

Choose the smallest evidence set that convincingly tests the requested outcome and its most relevant regression risk.

| Work | Minimum useful evidence |
| --- | --- |
| Code change | Targeted type/build/test check; add runtime or integration evidence when the request depends on it. |
| Bug fix | Reproduce or identify failure, apply fix, show the failure no longer occurs, and check nearby regression risk. |
| UI behavior | Render and exercise the requested flow; inspect runtime errors and relevant responsive/visual state. |
| Research | Use reliable, preferably primary evidence; cross-check claims that matter or remain uncertain. |
| Configuration | Inspect resulting state and exercise the real endpoint, service, or integration when possible. |

Clearly distinguish `implemented`, `verified`, and `not verified`. A blocked runtime, unavailable credential, or unrun device test is a limit to report, not permission to declare success. On failed verification, return evidence to `recovering-agent-failures`.
