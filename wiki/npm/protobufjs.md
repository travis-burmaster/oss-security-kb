# protobufjs (npm)

**Registry:** npm  
**Weekly Downloads:** 62,149,725 (npm downloads API, 2026-05-05 to 2026-05-11)  
**Repository:** https://github.com/protobufjs/protobuf.js  
**Security Contact:** GitHub private vulnerability reporting / upstream SECURITY.md  
**Disclosure Policy:** https://github.com/protobufjs/protobuf.js/security/policy  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-12 | OpenClaw recurring review | public advisory mapping for the npm `protobufjs` package | public-source curation (OSV.dev package query and individual vulnerability records, GitHub Advisory Database records, public CVE aliases, npm registry/download metadata, upstream SECURITY.md and release notes, local Claude-compatible proxy draft assist) | Added initial page mapping 11 public advisories across prototype pollution / injection, generated-code code injection, parser / recursion / option-path DoS, overlong UTF-8 decoding, and legacy regex DoS. Current npm `latest` was `8.2.0` during review, with maintained 7.x and 8.x release trains visible in upstream releases. | https://osv.dev/list?ecosystem=npm&q=protobufjs |
| *No public proactive source-code audit on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

This table is a package-level public advisory map from OSV.dev / GitHub Advisory Database for `protobufjs`, cross-checked against public CVE aliases where available.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2018-3738 / GHSA-762f-c2wg-m8c8 | MEDIUM | Denial of Service in protobufjs | 6.8.6, 5.0.3 | https://osv.dev/vulnerability/GHSA-762f-c2wg-m8c8 ; https://github.com/advisories/GHSA-762f-c2wg-m8c8 ; https://www.cve.org/CVERecord?id=CVE-2018-3738 |
| CVE-2022-25878 / GHSA-g954-5hwp-pp24 | HIGH | Prototype Pollution in protobufjs | 6.11.3, 6.10.3 | https://osv.dev/vulnerability/GHSA-g954-5hwp-pp24 ; https://github.com/advisories/GHSA-g954-5hwp-pp24 ; https://www.cve.org/CVERecord?id=CVE-2022-25878 |
| CVE-2023-36665 / GHSA-h755-8qp9-cq85 | CRITICAL | protobufjs Prototype Pollution vulnerability | 6.11.4, 7.2.5 | https://osv.dev/vulnerability/GHSA-h755-8qp9-cq85 ; https://github.com/advisories/GHSA-h755-8qp9-cq85 ; https://www.cve.org/CVERecord?id=CVE-2023-36665 |
| CVE-2026-41242 / GHSA-xq3m-2v4x-88gg | CRITICAL | Arbitrary code execution in protobufjs | 8.0.1, 7.5.5 | https://osv.dev/vulnerability/GHSA-xq3m-2v4x-88gg ; https://github.com/advisories/GHSA-xq3m-2v4x-88gg ; https://www.cve.org/CVERecord?id=CVE-2026-41242 |
| CVE-2026-44288 / GHSA-q6x5-8v7m-xcrf | MEDIUM | protobufjs has overlong UTF-8 decoding | 7.5.6, 8.0.2, 1.1.1 | https://osv.dev/vulnerability/GHSA-q6x5-8v7m-xcrf ; https://github.com/advisories/GHSA-q6x5-8v7m-xcrf ; https://www.cve.org/CVERecord?id=CVE-2026-44288 |
| CVE-2026-44289 / GHSA-685m-2w69-288q | HIGH | protobuf.js: Denial of service through unbounded protobuf recursion | 7.5.6, 8.0.2 | https://osv.dev/vulnerability/GHSA-685m-2w69-288q ; https://github.com/advisories/GHSA-685m-2w69-288q ; https://www.cve.org/CVERecord?id=CVE-2026-44289 |
| CVE-2026-44290 / GHSA-jvwf-75h9-cwgg | HIGH | protobuf.js: Process-wide denial of service through unsafe option paths | 7.5.6, 8.0.2 | https://osv.dev/vulnerability/GHSA-jvwf-75h9-cwgg ; https://github.com/advisories/GHSA-jvwf-75h9-cwgg ; https://www.cve.org/CVERecord?id=CVE-2026-44290 |
| CVE-2026-44291 / GHSA-75px-5xx7-5xc7 | HIGH | protobuf.js: Code generation gadget after prototype pollution | 7.5.6, 8.0.2 | https://osv.dev/vulnerability/GHSA-75px-5xx7-5xc7 ; https://github.com/advisories/GHSA-75px-5xx7-5xc7 ; https://www.cve.org/CVERecord?id=CVE-2026-44291 |
| CVE-2026-44292 / GHSA-fx83-v9x8-x52w | MEDIUM | protobuf.js: Prototype injection in generated message constructors | 7.5.6, 8.0.2 | https://osv.dev/vulnerability/GHSA-fx83-v9x8-x52w ; https://github.com/advisories/GHSA-fx83-v9x8-x52w ; https://www.cve.org/CVERecord?id=CVE-2026-44292 |
| CVE-2026-44293 / GHSA-66ff-xgx4-vchm | HIGH | protobuf.js: Code injection through bytes field defaults in generated toObject code | 7.5.6, 8.0.2 | https://osv.dev/vulnerability/GHSA-66ff-xgx4-vchm ; https://github.com/advisories/GHSA-66ff-xgx4-vchm ; https://www.cve.org/CVERecord?id=CVE-2026-44293 |
| CVE-2026-44294 / GHSA-2pr8-phx7-x9h3 | MEDIUM | protobuf.js: Denial of service from crafted field names in generated code | 7.5.6, 8.0.2 | https://osv.dev/vulnerability/GHSA-2pr8-phx7-x9h3 ; https://github.com/advisories/GHSA-2pr8-phx7-x9h3 ; https://www.cve.org/CVERecord?id=CVE-2026-44294 |

