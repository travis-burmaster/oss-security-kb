# Argo CD (Kubernetes / CNCF)

**Registry:** k8s
**Weekly Downloads:** unknown (deployed via Helm chart or manifest; no registry download count)
**Repository:** https://github.com/argoproj/argo-cd
**Security Contact:** security@argoproj.io
**Disclosure Policy:** https://github.com/argoproj/argo-cd/blob/master/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

56 GHSA advisories exist in github/advisory-database (2018–2026). 31 are mapped individually below; the remaining 25 are noted in Security Posture Notes. All rows link to their primary source.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2018-21034 / GHSA-xj7v-c82w-92q2 | Moderate (CVSS 7.1) | Sensitive info exposure — authenticated users retrieve git-stored secrets and manifests via API | 1.5.0-rc1 | [GHSA-xj7v-c82w-92q2](https://github.com/advisories/GHSA-xj7v-c82w-92q2) |
| CVE-2020-11576 / GHSA-vj54-cjrx-x696 | Moderate | Observable discrepancy / user enumeration: `/api/v1/session` returns 401 for valid accounts and 404 for invalid ones | v1.5.1 | [GHSA-vj54-cjrx-x696](https://github.com/advisories/GHSA-vj54-cjrx-x696) |
| CVE-2021-23347 / GHSA-qq5v-f4c3-395c | Moderate (CVSS 5.4) | XSS via malicious SSO provider crafting error messages rendered in CLI | v1.7.13, v1.8.6 | [GHSA-qq5v-f4c3-395c](https://github.com/advisories/GHSA-qq5v-f4c3-395c) |
| CVE-2022-24348 / GHSA-63qx-x74g-jcr7 | High (CVSS 8.7) | Path traversal and symlink dereference in Helm chart handling leaks encrypted secrets and enables filesystem enumeration via verbose errors | v2.1.9, v2.2.4, v2.3.0 | [GHSA-63qx-x74g-jcr7](https://github.com/advisories/GHSA-63qx-x74g-jcr7) |
| CVE-2022-24768 / GHSA-2f5v-8r3f-8pww | Critical (CVSS 9.9) | Improper access control: users with sync/override/update/delete privileges escalate to admin; secondary path exposes Kubernetes Events | v2.1.14, v2.2.8, v2.3.2 | [GHSA-2f5v-8r3f-8pww](https://github.com/advisories/GHSA-2f5v-8r3f-8pww) |
| CVE-2022-24904 / GHSA-6gcg-hp2x-q54h | Moderate (CVSS 4.3) | Symlink following in repo-server leaks manifests outside repository root via directory-type Applications | v2.1.15, v2.2.9, v2.3.4 | [GHSA-6gcg-hp2x-q54h](https://github.com/advisories/GHSA-6gcg-hp2x-q54h) |
| CVE-2022-24905 / GHSA-xmg8-99r8-jc2j | Moderate (CVSS 4.3) | Login screen message spoofing via crafted SSO error URLs when SSO is enabled | v2.1.15, v2.2.9, v2.3.4 | [GHSA-xmg8-99r8-jc2j](https://github.com/advisories/GHSA-xmg8-99r8-jc2j) |
| CVE-2022-29165 / GHSA-r642-gv9p-2wjj | Critical (CVSS 9.8) | JWT blind trust: when anonymous access is enabled, unauthenticated users can forge tokens to impersonate any user or admin | v2.1.15, v2.2.9, v2.3.4 | [GHSA-r642-gv9p-2wjj](https://github.com/advisories/GHSA-r642-gv9p-2wjj) |
| CVE-2022-31034 / GHSA-2m7h-86qq-fp4v | High (CVSS 8.6) | Insecure entropy (non-cryptographic PRNG) in PKCE/OAuth state/nonce/code_verifier parameters — SSO auth bypass risk | v2.1.16, v2.2.10, v2.3.5, v2.4.1 | [GHSA-2m7h-86qq-fp4v](https://github.com/advisories/GHSA-2m7h-86qq-fp4v) |
| CVE-2022-31035 / GHSA-h4w9-6x78-8vrj | Critical (CVSS 8.7) | XSS: `javascript:` URIs in deployment link annotations execute in admin context when clicked; full CRUD on cluster resources | v2.1.16, v2.2.10, v2.3.5, v2.4.1 | [GHSA-h4w9-6x78-8vrj](https://github.com/advisories/GHSA-h4w9-6x78-8vrj) |
| CVE-2022-31036 / GHSA-q4w5-4gq2-98vm | Moderate (CVSS 4.3) | Symlink following in repo-server allows out-of-bounds YAML file reads | v2.1.16, v2.2.10, v2.3.5, v2.4.1 | [GHSA-q4w5-4gq2-98vm](https://github.com/advisories/GHSA-q4w5-4gq2-98vm) |
| CVE-2022-31102 / GHSA-pmjg-52h9-72qv | Low (CVSS 3.1) | XSS in `/auth/callback` page; exploitation requires encryption key access (very high bar) | v2.3.6, v2.4.5 | [GHSA-pmjg-52h9-72qv](https://github.com/advisories/GHSA-pmjg-52h9-72qv) |
| CVE-2022-31105 / GHSA-7943-82jg-wmw5 | High (CVSS 8.6) | TLS certificate verification skipped for OIDC provider connections when SSO enabled — MitM enables forged OIDC tokens | v2.2.11, v2.3.6, v2.4.5 | [GHSA-7943-82jg-wmw5](https://github.com/advisories/GHSA-7943-82jg-wmw5) |
| CVE-2022-41354 / GHSA-2q5c-qw9c-fmvq | Moderate (CVSS 4.3) | Application name enumeration via inconsistent API error messages for existing-but-inaccessible vs. nonexistent apps | v2.4.28, v2.5.16, v2.6.7 | [GHSA-2q5c-qw9c-fmvq](https://github.com/advisories/GHSA-2q5c-qw9c-fmvq) |
| CVE-2023-22482 / GHSA-q9hr-j4rf-8fjc | Critical (CVSS 8.6) | JWT audience claim not verified — OIDC tokens intended for other services accepted, enabling privilege escalation via unintended group claims | v2.3.14, v2.4.20, v2.5.8, v2.6.0-rc5 | [GHSA-q9hr-j4rf-8fjc](https://github.com/advisories/GHSA-q9hr-j4rf-8fjc) |
| CVE-2023-22736 / GHSA-6p4m-hw2h-6gmw | High (CVSS 7.5) | Controller reconciles Applications outside configured namespaces when sharding enabled (apps-in-any-namespace feature) — namespace isolation bypass | v2.5.8, v2.6.0-rc5 | [GHSA-6p4m-hw2h-6gmw](https://github.com/advisories/GHSA-6p4m-hw2h-6gmw) |
| CVE-2023-23947 / GHSA-3jfq-742w-xg8j | Critical (CVSS 9.1) | Out-of-bounds cluster secret update: any cluster-secret-update permission allows modifying arbitrary cluster secrets → privilege escalation, TLS MitM, deployment-restriction bypass | v2.3.17, v2.4.23, v2.5.11, v2.6.2 | [GHSA-3jfq-742w-xg8j](https://github.com/advisories/GHSA-3jfq-742w-xg8j) |
| CVE-2023-25163 / GHSA-mv6w-j4xc-qpfw | Moderate (CVSS 7.1) | Repository credentials leak in user-facing error messages and server logs (introduced in v2.6.0) | v2.6.1 | [GHSA-mv6w-j4xc-qpfw](https://github.com/advisories/GHSA-mv6w-j4xc-qpfw) |
| CVE-2023-40025 / GHSA-c8xw-vjgf-94hr | High | Web terminal websocket not terminated on token expiry — attacker retains access after authentication should have ended | v2.6.14, v2.7.12, v2.8.1 | [GHSA-c8xw-vjgf-94hr](https://github.com/advisories/GHSA-c8xw-vjgf-94hr) |
| CVE-2023-40029 / GHSA-fwr2-64vr-xv9m | Critical (CVSS 8.7) | Cluster credentials leaked via `kubectl.kubernetes.io/last-applied-configuration` annotation exposed in cluster details API | v2.6.15, v2.7.14, v2.8.3 | [GHSA-fwr2-64vr-xv9m](https://github.com/advisories/GHSA-fwr2-64vr-xv9m) |
| CVE-2023-40584 / GHSA-g687-f2gx-6wm8 | Moderate (CVSS 7.1) | repo-server DoS: tar.gz archives extracted without size validation; no permission check before temp-file deletion | v2.6.15, v2.7.14, v2.8.3 | [GHSA-g687-f2gx-6wm8](https://github.com/advisories/GHSA-g687-f2gx-6wm8) |
| CVE-2024-21652 / GHSA-x32m-mvfj-52xv | Critical (CVSS 9.8) | Brute-force protection bypass via crash-induced memory reset: DoS resets in-memory failed-login counter, enabling unlimited credential guessing | v2.8.13, v2.9.9, v2.10.4 | [GHSA-x32m-mvfj-52xv](https://github.com/advisories/GHSA-x32m-mvfj-52xv) |
| CVE-2024-21662 / GHSA-2vgg-9h6w-m454 | Moderate (CVSS 5.3) | Brute-force protection bypass via 1000-entry cache overflow across many usernames, evicting admin entries | v2.8.13, v2.9.9, v2.10.4 | [GHSA-2vgg-9h6w-m454](https://github.com/advisories/GHSA-2vgg-9h6w-m454) |
| CVE-2024-22424 / GHSA-92mw-q256-5vwg | High (CVSS 8.8) | CSRF: CORS bypass via non-sensitive content-type (`text/plain`) enables API manipulation without authentication from same parent domain | v2.7.16, v2.8.8, v2.9.4, v2.10-rc2 | [GHSA-92mw-q256-5vwg](https://github.com/advisories/GHSA-92mw-q256-5vwg) |
| CVE-2024-36106 / GHSA-3cqf-953p-h5cp | Moderate (CVSS 5.7) | Cluster name enumeration via inconsistent error messages (distinct response for existing vs. nonexistent clusters) | v2.9.17, v2.10.12, v2.11.3 | [GHSA-3cqf-953p-h5cp](https://github.com/advisories/GHSA-3cqf-953p-h5cp) |
| CVE-2024-37152 / GHSA-87p9-x75h-p4j2 | Moderate (CVSS 4.3) | Unauthenticated access to `/api/v1/settings` exposes sensitive deployment configuration | v2.9.17, v2.10.12, v2.11.3 | [GHSA-87p9-x75h-p4j2](https://github.com/advisories/GHSA-87p9-x75h-p4j2) |
| CVE-2025-23216 / GHSA-47g2-qmh2-749v | Moderate (CVSS 7.1) | Secret values not scrubbed from patch error messages and diff views — secrets visible to all read-access users when invalid Secret is synced | v2.11.13, v2.12.10, v2.13.4 | [GHSA-47g2-qmh2-749v](https://github.com/advisories/GHSA-47g2-qmh2-749v) |
| CVE-2025-59537 / GHSA-wp4p-9pxh-cgx2 | High (CVSS 9.0) | Unauthenticated DoS: malformed Gogs webhook payload with missing repository data triggers nil-pointer deref in `affectedRevisionInfo`; crashes server | v2.14.20, v3.0.19, v3.1.8, v3.2.0-rc2 | [GHSA-wp4p-9pxh-cgx2](https://github.com/advisories/GHSA-wp4p-9pxh-cgx2) |
| CVE-2026-42880 / GHSA-3v3m-wc6v-x4x3 | Critical (CVSS 9.1) | ServerSideDiff endpoint returns unmasked Kubernetes Secret values (SA tokens, TLS certs, DB creds) to any user with basic read access via `IncludeMutationWebhook=true` | v3.2.11, v3.3.9 | [GHSA-3v3m-wc6v-x4x3](https://github.com/advisories/GHSA-3v3m-wc6v-x4x3) |
| CVE-2026-45737 / GHSA-rg3g-4rw9-gqrp | Moderate | ServerSideDiff secret extraction via `last-applied-configuration` annotation (incomplete fix for CVE-2026-42880) | v3.2.12, v3.3.10, v3.4.2 | [GHSA-rg3g-4rw9-gqrp](https://github.com/advisories/GHSA-rg3g-4rw9-gqrp) |
| CVE-2026-45738 / GHSA-h98r-wv3h-fr38 | High (CVSS 7.1) | Stored XSS via `javascript:` URI in application link annotation — developer-to-admin privilege escalation via session hijacking | v3.2.12, v3.3.10, v3.4.2 | [GHSA-h98r-wv3h-fr38](https://github.com/advisories/GHSA-h98r-wv3h-fr38) |

*OSV link: https://osv.dev/list?ecosystem=Go&q=argoproj%2Fargo-cd* (note: OSV.dev API blocked in this environment; cross-reference github/advisory-database directly)

*Full GHSA list (56 advisories): https://github.com/argoproj/argo-cd/security/advisories*

## Security Posture Notes

Argo CD is a CNCF Graduated project (graduated 2022). It is the dominant GitOps continuous delivery tool for Kubernetes, with >17K GitHub stars and widespread deployment in production Kubernetes clusters. Security disclosures follow a formal SECURITY.md process at security@argoproj.io with coordinated release timelines across supported minor versions (typically 3 minor versions patched simultaneously).

**Recurring vulnerability themes (2021–2026):**
1. **Repo-server symlink / path traversal (≥3 advisories 2022)**: The repo-server processes untrusted Helm chart content and git repositories; symlink following repeatedly escaped the intended extraction root, leaking manifests, YAML secrets, and encrypted files. Fixed by randomizing temp paths (v2.3+) and restricting permissions.
2. **SSO / JWT boundary failures (≥6 advisories 2022–2023)**: Multiple JWT, OIDC, and OAuth2 implementation bugs — blind JWT trust when anonymous access enabled (CVE-2022-29165, Critical 9.8), audience claim bypass (CVE-2023-22482, Critical 8.6), TLS skip for OIDC connections (CVE-2022-31105, High), insecure PRNG for PKCE/state/nonce (CVE-2022-31034, High) — collectively mean every SSO integration path carried significant risk through v2.6.
3. **RBAC authorization bypass (≥4 advisories 2022–2023)**: Users with limited permissions consistently found paths to escalate (CVE-2022-24768 Critical 9.9, CVE-2023-23947 Critical 9.1); namespace isolation bypassed when controller sharding enabled (CVE-2023-22736 High 7.5).
4. **Secret leakage via annotation (2023, 2026)**: The `kubectl.kubernetes.io/last-applied-configuration` annotation surfaced twice as a credential exposure vector — once in cluster details (CVE-2023-40029 Critical 8.7) and again as an incomplete-fix bypass in the ServerSideDiff feature (CVE-2026-45737); the root cause is k8s's default behavior of storing full manifests in annotations.
5. **Brute-force protection bypass pair (2024)**: Two independent bypasses landed together (CVE-2024-21652 Critical 9.8 via crash-reset; CVE-2024-21662 Moderate via cache overflow), collectively voiding the rate-limiting controls added in earlier releases.
6. **ServerSideDiff secret extraction cluster (2026)**: CVE-2026-42880 (Critical 9.1) exposed plaintext secrets through the new ServerSideDiff feature; CVE-2026-45737 was the incomplete-fix follow-on; both fixed in v3.2.12/v3.3.10/v3.4.2.

**25 additional GHSA advisories (not individually mapped in this pass):** The full 56-entry advisory set includes additional XSS, information disclosure, DoS, and permission-boundary issues from 2021–2025 spanning GHSA-6w87-g839-9wv7, GHSA-xcqr-9h24-vrgw, GHSA-h8jc-jmrf-9h8f (2021), GHSA-h6h5-6fmq-rh28, GHSA-r9cr-hvjj-496v, GHSA-96jv-vj39-x4j6, GHSA-jhqp-vf4w-rpwq (2022), GHSA-jwv5-8mqv-g387, GHSA-g623-jcgg-mhmm, GHSA-6v85-wr92-q4p7, GHSA-jhwx-mhww-rgc3, GHSA-9m6p-x4h2-6frq, GHSA-2gvw-w6fj-7m3c, GHSA-9766-5277-j5hr (2024), GHSA-jmvp-698c-4x3w, GHSA-v8wx-v5jq-qhhw (2024), GHSA-gppm-hq3p-h4rp (2024-11), GHSA-58fx-7v9q-3g56, GHSA-274v-mgcv-cm8j, GHSA-2hj5-g64g-fp6p (2025), GHSA-gpx4-37g2-c8pv, GHSA-f9gq-prrc-hrhc, GHSA-786q-9hcg-v9ff, GHSA-g88p-r42r-ppp9 (2025). See the [full advisory list](https://github.com/argoproj/argo-cd/security/advisories) for details.

**Current status (2026-07-26):** Latest stable is v3.4.5 (released 2026-07-09). Active development supports v2 and v3 lines. The v2 branch (v2.14.x) is the final v2 stable line; v3 (v3.x) is the current development trajectory with the App-in-Any-Namespace, ServerSideDiff, and Argo CD v3 API improvements — the ServerSideDiff feature introduced two Critical advisories in 2026. Anonymous access (disabled by default) and multi-tenant RBAC configurations are the highest-risk deployment patterns.

## Dependencies of Note

- `k8s.io/client-go` — Kubernetes client; subject to k8s-ecosystem vulnerability history
- `helm.sh/helm/v3` — Helm chart rendering; repo-server symlink issues partially originate here
- `github.com/go-jose/go-jose` — JOSE/JWT processing; has its own advisory history (7 advisories mapped in [[go/github.com/go-jose/go-jose]])
- `github.com/golang-jwt/jwt` — JWT parsing; advisory history in [[go/github.com/golang-jwt/jwt]]
- `golang.org/x/net` — HTTP/2 and networking; advisory history in [[go/golang.org-x-net]]

## Open Questions

- Map the remaining 25 GHSA advisories (GHSA-6w87-g839-9wv7 and others listed above) for complete coverage.
- Check whether v2.14.x receives the CVE-2026-45738 (stored XSS) fix — advisory notes v2 "up to v2.14.21 unpatched".
- Review whether the SECURITY.md disclosure process includes a bug bounty program or only coordinated disclosure.
- Assess downstream impact: clusters using the non-default `apps-in-any-namespace` feature should audit for CVE-2023-22736 exposure.

## Related Pages

- [[kubernetes/kube-apiserver]]
- [[kubernetes/helm]]
- [[kubernetes/index]]
- [[go/github.com/go-jose/go-jose]]

---
*Last updated: 2026-07-26 | Sources: 31 GHSA advisories (github/advisory-database via WebFetch + mcp__github__search_code), argoproj/argo-cd GitHub release page*
