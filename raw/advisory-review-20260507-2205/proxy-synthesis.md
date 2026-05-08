# OSS Security KB Update Proposal: `github.com/prometheus/client_golang`

---

## 1. Evidence Normalization & Deduplication

The evidence contains **2 OSV records** and **1 GitHub Advisory**, all mapping to a single vulnerability:

| Source ID | Alias(es) | Duplicate? |
|---|---|---|
| GHSA-cg3q-j54f-5p7p | CVE-2022-21698, GO-2022-0322 | Primary |
| GO-2022-0322 | CVE-2022-21698, GHSA-cg3q-j54f-5p7p | Duplicate of above |
| GitHub Advisory GHSA-cg3q-j54f-5p7p | CVE-2022-21698 | Same as primary |

**Result:** 1 unique vulnerability after normalization.

---

## 2. Vulnerability Record

### CVE-2022-21698 — Denial of Service via Unbounded Label Cardinality in `promhttp`

| Field | Value |
|---|---|
| **CVE** | CVE-2022-21698 |
| **GHSA** | GHSA-cg3q-j54f-5p7p |
| **Go Vuln ID** | GO-2022-0322 |
| **Severity** | High |
| **Type** | Uncontrolled Resource Consumption (CWE-400) / Denial of Service |
| **Affected package** | `github.com/prometheus/client_golang` (subpackage `promhttp`) |
| **Affected versions** | `< 1.11.1` |
| **Fixed version** | **`v1.11.1`** (released 2022-02-15) |
| **Fix PRs** | [#962](https://github.com/prometheus/client_golang/pull/962) (main), [#987](https://github.com/prometheus/client_golang/pull/987) (backport to v1.11.x) |
| **Published** | 2022-02-16 |

#### Exposure Conditions (all must be true)

An application is exploitable **only if all four** conditions hold:

1. Uses any `promhttp.InstrumentHandler*` middleware **except** `RequestsInFlight`.
2. Does **not** filter or restrict HTTP methods before the middleware executes.
3. Passes a metric containing a `method` label name to the middleware.
4. No upstream firewall, load balancer, or reverse proxy filters requests with non-standard HTTP methods.

An attacker sends requests with arbitrary, non-standard HTTP method strings, each creating a new time-series label value. This causes unbounded cardinality growth, leading to memory exhaustion and denial of service.

#### Mitigations (if upgrade not possible)

- Remove the `method` label from counters/gauges used with `InstrumentHandler*`.
- Disable affected `promhttp` handlers.
- Add custom middleware upstream of `promhttp` to sanitize `http.Request.Method`.
- Configure a reverse proxy / WAF to allow only standard HTTP methods.

---

## 3. Drafted KB Page Notes (repo style)

```markdown
# github.com/prometheus/client_golang

## Vulnerabilities

### CVE-2022-21698 – DoS via unbounded HTTP method label cardinality in promhttp

- **Identifiers:** CVE-2022-21698 · GHSA-cg3q-j54f-5p7p · GO-2022-0322
- **Severity:** High
- **Affected versions:** < 1.11.1
- **Fixed version:** v1.11.1
- **Component:** `promhttp` (InstrumentHandler* middleware)
- **Fix:** [PR #962](https://github.com/prometheus/client_golang/pull/962), backported in [PR #987](https://github.com/prometheus/client_golang/pull/987). Adds validation of `method` and `code` label values before recording metrics.

#### Description

The `promhttp.InstrumentHandler*` middleware records HTTP method values as
metric labels without sanitization. Requests with arbitrary non-standard
methods create unbounded label cardinality, leading to memory exhaustion
and denial of service.

#### Exposure Conditions

All of the following must be true:
1. Application uses `promhttp.InstrumentHandler*` (except `RequestsInFlight`).
2. No method filtering occurs before the middleware.
3. A metric with a `method` label is passed to the middleware.
4. No upstream proxy/firewall restricts HTTP methods.

#### Workarounds

- Remove `method` label from instrumented metrics.
- Sanitize request methods in custom middleware before promhttp.
- Use a reverse proxy or WAF to allow only known HTTP methods.

#### References

- [Advisory](https://github.com/prometheus/client_golang/security/advisories/GHSA-cg3q-j54f-5p