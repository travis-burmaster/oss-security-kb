# Advisory Review Notes — 2026-06-20

## Targets Selected

1. **rust/ring** — crates.io cryptographic library (~134M weekly downloads); RUSTSEC-2025-0009 DoS advisory found
2. **dotnet/SixLabors.ImageSharp** — NuGet image processing library (~273M total downloads); 7 GHSA advisories found
3. **rust/regex** — crates.io regex engine (~183M weekly downloads); RUSTSEC-2022-0013 ReDoS advisory found

## Sources Consulted

### rustsec/advisory-db (via GitHub MCP code search + raw.githubusercontent.com)
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/ring/RUSTSEC-2025-0007.md (withdrawn maintenance hiatus)
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/ring/RUSTSEC-2025-0009.md (DoS — AES/QUIC overflow)
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/ring/RUSTSEC-2025-0010.md (informational — 0.16.x unmaintained)
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/regex/RUSTSEC-2022-0013.md (ReDoS / complexity limit)

### github/advisory-database (via raw.githubusercontent.com)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/03/GHSA-4p46-pwfr-66x6/GHSA-4p46-pwfr-66x6.json (ring CVE-2025-4432)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/03/GHSA-65x7-c272-7g7r/GHSA-65x7-c272-7g7r.json (ImageSharp CVE-2024-27929)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/04/GHSA-g85r-6x2q-45w7/GHSA-g85r-6x2q-45w7.json (ImageSharp CVE-2024-32035)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/04/GHSA-5x7m-6737-26cr/GHSA-5x7m-6737-26cr.json (ImageSharp CVE-2024-32036)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/07/GHSA-63p8-c4ww-9cg7/GHSA-63p8-c4ww-9cg7.json (ImageSharp CVE-2024-41131)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/07/GHSA-qxrv-gp6x-rc23/GHSA-qxrv-gp6x-rc23.json (ImageSharp CVE-2024-41132)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/03/GHSA-2cmq-823j-5qj8/GHSA-2cmq-823j-5qj8.json (ImageSharp CVE-2025-27598)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/07/GHSA-rxmq-m78w-7wmc/GHSA-rxmq-m78w-7wmc.json (ImageSharp CVE-2025-54575)

### Registry APIs
- https://crates.io/api/v1/crates/ring — total_downloads: 581,947,127; recent_downloads: 134,594,184; newest_version: 0.17.14
- https://crates.io/api/v1/crates/regex — total_downloads: 913,597,780; recent_downloads: 183,058,252; newest_version: 1.12.4
- https://www.nuget.org/packages/SixLabors.ImageSharp — total downloads: ~273.3M; latest version: 4.0.0
- https://api.nuget.org/v3/registration5-gz-semver2/sixlabors.imagesharp/index.json — version metadata

### Project Documentation
- https://github.com/briansmith/ring/blob/main/RELEASES.md — ring v0.17.12 security release notes
- https://www.rust-lang.org/policies/security — Rust Security Response WG policy (applies to regex)

## OSV.dev Status
OSV.dev API (https://api.osv.dev) returned HTTP 403 blocked by environment network policy. All advisory content sourced directly from rustsec/advisory-db and github/advisory-database.

## Findings Summary
- ring: 2 active advisories (RUSTSEC-2025-0009/CVE-2025-4432, RUSTSEC-2025-0010), 1 withdrawn (RUSTSEC-2025-0007)
- SixLabors.ImageSharp: 7 GHSA advisories (CVE-2024-27929, CVE-2024-32035, CVE-2024-32036, CVE-2024-41131, CVE-2024-41132, CVE-2025-27598, CVE-2025-54575)
- regex: 1 advisory (RUSTSEC-2022-0013/CVE-2022-24713)
- Total new vulnerability rows: 10 (2 ring + 7 ImageSharp + 1 regex)
- Packages ruled out: Dapper (NuGet) — no advisories found in github/advisory-database; NLog (NuGet) — no advisories found
