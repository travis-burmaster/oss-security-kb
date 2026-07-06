# Advisory Review Evidence — 2026-07-06 00:00 UTC

## Targets

| Package | Ecosystem | Page |
|---------|-----------|------|
| github.com/moby/moby | Go | wiki/go/github.com/moby/moby.md |
| tower-http | Rust / crates.io | wiki/rust/tower-http.md |

## Sources Consulted

### moby/moby (Go)

- https://github.com/moby/moby/security/advisories — GitHub security advisories page (paginated HTML, page 1 and page 2); enumerated all published advisories 2021–2026
- https://github.com/advisories/GHSA-3fwx-pjgw-3558 — CVE-2021-41091 data directory permissions
- https://github.com/advisories/GHSA-xmmx-7jpf-fx42 — CVE-2021-41190 OCI manifest ambiguity
- https://github.com/advisories/GHSA-2mm7-x5h6-5pvq — CVE-2022-24769 non-empty inheritable capabilities
- https://github.com/advisories/GHSA-rc4r-wh2q-q6c4 — CVE-2022-36109 supplementary group bypass
- https://github.com/advisories/GHSA-vp35-85q5-9f25 — build leaks host paths via git CVE-2022-39253
- https://github.com/advisories/GHSA-232p-vwff-86mp — CVE-2023-28840 Swarm overlay unauthenticated (xt_u32)
- https://github.com/advisories/GHSA-33pg-m6jh-5237 — CVE-2023-28841 Swarm overlay unencrypted RHEL 9+
- https://github.com/advisories/GHSA-6wrf-mxfj-pf5p — CVE-2023-28842 Swarm single-endpoint unauthenticated
- https://github.com/advisories/GHSA-vwm3-crmr-xfxw — VXLAN port exposure documentation advisory
- https://github.com/advisories/GHSA-jq35-85cj-fj4p — /sys/powercap accessible to containers
- https://github.com/advisories/GHSA-mq39-4gv4-mvpx — CVE-2024-29018 DNS from internal networks leak
- https://github.com/advisories/GHSA-xw73-rw38-6vjc — CVE-2024-24557 classic builder cache poisoning
- https://github.com/advisories/GHSA-x84c-p2g9-rqv9 — CVE-2024-32473 IPv6 on IPv4-only interfaces
- https://github.com/advisories/GHSA-v23v-6jw2-98fq — CVE-2024-41110 AuthZ plugin bypass regression (Critical CVSS 9.9)
- https://github.com/advisories/GHSA-4vq8-7jfc-9cvp — CVE-2025-54410 firewalld bridge isolation loss
- https://github.com/advisories/GHSA-x4rx-4gw3-53p4 — CVE-2025-54388 firewalld published ports exposed
- https://github.com/advisories/GHSA-pxq6-2prw-chj9 — CVE-2026-33997 plugin privilege off-by-one
- https://github.com/advisories/GHSA-x744-4wpc-v9h2 — CVE-2026-34040 AuthZ oversized-request bypass (incomplete fix)
- https://github.com/advisories/GHSA-vp62-88p7-qqf5 — CVE-2026-41568 docker cp empty file race
- https://github.com/advisories/GHSA-x86f-5xw2-fm2r — CVE-2026-41567 PUT /archive executes container binary
- https://github.com/advisories/GHSA-rg2x-37c3-w2rh — CVE-2026-42306 docker cp bind mount race
- https://pkg.go.dev/github.com/moby/moby — pkg.go.dev module page; confirmed 5 active GO-2026-* vulnerabilities (GO-2026-4883, GO-2026-4887, GO-2026-5617, GO-2026-5668, GO-2026-5746)
- https://github.com/moby/moby/blob/master/SECURITY.md — moby security policy

### tower-http (Rust / crates.io)

- https://rustsec.org/advisories/RUSTSEC-2022-0043.html — canonical GHSA-aliased ServeDir Windows path traversal advisory
- https://rustsec.org/advisories/RUSTSEC-2021-0135.html — predecessor duplicate record for same flaw
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/tower-http/RUSTSEC-2022-0043.toml — TOML source via GitHub
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/tower-http/RUSTSEC-2021-0135.toml — TOML source via GitHub
- https://github.com/tower-rs/tower-http/pull/204 — upstream fix PR referenced by both advisories
- https://crates.io/api/v1/crates/tower-http — crates.io API for download counts and version metadata
- https://github.com/tower-rs/tower-http/security — confirmed "no published security advisories" on GitHub; both advisories filed via RustSec directly

## API Blockers

- `https://api.osv.dev` — HTTP 403 (blocked by environment network policy); all advisory data sourced via GitHub and rustsec/advisory-db instead.

## Advisory Counts

| Package | Advisories Mapped | Severity Highlights |
|---------|-------------------|---------------------|
| moby/moby | 21 | 1 Critical (CVSS 9.9), 4 High, 11 Moderate, 3 Low, 2 High |
| tower-http | 2 (same flaw) | 2 Moderate (Windows-only file-disclosure) |
| **Total** | **23** | |

## Pages Updated

| File | Change |
|------|--------|
| wiki/go/github.com/moby/moby.md | New page (21 advisory rows) |
| wiki/rust/tower-http.md | New page (2 advisory rows) |
| wiki/go/index.md | Added moby/moby entry (19→20 pages) |
| wiki/rust/index.md | Added tower-http entry (19→20 pages) |
| wiki/index.md | Count 207→209, date updated, Rust+Go counts updated |
| wiki/log.md | Prepended [2026-07-06] entry |
