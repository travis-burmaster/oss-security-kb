# Advisory Review Notes — 2026-07-12

## Pass Summary

- **Date:** 2026-07-12
- **Targets:** 3 packages (1 Maven, 2 Rust/crates.io)
- **OSV.dev:** blocked (HTTP 403) — not used
- **Primary sources:** github/advisory-database (via mcp__github__search_code + WebFetch on raw.githubusercontent.com), rustsec/advisory-db (via mcp__github__search_code + WebFetch on raw.githubusercontent.com), crates.io API

---

## Target 1: commons-collections:commons-collections (Maven)

### Sources consulted
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-fjq5-5j5f-mvxh/GHSA-fjq5-5j5f-mvxh.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2020/06/GHSA-6hgm-866r-3cjv/GHSA-6hgm-866r-3cjv.json
- https://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability (FoxGlove blog — URL in GHSA references, not fetched directly)
- https://github.com/apache/commons-collections (repository metadata)
- Maven Central search API (https://search.maven.org) — returned HTTP 403, download stats unavailable

### Advisories found
| ID | CVE | Severity | Fixed in |
|----|-----|----------|----------|
| GHSA-fjq5-5j5f-mvxh | CVE-2015-7501 | Critical CVSS 9.8 | commons-collections 3.2.2; commons-collections4 4.1 |
| GHSA-6hgm-866r-3cjv | CVE-2015-6420 | High | commons-collections 3.2.2; commons-collections4 4.1 |

### Decision
Advisory-mapped. Two distinct GHSA records for the same class of gadget-chain deserialization attack surface, same fix versions.

---

## Target 2: nix (crates.io)

### Sources consulted
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/nix/RUSTSEC-2021-0119.md
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/01/GHSA-76w9-p8mg-j927/GHSA-76w9-p8mg-j927.json
- https://crates.io/api/v1/crates/nix (download stats: ~660M total, ~17M/week est., latest 0.31.3)
- https://github.com/nix-rust/nix/issues/1541 (upstream issue, URL from RustSec record)

### Advisories found
| ID | CVE | Severity | Fixed in |
|----|-----|----------|----------|
| RUSTSEC-2021-0119 / GHSA-76w9-p8mg-j927 | CVE-2021-45707 | Moderate CVSS 6.7 | 0.20.2, 0.21.2, 0.22.2, ≥ 0.23.0 |

### Decision
Advisory-mapped. One confirmed RustSec advisory: OOB write in getgrouplist on Linux/FreeBSD/Android/etc. when user has > 16 groups.

---

## Target 3: quinn (crates.io)

### Sources consulted
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/quinn/RUSTSEC-2021-0035.md
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/08/GHSA-fhv4-fx3v-77w6/GHSA-fhv4-fx3v-77w6.json
- https://crates.io/api/v1/crates/quinn (download stats: ~223M total, ~9M/week est., latest 0.11.11)
- https://github.com/quinn-rs/quinn/issues/968 (upstream issue, URL from RustSec record)

### Advisories found
| ID | CVE | Severity | Fixed in |
|----|-----|----------|----------|
| RUSTSEC-2021-0035 / GHSA-fhv4-fx3v-77w6 | CVE-2021-28036 | High CVSS 7.5 (informational unsound) | 0.5.4, 0.6.2, ≥ 0.7.0 |

### Decision
Advisory-mapped. One confirmed RustSec advisory: invalid SocketAddr memory layout assumption (informational unsound).
