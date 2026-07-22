# ingress-nginx (Kubernetes)

**Registry:** Kubernetes / CNCF / k8s.io Go module
**Weekly Downloads:** N/A — deployed as a Kubernetes controller container; millions of cluster deployments via Helm chart (most widely used Kubernetes ingress controller)
**Repository:** https://github.com/kubernetes/ingress-nginx
**Security Contact:** security@kubernetes.io / https://github.com/kubernetes/ingress-nginx/security/advisories
**Disclosure Policy:** https://kubernetes.io/docs/reference/issues-security/security/ (coordinated via Kubernetes Security Response Committee)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-07-22 | OSS Security KB | GHSA database lookup | automated | 12 public advisories mapped (CVE-2021-25742 through CVE-2025-1974) | [github/advisory-database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-1974 / GHSA-mgvx-rpfc-9mpv | **Critical — CVSS 9.8** | **IngressNightmare — Unauthenticated RCE via admission webhook:** An unauthenticated attacker with pod-network access can send a crafted request to the ingress-nginx admission webhook and achieve arbitrary code execution in the ingress-nginx controller pod. The controller runs with a cluster-scoped serviceaccount token that can read all Secrets cluster-wide in the default installation, making successful exploitation equivalent to full cluster takeover. No authentication or cluster account is required. | 1.11.5 / 1.12.1 | [GHSA-mgvx-rpfc-9mpv](https://github.com/advisories/GHSA-mgvx-rpfc-9mpv) |
| CVE-2025-1098 / GHSA-vg63-w3p9-jc9m | **Critical — CVSS 9.9** | **IngressNightmare — mirror annotation config injection → RCE:** The `mirror-target` and `mirror-host` Ingress annotations are not sanitized before being inserted into the generated nginx configuration. Any user with Ingress create/update permission can inject arbitrary nginx directives, leading to code execution in the controller and cluster-wide Secret exposure. | 1.11.5 / 1.12.1 | [GHSA-vg63-w3p9-jc9m](https://github.com/advisories/GHSA-vg63-w3p9-jc9m) |
| CVE-2025-1097 / GHSA-823x-fv5p-h7hw | **Critical — CVSS 9.1** | **IngressNightmare — auth-tls-match-cn annotation config injection → RCE:** The `auth-tls-match-cn` Ingress annotation value is embedded in the nginx configuration without sanitization, allowing Ingress creators to inject arbitrary nginx directives, execute code in the controller context, and access cluster Secrets. | 1.11.5 / 1.12.1 | [GHSA-823x-fv5p-h7hw](https://github.com/advisories/GHSA-823x-fv5p-h7hw) |
| CVE-2025-24514 / GHSA-fwwp-xcxw-39vq | **Critical — CVSS 9.1** | **IngressNightmare — auth-url annotation config injection → RCE:** The `auth-url` Ingress annotation is inserted into the generated nginx configuration without sanitization. Users with Ingress permissions can inject arbitrary nginx directives, achieve code execution in the controller, and disclose cluster Secrets. | 1.11.5 / 1.12.1 | [GHSA-fwwp-xcxw-39vq](https://github.com/advisories/GHSA-fwwp-xcxw-39vq) |
| CVE-2024-7646 / GHSA-qx8j-xj5q-v7r3 | **Critical — CVSS 9.9** | **Annotation validation bypass → arbitrary command injection:** An actor with permission to create Ingress objects can bypass the annotation validation mechanism to inject arbitrary commands and obtain the ingress-nginx controller credentials. In the default installation, that credential provides access to all cluster Secrets. | Upstream PRs #11719 / #11721; see advisory for version range | [GHSA-qx8j-xj5q-v7r3](https://github.com/advisories/GHSA-qx8j-xj5q-v7r3) |
| CVE-2023-5043 / GHSA-5wj4-wffq-3378 | **High — CVSS 7.6** | **configuration-snippet annotation command injection:** The `nginx.ingress.kubernetes.io/configuration-snippet` annotation can be used by any Ingress creator to inject arbitrary nginx configuration, execute arbitrary commands, and steal the controller's credential (which in the default install grants cluster-wide Secret access). Multi-tenant environments allowing non-admin Ingress creation are most exposed. The `--enable-annotation-validation` flag added in v1.9.0 restricts annotation contents. | v1.9.0 (`--enable-annotation-validation` flag required for full mitigation) | [GHSA-5wj4-wffq-3378](https://github.com/advisories/GHSA-5wj4-wffq-3378) |
| CVE-2023-5044 / GHSA-fp9f-44c2-cw27 | **High** | **permanent-redirect annotation command injection:** The `nginx.ingress.kubernetes.io/permanent-redirect` annotation is not sanitized before use in the nginx configuration, allowing Ingress creators to inject arbitrary commands and obtain the controller credential. | v1.9.0 | [GHSA-fp9f-44c2-cw27](https://github.com/advisories/GHSA-fp9f-44c2-cw27) |
| CVE-2022-4886 / GHSA-gvrm-w2f9-f77q | **High — CVSS 8.1** | **Path sanitization bypass via log_format directive:** The sanitization of `spec.rules[].http.paths[].path` in Ingress objects can be bypassed by embedding a `log_format` directive, enabling a user with Ingress permissions to make the controller expose its credential files (e.g., serviceaccount token or TLS private keys) via the nginx access log. | 1.8.0 | [GHSA-gvrm-w2f9-f77q](https://github.com/advisories/GHSA-gvrm-w2f9-f77q) |
| CVE-2021-25742 / GHSA-4pp2-3663-mcw8 | **Moderate** | **Custom snippets → cluster-wide Secret disclosure:** A user who can create or update Ingress objects can use the custom snippets annotation feature to construct nginx configuration that reads and exposes all cluster Secrets accessible to the controller. | v1.1.0 (custom snippets gating) | [GHSA-4pp2-3663-mcw8](https://github.com/advisories/GHSA-4pp2-3663-mcw8) |
| CVE-2021-25745 / GHSA-pvmg-xgmx-9mxh | **High** | **Ingress path field → controller credential disclosure:** The `spec.rules[].http.paths[].path` field of an Ingress object can be crafted to cause the controller to include its own TLS credential files (serviceaccount token, TLS keys) in the nginx configuration output, enabling credential theft with cluster-wide Secret access. | v1.2.0 | [GHSA-pvmg-xgmx-9mxh](https://github.com/advisories/GHSA-pvmg-xgmx-9mxh) |
| CVE-2021-25746 / GHSA-79xv-4hmm-pw72 | **High** | **Metadata annotation → controller credential disclosure:** `.metadata.annotations` on an Ingress object can be constructed to embed the controller's credential files in the generated nginx configuration, enabling credential theft. | v1.2.0 | [GHSA-79xv-4hmm-pw72](https://github.com/advisories/GHSA-79xv-4hmm-pw72) |
| CVE-2021-25748 / GHSA-863x-868h-968x | **Moderate** | **Path sanitization newline bypass → credential disclosure:** A newline character in the `spec.rules[].http.paths[].path` field can bypass path sanitization, allowing Ingress creators to inject configuration that reads and exposes the controller's credential files (serviceaccount token and TLS keys). | v1.2.0 | [GHSA-863x-868h-968x](https://github.com/advisories/GHSA-863x-868h-968x) |

## Security Posture Notes

`ingress-nginx` is the most widely deployed Kubernetes Ingress controller, acting as the nginx reverse proxy frontend for the majority of Kubernetes-hosted web services. The controller runs with a cluster-scoped serviceaccount token that can read all Secrets across every namespace in the default installation, making it one of the highest-value lateral-movement targets in any Kubernetes cluster.

**Dominant vulnerability class — annotation injection:**

Every advisory in this set (2021–2025) exploits the same root cause: Ingress object annotations and spec fields are templated into the generated nginx configuration without sufficient sanitization. Any Kubernetes user who can create or update `Ingress` objects (`networking.k8s.io/v1` or `extensions/v1beta1`) can inject arbitrary nginx directives, execute OS commands, and steal the controller's serviceaccount token — which, in a default installation, grants cluster-wide `Secret` read access covering database passwords, TLS private keys, and cloud-provider API tokens.

**IngressNightmare (March 2025)** — CVE-2025-1974, CVE-2025-1097, CVE-2025-1098, CVE-2025-24514 — is the most severe iteration. CVE-2025-1974 requires **no cluster authentication at all**: any host on the pod network can target the admission webhook, exploiting the Lua library-loading path to achieve unauthenticated RCE.

**Key mitigations:**
- Upgrade to **≥ 1.11.5** (v1.11.x) or **≥ 1.12.1** (v1.12.x) to address the full IngressNightmare cluster.
- Enable `--enable-annotation-validation` (v1.9.0+) to restrict annotation injection surface.
- Apply least-privilege RBAC: restrict Ingress create/update to trusted users only in multi-tenant clusters.
- Scope the controller's serviceaccount to namespace-scoped Secret access when cluster-wide access is unnecessary.
- Network-isolate the admission webhook endpoint to only the Kubernetes API server if possible.

**Upstream security practices:** The Kubernetes Security Response Committee coordinates disclosure and CVE assignment; the project files all advisories via GitHub Security Advisories with coordinated embargo periods.

## Dependencies of Note

- **`k8s.io/client-go`** — Kubernetes API client used by the controller; inherits control-plane advisory exposure.
- **nginx** — the underlying C reverse proxy whose configuration is generated by the controller. C-level nginx CVEs (e.g., CVE-2024-7347 MP4 module memory corruption) are separate from Go controller bugs but affect deployed instances.
- **Lua / LuaJIT** — used for the controller's rate-limiting and traffic-management features; CVE-2025-1974 exploited the Lua library-loading mechanism via a crafted `AdmissionReview` payload.

## Open Questions

- Confirm the exact patched release for CVE-2024-7646 (GHSA-qx8j-xj5q-v7r3 is unreviewed; fixed via upstream PRs #11719 and #11721 but no explicit version boundary in the advisory).
- Survey advisories between 1.12.1 and current HEAD (late 2025–2026) for any post-IngressNightmare issues not yet captured.
- Clarify whether CVE-2021-25742 (custom snippets) is fully addressed by the v1.1.0 feature gate alone or also requires `--enable-annotation-validation`.

## Related Pages

- [[kubernetes/containerd]]
- [[kubernetes/kube-apiserver]]
- [[kubernetes/kubelet]]
- [[kubernetes/index]]

---
*Last updated: 2026-07-22 | Sources: github/advisory-database (GHSA-mgvx-rpfc-9mpv, GHSA-vg63-w3p9-jc9m, GHSA-823x-fv5p-h7hw, GHSA-fwwp-xcxw-39vq, GHSA-qx8j-xj5q-v7r3, GHSA-5wj4-wffq-3378, GHSA-fp9f-44c2-cw27, GHSA-gvrm-w2f9-f77q, GHSA-4pp2-3663-mcw8, GHSA-pvmg-xgmx-9mxh, GHSA-79xv-4hmm-pw72, GHSA-863x-868h-968x)*
