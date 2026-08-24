# Advisory Review — 2026-08-24 07:30 UTC

## Targets

### kubernetes/coredns
- github.com/coredns/coredns (Go / CNCF graduated / Kubernetes default DNS)
- Ecosystem: Kubernetes

### dotnet/Azure.Identity
- Azure.Identity (NuGet / Microsoft)
- Ecosystem: .NET / NuGet

## Sources Consulted

### CoreDNS advisories (github/advisory-database via WebFetch on raw.githubusercontent.com)

| GHSA | CVE | Status | Fetched |
|------|-----|--------|---------|
| GHSA-c9v3-4pv7-87pr | CVE-2026-26017 | github-reviewed | yes |
| GHSA-qhmp-q7xh-99rh | CVE-2026-33190 | github-reviewed | yes |
| GHSA-vp29-5652-4fw9 | CVE-2026-35579 | github-reviewed | yes |
| GHSA-h8mm-c463-wjq3 | CVE-2026-33489 | github-reviewed | yes |
| GHSA-63cw-r7xf-jmwr | CVE-2026-32936 | github-reviewed | yes |
| GHSA-2wpx-qpw2-g5h5 | CVE-2026-32934 | github-reviewed | yes |
| GHSA-h75p-j8xm-m278 | CVE-2026-26018 | github-reviewed | yes |
| GHSA-cvx7-x8pj-x2gw | CVE-2025-47950 | github-reviewed | yes |
| GHSA-hfmw-7g3m-gj6q | CVE-2023-28452 | github-reviewed | yes |
| GHSA-527x-5wrf-22m2 | CVE-2025-68151 | github-reviewed | yes |
| GHSA-m9w6-wp3h-vq8g | CVE-2024-0874  | github-reviewed | yes |
| GHSA-h828-v5pv-33qx | CVE-2022-2837  | github-reviewed | yes |
| GHSA-ch7v-37xg-75ph | CVE-2022-2835  | github-reviewed | yes |
| GHSA-h92q-fgpp-qhrq | CVE-2023-30464 | github-reviewed | yes |
| GHSA-gv9j-4w24-q7vx | CVE-2019-19794 | github-reviewed | yes |
| GHSA-hw5w-qhp3-88f5 | —              | unreviewed (2023/03) | not fetched — skipped per methodology (unreviewed) |
| GHSA-44r7-7p62-q3fr | —              | github-reviewed | not fetched — already covered in go/github.com/miekg/dns page (upstream miekg/dns issue) |
| GHSA-93mf-426m-g6x9 | —              | github-reviewed (2025/09) | not fetched — flagged for future pass |

Total CoreDNS advisories confirmed and mapped: 15

### Azure.Identity advisories (github/advisory-database via WebFetch)

| GHSA | CVE | Status | Fetched |
|------|-----|--------|---------|
| GHSA-5mfx-4wcx-rv27 | CVE-2023-36414 | github-reviewed | yes |
| GHSA-wvxc-855f-jvrv | CVE-2024-29992 | github-reviewed | yes |
| GHSA-m5vv-6r4h-3vj9 | CVE-2024-35255 | github-reviewed | yes |

Total Azure.Identity advisories confirmed and mapped: 3

### Metadata sources

- CoreDNS GitHub: https://github.com/coredns/coredns (star count, CNCF status, security contact)
- CoreDNS security policy: https://github.com/coredns/coredns/security/policy
- NuGet API: https://api.nuget.org/v3/registration5-gz-semver2/azure.identity/index.json (partial)
- NuGet package page: https://www.nuget.org/packages/Azure.Identity (1.9B total downloads, 1.21.0 latest stable)
- Azure.Identity CHANGELOG: https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/identity/Azure.Identity/CHANGELOG.md#1102-2023-10-10
- MSRC advisory: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36414

## OSV.dev
Blocked (HTTP 403) — no OSV data obtained.

## Notes
- CoreDNS GHSA-hw5w-qhp3-88f5 was returned by search but is marked unreviewed; skipped per methodology.
- GHSA-44r7-7p62-q3fr (miekg/dns predictable TXID) is the upstream root cause of CVE-2019-19794 in CoreDNS; already covered in go/github.com/miekg/dns page.
- GHSA-93mf-426m-g6x9 (2025/09) not fetched — flagged as open question for a future pass.
- Azure.Identity CVE-2023-36414 CVSS vector (AV:N/AC:L/PR:L) produces 8.8 High by CVSS 3.1 calculator; advisory raw field may state 9.8 but the MSRC advisory page is the canonical source.
