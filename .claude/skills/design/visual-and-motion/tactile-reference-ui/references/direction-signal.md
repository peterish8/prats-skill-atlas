# Precision signal

Primary references: [01](../assets/design-kit/references/01-dashboard-handheld-overview.png), [04](../assets/design-kit/references/04-ai-activity-analytics-dashboard.png), [06](../assets/design-kit/references/06-zentra-finance-dashboard.png). Use `Theme direction="signal"`.

## Visual contract

Data structure supplies the visual interest. Numbers, time windows, active navigation and clear chart relationships dominate. Atmospheric color is a bounded insight accent, not a background for all analysis. This direction fits a genuine working dashboard rather than an ornamental marketing bento.

| Setting | Rebuild estimate / target |
|---|---|
| Substrate / ink | `#f8fafc` / `#0f172a`; card white |
| Muted / border | `#475569` / `#cbd5e1` |
| Accent | Indigo `#4338ca`; chart category colors require visible labels |
| Radii | 12 px card; 8 px control; 6–8 px small status |
| Page title | 28–36 px; section title 18–24 px; metric 32–48 px |
| Data body | 14–16 px; label 13–14 px; metadata 12–13 px |
| Grid | Desktop twelve columns, 16–20 px gap; wide chart 7–8 columns |
| Table row | 44–52 px normal; cell padding 10–14 px |
| Shadow | Small `0 1px 2px #0f172a0d`; wide `0 10px 24px -18px #0f172a47` |
| Number style | Tabular figures, consistent units/precision within a column |

## Composition anatomy

Use an orderly top bar or compact left rail, breadcrumb/context plus search, page heading with explicit date/scope controls, primary measures, a dominant chart/table and a contextual detail region. In 06 the wide funnel and right volume summary share the first major row; retention and two smaller metrics occupy a second row with one colored insight panel. In 04 the two large metrics precede tabs and a workflow area. Pick the structure that matches the actual information dependency.

A dashboard should not display eight identical summary tiles when one dominant measure and its explanation are more useful. Place related metrics near each other and label their units/periods. App navigation remains recognizable; decorative icon-only rails need accessible names and visible active context.

## Component mapping and data recipe

Use `Surface depth="flat"|"raised"`, `MetricCard`, `Badge`, `Tabs`, `Sparkline`, `Meter`, `Field`, `Switch` and `Dialog`. The kit intentionally does not export a pretend universal data table: use semantic table markup and the host's sorting/pagination model. A compact sparkline needs an adjacent label, date range and textual summary; use a fuller chart/table when users need exact comparisons. A meter's value/max must represent a real bounded measure; its `valueText` explains the count or unit.

For segmented usage art, build a finite row of simple bars from actual values, with a textual count and legend. Category lines must distinguish through shape/labels as well as color. Decorative funnel hatch belongs within bars, at a low opacity; it cannot change the numerical encoding. Never use chart coordinates from `sparklinePoints` for financial arithmetic; they are display positions only.

## Complete workspace UX

Sequence: resolve scope/time range → view summary → inspect dominant evidence/chart → select a row → inspect details → perform a relevant action → receive clear status. Loading preserves layout and labels; missing data says what is missing and over what scope; error provides retry without dropping filters; partial results show coverage separately; stale results show date; permission state identifies a safe next action. Filters have selected labels, clear/reset and genuine result updates. Table empty states distinguish no records from no filter matches.

In finance/evidence work, preserve separate source support, calculation status and coverage; retain dates, periods, units, disclosure scope and provenance. Decorative green never implies VERIFIED. The reference's numerical dashboard is not authority to invent trust scores, rankings or business performance.

## Responsive and motion

At 1024 px compress navigation and use eight columns; at 760 px summaries stack in order of importance and the detail panel becomes inline. On a phone, preserve the table's essential context using a scoped horizontal region or a purposeful record list; do not hide all columns arbitrarily. Keep filters reachable and table headers associated. Render one context menu/popover at a time with host accessibility behavior.

Data updates should be immediate. Use a subtle 150–180 ms background change to explain a changed value, not a number roll or chart dance. Tabs activate normally with arrow navigation; visual underline change does not delay data. No decorative ambient animation behind working data. Validate keyboard navigation, sorting states, errors and one actual detail flow.

## Acceptance and exclusions

Accept: readable dense values, explicit scopes, meaningful hierarchy, strong active states and calm surfaces. Reject: pastel unreadable labels, unlabelled charts, metric grids with no prioritization, fake success numbers, hovering every table row upward or motion that obscures changing results. A clean layout cannot prove data accuracy.

