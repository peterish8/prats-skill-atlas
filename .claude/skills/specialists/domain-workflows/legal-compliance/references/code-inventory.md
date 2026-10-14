# Code inventory: what to look for

Search source directories only (exclude `node_modules`, lockfiles, build output, vendored
clones). On large monorepos scope each search to the app folders; a recursive grep over an
unfiltered tree can take minutes.

| Question | Search for | Why it matters |
|---|---|---|
| Fonts or scripts from a third party | `fonts.googleapis`, `fonts.gstatic`, `<script src="https://`, `<link href="https://` | Sends each visitor's IP to that party (EU Google Fonts ruling). Self-host instead. |
| Analytics | `gtag`, `google-analytics`, `posthog`, `mixpanel`, `amplitude`, `plausible`, `@vercel/analytics`, `segment` | Must be described in the policy; cookies or cross-site IDs need consent in the EU. |
| Session replay | `clarity`, `hotjar`, `fullstory`, `logrocket`, `replay`, `rrweb`, `disable_session_recording` | Wiretap suits in the US, needs consent. Check the default, it is often on. |
| Error tracking | `sentry`, `bugsnag`, `datadog` | A processor to list. Check replay and PII scrubbing settings. |
| Sign-in | `signIn(`, `OAuth`, `passport`, `next-auth`, `clerk`, `supabase.auth`, `firebase/auth`, `@convex-dev/auth` | Where consent and age are asked. Note whether age is asked at all. |
| Personal data stored | schema files, `email`, `displayName`, `phone`, `address`, `dob`, `birth`, `location`, `ip`, `deviceId` | The list the privacy policy must match. |
| Behavioural profiling | `taste`, `recommend`, `history`, `recentlyPlayed`, `tracking`, `personaliz` | Banned for children in India; needs an off switch for withdrawal of consent. |
| Email sending | `resend`, `sendgrid`, `nodemailer`, `mailchimp`, `ses`, `postmark` | Marketing mail needs consent, unsubscribe and a postal address. |
| Payments | `stripe`, `razorpay`, `paddle`, `subscription`, `checkout`, `price` | Renewal terms beside the button, easy cancel, e-mandates in India. |
| User uploads and public content | `upload`, `storage`, `avatar`, `cover`, `isPublic`, `share`, `comment`, `post` | Host liability: needs a takedown route and a report link. |
| Policy pages | `privacy`, `terms`, `copyright`, `dmca`, `grievance` | Usually missing. Check mobile About screens too, and whether their claims are true. |
| Account deletion and export | `deleteAccount`, `delete account`, `erase`, `export` | Required by privacy laws and by app stores. |
| Retention | cron or scheduler files, `sweep`, `cleanup`, `ttl`, `expires` | Data may not be kept forever. Look for a last-active marker. |
| Licences | `LICENSE*`, `"license"` in package.json, bundled fonts (`*.otf`, `*.ttf`), vendored or "ported from" code | A public repo without a licence is not open source. Ported GPL code forces GPL. Proprietary fonts cannot be redistributed. |
| Secrets in history | see below | A public repo exposes every past commit. |
| Third-party private APIs | `token`, `innertube`, `scrape`, unofficial API hosts in env examples | Terms-of-service and licensing exposure; often the largest risk. |

## Secrets in git history

Check which key files were ever added, then scan added lines for token shapes. Mask values in
the output and never repeat a found secret in the reply.

```bash
git log --all --diff-filter=A --name-only --format= | sort -u \
  | grep -iE '(^|/)\.env($|\.)|\.pem$|\.jks$|\.keystore$|\.p12$|google-services\.json|service-account|credentials' \
  | grep -v '\.env\.example$'
```

```bash
git log --all -p --format='@@C %h' -- . ':(exclude)*package-lock.json' \
  | awk '/^@@C /{c=$2} /^\+\+\+ /{f=$2} /^\+/{ if ($0 ~ /(AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{24,}|AIza[0-9A-Za-z_-]{35}|-----BEGIN [A-Z ]*PRIVATE KEY|xox[baprs]-[A-Za-z0-9-]{10,}|eyJ[A-Za-z0-9_-]{20,}\.eyJ[A-Za-z0-9_-]{20,})/) { m=$0; gsub(/^\+[ \t]*/,"",m); print c, f, substr(m,1,40) "..." } }' \
  | sort -u
```

`AKIAIOSFODNN7EXAMPLE` is AWS's documented example key, not a leak. A real hit means: rotate
the key first, then decide with the user whether to rewrite history.

## Repo visibility

`gh repo view <owner>/<repo> --json visibility,licenseInfo` tells whether the repo is already
public and whether GitHub sees a licence.
