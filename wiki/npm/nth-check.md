# nth-check (npm)

**Registry:** npm
**Weekly Downloads:** ~52,234,671 (2026-04-14 to 2026-04-20)
**Repository:** https://github.com/fb55/nth-check
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-22 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public upstream fix-commit references, npm registry metadata, npm downloads API, local Claude-compatible proxy used only as a drafting aid) | Added a new advisory-mapped page for `nth-check` covering its single currently published npm package advisory: the pre-`2.0.1` regex-complexity denial-of-service issue tracked as `GHSA-rp65-9cf3-cjxr` / `CVE-2021-3803`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-rp65-9cf3-cjxr / CVE-2021-3803 | High | Public GHSA / OSV records describe inefficient regular-expression complexity in `nth-check`, allowing crafted invalid CSS nth expressions to trigger denial-of-service behavior during parsing before `2.0.1`. | 2.0.1 | https://github.com/advisories/GHSA-rp65-9cf3-cjxr |

## Security Posture Notes

- `nth-check` has a **small currently published package-advisory footprint** in this pass: one ReDoS-style parser issue rather than a long advisory chain.
- The upstream remediation trail is crisp and easy to verify publicly: fix commit `9894c1d` explicitly says `fix(parse): Replace regex with hand-rolled parser (#9)`, which matches the advisory's parser-complexity theme.
- This package's risk profile is shaped less by direct application use and more by **massive transitive reach** through HTML / CSS selector tooling (**~52.2M weekly downloads** in this review window).
- No repository-root `SECURITY.md` was confirmed in this pass, so the public disclosure path looks less formal than some similarly popular infrastructure packages.
- No additional package-scoped OSV records were surfaced for `nth-check` in this pass beyond `GHSA-rp65-9cf3-cjxr`.
- The vulnerability class matters because selector parsing often runs on semi-trusted or attacker-shaped content in scraping, sanitization, and transformation pipelines.

## Recommendations for Developers

1. **Upgrade to `2.0.1` or later** wherever `nth-check` still resolves below the fixed release.
2. **Audit transitive dependency trees** in HTML / CSS parsing stacks, because many applications inherit this package indirectly.
3. **Be cautious about regex-heavy parser helpers** exposed to untrusted selector-like input, especially in batch-processing or server-side parsing paths.

## Dependencies of Note

- Frequently lands transitively through selector and DOM-processing libraries rather than as a direct top-level dependency.
- Small parser utilities like this can become high-blast-radius risks because they sit underneath broader content-processing toolchains.

## Open Questions

- Which current high-download packages still pin `nth-check` below `2.0.1` transitively?
- Has the newer hand-rolled parser received any later public hardening review beyond the original fix commit?
- Should future KB work cross-link selector-parser packages that share ReDoS-sensitive parsing behavior?

## Related Pages

- [[npm/marked]]
- [[npm/markdown-it]]
- [[npm/index]]

---
*Last updated: 2026-04-22 | Sources: 6 (OSV.dev package query, OSV / GitHub Advisory Database record for GHSA-rp65-9cf3-cjxr, public fix commit fb55/nth-check@9894c1d, npm registry metadata, npm downloads API, public repository metadata / root contents check)*
