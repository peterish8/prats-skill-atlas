---
name: billing-compliance
description: "Check current platform, storefront, subscription, disclosure, and alternative-payment constraints before changing digital-product billing. Use for web, iOS, Android, or cross-platform monetization plans."
---

# Billing compliance

Turn a monetization proposal into an implementation plan that is policy-aware, region-aware, reviewable, and safe to roll back.

## Workflow

1. Identify product type, digital or physical consumption, platform, storefront, region, customer type, and purchase location.
2. Read the current official Apple, Google, payment-provider, tax, and applicable consumer-protection guidance; record access dates.
3. Determine required billing system, permitted links or alternatives, entitlement or program enrollment, disclosures, restore behavior, and reporting duties.
4. Map checkout, receipt, entitlement, renewal, grace period, refund, cancellation, family or account sharing, and support states.
5. Model fees, taxes, failed payments, fraud, chargebacks, reconciliation, and data responsibilities.
6. Design implementation, feature gating, audit evidence, staged rollout, and compliant fallback.
7. Escalate legal uncertainty rather than presenting policy interpretation as legal advice.

## Deliverable

Return:
- jurisdiction and platform matrix
- official-source policy ledger
- billing lifecycle and entitlement model
- implementation and review checklist
- rollout, monitoring, and rollback plan

## Guardrails

- Always verify rules live because platform policies change.
- Do not generalize a US iOS option to another storefront or Android.
- Never bypass platform review or obscure the actual merchant and cancellation path.

## Evidence baseline

- [Apple, App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Google Play, Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en)
- [Apple, External Purchase](https://developer.apple.com/documentation/StoreKit/external-purchase)
