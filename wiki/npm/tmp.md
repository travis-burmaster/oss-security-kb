# tmp (npm)

**Registry:** npm
**Weekly Downloads:** ~61,683,987 (2026-04-13 to 2026-04-19)
**Repository:** https://github.com/raszi/node-tmp
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/raszi/node-tmp/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-20 | OpenClaw recurring review | package advisory normalization | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream issue / fix-commit references, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for tmp's currently published package-scoped vulnerability history. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-54798 / GHSA-52f5-9888-hmc6 | Low | A symlink in the `dir` parameter could bypass the package's intended temp-directory boundary checks, allowing temporary file or directory creation outside the expected `tmpDir` scope. Public advisory text ties the bug to symlink resolution in `_resolvePath()` and points to a fix commit that resolves the real path before validation. | 0.2.4 | https://github.com/advisories/GHSA-52f5-9888-hmc6 |

## Security Posture Notes

- `tmp` has a **small published package-level advisory history** in this review window: one low-severity but real path-boundary issue affecting the `dir` option.
- The advisory is low severity in GitHub's reviewed record, but the bug class still matters because callers often treat temporary-directory helpers as security-relevant primitives rather than convenience utilities.
- Public evidence ties the flaw specifically to **symlink handling**: checks intended to keep `dir` under the system temp directory could be bypassed when a relative path inside the temp tree actually resolved somewhere else.
- Current npm metadata shows the package still has substantial ecosystem reach (~61.7M downloads in the review week), so even a low-severity temp-path bug is worth curating for downstream users.
- This package sits in the same general risk family as archive extractors and file-upload helpers: path resolution, symlinks, and filesystem trust-boundary assumptions deserve extra scrutiny.

## Recommendations for Developers

1. **Upgrade to `0.2.4` or newer** to pick up the published symlink-handling fix.
2. Treat the `dir` option as a **filesystem trust boundary**, especially if any portion of it can be influenced by user input, configuration files, or writable directories shared with less-trusted code.
3. On systems with shared temp areas or attacker-writable intermediate paths, add regression tests that exercise symlinked directories rather than testing only direct real paths.
4. Prefer defense in depth: use restrictive filesystem permissions and avoid mixing sensitive temporary-file creation with directories writable by other principals.

## Dependencies of Note

- `tmp` is frequently used as a helper in CLI tools, installers, build systems, and file-processing pipelines where the temporary directory path may be assumed safe by higher layers.
- Filesystem path canonicalization and symlink behavior are the key security-relevant surfaces in the currently published advisory trail.

## Open Questions

- Are there other public issue threads or release notes that clarify whether `0.2.4` fully closes related path-resolution edge cases beyond the one published advisory gathered here?
- Which high-download packages in the npm ecosystem still transitively pin `tmp` below `0.2.4`?
- Would a future KB pass benefit from a cross-package note comparing `tmp`, archive extractors, and upload middleware on symlink / path-boundary failure modes?

## Related Pages

- [[npm/tar]]
- [[npm/multer]]
- [[npm/index]]

---
*Last updated: 2026-04-20 | Sources: 6 (OSV.dev package query for npm/tmp, OSV vulnerability record for GHSA-52f5-9888-hmc6, GitHub Advisory Database entry for the same GHSA ID, public CVE record via advisory alias, upstream issue / fix-commit references linked from the advisory record, npm registry metadata, npm downloads API)*
