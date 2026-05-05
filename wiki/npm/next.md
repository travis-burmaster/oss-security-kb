# next (npm)

**Registry:** npm
**Weekly Downloads:** ~33,646,933 (2026-04-27 to 2026-05-03)
**Repository:** https://github.com/vercel/next.js
**Security Contact:** GitHub Security Advisories / Vercel security channels
**Disclosure Policy:** public GitHub Security Advisory flow and Vercel security reporting
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-04 | OpenClaw recurring review | package advisory refresh | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database public records, public CVE aliases, npm registry metadata, npm downloads API, and local proxy synthesis used only as a drafting aid) | Expanded the page from a single 2026 App Router / Server Function DoS entry to the current public package-scoped advisory set returned by OSV / GHSA for `next`, with 42 records spanning legacy traversal / XSS issues, image optimizer flaws, cache poisoning, middleware authorization bypasses, Server Actions / Server Components issues, request smuggling, SSRF, RCE, source exposure, and 2026 DoS / CSRF fixes. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| 2026-04-27 | OpenClaw recurring review | new package page | public-source curation (GitHub Advisory Database pages, upstream public GitHub security advisory, maintainer/public changelog link referenced by GHSA) | Added Next.js DoS advisory (GHSA-q4gf-8mx6-v5v3) tied to upstream React Server Components issue (CVE-2026-23869). | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

The table below is a package-level advisory map from the public OSV.dev query for npm `next`, cross-checked against GitHub Advisory Database public records where available. It is intentionally a curation map, not a claim that every deployment is exploitable.

