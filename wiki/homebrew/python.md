# python (Homebrew)

**Registry:** Homebrew
**Weekly Downloads:** unknown (formulae.brew.sh blocked in this pass)
**Repository:** https://github.com/Homebrew/homebrew-core/blob/master/Formula/p/python@3.13.rb
**Security Contact:** security@python.org
**Disclosure Policy:** https://www.python.org/dev/security/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

Advisories below are CPython-level vulnerabilities that apply to the Homebrew-installed Python. The Homebrew formula (`python@3.13`) tracks upstream CPython releases with typically a 1–3 day patch lag.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-11940 | High | tarfile hardlink→symlink path traversal bypass — a hardlink referencing a symlink at a deeper archive path bypasses `data`/`tar` filter validation; symlink is recreated at the hardlink's shallower path, escaping the destination directory to enable out-of-destination file reads/writes; incomplete fix for CVE-2025-4330 (CWE-22) | CPython upstream commits (June 2026) | [GHSA-9mc4-rqmq-h467](https://github.com/advisories/GHSA-9mc4-rqmq-h467) |
| CVE-2024-12254 | High | asyncio writelines() memory exhaustion — `asyncio.writelines()` (Python 3.12+) does not pause writing when the send buffer reaches the high-water mark, leading to unbounded memory growth and OOM; affects macOS and Linux; network-accessible asyncio servers exposing writelines() paths are at risk | Python 3.12.x / 3.13.x upstream commits (Dec 2024) | [GHSA-ph84-rcj2-fxxm](https://github.com/advisories/GHSA-ph84-rcj2-fxxm) |
| CVE-2026-4519 | Moderate CVSS 4.3 | webbrowser.open() leading-dash CLI injection — URLs beginning with a dash character are passed to browser subprocesses and interpreted as command-line options; patched to reject leading-dash inputs | CPython upstream commits (March 2026) | [GHSA-rm92-fj5q-mpj5](https://github.com/advisories/GHSA-rm92-fj5q-mpj5) |
| CVE-2026-3446 | Moderate CVSS 4.0 | base64 module silent truncation of malformed data — decode functions stop processing at the first padded quad regardless of whether additional data follows, silently accepting malformed base64 and causing interoperability inconsistencies; immediate workaround: use `validate=True` parameter | CPython upstream commits (April 2026) | [GHSA-8r9f-h969-mm4m](https://github.com/advisories/GHSA-8r9f-h969-mm4m) |
| CVE-2024-3219 | Medium CVSS 4.0 | socket.socketpair() race condition (Windows/non-AF_UNIX) — the pure-Python fallback for `socket.socketpair()` on platforms lacking AF_UNIX support (Windows, some embedded OSes) does not verify the connection before returning, allowing a malicious local peer to substitute a different socket; macOS unaffected (uses AF_UNIX natively) | CPython upstream commits (July 2024) | [GHSA-r8h6-cwxj-rv5j](https://github.com/advisories/GHSA-r8h6-cwxj-rv5j) |
| CVE-2026-18503 | Low CVSS 4.0 | csv.Sniffer ReDoS — super-linear regular-expression work during CSV dialect sniffing in `csv.Sniffer.sniff()`; applications passing unbounded, attacker-controlled input to sniff() can experience significant CPU consumption (CWE-1176) | CPython upstream commits (Aug 2026) | [GHSA-2345-wr3r-cxf2](https://github.com/advisories/GHSA-2345-wr3r-cxf2) |

## Security Posture Notes

The `python@3.13` Homebrew formula (and the versioned `python@3.12`, `python@3.11` formulae) tracks upstream CPython releases. Homebrew maintainers typically land security updates within 1–3 days of a CPython release. macOS ships its own Python 2.7 legacy stub and a separately managed Python 3.x via Xcode Command Line Tools; the Homebrew formula provides a distinct, user-managed interpreter at `/opt/homebrew/bin/python3`. Security patches from Homebrew do not affect the system or Xcode Python versions.

The Python Security Response Team (PSRT) discloses vulnerabilities through the standard CPython release process with announcements on the [python-announce](https://mail.python.org/mailman/listinfo/python-announce-list) mailing list. Critical issues follow a coordinated embargo; lower-severity issues may ship in regular point releases.

The GHSA database contains 138 CPython-related records. This pass mapped 6 recent advisories (2024–2026). The full historical set includes recurring advisory classes not yet individually mapped here:
- Multiple `urllib` / `urllib.parse` SSRF and bypass issues (e.g., CVE-2023-24329, CVE-2022-42919)
- `zipfile` / `tarfile` path traversal series predating the CVE-2025-4330 / CVE-2026-11940 chain
- `ssl` module TLS boundary and CA verification issues

## Dependencies of Note

- **OpenSSL** — the Homebrew Python formula links against Homebrew's OpenSSL 3.x rather than macOS system LibreSSL; OpenSSL CVEs may affect Python's TLS operations (see [[homebrew/openssl@3]])
- **sqlite** — CPython's `sqlite3` stdlib module bundles or links against system SQLite; see [[homebrew/sqlite]] for SQLite-level CVEs

## Open Questions

- CVE-2025-4330 (original tarfile symlink bypass, parent issue of CVE-2026-11940) should be individually mapped in a future pass.
- urllib/urllib3 SSRF boundary advisories from 2022–2025 not yet individually mapped.
- Download analytics unavailable (formulae.brew.sh blocked); retry in future pass.
- Python 3.11 and 3.12 Homebrew formulas reach EOL at upstream schedule — track when Homebrew drops them and what the upgrade path advisory looks like.

## Related Pages

- [[homebrew/openssl@3]] — linked OpenSSL dependency
- [[homebrew/sqlite]] — linked SQLite dependency
- [[python/flask]], [[python/django]] — major packages built on this interpreter
- [[homebrew/index]]

---
*Last updated: 2026-09-02 | Sources: 6 (GHSA)*
