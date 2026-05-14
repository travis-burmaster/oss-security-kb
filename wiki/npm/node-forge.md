# node-forge (npm)

**Registry:** npm
**Weekly Downloads:** ~33,510,143 (2026-05-06 to 2026-05-12)
**Repository:** https://github.com/digitalbazaar/forge
**Security Contact:** GitHub Security Advisories / repository maintainers
**Disclosure Policy:** https://github.com/digitalbazaar/forge/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-14 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / upstream repository advisories surfaced through OSV, public CVE / NVD records, upstream commits / PRs referenced by public advisories, npm registry metadata, npm downloads API, GitHub repository metadata, local Claude-compatible proxy synthesis used as a drafting aid) | Added an advisory-mapped baseline for `node-forge`, covering public signature-verification, certificate-chain-validation, ASN.1 parsing, BigInteger denial-of-service, URL parsing / open redirect, and legacy prototype-pollution advisories through the `1.4.0` fix train. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-33896 / GHSA-2328-f5f3-gj25 | High | Public advisory describes an RFC 5280 certificate-chain verification bypass involving `basicConstraints` handling. | 1.4.0 | https://github.com/digitalbazaar/forge/security/advisories/GHSA-2328-f5f3-gj25 |
| CVE-2026-33894 / GHSA-ppp5-5v6c-4jwp | High | RSA-PKCS signature forgery due to accepting ASN.1 structures with an extra field in the encoded digest information. | 1.4.0 | https://github.com/digitalbazaar/forge/security/advisories/GHSA-ppp5-5v6c-4jwp |
| CVE-2026-33895 / GHSA-q67f-28xg-22rw | High | Ed25519 signature forgery / malleability because verification missed the `S > L` order-bound check. | 1.4.0 | https://github.com/digitalbazaar/forge/security/advisories/GHSA-q67f-28xg-22rw |
| CVE-2026-33891 / GHSA-5m6q-g25r-mvwx | High | Denial of service from an infinite loop in `BigInteger.modInverse()` when called with zero input. | 1.4.0 | https://github.com/digitalbazaar/forge/security/advisories/GHSA-5m6q-g25r-mvwx |
| CVE-2025-66031 / GHSA-554w-wpv2-vw27 | High | ASN.1 parser unbounded recursion can allow denial of service on crafted nested input. | 1.3.2 | https://github.com/digitalbazaar/forge/security/advisories/GHSA-554w-wpv2-vw27 |
| CVE-2025-12816 / GHSA-5gfm-wpxj-wjgq | High | ASN.1 validator desynchronization / interpretation-conflict issue in public advisory data. | 1.3.2 | https://github.com/digitalbazaar/forge/security/advisories/GHSA-5gfm-wpxj-wjgq |
| CVE-2025-66030 / GHSA-65ch-62r8-g69g | Moderate | ASN.1 OID integer-truncation vulnerability that can alter interpreted object identifiers. | 1.3.2 | https://github.com/digitalbazaar/forge/security/advisories/GHSA-65ch-62r8-g69g |
| CVE-2022-24771 / GHSA-cfm4-qjh2-4765 | High | Improper cryptographic-signature verification in `node-forge`; public records tie the fix to the 1.3.0 signature-validation release. | 1.3.0 | https://github.com/digitalbazaar/forge/security/advisories/GHSA-cfm4-qjh2-4765 |
| CVE-2022-24772 / GHSA-x4jg-mjrx-434g | High | Improper cryptographic-signature verification in `node-forge`, fixed alongside the 2022 1.3.0 signature-validation cluster. | 1.3.0 | https://github.com/digitalbazaar/forge/security/advisories/GHSA-x4jg-mjrx-434g |
| CVE-2022-24773 / GHSA-2r2c-g63r-vccr | Moderate | Improper cryptographic-signature verification in `node-forge`, fixed alongside the 2022 1.3.0 signature-validation cluster. | 1.3.0 | https://github.com/digitalbazaar/forge/security/advisories/GHSA-2r2c-g63r-vccr |
| CVE-2022-0122 / GHSA-8fr3-hfg3-gpgp / GHSA-gf8q-jrpm-jvxq | Moderate | URL parsing / open-redirect behavior; OSV includes both a CVE-backed record and an upstream GHSA record for the same public vulnerability lineage. | 1.0.0 | https://github.com/advisories/GHSA-8fr3-hfg3-gpgp |
| GHSA-5rrq-pxf6-6jx5 | Low | Prototype pollution in the legacy `node-forge` debug API. | 1.0.0 | https://github.com/digitalbazaar/forge/security/advisories/GHSA-5rrq-pxf6-6jx5 |
| CVE-2020-7720 / GHSA-92xj-mqp7-vmcj | High | Prototype pollution in `node-forge`, fixed in the 0.10.0 line according to public OSV / advisory records. | 0.10.0 | https://github.com/advisories/GHSA-92xj-mqp7-vmcj |
| GHSA-wxgw-qj99-44c2 | Low | Prototype pollution in the `util.setPath` API. | 0.10.0 | https://github.com/digitalbazaar/forge/security/advisories/GHSA-wxgw-qj99-44c2 |

