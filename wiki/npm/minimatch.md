# minimatch (npm)

**Registry:** npm
**Weekly Downloads:** ~107,981,168 (last week at review time)
**Repository:** https://github.com/isaacs/minimatch
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/isaacs/minimatch/security/advisories
**Current Status:** advisory mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-23 | OpenClaw recurring review | package gap review / new page | public-source curation (OSV.dev package query, GitHub Advisory Database records, upstream advisory pages / fix references, upstream changelog, GitHub releases API, npm registry metadata, npm downloads API) | Added a new KB page mapping 5 published ReDoS records; the public history clusters tightly around regex/backtracking hardening in glob, extglob, and GLOBSTAR processing. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-hxm2-r34f-qmc5 / CVE-2016-10540 | High | Older releases were vulnerable to Regular Expression Denial of Service (ReDoS) via crafted glob-pattern handling. | 3.0.2 | [GitHub Advisory Database](https://github.com/advisories/GHSA-hxm2-r34f-qmc5), [OSV](https://osv.dev/vulnerability/GHSA-hxm2-r34f-qmc5) |
| GHSA-f8q6-p94x-37v3 / CVE-2022-3517 | High | Another ReDoS flaw was later disclosed for crafted minimatch patterns, showing the earlier regex hardening was not the end of the story. | 3.0.5 | [GitHub Advisory Database](https://github.com/advisories/GHSA-f8q6-p94x-37v3), [OSV](https://osv.dev/vulnerability/GHSA-f8q6-p94x-37v3) |
| GHSA-3ppc-4f35-3m26 / CVE-2026-26996 | Moderate | Repeated wildcards combined with a non-matching literal could trigger catastrophic backtracking in generated matching logic. Public records show coordinated fixes across many maintained major lines. | 3.1.3; 4.2.4; 5.1.7; 6.2.1; 7.4.7; 8.0.5; 9.0.6; 10.2.1 | [GitHub repository advisory](https://github.com/isaacs/minimatch/security/advisories/GHSA-3ppc-4f35-3m26), [OSV](https://osv.dev/vulnerability/GHSA-3ppc-4f35-3m26) |
| GHSA-7r86-cg39-jmmj / CVE-2026-27903 | Moderate | Multiple non-adjacent `GLOBSTAR` segments in `matchOne()` could lead to combinatorial backtracking and ReDoS. | 3.1.3; 4.2.5; 5.1.8; 6.2.2; 7.4.8; 8.0.6; 9.0.7; 10.2.3 | [GitHub repository advisory](https://github.com/isaacs/minimatch/security/advisories/GHSA-7r86-cg39-jmmj), [OSV](https://osv.dev/vulnerability/GHSA-7r86-cg39-jmmj) |
| GHSA-23c5-xmqv-rm74 / CVE-2026-27904 | High | Nested `*()` extglobs could still generate catastrophically backtracking regular expressions, extending the 2026 ReDoS fix train one patch release further on several major lines. | 3.1.4; 4.2.5; 5.1.8; 6.2.2; 7.4.8; 8.0.6; 9.0.7; 10.2.3 | [GitHub repository advisory](https://github.com/isaacs/minimatch/security/advisories/GHSA-23c5-xmqv-rm74), [OSV](https://osv.dev/vulnerability/GHSA-23c5-xmqv-rm74) |

## Security Posture Notes

- The public advisory history is unusually consistent: every published record in this review is a ReDoS finding, not a scattered mix of unrelated bug classes.
- The attack surface is pattern processing itself — public advisories repeatedly point to glob, extglob, and `GLOBSTAR` matching logic as the source of catastrophic or combinatorial backtracking.
- The upstream changelog's 3.x note "Added basic redos protection" is helpful context, but later public records show that the package still required more rounds of hardening after that initial mitigation.
- The 2026 advisory cluster required coordinated patch releases across many major lines, which suggests two things from public evidence alone: minimatch has a fragmented downstream version footprint, and maintainers considered the fixes important enough to backport broadly.
- The 2026 sequence also looks like an incomplete-fix chain from public records: `CVE-2026-26996` landed first, `CVE-2026-27903` followed with broader `GLOBSTAR` backtracking coverage, and `CVE-2026-27904` extended the fix train again for nested `*()` extglobs.
- This package's ecosystem blast radius is large because it is a foundational transitive dependency rather than a niche application library; the npm downloads snapshot gathered in this pass was about 108M per week.
- Public repository advisories and fix references are available for the newer issues, which is better disclosure posture than many small ecosystem utilities.
- npm registry metadata in this review showed `latest=10.2.5`, which is newer than the 10.x patched versions listed in the 2026 advisories and therefore clears the currently mapped public record for that major line.

## Recommendations for Developers

1. **Upgrade to a patched release in your current major line** at minimum: `3.1.4`, `4.2.5`, `5.1.8`, `6.2.2`, `7.4.8`, `8.0.6`, `9.0.7`, or `10.2.3`+ depending on the branch you consume.
2. **Avoid feeding untrusted user input into glob-pattern APIs**. The public record here is entirely about crafted-pattern complexity, so treat the pattern itself as a sensitive input surface.
3. **Prefer the newest maintained major line when possible**, not just the oldest patched point release, because the advisory history shows repeated follow-on hardening rather than a one-and-done fix.
4. **Audit transitive consumers**, not only direct dependencies, since minimatch often enters applications indirectly through build tools, packaging tools, and file-matching utilities.
5. **Keep dependency scanning enabled** for this package family because repeated ReDoS disclosures are a clear public trend rather than an isolated historical event.

## Dependencies of Note

- `minimatch` is often consumed transitively by build, packaging, and file-walking tooling, which raises its practical blast radius well above what a small utility library might suggest.
- Public evidence in this pass points to regex generation and match evaluation as the core sensitive surface, not to network-facing behavior or parser deserialization.

## Open Questions

- Has upstream published any broader guidance on safe use of complex or user-influenced glob patterns beyond the advisory text and fix commits?
- Which high-download downstream packages still pin pre-2026 patch lines in practice?
- Would future public research show additional distinct pattern families beyond repeated wildcards, multiple `GLOBSTAR` segments, and nested `*()` extglobs?

## Related Pages

- [[npm/micromatch]]
- [[npm/glob-parent]]
- [[npm/braces]]
- [[npm/path-to-regexp]]
- [[npm/index]]

---
*Last updated: 2026-04-23 | Sources: 10 (OSV.dev package query for npm/minimatch, 5 public GitHub Advisory Database / repository advisory records for the published GHSA/CVE set, upstream changelog, GitHub releases API, npm registry metadata, npm downloads API)*
