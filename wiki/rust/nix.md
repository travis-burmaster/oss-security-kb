# nix (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~12.1M/week est. (as of 2026-08-07; ~157.9M 90-day downloads, ~710M total)
**Repository:** https://github.com/nix-rust/nix
**Security Contact:** none listed (no SECURITY.md confirmed in this pass)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Notes |
|------|---------|-------|-------|
| 2026-08-07 | nightly-bot | RustSec + GHSA advisory search | 1 advisory mapped; OSV.dev blocked; sourced from rustsec/advisory-db and github/advisory-database |

## Known Vulnerabilities

| ID | Severity | CVSS | Description | Affected Versions | Fixed In | Primary Source |
|----|----------|------|-------------|-------------------|----------|----------------|
| CVE-2021-45707 / RUSTSEC-2021-0119 / GHSA-76w9-p8mg-j927 / GHSA-wgrg-5h56-jg27 | High | — | Heap buffer overflow in `nix::unistd::getgrouplist` when a user belongs to more than 16 groups; affects Linux, FreeBSD, Android, NetBSD, DragonFly, OpenBSD, and Fuchsia; macOS is NOT affected; versions < 0.16.0 are NOT affected (code path absent) | 0.16.0–0.22.x (unpatched lines: 0.20.0–0.20.1, 0.21.0–0.21.1, 0.22.0–0.22.1) | ≥ 0.20.2, ≥ 0.21.2, ≥ 0.22.2, ≥ 0.23.0 | [RUSTSEC-2021-0119](https://rustsec.org/advisories/RUSTSEC-2021-0119.html) |

## Security Posture Notes

`nix` provides Rust-idiomatic bindings to POSIX and Unix system calls (file I/O, process management, sockets, user/group management, signals, terminals, and more). It is one of the highest-download Rust crates outside the async runtime ecosystem, with ~12.1M weekly downloads and transitive usage across daemons, network services, container tooling, and embedded systems software.

**RUSTSEC-2021-0119 — `getgrouplist` heap overflow:** The C `getgrouplist(3)` function has a well-known hazard: it signals buffer truncation but may still overflow a too-small buffer on some platforms. Pre-fix versions of `nix` allocated space for 16 groups and called `getgrouplist` without handling the truncation case, producing a heap buffer overflow when a user belongs to more than 16 groups. The overflow corrupts heap memory adjacent to the groups array. Exploitability depends on context — a local user with more than 16 group memberships who can trigger the call path could potentially influence control flow.

**Platform scope:** Only Linux, FreeBSD, Android, NetBSD, DragonFly, OpenBSD, and Fuchsia are affected. macOS uses a different underlying implementation and is explicitly not affected. Versions < 0.16.0 predate the affected code path and are also unaffected.

**Patch distribution:** Three parallel stable-branch patches (0.20.2, 0.21.2, 0.22.2) were released simultaneously; all releases ≥ 0.23.0 incorporate the fix.

No formal disclosure policy or security contact is documented. Future advisories are likely to surface via the RustSec advisory database and GitHub's private vulnerability reporting interface.

## Dependencies of Note

- `libc` — low-level C FFI bindings; nix wraps `libc` for POSIX syscall access

## Open Questions

- No additional RUSTSEC or GHSA advisories found beyond RUSTSEC-2021-0119 in this pass. Given the crate's large surface area and ~12.1M weekly downloads, future re-checks are warranted.

## Related Pages

- [[rust/tokio]]
- [[rust/actix-web]]
