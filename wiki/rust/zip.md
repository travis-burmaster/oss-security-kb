# zip (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~5M/week est. (64M 90-day recent; as of 2026-08-28)
**Repository:** https://github.com/zip-rs/zip2
**Security Contact:** none listed (no formal SECURITY.md; advisories filed via RustSec advisory-db)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-08-28 | OSS Security KB (nightly pass) | public advisory database mapping | automated lookup (RustSec advisory-db + GHSA) | 1 advisory record mapped | [rustsec/advisory-db](https://github.com/rustsec/advisory-db/tree/main/crates/zip) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2025-0168 / GHSA-94vh-gphv-8pm8 / CVE-2025-29787 | Medium (CVSS:4.0) | Path traversal via symlinks during archive extraction. Symbolic links placed earlier in an archive can be exploited to write subsequent files to arbitrary filesystem locations outside the intended extraction directory, bypassing canonical-path checks in `ZipArchive::extract` and `ZipStreamReader::extract`. Affects zip 1.3.0–2.2.x; versions < 1.3.0 are unaffected. | ≥ 2.3.0 | [GHSA-94vh-gphv-8pm8](https://github.com/advisories/GHSA-94vh-gphv-8pm8) |

## Security Posture Notes

The `zip` crate (hosted at `zip-rs/zip2`) is the dominant Rust library for reading and writing ZIP archives, with ~250M all-time crates.io downloads and ~5M downloads per week. It is widely used in build tooling, package managers, backup utilities, and file-processing pipelines.

**Advisory pattern:** The single confirmed advisory (RUSTSEC-2025-0168, published 2026-03-16) follows a classic archive extraction symlink race pattern: a malicious archive places a symlink entry early, which the extractor resolves before validating that subsequent write destinations remain within the extraction root. Both affected extraction entry points (`ZipArchive::extract` and `ZipStreamReader::extract`) share the flaw. The root cause is symlink-following without post-extraction canonical-path enforcement.

**Affected versions:** 1.3.0 through 2.2.x only. Versions earlier than 1.3.0 are explicitly unaffected because the vulnerable extraction codepath was introduced in 1.3.0.

**Remediation:** Upgrade to zip ≥ 2.3.0. Applications that cannot upgrade should either refuse to extract untrusted ZIP archives or implement their own path-canonicalization and symlink-rejection logic before passing entries to extraction functions.

**Maintenance posture:** The crate is actively maintained under the `zip-rs` GitHub organization. No SECURITY.md is present; security disclosures appear to flow through the RustSec advisory-db PR process.

## Dependencies of Note

None flagged (the `zip` crate's dependency surface is minimal: `deflate64`, `zstd`, `flate2`, `bzip2`, and similar codec crates; none carry currently-active security advisories relevant to zip's use of them).

## Open Questions

- Confirm whether `zip_next` (RUSTSEC-2024-0337, a related but distinct crate) poses an upgrade-path confusion risk for projects that accidentally depend on both `zip` and `zip_next`.
- Monitor whether zip 2.3.x introduces additional hardening beyond the symlink-check fix (e.g., configurable max path depth, symlink disallow-by-default mode).
- Assess whether the lack of a SECURITY.md creates a reporting gap for future researchers and whether a responsible-disclosure pointer should be added to the crate metadata.

## Related Pages

- [[rust/tar]]
- [[rust/index]]
- [[npm/tar]]
- [[npm/tar-fs]]
- [[linux/tar]]

---
*Last updated: 2026-08-28 | Sources: rustsec/advisory-db (1 advisory mapped: RUSTSEC-2025-0168), GHSA-94vh-gphv-8pm8, crates.io metadata*
