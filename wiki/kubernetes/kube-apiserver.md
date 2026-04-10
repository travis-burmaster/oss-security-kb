# kube-apiserver (kubernetes)

**Registry:** k8s
**Weekly Downloads:** unknown (as of 2026-04-10)
**Repository:** https://github.com/kubernetes/kubernetes
**Security Contact:** https://github.com/kubernetes/committee-security-response#contacting-the-src
**Disclosure Policy:** https://kubernetes.io/security/
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| Review pending | — | This page has not yet been populated with component-specific advisory history. Start with the Kubernetes official CVE feed, SRC disclosures, and upstream issue history. | — | https://kubernetes.io/docs/reference/issues-security/official-cve-feed/ |

*Official Kubernetes CVE feed: https://kubernetes.io/docs/reference/issues-security/official-cve-feed/*

## Security Posture Notes

- `kube-apiserver` is one of the highest-value pages the KB can grow because it is the control-plane request gateway for authentication, authorization, admission, API object validation, and persistence flows.
- The upstream Kubernetes project publishes a formal security process and dedicated Security Response Committee contact path, which gives this page a strong disclosure anchor even before advisory curation is filled in.
- Vulnerability history here will need careful scoping because many Kubernetes advisories span multiple components or configuration assumptions rather than a single binary.

## Dependencies of Note

- `etcd` is a closely related follow-on page because storage-layer bugs and access-control assumptions often intersect with API-server risk.
- Admission webhooks, aggregated APIs, and authn/authz integrations are likely future cross-links once the KB has more Kubernetes coverage.

## Open Questions

- Which published Kubernetes CVEs primarily affect `kube-apiserver` versus broader cluster configuration or adjacent components?
- Are there public component-focused audits of request decoding, admission control, or impersonation / authorization paths?
- Should future pages track default deployment hardening guidance separately from software vulnerability history?

## Related Pages

- [[kubernetes/index]]

---
*Last updated: 2026-04-10 | Sources: 3 (upstream repository, SECURITY_CONTACTS, Kubernetes security / CVE feed documentation)*
