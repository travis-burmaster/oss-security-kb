# k8s.io/client-go (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (high; de facto standard Go client for Kubernetes; ~9,868 GitHub stars; used by virtually every Go-based operator, controller, CLI tool, and integration)
**Repository:** https://github.com/kubernetes/client-go
**Security Contact:** security@kubernetes.io
**Disclosure Policy:** https://kubernetes.io/docs/reference/issues-security/security/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-08-26 | oss-security-kb pass | public advisory database | advisory-mapping | 3 GHSA advisories mapped | [GHSA search](https://github.com/advisories?query=k8s.io%2Fclient-go) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-11250 / GHSA-jmrx-5g74-6v2f | Moderate (CVSS 6.5 AV:N/AC:L/PR:L/UI:N) | Bearer tokens and Basic Auth credentials written to application logs at verbosity level 7 or higher; anyone with access to logs can extract credentials | k8s.io/client-go 0.17.0 / k8s.io/kubernetes 1.16.0-beta.1 | [GHSA-jmrx-5g74-6v2f](https://github.com/advisories/GHSA-jmrx-5g74-6v2f) |
| CVE-2019-11244 / GHSA-2575-pghm-6qqx | Moderate (CVSS AV:L/AC:L/PR:L/UI:R) | Schema info cached by kubectl in `~/.kube/http-cache` (or `--cache-dir`) written with world-writable permissions (rw-rw-rw-); other local users can tamper with cached files to disrupt kubectl operations | k8s.io/client-go 1.12.9 | [GHSA-2575-pghm-6qqx](https://github.com/advisories/GHSA-2575-pghm-6qqx) |
| CVE-2020-8565 / GHSA-8cfg-vx93-jvxw | Moderate (CVSS AV:L/AC:H/PR:L/UI:N) | Authorization and bearer tokens written to log files when verbosity level is 9 or higher; an incomplete fix for CVE-2019-11250 that raised the threshold but did not eliminate the exposure; affects both API server logs and kubectl output | k8s.io/client-go 0.17.16 / 0.18.14 / 0.19.6 / 0.20.0-alpha.2; k8s.io/kubernetes 1.20.0-alpha.2 | [GHSA-8cfg-vx93-jvxw](https://github.com/advisories/GHSA-8cfg-vx93-jvxw) |

## Security Posture Notes

`k8s.io/client-go` is the official Go client library for the Kubernetes API and is used by virtually every Go-based Kubernetes operator, controller, CLI tool, and platform integration (including kubectl itself). It provides authentication, API discovery, watch/list mechanics, typed and dynamic clients, and the informer/cache subsystem.

All three public advisories fall in the **credential-exposure via logging** category. CVE-2019-11250 and CVE-2020-8565 form an incomplete-fix chain: the first fix raised the credential-logging verbosity threshold from 7 to 9, but the exposure at level 9 was not eliminated until the second patch. CVE-2019-11244 is independent, concerning world-writable file permissions on the kubectl HTTP cache directory. All issues are fixed in releases corresponding to Kubernetes ≥ 1.12.9 / ≥ 1.17.0. Current releases (v0.3x.x, tracking Kubernetes 1.3x) are unaffected.

Kubernetes operates a coordinated disclosure program through its Product Security Committee. Vulnerabilities are reported to security@kubernetes.io with a 90-day disclosure policy. CVSSv3 vectors are published alongside each advisory. A security.md is maintained at https://github.com/kubernetes/kubernetes/blob/master/SECURITY.md.

## Dependencies of Note

- `k8s.io/apimachinery`, `k8s.io/api` — API type definitions bundled in the module
- `google.golang.org/grpc` (covered: [[go/google.golang.org/grpc]])
- `golang.org/x/net` (covered: [[go/golang.org-x-net]])

## Open Questions

- Have any third-party security audits of the client-go transport or auth sub-packages been published?
- Are there any advisories specific to the `dynamic`, `informer`, or `tools/cache` sub-packages?

## Related Pages

- [[go/go.etcd.io/etcd-v3]]
- [[go/google.golang.org/grpc]]
- [[kubernetes/kube-apiserver]]
- [[go/index]]

---
*Last updated: 2026-08-26 | Sources: 3 GHSA advisories (github/advisory-database)*
