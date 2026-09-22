# com.squareup.okhttp3:okhttp (Maven)

**Registry:** Maven Central
**Weekly Downloads:** unknown (Maven Central download stats unavailable via API)
**Repository:** https://github.com/square/okhttp
**Security Contact:** https://github.com/square/okhttp/security
**Disclosure Policy:** https://github.com/square/okhttp/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-09-22 | oss-security-kb nightly | api-surface / advisory-review | automated | 3 advisories mapped | [GHSA database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2016-2402 / GHSA-4hc2-jh7r-wrc3 | Moderate CVSS 5.9 AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N | Certificate pinning bypass — OkHttp accepts a certificate chain containing a certificate from a non-pinned trusted CA plus the pinned certificate, bypassing pin enforcement and enabling MitM; CWE-295 | 2.7.4 / 3.1.2 | [GHSA-4hc2-jh7r-wrc3](https://github.com/advisories/GHSA-4hc2-jh7r-wrc3) |
| GHSA-3cqm-mf7h-prrj | High CVSS 7.5 AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N | Hostname verification bypass in OkHostnameVerifier.verifyHostName via improper crypto use on Android 8.1–11; allows attacker to present certificate for wrong domain; CWE-295 | 4.9.2 | [GHSA-3cqm-mf7h-prrj](https://github.com/advisories/GHSA-3cqm-mf7h-prrj) |
| CVE-2023-3782 / GHSA-w28c-cgxf-w8gv | Moderate CVSS 5.9 AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H | Brotli zip-bomb DoS via BrotliInterceptor — malicious web server or MitM injects Brotli-compressed payload causing client-side resource exhaustion; only affects callers using the optional BrotliInterceptor; CWE-400 | see upstream issue #7738 | [GHSA-w28c-cgxf-w8gv](https://github.com/advisories/GHSA-w28c-cgxf-w8gv) |

## Security Posture Notes

OkHttp is the dominant HTTP/HTTP2 client library for Android and JVM environments, maintained by Square Engineering. It is a transitive dependency of Retrofit (Android REST client), Coil, Picasso, Glide (with OkHttp integration), the OkHttp adapters for Spring WebClient and Micronaut, and many Apache Pulsar / Kafka tooling clients. The library has a strong security record relative to its usage volume.

All three confirmed advisories involve TLS/certificate handling or decompression boundaries rather than code execution or authentication bypass classes. The certificate pinning bypass (CVE-2016-2402) was the most widely cited: the fix required OkHttp to check that every certificate in a chain matches a known pin when pinning is configured. The Android hostname verification bypass (GHSA-3cqm-mf7h-prrj) is partly an interaction with the Android Conscrypt / platform TLS stack rather than a pure OkHttp code defect; OkHttp 4.9.2 works around affected Android versions.

The Brotli DoS (CVE-2023-3782) requires use of the optional `okhttp-brotli` interceptor artifact (not bundled in the main `okhttp` dependency) and a MitM or malicious-server position — it is client-side only, affects no server deployment, and has no fixed version listed in the GHSA record (mitigation: disable BrotliInterceptor or bound decompression size).

Current recommended minimum: **5.0.x** (stable since 2024, Android-first API). OkHttp 3.x and 4.x both carry the historical pinning bypass; 4.x ≥ 4.9.2 resolves the Android hostname verification issue.

## Dependencies of Note

- `com.squareup.okio:okio` — Square's buffered I/O library; OkHttp's core byte-stream layer. `okio` has had its own independent advisory history (not yet in this wiki).
- `org.conscrypt:conscrypt-android` — Android TLS provider; the hostname verification bypass interacts with Conscrypt's verifier behavior.

## Open Questions

- GHSA-w28c-cgxf-w8gv (CVE-2023-3782) has no fixed version in the advisory; confirm fix status from upstream issue #7738 and whether a patched `okhttp-brotli` artifact exists.
- Add a page for `com.squareup.okio:okio` — OkHttp's foundational I/O layer is widely used independently of OkHttp.
- Confirm whether OkHttp 5.x (Kotlin-rewrite) carries any new GHSA advisories not yet in the database.

## Related Pages

- [[maven/org.apache.httpcomponents.client5/httpclient5]] — Apache HTTP Client 5.x
- [[maven/index]]

---
*Last updated: 2026-09-22 | Sources: 3 (GHSA-4hc2-jh7r-wrc3, GHSA-3cqm-mf7h-prrj, GHSA-w28c-cgxf-w8gv)*
