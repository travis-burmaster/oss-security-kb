# tar (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~3.3M/week est. (43.4M 90-day; as of 2026-07-25)
**Repository:** https://github.com/alexcrichton/tar-rs
**Security Contact:** none listed (no SECURITY.md; advisories reported via RustSec advisory-db)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-07-25 | OSS Security KB (nightly pass) | public advisory database mapping | automated lookup (RustSec advisory-db) | 4 advisory records mapped | [rustsec/advisory-db](https://github.com/rustsec/advisory-db/tree/main/crates/tar) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2018-0002 / CVE-2018-20990 | High (CVSS:3.0 AV:N/AC:L/PR:N I:H) | `unpack_in` allows hard links and symlinks in archives to escape the extraction directory and overwrite arbitrary files. Discovered by Max Justicz. | ≥ 0.4.16 | [GHSA-2367-c296-3mp2](https://github.com/advisories/GHSA-2367-c296-3mp2) |
| RUSTSEC-2021-0080 / CVE-2021-38511 | High (CVSS:3.1 AV:N/AC:L/PR:N I:H) | `Archive::unpack` can create directories outside the intended extraction root when processing symlinks; intermediate directories are created before the final error is raised, leaving attacker-controlled paths on the filesystem. Discovered by Martin Michaelis and Nikhil Benesch. | ≥ 0.4.36 | [GHSA-62jx-8vmh-4mcw](https://github.com/advisories/GHSA-62jx-8vmh-4mcw) |
| RUSTSEC-2026-0067 / CVE-2026-33056 | Moderate (CVSS:4.0 AV:N/AC:L VI:L) | Symlink-following enables `chmod` on arbitrary directories during extraction: `unpack_dir` calls `fs::metadata()` which follows symlinks, so a malicious tarball can pair a symlink entry with a same-named directory entry and cause the extractor to apply `chmod` to the symlink target outside the extraction root. Affects `Entry::unpack` and `Entry::unpack_in`. | ≥ 0.4.45 | [GHSA-j4xf-2g29-59ph](https://github.com/advisories/GHSA-j4xf-2g29-59ph) |
| RUSTSEC-2026-0068 / CVE-2026-33055 | Moderate (CVSS:4.0 AV:N/AC:L VC:L/VI:L) | Inconsistent PAX size header handling: tar-rs skips the PAX `size` header override when the base header size is nonzero, diverging from other tar parsers (e.g., Go's `archive/tar`, GNU tar) that apply PAX overrides unconditionally. This mismatch enables archive-manipulation / polyglot attacks where different parsers interpret the same archive differently, creating a potential security boundary bypass when tar-rs sits downstream of a trusted parser. | ≥ 0.4.45 | [GHSA-gchp-q4r4-x4ff](https://github.com/advisories/GHSA-gchp-q4r4-x4ff) |

## Security Posture Notes

The `tar` crate (tar-rs) is the dominant Rust library for reading and writing POSIX tar archives, with ~3.3M downloads per week and ~197M total crates.io downloads. It is widely used as a dependency in build tools, package managers, backup utilities, and CI infrastructure.

**Vulnerability pattern:** All four published advisories involve archive extraction boundary failures — hard link/symlink escape (2018), symlink-induced directory creation outside root (2021), symlink-following `chmod` (2026), and PAX header inconsistency (2026). The recurring root cause is the inherent complexity of the POSIX tar format: multiple header extension mechanisms (PAX, GNU, v7), link types (hard, soft), and permission operations interact across the extraction pipeline in ways that require careful, defense-in-depth validation.

The two 2026 advisories (RUSTSEC-2026-0067 and RUSTSEC-2026-0068) were both published 2026-03-19 and both fixed in **0.4.45**. The current release **0.4.46** is patched for all four known advisories.

No SECURITY.md or formal disclosure policy is documented in the repository. Responsible disclosure appears to have occurred informally through the RustSec advisory-db PR process for all four advisories.

The crate is maintained by Alex Crichton; commit activity is periodic rather than continuous. Embedding applications that extract untrusted archives should validate that they are on ≥ 0.4.45 and should consider applying application-level extraction allowlists (e.g., checking all extracted paths before applying to disk).

## Dependencies of Note

None flagged (the `tar` crate has minimal dependencies; it depends only on `filetime` and `xattr`).

## Open Questions

- Determine whether the PAX size header inconsistency (RUSTSEC-2026-0068 / CVE-2026-33055) is exploitable in common downstream callers (e.g., `cargo`, `flate2`-based extractors) — the GHSA characterizes it as a boundary-confusion risk but does not provide a concrete exploit chain.
- Assess whether the no-SECURITY.md gap warrants a stub note or outreach given the crate's download volume.
- Monitor whether 0.4.47+ introduces additional extraction hardening (e.g., symlink-following mitigations beyond the 0.4.45 patch).

## Related Pages

- [[rust/index]]
- [[npm/tar]]
- [[npm/tar-fs]]
- [[linux/tar]]

---
*Last updated: 2026-07-25 | Sources: rustsec/advisory-db (4 advisories mapped), crates.io metadata*
