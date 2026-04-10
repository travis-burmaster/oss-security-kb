# kube-apiserver (kubernetes)

**Registry:** k8s
**Weekly Downloads:** unknown (as of 2026-04-10)
**Repository:** https://github.com/kubernetes/kubernetes
**Security Contact:** https://github.com/kubernetes/committee-security-response#contacting-the-src
**Disclosure Policy:** https://kubernetes.io/security/
**Current Status:** audit-ingested

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-10 | [@travis-burmaster](https://github.com/travis-burmaster) | partial-source (RBAC, admission, authn) | hybrid (manual review + automated search) | 9 findings (4 medium, 5 low) | [oss-security-kb #audit/kube-apiserver-rbac-2026-04](https://github.com/travis-burmaster/oss-security-kb) |

**Audit scope:** 420 Go source files across `plugin/pkg/auth/`, `staging/src/k8s.io/apiserver/pkg/authorization/`, `staging/src/k8s.io/apiserver/pkg/authentication/`, `staging/src/k8s.io/apiserver/pkg/admission/`, `pkg/registry/rbac/`, and `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/`. Commit `f5c7b42` (kubernetes/kubernetes main branch, 2026-04-10).

**Not in scope:** etcd interaction, aggregated API servers, CRD admission, scheduler, kubelet, cloud-provider integrations.

## Findings

### Medium Severity

#### M1: "edit" ClusterRole Grants Namespace-Scoped Service Account Impersonation

**Severity:** Medium-High
**Type:** Privilege escalation via overly broad default RBAC policy
**Affected:** All Kubernetes clusters using default edit/admin ClusterRoles where privileged ServiceAccounts exist in the same namespace

The bootstrap `edit` ClusterRole includes the `impersonate` verb on `serviceaccounts` (core API group). This rule aggregates into `admin` and is inherited by `cluster-admin`. Any user with `edit` via a RoleBinding in namespace X can impersonate **any** ServiceAccount in namespace X by setting `Impersonate-User: system:serviceaccount:X:<sa-name>`.

If any ServiceAccount in that namespace has elevated privileges (e.g., a CI/CD bot with `admin` or `cluster-admin` via ClusterRoleBinding), the attacker inherits all of those permissions — including the ability to create new RoleBindings, read Secrets, and potentially escalate to cluster-admin.

**Code references:**
- Bootstrap policy rule: `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:159`
- Impersonation filter: `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/impersonation.go:74-118`
- Namespace-scoped authorization check: `impersonation.go:79` (SA namespace passed in attributes)

**Exploit scenario:**
```bash
# User has "edit" RoleBinding in namespace "production"
kubectl get serviceaccounts -n production
kubectl auth can-i --list --as=system:serviceaccount:production:deploy-bot
kubectl get secrets -n production --as=system:serviceaccount:production:deploy-bot
kubectl create rolebinding escalate --clusterrole=admin \
  --user=attacker -n production \
  --as=system:serviceaccount:production:deploy-bot
```

**Mitigations:**
- Namespace scoping limits impersonation to SAs in the bound namespace only
- Impersonation is SA-only — cannot impersonate users, groups, or UIDs via the `edit` role
- Chaining impersonation is blocked (headers stripped before forwarding)
- KEP 5284 introduces constrained impersonation as a more granular replacement

**Gaps:** No per-SA restriction, no admission policy protection, cluster-admin path exists if any SA in the namespace has ClusterRoleBinding to cluster-admin.

**Status:** Known to maintainers (code comment at line 157 labels it an "escalating resource"), no CVE issued, KEP 5284 in progress. Largely unknown to cluster operators.

---

#### M2: Admission Reinvocation Skips Newly-Matching Webhooks

**Severity:** Medium
**Type:** Admission control bypass via label mutation

A mutating webhook A can add labels that would cause validating webhook B to match, but if B didn't match in the first admission pass, it is **never called** during reinvocation. Reinvocation only re-invokes webhooks that were already called and have `ReinvocationPolicy: IfNeeded`.

Additionally, reinvocation is capped at exactly one re-pass — mutations during the second round are never re-validated.

**Code references:**
- `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/mutating/dispatcher.go:146-199`
- Reinvocation cap: `reinvocation.go:47`

**Impact:** Policy bypass if webhooks use label-based matching and an attacker controls a mutating webhook upstream in the admission chain.

---

#### M3: Dry-Run Silent Webhook Skip

**Severity:** Medium
**Type:** Validation bypass on dry-run requests

A webhook with `failurePolicy: Ignore` and `sideEffects: nil` silently skips validation on dry-run requests. The nil `SideEffects` triggers `ErrCallingWebhook`, which the `Ignore` policy swallows without blocking the request.

**Code references:**
- `mutating/dispatcher.go:248-255`
- `validating/dispatcher.go:249-256`

**Impact:** Dry-run requests can bypass validation for misconfigured webhooks, potentially leaking information about what would be admitted.

---

#### M4: Fail-Open with FailurePolicy: Ignore

**Severity:** Medium
**Type:** Admission bypass via webhook disruption

Any webhook with `failurePolicy: Ignore` allows requests through on timeout or network error. The only signal is an audit annotation at `failed-open.{mutation|validation}.webhook.admission.k8s.io/`. An attacker who can disrupt connectivity to the webhook endpoint (e.g., via NetworkPolicy manipulation or DNS poisoning) can bypass all validation from that webhook.

**Code references:**
- `mutating/dispatcher.go:204-224`
- `validating/dispatcher.go:199-215`
- Panic handling also respects Ignore: `validating/dispatcher.go:143-161`

**Impact:** Well-known by design, but under-audited in production clusters. Recommend monitoring fail-open audit annotations.

---

### Low Severity

#### L1: v1beta1 Admission Response UID Not Verified

For `admissionv1beta1.AdmissionReview` responses, neither the UID nor the GVK is verified — the code explicitly states "allow any." A MITM on webhook traffic could spoof responses. The v1 API correctly verifies both.

**Code:** `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/request/admissionreview.go:101-126`
**Mitigation:** v1beta1 is deprecated; migrate webhooks to v1.

#### L2: Audit Annotation Exfiltration Channel

Mutating and validating webhooks can set arbitrary `AuditAnnotations` in their response. A malicious webhook could encode sensitive object data into annotation values, exfiltrating it through the audit pipeline. The apiserver avoids logging patches but does not filter webhook-supplied annotations.

**Code:** `mutating/dispatcher.go:319-323, 458`

#### L3: X-Remote-* Headers Not Cleared on Failed x509 Verification

When front-proxy x509 certificate verification fails, `ClearAuthenticationHeaders` is never called. Attacker-supplied `X-Remote-User`/`X-Remote-Group` headers survive on the request for downstream handlers and audit loggers. Not directly exploitable (no authenticator reads these without the x509 gate passing) but a defense-in-depth gap.

**Code:** `staging/src/k8s.io/apiserver/pkg/authentication/request/headerrequest/requestheader.go:131`

#### L4: NonResourceURL Wildcard Uses TrimRight Instead of TrimSuffix

A RBAC rule like `/api/**` is trimmed via `TrimRight("*")` to `/api/`, identical to `/api/*`. This results in broader matching than visually implied, though no direct exploitation path was found.

**Code:** `pkg/apis/rbac/v1/evaluation_helpers.go:102`

#### L5: Extra Header Key Collision via URL Encoding

Two different percent-encoded `Impersonate-Extra-*` header names can URL-decode to the same key, causing their values to merge via `append`. Minor data integrity issue.

**Code:** `staging/src/k8s.io/apiserver/pkg/authentication/request/headerrequest/requestheader.go:202-217`

---

### Confirmed Safe

| Area | Status |
|------|--------|
| RBAC escalation prevention (create bindings) | Three-tier check (system:masters → escalate/bind verbs → ConfirmNoEscalation) correctly implemented |
| Aggregate ClusterRoles | Requires cluster-admin to create; label injection bounded by user's existing permissions |
| TOCTOU between mutation and validation | Not present — same in-memory object used throughout |
| OIDC "none" algorithm | Blocked by explicit allowlist (RS/ES/PS families only) |
| Token expiry handling | Delegated to go-oidc library, no custom clock-skew bugs |
| Impersonation chaining | Blocked — headers stripped before forwarding |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| (none on record — see [Kubernetes CVE feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/) for component-specific advisories) | — | — | — | — |

## Security Posture Notes

- `kube-apiserver` is one of the highest-value components the KB can cover because it is the control-plane request gateway for authentication, authorization, admission, API object validation, and persistence flows.
- The upstream Kubernetes project publishes a formal security process and dedicated Security Response Committee contact path.
- Vulnerability history here needs careful scoping because many Kubernetes advisories span multiple components or configuration assumptions rather than a single binary.
- The "edit" ClusterRole's impersonation grant (M1) represents the highest practical risk for most clusters, because privileged ServiceAccounts in shared namespaces are common in CI/CD and GitOps deployments.

## Recommendations for Cluster Operators

1. **Audit ServiceAccount bindings** in every namespace where `edit` or `admin` is granted. If any SA has elevated privileges (especially ClusterRoleBindings), this is an escalation path.
2. **Adopt KEP 5284 constrained impersonation** when available in your cluster version.
3. **Consider removing the impersonate rule from the edit aggregate** by creating a custom ClusterRole that overrides `system:aggregate-to-edit` without the impersonate grant.
4. **Monitor fail-open audit annotations** (`failed-open.*.webhook.admission.k8s.io/`) for evidence of admission bypass.
5. **Migrate all webhooks to admissionregistration.k8s.io/v1** to get UID verification on responses.
6. **Set `failurePolicy: Fail`** on security-critical webhooks and test resilience separately.

## Dependencies of Note

- `etcd` is a closely related follow-on page because storage-layer bugs and access-control assumptions often intersect with API-server risk.
- Admission webhooks, aggregated APIs, and authn/authz integrations are likely future cross-links once the KB has more Kubernetes coverage.

## Open Questions (Resolved and Remaining)

- ~~Are there public component-focused audits of request decoding, admission control, or impersonation / authorization paths?~~ **Resolved:** This audit covers RBAC, admission, authn, and impersonation paths. Request decoding and storage-layer audits remain open.
- ~~Which published Kubernetes CVEs primarily affect `kube-apiserver` versus broader cluster configuration or adjacent components?~~ **Partially resolved:** No existing CVE covers the edit-role impersonation vector (M1). Advisory mapping of other k8s CVEs to kube-apiserver is still pending.
- Should future pages track default deployment hardening guidance separately from software vulnerability history?

## Related Pages

- [[kubernetes/index]]

---
*Last updated: 2026-04-10 | Sources: 6 (upstream repository, SECURITY_CONTACTS, Kubernetes security / CVE feed documentation, source code audit of 420 Go files at commit f5c7b42, KEP 5284, bootstrap RBAC policy)*
*Auditor contact: [@travis-burmaster](https://github.com/travis-burmaster)*
