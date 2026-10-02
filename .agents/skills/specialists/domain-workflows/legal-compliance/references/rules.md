# Baseline rules and how to confirm them

Figures below were confirmed by web search on 2 October 2026 unless marked *(unverified)*.
Re-run the search before quoting any number: penalties are inflation-adjusted yearly and
phase-in dates move.

## India (operator based in India, or Indian users)

| Rule | What it asks | Applies when | Confirm with |
|---|---|---|---|
| DPDP Act 2023 + DPDP Rules 2025 | Plain-language notice, consent by clear action, a published contact for data questions, rights to access, correct and erase (answer within 90 days), withdraw consent as easily as given, breach notice to affected people and the Board, keep data only as long as needed. Free services are covered; only personal or household use is exempt. | Any account or personal data. Rules notified 13-14 Nov 2025; main duties start 18 months later (about May 2027). | `DPDP Rules 2025 notified phased implementation 18 months` (pib.gov.in) |
| DPDP s.9, children | Everyone under 18 is a child. Verifiable parental consent; no tracking, behavioural monitoring or targeted ads for children. Penalty up to Rs 200 crore. | Accounts open to under-18s, any profiling. Simplest route: 18+ accounts. | `DPDP Act section 9 verifiable parental consent under 18 penalty` |
| IT Act s.79 + Intermediary Rules 2021 | Publish rules, privacy policy and user agreement; name a grievance officer; acknowledge complaints in 24 hours, resolve in 15 days; act on court or government orders within 36 hours. | Any user-generated or user-shared content. In force now. | `IT Intermediary Guidelines Rules 2021 rule 3 grievance officer 24 hours 15 days` (meity.gov.in) |
| Copyright Act 1957 s.52(1)(c) + Copyright Rules 2013 r.75 | On a valid notice, remove the item within 36 hours for 21 days unless a court order follows. | User uploads. | `Copyright Rules 2013 rule 75 takedown 36 hours` |
| Music and video licensing | Internet streaming cannot use the s.31D statutory licence (Tips v. Wynk, Bombay HC 2019). Needs agreements with labels and societies (IPRS, PPL). Being free does not change this. | Any service that streams recordings it has no licence for. | `Tips v Wynk section 31D internet streaming` |
| RBI e-mandate rules | Authentication when a recurring mandate is set up, a pre-debit notice 24 hours before each charge, extra authentication above Rs 15,000. | Recurring card or UPI payments. | `RBI e-mandate pre-debit notification 15000 AFA` (Stripe or Razorpay docs) |
| Dark-pattern guidelines 2023, Consumer Protection (E-Commerce) Rules 2020 *(unverified)* | No subscription traps, drip pricing or false urgency; seller name, address, grievance officer and refund policy shown. | Selling anything. | `CCPA dark patterns guidelines 2023 subscription trap` |

## United States (US users)

| Rule | What it asks | Applies when | Confirm with |
|---|---|---|---|
| COPPA | Verifiable parental consent before collecting data from under-13s. Max civil penalty $53,088 per violation (2025 figure; the 2026 adjustment was reported cancelled). FTC and states enforce; no private suits. | Service directed at children, or actual knowledge a user is under 13. Not asking age is not itself a violation. | `FTC inflation-adjusted civil penalty amounts` (ftc.gov) |
| CAN-SPAM | Commercial email needs honest headers, a working unsubscribe honoured in 10 business days, and a physical postal address. Up to $53,088 per email. FTC enforces. | Marketing email. | `CAN-SPAM compliance guide FTC` |
| California CIPA and session replay | Suits claim replay is wiretapping, $5,000 per violation *(statute figure unverified)*. Courts are split and many cases are dismissed (Ninth Circuit, Popa, Aug 2025: no concrete injury). | Session replay on by default for California visitors. | `session replay CIPA dismissed Ninth Circuit` |
| California Automatic Renewal Law | Renewal terms clear and in visual proximity to the consent request; easy cancellation; amendments effective 1 July 2025. Non-compliant goods may be an unconditional gift *(unverified)*. | Subscriptions sold to Californians. | `California automatic renewal law 17602 2025 amendments` |
| DMCA s.512 | Safe harbour for user uploads needs a registered agent ($6 at copyright.gov) and the same contact on the site, plus takedown on notice. Statutory damages up to $150,000 per work for wilful infringement *(unverified)*. Does not cover content the service itself fetches. | User uploads, US rightsholders. | `DMCA designated agent directory FAQ fee` (copyright.gov) |

## European Union (EU visitors)

| Rule | What it asks | Applies when | Confirm with |
|---|---|---|---|
| GDPR, third-party embeds | LG Muenchen 3 O 17493/20 (20 Jan 2022) awarded EUR 100 for sending a visitor's IP to Google through Google Fonts with no consent. Legitimate interest failed because self-hosting is possible. | Any third-party font, script or embed loaded without consent. | `LG München Google Fonts 3 O 17493/20` (gdprhub.eu) |
| GDPR generally | Lawful basis, notice, rights, processors under contract, transfers. | Offering the service to people in the EU. | search the specific point |
| ePrivacy cookies | Consent before non-essential cookies or device storage. | Analytics or ad cookies. | search the specific point |

## Platforms and licences

- **Google Play / App Store** *(unverified)*: privacy policy link, a data-safety declaration,
  and for apps with accounts an in-app and web path to delete the account.
- **Open source**: a public repository with no licence file grants nobody any rights. Code
  ported or copied from a GPL project must be released under the GPL. Keep the original
  authors' notices in a credits file. Check the upstream LICENSE file itself; badges and
  third-party summaries are not proof.
- **Fonts and assets**: proprietary fonts (Apple SF Pro, most foundry faces) cannot be
  redistributed in a repo or an app build. Replace with an openly licensed face.

## Reading a penalty honestly

For each figure answer four questions in the reply: is it a maximum; who can bring the claim;
what condition triggers it; and has a court actually awarded it in a comparable case.
