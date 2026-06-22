# nginx (Linux)

**Registry:** distro (nginx.org APT/YUM repos, Debian/Ubuntu/RHEL packages)
**Weekly Downloads:** N/A — installed via OS package manager; among the top two most-deployed web servers globally
**Repository:** https://trac.nginx.org/nginx (canonical Mercurial) / mirror: https://github.com/nginx/nginx
**Security Contact:** https://nginx.org/en/security_advisories.html
**Disclosure Policy:** https://nginx.org/en/security_advisories.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-22 | OSS Security KB | GHSA database lookup | automated | 6 representative public advisories mapped (CVE-2017-7529 through CVE-2024-7347) | [github/advisory-database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-7529 / GHSA-85mj-h68w-w736 | High — CVSS 7.5 | Integer overflow in the range filter module: nginx versions 0.5.6 through 1.13.2 were vulnerable to an integer overflow in `ngx_http_range_filter_module` when processing crafted HTTP `Range` headers. The overflow could leak potentially sensitive information from worker memory to the attacker. | 1.13.3 (mainline), 1.12.1 (stable) | [GHSA-85mj-h68w-w736](https://github.com/advisories/GHSA-85mj-h68w-w736) |
| CVE-2019-20372 / GHSA-c9vh-3f9g-f2xf | Medium — CVSS 5.3 | HTTP request smuggling via `error_page`: nginx before 1.17.7 allowed HTTP request smuggling in certain `error_page` configurations when deployed behind a load balancer, enabling attackers to read web pages not intended for them. Requires a specific server configuration combining `error_page` with upstream proxying. | 1.17.7 | [GHSA-c9vh-3f9g-f2xf](https://github.com/advisories/GHSA-c9vh-3f9g-f2xf) |
| CVE-2021-23017 / GHSA-83p9-mcpm-374v | Critical — CVSS 9.4 | DNS resolver off-by-one heap overwrite: an attacker who can forge UDP DNS responses can trigger a 1-byte memory overwrite in the nginx resolver via an off-by-one write, potentially causing worker process crash or, under favorable memory layout conditions, arbitrary code execution. Exploitable only when the `resolver` directive is configured. | 1.21.0 (mainline), 1.20.1 (stable) | [GHSA-83p9-mcpm-374v](https://github.com/advisories/GHSA-83p9-mcpm-374v) |
| CVE-2022-41741 / GHSA-3v5h-538g-pr7g | High — CVSS 7.8 | `ngx_http_mp4_module` memory corruption: a local attacker who can supply a specially crafted MP4 file for processing can corrupt nginx worker memory, potentially causing worker termination or other impact. Affects only builds with `--with-http_mp4_module` when the `mp4` directive is active in the configuration. | 1.23.2 (mainline), 1.22.1 (stable) | [GHSA-3v5h-538g-pr7g](https://github.com/advisories/GHSA-3v5h-538g-pr7g) |
| CVE-2022-41742 / GHSA-wj45-j4gh-fm3x | High | `ngx_http_mp4_module` worker memory disclosure: companion to CVE-2022-41741 in the same module and release cycle; a crafted audio or video file can cause a worker process crash or disclose portions of worker memory. Same scope and configuration prerequisites as CVE-2022-41741. | 1.23.2 (mainline), 1.22.1 (stable) | [GHSA-wj45-j4gh-fm3x](https://github.com/advisories/GHSA-wj45-j4gh-fm3x) |
| CVE-2024-7347 / GHSA-3r23-64c4-mj87 | Moderate — CVSS 7.1 | `ngx_http_mp4_module` worker memory over-read: a specially crafted MP4 file can trigger an over-read of worker process memory, resulting in worker termination. Same module / configuration prerequisites as the 2022 MP4 cluster. Affects NGINX Open Source and NGINX Plus; versions that have reached End of Technical Support are not evaluated by upstream. | 1.27.1 (mainline), 1.26.2 (stable) | [GHSA-3r23-64c4-mj87](https://github.com/advisories/GHSA-3r23-64c4-mj87) |

## Security Posture Notes

nginx is one of the two most-deployed HTTP servers and reverse proxies globally, running in high-traffic production infrastructure and serving as the default ingress in most Kubernetes clusters (nginx Ingress Controller). Its attack surface spans the HTTP/1.1 and HTTP/2 parsers, the optional stream/mail modules, the DNS resolver, and optional media-serving modules.

**Recurring vulnerability class — `ngx_http_mp4_module`:** CVE-2022-41741, CVE-2022-41742, and CVE-2024-7347 form a persistent pattern of memory corruption/disclosure bugs in the optional MP4 streaming module. Sites that do not need MP4 pseudo-streaming should compile without `--with-http_mp4_module` or omit the `mp4` configuration directive.

**DNS resolver risk (CVE-2021-23017):** The `resolver` directive is off by default; enabling it against untrusted or attacker-influenced DNS opens the highest-severity attack class in nginx's public history. Prefer `resolver_timeout` and pin resolver IPs to trusted hosts when the directive is required.

**HTTP request smuggling (CVE-2019-20372):** nginx is frequently deployed as the terminating proxy behind load balancers (ELB, haproxy, Cloudflare). HTTP/1.1 request-smuggling is an ongoing ecosystem challenge; CVE-2019-20372 specifically depends on certain `error_page` configurations and requires the proxy chain.

**Distro package lag:** Distro packages (Debian, Ubuntu, RHEL/CentOS) may lag behind upstream nginx releases by days to weeks. The nginx.org official APT/YUM repositories track upstream mainline and stable branches more closely.

**nginx Ingress Controller:** Running nginx inside Kubernetes as an Ingress controller adds the Lua extensibility layer and admission-controller attack surface; the controller's own CVE history (separate from core nginx) should be reviewed separately.

## Dependencies of Note

- **OpenSSL / BoringSSL / LibreSSL** — TLS implementation bundled or linked at build time; nginx TLS vulnerabilities often follow upstream OpenSSL advisories. See [[linux/openssl]].
- **PCRE / PCRE2** — used for `location` and `rewrite` regex matching; ReDoS in complex regex configurations is possible.
- **zlib / libatomic_ops** — no specific advisories flagged for this pass.

## Open Questions

- Map earlier range-filter era advisories (pre-2017) for completeness; nginx has security advisories back to 2009 on nginx.org/en/security_advisories.html.
- Review the nginx Ingress Controller CVE list (separate from core nginx) for a future Kubernetes-ecosystem sub-page.
- Check whether CVE-2024-7347 fixed version (1.27.1 / 1.26.2) matches what is available in Debian stable / Ubuntu LTS at the time of a future pass.

## Related Pages

- [[linux/openssl]]
- [[linux/curl]]
- [[linux/index]]

---
*Last updated: 2026-06-22 | Sources: github/advisory-database (GHSA-85mj-h68w-w736, GHSA-c9vh-3f9g-f2xf, GHSA-83p9-mcpm-374v, GHSA-3v5h-538g-pr7g, GHSA-wj45-j4gh-fm3x, GHSA-3r23-64c4-mj87), nginx.org/en/security_advisories.html*
