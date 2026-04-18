# yargs-parser (npm)

**Registry:** npm
**Weekly Downloads:** ~176,636,757 (last week, fetched 2026-04-18)
**Repository:** https://github.com/yargs/yargs-parser
**Security Contact:** none listed
**Disclosure Policy:** GitHub Security Advisories / repository maintenance channels
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-17 | OpenClaw recurring review | package advisory curation | public-source curation (GitHub Advisory Database, OSV.dev, public CVE aliases, upstream changelog / fix commits, npm registry metadata, npm downloads API) | 1 published package advisory mapped; public fix metadata shows coordinated remediation across multiple maintained major lines | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-7608 / GHSA-p9pc-299p-vxgp | Moderate | Parsing attacker-controlled arguments such as `--foo.__proto__.bar baz` could modify `Object.prototype`, creating a prototype-pollution condition that affects downstream objects created afterward. | 5.0.1 / 13.1.2 / 15.0.1 / 18.1.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-p9pc-299p-vxgp), [OSV](https://osv.dev/vulnerability/GHSA-p9pc-299p-vxgp) |

## Security Posture Notes

- `yargs-parser` is the argument-parsing engine behind the widely used `yargs` CLI ecosystem, so even a single published vulnerability has outsized transitive reach.
- Public advisory data currently shows **one published package-level record** for the package: `CVE-2020-7608` / `GHSA-p9pc-299p-vxgp`.
- GitHub Advisory Database and OSV both show the same unusual remediation shape: multiple concurrently maintained major lines were fixed separately at `5.0.1`, `13.1.2`, `15.0.1`, and `18.1.1`.
- Upstream changelog text for `18.1.1` explicitly says `__proto__` will be rewritten to `___proto___` during parse, patching a potential prototype-pollution vulnerability; the corresponding public commit metadata matches that explanation.
- Practical risk depends on where the parsed object flows next. A CLI that only reads booleans and strings locally is lower risk than frameworks or wrappers that merge parser output into broader configuration or runtime objects.
- Current npm metadata shows the latest release is `22.0.0`, well past the publicly documented fixed versions.

## Recommendations for Developers

1. **Upgrade to the fixed release for your active major line**: `5.0.1`, `13.1.2`, `15.0.1`, `18.1.1`, or any newer maintained release.
2. **Avoid merging parsed argv output into privileged configuration objects** without key sanitization, even after upgrading.
3. **Audit transitive CLI dependencies**, because `yargs-parser` often arrives via larger toolchains rather than by explicit direct use.

## Dependencies of Note

- Commonly inherited via `yargs` and downstream CLI frameworks, scaffolding tools, and developer tooling.
- The package's public vulnerability history is small, but its ecosystem blast radius is large.

## Open Questions

- Which still-supported enterprise or distro-packaged CLI stacks continue to pin pre-fix `13.x`, `15.x`, or `18.x` branches?
- Are there public maintainer notes beyond changelog / advisory text that document any compatibility issues from rewriting `__proto__` keys?

## Related Pages

- [[npm/minimist]]
- [[npm/semver]]
- [[npm/cross-spawn]]
- [[npm/index]]

---
*Last updated: 2026-04-17 | Sources: 6 (GitHub Advisory Database JSON / GHSA page, OSV.dev package query, public CVE alias, upstream CHANGELOG.md, upstream fix commit metadata, npm registry metadata, npm downloads API)*
