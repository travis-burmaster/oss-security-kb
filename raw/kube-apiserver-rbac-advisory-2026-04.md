# Kubernetes Security Advisory: "edit" ClusterRole Enables Namespace-Scoped Privilege Escalation via ServiceAccount Impersonation

**Date:** 2026-04-10
**Reporter:** Travis Burmaster ([@travis-burmaster](https://github.com/travis-burmaster))
**Affected Component:** kube-apiserver — RBAC bootstrap policy + impersonation filter
**Affected Versions:** All current Kubernetes versions using default bootstrap RBAC roles
**Severity Assessment:** Medium-High (CVSS estimated 7.1 — network/low complexity/high impact within namespace scope)

## Summary

The default Kubernetes `edit` ClusterRole includes the `impersonate` verb on `serviceaccounts` in the core API group. When granted via a namespaced RoleBinding, this allows a user to impersonate **any** ServiceAccount within that namespace. If any ServiceAccount in the namespace holds elevated privileges via ClusterRoleBindings (common in CI/CD, GitOps, and monitoring deployments), this creates a direct privilege escalation path — potentially to cluster-admin.

This behavior is acknowledged in the source code (labeled as an "escalating resource" at `bootstrappolicy/policy.go:157`) and partially addressed by KEP 5284 (constrained impersonation), but:
- No CVE has been issued
- The behavior is not prominently documented in the ClusterRole reference documentation
- Most cluster operators are unaware that `edit` includes impersonation capabilities
- Real-world clusters commonly have privileged ServiceAccounts co-located in namespaces where `edit` is granted

## Technical Details

### Root Cause

The bootstrap policy at `plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go:159` defines:

```go
rbacv1helpers.NewRule("impersonate").Groups(legacyGroup).Resources("serviceaccounts").RuleOrDie()
```

This rule is part of `editRules()` (line 155), materialized into `system:aggregate-to-edit` (line 413), which carries the aggregation label `rbac.authorization.k8s.io/aggregate-to-edit: true`. Through aggregation, this rule propagates to `admin` and is implicitly available in `cluster-admin`.

### Impersonation Mechanism

The impersonation filter at `staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/impersonation.go` processes `Impersonate-User` headers (line 218-226). When the header value matches `system:serviceaccount:<namespace>:<name>`, the filter:

1. Constructs authorization attributes with `Verb: "impersonate"`, `Resource: "serviceaccounts"`, and `Namespace: <sa-namespace>` (line 74-81)
2. Calls `Authorize()` against the RBAC authorizer (line 118)
3. RBAC evaluates RoleBindings in the target SA's namespace — a RoleBinding in namespace X satisfies the check for SAs in namespace X

### Exploitation

```bash
# Attacker has "edit" RoleBinding in namespace "production"

# 1. Enumerate service accounts
kubectl get serviceaccounts -n production

# 2. Identify a privileged SA (e.g., CI/CD bot with admin ClusterRoleBinding)
kubectl auth can-i --list --as=system:serviceaccount:production:deploy-bot

# 3. Impersonate and perform privileged operations
kubectl get secrets -n production --as=system:serviceaccount:production:deploy-bot

# 4. Create a persistent escalation path
kubectl create rolebinding attacker-admin --clusterrole=admin \
  --user=attacker -n production \
  --as=system:serviceaccount:production:deploy-bot
```

### Scope Limitations

- **Namespace-scoped:** Impersonation is limited to SAs in the namespace where the attacker has a RoleBinding
- **SA-only:** The `edit` role grants impersonation on `serviceaccounts` only — not `users`, `groups`, `uids`, or `userextras`
- **No chaining:** Impersonation headers are stripped before forwarding (impersonation.go:172-181)

### Path to Cluster-Admin

If any ServiceAccount in the attacker's namespace has a ClusterRoleBinding to `cluster-admin` (or any ClusterRole with wildcard permissions), the attacker inherits full cluster control. This configuration is common in:
- CI/CD pipelines (Jenkins, ArgoCD, Tekton service accounts)
- Monitoring agents (Prometheus, Datadog)
- GitOps controllers (Flux, ArgoCD)
- Backup operators (Velero)

## Additional Findings from the Same Audit

During the same audit session, three additional medium-severity issues were identified:

1. **Admission reinvocation skips newly-matching webhooks** — Mutating webhook A can add labels that cause validating webhook B to match, but B is skipped if it didn't match in round 1. (mutating/dispatcher.go:146-199)

2. **Dry-run silent webhook skip** — A webhook with `failurePolicy: Ignore` + `sideEffects: nil` silently skips validation on dry-run requests. (mutating/dispatcher.go:248-255)

3. **Fail-open webhook bypass** — Webhooks with `failurePolicy: Ignore` allow requests through on timeout/network disruption, with only an audit annotation as signal. (mutating/dispatcher.go:204-224)

Full audit report with 5 additional low-severity findings and confirmed-safe areas is available at: https://github.com/travis-burmaster/oss-security-kb/tree/main/wiki/kubernetes/kube-apiserver.md

## Recommended Fix

1. **Short term:** Remove the `impersonate` rule from `editRules()` in the bootstrap policy. This is a breaking change for clusters that rely on this behavior, so it should be gated behind a feature flag or announced with a deprecation period.

2. **Long term:** Accelerate adoption of KEP 5284 constrained impersonation, which allows fine-grained impersonation policies rather than blanket verb grants.

3. **Documentation:** Prominently document the impersonation capability in the `edit` and `admin` ClusterRole reference pages, with a security warning about co-locating privileged ServiceAccounts in namespaces where these roles are granted.

## Recommended Operator Mitigations

1. Audit all ServiceAccount bindings in namespaces where `edit` or `admin` RoleBindings exist
2. Move privileged ServiceAccounts to dedicated namespaces without broad `edit`/`admin` grants
3. Create a custom ClusterRole that overrides `system:aggregate-to-edit` without the impersonate rule
4. Monitor audit logs for impersonation activity (`user.extra.impersonated-user`)

## Disclosure Timeline

| Date | Action |
|------|--------|
| 2026-04-10 | Source code audit conducted; findings documented |
| 2026-04-10 | Advisory submitted to Kubernetes SRC |
| TBD | SRC response / triage |
| TBD | Public disclosure (coordinated with SRC) |

## Contact

- **Reporter:** Travis Burmaster
- **GitHub:** [@travis-burmaster](https://github.com/travis-burmaster)
- **Knowledge Base:** https://github.com/travis-burmaster/oss-security-kb

## Methodology

Partial source audit of 420 Go files from kubernetes/kubernetes at commit `f5c7b42`. Three parallel manual+automated reviews covering RBAC privilege escalation, admission control bypass, and authentication chain analysis. Hybrid methodology: manual code review of critical paths + grep/automated search for dangerous patterns.
