# tar-fs (npm)

**Registry:** npm
**Weekly Downloads:** ~43,732,201 (2026-04-17 to 2026-04-23)
**Repository:** https://github.com/mafintosh/tar-fs
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/mafintosh/tar-fs/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-24 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / public GitHub security advisories, public CVE records, maintainer fix commits, npm registry metadata, npm downloads API) | Added a new advisory-mapped page for `tar-fs` after a clean review of its published package-level extraction-path vulnerability history across the 1.x, 2.x, and 3.x lines. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2018-20835 / GHSA-x2mc-8fgj-3wmr | High | A crafted tarball could use a hardlink to an existing file followed by a plain file with the same name, leading to arbitrary file overwrite during extraction on older `1.x` releases. | 1.16.2 | https://github.com/advisories/GHSA-x2mc-8fgj-3wmr |
| CVE-2024-12905 / GHSA-pq67-2wwv-3xjx | Critical | Public advisory records describe link-following and path-traversal behavior that can let a crafted archive write or overwrite files outside the intended extraction directory. | 1.16.4 / 2.1.2 / 3.0.7 | https://github.com/advisories/GHSA-pq67-2wwv-3xjx |
| CVE-2025-48387 / GHSA-8cj5-5rvv-wf4v | High | A specific crafted tarball could still escape the requested extraction directory; the public advisory notes a temporary workaround of ignoring non-file and non-directory entries until patched versions were installed. | 1.16.5 / 2.1.3 / 3.0.9 | https://github.com/advisories/GHSA-8cj5-5rvv-wf4v |
| CVE-2025-59343 / GHSA-vj76-c3g6-qr5v | High | Public advisory text says symlink validation could be bypassed when the destination directory was predictable, enabling another extraction-boundary escape with a crafted tarball. | 1.16.6 / 2.1.4 / 3.1.1 | https://github.com/advisories/GHSA-vj76-c3g6-qr5v |

## Security Posture Notes

- `tar-fs` shows a **clear recurring vulnerability pattern around archive extraction trust boundaries**: hardlinks, symlink handling, link following, and path traversal repeatedly reappear in its public advisory trail.
- The package's public history is notable for **serial follow-on fixes across maintained lines** rather than one isolated bug; the 2024-2025 cluster landed as successive repairs on `1.x`, `2.x`, and `3.x` rather than as a single one-and-done hardening release.
- Because `tar-fs` is still heavily used (~43.7M weekly npm downloads in this pass), these are not merely niche local-file bugs: they can propagate through CLIs, package managers, build pipelines, and other tooling that extracts attacker-controlled or semi-trusted archives.
- The strongest operational theme from the public evidence is that **archive extraction should be treated as a security boundary**, not just convenience I/O. Callers should be cautious about symlinks, hardlinks, and destination-path assumptions even when a package appears patched.
- Current npm metadata in this pass showed `3.1.2` as latest, which is beyond all currently published fixed versions gathered here. That is a good sign operationally, but the recent advisory cadence suggests downstream users should keep watching patch releases closely.

## Recommendations for Developers

1. **Upgrade to `3.1.1` or newer on the 3.x line**; prefer the current latest `3.1.2` unless compatibility constraints force an older maintained line.
2. If pinned to older branches, use at least **`2.1.4` on 2.x** or **`1.16.6` on 1.x** so the full currently published package-advisory set from this pass is covered.
3. Treat extraction of untrusted archives as a **filesystem trust-boundary operation**: isolate extraction directories, avoid running as a privileged user, and validate downstream handling of extracted paths.
4. Add regression tests for **symlink, hardlink, and nested path traversal cases** rather than only testing straightforward file and directory entries.
5. Consider defense in depth even on patched versions, especially in CI or automation contexts that unpack archives from less-trusted sources.

## Dependencies of Note

- `tar-fs` is commonly used in tooling and automation that pack or extract tar archives, so the package often matters transitively rather than only as a direct application dependency.
- Symlink and hardlink semantics are part of the real security surface here; archive processing code that assumes entry names alone define safety is at higher risk.
- Public advisories and downstream Debian LTS notices both show that these flaws matter beyond npm-only contexts.

## Open Questions

- Has the maintainer published a broader design note or hardening roadmap for extraction safety beyond the advisory-by-advisory fix commits?
- Which high-volume downstream packages still transitively pin `tar-fs` below `3.1.1` or below the fully patched branch tips on older lines?
- Would a future KB pass benefit from a cross-package comparison of `tar`, `tar-fs`, and similar archive extractors to make repeated symlink / traversal failure modes easier to spot?

## Related Pages

- [[npm/tar]]
- [[npm/tmp]]
- [[npm/multer]]
- [[npm/index]]

---
*Last updated: 2026-05-02 | Sources: 8 (OSV.dev package query for npm/tar-fs, OSV vulnerability records for the four GHSA entries, GitHub Advisory Database / public GitHub security advisories, public CVE / NVD records, maintainer fix commits, Debian LTS advisories, npm registry metadata, npm downloads API)*