*Full OSV package listing: https://osv.dev/list?ecosystem=npm&q=protobufjs*

## Security Posture Notes

- `protobufjs` is high-blast-radius infrastructure: npm reported more than 62 million weekly downloads during this review, and it is commonly used transitively for protobuf parsing / serialization in Node.js applications and tooling.
- Prototype-pollution and prototype-injection boundaries recur across the public record. The 2022 and 2023 advisories cover direct prototype-pollution issues, while the 2026 cluster includes generated-message constructor and code-generation gadget variants that become important when `.proto` definitions or message data can be attacker influenced.
- Dynamic code-generation paths are a distinct risk theme. Public records include `CVE-2026-41242` arbitrary code execution fixed in `7.5.5` / `8.0.1`, followed by `CVE-2026-44293` code injection through bytes-field defaults fixed in `7.5.6` / `8.0.2`.
- Resource-exhaustion records span older parser-regex DoS (`CVE-2018-3738`) and newer recursion / option-path / crafted-field-name DoS issues fixed in `7.5.6` and `8.0.2`.
- Upstream `SECURITY.md` lists only `8.x` and `7.5.x` as supported release lines, states that `< 7.5` is unsupported, and says malformed or adversarial `.proto` / JSON descriptor input is now considered part of the supported input surface for active lines.
- Upstream releases show active parallel maintenance for the 7.x and 8.x lines in 2026: `protobufjs-v7.5.5` explicitly backported two reported security fixes, `protobufjs-v7.5.6` backported input hardening and CLI fixes, and `protobufjs-v8.0.2` carried the corresponding 8.x hardening.
- The review did not perform active vulnerability hunting or exploit validation; it only normalized already-public advisory and release-note evidence.

## Dependencies of Note

- Consumers should inventory both direct `protobufjs` usage and transitive usage through code-generation / API-client tooling, because application exposure depends heavily on whether untrusted schemas, descriptors, options, or message payloads reach parser and generated-code paths.
- Package managers may resolve either 7.x or 8.x depending on dependency constraints. Public fixed versions often list both `7.5.x` and `8.0.x`, so remediation checks should verify the actually installed major line rather than assuming npm `latest` applies everywhere.

## Open Questions

- Are there public downstream incident reports or maintainer write-ups that clarify reachability for the 2026 generated-code and option-path vulnerabilities in common frameworks or API-client generators?
- Should future passes split CLI / static-code-generation exposure from runtime parser / reflection exposure for packages that use `protobufjs` only at build time?

## Related Pages

- [[npm/jsonwebtoken]]
- [[npm/js-yaml]]
- [[npm/lodash]]
- [[npm/yargs-parser]]
- [[npm/index]]

---
*Last updated: 2026-05-12 | Sources: OSV package query and individual vulnerability records for `protobufjs`; GitHub Advisory Database records; public CVE aliases; npm registry and downloads API; upstream SECURITY.md and GitHub releases; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid.*