| Published | CVE / Issue | Public advisory summary | Fixed in | Source |
|-----------|-------------|-------------------------|----------|--------|
| 2026-04-10 | GHSA-q4gf-8mx6-v5v3 | Next.js has a Denial of Service with Server Components | 15.5.15, 16.2.3 | https://github.com/advisories/GHSA-q4gf-8mx6-v5v3 |
| 2026-03-17 | GHSA-mq59-m269-xvcx / CVE-2026-27978 | Next.js: null origin can bypass Server Actions CSRF checks | 16.1.7 | https://github.com/advisories/GHSA-mq59-m269-xvcx |
| 2026-03-17 | GHSA-jcc7-9wpm-mj36 / CVE-2026-27977 | Next.js: null origin can bypass dev HMR websocket CSRF checks | 16.1.7 | https://github.com/advisories/GHSA-jcc7-9wpm-mj36 |
| 2026-03-17 | GHSA-h27x-g6w4-24gq / CVE-2026-27979 | Next.js: Unbounded postponed resume buffering can lead to DoS | 16.1.7 | https://github.com/advisories/GHSA-h27x-g6w4-24gq |
| 2026-03-17 | GHSA-ggv3-7p47-pfv8 / CVE-2026-29057 | Next.js: HTTP request smuggling in rewrites | 15.5.13, 16.1.7 | https://github.com/advisories/GHSA-ggv3-7p47-pfv8 |
| 2026-03-17 | GHSA-3x4c-7xq6-9pq8 / CVE-2026-27980 | Next.js: Unbounded next/image disk cache growth can exhaust storage | 15.5.14, 16.1.7 | https://github.com/advisories/GHSA-3x4c-7xq6-9pq8 |
| 2026-01-28 | GHSA-h25m-26qc-wcjf | Next.js HTTP request deserialization can lead to DoS when using insecure React Server Components | 15.0.8, 15.1.12, 15.2.9, 15.3.9, 15.4.11, 15.5.10, 15.6.0-canary.61, 16.0.11, 16.1.5 | https://github.com/advisories/GHSA-h25m-26qc-wcjf |
| 2026-01-28 | GHSA-5f7q-jpqc-wp7h / CVE-2025-59472 | Next.js has Unbounded Memory Consumption via PPR Resume Endpoint | 15.6.0-canary.61, 16.1.5 | https://github.com/advisories/GHSA-5f7q-jpqc-wp7h |
| 2026-01-27 | GHSA-9g9p-9gw9-jx7f / CVE-2025-59471 | Next.js self-hosted applications vulnerable to DoS via Image Optimizer remotePatterns configuration | 15.5.10, 16.1.5 | https://github.com/advisories/GHSA-9g9p-9gw9-jx7f |
| 2025-12-12 | GHSA-5j59-xgg2-r9c4 | Next has a Denial of Service with Server Components - Incomplete Fix Follow-Up | 14.2.35, 15.0.7, 15.1.11, 15.2.8, 15.3.8, 15.4.10, 15.5.9, 15.6.0-canary.60, 16.0.10, 16.1.0-canary.19 | https://github.com/advisories/GHSA-5j59-xgg2-r9c4 |
| 2025-12-11 | GHSA-w37m-7fhw-fmv9 | Next Server Actions Source Code Exposure | 15.0.6, 15.1.10, 15.2.7, 15.3.7, 15.4.9, 15.5.8, 15.6.0-canary.59, 16.0.9, 16.1.0-canary.17 | https://github.com/advisories/GHSA-w37m-7fhw-fmv9 |
| 2025-12-11 | GHSA-mwv6-3258-q52c | Next Vulnerable to Denial of Service with Server Components | 14.2.34, 15.0.6, 15.1.10, 15.2.7, 15.3.7, 15.4.9, 15.5.8, 15.6.0-canary.59, 16.0.9, 16.1.0-canary.17 | https://github.com/advisories/GHSA-mwv6-3258-q52c |
| 2025-12-03 | GHSA-9qr9-h5gf-34mp | Next.js is vulnerable to RCE in React flight protocol | 15.0.5, 15.1.9, 15.2.6, 15.3.6, 15.4.8, 15.5.7, 16.0.7 | https://github.com/advisories/GHSA-9qr9-h5gf-34mp |
| 2025-08-29 | GHSA-xv57-4mr9-wg8v / CVE-2025-55173 | Next.js Content Injection Vulnerability for Image Optimization | 14.2.31, 15.4.5 | https://github.com/advisories/GHSA-xv57-4mr9-wg8v |
| 2025-08-29 | GHSA-g5qg-72qw-gw5v / CVE-2025-57752 | Next.js Affected by Cache Key Confusion for Image Optimization API Routes | 14.2.31, 15.4.5 | https://github.com/advisories/GHSA-g5qg-72qw-gw5v |
| 2025-08-29 | GHSA-4342-x723-ch2f / CVE-2025-57822 | Next.js Improper Middleware Redirect Handling Leads to SSRF | 14.2.32, 15.4.7 | https://github.com/advisories/GHSA-4342-x723-ch2f |
| 2025-07-03 | GHSA-r2fc-ccr8-96c4 / CVE-2025-49005 | Next.js has a Cache poisoning vulnerability due to omission of the Vary header | 15.3.3 | https://github.com/advisories/GHSA-r2fc-ccr8-96c4 |
| 2025-07-03 | GHSA-67rr-84xm-4c7r / CVE-2025-49826 | Next.JS vulnerability can lead to DoS via cache poisoning | 15.1.8 | https://github.com/advisories/GHSA-67rr-84xm-4c7r |
| 2025-05-28 | GHSA-3h52-269p-cp9r / CVE-2025-48068 | Information exposure in Next.js dev server due to lack of origin verification | 14.2.30, 15.2.2 | https://github.com/advisories/GHSA-3h52-269p-cp9r |
| 2025-05-15 | GHSA-qpjv-v59x-3qc4 / CVE-2025-32421 | Next.js Race Condition to Cache Poisoning | 14.2.24, 15.1.6 | https://github.com/advisories/GHSA-qpjv-v59x-3qc4 |
| 2025-04-02 | GHSA-223j-4rm8-mrmf / CVE-2025-30218 | Next.js may leak x-middleware-subrequest-id to external hosts | 12.3.6, 13.5.10, 14.2.26, 15.2.4 | https://github.com/advisories/GHSA-223j-4rm8-mrmf |
| 2025-03-21 | GHSA-f82v-jwr5-mffw / CVE-2025-29927 | Authorization Bypass in Next.js Middleware | 12.3.5, 13.5.9, 14.2.25, 15.2.3 | https://github.com/advisories/GHSA-f82v-jwr5-mffw |
| 2025-01-03 | GHSA-7m27-7ghc-44w9 / CVE-2024-56332 | Next.js Allows a Denial of Service (DoS) with Server Actions | 13.5.8, 14.2.21, 15.1.2 | https://github.com/advisories/GHSA-7m27-7ghc-44w9 |
| 2024-12-17 | GHSA-7gfc-8cq8-jh5f / CVE-2024-51479 | Next.js authorization bypass vulnerability | 14.2.15 | https://github.com/advisories/GHSA-7gfc-8cq8-jh5f |
| 2024-10-14 | GHSA-g77x-44xx-532m / CVE-2024-47831 | Denial of Service condition in Next.js image optimization | 14.2.7 | https://github.com/advisories/GHSA-g77x-44xx-532m |
| 2024-09-17 | GHSA-gp8f-8m3g-qvj9 / CVE-2024-46982 | Next.js Cache Poisoning | 13.5.7, 14.2.10 | https://github.com/advisories/GHSA-gp8f-8m3g-qvj9 |
| 2024-07-10 | GHSA-fq54-2j52-jc42 / CVE-2024-39693 | Next.js Denial of Service (DoS) condition | 13.5.0 | https://github.com/advisories/GHSA-fq54-2j52-jc42 |
| 2024-05-09 | GHSA-fr5h-rqp8-mj6g / CVE-2024-34351 | Next.js Server-Side Request Forgery in Server Actions | 14.1.1 | https://github.com/advisories/GHSA-fr5h-rqp8-mj6g |
| 2024-05-09 | GHSA-77r5-gw3j-2mpf / CVE-2024-34350 | Next.js Vulnerable to HTTP Request Smuggling | 13.5.1 | https://github.com/advisories/GHSA-77r5-gw3j-2mpf |
| 2023-10-22 | GHSA-c59h-r6p8-q9wc / CVE-2023-46298 | Next.js missing cache-control header may lead to CDN caching empty reply | 13.4.20-canary.13 | https://github.com/advisories/GHSA-c59h-r6p8-q9wc |
| 2022-08-30 | GHSA-wff4-fpwg-qqv3 / CVE-2022-36046 | Unexpected server crash in Next.js | 12.2.4 | https://github.com/advisories/GHSA-wff4-fpwg-qqv3 |
| 2022-02-17 | GHSA-fmvm-x8mv-47mj / CVE-2022-23646 | Improper CSP in Image Optimization API for Next.js versions between 10.0.0 and 12.1.0 | 12.1.0 | https://github.com/advisories/GHSA-fmvm-x8mv-47mj |
| 2022-01-28 | GHSA-wr66-vrwm-5g5x / CVE-2022-21721 | Denial of Service Vulnerability in next.js | 12.0.9 | https://github.com/advisories/GHSA-wr66-vrwm-5g5x |
| 2021-12-07 | GHSA-25mp-g6fv-mqxx / CVE-2021-43803 | Unexpected server crash in Next.js. | 11.1.3, 12.0.5 | https://github.com/advisories/GHSA-25mp-g6fv-mqxx |
| 2021-09-01 | GHSA-9gr3-7897-pp7m / CVE-2021-39178 | XSS in Image Optimization API for Next.js | 11.1.1 | https://github.com/advisories/GHSA-9gr3-7897-pp7m |
| 2021-08-12 | GHSA-vxf5-wxwp-m7g9 / CVE-2021-37699 | Open Redirect in Next.js | 11.1.0 | https://github.com/advisories/GHSA-vxf5-wxwp-m7g9 |
| 2020-10-08 | GHSA-x56p-c8cg-q435 / CVE-2020-15242 | Open Redirect in Next.js versions | 9.5.4 | https://github.com/advisories/GHSA-x56p-c8cg-q435 |
| 2020-09-04 | GHSA-5vj8-3v2h-h38v | Remote Code Execution in next | 5.1.0 | https://github.com/advisories/GHSA-5vj8-3v2h-h38v |
| 2020-03-30 | GHSA-fq77-7p7r-83rj / CVE-2020-5284 | Directory Traversal in Next.js | 9.3.2 | https://github.com/advisories/GHSA-fq77-7p7r-83rj |
| 2018-10-15 | GHSA-qw96-mm2g-c8m7 / CVE-2018-18282 | Next.js has cross site scripting (XSS) vulnerability via the 404 or 500 /_error page | 7.0.2 | https://github.com/advisories/GHSA-qw96-mm2g-c8m7 |
| 2018-01-24 | GHSA-m34x-wgrh-g897 / CVE-2018-6184 | Directory traversal vulnerability in Next.js | 4.2.3 | https://github.com/advisories/GHSA-m34x-wgrh-g897 |
| 2017-12-05 | GHSA-3f5c-4qxj-vmpf / CVE-2017-16877 | Next.js Directory Traversal Vulnerability | 2.4.1 | https://github.com/advisories/GHSA-3f5c-4qxj-vmpf |

