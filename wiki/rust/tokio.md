# tokio (rust)

**Registry:** crates.io
**Weekly Downloads:** unknown (as of 2026-04-13)
**Repository:** https://github.com/tokio-rs/tokio
**Security Contact:** mailto:security@tokio.rs
**Disclosure Policy:** https://github.com/tokio-rs/tokio/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-13 | OpenClaw recurring review | crate advisory history | manual | 5 publicly disclosed crate advisories / RustSec entries curated from OSV, RustSec, CVE / GHSA aliases, Tokio security-policy text, and public fix / release references | https://osv.dev/list?ecosystem=crates.io&q=tokio |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-38191 / GHSA-2grh-hm3w-w7hv / RUSTSEC-2021-0072 | High | `JoinHandle::abort` could drop a `LocalSet` task on the wrong thread, creating a race condition and possible memory-safety breakage in code using thread-local-only state such as `Rc` or `RefCell`. | 1.5.1 / 1.6.3 / 1.7.2 / 1.8.1 | https://rustsec.org/advisories/RUSTSEC-2021-0072.html |
| CVE-2021-45710 / GHSA-fg7r-2g4j-5cgr / RUSTSEC-2021-0124 | High | Closing a `tokio::sync::oneshot` receiver and then racing send / receive operations could trigger a data race with observed memory corruption in affected code paths. | 1.8.4 / 1.13.1 | https://rustsec.org/advisories/RUSTSEC-2021-0124.html |
| CVE-2023-22466 / GHSA-7rrj-xr53-82p7 / RUSTSEC-2023-0001 | Moderate | On Windows named-pipe servers, calling `pipe_mode` could silently disable `reject_remote_clients`, weakening an intended local-only boundary unless callers set the options in the safe order. | 1.18.4 / 1.20.3 / 1.23.1 | https://rustsec.org/advisories/RUSTSEC-2023-0001.html |
| GHSA-4q83-7cq4-p6wg / RUSTSEC-2023-0005 | Moderate | `tokio::io::ReadHalf<T>::unsplit` was unsound and could violate the `Pin` contract under uncommon but real `!Unpin` / `io-util` usage, so this is best treated as a memory-safety break rather than a generic remote exploit claim. | 1.18.5 / 1.20.4 / 1.24.2 | https://rustsec.org/advisories/RUSTSEC-2023-0005.html |
| GHSA-rr8g-9fpq-6wmg / RUSTSEC-2025-0023 | Moderate | Tokio's broadcast channel could call `Clone` in parallel while requiring only `Send`, creating unsoundness for values whose `Clone` behavior depends on the value also being `Sync`. | 1.38.2 / 1.42.1 / 1.43.1 / 1.44.2 | https://rustsec.org/advisories/RUSTSEC-2025-0023.html |

*Full advisory history (OSV): https://osv.dev/list?ecosystem=crates.io&q=tokio*

## Security Posture Notes

- Tokio has a relatively mature disclosure process for a foundational Rust crate: the public security policy routes reports to `security@tokio.rs`, discourages public issue filing for undisclosed problems, and says disclosures are coordinated through GitHub advisories, RustSec, and release notes.
- The published advisory history clusters around **memory-safety / unsoundness bugs** plus one **configuration-boundary failure** on Windows named pipes. That is a recognizable risk profile for a performance-sensitive async runtime with deep concurrency and I/O internals.
- Several advisories are highly conditional rather than universally exploitable. The KB should be careful not to overstate them as generic remote-code-execution bugs; the public records support framing them as memory-safety, thread-safety, or configuration-integrity failures with exploitability shaped by calling patterns and enabled features.
- Tokio appears willing to backport security fixes across multiple maintained lines. The public `tokio-1.8.4` release notes explicitly call out the backport for `RUSTSEC-2021-0124`, which is a useful operational signal for downstream users pinned to older 1.x branches.
- The Windows named-pipe issue (`RUSTSEC-2023-0001`) stands out because it is not an abstract soundness concern: it can directly weaken a trust boundary if applications rely on Tokio defaults or set `ServerOptions` in the wrong order.
- Even when a Tokio flaw is narrow, downstream blast radius can be large because Tokio underpins a substantial share of the Rust async ecosystem; that makes clear version / branch guidance especially valuable in a KB page.

## Dependencies of Note

- The Rust async stack around `mio`, `bytes`, `hyper`, `tower`, `axum`, and `tonic` is the natural next review cluster because many production services inherit Tokio behavior through those libraries rather than depending on Tokio directly.
- Windows named-pipe consumers deserve separate attention because `RUSTSEC-2023-0001` depends on OS-specific behavior and application configuration order, not just crate version.
- The `io-util` and channel APIs are notable because multiple public Tokio advisories concentrate in those surfaces rather than in scheduler basics alone.

## Open Questions

- Are there public independent audit reports for Tokio beyond the advisory trail itself, or is the current public record mostly maintainer-driven disclosure and patch work?
- Which downstream Rust framework pages should explicitly cross-link Tokio once more async ecosystem coverage exists, so inherited runtime risk is easier to follow?
- Is there a public maintainer writeup explaining supported-branch security backport policy in more detail than the current release notes and security-policy text?

## Related Pages

- [[rust/serde]]
- [[rust/index]]

---
*Last updated: 2026-04-13 | Sources: 5 (OSV package query, five RustSec advisory pages, CVE / GHSA aliases via OSV and RustSec, Tokio security policy, public Tokio release notes)*
