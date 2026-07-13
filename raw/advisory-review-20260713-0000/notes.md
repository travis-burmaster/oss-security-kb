# Advisory Review — 2026-07-13

Pass type: public-information-only advisory mapping
Ecosystems targeted: Maven, Go, Rust/crates.io
OSV.dev API: blocked (HTTP 403) — not consulted
Maven Central stats API: blocked (HTTP 403) — not consulted
openssl.org/news: blocked (HTTP 403) — not consulted
pkg.go.dev: accessible (importers count only; module pages available)
crates.io API: accessible (download counts available)

## Packages Researched

### maven/org.apache.commons/commons-text

**Primary sources consulted:**
- `mcp__github__search_code` query: `commons-text CVE-2022-42889 repo:github/advisory-database` → confirmed GHSA-599f-7c49-w659
- WebFetch of GHSA JSON: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/10/GHSA-599f-7c49-w659/GHSA-599f-7c49-w659.json
  - CVE-2022-42889 Critical CVSS 9.8 — Text4Shell StringSubstitutor RCE; affects 1.5–1.9; fixed 1.10.0
- `mcp__github__search_code` for additional commons-text advisories: `commons-text StringSubstitutor GHSA repo:github/advisory-database` — 0 additional results
- `mcp__github__search_code` confirmation: `commons-text org.apache.commons repo:github/advisory-database` — 1 result (GHSA-599f-7c49-w659 only)
- Maven Central version API: blocked HTTP 403; latest stable not confirmed; 1.10.0 is minimum safe
- advisory count: 1 confirmed advisory in github/advisory-database

### go/github.com/tidwall/gjson

**Primary sources consulted:**
- `mcp__github__search_code` query: `gjson tidwall GHSA repo:github/advisory-database` → found GHSA-ppj4-34rq-v8j9, GHSA-wjm3-fq3r-5x46, GHSA-w942-gw6m-p62c, GHSA-p64j-r5f4-pwwx, GHSA-c9gm-7rfj-8w5h (withdrawn)
- WebFetch of GHSA JSONs:
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/10/GHSA-ppj4-34rq-v8j9/GHSA-ppj4-34rq-v8j9.json — CVE-2021-42836 High CVSS 9.1 ReDoS, fixed 1.9.3
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/05/GHSA-wjm3-fq3r-5x46/GHSA-wjm3-fq3r-5x46.json — CVE-2020-36066 High CVSS 9.1 DoS, fixed 1.6.5
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/06/GHSA-w942-gw6m-p62c/GHSA-w942-gw6m-p62c.json — CVE-2020-35380 High CVSS 7.5 OOB panic, fixed 1.6.4
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/02/GHSA-p64j-r5f4-pwwx/GHSA-p64j-r5f4-pwwx.json — CVE-2020-36067 High CVSS 7.5 slice OOB, fixed 1.6.6
- `mcp__github__search_code` post-1.9.3 search: `gjson tidwall repo:github/advisory-database path:advisories/github-reviewed/2022 OR 2023 OR 2024` — 2 results, both already included or withdrawn
- WebFetch of pkg.go.dev: https://pkg.go.dev/github.com/tidwall/gjson — current version v1.19.0 (May 2026), 10,420 importers
- advisory count: 4 active advisories confirmed; 1 withdrawn duplicate (GHSA-c9gm-7rfj-8w5h)

### rust/mio

**Primary sources consulted:**
- `mcp__github__search_code` query: `mio named pipe windows repo:rustsec/advisory-db` → found RUSTSEC-2024-0019
- `mcp__github__search_code` query: `mio repo:rustsec/advisory-db path:crates/mio` → found RUSTSEC-2024-0019 and RUSTSEC-2020-0081
- WebFetch of RustSec advisories:
  - https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/mio/RUSTSEC-2024-0019.md — CVE-2024-27308 / GHSA-r8w9-5wcg-vfj7 High: Windows named-pipe use-after-free, affects mio ≥ 0.7.2 ≤ 0.8.10 (Windows), fixed ≥ 0.8.11
  - https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/mio/RUSTSEC-2020-0081.md — CVE-2020-35922 / GHSA-pf3p-x6qj-6j7q High local: SocketAddr memory-layout unsoundness, affects 0.7.0–0.7.5, fixed ≥ 0.7.6
- WebFetch of crates.io API: https://crates.io/api/v1/crates/mio — current stable 1.2.1, ~846M total downloads, ~196M recent
- advisory count: 2 confirmed advisories in rustsec/advisory-db

## Confidence Table

| Advisory | Source confirmed? | URL fetched? | CVSS confirmed? |
|----------|------------------|-------------|----------------|
| GHSA-599f-7c49-w659 / CVE-2022-42889 | ✓ | ✓ | ✓ Critical 9.8 |
| GHSA-w942-gw6m-p62c / CVE-2020-35380 | ✓ | ✓ | ✓ High 7.5 |
| GHSA-wjm3-fq3r-5x46 / CVE-2020-36066 | ✓ | ✓ | ✓ High 9.1 |
| GHSA-p64j-r5f4-pwwx / CVE-2020-36067 | ✓ | ✓ | ✓ High 7.5 |
| GHSA-ppj4-34rq-v8j9 / CVE-2021-42836 | ✓ | ✓ | ✓ High 9.1 |
| RUSTSEC-2020-0081 / GHSA-pf3p-x6qj-6j7q | ✓ | ✓ | ✓ High (local) |
| RUSTSEC-2024-0019 / GHSA-r8w9-5wcg-vfj7 | ✓ | ✓ | ✓ High (Windows) |
