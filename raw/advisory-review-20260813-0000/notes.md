# Advisory Review Pass — 2026-08-13

## Targets
- `go/github.com/open-policy-agent/opa` (new page)
- `dotnet/log4net` (new page)

## Sources consulted

### OPA (go/github.com/open-policy-agent/opa)

**Discovery:**
- mcp__github__search_code: query `open-policy-agent/opa repo:github/advisory-database path:advisories` → 7 results

**Advisories fetched:**
1. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/02/GHSA-hcw3-j74m-qc58/GHSA-hcw3-j74m-qc58.json
   — CVE-2022-23628, Moderate CVSS 5.4, AST pretty-print reorders arrays, fixed 0.37.2
2. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-x7f3-62pm-9p38/GHSA-x7f3-62pm-9p38.json
   — CVE-2022-28946, High CVSS 7.5, OOB in ast/parser.go, fixed 0.40.0
3. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/07/GHSA-2m4x-4q9j-w97g/GHSA-2m4x-4q9j-w97g.json
   — CVE-2022-33082, High, AST compiler DoS, fixed 0.42.0
4. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/09/GHSA-f524-rf33-2jjr/GHSA-f524-rf33-2jjr.json
   — CVE-2022-36085, High CVSS 7.1, WithUnsafeBuiltins bypass, fixed 0.43.1
5. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/08/GHSA-c77r-fh37-x2px/GHSA-c77r-fh37-x2px.json
   — CVE-2024-8260, Moderate, Windows SMB force-auth, fixed 0.68.0
6. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/05/GHSA-6m8w-jc87-6cr7/GHSA-6m8w-jc87-6cr7.json
   — CVE-2025-46569, High CVSS:4.0 7.3, Data API Rego injection, fixed 1.4.0
7. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/02/GHSA-9f29-v6mm-pw6w/GHSA-9f29-v6mm-pw6w.json
   — CVE-2026-26205, High (opa-envoy-plugin), double-slash path auth bypass, fixed 1.13.2-envoy-2

**Registry/metadata:**
- OPA GitHub stars/metadata retrieved via mcp__github__ tools: 12,097 stars, 1,649 forks, current v1.19.0
- pkg.go.dev: https://pkg.go.dev/github.com/open-policy-agent/opa — current v1.19.0 (2026-07-30), Apache-2.0, CNCF graduated
- Cure53 audit: https://github.com/open-policy-agent/opa/blob/main/SECURITY_AUDIT.pdf (confirmed present, full findings not individually mapped)
- SECURITY.md: https://github.com/open-policy-agent/opa/blob/main/SECURITY.md (confirmed present)

### log4net (dotnet/log4net)

**Discovery:**
- mcp__github__search_code: query `log4net repo:github/advisory-database path:advisories` → 5 results

**Advisories fetched:**
1. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/01/GHSA-2cwj-8chv-9pp9/GHSA-2cwj-8chv-9pp9.json
   — CVE-2018-1285, Critical CVSS 9.8, XXE in config parsing, fixed 2.0.10; CONFIRMED direct library advisory
2. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-f9fr-w54q-772h/GHSA-f9fr-w54q-772h.json
   — CVE-2006-0743, Moderate, format string in LocalSyslogAppender, fixed 1.2.10; CONFIRMED direct library advisory
3. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/04/GHSA-4f7c-pmjv-c25w/GHSA-4f7c-pmjv-c25w.json
   — CVE-2026-40021, Moderate CVSS 5.3, XML forbidden-char log suppression, fixed 3.3.0; CONFIRMED direct library advisory
4. https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2021/12/GHSA-6vh7-mxw3-7f49/GHSA-6vh7-mxw3-7f49.json
   — CVE-2021-44028, Moderate; DOWNSTREAM PRODUCT advisory (Quest KACE Desktop Authority); not mapped as direct log4net advisory
5. https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2023/12/GHSA-64fx-j998-rqp7/GHSA-64fx-j998-rqp7.json
   — CVE-2023-45253, High CVSS 9.1; DOWNSTREAM PRODUCT advisory (Huddly HuddlyCameraService); not mapped as direct log4net advisory

**Registry/metadata:**
- NuGet total downloads: 418M+ (via nuget.org/packages/log4net)
- Latest stable: 3.3.2 (2026-06-25) via NuGet flatcontainer API
- Repository: https://github.com/apache/logging-log4net
- Security contact: security@apache.org

## OSV.dev
API blocked (HTTP 403) — not consulted.

## Pages created
- wiki/go/github.com/open-policy-agent/opa.md
- wiki/dotnet/log4net.md

## Pages updated
- wiki/go/index.md (added OPA entry; count 24→25)
- wiki/dotnet/index.md (added log4net entry; count 11→12)
- wiki/index.md (Go 24→25; .NET 11→12; total 254→256; date updated)
- wiki/log.md (prepended new entry)
