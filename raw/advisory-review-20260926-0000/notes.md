# Advisory Review — 2026-09-26

## Pass summary

Targets: `rust/ammonia` (new), `dotnet/Microsoft.AspNetCore.SignalR` (new)  
Also backfilled wiki/index.md missing entries from prior passes.

---

## rust/ammonia

**Crate:** ammonia  
**Registry:** crates.io  
**Downloads:** ~4.4M/week, ~16.7M total (crates.io API, 2026-09-26)  
**Latest stable:** 4.2.0  
**Repository:** https://github.com/rust-ammonia/ammonia

### URLs consulted

- https://crates.io/api/v1/crates/ammonia (download stats, latest version)
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/ammonia/RUSTSEC-2019-0001.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/ammonia/RUSTSEC-2021-0074.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/ammonia/RUSTSEC-2022-0003.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/ammonia/RUSTSEC-2025-0071.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/ammonia/RUSTSEC-2026-0193.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/ammonia/RUSTSEC-2026-0213.md
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/09/GHSA-mm7x-qfjj-5g2c/GHSA-mm7x-qfjj-5g2c.json
- mcp__github__search_code: `ammonia repo:rustsec/advisory-db path:crates` → 6 results
- mcp__github__search_code: `ammonia repo:github/advisory-database path:advisories` → 4 results (GHSA-p2g9-94wh-65c2, GHSA-5hp8-35wj-m525, GHSA-5325-xw5m-phm3, GHSA-mm7x-qfjj-5g2c)

### Advisories confirmed

| ID | CVE | Description | Fixed |
|----|-----|-------------|-------|
| RUSTSEC-2019-0001 | CVE-2019-15542 | Stack overflow via deeply-nested HTML (recursive serializer) | ≥ 2.1.0 |
| RUSTSEC-2021-0074 | CVE-2021-38193 | Mutation XSS — namespace-incompatible raw-text elements in SVG/MathML | ≥ 2.1.3 / ≥ 3.1.0 |
| RUSTSEC-2022-0003 | — (GHSA-p2g9-94wh-65c2) | Form-feed char injection in `clean_text` for unquoted HTML attributes | ≥ 3.1.3 |
| RUSTSEC-2025-0071 | — (GHSA-mm7x-qfjj-5g2c, Low CVSS 4.0) | Mutation XSS — namespace-incompatible tags when SVG/MathML + raw-text elements | ≥ 3.3.1 / ≥ 4.0.1 / ≥ 4.1.2 |
| RUSTSEC-2026-0193 | CVE-2026-63430 | Mutation XSS — math+annotation-xml + encoding disabled | ≥ 3.3.2 / ≥ 4.0.2 / ≥ 4.1.3 |
| RUSTSEC-2026-0213 | — | XSS — SVG animate/set attributeName filter bypass | ≥ 3.3.3 / ≥ 4.0.3 / ≥ 4.1.4 |

Note: GHSA-5hp8-35wj-m525 and GHSA-5325-xw5m-phm3 were found in the GHSA search but not individually fetched — likely mirrors of RUSTSEC-2021-0074 (both filed August 2021). Not separately mapped to avoid double-counting without confirmation.

---

## dotnet/Microsoft.AspNetCore.SignalR

**Package:** Microsoft.AspNetCore.SignalR  
**Registry:** NuGet  
**Downloads:** unknown (NuGet registration feed does not expose download counts)  
**Latest stable:** 1.2.13 (September 2026)  
**Repository:** https://github.com/dotnet/aspnetcore  
**Security policy:** https://github.com/dotnet/aspnetcore/security/policy

### URLs consulted

- https://api.nuget.org/v3/registration5-gz-semver2/microsoft.aspnetcore.signalr/index.json (latest version, no download count available)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-4jxx-4qxw-prxm/GHSA-4jxx-4qxw-prxm.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/08/GHSA-j8rm-cm55-qqj6/GHSA-j8rm-cm55-qqj6.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/02/GHSA-g74q-5xw3-j7q9/GHSA-g74q-5xw3-j7q9.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-4vgm-c2wm-63mw/GHSA-4vgm-c2wm-63mw.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/07/GHSA-j8gr-8fp3-5q5h/GHSA-j8gr-8fp3-5q5h.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/06/GHSA-f8h2-vmm9-qhj6/GHSA-f8h2-vmm9-qhj6.json
- mcp__github__search_code: `SignalR NuGet repo:github/advisory-database path:advisories` → 6 results

### Advisories confirmed

| GHSA | CVE | Severity | Package | Description | Fixed |
|------|-----|----------|---------|-------------|-------|
| GHSA-4jxx-4qxw-prxm | CVE-2019-0982 | High 7.5 AV:N | ...Protocols.MessagePack 1.0.x/1.1.x | DoS via improper request handling | 1.0.11/1.1.5 |
| GHSA-j8rm-cm55-qqj6 | CVE-2023-35391 | High 7.5 AV:L | ...StackExchangeRedis / ...Redis | Info disclosure via Redis backplane | 7.0.10/6.0.21/1.0.40 |
| GHSA-g74q-5xw3-j7q9 | CVE-2024-21386 | High 7.5 AV:N | App.Runtime | DoS via malicious client | .NET 8.0.2/7.0.16/6.0.27 |
| GHSA-4vgm-c2wm-63mw | CVE-2026-26130 | High 7.5 AV:N | App.Runtime | DoS via uncontrolled resource (CWE-770) | .NET 10.0.4/9.0.14/8.0.25 |
| GHSA-j8gr-8fp3-5q5h | CVE-2026-56170 | High 7.5 AV:N | App.Runtime | DoS via stateful reconnect (CWE-770) | .NET 10.0.6/9.0.15/8.0.26 |
| GHSA-f8h2-vmm9-qhj6 | CVE-2026-45591 | High CWE-400/787 | ...Protocols.MessagePack | Stack overflow DoS via nested MessagePack | .NET 10.0.9/9.0.17/8.0.28 |

Note: GHSA-4vgm-c2wm-63mw (CVE-2026-26130) describes a general "ASP.NET Core" resource-consumption DoS. Root cause not confirmed as SignalR-specific from public advisory text; included here because it was returned in the SignalR-focused GHSA search.

---

## Sources not consulted

- OSV.dev API (https://api.osv.dev) — blocked HTTP 403 per CLAUDE.md
- formulae.brew.sh — blocked by network egress proxy
