# org.bouncycastle:bcpkix-jdk18on (Maven)

**Registry:** Maven (Maven Central)
**Weekly Downloads:** unknown
**Repository:** https://github.com/bcgit/bc-java
**Security Contact:** Bouncy Castle project / GitHub Security Advisory process
**Disclosure Policy:** not identified in this pass
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-11 | OpenClaw recurring review | advisory mapping (public records only) | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database aliases surfaced through OSV, public CVE / NVD records, Bouncy Castle CVE wiki / commit references surfaced through OSV, Maven Central metadata; local proxy synthesis used only as a drafting aid) | Added initial Maven package page mapping 3 public `bcpkix-jdk18on` advisories across PEM / ASN.1 denial of service, PKIX certificate-path excessive allocation, and composite-signature validation behavior. | https://osv.dev/list?ecosystem=Maven&q=org.bouncycastle%3Abcpkix-jdk18on |

## Known Vulnerabilities

The table below is a package-level public advisory map from OSV.dev for `org.bouncycastle:bcpkix-jdk18on`, cross-checked against GHSA aliases, public CVE / NVD records, Bouncy Castle CVE wiki / commit references surfaced from the advisory trail, and Maven Central metadata. Maven Central metadata reported `1.84` as the latest release during this pass.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-5588 / GHSA-wg6q-6289-32hp | High / cryptographic validation boundary | OSV and the public advisory describe a Bouncy Castle PKIX-module issue where a draft composite-signature verifier accepts an empty signature sequence as valid; OSV maps affected `bcpkix-jdk18on` releases from 1.71 through 1.83. | 1.84 | https://osv.dev/vulnerability/GHSA-wg6q-6289-32hp ; https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%905588 ; https://nvd.nist.gov/vuln/detail/CVE-2026-5588 |
| CVE-2025-8916 / GHSA-4cx2-fc23-5wg6 | Moderate / DoS | Excessive allocation in PKIX certificate-path review code can allow crafted certificate-path inputs to drive resource consumption; OSV maps affected `bcpkix-jdk18on` releases from 1.71 through 1.78.1. | 1.79 | https://osv.dev/vulnerability/GHSA-4cx2-fc23-5wg6 ; https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902025%E2%80%908916 ; https://nvd.nist.gov/vuln/detail/CVE-2025-8916 |
| CVE-2023-33202 / GHSA-wjxj-5m7g-mg7q | Moderate / DoS | Crafted ASN.1 data parsed through `org.bouncycastle.openssl.PEMParser` can trigger an `OutOfMemoryError`, creating a denial-of-service risk for services that parse attacker-supplied PEM / certificate material. | 1.73 | https://osv.dev/vulnerability/GHSA-wjxj-5m7g-mg7q ; https://github.com/bcgit/bc-java/wiki/CVE-2023-33202 ; https://nvd.nist.gov/vuln/detail/CVE-2023-33202 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.bouncycastle%3Abcpkix-jdk18on*

## Security Posture Notes

- `1.84` is the current Maven Central release and the fix boundary for the 2026 composite-signature validation advisory. Projects that use `bcpkix-jdk18on` should prefer `>= 1.84` rather than stopping at the older 1.79 or 1.73 security boundaries.
- The public advisory surface for this artifact is concentrated in **PKIX / certificate parsing and validation** rather than generic cryptographic-provider primitives. This is distinct from, but related to, the broader `bcprov-jdk18on` provider page.
- Risk is highest where services process attacker-supplied certificates, PEM blobs, PKCS structures, or composite-signature material in online request paths.
- The `bcpkix-jdk18on` artifact starts at 1.71 in Maven Central metadata. Older upstream ranges in shared Bouncy Castle advisories therefore need artifact-specific mapping before being copied into downstream dependency guidance.
- No private, embargoed, or speculative vulnerability claims were used in this pass.

## Dependencies of Note

- This page focuses on the direct `org.bouncycastle:bcpkix-jdk18on` artifact. Related Bouncy Castle artifacts such as `bcprov-jdk18on`, FIPS artifacts, and older `jdk15on` / `jdk15to18` lines can share advisory families but should be mapped separately.
- Maven Central metadata showed active releases through `1.84` with `lastUpdated` timestamp `20260414022928` during this pass.

## Open Questions

- Should the KB add older Bouncy Castle artifact-line pages (`bcpkix-jdk15on`, `bcprov-jdk15on`, and `jdk15to18` variants) for projects still pinned to legacy Java baselines?
- Which Java frameworks or enterprise products bring `bcpkix-jdk18on` transitively into certificate, S/MIME, CMS, or PKIX validation paths?
- Should the KB add a Bouncy Castle family overview page to explain which advisories are provider-wide versus PKIX-artifact-specific?

## Related Pages

- [[maven/org.bouncycastle/bcprov-jdk18on]]
- [[maven/org.springframework/spring-webmvc]]
- [[maven/index]]

---
*Last updated: 2026-05-11 | Sources: 5 (OSV package query and individual vulnerability records, GitHub Advisory Database public aliases, public CVE / NVD records, Bouncy Castle CVE wiki / commit references surfaced through OSV, Maven Central metadata)*
