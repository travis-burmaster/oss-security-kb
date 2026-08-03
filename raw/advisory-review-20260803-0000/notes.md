# Advisory Review — 2026-08-03

**Pass targets:** linux/vim, dotnet/Duende.IdentityServer  
**Ecosystems:** Linux (system packages), .NET / NuGet  
**Date:** 2026-08-03  
**OSV.dev:** blocked (HTTP 403) — not used  

---

## URLs Consulted

### GitHub Advisory Database searches (mcp__github__search_code)

- `vim repo:github/advisory-database path:advisories` → 788 total results
- `"github.com/vim/vim" OR "vim/vim" repo:github/advisory-database path:advisories` → 174 confirmed vim/vim-specific results
- `Duende IdentityServer repo:github/advisory-database path:advisories/github-reviewed` → 3 results (GHSA-ff4q-64jc-gx98, GHSA-55p7-v223-x366, GHSA-v9xq-2mvm-x8xc)
- `Dapper repo:github/advisory-database path:advisories` → 2 results (unrelated: @dapperduckling/keycloak-connector-server XSS; DapperDesk 2005 PHP SQL injection — neither is the .NET Dapper ORM; target dropped)

### Advisory JSON files fetched (raw.githubusercontent.com)

**vim advisories:**
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/07/GHSA-8c77-jprp-cxfj/GHSA-8c77-jprp-cxfj.json — CVE-2022-2284 heap OOB (High)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/08/GHSA-qqpf-7vhq-8phw/GHSA-qqpf-7vhq-8phw.json — CVE-2022-2946 UAF (High)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2023/01/GHSA-hv9j-pr23-x4hf/GHSA-hv9j-pr23-x4hf.json — CVE-2023-0433 heap OOB (High)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/02/GHSA-qfh8-x72v-whwp/GHSA-qfh8-x72v-whwp.json — CVE-2022-0443 UAF (Critical)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/04/GHSA-jx5v-4rgm-j8mg/GHSA-jx5v-4rgm-j8mg.json — CVE-2004-1138 modeline exec (High)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/01/GHSA-72hg-72h4-39fg/GHSA-72hg-72h4-39fg.json — CVE-2022-0158 heap OOB (Moderate)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/01/GHSA-vq66-5g5m-5rgg/GHSA-vq66-5g5m-5rgg.json — CVE-2022-0351 before-buffer-start access (High)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/10/GHSA-vwcr-hcq5-36jr/GHSA-vwcr-hcq5-36jr.json — CVE-2022-3705 qf_update_buffer UAF (High)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2023/09/GHSA-424w-j4hf-8cgp/GHSA-424w-j4hf-8cgp.json — CVE-2023-4734 integer overflow (High)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/04/GHSA-pq29-2m6m-938v/GHSA-pq29-2m6m-938v.json — CVE-2022-1381 heap OOB skip_range (High)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2023/05/GHSA-6v7c-pq5w-2jwg/GHSA-6v7c-pq5w-2jwg.json — CVE-2023-2610 integer overflow (High)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2023/09/GHSA-ph6h-mvrc-7rq5/GHSA-ph6h-mvrc-7rq5.json — CVE-2023-4750 UAF (High)

**IdentityServer advisories:**
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/07/GHSA-ff4q-64jc-gx98/GHSA-ff4q-64jc-gx98.json — CVE-2024-39694 open redirect (Moderate)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/07/GHSA-55p7-v223-x366/GHSA-55p7-v223-x366.json — no CVE, IdentityServer4 EOL open redirect (Moderate)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/10/GHSA-v9xq-2mvm-x8xc/GHSA-v9xq-2mvm-x8xc.json — CVE-2024-49755 DPoP cnf claim validation (Low)

### NuGet download stats

- https://api.nuget.org/v3/flat2/duende.identityserver/index.json — current 8.0.4; ~26.3M total downloads
- https://api.nuget.org/v3/flat2/identityserver4/index.json — current 4.1.2 (EOL); ~67.8M total downloads

---

## Advisory count summary

| Page | New advisories mapped | Total GHSA scope |
|------|----------------------|------------------|
| linux/vim | 12 | 174+ (vim/vim repo) |
| dotnet/Duende.IdentityServer | 3 | 3 (all github-reviewed) |
