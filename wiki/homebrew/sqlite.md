# sqlite (Homebrew)

**Registry:** Homebrew
**Weekly Downloads:** unknown (formulae.brew.sh analytics unavailable in this environment; SQLite is among the most widely deployed embedded databases globally; macOS ships a separate system SQLite independent of the Homebrew formula)
**Repository:** https://github.com/sqlite/sqlite (GitHub mirror; canonical source: https://www.sqlite.org/src)
**Security Contact:** security@sqlite.org
**Disclosure Policy:** https://www.sqlite.org/security.html
**Current Status:** advisory-mapped

## Audit History

*No audits on record.*

## Known Vulnerabilities

All entries reference the **upstream SQLite C library** version at which the fix was released. The Homebrew `sqlite` formula tracks upstream releases; macOS's system SQLite (`/usr/lib/libsqlite3.dylib`) is Apple-maintained and versioned independently — consult Apple Security Updates for system library fixes.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-35737 | High (CVSS 3.1: 9.1 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H) | **printf array-bounds overflow** — `sqlite3_str_vappendf` (the internal `printf`-style formatter) does not bound-check when billions of bytes are specified as a string argument via the C API; on 64-bit systems triggers a heap out-of-bounds write, potentially crashing or enabling memory corruption; on 32-bit systems integer overflow reliably causes crash. Affects SQLite 1.0.12 through 3.39.1; also inherited by any language binding that bundles SQLite (e.g., Rust `libsqlite3-sys` < 0.25.1). | 3.39.2 (2022-08-04) | [GHSA-jw36-hf63-69r9](https://github.com/advisories/GHSA-jw36-hf63-69r9) · [RUSTSEC-2022-0090](https://rustsec.org/advisories/RUSTSEC-2022-0090.html) |
| CVE-2025-6965 | High (CVSS 3.1: 9.8 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | **Aggregate function memory corruption** — The bytecode execution engine allows the count of aggregate function terms to exceed the number of available result columns, triggering out-of-bounds memory access; exploitable via crafted SQL against any application that processes untrusted queries. Affects SQLite before 3.50.2; also inherited by bundled wrappers (e.g., .NET `SQLitePCLRaw.lib.e_sqlite3` ≤ 2.1.11). | 3.50.2 (2025-06-21) | [GHSA-2m69-gcr7-jv3q](https://github.com/advisories/GHSA-2m69-gcr7-jv3q) (via SQLitePCLRaw.lib.e_sqlite3 NuGet advisory) |

## Security Posture Notes

- SQLite is one of the most widely deployed software components in existence: estimated to be on over one trillion devices. On macOS it is a system-level dependency shipped with the OS, and the Homebrew formula installs a parallel, user-managed copy that matches the upstream release cadence more closely than the OS version.
- **macOS system SQLite lag**: Apple's system `libsqlite3.dylib` is patched via Security Updates and typically lags several minor versions behind upstream; applications relying on the system library should consult [Apple Security Releases](https://support.apple.com/en-us/103408).
- **CVE tracking challenge**: SQLite has an extensive CVE history (hundreds of NVD records dating from the early 2000s), but many older CVEs are categorised as "unreviewed" in GitHub's advisory database. This page maps only CVEs with confirmed fix versions from authoritative sources. For the full upstream vulnerability list, see https://www.sqlite.org/cves.html and https://www.sqlite.org/security.html.
- SQLite is not memory-safe; its C implementation has recurring parser and bytecode-engine boundary issues. The `--SQLITE_ENABLE_MEMSYS5` strict-mode and the JSON/FTS/RTree extension surface have historically produced additional CVEs not covered here.
- The `sqlite3` Homebrew formula is typically updated within 1–3 days of an upstream release; Formula PRs are tracked at https://github.com/Homebrew/homebrew-core.

## Dependencies of Note

- Many Homebrew-installed packages link or bundle SQLite: `python`, `php`, `node`, `ruby`, `git`, `curl`, `imagemagick`, among others. A vulnerable system SQLite (or an old Homebrew formula) may be inherited by any of these.
- Rust bindings: `rusqlite` (links against system or bundled SQLite) and `libsqlite3-sys` (optionally bundles upstream SQLite source). See RUSTSEC-2022-0090 and the GHSA tracking entry for the bundled-copy exposure surface.

## Open Questions

- Which Homebrew-installed packages link dynamically against the formula's SQLite vs statically bundle their own copy?
- Are there additional CVEs in the 2023–2025 NVD record set (between CVE-2022-35737 and CVE-2025-6965) warranting explicit mapping in this page?
- Does the Homebrew formula include `--SQLITE_ENABLE_MEMSYS5` or any hardening flags that might affect exploitability of known CVEs on macOS?

## Related Pages

- [[homebrew/openssl@3]]
- [[homebrew/curl]]
- [[homebrew/index]]

---
*Last updated: 2026-08-10 | Sources: 3 (GHSA-jw36-hf63-69r9 via github/advisory-database; RUSTSEC-2022-0090 via rustsec/advisory-db; GHSA-2m69-gcr7-jv3q via github/advisory-database; sqlite.org/security.html referenced for posture notes)*
