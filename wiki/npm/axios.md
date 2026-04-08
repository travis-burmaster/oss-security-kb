# axios (npm)

**Registry:** npm
**Weekly Downloads:** unknown (as of 2026-04-08)
**Repository:** https://github.com/axios/axios
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-fw8c-xr5c-95f9 / MAL-2026-2306 | Critical | Compromised npm publishes of axios introduced a malicious transitive dependency (`plain-crypto-js`) and remote-access-trojan behavior in published package versions | Downgrade immediately to 1.14.0 (1.x) or 0.30.3 (0.x); avoid 1.14.1 and 0.30.4 | https://advisories.gitlab.com/pkg/npm/axios/GHSA-fw8c-xr5c-95f9/ |

## Security Posture Notes

- Axios is one of the most widely used HTTP client libraries in the JavaScript ecosystem, so supply-chain compromise has unusually large blast radius.
- This incident is notable because it was not just a normal code vulnerability; it appears to have involved compromised package publication and malicious dependency injection.
- Public reporting indicates the npm registry removed the malicious versions and that the `latest` tag was reverted to a safe release.
- This package should become a model KB page for documenting supply-chain compromise response, not just traditional code defects.

## Dependencies of Note

- `plain-crypto-js@4.2.1` was publicly reported as the malicious transitive dependency associated with the compromised publish incident.

## Open Questions

- Has axios published a formal post-incident disclosure or postmortem beyond issue threads and external writeups?
- What hardening steps were taken for maintainer accounts, npm publishing, and release verification after the incident?
- Which downstream packages or lockfiles may still have pulled the compromised versions during the exposure window?

## Related Pages

- [[npm/index]]
- [[npm/express]]
- [[npm/koa-router]]

---
*Last updated: 2026-04-08 | Sources: 4*