*Full OSV package listing: https://osv.dev/list?ecosystem=npm&q=next*

## Security Posture Notes

- `next` has a **large and fast-moving public advisory surface** for a framework package: this pass found 42 package-scoped OSV records, with many 2024-2026 entries concentrated in modern App Router, Server Actions, Server Components / React Flight, image optimization, middleware, and cache behavior.
- The most operationally important recent cluster is **request-handling logic that sits in front of application code**: middleware authorization bypass (`GHSA-f82v-jwr5-mffw` / `CVE-2025-29927`), middleware header leakage (`GHSA-223j-4rm8-mrmf` / `CVE-2025-30218`), request smuggling (`GHSA-77r5-gw3j-2mpf` and `GHSA-ggv3-7p47-pfv8`), and SSRF via Server Actions / middleware redirect handling (`GHSA-fr5h-rqp8-mj6g`, `GHSA-4342-x723-ch2f`).
- A second clear cluster is **resource-exhaustion / denial-of-service behavior** in framework-managed endpoints: Server Actions, Server Components, Partial Prerendering / resume endpoints, image optimizer caching, and deserialization paths all appear in the public advisory trail.
- Public records also include **high-consequence but narrower-trigger issues** such as React Flight protocol RCE (`GHSA-9qr9-h5gf-34mp`) and Server Actions source-code exposure (`GHSA-w37m-7fhw-fmv9`). These should be tracked separately from generic DoS because the remediation urgency and blast radius can be different.
- Current npm metadata in this pass showed `latest` as `16.2.4`, with maintained dist-tags also present for older lines such as `next-13`, `next-14`, and `backport`. That means downstream projects should prefer maintained branch tips rather than relying on a single old “fixed in” version from one advisory.
- Older `next` releases have legacy traversal, XSS, open-redirect, and server-crash advisories. For modern users, the more relevant lesson is that **framework defaults and deployment topology matter**: CDN/proxy behavior, middleware trust boundaries, self-hosted image optimization, Server Actions, and RSC endpoints can all become part of the security boundary.

