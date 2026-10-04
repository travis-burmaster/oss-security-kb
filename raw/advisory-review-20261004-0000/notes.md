# Advisory Review Pass — 2026-10-04

## Targets

1. **rust/pyo3** (new advisory-mapped page) — 2 RUSTSEC advisories confirmed
2. **go/github.com/aws/aws-sdk-go-v2** (new advisory-mapped page) — 1 GHSA advisory confirmed
3. **rust/serde_json** (status upgrade: baseline stub → advisory-mapped) — 0 direct advisories; 4th independent pass confirming no RUSTSEC/GHSA advisory for serde_json directly

## Advisory Sources

### rust/pyo3

- RUSTSEC-2026-0013 / GHSA-47qc-857f-7w7f (High: type confusion in abi3 + Python 3.12+ subclassing path; fixed 0.28.2)
  - Primary: https://rustsec.org/advisories/RUSTSEC-2026-0013.html
  - rustsec/advisory-db path: crates/pyo3/RUSTSEC-2026-0013.md
  - GitHub advisory: https://github.com/advisories/GHSA-47qc-857f-7w7f

- RUSTSEC-2026-0177 (High: missing Sync bound on PyCFunction::new_closure enabling data race; fixed 0.29.0)
  - Primary: https://rustsec.org/advisories/RUSTSEC-2026-0177.html
  - rustsec/advisory-db path: crates/pyo3/RUSTSEC-2026-0177.md

- crates.io API metadata: https://crates.io/api/v1/crates/pyo3
  - Total downloads: 266,118,612 (as of 2026-10-04)
  - Recent (90-day): 63,140,744
  - Current version: 0.29.3 (2026-09-30)
  - Repository: https://github.com/pyo3/pyo3

- mcp__github__search_code searches:
  - `crate = "pyo3" repo:rustsec/advisory-db` — 2 results (RUSTSEC-2026-0013, RUSTSEC-2026-0177); all others are in unrelated crate dirs

### go/github.com/aws/aws-sdk-go-v2

- GHSA-xmrv-pmrh-hhx2 (Moderate CVSS 5.9 AV:N/AC:H: EventStream header decoder panic DoS; 12 affected service modules; fixed 2026-03-23)
  - Primary: https://github.com/advisories/GHSA-xmrv-pmrh-hhx2
  - github/advisory-database path: advisories/github-reviewed/2026/04/GHSA-xmrv-pmrh-hhx2/GHSA-xmrv-pmrh-hhx2.json
  - Upstream security advisory: https://github.com/aws/aws-sdk-go-v2/security/advisories/GHSA-xmrv-pmrh-hhx2

- pkg.go.dev metadata: https://pkg.go.dev/github.com/aws/aws-sdk-go-v2
  - Current version: v1.47.1 (2026-09-24)
  - Min Go: 1.24
  - License: Apache-2.0

- mcp__github__search_code search:
  - `aws-sdk-go-v2 repo:github/advisory-database Go ecosystem` — 2 results; 1 is GHSA-xmrv-pmrh-hhx2 (relevant); 1 is GHSA-xcq4-m2r3-cmrj (targets Trivy, only cites aws-sdk-go-v2 indirectly; excluded)

### rust/serde_json (status upgrade)

- mcp__github__search_code searches:
  - `crate = "serde_json" path:crates/serde_json repo:rustsec/advisory-db` — 0 results
  - `crate = "serde_json" repo:rustsec/advisory-db` — 3 results, all in unrelated crate files (gix-attributes, json, json5) where serde_json is mentioned as a comparison/alternative, not as the affected package
- Prior passes confirming the same: 2026-04-20, 2026-07-19, 2026-10-02 (logged under serde pass), and this pass 2026-10-04
- Status upgrade from baseline stub to advisory-mapped is appropriate: advisory-mapping work is complete, no advisories to map

## Index Changes

- wiki/rust/pyo3.md: new (advisory-mapped)
- wiki/go/github.com/aws/aws-sdk-go-v2.md: new (advisory-mapped)
- wiki/rust/serde_json.md: Current Status updated to advisory-mapped; last-updated updated
- wiki/rust/index.md: pyo3 entry added; serde_json entry updated to advisory-mapped
- wiki/go/index.md: aws-sdk-go-v2 entry added
- wiki/index.md: Rust count 50→51, Go count 36→37, total 309→311; serde_json entry updated
- wiki/log.md: new entry prepended
