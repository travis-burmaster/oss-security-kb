# yaml (npm)

**Registry:** npm
**Weekly Downloads:** ~142,006,684 (2026-04-14 to 2026-04-20)
**Repository:** https://github.com/eemeli/yaml
**Security Contact:** none clearly listed in this pass
**Disclosure Policy:** GitHub Security Advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-21 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / upstream GitHub security advisories, public CVE records, upstream release notes / fix commits, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for `yaml`'s published package security history, covering the 2023 degenerate-input exception fix and the 2026 deeply nested collection stack-overflow fix. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-2251 / GHSA-f9xv-q969-pqx4 | Moderate | Public advisory records describe an uncaught exception path affecting `yaml` from `2.0.0-5` up to but not including `2.2.2`. Upstream `v2.2.2` release notes say the patch release included a fix for an error thrown by `parseDocument` on degenerate input and explicitly reference the CVE. | 2.2.2 | https://github.com/advisories/GHSA-f9xv-q969-pqx4 |
| CVE-2026-33532 / GHSA-48c2-rrv3-qjmp | Moderate | Public advisory text says deeply nested YAML flow collections could trigger `RangeError: Maximum call stack size exceeded` during compose / resolve, and that the resulting exception is not a `YAMLParseError`. Upstream `v2.8.3` release notes tie the fix to catching stack overflow during node composition. | 2.8.3 | https://github.com/advisories/GHSA-48c2-rrv3-qjmp |

## Security Posture Notes

- `yaml` currently has a **small but meaningful public advisory history** centered on parser robustness and exception-handling behavior rather than on a long trail of code-execution or trust-boundary bugs.
- The 2023 and 2026 records are related in one important operational way: both involve **input shapes that can trigger unexpected parser failure modes**. One is framed as an uncaught exception on degenerate input, and the later one is more specific about a stack overflow during recursive node composition for deeply nested collections.
- The 2026 advisory deserves extra attention because the public advisory text explicitly notes that the thrown `RangeError` is **not** a `YAMLParseError`. That matters for applications whose error handling assumes all bad YAML will surface through YAML-specific exception types.
- Current npm metadata in this pass shows extremely high deployment volume (~142.0M downloads in the last review week), so even moderate parser-availability issues have broad downstream relevance through transitive build tooling, configuration loaders, and developer tooling.
- Public release notes line up cleanly with the advisory set gathered here: `v2.2.2` calls out the `parseDocument` / `CVE-2023-2251` fix, and `v2.8.3` calls out catching stack overflow during node composition. Current npm metadata in this pass showed `2.8.3` as latest, which also means the newest public fix point is the current release.

## Recommendations for Developers

1. **Upgrade to `2.8.3` or newer** if you want coverage for the full currently published package-advisory set reviewed in this pass.
2. **Treat YAML parsing as attacker-adjacent input handling** when configuration, manifests, or content can come from semi-trusted or untrusted sources.
3. **Do not assume only `YAMLParseError` needs to be caught**; the 2026 advisory explicitly documents a non-YAMLParseError `RangeError` failure mode on vulnerable versions.
4. **Apply input-size and nesting-depth limits where practical**, especially in services that parse user-supplied YAML synchronously inside request paths.
5. **Audit transitive usage too**, because `yaml` often arrives under build tools, configuration loaders, and ecosystem helpers rather than appearing only as a direct application dependency.

## Dependencies of Note

- Commonly used in configuration parsing, CI/CD tooling, frontend build systems, and content-processing pipelines.
- Risk increases where applications parse attacker-controlled or tenant-controlled YAML directly, or where parser failures can abort builds, requests, or background jobs.

## Open Questions

- Are there public maintainer notes or issue threads that explain real-world exploitability and expected exception-handling patterns for `CVE-2026-33532` beyond the advisory text and release note?
- Should the KB eventually add a small parser-hardening cluster linking `yaml`, `js-yaml`, and `xml2js` around denial-of-service and error-surface handling?
- Which high-download downstream packages still pin `yaml` below `2.8.3` in practice?

## Related Pages

- [[npm/js-yaml]]
- [[npm/xml2js]]
- [[npm/postcss]]
- [[npm/index]]

---
*Last updated: 2026-04-21 | Sources: 8 (OSV.dev package query for npm/yaml, OSV vulnerability records for GHSA-f9xv-q969-pqx4 and GHSA-48c2-rrv3-qjmp, GitHub Advisory Database / upstream GitHub security advisories, public CVE records, upstream release notes for v2.2.2 and v2.8.3, upstream fix commits, npm registry metadata, npm downloads API)*