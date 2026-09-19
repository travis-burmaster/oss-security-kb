# Advisory Review Pass — 2026-09-19 08:30 UTC

## Targets
- kubernetes/kube-controller-manager (new, advisory-mapped)
- dotnet/StackExchange.Redis (new, baseline stub)

## Sources Consulted

### kube-controller-manager
- GitHub Advisory Database search: `mcp__github__search_code` with query `kube-controller-manager repo:github/advisory-database`
- GHSA-x6mj-w4jf-jmgw (CVE-2020-8555): https://github.com/advisories/GHSA-x6mj-w4jf-jmgw
- GHSA-5x96-j797-5qqw (CVE-2020-8566): https://github.com/advisories/GHSA-5x96-j797-5qqw
- GHSA-h7wq-jj8r-qm7p (CVE-2024-0793): https://github.com/advisories/GHSA-h7wq-jj8r-qm7p
- GHSA-r6j8-c6r2-37rr (CVE-2025-13281): https://github.com/advisories/GHSA-r6j8-c6r2-37rr
- Kubernetes security disclosure policy: https://kubernetes.io/docs/reference/issues-security/security/
- Kubernetes GitHub repository: https://github.com/kubernetes/kubernetes

### StackExchange.Redis
- GitHub Advisory Database search: `mcp__github__search_code` with query `StackExchange.Redis NuGet repo:github/advisory-database` — 0 results
- NuGet registry API: azuresearch-usnc.nuget.org blocked by proxy; download stats unavailable
- GitHub repository: https://github.com/StackExchange/StackExchange.Redis
- Redis vulnerability disclosure: https://redis.io/redis-responsible-vulnerability-disclosure/

## Methodology Notes
- OSV.dev API blocked (HTTP 403) — not used
- NuGet total download stats unavailable (azuresearch-usnc.nuget.org blocked)
- kubernetes.io domain blocked by egress proxy for some paths; GitHub advisory database used as primary source
- CVSS scores for KCM advisories confirmed via GitHub advisory pages
- GHSA-x6mj-w4jf-jmgw CVSS 6.3 confirmed (AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N)
- GHSA-r6j8-c6r2-37rr CVSS 6.5 confirmed (Moderate)

## Advisories Mapped
- kubernetes/kube-controller-manager: 4 advisories (CVE-2020-8555, CVE-2020-8566, CVE-2024-0793, CVE-2025-13281)
- dotnet/StackExchange.Redis: 0 advisories (baseline stub)
