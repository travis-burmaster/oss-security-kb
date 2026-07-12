# nix (crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~17M/week est. (as of 2026-07-12)
**Repository:** https://github.com/nix-rust/nix
**Security Contact:** none listed (GitHub private security advisory mechanism)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-45707 / RUSTSEC-2021-0119 / GHSA-76w9-p8mg-j927 | Moderate (CVSS 3.1 6.7 — AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) | Out-of-bounds write in `nix::unistd::getgrouplist`: when a user has more than 16 group memberships on Linux, FreeBSD, Android, NetBSD, DragonFly BSD, OpenBSD, or Fuchsia, the function calls libc `getgrouplist` with a length parameter larger than the buffer it provides. On glibc and Solaris libc, `getgrouplist` writes the actual group count back to the `ngroups` parameter on overflow; nix 0.16.0–0.22.1 doubles the buffer size but does not read this updated value, so the next call writes past the end of the heap buffer — memory corruption. Exploitation requires write access to `/etc/group`, which is normally root-only. Versions < 0.16.0 are unaffected. | 0.20.2, 0.21.2, 0.22.2, or ≥ 0.23.0; unaffected: < 0.16.0 | [RUSTSEC-2021-0119](https://rustsec.org/advisories/RUSTSEC-2021-0119.html); [GHSA-76w9-p8mg-j927](https://github.com/advisories/GHSA-76w9-p8mg-j927) |

## Security Posture Notes

`nix` provides idiomatic Rust bindings to POSIX and *nix system calls, covering process management (`fork`, `exec`, `waitpid`), file descriptors, Unix sockets, terminal I/O (`ioctl`, `tcgetattr`), signal handling, and user/group management (`getgroups`, `getgrouplist`, `getpwnam`). It is a foundational Unix-API layer used by terminal emulators, container runtimes, shell implementations, and CLI system-administration tooling.

The `getgrouplist` advisory (RUSTSEC-2021-0119, published 2021-09-27) affects nix 0.16.0 through the affected ranges on Linux, FreeBSD, Android, NetBSD, DragonFly BSD, OpenBSD, and Fuchsia. The Windows build is not affected (POSIX group APIs do not apply). Severity is Moderate because exploitation requires a privileged write to `/etc/group`.

The fix was released across three actively maintained minor branches simultaneously (0.20.2, 0.21.2, 0.22.2), and all 0.23.0+ versions include the fix. Downstream crates that pin to older `nix` minor lines should upgrade.

Current stable: **0.31.3** (released 2026-05). The crate is actively maintained under the [nix-rust](https://github.com/nix-rust) organization. No formal SECURITY.md or dedicated security email is published; the project uses GitHub's private security advisory mechanism.

**Total crates.io downloads:** ~660M (as of 2026-07-12).

## Dependencies of Note

- Depends on the `libc` crate — the C API boundary is the primary source of soundness risk for this crate.

## Open Questions

- Audit the broader `unsafe` surface in `nix::unistd` and other modules wrapping libc user/group APIs for similar `ngroups`-style accounting bugs.
- Monitor for new advisories as nix adds coverage for newer POSIX features and Linux-specific kernel APIs.

## Related Pages

- [[rust/tokio]]
- [[rust/index]]

---
*Last updated: 2026-07-12 | Sources: 2*
