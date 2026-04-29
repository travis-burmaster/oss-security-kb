# ajv (npm)

**Registry:** npm
**Weekly Downloads:** ~271,662,197 (as of 2026-04-25)
**Repository:** https://github.com/ajv-validator/ajv
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** none confirmed in this pass
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No audits on record.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-15366 / GHSA-v88g-cgmw-v5xw | Moderate | Prototype pollution in `ajv.validate()` from untrusted-schema handling; the public record says versions before `6.12.3` were affected. | 6.12.3 | [GHSA](https://github.com/advisories/GHSA-v88g-cgmw-v5xw), [OSV.dev](https://osv.dev/vulnerability/GHSA-v88g-cgmw-v5xw), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2020-15366), [v6.12.3 release](https://github.com/ajv-validator/ajv/releases/tag/v6.12.3) |
| CVE-2025-69873 / GHSA-2g4f-4pwh-qvx6 | Moderate | ReDoS when the `$data` option is enabled and runtime data can flow into the `pattern` keyword, which is passed into JavaScript `RegExp()` construction; public records show fixes on both the older `6.x` and modern `8.x` lines. | 6.14.0, 8.18.0 | [GHSA](https://github.com/advisories/GHSA-2g4f-4pwh-qvx6), [OSV.dev](https://osv.dev/vulnerability/GHSA-2g4f-4pwh-qvx6), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-69873), [upstream fix PRs](https://github.com/ajv-validator/ajv/pull/2586), [v8.18.0 release](https://github.com/ajv-validator/ajv/releases/tag/v8.18.0), [v6.14.0 release](https://github.com/ajv-validator/ajv/releases/tag/v6.14.0), [public disclosure writeup](https://raw.githubusercontent.com/EthanKim88/ethan-cve-disclosures/main/CVE-2025-69873-ajv-ReDoS.md) |

## Security Posture Notes

- Public package-scoped OSV / GHSA evidence gathered in this pass surfaced two direct published `ajv` advisories: a 2020 prototype-pollution issue on the `6.x` line and a 2025 ReDoS issue affecting both the legacy `6.x` and current `8.x` lines.
- The 2025 ReDoS record is narrower than a generic “ajv regex bug” claim: the public advisory and release notes tie it specifically to use of the `$data` option with the `pattern` keyword (runtime data becomes the pattern), so deployments not using `$data` may have less practical exposure even though upgrading remains the right fix.
- The public disclosure writeup for CVE-2025-69873 describes a remote DoS scenario where attacker-controlled data supplies a catastrophic-backtracking regex pattern (for example `^(a|a)*$`) when `$data: true` is enabled. (Treat this as illustrative context from that writeup, not a guarantee of exploitability in every deployment.)
- The `v8.18.0` release notes explicitly call out the security fix as “use configured RegExp engine with $data keyword to mitigate ReDoS attacks,” which makes the newer fix trail unusually clear for KB normalization.
- Current npm metadata shows `ajv` is well beyond the public fix points on the latest line, but its huge transitive reach still makes older vulnerable pins operationally relevant.
- No repository `SECURITY.md` or equivalent disclosure-policy file was confirmed via the GitHub contents API in this pass, so the page stays anchored to package advisories rather than implying a stronger upstream disclosure posture than was verified here.

## Dependencies of Note

- None flagged from this compact public-advisory pass.

## Open Questions

- Are there older security-relevant `ajv-keywords` or schema-extension interactions that later matured into package-scoped advisories and should be normalized separately from core `ajv`?
- Does upstream publish a preferred private-reporting channel outside a repository `SECURITY.md`, or is GitHub Security Advisories the de facto path?

## Related Pages

- [[npm/zod]]
- [[npm/yaml]]
- [[npm/index]]

---
*Last updated: 2026-04-29 | Sources: 11 (OSV.dev package query and vulnerability records, GitHub Advisory Database, public CVE / NVD records for CVE-2020-15366 and CVE-2025-69873, upstream fix PR / commit references surfaced through OSV, v6.12.3 release notes, v8.18.0 release notes, v6.14.0 tag/release reference, npm registry metadata, npm downloads API, public disclosure writeup for CVE-2025-69873 at EthanKim88/ethan-cve-disclosures)*
