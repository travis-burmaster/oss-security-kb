# Advisory Review Pass — 2026-08-21

## Targets

- `linux/zlib` (new page)
- `homebrew/gnupg` (new page)

## Environment Notes

- OSV.dev API blocked (HTTP 403) — not used
- formulae.brew.sh blocked — gnupg download stats marked "unknown"
- www.zlib.net blocked — version info derived from advisory records and training data
- GitHub advisory database accessible via mcp__github__search_code + WebFetch (raw.githubusercontent.com)

---

## linux/zlib research

### Search queries
- `CVE-2022-37434 repo:github/advisory-database path:advisories` → 1 result: GHSA-cfmr-vrgj-vqwv
- `CVE-2018-25032 repo:github/advisory-database path:advisories` → 2 results: GHSA-jc36-42cf-vqwj (github-reviewed/2022/03), GHSA-v6gp-9mmm-c6p5 (github-reviewed/2022/04)
- `CVE-2022-37434 zlib inflate heap repo:github/advisory-database path:advisories` → confirmed GHSA-cfmr-vrgj-vqwv
- `zlib CVE-2023 heap buffer repo:github/advisory-database path:advisories` → 2 results: GHSA-mq29-j5xf-cjwr (pyminizip, 2023/10), GHSA-q5fm-55c2-v6j9 (fiona, 2024/07)

### Advisory records fetched
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/08/GHSA-cfmr-vrgj-vqwv/GHSA-cfmr-vrgj-vqwv.json`
  → CVE-2022-37434, Critical CVSS 9.8, heap buffer over-read/overflow in inflate.c via large gzip header extra field; zlib through 1.2.12
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/03/GHSA-jc36-42cf-vqwj/GHSA-jc36-42cf-vqwj.json`
  → CVE-2018-25032, High CVSS 7.5, memory corruption in deflate path; zlib < 1.2.12 (GHSA is for nokogiri as downstream; upstream is zlib)
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/04/GHSA-v6gp-9mmm-c6p5/GHSA-v6gp-9mmm-c6p5.json`
  → CVE-2018-25032, High CVSS 7.5, confirmed upstream zlib vulnerability
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/10/GHSA-mq29-j5xf-cjwr/GHSA-mq29-j5xf-cjwr.json`
  → CVE-2023-45853, Critical CVSS 9.8, MiniZip integer overflow in zipOpenNewFileInZip4_64(); affects pyminizip (Python) as downstream; upstream is zlib MiniZip contrib code

### Fixed versions
- CVE-2018-25032: zlib 1.2.12 (released 2022-03-26)
- CVE-2022-37434: zlib 1.2.12.1 (released 2022-08-05)
- CVE-2023-45853: zlib 1.3.1 (released 2024-01-22); note: MiniZip contrib only, not core zlib

### Downstream note
GHSA-jc36-42cf-vqwj and GHSA-v6gp-9mmm-c6p5 are filed against nokogiri (RubyGems) which bundles zlib. The root CVE-2018-25032 is an upstream zlib vulnerability. Only the upstream zlib CVE is cited on the linux/zlib page.

---

## homebrew/gnupg research

### Search queries
- `gnupg repo:github/advisory-database path:advisories` → 108 total results (too broad)
- `CVE-2022-34903 gnupg repo:github/advisory-database path:advisories` → 1 result: GHSA-356p-pg27-x2cf
- `CVE-2019-13050 gnupg repo:github/advisory-database path:advisories` → 1 result: GHSA-ch5h-mpfr-fhxh
- `CVE-2018-9234 gnupg repo:github/advisory-database path:advisories` → 1 result: GHSA-mq99-p8pq-jp4q
- `CVE-2021-40528 gnupg repo:github/advisory-database path:advisories` → 1 result: GHSA-8m2v-68m9-q2c7
- `gnupg CVE-2024 repo:github/advisory-database path:advisories` → 4 results, all for GnuTLS (different project), not GnuPG
- `"gnupg" "signature" CVE repo:github/advisory-database path:advisories/unreviewed/2024` → 0 results

### Advisory records fetched
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/07/GHSA-356p-pg27-x2cf/GHSA-356p-pg27-x2cf.json`
  → CVE-2022-34903, Moderate CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:L/A:N; signature forgery via status-line injection; GnuPG through 2.3.6; fixed 2.3.7
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-ch5h-mpfr-fhxh/GHSA-ch5h-mpfr-fhxh.json`
  → CVE-2019-13050, High CVSS 9.0; persistent DoS via SKS keyserver certificate flooding; GnuPG through 2.2.16; no GnuPG patch
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-mq99-p8pq-jp4q/GHSA-mq99-p8pq-jp4q.json`
  → CVE-2018-9234, High CVSS 7.5; GnuPG 2.2.4–2.2.5 offline-master-key enforcement gap; no dedicated fix
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-8m2v-68m9-q2c7/GHSA-8m2v-68m9-q2c7.json`
  → CVE-2021-40528, Moderate; Libgcrypt < 1.9.4 ElGamal plaintext recovery; fixed Libgcrypt 1.9.4

### Download stats
- formulae.brew.sh blocked; analytics unavailable; stats marked "unknown"

### Notes
- CVE-2024-28835 returned in 2024 gnupg search but confirmed to be GnuTLS (separate library); not included
- No GnuPG-specific advisories confirmed in github/advisory-database for 2023-2026; deeper search may be warranted in a future pass
- CVE-2021-40528 technically affects Libgcrypt (not GnuPG directly), but Libgcrypt is GnuPG's crypto backend and GnuPG bundles it; included with clear attribution to Libgcrypt
