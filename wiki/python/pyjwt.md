# PyJWT (python)

**Registry:** PyPI  
**Weekly Downloads:** ~147,409,400 (PyPIStats last week, fetched 2026-05-15)  
**Repository:** https://github.com/jpadilla/pyjwt  
**Security Contact:** GitHub Security Advisory workflow / security@jpadilla.com  
**Disclosure Policy:** https://github.com/jpadilla/pyjwt/security/policy  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-15 | OpenClaw recurring review | package-level public advisory mapping for PyPI `PyJWT` / OSV package `pyjwt` | public-source curation from OSV.dev package and vulnerability records, GitHub Advisory Database records surfaced through OSV, public CVE / NVD records, upstream changelog and security policy, PyPI metadata, PyPIStats download data, and local proxy-assisted drafting | Added initial advisory-mapped page for PyJWT's published JWT verification-boundary history: legacy algorithm/key confusion, non-blocklisted public-key formats, issuer partial matching, and unknown JOSE `crit` header handling fixed through 2.12.0. | https://osv.dev/list?ecosystem=PyPI&q=pyjwt |

## Known Vulnerabilities

OSV returns canonical GHSA records plus PYSEC aliases for the older issues. This page counts the four GHSA / CVE-backed vulnerability records once each and keeps fixed-version boundaries tied to public advisory metadata and upstream changelog entries.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-11424 / GHSA-r9jw-mwhq-wp62 / PYSEC-2017-24 | High | Legacy algorithm/key-confusion issue: affected versions could misuse public-key material as an HMAC verification key. The upstream 1.5.1 changelog links the fix to guarding against PKCS#1 PEM encoded public keys and warning when decoding without explicit algorithms. | 1.5.1 | https://github.com/advisories/GHSA-r9jw-mwhq-wp62 ; https://nvd.nist.gov/vuln/detail/CVE-2017-11424 ; https://github.com/jpadilla/pyjwt/pull/277 |
| CVE-2022-29217 / GHSA-ffqj-6fqr-9h24 / PYSEC-2022-202 | High | Versions from 1.5.0 before 2.4.0 could accept non-blocklisted asymmetric public-key formats as HMAC secrets, creating another key-confusion / verification-integrity boundary issue. | 2.4.0 | https://github.com/jpadilla/pyjwt/security/advisories/GHSA-ffqj-6fqr-9h24 ; https://nvd.nist.gov/vuln/detail/CVE-2022-29217 ; https://github.com/jpadilla/pyjwt/releases/tag/2.4.0 |
| CVE-2024-53861 / GHSA-75c5-xw7c-p5pm | Low | Version 2.10.0 allowed partial issuer (`iss`) matching, so an attacker-controlled issuer string could match a configured issuer prefix rather than requiring exact issuer validation. | 2.10.1 | https://github.com/jpadilla/pyjwt/security/advisories/GHSA-75c5-xw7c-p5pm ; https://nvd.nist.gov/vuln/detail/CVE-2024-53861 ; https://github.com/jpadilla/pyjwt/commit/33022c25525c1020869c71ce2a4109e44ae4ced1 |
| CVE-2026-32597 / GHSA-752w-5fwx-jx9f | High | Versions before 2.12.0 accepted JWTs containing unknown JOSE `crit` header extensions without validating that the application understood and enforced those critical parameters. | 2.12.0 | https://github.com/jpadilla/pyjwt/security/advisories/GHSA-752w-5fwx-jx9f ; https://nvd.nist.gov/vuln/detail/CVE-2026-32597 ; https://github.com/jpadilla/pyjwt/releases/tag/2.12.0 |

*Full OSV package listing: https://osv.dev/list?ecosystem=PyPI&q=pyjwt*

## Security Posture Notes

- PyJWT is a high-blast-radius authentication library. The public advisory history is compact, but all substantive records sit directly on token verification semantics rather than peripheral tooling.
- The recurring theme is JWT verification policy: callers should pin allowed algorithms, validate issuer / audience expectations exactly, reject unknown critical headers unless explicitly supported, and avoid ambiguous key formats in verification paths.
- The 2026 `crit` header advisory makes `2.12.0` the conservative minimum fixed version for the public advisory set gathered in this pass; PyPI metadata showed latest release `2.12.1`.
- Download telemetry from PyPIStats showed roughly 147M downloads in the prior week and 584M in the prior month, making even narrow verification-boundary flaws widely relevant to downstream services.
- This review did not perform active vulnerability hunting, exploit validation, or live target testing. It only normalized already-public advisory, CVE, upstream changelog / policy, and package metadata.

## Dependencies of Note

- PyJWT's verification behavior often depends on how applications configure accepted algorithms, keys, JWKS retrieval / caching, issuer, audience, leeway, and claim validation.
- Downstream frameworks and identity integrations should be reviewed for whether they expose PyJWT defaults safely, especially around algorithm allowlists and exact issuer / audience matching.

## Open Questions

- Should future KB maintenance refresh adjacent JOSE / JWT packages such as `authlib` and `jwcrypto`, which OSV now shows as having multiple public JOSE / JWE advisory records?
- Are there high-usage framework integrations that pin PyJWT below `2.12.0` or wrap its verification API in a way that weakens caller-supplied constraints?
- Should the KB add a shared JWT verification-boundary note comparing PyJWT, python-jose, jsonwebtoken, and golang-jwt/jwt?

## Related Pages

- [[python/python-jose]]
- [[npm/jsonwebtoken]]
- [[go/github.com/golang-jwt/jwt]]
- [[python/cryptography]]
- [[python/index]]

---
*Last updated: 2026-05-15 | Sources: OSV package query and individual vulnerability records for PyPI `pyjwt`; GitHub Advisory Database entries for GHSA-r9jw-mwhq-wp62, GHSA-ffqj-6fqr-9h24, GHSA-75c5-xw7c-p5pm, and GHSA-752w-5fwx-jx9f; public CVE / NVD records for CVE-2017-11424, CVE-2022-29217, CVE-2024-53861, and CVE-2026-32597; PyPA advisory aliases; upstream changelog, release, pull-request / commit, and security-policy references; PyPI metadata; PyPIStats recent download data; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid.*
