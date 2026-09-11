# Standards and decision sources

Use primary sources as control catalogs, not as substitutes for product-specific reasoning. Prefer repository policies that are at least as protective. Re-check version-sensitive guidance when live internet access is available.

## Security

- OWASP Application Security Verification Standard: https://owasp.org/www-project-application-security-verification-standard/
- OWASP Top 10 (2025): https://owasp.org/Top10/2025/0x00_2025-Introduction/
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/

Use ASVS to derive implementation requirements and WSTG to plan authorized verification. Focus first on access control, security configuration, supply chain, cryptography, injection, insecure design, authentication, integrity, security logging/alerting, and exceptional-condition handling. Automated tools scale discovery but do not prove a custom application's business logic secure.

## Accessibility

- WCAG 2.2 Recommendation: https://www.w3.org/TR/WCAG22/
- WCAG quick reference: https://www.w3.org/WAI/WCAG22/quickref/
- W3C form notifications: https://www.w3.org/WAI/tutorials/forms/notifications/
- W3C live-region error technique: https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA19

Target WCAG 2.2 AA unless the product contract requires more. Verify perceivable, operable, understandable, and robust behavior. Combine automated checks with keyboard, zoom/reflow, reduced-motion, contrast, and assistive-technology-oriented manual inspection.

## Web performance and networking

- Core Web Vitals: https://web.dev/articles/vitals
- Highest-impact Core Web Vitals improvements: https://web.dev/articles/top-cwv
- Lighthouse: https://developer.chrome.com/docs/lighthouse/
- Performance budgets: https://web.dev/articles/performance-budgets-101
- HTTP caching: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching
- Cache-Control: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control
- HTTP idempotency: https://developer.mozilla.org/en-US/docs/Glossary/Idempotent
- Retry-After: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Retry-After

Use LCP, INP, and CLS as user-centered signals, supported by request waterfalls, payload sizes, long tasks, caching, and real-user data when available. Compare like-for-like cold/repeat runs; lab data and field data answer different questions.

## Testing

- Playwright network inspection and mocking: https://playwright.dev/docs/network
- Playwright actionability and auto-waiting: https://playwright.dev/docs/actionability

Prefer observable outcomes, semantic locators, isolated test state, deterministic network simulation, and assertions over fixed sleeps. Do not commit reusable authenticated browser state containing cookies or tokens.

## Reliability and observability

- OpenTelemetry observability primer: https://opentelemetry.io/docs/concepts/observability-primer/
- OpenTelemetry signals: https://opentelemetry.io/docs/concepts/signals/
- Google SRE monitoring guidance: https://sre.google/resources/book-update/monitoring-distributed-systems/

Measure reliability from the user's perspective. Instrument critical journeys with bounded-cardinality metrics, structured logs, and traces where architecture justifies them. Correlate signals, redact sensitive data, and alert on actionable symptoms rather than every internal event.

## Public-site discoverability

- Google Search Essentials: https://developers.google.com/search/docs/essentials
- Google Search metadata guidance: https://developers.google.com/search/docs/appearance/title-link
- Schema.org vocabulary: https://schema.org/docs/schemas.html

Apply search guidance only to pages intended for public indexing. Never add misleading structured data or accidentally index private, duplicate, staging, filtered, or account-specific content.

## Interpretation rules

- Treat legal, regulatory, payment, health, financial, and privacy obligations as context-specific. Identify relevant evidence and request qualified review when needed; do not claim legal compliance from a code audit.
- Treat a missing control as applicable only after confirming the architecture and threat model.
- Cite a standard in reports only when the verified issue maps directly to it.
- Prefer a smaller set of verified high-impact controls over a long list of untested claims.
