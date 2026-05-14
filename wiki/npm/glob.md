# glob (npm)

**Registry:** npm
**Weekly Downloads:** ~355,376,006 (2026-05-06 to 2026-05-12)
**Current Version:** 13.0.6 (as of 2026-05-13)
**Repository:** https://github.com/isaacs/node-glob
**Security Contact:** https://github.com/isaacs/node-glob/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-13 | OpenClaw recurring review | public advisory review | OSV / GHSA / CVE / upstream security advisory and fix commits / npm registry and downloads metadata | 1 public package-scoped advisory for CLI command injection through `-c` / `--cmd` filename handling | https://osv.dev/list?ecosystem=npm&q=glob |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-64756 / GHSA-5j98-mcp5-4vw2 | High | The `glob` CLI `-c` / `--cmd` option executed a supplied command with `shell: true` and passed matched filenames as arguments, allowing shell metacharacters in malicious filenames to trigger command injection under the invoking user or CI account. | 10.5.0 / 11.1.0 | https://osv.dev/vulnerability/GHSA-5j98-mcp5-4vw2 |

## Security Posture Notes

- The confirmed public record is scoped to the CLI command-execution feature, not ordinary library glob expansion by itself.
- The risk is most relevant in automation or developer tooling that runs `glob -c` over attacker-controlled worktrees, archives, or generated filenames.
- `glob` has a very high npm transitive footprint, but this page avoids treating dependency presence alone as evidence of exploitability for the CLI-specific advisory.

## Dependencies of Note

- Shell invocation semantics and filename trust are the key boundary for the published advisory.
- Related globbing packages such as `minimatch`, `glob-parent`, and `brace-expansion` have separate pages because their public advisory histories are package-scoped to those libraries.

## Open Questions

- Should future KB guidance distinguish packages whose advisories apply only to optional CLI surfaces from packages whose library API is directly affected?

## Related Pages

- [[npm/minimatch]]
- [[npm/glob-parent]]
- [[npm/brace-expansion]]
- [[npm/index]]

---
*Last updated: 2026-05-13 | Sources: 6 (OSV package query + OSV vulnerability record; GitHub Advisory Database / upstream GitHub security advisory; public CVE/NVD record; upstream fix commits; npm registry metadata; npm downloads API; local proxy synthesis used only as drafting aid)*
