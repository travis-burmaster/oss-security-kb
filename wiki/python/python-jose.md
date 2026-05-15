# python-jose (python)

**Registry:** PyPI  
**Weekly Downloads:** ~9,680,663 (PyPIStats last week, fetched 2026-05-15)  
**Repository:** https://github.com/mpdavis/python-jose  
**Security Contact:** GitHub issue tracker / repository security posture not further confirmed in this pass  
**Disclosure Policy:** none located in this pass  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-15 | OpenClaw recurring review | package-level public advisory mapping for PyPI `python-jose` | public-source curation from OSV.dev package and vulnerability records, GitHub Advisory Database records surfaced through OSV, public CVE / NVD records, upstream issues / PRs / releases referenced by public records, PyPI metadata, PyPIStats download data, and local proxy-assisted drafting | Added initial advisory-mapped page for python-jose's published JOSE / JWT vulnerability history: HMAC timing comparison, OpenSSH ECDSA key algorithm confusion, and compressed-JWE resource-exhaustion behavior fixed through 3.4.0. | https://osv.dev/list?ecosystem=PyPI&q=python-jose |

## Known Vulnerabilities

OSV returns canonical GHSA records plus PYSEC aliases for the same underlying issues. This page counts the three GHSA / CVE-backed vulnerability records once each and keeps fixed-version boundaries tied to public advisory metadata.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2016-7036 / GHSA-w799-prg3-cx77 / PYSEC-2017-28 | Critical | Versions before 1.3.2 failed to use constant-time comparison for HMAC keys, creating a timing side-channel in token verification contexts. | 1.3.2 | https://github.com/advisories/GHSA-w799-prg3-cx77 ; https://nvd.nist.gov/vuln/detail/CVE-2016-7036 ; https://github.com/mpdavis/python-jose/releases/tag/1.3.2 |
| CVE-2024-33663 / GHSA-6c5p-j8vq-pqhj / PYSEC-2024-232 | Critical | Versions through 3.3.0 had algorithm confusion with OpenSSH ECDSA keys and other key formats, a JOSE verification-boundary issue similar in class to PyJWT CVE-2022-29217. | 3.4.0 | https://github.com/advisories/GHSA-6c5p-j8vq-pqhj ; https://nvd.nist.gov/vuln/detail/CVE-2024-33663 ; https://github.com/mpdavis/python-jose/issues/346 |
| CVE-2024-33664 / GHSA-cjwg-qfpm-7377 / PYSEC-2024-233 | Moderate | Versions through 3.3.0 could consume excessive resources when decoding a crafted compressed JWE token with a high compression ratio, described publicly as a "JWT bomb" denial-of-service issue. | 3.4.0 | https://github.com/advisories/GHSA-cjwg-qfpm-7377 ; https://nvd.nist.gov/vuln/detail/CVE-2024-33664 ; https://github.com/mpdavis/python-jose/issues/344 ; https://github.com/mpdavis/python-jose/pull/345 ; https://github.com/mpdavis/python-jose/releases/tag/3.4.0 |

*Full OSV package listing: https://osv.dev/list?ecosystem=PyPI&q=python-jose*

## Security Posture Notes

- `python-jose` is a JOSE / JWT implementation with high authentication and authorization blast radius when used for bearer-token verification. This pass measured roughly 9.7M weekly and 41.4M monthly PyPI downloads.
- The public advisory history clusters around cryptographic verification semantics and token decompression / parsing resource consumption. These are high-impact boundaries because small API misunderstandings can become authentication bypasses or service-wide denial of service.
- The 2024 fix train is important for deployments still on `3.3.0` or earlier: both the OpenSSH ECDSA key algorithm-confusion issue and compressed-JWE resource-exhaustion issue list `3.4.0` as the fixed version in public records. PyPI metadata showed current latest `3.5.0` during this review.
- This page does not claim a full-source audit or active vulnerability assessment. It only normalizes public advisory, CVE, upstream issue / PR / release, and package metadata.

## Dependencies of Note

- Consumers should verify which cryptographic backend / optional extras they install and which key formats they allow in token verification paths.
- Applications should restrict accepted JOSE algorithms and key material explicitly rather than relying on unvalidated token headers or ambiguous key formats.
- Services that accept JWE input should consider decompression and token-size limits at application boundaries in addition to package upgrades.

## Open Questions

- Is there a documented private disclosure policy or security contact for the upstream project that should be captured if later published?
- Should future KB work add or refresh adjacent JOSE / JWT packages such as `pyjwt`, `authlib`, or `jwcrypto` for comparison against algorithm-confusion and decompression-risk classes?
- Are there public third-party audits of python-jose's key handling and JWE/JWS parsing surfaces that can be cited without relying on private assessments?

## Related Pages

- [[python/cryptography]]
- [[npm/jsonwebtoken]]
- [[go/github.com/golang-jwt/jwt]]
- [[python/index]]

---
*Last updated: 2026-05-15 | Sources: OSV package query and individual vulnerability records for PyPI `python-jose`; GitHub Advisory Database entries for GHSA-w799-prg3-cx77, GHSA-6c5p-j8vq-pqhj, and GHSA-cjwg-qfpm-7377; public CVE / NVD records for CVE-2016-7036, CVE-2024-33663, and CVE-2024-33664; PyPA advisory aliases; upstream issues, PR, release references, and PyPI metadata; PyPIStats recent download data; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid.*
