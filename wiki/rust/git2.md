# git2 (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~15.9M (as of 2026-09-25)
**Repository:** https://github.com/rust-lang/git2-rs
**Security Contact:** security@rust-lang.org (Rust Security Response WG)
**Disclosure Policy:** https://www.rust-lang.org/policies/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2023-0002 (**withdrawn**) | — (Informational) | SSH host key validation suppressed by default: the libgit2 C callback always ignores the `is_valid` argument and returns 0, treating unverified SSH host keys as valid; enables MitM delivery of malicious git objects / information disclosure. Related to CVE-2022-46176 (Cargo). Advisory published 2023-01-12 and **withdrawn 2023-01-13** from RustSec DB; underlying issue was fixed in 0.16.0. | 0.16.0 | [RUSTSEC-2023-0002](https://rustsec.org/advisories/RUSTSEC-2023-0002.html) |
| RUSTSEC-2026-0008 / GHSA-j39j-6gw9-jw6h | Informational / unsound | `Buf::new()` and `Buf::default()` pass a null pointer to `slice::from_raw_parts`, violating the requirement that the data pointer be non-null even for zero-length slices; constitutes undefined behavior accessible from safe code | 0.20.4 | [RUSTSEC-2026-0008](https://rustsec.org/advisories/RUSTSEC-2026-0008.html) |
| RUSTSEC-2026-0183 | Informational / unsound | `Remote::list()` passes a null pointer to `slice::from_raw_parts` when the remote advertises no references; undefined behavior in safe code | 0.21.0 | [RUSTSEC-2026-0183](https://rustsec.org/advisories/RUSTSEC-2026-0183.html) |
| RUSTSEC-2026-0184 | Informational / unsound | `Blame::blame_buffer()` constructs `Signature` objects from null pointers when author/committer data is unavailable in buffer-blame results; null-pointer dereference (UB) on access to the resulting Signature | 0.21.0 | [RUSTSEC-2026-0184](https://rustsec.org/advisories/RUSTSEC-2026-0184.html) |

*OSV: https://osv.dev/list?ecosystem=crates.io&q=git2*

## Security Posture Notes

`git2` provides safe Rust bindings to libgit2 (the C library used by Cargo, GitHub Desktop, and many other Git toolchain components). It is maintained under the `rust-lang` GitHub organization and is a direct transitive dependency of Cargo (the Rust package manager), giving it a very wide blast radius.

The 2026 advisory cluster (RUSTSEC-2026-0008/0183/0184) follows a recurring unsoundness pattern in Rust–C FFI bindings: libgit2 returns null pointers for empty or unavailable data, and the Rust wrapper passes these directly to `slice::from_raw_parts` without the non-null check that Rust's safety model requires. None of the three carry assigned CVEs or public exploit proofs; all are classified informational/unsound. All three were remediated in 0.20.4 (Buf) and 0.21.0 (Remote::list, Blame::blame_buffer). Current stable is 0.21.0 (May 2026).

The withdrawn 2023 advisory (RUSTSEC-2023-0002) described a behaviorally distinct issue: the SSH host-key-validation callback unconditionally accepted all server keys, enabling man-in-the-middle attacks over SSH. The fix (0.16.0) made the callback respect libgit2's validity judgment. The advisory was withdrawn the day after publication; the most likely explanation is that the primary advisory and CVE assignment (CVE-2022-46176) was assigned to Cargo rather than git2 directly. The underlying fix is present in 0.16.0 regardless of advisory status.

Security issues may be directed to the `rust-lang/git2-rs` GitHub repository or to the Rust Security Response WG at security@rust-lang.org per the upstream disclosure policy.

## Dependencies of Note

- `libgit2-sys` — low-level C bindings and bundled libgit2 source; carries its own upstream CVE exposure (e.g., CVE-2024-24577 heap overflow in libgit2 < 1.6.5). The bundled libgit2 version in libgit2-sys tracks upstream releases; check the libgit2-sys changelog for the bundled libgit2 version when auditing.
- `openssl` / `openssl-sys` (optional, TLS backend) — see [[rust/openssl]].

## Open Questions

- Does the bundled libgit2 in the latest `libgit2-sys` carry any unpatched upstream CVEs (e.g., post-1.8.x advisories)?
- Is CVE-2022-46176 (Cargo SSH host key bypass) fully addressed in all Cargo versions that bundle git2 ≥ 0.16.0?

## Related Pages

- [[go/github.com/go-git/go-git]]
- [[rust/index]]

---
*Last updated: 2026-09-25 | Sources: 4*
