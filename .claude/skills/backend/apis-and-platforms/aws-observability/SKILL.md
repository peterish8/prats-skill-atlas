---
name: aws-observability
description: >-
  Builds, configures, debugs, and optimizes AWS observability: CloudWatch Log Insights,
  metric/composite/anomaly alarms, dashboards, custom metrics/EMF, X-Ray tracing,
  ADOT collector config, CloudTrail auditing, synthetics/canaries, and Dynamic Instrumentation
  (live breakpoints/snapshots without redeploy). Owns Application Signals onboarding:
  instrumenting a service (Python, Node.js, Java, or .NET on EC2, ECS, EKS, or Lambda)
  with the ADOT SDKs so it appears as a monitored service in Application Signals,
  enabling ServiceEvents, and propagating CI/CD git and deployment metadata via Terraform
  or deployment manifests. Also covers CloudWatch Omni (log/trace queries, dashboards,
  alerts, views, DevOps Agent handoff) and running online/continuous trace evaluations
  on a deployed agent's OTel traces against evaluation datasets (create/list/enable/disable/delete).
  Not for app logging, security threat detection, or evaluating SageMaker/Bedrock
  models.
version: 4
---

# AWS Observability

## Overview

Domain expertise for AWS observability across metrics, logs, and traces, covering the full lifecycle: **enabling/onboarding** a service to Application Signals using ADOT (AWS Distro for OpenTelemetry) auto-instrumentation SDKs and ServiceEvents — making the service show up in Application Signals — on EC2, ECS, EKS, and Lambda in Python, Node.js, Java, and .NET.

