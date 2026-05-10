# org.bouncycastle:bcprov-jdk18on (Maven)

**Registry:** Maven (Maven Central)
**Weekly Downloads:** unknown
**Repository:** https://github.com/bcgit/bc-java
**Security Contact:** Bouncy Castle project / GitHub Security Advisory process
**Disclosure Policy:** not identified in this pass
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-10 | OpenClaw recurring review | advisory mapping (public records only) | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database aliases, public CVE records, Bouncy Castle CVE wiki / release notes, Maven Central metadata; local proxy synthesis used only as a drafting aid) | Added initial Maven package page mapping 9 public `bcprov-jdk18on` advisories across timing side channels, certificate / ASN.1 denial of service, LDAP injection, and DNS-poisoning-relevant certificate validation behavior. | https://osv.dev/list?ecosystem=Maven&q=org.bouncycastle%3Abcprov-jdk18on |

## Known Vulnerabilities

The table below is a package-level public advisory map from OSV.dev for `org.bouncycastle:bcprov-jdk18on`, cross-checked against GHSA aliases, public CVE records, Bouncy Castle CVE wiki pages / release notes, and Maven Central metadata. Maven Central metadata reported `1.84` as the latest release during this pass.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-5598 / GHSA-p93r-85wp-75v3 | High / timing side channel | Bouncy Castle's public advisory describes non-constant-time comparisons that can risk private-key leakage in FrodoKEM; OSV maps affected `bcprov-jdk18on` releases from 1.71 through 1.83. | 1.84 | https://osv.dev/vulnerability/GHSA-p93r-85wp-75v3 ; https://github.com/bcgit/bc-java/wiki/CVE-2026-5598 ; https://www.bouncycastle.org/latest_releases.html |
| CVE-2026-0636 / GHSA-c3fc-8qff-9hwx | Moderate / LDAP injection | LDAP injection in `LDAPStoreHelper.java`; OSV maps the maintained JDK 18+ provider line from 1.74 through 1.83, and Bouncy Castle release notes list the fix in the 1.84 security-fix set. | 1.84 | https://osv.dev/vulnerability/GHSA-c3fc-8qff-9hwx ; https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%900636 ; https://www.bouncycastle.org/latest_releases.html |
| CVE-2025-8885 / GHSA-67mf-3cr5-8w23 | Moderate / DoS | Excessive allocation in `ASN1ObjectIdentifier` processing can allow crafted ASN.1 input to drive resource consumption. | 1.78 | https://osv.dev/vulnerability/GHSA-67mf-3cr5-8w23 ; https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902025%E2%80%908885 |
| CVE-2024-34447 / GHSA-4h8f-2wvx-gg5w | Moderate / certificate validation integrity | Bouncy Castle's Java cryptography API advisory is described by OSV / CVE records as DNS-poisoning-relevant behavior in certificate validation paths. | 1.78 | https://osv.dev/vulnerability/GHSA-4h8f-2wvx-gg5w ; https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902024%E2%80%9034447 ; https://nvd.nist.gov/vuln/detail/CVE-2024-34447 |
| CVE-2024-30171 / GHSA-v435-xc8x-wvr9 | Moderate / timing side channel | RSA key-exchange timing side channel associated with the Marvin Attack class; OSV maps the fix boundary for `bcprov-jdk18on` to 1.78. | 1.78 | https://osv.dev/vulnerability/GHSA-v435-xc8x-wvr9 ; https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902024%E2%80%9030171 |
| CVE-2024-30172 / GHSA-m44j-cfrm-g8qc | Moderate / DoS | Crafted signature and public-key inputs can trigger an infinite loop in affected Bouncy Castle Java releases. | 1.78 | https://osv.dev/vulnerability/GHSA-m44j-cfrm-g8qc ; https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902024%E2%80%9030172 |
| CVE-2024-29857 / GHSA-8xfc-gm6g-vgpv | Moderate / DoS | Certificate parsing issues can cause high CPU usage during parameter evaluation, making malformed certificate material a resource-exhaustion risk. | 1.78 | https://osv.dev/vulnerability/GHSA-8xfc-gm6g-vgpv ; https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902024%E2%80%9029857 |
| CVE-2023-33201 / GHSA-hr8g-6v94-x4m9 | Moderate / LDAP injection | Earlier LDAP injection record in Bouncy Castle's certificate-store lookup behavior; OSV lists the fix boundary at 1.74. | 1.74 | https://osv.dev/vulnerability/GHSA-hr8g-6v94-x4m9 ; https://bouncycastle.org/releasenotes.html#r1rv74 |
| CVE-2023-33202 / GHSA-wjxj-5m7g-mg7q | Moderate / DoS | Denial-of-service record in Bouncy Castle Java; OSV lists the affected `bcprov-jdk18on` line through 1.72 and the fix at 1.73. | 1.73 | https://osv.dev/vulnerability/GHSA-wjxj-5m7g-mg7q ; https://github.com/bcgit/bc-java/wiki/CVE-2023-33202 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.bouncycastle%3Abcprov-jdk18on*

## Security Posture Notes

- The public advisory pattern is concentrated in **cryptographic side channels**, **certificate / ASN.1 parsing resource exhaustion**, and **directory / name-resolution boundary behavior** rather than web-framework-style request handling.
- `1.78` is a major security boundary for the 2024 cluster, including the Marvin Attack timing-side-channel record, certificate parsing CPU exhaustion, infinite-loop DoS, DNS-poisoning-relevant certificate validation behavior, and ASN.1 object identifier excessive allocation.
- `1.84` is the current Maven Central release and the fix boundary for the 2026 LDAP injection and FrodoKEM timing-channel records surfaced in this pass. Projects that can upgrade should prefer `>= 1.84` over stopping at the 1.78 boundary.
- Impact depends heavily on how the provider is used. Risk is highest where services process attacker-supplied certificates, signatures, keys, ASN.1 objects, LDAP-backed certificate stores, or KEM inputs in online request paths.
- Because Bouncy Castle is often present as a transitive cryptographic provider, downstream inventory should check SBOMs, shaded JARs, application-server bundles, and framework dependency trees rather than only direct `pom.xml` declarations.

## Dependencies of Note

- This page focuses on the direct `org.bouncycastle:bcprov-jdk18on` artifact. Related Bouncy Castle artifacts such as `bcpkix-jdk18on` can share some advisory records but should be mapped separately when the KB expands coverage.
- Maven Central metadata showed active releases through `1.84`; no private or unpublished vulnerability claims were used.

## Open Questions

- Should the KB add sibling pages for `org.bouncycastle:bcpkix-jdk18on` and older `jdk15on` / `jdk15to18` lines to make Bouncy Castle artifact-family coverage easier to follow?
- Which high-usage Java frameworks or enterprise products still pin Bouncy Castle provider versions below 1.78 or 1.84 in supported release trains?
- Should the KB add a cross-ecosystem note for cryptographic timing side-channel advisories that compares Bouncy Castle Java, Bouncy Castle C#, OpenSSL, and language-native crypto libraries?

## Related Pages

- [[maven/org.springframework/spring-core]]
- [[maven/org.apache.logging.log4j/log4j-core]]
- [[maven/index]]

---
*Last updated: 2026-05-10 | Sources: 6 (OSV package query and individual vulnerability records, GitHub Advisory Database public aliases, public CVE records, Bouncy Castle CVE wiki pages, Bouncy Castle release notes, Maven Central metadata)*
