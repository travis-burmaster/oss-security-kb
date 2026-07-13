# gjson (Go)

**Registry:** pkg.go.dev
**Module:** github.com/tidwall/gjson
**Weekly Downloads:** ~2–3M/week est. (10,420 importers as of 2026-07-13)
**Repository:** https://github.com/tidwall/gjson
**Security Contact:** none listed (reports via GitHub issues)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No public proactive audits on record.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-35380 / GHSA-w942-gw6m-p62c | **High CVSS 7.5** | Out-of-bounds panic: maliciously crafted JSON objects trigger an OOB memory access causing a `panic`, enabling remote DoS. Distinct code path from CVE-2020-36066/36067. | 1.6.4 | [GHSA-w942-gw6m-p62c](https://github.com/advisories/GHSA-w942-gw6m-p62c) |
| CVE-2020-36066 / GHSA-wjm3-fq3r-5x46 | **High CVSS 9.1** | Denial of service via crafted JSON: a specially formed JSON document triggers a panic; distinct from CVE-2020-35380 (different code path). | 1.6.5 | [GHSA-wjm3-fq3r-5x46](https://github.com/advisories/GHSA-wjm3-fq3r-5x46) |
| CVE-2020-36067 / GHSA-p64j-r5f4-pwwx | **High CVSS 7.5** | Improper array-index validation: a crafted GET call causes `panic: runtime error: slice bounds out of range`; distinct from CVE-2020-35380/36066. | 1.6.6 | [GHSA-p64j-r5f4-pwwx](https://github.com/advisories/GHSA-p64j-r5f4-pwwx) |
| CVE-2021-42836 / GHSA-ppj4-34rq-v8j9 | **High CVSS 9.1** | ReDoS: crafted JSON input triggers a regular-expression denial of service in the path evaluation engine; attackers who supply JSON to any gjson parsing call can cause unbounded CPU consumption. | 1.9.3 | [GHSA-ppj4-34rq-v8j9](https://github.com/advisories/GHSA-ppj4-34rq-v8j9) |

*Note: GHSA-c9gm-7rfj-8w5h (2022) was published as a duplicate of GHSA-ppj4-34rq-v8j9 and subsequently withdrawn.*

## Security Posture Notes

- **gjson** is a widely-used Go JSON path extraction library with 10,420+ importers including CLI tools, API proxies, observability pipelines, and Kubernetes operators; any service that parses attacker-controlled JSON via gjson is in-scope for the above DoS advisories.
- **CVE-2020-35380/36066/36067 cluster:** Three distinct out-of-bounds / bounds-check failures in the JSON parsing engine, fixed in rapid succession across 1.6.4, 1.6.5, and 1.6.6. All three require only access to the JSON parsing path; no authentication needed for network-accessible services. Any deployment on < 1.6.6 should treat all three as a combined DoS cluster and upgrade in one step.
- **CVE-2021-42836 (ReDoS):** A separate class of issue — attacker-controlled JSON can trigger catastrophic backtracking in a regex used in gjson's path evaluation. Affects < 1.9.3; fixed by replacing the regex with a non-backtracking implementation.
- **No advisories found post-1.9.3:** The GitHub Advisory Database search found no additional gjson advisories for versions 1.9.3 through 1.19.0 (current as of May 2026). The library appears to have maintained a clean advisory record for four+ years post-1.9.3.
- **No formal security contact or SECURITY.md:** Vulnerability reports should be submitted via GitHub issues or the repository contact; there is no dedicated private disclosure channel listed.

## Dependencies of Note

- None flagged.

## Open Questions

- Does the gjson path evaluation engine have ongoing fuzzing coverage (OSS-Fuzz or equivalent)?
- Should a formal SECURITY.md and private reporting path be added upstream?

## Related Pages

- [[go/index]]

---
*Last updated: 2026-07-13 | Sources: 4 (GHSA-w942-gw6m-p62c, GHSA-wjm3-fq3r-5x46, GHSA-p64j-r5f4-pwwx, GHSA-ppj4-34rq-v8j9)*