## Recommendations for Developers

1. **Track the maintained branch tip for your major line**, not just the first fixed version for one CVE. As of this review, npm metadata showed `latest` at `16.2.4`, `backport` at `15.5.15`, `next-14` at `14.2.35`, and `next-13` at `13.5.11`.
2. **Prioritize middleware and request-boundary fixes** if your app uses middleware for authentication, rewrites, redirects, or edge routing. Public advisories show multiple ways those layers can affect authorization, SSRF, or request smuggling outcomes.
3. **Review Server Actions / Server Components exposure** separately from normal page rendering. The public 2025-2026 advisories repeatedly involve RSC / React Flight deserialization, Server Functions, Server Actions, and resume endpoints.
4. **Harden image optimization deployments** with conservative remote-pattern configuration, cache limits, and monitoring for disk / memory growth, because multiple public advisories target image optimizer behavior.
5. **Add reverse-proxy/CDN guardrails** where feasible: strip unexpected internal Next.js headers, apply body-size and timeout limits, and treat cache keys / `Vary` behavior as security-relevant.
6. **Do not treat development-server advisories as production-only findings.** The public dev-server origin-check issues matter most when developer tooling is reachable from untrusted networks or browsers.

## Dependencies of Note

- `next` security often depends on coordinated behavior across React / React Server Components, framework routing, middleware, cache layers, and deployment adapters rather than one small direct dependency.
- Self-hosted deployments may carry different exposure than fully managed deployments, especially for image optimization, CDN caching, header filtering, and reverse-proxy request limits.
- Several advisory summaries mention upstream React Server Components / React Flight behavior, so related pages such as `react` and `react-server-dom-webpack` should be cross-checked in future passes.

## Open Questions

- Which advisories in the 2025-2026 cluster have materially different exposure on Vercel-managed deployments versus self-hosted Node / container deployments?
- Should the KB split out a dedicated cross-package page for React Server Components / React Flight vulnerabilities that affect `next`, `react`, and `react-server-dom-webpack` together?
- Which high-traffic templates or starter kits still pin `next` below the maintained branch tips for 13.x, 14.x, or 15.x?

## Related Pages

- [[npm/react]]
- [[npm/react-server-dom-webpack]]
- [[npm/vite]]
- [[npm/webpack-dev-server]]
- [[npm/index]]

---
*Last updated: 2026-05-04 | Sources: 7 (OSV.dev package query for npm/next, OSV vulnerability records for the 42 listed GHSA entries, GitHub Advisory Database public advisory records, public CVE aliases referenced by those records, npm registry metadata, npm downloads API, local Claude-compatible proxy synthesis saved under `raw/advisory-review-20260504-2239/` and used only as a drafting aid)*