**Works best with** the [AWS MCP server](https://docs.aws.amazon.com/aws-mcp/) — enables running CLI commands, querying CloudWatch, and validating configurations directly. All guidance also works with standard AWS CLI access.

**Note:** Reference files contain specific runtime versions, quota values, and feature matrices that may change. When precision matters (e.g., deploying to production, choosing a runtime, or checking a quota), confirm values against current AWS documentation rather than relying solely on the values in these files.

## Detect the environment first: CloudWatch Omni vs. classic CloudWatch

Some requests can be served by **CloudWatch Omni** (Application/Agent Observability — Spaces, Omni SQL, Omni alerts, Omni dashboards) or by **classic CloudWatch** (Log Insights, metric/composite alarms, classic dashboards), and the natural wording ("set up an alert for high latency", "build a dashboard") does not say which. Classic CloudWatch answers under `aws cloudwatch`; Omni's control plane answers under `aws cloudwatch-omni`. Because the wording alone does not reveal which the user means, detect the environment before acting rather than guess.

**Before routing any request that could be either, determine whether Omni is enabled in the target Region:**

```
aws___call_aws → aws cloudwatch-omni list-domains
aws___call_aws → aws cloudwatch-omni list-spaces        # scope to the target Region
```

- **A Domain and a Space exist in the target Region →** Omni is enabled; the Omni rows below apply.
- **No Space (or Omni not enabled) →** route the same user need to its **classic CloudWatch** equivalent instead — alarms → [alarms.md](references/alarms.md), dashboards → [dashboards.md](references/dashboards.md), queries → [log-insights.md](references/log-insights.md), metrics → [metrics.md](references/metrics.md).
- **Ambiguous but the user names the product** ("Omni", "Application Observability", a `spaceId`) → take that as the signal; otherwise probe first, and only ask the user if the probe is inconclusive.

A Space is **one per account per Region** — always probe the Region the request targets, not just the default one. An Omni query against the wrong Region returns an empty result that is easily misread as "no data."

Rows below that route into `references/omni/…` or `references/omni-agents.md` are **Omni-only**: they assume this check found a Space. If it did not, serve the equivalent need from the classic-CloudWatch references above.

## Routing

| User need | Action |
|-----------|--------|
| Enabling/onboarding a service to Application Signals (auto-instrumentation) | Read [application-signals-onboarding.md](references/application-signals-onboarding.md) |
| Propagating ServiceEvents git/deployment metadata through CI/CD | Read [application-signals-cicd-metadata.md](references/application-signals-cicd-metadata.md) |
| Per-platform/per-language enablement steps | Read the matching `references/appsignals-guides/<platform>-<language>.md` (e.g. [eks-python.md](references/appsignals-guides/eks-python.md)) |
| Writing Log Insights queries (pipe-delimited syntax: fields, filter, stats, sort, parse, display) | Read [log-insights.md](references/log-insights.md) |
| Configuring alarms (metric, composite, anomaly) | Read [alarms.md](references/alarms.md) |
| Publishing custom metrics or using EMF | Read [metrics.md](references/metrics.md) |
| Setting up X-Ray tracing or ADOT | Read [tracing.md](references/tracing.md) |
| Building dashboards | Read [dashboards.md](references/dashboards.md) |
| Debugging observability issues | Read [troubleshooting.md](references/troubleshooting.md) — starts with the 5 most common fixes |
| Debugging canary failures | Read [synthetics.md](references/synthetics.md) — see Common failures table |
| CloudTrail operational auditing | Read [cloudtrail.md](references/cloudtrail.md) |
| Setting up Lambda monitoring with CDK | Use [alarm-template.ts](assets/alarm-template.ts) as a starting point |
| Creating synthetic canaries | Read [synthetics.md](references/synthetics.md) |
| Configuring ADOT collector | Use [otel-config.yaml](assets/otel-config.yaml) as a starting point |
| Debugging a running service with breakpoints/snapshots — Dynamic Instrumentation (**modifies live services and capture live data**) | Read [dynamic-instrumentation.md](references/dynamic-instrumentation.md) in full before acting. Confirm with the user before any create/delete, and narrate before significant actions: observation → hypothesis → proposed action → expected result. Diagnosing running-service root cause from source/code inspection. Source inspection alone identifies hypotheses, not confirmed root causes. Keep suspected causes tentative until runtime evidence confirms them. |
| Building evaluation datasets from traces or scoring agents | Read [references/omni-agents.md](references/omni-agents.md) for dataset curation and on-demand/online evaluation via AgentCore APIs |
| Evaluating/scoring an agent's quality, choosing which evaluator to use, or checking whether it picks the right tools | Read [references/omni-agents.md](references/omni-agents.md) — evaluator discovery + on-demand scoring via AgentCore APIs |
| Scoring a specific trace on demand, or reading back evaluation scores from earlier runs | Read [references/omni-agents.md](references/omni-agents.md) — on-demand `evaluate` and querying stored `gen_ai.evaluation.*` scores |
| Setting up continuous/online evaluation of a live agent, or authoring a custom (e.g. brand-voice) evaluator | Read [references/omni-agents.md](references/omni-agents.md) — online-evaluation config and custom evaluator authoring |
| Auditing whether an agent's instrumentation is healthy and traces are flowing | Read [references/omni-agents.md](references/omni-agents.md) — staged instrumentation audit |
| Writing SQL queries for logs and traces in CloudWatch Omni (SELECT ... FROM logs.default / traces.default / default — Application Observability or Agent Observability), including TABLESAMPLE (n PERCENT) table sampling | Read [references/omni/log-trace-query.md](references/omni/log-trace-query.md) |
| Creating, managing, or querying views in CloudWatch Omni (FROM view.<name> — named reusable SQL queries) | Read [references/omni/views.md](references/omni/views.md) |
| When and how to hand an investigation off to the AWS DevOps Agent for cross-service root-cause analysis, and how to interpret its findings | Read [references/omni/devops-agent.md](references/omni/devops-agent.md) |
| Building or authoring a dashboard in CloudWatch Omni (panels[] body, panel types, the nine visualizations, the 60-column grid, archetype templates) | Read [references/omni/dashboard.md](references/omni/dashboard.md) |
| Working with a CloudWatch Omni **alert** on an Omni-enabled account — any question mentioning an Omni **alert**, `ListAlerts`, `GetAlert`, `CreateAlert`, `UpdateAlert`, `DeleteAlert`, `ListAlertContributors`, a `profileId`, an alert ARN, or how Omni alerts differ from a classic **alarm** — what alerts are, how they are evaluated (FIELD_VALUE vs COUNT_OF_RESULTS, contributors), their OK/WARNING/CRITICAL/NODATA state, no-data treatment, notification rules, and the alert APIs. The Omni alert API is real and first-class; do NOT redirect to classic CloudWatch alarms | Read [references/omni/alert-setup.md](references/omni/alert-setup.md). For classic alarms when Omni is not enabled, read [alarms.md](references/alarms.md) instead |
| Reading back stored evaluation scores in Omni — writing the query over `logs.default` eval-result records (`gen_ai.evaluation.*`), and reporting per-evaluator rollup + drilling into the WHY | Read [references/omni-agents.md](references/omni-agents.md) — "Reading stored eval scores" section (query surface + reader) |
| Spans multiple areas | Read the most specific reference first, then consult others as needed |

## Files

| File | Content |
|------|---------|
| [application-signals-onboarding.md](references/application-signals-onboarding.md) | Enable Application Signals auto-instrumentation: EKS add-on, CloudWatch Agent IAM, OTLP endpoints, ServiceEvents env vars, Dynamic Instrumentation — two-tier scope by platform/language |
| [application-signals-cicd-metadata.md](references/application-signals-cicd-metadata.md) | ServiceEvents git & deployment metadata propagation through CI/CD (the 5 `OTEL_AWS_SERVICE_EVENTS_*` vars) |
| `references/appsignals-guides/` (e.g. [eks-python.md](references/appsignals-guides/eks-python.md)) | 16 per-platform × per-language enablement guides (EC2/ECS/EKS/Lambda × Python/Node.js/Java/.NET) |
| [alarms.md](references/alarms.md) | Metric, composite, anomaly detection alarms — configuration, constraints, recommended defaults |
| [log-insights.md](references/log-insights.md) | Complete query syntax, commands, functions, known issues, reusable query library |
| [metrics.md](references/metrics.md) | Custom metrics, EMF spec, metric filters, high-resolution, retention |
| [tracing.md](references/tracing.md) | X-Ray → ADOT migration, sampling rules, annotations vs metadata, collector config |
| [dashboards.md](references/dashboards.md) | Widget types, cross-account/region, dynamic labels, sharing |
| [troubleshooting.md](references/troubleshooting.md) | Error → cause → fix for all observability services |
| [cloudtrail.md](references/cloudtrail.md) | Operational auditing, event types, S3+Athena queries |
| [synthetics.md](references/synthetics.md) | Canary runtime/blueprint constraints, VPC networking, common failures |
| [alarm-template.ts](assets/alarm-template.ts) | Best-practice CDK Lambda monitoring (alarms + dashboard) |
| [otel-config.yaml](assets/otel-config.yaml) | ADOT collector config for X-Ray traces + CloudWatch EMF metrics |
| [dynamic-instrumentation.md](references/dynamic-instrumentation.md) | Dynamic Instrumentation debugging loop — breakpoints/probes on live code, snapshot capture + correlation analysis, create/delete gating, snapshot PII handling. Runs via `scripts/di_instrumentation.py` + `scripts/di_snapshots.py`. |
| [references/omni-agents.md](references/omni-agents.md) | Agent datasets & evaluation reference — dataset curation from traces, on-demand/online evaluation via AgentCore APIs |
| [references/omni/log-trace-query.md](references/omni/log-trace-query.md) | SQL query syntax for logs and traces in CloudWatch Omni — table addressing, time range, system fields, field access, schema discovery, supported operations, functions, common patterns, constraints, TABLESAMPLE sampling |
| [references/omni/views.md](references/omni/views.md) | Views reference for CloudWatch Omni — creating/managing named SQL views (CreateView, UpdateView, DeleteView, ListViews), using views in queries (FROM view.<name>), naming rules, constraints, composition patterns |
| [references/omni/devops-agent.md](references/omni/devops-agent.md) | Handing investigations off to the AWS DevOps Agent — when to delegate a deep cross-service root cause, how to hand off from CloudWatch Omni, and how to interpret the findings (root cause, impact path / blast radius, the proposed mitigation plan). Connecting the DevOps Agent to a Space lives in the setting-up-cloudwatch-observability skill |
| [references/omni/dashboard.md](references/omni/dashboard.md) | Building a CloudWatch Omni dashboard — composition recipes, grounding panel queries, the panels[] JSON body and panel types, the nine visualizations, the 60-column grid layout, and per-resource archetype templates |
| [references/omni/alert-setup.md](references/omni/alert-setup.md) | CloudWatch Omni alerts reference — what an alert is, alertId vs name, Space-level ownership and the profileId an alert runs under, SQL and PromQL rule queries, evaluation (the FIELD_VALUE and COUNT_OF_RESULTS threshold modes and the contributors FIELD_VALUE produces), the OK/WARNING/CRITICAL/NODATA states, no-data treatment, notification rules (sns/slack only), and a section per API: CreateAlert, GetAlert, ListAlerts, UpdateAlert, DeleteAlert, ListAlertContributors |
| [scripts/](scripts/) | Helper scripts for trace-to-dataset conversion and evaluation execution |
