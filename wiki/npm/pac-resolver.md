# pac-resolver (npm)

**Registry:** npm
**Weekly Downloads:** ~25,000,000 (as of 2026-04-21)
**Repository:** https://github.com/TooTallNate/proxy-agents/tree/main/packages/pac-resolver
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-21 | [@travis-burmaster](https://github.com/travis-burmaster) | package advisory review | public-source curation (OSV.dev, public CVE record, upstream release notes, npm registry metadata) | 1 published package advisory mapped | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-9j49-mfvp-vmhm / CVE-2021-23406 | High | Unsafe PAC-file handling could lead to code injection when the package is used with untrusted PAC input. Public advisory text notes that the practical fix landed through the maintainer-controlled `degenerator` dependency used by `pac-resolver`. | 5.0.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-9j49-mfvp-vmhm) |

## Security Posture Notes

- Maintenance status: actively maintained; npm metadata shows recent publishes through `9.0.1` on 2026-04-06.
- Known sensitive surfaces: any workflow that compiles or executes attacker-controlled PAC content, plus the package's code-generation / sandbox boundary via `degenerator`.
- Disclosure maturity: no standalone `SECURITY.md` or separate disclosure-policy URL was confirmed in the public evidence gathered for this pass.
- Notes: the public release trail for the `5.0.0` security line says the main change was updating `degenerator` to use `vm2` under the hood for running untrusted code, matching the advisory's note that the effective fix lived in the dependency layer.
- Notes: current `9.0.1` metadata is well past the vulnerable `< 5.0.0` range, but this package remains high-value because of its large install base and its role in evaluating PAC logic.

## Dependencies of Note

- `degenerator` — directly called out by the published advisory as the dependency where the fix was applied.
- `netmask` — present in current dependency metadata; worth keeping in view because IP / network-classification helpers have had published security history elsewhere, even though no new `pac-resolver` package-level finding was added from that relationship in this pass.

## Open Questions

- What sandboxing / code-execution boundary does the current `degenerator` line use after the older `vm2`-based remediation path, and does that materially change residual risk for untrusted PAC content?
- Does the `proxy-agents` monorepo expose a GitHub private reporting channel or other disclosure route that was not surfaced in this quick public pass?
- Are there other publicly disclosed PAC-evaluation edge cases in adjacent packages (`pac-proxy-agent`, `proxy-agents`) that should be cross-linked in a broader review?

## Related Pages

- [[npm/index]]

---
*Last updated: 2026-04-21 | Sources: 5 (OSV.dev package query, GitHub Advisory Database, public CVE/NVD record for CVE-2021-23406, upstream `node-pac-proxy-agent` 5.0.0 release notes, npm registry / downloads metadata)*
