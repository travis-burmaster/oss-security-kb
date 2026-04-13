# minimist (npm)

**Registry:** npm
**Weekly Downloads:** unknown (as of 2026-04-07)
**Repository:** https://github.com/minimistjs/minimist
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
| CVE-2020-7598 | High | Prototype pollution via argument parsing | 1.2.3 / 0.2.1 | https://github.com/advisories/GHSA-vh95-rmgr-6w4m |
| CVE-2021-44906 | Critical | Incomplete fix for prior prototype pollution issue; `constructor.prototype` payloads still reached object prototypes | 1.2.6 / 0.2.4 | https://github.com/advisories/GHSA-xvch-5gv4-984h |

## Security Posture Notes

- Tiny package, huge blast radius because it sits in CLI parsing paths throughout the npm ecosystem.
- Historically important because the bug class is simple, common, and widely propagated through transitive dependencies.
- Public advisory history shows a clear incomplete-fix pattern: CVE-2020-7598 covered `__proto__`-style pollution payloads, but a later published follow-up (CVE-2021-44906 / GHSA-xvch-5gv4-984h) states that `constructor.prototype` paths in `setKey()` still remained reachable before 1.2.6 / 0.2.4.
- The public OSV / GHSA records make the exploit precondition explicit: the issue matters when attackers can control argv-like input passed into `minimist`, which is common in wrapper CLIs, task runners, and developer tooling.
- The public fix trail is also unusually useful for KB readers: GitHub Advisory references point to multiple fix commits, and the public backport thread plus PR `#24` ("Robustness: rework isConstructorOrProto") show that maintainers revisited the original mitigation rather than treating the 2020 patch as final.
- Public proof-of-concept material exists showing practical `__proto__` and `constructor.prototype` payload exploitation, which makes minimist valuable as a teaching/example package for argument-parser risk.
- High-value candidate for surface mapping beyond just known CVEs.

## Dependencies of Note

- Often appears as a transitive dependency in CLIs and build tools.
- Especially important to track transitively because downstream consumers may not realize they are inheriting vulnerable parser behavior from tiny utility dependencies.

## Open Questions

- Which currently popular packages still pin vulnerable minimist versions transitively, especially on the older `0.2.x` branch?
- Has anyone published a modern full-source audit after the `1.2.6` / `0.2.4` follow-up fixes landed?
- Are there parser edge cases beyond the published `__proto__` and `constructor.prototype` CVE lineage worth cataloging?
- Which downstream exploit chains turn this parser flaw into practical command execution, config corruption, or environment tampering?

## Related Pages

- [[npm/index]]
- [[npm/lodash]]
- [[npm/semver]]

---
*Last updated: 2026-04-13 | Sources: 6 (GitHub Advisory Database / GHSA, OSV, CVE records, public maintainer issue + PR history)*
