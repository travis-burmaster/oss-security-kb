# Advisory Review Pass — 2026-08-10

**Ecosystems targeted:** Rust/crates.io, Homebrew
**Tools used:** mcp__github__search_code, WebFetch (raw.githubusercontent.com), crates.io API
**OSV.dev status:** HTTP 403 blocked (expected per CLAUDE.md; not used)
**formulae.brew.sh status:** EGRESS_BLOCKED (downloads marked "unknown")

---

## Target 1: rust/zerocopy

**Selection rationale:** High download volume (~792M total / ~17M/week) for a foundational Google-maintained memory-manipulation crate; appears in Fuchsia, Chromium, Android, TensorFlow dependency trees; not previously covered in the wiki.

### Sources consulted

| URL | Content |
|-----|---------|
| `mcp__github__search_code` query: `zerocopy repo:rustsec/advisory-db path:crates` | 1 result: `crates/zerocopy/RUSTSEC-2023-0074.md` |
| `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/zerocopy/RUSTSEC-2023-0074.md` | Full advisory text |
| `mcp__github__search_code` query: `zerocopy repo:github/advisory-database path:advisories` | 27 results; 2 in github-reviewed: GHSA-3mv5-343c-w2qg, GHSA-rjhf-4mh8-9xjq |
| `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/12/GHSA-3mv5-343c-w2qg/GHSA-3mv5-343c-w2qg.json` | Confirmed package=zerocopy, ecosystem=crates.io, severity=LOW |
| `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/12/GHSA-rjhf-4mh8-9xjq/GHSA-rjhf-4mh8-9xjq.json` | Confirmed same advisory, severity=MODERATE |
| `https://crates.io/api/v1/crates/zerocopy` | total_downloads=792,520,238; recent_downloads=218,492,798 (90-day); max_version=0.9.0-alpha.0 |

### Advisories mapped

| ID | Severity | Notes |
|----|----------|-------|
| RUSTSEC-2023-0074 / GHSA-3mv5-343c-w2qg / GHSA-rjhf-4mh8-9xjq | Moderate (GHSA github-reviewed) / LOW (GHSA other) | Same advisory; no CVE assigned. Fixed across 0.2.9 / 0.3.2 / 0.4.1 / 0.5.2 / 0.6.6 / 0.7.31 |

### Negative results

- 25 of 27 zerocopy search results in github/advisory-database are "unreviewed" (NVD imports for packages in other ecosystems mentioning "zerocopy" in description); none confirmed to be for the rust zerocopy crate.
- No advisories found for 0.8.x or 0.9.x lines.

---

## Target 2: homebrew/sqlite

**Selection rationale:** Listed as a future target in wiki/homebrew/index.md; Homebrew ecosystem has lowest wiki coverage (6 pages); SQLite is among the most widely deployed software globally (estimated 1 trillion devices).

**Advisory sourcing challenge:** SQLite is a C library; its CVEs are tracked in NVD and on sqlite.org, not natively in github/advisory-database for the upstream project. Language wrappers that bundle SQLite often carry GHSA records that reference upstream C library CVEs with precise fix versions — these serve as primary-source proxies.

### Sources consulted

| URL | Content |
|-----|---------|
| `mcp__github__search_code` query: `sqlite repo:github/advisory-database path:advisories/github-reviewed` | 132 results |
| `mcp__github__search_code` query: `libsqlite3-sys repo:rustsec/advisory-db path:crates` | 1 result: `crates/libsqlite3-sys/RUSTSEC-2022-0090.md` |
| `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/libsqlite3-sys/RUSTSEC-2022-0090.md` | CVE-2022-35737 confirmed: printf array-bounds overflow; SQLite 1.0.12–3.39.1; fixed 3.39.2 |
| `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/08/GHSA-jw36-hf63-69r9/GHSA-jw36-hf63-69r9.json` | CVE-2022-35737: libsqlite3-sys < 0.25.1, CVSS 9.1 HIGH |
| `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/07/GHSA-2m69-gcr7-jv3q/GHSA-2m69-gcr7-jv3q.json` | CVE-2025-6965: SQLitePCLRaw.lib.e_sqlite3 ≤ 2.1.11, CVSS 9.8 HIGH; SQLite < 3.50.2 |
| `https://formulae.brew.sh/api/formula/sqlite.json` | BLOCKED (EGRESS_BLOCKED) |

### Advisories mapped

| CVE | Severity | Upstream fix | Primary source |
|-----|----------|-------------|----------------|
| CVE-2022-35737 | High CVSS 9.1 | SQLite 3.39.2 | GHSA-jw36-hf63-69r9 / RUSTSEC-2022-0090 |
| CVE-2025-6965 | High CVSS 9.8 | SQLite 3.50.2 | GHSA-2m69-gcr7-jv3q |

### Rejected results from sqlite GHSA search

- GHSA-2497-gp99-2m74: CVE-2026-21696 for pterodactyl/wings (Go) — application-level SQLite parameter limit bug, not a C library CVE
- GHSA-339v-266x-79xr: CVE-2026-53602 for forgekeep/nebula-mesh (Go) — application-level authorization gap, unrelated
- GHSA-j7fr-3v8c-3qc3: CVE-2026-54620 for sqlite3-ruby gem — use-after-free in Ruby wrapper, not C library
- GHSA-x783-xp3g-mqhp: CVE-2026-40315 for PraisonAI (PyPI) — SQL injection in application layer, unrelated
- 128 additional results not checked; focused on results traceable to upstream SQLite C library CVEs

---

## Master index corrections

| Correction | Before | After |
|-----------|--------|-------|
| Total page count | 250 | 254 |
| Rust count | 32 | 34 |
| .NET count | 10 | 11 |
| Homebrew count | 6 | 7 |
| linux/openssl description | "baseline stub · upstream-first page for future distro normalization" | "advisory mapped · [correct description]" |
| Missing entries | — | prost (Rust), Microsoft.AspNetCore.Authentication.Negotiate (.NET) added retroactively from 2026-08-09 pass |
| Last updated date | 2026-08-08 | 2026-08-10 |

---

## Packages researched but not mapped (negative results / pivots)

| Package | Reason |
|---------|--------|
| homebrew/gnupg | github-reviewed GHSAs found were for `in-toto` (PyPI) and other Python packages that use gnupg, not the C library; no GHSA directly tracking gnupg/gnupg repository advisory history |
| linux/openssl | Already advisory-mapped with comprehensive 2014–2026 CVE history (confirmed by reading the existing file); no gap filling needed in this pass |
