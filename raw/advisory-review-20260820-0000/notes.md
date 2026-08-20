# Advisory Review Pass — 2026-08-20

## Targets

1. `rsa` (Rust / crates.io)
2. `golang.org/x/oauth2` (Go)

## Sources consulted

### rust/rsa

- rustsec/advisory-db: `crates/rsa/RUSTSEC-2023-0071.md`
  - https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/rsa/RUSTSEC-2023-0071.md
  - Advisory: RUSTSEC-2023-0071, CVE-2023-49092, GHSA-c38w-74pg-36hr, GHSA-4grx-2x9w-596c
  - Published: 2023-11-22; no patched version confirmed as of 2026-08-20

- github/advisory-database search: `CVE-2023-49092 repo:github/advisory-database path:advisories`
  - Found: `advisories/github-reviewed/2023/11/GHSA-c38w-74pg-36hr/GHSA-c38w-74pg-36hr.json`
  - Found: `advisories/github-reviewed/2023/11/GHSA-4grx-2x9w-596c/GHSA-4grx-2x9w-596c.json`
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/11/GHSA-c38w-74pg-36hr/GHSA-c38w-74pg-36hr.json
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/11/GHSA-4grx-2x9w-596c/GHSA-4grx-2x9w-596c.json
  - GHSA-c38w-74pg-36hr: ecosystem crates.io, affected 0 through 0.9.6, no patched (at filing)
  - GHSA-4grx-2x9w-596c: same advisory, second alias

- crates.io API: `https://crates.io/api/v1/crates/rsa`
  - total_downloads: 202,889,842; recent_downloads: 46,124,127
  - max_stable_version: 0.9.10; max_version: 0.10.0-rc.18
  - repository: https://github.com/RustCrypto/RSA

- crates.io versions API: `https://crates.io/api/v1/crates/rsa/versions`
  - 0.9.7 (2024-11-26), 0.9.8 (2025-03-12), 0.9.9 (2025-11-13), 0.9.10 (2026-01-06) — none yanked
  - RUSTSEC advisory still lists no patched versions; all 0.9.x assumed affected

- RustCrypto/RSA SECURITY.md: https://github.com/RustCrypto/RSA/blob/master/SECURITY.md
  - Security contact: GitHub private advisory at https://github.com/RustCrypto/RSA/security/advisories/new
  - 90-day minimum responsible disclosure; fixes applied to most recent release only

- Marvin Attack reference: https://people.redhat.com/~hkario/marvin/
- RustCrypto/RSA tracking issue: https://github.com/RustCrypto/RSA/issues/626

- Companion crate rsa-export: RUSTSEC-2024-0333 found at crates/rsa-export/RUSTSEC-2024-0333.md
  - Separate advisory for a different crate; NOT included on the rsa page

### go/golang.org/x/oauth2

- github/advisory-database search: `golang.org/x/oauth2 repo:github/advisory-database path:advisories`
  - Returned 3 results total
  - GHSA-6v2p-p543-phr9 (2025/07) — confirmed as direct oauth2 advisory
  - GHSA-5pf6-2qwx-pxm2 (2024/03) — confirmed as github.com/cloudevents/sdk-go/v2 (references oauth2 in context but is NOT an oauth2 advisory)
  - GHSA-c6gw-w398-hv78 (2025/02) — confirmed as go-jose (references oauth2 in context but is NOT an oauth2 advisory)

- GHSA-6v2p-p543-phr9:
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/07/GHSA-6v2p-p543-phr9/GHSA-6v2p-p543-phr9.json
  - CVE-2025-22868 / GO-2025-3488
  - Package: golang.org/x/oauth2 (Go ecosystem)
  - Severity: High; CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
  - Affected: all versions < 0.27.0; Fixed: 0.27.0
  - Fix CL: https://go.dev/cl/652155; Issue: https://go.dev/issue/71490
  - Govulncheck: https://pkg.go.dev/vuln/GO-2025-3488

- pkg.go.dev: https://pkg.go.dev/golang.org/x/oauth2
  - Latest version: v0.36.0 (2026-02-11)
  - Known importers: 48,088+
  - Maintained by Go team at Google (golang.org/x/ extended stdlib)
  - Repository: https://github.com/golang/oauth2

- Go security policy: https://go.dev/security/policy
  - Disclosure email: security@golang.org

## Decision log

- cobra (github.com/spf13/cobra) was the initial second candidate; no advisories found in github/advisory-database (total_count: 0); discarded
- go-playground/validator: no advisories found (total_count: 0); discarded
- golang.org/x/oauth2 selected; 1 direct advisory confirmed with high blast radius (48,088+ importers)
- grpc-gateway (1 advisory) was noted; not selected in favor of oauth2 given higher importer count and simpler mapping
