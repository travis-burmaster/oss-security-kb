# Advisory Review — 2026-08-14 Pass Notes

**Date:** 2026-08-14  
**Ecosystems targeted:** Go (pkg.go.dev), .NET/NuGet  
**OSV.dev status:** Blocked (HTTP 403) — not used  
**Primary sources:** github/advisory-database (via mcp__github__search_code + WebFetch on raw.githubusercontent.com), nuget.org, GitHub repository metadata

---

## Target 1: go/github.com/lestrrat-go/jwx

**Rationale:** Under-covered Go ecosystem; JOSE/JWT libraries are high-security-relevance; similar library (go-jose/go-jose) already has 7 advisories mapped, making lestrrat-go/jwx a logical coverage gap.

**Advisory search query:** `lestrrat-go/jwx repo:github/advisory-database` via mcp__github__search_code  
**Results:** 4 total (GHSA-rm8v-mxj3-5rmq, GHSA-7f9x-gw85-8grf, GHSA-pvcr-v8j8-j5q3, GHSA-hj3v-m684-v259)  
**All 4 fetched individually via WebFetch on raw.githubusercontent.com paths**

### URLs consulted

- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/06/GHSA-rm8v-mxj3-5rmq/GHSA-rm8v-mxj3-5rmq.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/12/GHSA-7f9x-gw85-8grf/GHSA-7f9x-gw85-8grf.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/01/GHSA-pvcr-v8j8-j5q3/GHSA-pvcr-v8j8-j5q3.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/03/GHSA-hj3v-m684-v259/GHSA-hj3v-m684-v259.json
- https://pkg.go.dev/github.com/lestrrat-go/jwx/v2 (version and import count)
- https://api.github.com/repos/lestrrat-go/jwx (repo metadata — returned 403; used mcp__github__search_repositories instead)
- mcp__github__search_repositories query: `lestrrat-go/jwx` — returned repo: 2,414 stars, default_branch: `develop/v4`, updated_at: 2026-08-13, open_issues: 0

### Advisory mapping notes

| GHSA | CVE | Summary | Affected | Fixed |
|------|-----|---------|---------|-------|
| GHSA-rm8v-mxj3-5rmq | none | AES-CBC padding oracle timing attack | v1 ≤ 1.2.25, v2 ≤ 2.0.10 | v1.2.26 / v2.0.11 |
| GHSA-7f9x-gw85-8grf | CVE-2023-49290 | PBES2 p2c CPU exhaustion DoS | v1 ≤ 1.2.26, v2 ≤ 2.0.17 | v1.2.27 / v2.0.18 |
| GHSA-pvcr-v8j8-j5q3 | CVE-2024-21664 | JWS nil-pointer dereference DoS | v1 1.0.8–1.2.27, v2 ≤ 2.0.18 | v1.2.28 / v2.0.19 |
| GHSA-hj3v-m684-v259 | CVE-2024-28122 | JWE decompression bomb DoS | v1 ≤ 1.2.28, v2 ≤ 2.0.20 | v1.2.29 / v2.0.21 |

---

## Target 2: dotnet/Azure.Identity

**Rationale:** Under-covered .NET/NuGet ecosystem; Azure.Identity is the primary Azure SDK authentication library with 1.9B+ downloads and extremely high blast radius; not previously covered in the KB.

**Advisory search query:** `Azure.Identity repo:github/advisory-database` via mcp__github__search_code  
**Results:** 3 total (GHSA-5mfx-4wcx-rv27, GHSA-wvxc-855f-jvrv, GHSA-m5vv-6r4h-3vj9)  
**All 3 fetched individually via WebFetch on raw.githubusercontent.com paths**

### URLs consulted

- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/10/GHSA-5mfx-4wcx-rv27/GHSA-5mfx-4wcx-rv27.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/04/GHSA-wvxc-855f-jvrv/GHSA-wvxc-855f-jvrv.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/06/GHSA-m5vv-6r4h-3vj9/GHSA-m5vv-6r4h-3vj9.json
- https://www.nuget.org/packages/Azure.Identity (download stats: 1.9 billion total, latest stable 1.21.0, ~3.4M downloads/day)
- https://github.com/Azure/azure-sdk-for-net/blob/main/SECURITY.md (security contact)

### Advisory mapping notes

| GHSA | CVE | Severity | Summary | Fixed |
|------|-----|---------|---------|-------|
| GHSA-5mfx-4wcx-rv27 | CVE-2023-36414 | Critical CVSS 9.9 | Remote code execution | 1.10.2 |
| GHSA-wvxc-855f-jvrv | CVE-2024-29992 | Moderate CVSS 7.1 AV:L | Information disclosure (CWE-522) | 1.11.0 |
| GHSA-m5vv-6r4h-3vj9 | CVE-2024-35255 | Medium CVSS 6.2 AV:L | Cross-ecosystem EoP / info disclosure | 1.11.4 (NuGet) |

**Note on CVE-2024-35255 cross-ecosystem scope:** Also affects azure-identity (PyPI < 1.16.1), @azure/identity (npm < 4.2.1), com.azure:azure-identity (Maven < 1.12.2), azure-sdk-for-go (< 1.6.0-beta.4), Microsoft.Identity.Client (NuGet 4.49.1–4.60.3 and 4.61.0–4.61.2), @azure/msal-node (npm 2.7.0–2.9.1), com.microsoft.azure:msal4j (Maven 1.14.4-beta–1.15.0). Future passes should verify PyPI azure-identity coverage separately.

---

## Summary

- Pages added: 2 (go/github.com/lestrrat-go/jwx, dotnet/Azure.Identity)
- Advisory rows mapped: 7 (4 + 3)
- Sources consulted: github/advisory-database (7 GHSA records), nuget.org, mcp__github__search_repositories, pkg.go.dev
- No advisories invented or inferred; all rows linked to primary GHSA sources
