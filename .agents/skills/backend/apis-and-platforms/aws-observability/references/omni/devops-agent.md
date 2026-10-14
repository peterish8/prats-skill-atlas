# Handing Off Investigations to the AWS DevOps Agent

CloudWatch Omni can hand deep, autonomous investigations off to the **AWS DevOps
Agent**. Omni handles the conversation and the UI; for a hard "why is this
broken?" it delegates to the AWS DevOps Agent and brings the findings back into
the Omni experience.

> **The AWS DevOps Agent is an AWS AI agent — a distinct AWS feature, not a part of
> CloudWatch Omni.** It is an AI-powered, always-available agent that autonomously
> investigates operational issues across your AWS, multicloud, and on-premises
> environments, correlating telemetry, code, and deployment data to find the root
> cause. Learn more:
> [About AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html).

This reference covers **using** a connected DevOps Agent — when to hand an
investigation off and how to read what it returns. **Connecting** the DevOps Agent
to a Space (the connect flow, the Space operator role's managed policies) is
first-time setup — see the **setting-up-cloudwatch-observability** skill's
`devops-agent-integration` reference for that.

## When to hand off an investigation

Reach for a delegated AWS DevOps Agent investigation when the ask is a **deep,
cross-service root cause**, not a quick lookup:

- "**Why** is this service slow / erroring / broken?" — open-ended, multi-service
  root-cause questions.
- Incidents that span several services or accounts and need correlation you can't
  reach in a single step.
- A long-running, autonomous investigation you want to run while you do other work.

Handle quick metric checks, log lookups, and single-step questions directly in
CloudWatch Omni — they don't need the DevOps Agent. For a full root cause of an
incident or a surfaced insight, the DevOps Agent is the best option.

## How to hand off

You don't drive the DevOps Agent step by step — you hand it a problem and it runs
an autonomous, end-to-end investigation. From CloudWatch Omni:

- Ask a root-cause question in the conversation (e.g. "why is checkout erroring?"),
  or hand off from an **alarm** or a surfaced **insight** you're looking at.
- Omni delegates to the DevOps Agent space connected to your Space (see the
  setup reference) and the investigation runs on its own — it may take several
  minutes for a deep one.
- Omni surfaces the investigation as it runs and brings the results back into the
  conversation, so you can act on them without leaving Omni.

The DevOps Agent investigates using the access configured in the connected AWS
DevOps Agent space, and can reach beyond CloudWatch — correlating against the
observability, code, and CI/CD tools you've connected to it.

## What it produces — and how to interpret it

A delegated investigation returns more than a chart. Read its output in these
layers:

- **Root cause** — the specific fault it settled on, reached by correlating
  telemetry, code, and deployment data. Treat this as the headline: the "what
  broke and why," not just "what alarmed."
- **Impact path and blast radius** — the DevOps Agent builds and continuously
  updates an application topology of your resources and their relationships, and
  uses it to show the affected components, trace the impact path, and scope the
  blast radius (including across connected accounts). Use this to judge how far the
  issue reaches before you act.
- **Mitigation plan** — after settling on a root cause it usually **proposes**
  specific actions to resolve the issue, validate the fix, and revert if needed.
  These are proposals for you to review and apply — it presents the plan, it does
  not silently change your resources.
- **Correlated incidents** — it consolidates related incidents into a single
  investigation, so one set of findings can explain several symptoms; don't read
  the consolidated symptoms as separate root causes.
- **Proactive recommendations** — separately from a live incident, it analyzes
  patterns across past incidents and recommends improvements (observability,
  infrastructure, governance, and code optimization) so the same problems don't
  recur.

Its investigations and recommendations get sharper over time as it learns your
environment, so early results may be less precise than later ones. (The DevOps
Agent also has release-management capabilities — reviewing release readiness and
testing changes before they ship — currently in preview and separate from the
investigation work CloudWatch Omni delegates to it.)
