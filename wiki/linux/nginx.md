# nginx (Linux)

**Registry:** distro (nginx.org APT/YUM repos, Debian/Ubuntu/RHEL packages)
**Weekly Downloads:** N/A — installed via OS package manager; among the top two most-deployed web servers globally
**Repository:** https://github.com/nginx/nginx (canonical since 2024) / historical: https://trac.nginx.org/nginx
**Security Contact:** https://nginx.org/en/security_advisories.html
**Disclosure Policy:** https://nginx.org/en/security_advisories.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-11-19 | OSS Security KB | GHSA database lookup + upstream changelog (`docs/xml/nginx/changes.xml`, mainline and stable-1.30 / stable-1.28 branches) | automated | 36 advisories published 2026-02-04 through 2026-11-18 mapped, including the 2026-11-18 "nginx2root" HTTP/2 / HTTP/3 / mail cluster | [github/advisory-database](https://github.com/github/advisory-database), [nginx changes.xml](https://github.com/nginx/nginx/blob/master/docs/xml/nginx/changes.xml) |
| 2026-06-22 | OSS Security KB | GHSA database lookup | automated | 6 representative public advisories mapped (CVE-2017-7529 through CVE-2024-7347) | [github/advisory-database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

Severity labels are the GitHub Advisory Database labels. Where a score is shown, it is the CVSS 3.1 base score calculated from the CVSS 3.1 vector in the GHSA record; GHSA's "Critical" label on several 2026 records reflects the CNA's CVSS 4.0 rating, so it can sit above the 3.1 score. Fixed versions come from the upstream nginx changelog: mainline 1.31.x, stable 1.30.x, and (for early-2026 fixes) stable 1.28.x.

### 2026 advisories (newest first)

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-123007 / GHSA-m4q8-cf44-f42r | Critical — CVSS 3.1 8.1 | **nginx2root.** HTTP/2 flow-control window integer underflow: crafted traffic pushes the flow-control window past its allowed threshold, causing a heap buffer overflow in the worker. Code execution is possible when ASLR is disabled or bypassed. Affects any configuration that uses HTTP/2. | 1.31.9, 1.30.7 | [GHSA-m4q8-cf44-f42r](https://github.com/advisories/GHSA-m4q8-cf44-f42r), [F5 K000163926](https://my.f5.com/manage/s/article/K000163926) |
| CVE-2026-123633 / GHSA-7xxj-p8w5-434q | Critical — CVSS 3.1 8.1 | **nginx2root.** Use-after-free when HTTP/2 client connections are proxied to a backend and the worker is running low on `worker_connections`. Code execution possible when ASLR is disabled or bypassed. | 1.31.9, 1.30.7 | [GHSA-7xxj-p8w5-434q](https://github.com/advisories/GHSA-7xxj-p8w5-434q), [F5 K000163928](https://my.f5.com/manage/s/article/K000163928) |
| CVE-2026-123634 / GHSA-qxf8-26hv-4jh5 | Critical — CVSS 3.1 8.1 | **nginx2root.** Use-after-free when nginx proxies to a server name containing variables and an SSI or `mirror` subrequest resolves the same server name. Code execution possible when ASLR is disabled or bypassed. | 1.31.9, 1.30.7 | [GHSA-qxf8-26hv-4jh5](https://github.com/advisories/GHSA-qxf8-26hv-4jh5), [F5 K000163925](https://my.f5.com/manage/s/article/K000163925) |
| CVE-2026-121810 / GHSA-fxx2-rrmx-x4v2 | Critical — CVSS 3.1 8.1 | **nginx2root.** Use-after-free in configurations that use HTTP/3; remote unauthenticated, with conditions beyond the attacker's control. Code execution possible when ASLR is disabled or bypassed. | 1.31.9, 1.30.7 | [GHSA-fxx2-rrmx-x4v2](https://github.com/advisories/GHSA-fxx2-rrmx-x4v2), [F5 K000163927](https://my.f5.com/manage/s/article/K000163927) |
| CVE-2026-113425 / GHSA-rmpv-v5m5-rr27 | Critical — CVSS 3.1 8.1 | **nginx2root.** Use-after-free in the mail proxy; remote unauthenticated attacker can crash or corrupt a worker, with code execution as a potential impact. | 1.31.9, 1.30.7 | [GHSA-rmpv-v5m5-rr27](https://github.com/advisories/GHSA-rmpv-v5m5-rr27), [F5 K000163931](https://my.f5.com/manage/s/article/K000163931) |
| CVE-2026-118899 / GHSA-mjqw-rmmf-hgxf | High — CVSS 3.1 7.5 | Infinite loop while reading the request body over TLS 1.3 on an `ssl` listener; the worker stops serving new and existing connections (unauthenticated DoS). | 1.31.9, 1.30.7 | [GHSA-mjqw-rmmf-hgxf](https://github.com/advisories/GHSA-mjqw-rmmf-hgxf), [F5 K000163930](https://my.f5.com/manage/s/article/K000163930) |
| CVE-2026-123640 / GHSA-c32q-x8cv-vhfr | Moderate — CVSS 3.1 5.3 | `ngx_stream_ssl_preread_module`: a crafted ClientHello forges preread variables, which can bypass stream routing segmentation and reach backends that should be unreachable. | 1.31.9, 1.30.7 | [GHSA-c32q-x8cv-vhfr](https://github.com/advisories/GHSA-c32q-x8cv-vhfr), [F5 K000163935](https://my.f5.com/manage/s/article/K000163935) |
| CVE-2026-125283 / GHSA-cgqq-hx2v-pf8c | Moderate — CVSS 3.1 5.3 | `try_files` plus `alias` with a `map` variable: certain regex capture combinations cause a buffer overflow and worker segfault. | 1.31.9, 1.30.7 | [GHSA-cgqq-hx2v-pf8c](https://github.com/advisories/GHSA-cgqq-hx2v-pf8c), [F5 K000163933](https://my.f5.com/manage/s/article/K000163933) |
| CVE-2026-120993 / GHSA-39qv-989q-vg33 | Moderate — CVSS 3.1 5.3 | Stream module with dynamic certificate loading plus `proxy_protocol` v2: an abbreviated TLS handshake terminates the worker (DoS). | 1.31.9 (mainline; not listed in the stable 1.30.7 changelog) | [GHSA-39qv-989q-vg33](https://github.com/advisories/GHSA-39qv-989q-vg33), [F5 K000163932](https://my.f5.com/manage/s/article/K000163932) |
| CVE-2026-120967 / GHSA-q9wg-m5cc-h828 | Moderate — CVSS 3.1 4.8 | Client certificate verification bypass when `ssl_verify_client on` is set in a non-default stream virtual server. | 1.31.9, 1.30.7 | [GHSA-q9wg-m5cc-h828](https://github.com/advisories/GHSA-q9wg-m5cc-h828), [F5 K000163934](https://my.f5.com/manage/s/article/K000163934) |
| CVE-2026-97205 / GHSA-ff5w-vvxc-fm9x | Critical — CVSS 3.1 8.1 | `ngx_http_core_module`: with AIO enabled, an SSI page using `include virtual` can trigger a use-after-free. Code execution possible when ASLR is disabled or bypassed. | 1.31.7, 1.30.6 | [GHSA-ff5w-vvxc-fm9x](https://github.com/advisories/GHSA-ff5w-vvxc-fm9x), [F5 K000162608](https://my.f5.com/manage/s/article/K000162608) |
| CVE-2026-93479 / GHSA-v72q-v4vf-2mx7 | Critical — CVSS 3.1 8.1 | Heap overflow when a regex `map`'s capture variables are referenced by `root` or a log format before the map output variable. Code execution possible when ASLR is disabled or bypassed. | 1.31.7, 1.30.6 | [GHSA-v72q-v4vf-2mx7](https://github.com/advisories/GHSA-v72q-v4vf-2mx7), [F5 K000162607](https://my.f5.com/manage/s/article/K000162607) |
| CVE-2026-15176 / GHSA-cvv4-j4mx-w8q5 | Critical — CVSS 3.1 8.1 | Heap overflow when `alias` is combined with `rewrite` and a `set`/`return` (or log format) referencing `$request_filename`. Code execution possible when ASLR is disabled or bypassed. | 1.31.7, 1.30.6 | [GHSA-cvv4-j4mx-w8q5](https://github.com/advisories/GHSA-cvv4-j4mx-w8q5), [F5 K000162416](https://my.f5.com/manage/s/article/K000162416) |
| CVE-2026-97629 / GHSA-qhwc-5g9q-3669 | High — CVSS 3.1 6.5 | With `ssl_session_cache shared:...` and no explicit `ssl_session_ticket_key`, an attacker can non-deterministically forge client TLS sessions and bypass client certificate verification. | 1.31.7, 1.30.6 | [GHSA-qhwc-5g9q-3669](https://github.com/advisories/GHSA-qhwc-5g9q-3669), [F5 K000162606](https://my.f5.com/manage/s/article/K000162606) |
| CVE-2026-95101 / GHSA-g6r5-95cx-mpp9 | Moderate — CVSS 3.1 5.3 | HTTP/3 with `proxy_request_buffering on`: attacker can inject data into the proxied request. | 1.31.7, 1.30.6 | [GHSA-g6r5-95cx-mpp9](https://github.com/advisories/GHSA-g6r5-95cx-mpp9), [F5 K000162613](https://my.f5.com/manage/s/article/K000162613) |
| CVE-2026-90439 / GHSA-fjgw-pmcm-g7j7 | Moderate — CVSS 3.1 6.5 | HTTP/3 built against OpenSSL 3.5.0 or earlier: limited heap overflow during the TLS handshake (worker restart or limited data corruption). | 1.31.6, 1.30.5 | [GHSA-fjgw-pmcm-g7j7](https://github.com/advisories/GHSA-fjgw-pmcm-g7j7), [F5 K000162604](https://my.f5.com/manage/s/article/K000162604) |
| CVE-2026-42533 / GHSA-fxfg-v4rj-hp95 | Critical — CVSS 3.1 8.1 | Heap overflow when a string expression references a regex `map`'s capture variables before the map output variable. Code execution possible when ASLR is disabled or bypassed. | 1.31.3, 1.30.4 | [GHSA-fxfg-v4rj-hp95](https://github.com/advisories/GHSA-fxfg-v4rj-hp95), [F5 K000162097](https://my.f5.com/manage/s/article/K000162097) |
| CVE-2026-60005 / GHSA-vxcv-h5wj-jxr5 | High — CVSS 3.1 8.2 | `ngx_http_slice_module` (not built by default): uninitialized memory access with unnamed regex captures or background cache updates, leading to limited memory disclosure or worker restart. | 1.31.3, 1.30.4 | [GHSA-vxcv-h5wj-jxr5](https://github.com/advisories/GHSA-vxcv-h5wj-jxr5), [F5 K000162100](https://my.f5.com/manage/s/article/K000162100) |
| CVE-2026-56434 / GHSA-m73p-xg7q-m8f2 | High — CVSS 3.1 6.5 | `ngx_http_ssi_module` with `proxy_pass` and `proxy_buffering off`: an attacker controlling upstream responses (MITM) can cause a heap over-read or worker restart. | 1.31.3, 1.30.4 | [GHSA-m73p-xg7q-m8f2](https://github.com/advisories/GHSA-m73p-xg7q-m8f2), [F5 K000162098](https://my.f5.com/manage/s/article/K000162098) |
| CVE-2026-42530 / GHSA-5mcp-3252-f5vr | Critical — CVSS 3.1 8.1 | HTTP/3: reopening a QPACK encoder stream causes a use-after-free. Code execution possible when ASLR is disabled or bypassed. | 1.31.2 (mainline; not listed in the stable 1.30.x changelog) | [GHSA-5mcp-3252-f5vr](https://github.com/advisories/GHSA-5mcp-3252-f5vr), [F5 K000161616](https://my.f5.com/manage/s/article/K000161616) |
| CVE-2026-42055 / GHSA-78jw-ww3g-9wp7 | Critical — CVSS 3.1 8.1 | HTTP/2 upstream proxying (`proxy_http_version 2` or `grpc_pass`) with `ignore_invalid_headers off` and `large_client_header_buffers` above 2 MB: heap overflow from large headers. Code execution possible when ASLR is disabled or bypassed. | 1.31.2, 1.30.3 | [GHSA-78jw-ww3g-9wp7](https://github.com/advisories/GHSA-78jw-ww3g-9wp7), [F5 K000161584](https://my.f5.com/manage/s/article/K000161584) |
| CVE-2026-48142 / GHSA-2388-jp8v-fg9w | Moderate — CVSS 3.1 4.8 | `ngx_http_charset_module` with `source_charset utf-8` and a `charset` directive: heap over-read (limited memory disclosure or restart). | 1.31.2, 1.30.3 | [GHSA-2388-jp8v-fg9w](https://github.com/advisories/GHSA-2388-jp8v-fg9w), [F5 K000161585](https://my.f5.com/manage/s/article/K000161585) |
| CVE-2026-9256 / GHSA-h78r-86c6-jgp4 | Critical — CVSS 3.1 8.1 | `ngx_http_rewrite_module`: overlapping PCRE captures (for example `^/((.*))$`) referenced together in a redirect or arguments replacement cause a heap overflow. Code execution possible when ASLR is disabled or bypassed. | 1.31.1, 1.30.2 | [GHSA-h78r-86c6-jgp4](https://github.com/advisories/GHSA-h78r-86c6-jgp4), [F5 K000161377](https://my.f5.com/manage/s/article/K000161377) |
| CVE-2026-42945 / GHSA-gcgv-v5gf-c543 | Critical — CVSS 3.1 8.1 | **"NGINX Rift."** `ngx_http_rewrite_module`: a `rewrite` followed by `rewrite`/`if`/`set` with an unnamed PCRE capture and a `?` in the replacement causes a heap overflow; code execution possible with ASLR disabled. VulnCheck reported in-the-wild exploitation days after disclosure (secondary report); not in the CISA KEV catalog as of catalog version 2026.11.18. | 1.31.0, 1.30.1 | [GHSA-gcgv-v5gf-c543](https://github.com/advisories/GHSA-gcgv-v5gf-c543), [F5 K000161019](https://my.f5.com/manage/s/article/K000161019) |
| CVE-2026-42946 / GHSA-fm65-xrrr-c358 | High — CVSS 3.1 6.5 | `ngx_http_scgi_module` / `ngx_http_uwsgi_module`: an attacker controlling upstream responses can cause excessive allocation or a heap over-read (memory disclosure or restart). | 1.31.0, 1.30.1 | [GHSA-fm65-xrrr-c358](https://github.com/advisories/GHSA-fm65-xrrr-c358), [F5 K000161027](https://my.f5.com/manage/s/article/K000161027) |
| CVE-2026-40460 / GHSA-h7rq-f9gq-mc8r | Moderate — CVSS 3.1 6.5 | HTTP/3 QUIC: source IP address spoofing can bypass address-based authorization or rate limiting. | 1.31.0, 1.30.1 | [GHSA-h7rq-f9gq-mc8r](https://github.com/advisories/GHSA-h7rq-f9gq-mc8r), [F5 K000161068](https://my.f5.com/manage/s/article/K000161068) |
| CVE-2026-42926 / GHSA-v43f-895r-chhh | Moderate — CVSS 3.1 5.8 | HTTP/2 upstream proxying with `proxy_set_body`: attacker can inject HTTP/2 frame headers and payload bytes to the upstream peer. | 1.31.0, 1.30.1 | [GHSA-v43f-895r-chhh](https://github.com/advisories/GHSA-v43f-895r-chhh), [F5 K000161131](https://my.f5.com/manage/s/article/K000161131) |
| CVE-2026-42934 / GHSA-6vmc-2wh4-77qp | Moderate — CVSS 3.1 4.8 | `ngx_http_charset_module` with `charset_map` and unbuffered `proxy_pass`: heap over-read (limited disclosure or restart). | 1.31.0, 1.30.1 | [GHSA-6vmc-2wh4-77qp](https://github.com/advisories/GHSA-6vmc-2wh4-77qp), [F5 K000161028](https://my.f5.com/manage/s/article/K000161028) |
| CVE-2026-40701 / GHSA-x88q-x2r7-vg3g | Moderate — CVSS 3.1 4.8 | `ngx_http_ssl_module` with `ssl_verify_client` and `ssl_ocsp`: heap use-after-free in the worker. | 1.31.0, 1.30.1 | [GHSA-x88q-x2r7-vg3g](https://github.com/advisories/GHSA-x88q-x2r7-vg3g), [F5 K000161021](https://my.f5.com/manage/s/article/K000161021) |
| CVE-2026-27654 / GHSA-6r46-2qjx-j5j3 | High — CVSS 3.1 8.2 | `ngx_http_dav_module` MOVE/COPY with a prefix location and `alias`: buffer overflow that can crash the worker or rename files outside the document root. | 1.29.7, 1.28.3 | [GHSA-6r46-2qjx-j5j3](https://github.com/advisories/GHSA-6r46-2qjx-j5j3), [F5 K000160382](https://my.f5.com/manage/s/article/K000160382) |
| CVE-2026-32647 / GHSA-6364-x4qj-7w59 | High — CVSS 3.1 7.8 | `ngx_http_mp4_module`: crafted MP4 causes worker memory over-read or over-write, with possible code execution. | 1.29.7, 1.28.3 | [GHSA-6364-x4qj-7w59](https://github.com/advisories/GHSA-6364-x4qj-7w59), [F5 K000160366](https://my.f5.com/manage/s/article/K000160366) |
| CVE-2026-27784 / GHSA-hwq5-42j9-jvqj | High — CVSS 3.1 7.8 | `ngx_http_mp4_module` on 32-bit builds only: crafted MP4 causes worker memory over-read or over-write. | 1.29.7, 1.28.3 | [GHSA-hwq5-42j9-jvqj](https://github.com/advisories/GHSA-hwq5-42j9-jvqj), [F5 K000160364](https://my.f5.com/manage/s/article/K000160364) |
| CVE-2026-27651 / GHSA-82w2-x7hf-5h8r | High — CVSS 3.1 7.5 | `ngx_mail_auth_http_module` with CRAM-MD5 or APOP and an auth server that returns `Auth-Wait`: NULL dereference terminates the worker. | 1.29.7, 1.28.3 | [GHSA-82w2-x7hf-5h8r](https://github.com/advisories/GHSA-82w2-x7hf-5h8r), [F5 K000160383](https://my.f5.com/manage/s/article/K000160383) |
| CVE-2026-28755 / GHSA-hgfr-jmpr-2p89 | Moderate — CVSS 3.1 5.4 | `ngx_stream_ssl_module` with `ssl_verify_client on` and `ssl_ocsp on`: TLS handshake succeeds even when OCSP marks the client certificate revoked. | 1.29.7, 1.28.3 | [GHSA-hgfr-jmpr-2p89](https://github.com/advisories/GHSA-hgfr-jmpr-2p89), [F5 K000160368](https://my.f5.com/manage/s/article/K000160368) |
| CVE-2026-28753 / GHSA-ggr6-fmr8-2m8g | Moderate — CVSS 3.1 3.7 | `ngx_mail_smtp_module`: CRLF in DNS responses lets an attacker-controlled DNS server inject headers into the upstream SMTP connection. | 1.29.7, 1.28.3 | [GHSA-ggr6-fmr8-2m8g](https://github.com/advisories/GHSA-ggr6-fmr8-2m8g), [F5 K000160367](https://my.f5.com/manage/s/article/K000160367) |
| CVE-2026-1642 / GHSA-7chh-rv6q-8pp3 | High — CVSS 3.1 5.9 | Proxying to upstream TLS servers: an attacker with a MITM position on the upstream side can inject plain-text data into the proxied response. | 1.29.5, 1.28.2 | [GHSA-7chh-rv6q-8pp3](https://github.com/advisories/GHSA-7chh-rv6q-8pp3), [F5 K000159824](https://my.f5.com/manage/s/article/K000159824) |

### Earlier advisories (representative)

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-7347 / GHSA-3r23-64c4-mj87 | Moderate — CVSS 7.1 | `ngx_http_mp4_module` worker memory over-read: a specially crafted MP4 file can trigger an over-read of worker process memory, resulting in worker termination. Same module / configuration prerequisites as the 2022 MP4 cluster. Affects NGINX Open Source and NGINX Plus; versions that have reached End of Technical Support are not evaluated by upstream. | 1.27.1 (mainline), 1.26.2 (stable) | [GHSA-3r23-64c4-mj87](https://github.com/advisories/GHSA-3r23-64c4-mj87) |
| CVE-2022-41742 / GHSA-wj45-j4gh-fm3x | High | `ngx_http_mp4_module` worker memory disclosure: companion to CVE-2022-41741 in the same module and release cycle; a crafted audio or video file can cause a worker process crash or disclose portions of worker memory. Same scope and configuration prerequisites as CVE-2022-41741. | 1.23.2 (mainline), 1.22.1 (stable) | [GHSA-wj45-j4gh-fm3x](https://github.com/advisories/GHSA-wj45-j4gh-fm3x) |
| CVE-2022-41741 / GHSA-3v5h-538g-pr7g | High — CVSS 7.8 | `ngx_http_mp4_module` memory corruption: a local attacker who can supply a specially crafted MP4 file for processing can corrupt nginx worker memory, potentially causing worker termination or other impact. Affects only builds with `--with-http_mp4_module` when the `mp4` directive is active in the configuration. | 1.23.2 (mainline), 1.22.1 (stable) | [GHSA-3v5h-538g-pr7g](https://github.com/advisories/GHSA-3v5h-538g-pr7g) |
| CVE-2021-23017 / GHSA-83p9-mcpm-374v | Critical — CVSS 9.4 | DNS resolver off-by-one heap overwrite: an attacker who can forge UDP DNS responses can trigger a 1-byte memory overwrite in the nginx resolver via an off-by-one write, potentially causing worker process crash or, under favorable memory layout conditions, arbitrary code execution. Exploitable only when the `resolver` directive is configured. | 1.21.0 (mainline), 1.20.1 (stable) | [GHSA-83p9-mcpm-374v](https://github.com/advisories/GHSA-83p9-mcpm-374v) |
| CVE-2019-20372 / GHSA-c9vh-3f9g-f2xf | Medium — CVSS 5.3 | HTTP request smuggling via `error_page`: nginx before 1.17.7 allowed HTTP request smuggling in certain `error_page` configurations when deployed behind a load balancer, enabling attackers to read web pages not intended for them. Requires a specific server configuration combining `error_page` with upstream proxying. | 1.17.7 | [GHSA-c9vh-3f9g-f2xf](https://github.com/advisories/GHSA-c9vh-3f9g-f2xf) |
| CVE-2017-7529 / GHSA-85mj-h68w-w736 | High — CVSS 7.5 | Integer overflow in the range filter module: nginx versions 0.5.6 through 1.13.2 were vulnerable to an integer overflow in `ngx_http_range_filter_module` when processing crafted HTTP `Range` headers. The overflow could leak potentially sensitive information from worker memory to the attacker. | 1.13.3 (mainline), 1.12.1 (stable) | [GHSA-85mj-h68w-w736](https://github.com/advisories/GHSA-85mj-h68w-w736) |

*Live record: https://github.com/advisories?query=nginx and https://nginx.org/en/security_advisories.html*

## Security Posture Notes

nginx is one of the two most-deployed HTTP servers and reverse proxies globally, running in high-traffic production infrastructure and serving as the default ingress in many Kubernetes clusters. Its attack surface spans the HTTP/1.1, HTTP/2 and HTTP/3 (QUIC) parsers, the optional stream/mail modules, the DNS resolver, and optional media-serving modules.

**2026 advisory volume:** 36 CVEs were fixed between nginx 1.29.5 (2026-02-04) and 1.31.9 / 1.30.7 (2026-11-18). Thirteen carry a GHSA "Critical" label, and most of those are heap overflows or use-after-frees where F5 states code execution is possible when ASLR is disabled or bypassed. Anyone not on 1.31.9 (mainline) or 1.30.7 (stable) as of 2026-11-19 is missing at least nine of these fixes.

**"nginx2root" cluster (2026-11-18):** Five memory-safety CVEs (CVE-2026-123007, -123633, -123634, -121810, -113425) were disclosed together under the "nginx2root" name (Xint write-up and nginx2root.com are referenced from the GHSA records), alongside five lower-severity fixes in the same release. CVE-2026-123007 (HTTP/2 flow-control underflow) needs only HTTP/2 to be enabled, which makes it the broadest-reach item. The upstream fix commits are referenced in the GHSA records (for example nginx commit `b89c4100` for CVE-2026-123007 and `0c87dd1d` for CVE-2026-123633).

**Recurring classes in 2026:**
- *Regex capture handling in `rewrite` / `map`:* CVE-2026-42945, CVE-2026-9256, CVE-2026-42533, CVE-2026-93479, CVE-2026-15176 and CVE-2026-125283 are all buffer overflows driven by how PCRE captures are sized and reused across directives. Configurations with complex `rewrite`, `map`, `alias` and `try_files` logic carry the most exposure.
- *HTTP/2 and HTTP/3:* CVE-2026-123007, -123633, -121810, -42530, -42055, -42926, -95101, -90439 and -40460. Sites that do not need HTTP/3 should leave QUIC listeners off.
- *Client certificate verification bypasses:* CVE-2026-28755, CVE-2026-97629 and CVE-2026-120967. Deployments that rely on mTLS for authorization should treat these as authentication bypasses.
- *`ngx_http_mp4_module`:* CVE-2026-32647 and CVE-2026-27784 continue the 2022 to 2024 pattern. Sites that do not need MP4 pseudo-streaming should omit `--with-http_mp4_module` or the `mp4` directive.

**Exploitation status:** CVE-2026-42945 was reported as exploited in the wild by VulnCheck shortly after its 2026-05-13 disclosure (reported by Security Affairs and others; secondary sources). No nginx CVE appears in the CISA KEV catalog as of catalog version 2026.11.18.

**Excluded from this page:** CVE-2026-50107 (GHSA-gx48-gh32-62q5) is a configuration-injection bug in the NGINX Gateway Fabric control plane, not in nginx itself, and is not listed in the nginx changelog. It belongs on a future Gateway Fabric page.

**DNS resolver risk (CVE-2021-23017):** The `resolver` directive is off by default; enabling it against untrusted or attacker-influenced DNS opens one of the highest-severity attack classes in nginx's public history. CVE-2026-28753 (mail SMTP CRLF via DNS responses) is a newer example of resolver-sourced data crossing a trust boundary.

**HTTP request smuggling (CVE-2019-20372):** nginx is frequently deployed as the terminating proxy behind load balancers. CVE-2026-42926 and CVE-2026-95101 are newer request-injection bugs on the HTTP/2 and HTTP/3 upstream paths.

**Distro package lag:** Distro packages (Debian, Ubuntu, RHEL) may lag upstream nginx releases by days to weeks and usually backport fixes without changing the upstream version number. Check the distro security tracker rather than the version string.

**nginx Ingress Controller:** Running nginx inside Kubernetes as an Ingress controller adds the Lua extensibility layer and admission-controller attack surface; see [[kubernetes/ingress-nginx]] for that project's separate CVE history.

## Dependencies of Note

- **OpenSSL / BoringSSL / LibreSSL** — TLS implementation linked at build time. CVE-2026-90439 affects HTTP/3 builds against OpenSSL 3.5.0 and earlier specifically. See [[linux/openssl]].
- **PCRE / PCRE2** — used for `location`, `rewrite` and `map` regex matching; six 2026 CVEs involve capture handling in this path.
- **zlib / libatomic_ops** — no specific advisories flagged for this pass.

## Open Questions

- The 2026 table was assembled from GHSA code search plus the upstream `changes.xml`; nginx.org and F5 article pages were not reachable from this environment. A future pass should reconcile against https://nginx.org/en/security_advisories.html directly, including the "vulnerable" version ranges F5 publishes for each CVE.
- Confirm whether CVE-2026-120993 and CVE-2026-42530 affect the stable 1.30 branch at all (neither appears in the stable 1.30.x changelog).
- Map pre-2017 advisories for completeness; nginx has security advisories back to 2009.
- Track whether any nginx2root CVE is added to the CISA KEV catalog.
- Check Debian stable / Ubuntu LTS backport status for the 2026-11-18 fixes.

## Related Pages

- [[linux/openssl]]
- [[linux/curl]]
- [[kubernetes/ingress-nginx]]
- [[linux/index]]

---
*Last updated: 2026-11-19 | Sources: github/advisory-database (42 GHSA records listed above), nginx `docs/xml/nginx/changes.xml` on master / stable-1.30 / stable-1.28, F5 knowledge-base articles referenced from each GHSA record, CISA KEV catalog 2026.11.18 (cisagov/kev-data)*
