# Growth ethics and compliance

Use this reference for onboarding questions, personalization, paywalls, trials, subscriptions, billing, lifecycle messages, and referral mechanics.

## Bright-line product rules

- Present the total price, billing interval, renewal behavior, trial conversion, material limits, and cancellation path before commitment.
- Make accepting and declining optional data use comparably understandable. Do not use visual hierarchy to disguise the less profitable choice.
- Never fabricate testimonials, download counts, scarcity, countdowns, endorsements, or savings.
- Do not delay, hide, or shrink a close control to trap a user. A flow may create deliberate friction only to prevent harm or improve informed choice.
- Make cancellation and data deletion discoverable. Preserve access to required receipts and account controls.
- Collect only data tied to a named purpose. Define access, retention, deletion, and downstream sharing before launch.
- Do not expose sensitive details in notifications, referral payloads, screenshots, analytics properties, or experiment logs.

## Accessibility gate

Apply WCAG 2.2 to web flows and the target platform's accessibility guidance to native flows. Test keyboard and screen-reader operation, focus order and visibility, labels and instructions, error recovery, zoom/reflow, contrast, target size, motion reduction, authentication burden, and timeout behavior. Automated checks are necessary but insufficient.

Growth experiments must include accessibility guardrails when variants alter copy, order, interaction, forms, motion, authentication, or payment. Conversion uplift from an inaccessible variant is not a clean win.

## Payment and subscription gate

Apple and Google rules vary by storefront, app type, product type, and enrolled program. Before recommending external checkout or alternative billing:

1. Identify whether the purchase is digital content/functionality or a physical/person-to-person service.
2. Identify platform, storefront, region, app category, and entitlement/program eligibility.
3. Verify the current official policy and implementation requirements.
4. Model fees, taxes, refunds, churn, support, failed payments, and compliance operations across the full lifecycle.
5. Preserve a compliant fallback and rollback path.

Do not generalize a US iOS result to Android or other regions.

## Current official starting points

- Apple, [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/).
- Google Play, [Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en).
- W3C, [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/).
- NIST, [Privacy Framework](https://www.nist.gov/privacy-framework).
- FTC, [Bringing Dark Patterns to Light](https://www.ftc.gov/news-events/news/press-releases/2022/09/ftc-report-shows-rise-sophisticated-dark-patterns-designed-trick-trap-consumers).
- Apple, [Human Interface Guidelines: Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy/).

These links are starting points, not frozen legal advice. Recheck them when the work is performed.