## Security Posture Notes

- `node-forge` is a high-blast-radius JavaScript cryptography and PKI package, with roughly 33.5M npm downloads in the review window.
- The latest npm release observed in this pass is `1.4.0`, which public advisory data lists as the fixed version for the March 2026 certificate-chain, RSA / Ed25519 signature, and BigInteger denial-of-service records.
- The public vulnerability history is concentrated around cryptographic verification semantics, ASN.1 parsing / validation, and older utility APIs that exposed prototype-pollution and URL-parsing issues.
- Consumers should not treat the package as a generic parser for untrusted ASN.1 / certificate material unless they are on a fixed release and have input-size / recursion controls appropriate for their application.
- The GitHub repository was not archived during this review and showed recent activity, but downstream dependency trees may still pin older `0.x` / `1.0.x` / `1.3.x` releases.

## Recommendations for Developers

1. Upgrade to `node-forge@1.4.0` or newer to pick up the latest public fixed-version boundary identified in this review.
2. Inventory transitive uses in TLS, PKI, JWT/JWK, certificate-chain validation, browser-crypto polyfill, and build-tool dependency trees.
3. Prefer platform cryptography APIs or narrowly scoped, well-reviewed libraries for new cryptographic designs where possible.
4. Apply defense-in-depth around attacker-controlled certificate, ASN.1, RSA signature, Ed25519 signature, or BigInteger inputs.
5. Treat older `0.x`, `1.0.x`, and pre-`1.3.2` dependency pins as priority upgrade candidates, even when the affected use is transitive.

## Dependencies of Note

- Frequently appears transitively in JavaScript cryptography, certificate, PKI, TLS, WebCrypto-polyfill, and signing workflows.
- Highest-risk deployments are those verifying attacker-supplied certificates or signatures, parsing attacker-supplied ASN.1, or using older utility APIs with untrusted object paths.

## Open Questions

- Which top-level npm packages still pin `node-forge` below `1.4.0` after the 2026 advisory cluster?
- Are downstream applications relying on `node-forge` for certificate-chain decisions that should instead use platform TLS / PKI validation?
- Would a cross-package JavaScript crypto-primitives page help compare recurring issues across `node-forge`, `elliptic`, `jsonwebtoken`, `crypto-js`, and platform APIs?

## Related Pages

- [[npm/elliptic]]
- [[npm/jsonwebtoken]]
- [[npm/index]]

---
*Last updated: 2026-05-14 | Sources: 21 (OSV.dev package query for npm/node-forge, OSV vulnerability records for all GHSA IDs listed above, GitHub Advisory Database / upstream repository security advisory records surfaced through OSV, public CVE / NVD records, upstream commits / PRs referenced by public advisories, npm registry metadata, npm downloads API, GitHub repository metadata, local Claude-compatible proxy synthesis used as drafting aid only)*
