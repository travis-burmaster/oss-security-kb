# Proposed KB Updates for `handlebars` (npm)

---

## 1. Suggested Vulnerability Table Rows

### Historical Advisories (pre-2026, fixed before v4.7.9)

| GHSA / CVE | Title | Severity | Fixed In | Era |
|---|---|---|---|---|
| GHSA-9prh-257w-9277 / CVE-2015-8861 | Cross-Site Scripting in handlebars | High | 4.0.0 | 2015 |
| GHSA-q42p-pg8m-cqh6 | Prototype Pollution | High | 3.0.7 / 4.0.14 / 4.1.2 | 2018 |
| GHSA-2cf5-4w76-r9qv | Arbitrary Code Execution | Critical | 3.0.8 / 4.5.2 | 2019 |
| GHSA-g9r4-xpmj-mj65 | Prototype Pollution | High | 3.0.8 / 4.5.3 | 2019 |
| GHSA-q2c6-c6pm-g3gh | Arbitrary Code Execution | Critical | 3.0.8 / 4.5.3 | 2019 |
| GHSA-w457-6q6x-cgp9 / CVE-2019-19919 | Prototype Pollution | Critical | 3.0.8 / 4.3.0 | 2019 |
| GHSA-62gr-4qp9-h98f / CVE-2019-20922 | Regular Expression Denial of Service (ReDoS) | High | 4.4.5 | 2019 |
| GHSA-765h-qjxv-5f44 / CVE-2021-23383 | Prototype Pollution | Critical | 4.7.7 | 2021 |
| GHSA-f2jv-r9rf-7988 / CVE-2021-23369 | Remote Code Execution via template compilation | Critical | 4.7.7 | 2021 |

### 2026 Advisory Cluster (all fixed in v4.7.9, commit 68d8df5)

| GHSA / CVE | Title | Category |
|---|---|---|
| GHSA-2qvq-rjwj-gvw9 / CVE-2026-33916 | Prototype Pollution → XSS through Partial Template Injection | Prototype Pollution / XSS |
| GHSA-2w6w-674q-4c4q / CVE-2026-33937 | JavaScript Injection via AST Type Confusion | AST Type Confusion / Injection |
| GHSA-3mfm-83xf-c92r / CVE-2026-33938 | JavaScript Injection via AST Type Confusion (tampering `@partial-block`) | AST Type Confusion / Injection |
| GHSA-xhpv-hc6g-r9c6 / CVE-2026-33940 | JavaScript Injection via AST Type Confusion (object as dynamic partial) | AST Type Confusion / Injection |
| GHSA-xjpj-3mr7-gcpf / CVE-2026-33941 | JavaScript Injection in CLI Precompiler via Unescaped Names/Options | CLI Injection |
| GHSA-9cx6-37pm-9jff / CVE-2026-33939 | Denial of Service via Malformed Decorator Syntax in Compilation | DoS |
| GHSA-442j-39wm-28r2 | Property Access Validation Bypass in `container.lookup` | Sandbox Bypass |
| GHSA-7rx3-28cr-v5wh | Prototype Method Access Control Gap (`__lookupSetter__` missing from blocklist) | Sandbox Bypass |

---

## 2. Posture Notes

- **Current status:** v4.7.9 is the latest release and addresses all known advisories. Users on 4.7.9 have no outstanding GHSA against them from the evidence provided.
- **Breadth of 2026 cluster:** Eight distinct advisories were resolved in a single commit/release. Three share an "AST Type Confusion" root cause (CVE-2026-33937, -33938, -33940), two share a "sandbox/blocklist bypass" root cause (GHSA-442j, GHSA-7rx3), and the remainder are distinct (prototype-pollution-to-XSS, CLI injection, DoS). This indicates a coordinated security audit or disclosure batch rather than eight fully independent attack surfaces.
- **Long tail of historical issues:** Handlebars has had security-critical advisories in every major release line (3.x and 4.x) since 