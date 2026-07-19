# Advisory Review Evidence — 2026-07-19 06:00 UTC

## Pass Summary

- Targets: linux/openssl (upgrade baseline stub → advisory-mapped), go/github.com/miekg/dns (new page), rust/serde (stats refresh)
- OSV.dev API: blocked (HTTP 403) — used github/advisory-database + rustsec/advisory-db as fallbacks
- openssl-library.org advisory TXT files: blocked (HTTP 403) — used GHSA records as citable primary sources
- formulae.brew.sh: not accessed this pass

---

## Target 1: linux/openssl

**Goal:** Upgrade from baseline stub to advisory-mapped with confirmed historical CVEs.

### Sources Consulted

| URL / Source | Status | Notes |
|---|---|---|
| https://openssl-library.org/news/vulnerabilities/index.html | 403 blocked | Index page not accessible |
| https://openssl-library.org/news/secadv/20220315.txt | 403 blocked | CVE-2022-0778 advisory |
| https://openssl-library.org/news/secadv/20221101.txt | 403 blocked | CVE-2022-3602/3786 advisory |
| https://openssl-library.org/news/secadv/20230207.txt | 403 blocked | CVE-2023-0215/0286 advisory |
| mcp__github__search_code: `CVE-2022-0778 openssl repo:github/advisory-database` | Found GHSA-x3mh-jvjw-3xwx | openssl-src crate, same upstream CVE |
| mcp__github__search_code: `CVE-2022-3602 openssl repo:github/advisory-database` | Found GHSA-8rwr-x37p-mx23 | openssl-src crate |
| mcp__github__search_code: `CVE-2022-3786 openssl repo:github/advisory-database` | Found GHSA-h8jm-2x53-xhp5 | openssl-src crate |
| mcp__github__search_code: `CVE-2023-0215 openssl repo:github/advisory-database` | Found GHSA-r7jw-wp68-3xch | openssl-src crate |
| mcp__github__search_code: `CVE-2023-0286 openssl repo:github/advisory-database` | Found GHSA-x4qr-2fvf-3mr5 (pyca/cryptography context) | Referenced openssl-library.org/news/secadv/20230207.txt |
| mcp__github__search_code: `CVE-2024-0727 openssl repo:github/advisory-database` | Found GHSA-9v9h-cgj8-h64p | pyca/cryptography (PyPI), same upstream CVE |
| mcp__github__search_code: `CVE-2024-5535 openssl repo:github/advisory-database` | Found GHSA-4fc7-mvrr-wv2c (unreviewed) | Full advisory text confirmed via WebFetch |
| WebFetch: GHSA-x3mh-jvjw-3xwx raw JSON | OK | CVSS 7.5 High, fixed 1.0.2zd/1.1.1n/3.0.2 |
| WebFetch: GHSA-8rwr-x37p-mx23 raw JSON | OK | CVSS 9.8 High (initially Critical), fixed 3.0.7 |
| WebFetch: GHSA-h8jm-2x53-xhp5 raw JSON | OK | CVSS 7.5 High, fixed 3.0.7 |
| WebFetch: GHSA-r7jw-wp68-3xch raw JSON | OK | CVSS 7.5 High, fixed 1.0.2zj/1.1.1t/3.0.8 |
| WebFetch: GHSA-9v9h-cgj8-h64p raw JSON | OK | CVSS 7.1/AV:L Moderate, fixed cryptography 42.0.2 (upstream OpenSSL 3.0.13/3.1.5/3.2.1) |

### Advisory Mapping Notes

- CVE-2014-0160 (Heartbleed): No reviewed GHSA found in advisory-database; cited canonical upstream advisory URL as source. This is a historically established Critical vulnerability; details are unambiguous.
- CVE-2022-0778 / CVE-2022-3602 / CVE-2022-3786 / CVE-2023-0215: GHSA records are scoped to the Rust `openssl-src` crate (which bundles the upstream OpenSSL C library). The CVE IDs, descriptions, and upstream fix versions are identical to the upstream OpenSSL advisories.
- CVE-2023-0286: Referenced in the context of a separate GHSA for `sgx-dcap-quote-verify-python` and `pyca/cryptography`; upstream advisory URL confirmed from text match in advisory database.
- CVE-2024-0727: GHSA-9v9h-cgj8-h64p is scoped to Python `cryptography` package (affected < 42.0.2 because it bundles OpenSSL); upstream OpenSSL fix versions extracted from advisory text.
- CVE-2024-5535: GHSA-4fc7-mvrr-wv2c (unreviewed) full text confirmed via WebFetch; severity confirmed as Low per advisory text.

---

## Target 2: go/github.com/miekg/dns

### Sources Consulted

| URL / Source | Status | Notes |
|---|---|---|
| mcp__github__search_code: `miekg/dns repo:github/advisory-database path:advisories` | Found 3 records | GHSA-p55x-7x9v-q8m4, GHSA-44r7-7p62-q3fr, GHSA-9jcx-pr2f-qvq5 |
| WebFetch: GHSA-p55x-7x9v-q8m4 raw JSON | OK | CVE-2017-15133, High CVSS 7.5, TCP timing DoS, fixed 1.0.4 |
| WebFetch: GHSA-44r7-7p62-q3fr raw JSON | OK | CVE-2019-19794, Moderate, predictable TXID via math/rand, fixed 1.1.25 |
| WebFetch: GHSA-9jcx-pr2f-qvq5 raw JSON | OK | CVE-2018-17419, High CVSS 7.5, ParseZone nil ptr deref, fixed 1.0.10 |
| WebFetch: https://pkg.go.dev/github.com/miekg/dns | OK | v1.1.72 (Jan 22, 2026), 16,234+ importers |

### Advisory Summary

All 3 confirmed GHSA records found; no additional advisories found in this search scope. OSV blocked, so full OSV advisory history may contain additional entries (unlikely given pass coverage but possible).

---

## Target 3: rust/serde

### Sources Consulted

| URL / Source | Status | Notes |
|---|---|---|
| mcp__github__search_code: `serde repo:rustsec/advisory-db path:crates` | OK | Results: rmp-serde, serde_yml, serde_yaml, serde_cbor, serde-json-wasm — no `crates/serde/` directory advisory |
| WebFetch: https://crates.io/api/v1/crates/serde | OK | Total: 1,173,624,524 downloads; recent 90-day: 236,866,583; current: 1.0.229 (July 18, 2026) |

### Result

No advisory found for the core `serde` crate; status remains baseline stub. Download stats updated; related-crate advisories documented to sharpen scope boundaries.

---

## Files Changed

- `wiki/linux/openssl.md` — upgraded to advisory-mapped; added 8 historical CVEs (CVE-2014-0160, 2022-0778, 2022-3602, 2022-3786, 2023-0215, 2023-0286, 2024-0727, 2024-5535) + retained 2 existing 2026 CVEs
- `wiki/go/github.com/miekg/dns.md` — new advisory-mapped page; 3 CVEs
- `wiki/rust/serde.md` — download stats updated; advisory absence reconfirmed
- `wiki/go/index.md` — added miekg/dns entry
- `wiki/index.md` — Go 21→22, total 226→227, linux/openssl status corrected to advisory-mapped
- `wiki/log.md` — prepended entry
- `raw/advisory-review-20260719-0600/notes.md` — this file
