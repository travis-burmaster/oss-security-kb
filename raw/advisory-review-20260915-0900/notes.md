# Advisory Review Pass — 2026-09-15 09:00 UTC

## Targets Selected

### 1. go/github.com/quic-go/quic-go
**Rationale:** Dominant pure-Go QUIC implementation; counterpart to rust/quinn (already mapped). 1,603 pkg.go.dev importers. Prior passes had covered nats-server and go-redis; this fills the QUIC ecosystem gap.

### 2. rust/parking_lot
**Rationale:** 1B+ total crates.io downloads; foundational synchronization crate used by Tokio, Rayon, Diesel. Under-explored vs. its ecosystem centrality. RustSec advisory confirmed for lock_api sub-crate.

---

## URLs Consulted

### quic-go
- Advisory database search: `mcp__github__search_code` with query `"github.com/quic-go/quic-go" repo:github/advisory-database path:advisories/github-reviewed` → 10 results (2 excluded as advisories for downstream packages mentioning quic-go, not for the module directly)
- GHSA-3q6m-v84f-6p9h: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/10/GHSA-3q6m-v84f-6p9h/GHSA-3q6m-v84f-6p9h.json
- GHSA-ppxx-5m9h-6vxf: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/01/GHSA-ppxx-5m9h-6vxf/GHSA-ppxx-5m9h-6vxf.json
- GHSA-c33x-xqrf-c478: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/04/GHSA-c33x-xqrf-c478/GHSA-c33x-xqrf-c478.json
- GHSA-px8v-pp82-rcvr: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/12/GHSA-px8v-pp82-rcvr/GHSA-px8v-pp82-rcvr.json
- GHSA-j972-j939-p2v3: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/06/GHSA-j972-j939-p2v3/GHSA-j972-j939-p2v3.json
- GHSA-47m2-4cr7-mhcw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/10/GHSA-47m2-4cr7-mhcw/GHSA-47m2-4cr7-mhcw.json
- GHSA-g754-hx8w-x2g6: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/12/GHSA-g754-hx8w-x2g6/GHSA-g754-hx8w-x2g6.json
- GHSA-vvgj-x9jq-8cj9: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/06/GHSA-vvgj-x9jq-8cj9/GHSA-vvgj-x9jq-8cj9.json
- pkg.go.dev stats: https://pkg.go.dev/github.com/quic-go/quic-go

**Excluded (downstream consumers, not quic-go module):**
- GHSA-876p-8259-xjgg → go-libp2p RSA key exhaustion (mentions quic-go in description)
- GHSA-cvx7-x8pj-x2gw → CoreDNS DoQ stream exhaustion (mentions quic-go as QUIC substrate)

### parking_lot / lock_api
- RustSec search: `mcp__github__search_code` with query `lock_api repo:rustsec/advisory-db path:crates` → RUSTSEC-2020-0070
- RUSTSEC-2020-0070: https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/lock_api/RUSTSEC-2020-0070.md
- GHSA-hj9h-wrgg-hgmx: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/08/GHSA-hj9h-wrgg-hgmx/GHSA-hj9h-wrgg-hgmx.json
- GHSA-ppj3-7jw3-8vc4: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/08/GHSA-ppj3-7jw3-8vc4/GHSA-ppj3-7jw3-8vc4.json
- GHSA-gmv4-vmx3-x9f3: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/08/GHSA-gmv4-vmx3-x9f3/GHSA-gmv4-vmx3-x9f3.json
- GHSA-vh4p-6j7g-f4j9: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/08/GHSA-vh4p-6j7g-f4j9/GHSA-vh4p-6j7g-f4j9.json
- GHSA-5wg8-7c9q-794v: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/08/GHSA-5wg8-7c9q-794v/GHSA-5wg8-7c9q-794v.json
- crates.io API (parking_lot): https://crates.io/api/v1/crates/parking_lot
- crates.io API (lock_api): https://crates.io/api/v1/crates/lock_api

### StackExchange.Redis (investigated, not written)
- `mcp__github__search_code` with `StackExchange.Redis repo:github/advisory-database language:JSON path:advisories/github-reviewed` → 1 result: GHSA-j8rm-cm55-qqj6 (for Microsoft.AspNetCore.SignalR.StackExchangeRedis / SignalR backplane, not the core StackExchange.Redis NuGet package). Excluded; StackExchange.Redis itself has no confirmed public security advisories in the GitHub advisory database at time of review.

---

## Methodology Notes

- OSV.dev API returned HTTP 403; fallback to github/advisory-database via WebFetch on raw.githubusercontent.com used exclusively.
- Broader advisory search (`quic-go GHSA repo:github/advisory-database`) returned 19 results; targeted search (`"github.com/quic-go/quic-go"`) narrowed to 10 direct. Two of those 10 were confirmed as downstream packages by fetching advisory content.
- No advisories fabricated; every row cites a primary GHSA source.
- parking_lot "parking_lot" crate name returned 0 advisory results from broader search; lock_api search confirmed RUSTSEC-2020-0070 as the sole advisory.
