# cert-manager (Kubernetes)

**Registry:** k8s (Helm chart / container image)
**Weekly Downloads:** unknown (est. deployed in 60%+ of production Kubernetes clusters; 13,000+ GitHub stars)
**Repository:** https://github.com/cert-manager/cert-manager
**Security Contact:** security@cert-manager.io
**Disclosure Policy:** https://cert-manager.io/docs/contributing/security/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-12401 / GHSA-r4pg-vg54-wxx4 | Moderate (CVSS v3.1 5.9 / CVSS v4 4.0) | **PEM parsing CPU DoS.** Malformed PEM input causes `pem.Decode()` in the cert-manager controller to consume large amounts of CPU, denying service to the controller pod. An attacker with write access to a PEM-containing Secret can trigger this. Root cause is upstream Go bug golang/go#50116. Mitigation: strict RBAC limiting who can write PEM Secrets. | 1.12.14 / 1.15.4 / 1.16.2 | [GHSA-r4pg-vg54-wxx4](https://github.com/advisories/GHSA-r4pg-vg54-wxx4) |
| CVE-2026-25518 / GHSA-gx3x-vq4p-mhhv | Moderate (CVSS v3.1 AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H) | **DNS response controller panic DoS.** An attacker who can intercept DNS traffic or control an authoritative nameserver can inject a crafted DNS response (CWE-129 / CWE-704) triggering a panic in the cert-manager controller. Affects deployments using the DNS01 ACME challenge type only. Mitigation: DNS-over-HTTPS reduces interception risk but does not cover attacker-controlled authoritative servers. | 1.18.5 / 1.19.3 | [GHSA-gx3x-vq4p-mhhv](https://github.com/advisories/GHSA-gx3x-vq4p-mhhv) |
| CVE-2024-36537 / GHSA-9cfq-668r-pxhc | High (CVSS v3.1 7.2 AV:N/PR:H — unreviewed) | **Insecure service account token permissions in v1.14.4** (unreviewed advisory; sole reference is a GitHub Gist; no structured `affected` package data in the GHSA record; no fix version listed). Low confidence — included for completeness only. | none listed | [GHSA-9cfq-668r-pxhc](https://github.com/advisories/GHSA-9cfq-668r-pxhc) (unreviewed) |

## Security Posture Notes

cert-manager is the dominant Kubernetes certificate management solution supporting X.509 issuance via ACME/Let's Encrypt, Vault, Venafi, and self-signed CAs. It is a CNCF incubating project deployed in an estimated 60%+ of production Kubernetes clusters. The project maintains a public security disclosure policy at `https://cert-manager.io/docs/contributing/security/` with a dedicated security contact (`security@cert-manager.io`) and coordinates security releases under a 90-day responsible disclosure window.

The two confirmed reviewed advisories (CVE-2024-12401, CVE-2026-25518) are both controller-side DoS. Neither enables unauthorized certificate issuance or Secret exfiltration. CVE-2024-12401 requires write access to a PEM-containing Secret (mitigated by strict RBAC). CVE-2026-25518 requires DNS interception or control of an authoritative nameserver and only affects DNS01 challenge type deployments. GHSA-9cfq-668r-pxhc (unreviewed) has only a Gist as its primary source and should be treated with caution until independently confirmed.

Current stable versions (≥ 1.18.5 / ≥ 1.19.3) are unaffected by both confirmed reviewed advisories. Users on any 1.12.x / 1.13.x–1.15.x / 1.16.x maintenance stream should apply the respective patch releases for CVE-2024-12401.

cert-manager is written in Go and relies on `golang.org/x/crypto` and `golang.org/x/net`; see those pages for transitive exposure context.

## Dependencies of Note

- `golang.org/x/crypto` — SSH boundary and crypto history; see [[go/golang.org-x-crypto]]
- `golang.org/x/net` — HTTP/2 DoS and parser history; see [[go/golang.org-x-net]]
- CVE-2024-12401 root cause: upstream Go `encoding/pem` package (golang/go#50116); patched in cert-manager via `pem.Decode` wrapper

## Open Questions

- Whether any post-1.19.3 advisories have been published (pass date 2026-08-23); check `https://osv.dev/list?ecosystem=Go&q=cert-manager` on next pass.
- Whether GHSA-9cfq-668r-pxhc (CVE-2024-36537) is independently confirmed; currently unreviewed, sole reference is a Gist.
- ACME HTTP-01 challenge solver runs a temporary HTTP server — full attack surface not enumerated in public advisories.

## Related Pages

- [[kubernetes/ingress-nginx]]
- [[kubernetes/kube-apiserver]]
- [[kubernetes/index]]

---
*Last updated: 2026-08-23 | Sources: 3*
