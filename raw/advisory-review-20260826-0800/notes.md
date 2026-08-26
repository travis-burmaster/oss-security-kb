# Advisory Review — 2026-08-26 08:00 UTC

## Targets selected
1. `k8s.io/client-go` (Go) — Kubernetes official Go client library; no existing page; extremely high ecosystem usage (de facto standard for all Go-based Kubernetes tooling)
2. `github.com/aws/aws-sdk-go` (Go) — AWS SDK for Go v1; no existing page; high usage; EOL as of 2025-07-31

## Sources consulted

### k8s.io/client-go
- GHSA-jmrx-5g74-6v2f (CVE-2019-11250): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-jmrx-5g74-6v2f/GHSA-jmrx-5g74-6v2f.json
- GHSA-2575-pghm-6qqx (CVE-2019-11244): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/02/GHSA-2575-pghm-6qqx/GHSA-2575-pghm-6qqx.json
- GHSA-8cfg-vx93-jvxw (CVE-2020-8565): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/02/GHSA-8cfg-vx93-jvxw/GHSA-8cfg-vx93-jvxw.json
- GitHub repository metadata: https://api.github.com/repos/kubernetes/client-go
- Kubernetes security disclosure policy: https://kubernetes.io/docs/reference/issues-security/security/

### github.com/aws/aws-sdk-go
- GHSA-f5pg-7wfw-84q9 (CVE-2020-8911): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/02/GHSA-f5pg-7wfw-84q9/GHSA-f5pg-7wfw-84q9.json
- GHSA-7f33-f4f5-xwgw (CVE-2020-8912): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/02/GHSA-7f33-f4f5-xwgw/GHSA-7f33-f4f5-xwgw.json
- GHSA-6jvc-q2x7-pchv (CVE-2022-2582): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/12/GHSA-6jvc-q2x7-pchv/GHSA-6jvc-q2x7-pchv.json
- GHSA-76wf-9vgp-pj7w: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/02/GHSA-76wf-9vgp-pj7w/GHSA-76wf-9vgp-pj7w.json (WITHDRAWN — excluded as duplicate)
- GHSA-xmrv-pmrh-hhx2 (aws-sdk-go-v2 EventStream DoS, 2026): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/04/GHSA-xmrv-pmrh-hhx2/GHSA-xmrv-pmrh-hhx2.json (mentioned in posture notes only; affects v2 module, not v1)
- GitHub repository metadata: https://api.github.com/repos/aws/aws-sdk-go
- AWS vulnerability reporting: https://aws.amazon.com/security/vulnerability-reporting/

## Decisions and notes
- mcp__github__search_code used to enumerate all reviewed GHSA advisories for each package before fetching individual files
- GHSA-xcq4-m2r3-cmrj (Trivy scanner) appeared in aws-sdk-go search results but is for github.com/aquasecurity/trivy, not the AWS SDK — excluded
- GHSA-76wf-9vgp-pj7w excluded (WITHDRAWN, duplicate of GHSA-6jvc-q2x7-pchv per advisory database)
- Weekly download counts for both packages not available from pkg.go.dev in a machine-readable form; marked "unknown (high)"
- aws-sdk-go v1 archived status confirmed via GitHub API (archived: true, pushed_at: 2025-07-31)
