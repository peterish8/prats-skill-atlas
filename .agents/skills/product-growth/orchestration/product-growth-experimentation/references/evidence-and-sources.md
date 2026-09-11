# Evidence and sources

This source map supports the skill's decision rules. It is not an exhaustive literature review. Vendor sources are used for implementation guidance and should not be treated as neutral evidence that a vendor's product or tactic is superior. Accessed 2026-09-12.

## User needs and onboarding

1. GOV.UK Service Manual, [Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs). User needs should be based on research, focus on problems rather than solutions, and be refined through the product lifecycle.
2. Harvard Business School Working Knowledge, [Clay Christensen's Milkshake Marketing](https://www.library.hbs.edu/working-knowledge/clay-christensens-milkshake-marketing). JTBD frames product choice around progress in context rather than demographics alone.
3. Nielsen Norman Group, [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/). Show core choices first and reveal secondary complexity when needed.
4. Nielsen Norman Group, [Onboarding Tutorials vs. Contextual Help](https://www.nngroup.com/articles/onboarding-tutorials/). Help is most useful in context and should not require users to memorize long tutorials.
5. Amplitude, [Out-of-the-box Product Analytics](https://amplitude.com/docs/analytics/product-analytics). Product-health views connect onboarding, feature engagement, and retention around defined value events.

## Experimentation and measurement

6. Microsoft Research, [Diagnosing Sample Ratio Mismatch in Online Controlled Experiments](https://www.microsoft.com/en-us/research/publication/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments-a-taxonomy-and-rules-of-thumb-for-practitioners/). SRM is a broad data-quality warning and unresolved SRM can reverse decisions.
7. Microsoft Research, [A Dirty Dozen: Twelve Common Metric Interpretation Pitfalls](https://www.microsoft.com/en-us/research/publication/a-dirty-dozen-twelve-common-metric-interpretation-pitfalls-in-online-controlled-experiments/). Good metrics still require careful interpretation.
8. NIST, [Sample sizes required](https://www.itl.nist.gov/div898/handbook/prc/section2/prc222.htm). Sample size depends on significance, power, variability, and the effect to detect.
9. Statsig, [Frequentist Sequential Testing](https://docs.statsig.com/experiments/advanced-setup/sequential-testing). Repeated fixed-horizon peeking inflates false positives; sequential methods adjust for early looks.
10. Statsig, [Managing SRM](https://docs.statsig.com/experiments/monitoring/srm). Allocation imbalance often indicates non-random assignment or telemetry defects.
11. Amplitude, [Define your experiment's goals](https://www.amplitude.com/docs/feature-experiment/workflow/define-goals). Declare a primary outcome and guardrails close enough to the intervention.

## Pricing and monetization

12. Stripe, [Pricing experiments](https://stripe.com/resources/more/pricing-experiments). Isolate price where possible and measure conversion, ARPU, and retention together.
13. RevenueCat, [Getting Started with Experiments](https://www.revenuecat.com/docs/tools/experiments-v1/experiments-overview-v1). Subscription tests can vary price, trial, duration, and offering, with stable randomized assignment.
14. Apple, [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/). Digital-goods billing and external-purchase options depend on current storefront, entitlement, and app-type rules.
15. Google Play, [Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en). Play Billing and alternative-billing rules depend on product and program eligibility.

## Trust, privacy, and accessibility

16. FTC, [Bringing Dark Patterns to Light](https://www.ftc.gov/news-events/news/press-releases/2022/09/ftc-report-shows-rise-sophisticated-dark-patterns-designed-trick-trap-consumers). Hidden terms, obstructed cancellation, disguised ads, and manipulative data sharing can harm consumers and trigger enforcement.
17. W3C, [WCAG 2.2](https://www.w3.org/TR/WCAG22/). Accessibility requirements cover perceivable, operable, understandable, and robust interaction, including newer focus, target-size, redundant-entry, and authentication criteria.
18. NIST, [Privacy Framework](https://www.nist.gov/privacy-framework). Privacy risk should be managed throughout product and data lifecycles.
19. Apple, [Human Interface Guidelines: Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy/). Ask for protected data or capabilities when the need is clear and explain the purpose specifically.
20. Apple, [AdAttributionKit](https://developer.apple.com/documentation/AdAttributionKit). Privacy-preserving attribution provides aggregate postbacks without user- or device-specific data in signed attribution payloads.
21. Apple, [Human Interface Guidelines: Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications). Notifications should be consented, timely, high-value, concise, and free of exposed sensitive information.
