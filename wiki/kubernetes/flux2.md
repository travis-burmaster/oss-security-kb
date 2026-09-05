# Flux 2 (kubernetes)

**Registry:** k8s
**Weekly Downloads:** unknown (deployed as GitOps controller set, not a registry package)
**Repository:** https://github.com/fluxcd/flux2
**Security Contact:** security@fluxcd.io
**Disclosure Policy:** https://github.com/fluxcd/flux2/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-41254 / GHSA-35rf-v2jv-gfg7 | High CVSS 8.8 | kustomize-controller privilege escalation: malicious tenant embeds shell commands in Secrets linked to a Service Account referenced in a Kustomization; controller executes them at its own (cluster-admin-level) privileges | kustomize-controller v0.15.0 (flux2 v0.18.0) | [GHSA-35rf-v2jv-gfg7](https://github.com/advisories/GHSA-35rf-v2jv-gfg7) |
| CVE-2022-24817 / GHSA-vvmq-fwmg-2gjc | Critical CVSS 9.9 | Insufficient kubeconfig validation in kustomize-controller and helm-controller: kubeconfig files can embed `exec`-based token generators, enabling arbitrary code execution and privilege escalation in multi-tenant clusters | kustomize-controller v0.23.0, helm-controller v0.19.0, flux2 v0.29.0 | [GHSA-vvmq-fwmg-2gjc](https://github.com/advisories/GHSA-vvmq-fwmg-2gjc) |
| CVE-2022-24878 / GHSA-7pwf-jg34-hxwp | High CVSS 7.5 | Crafted `kustomization.yaml` triggers uncontrolled recursion (infinite loop) in kustomize-controller, causing DoS for all tenants sharing the controller | kustomize-controller v0.24.0 (flux2 v0.29.0) | [GHSA-7pwf-jg34-hxwp](https://github.com/advisories/GHSA-7pwf-jg34-hxwp) |
| CVE-2022-36035 / GHSA-xwf3-6rgv-939r | High CVSS 7.6 | Flux CLI path traversal: malicious applications sharing the shell environment can inject arbitrary content into Flux deployments targeting Kubernetes clusters | flux2 v0.32.0 | [GHSA-xwf3-6rgv-939r](https://github.com/advisories/GHSA-xwf3-6rgv-939r) |
| CVE-2022-36049 / GHSA-p2g7-xwvr-rrw3 | High CVSS 7.1 | Upstream Helm SDK flaw causes uncontrolled memory consumption in helm-controller, crashing the controller; exploitable by any tenant able to create or modify a HelmRelease resource | helm-controller v0.23.0 (flux2 v0.32.0) | [GHSA-p2g7-xwvr-rrw3](https://github.com/advisories/GHSA-p2g7-xwvr-rrw3) |
| CVE-2022-39272 / GHSA-f4p5-x4vc-mh4v | Moderate | Invalid `metav1.Duration` values in `.spec.interval` or `.spec.timeout` stop an entire object type from being reconciled; exploitable by any user with write access to Flux resources | source-controller v0.30.0, kustomize-controller v0.29.0, helm-controller v0.24.0, notification-controller v0.27.0, image-automation-controller v0.26.0, image-reflector-controller v0.22.0; flux2 v0.35.0 | [GHSA-f4p5-x4vc-mh4v](https://github.com/advisories/GHSA-f4p5-x4vc-mh4v) |
| CVE-2024-31216 / GHSA-v554-xwgw-hc3w | Moderate | Azure Blob Storage SAS tokens logged in plaintext by source-controller on connection errors, leaking credentials to anyone with log access | source-controller v1.2.5 | [GHSA-v554-xwgw-hc3w](https://github.com/advisories/GHSA-v554-xwgw-hc3w) |
| CVE-2026-23990 / GHSA-4xh5-jcj2-ch8q | Moderate | Flux Operator Web UI impersonation bypass: CEL expressions that evaluate to empty strings cause impersonation headers to be omitted; requests execute under the operator service account, enabling privilege escalation for any authenticated user | Flux Operator v0.40.0 | [GHSA-4xh5-jcj2-ch8q](https://github.com/advisories/GHSA-4xh5-jcj2-ch8q) |
| CVE-2026-40109 / GHSA-h9cx-xjg6-5v2w | Low CVSS 4.2 | notification-controller GCR Receiver does not validate the `email` claim in Google OIDC tokens for Pub/Sub push authentication, allowing unauthorized reconciliation triggering | notification-controller v1.8.3 | [GHSA-h9cx-xjg6-5v2w](https://github.com/advisories/GHSA-h9cx-xjg6-5v2w) |
| CVE-2026-47680 / GHSA-jjrm-hr5f-673x | Moderate | source-controller path traversal: Bucket resource allows writes outside the working directory; GitRepository sparse-checkout allows path enumeration on the controller pod | source-controller v1.8.5 | [GHSA-jjrm-hr5f-673x](https://github.com/advisories/GHSA-jjrm-hr5f-673x) |

## Security Posture Notes

CNCF-graduated GitOps continuous delivery platform for Kubernetes (8,383 GitHub stars; latest v2.9.5 released 2026-08-31). Flux 2 is a collection of independently released Go controllers — source-controller, kustomize-controller, helm-controller, notification-controller, image-automation-controller, and image-reflector-controller — bundled together in the flux2 meta-repository.

Prominent security themes:
- **Multi-tenant privilege escalation (2021–2022):** The Critical CVSS 9.9 kubeconfig exec-injection advisory (CVE-2022-24817) is the most severe on record. Combined with the kustomize-controller privilege escalation (CVE-2021-41254), these represent a significant multi-tenant threat surface in shared clusters where tenants have write access to Flux resources.
- **DoS via crafted resources:** Recurring pattern — kustomize-controller infinite loop (CVE-2022-24878), helm-controller Helm SDK memory exhaustion (CVE-2022-36049), and cross-controller invalid-Duration reconciliation halt (CVE-2022-39272).
- **Credential/secret leakage into logs:** Azure SAS token leak (CVE-2024-31216) is representative; log access should be considered a security boundary.

Security disclosures via security@fluxcd.io with published disclosure policy.

## Dependencies of Note

- Helm SDK — CVE-2022-36049 propagated from upstream Helm SDK memory-consumption flaw into helm-controller; see [[kubernetes/helm]]
- Kubernetes kustomize — CVE-2022-24878 recursion flaw propagated through kustomize-controller
- Flux Operator (by ControlPlane) — a separate product with overlapping advisory surface (CVE-2026-23990 / GHSA-4xh5-jcj2-ch8q)

## Open Questions

- Flux Operator is a distinct product from the fluxcd org's controllers; determine whether a separate `kubernetes/flux-operator` page is warranted for future passes
- image-automation-controller and image-reflector-controller GHSA records not individually mapped in this pass

## Related Pages

- [[kubernetes/argo-cd]]
- [[kubernetes/helm]]
- [[kubernetes/index]]

---
*Last updated: 2026-09-05 | Sources: 10 GHSA advisories (github/advisory-database)*
