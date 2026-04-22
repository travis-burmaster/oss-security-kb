# OSS Security KB — Master Index

*78 packages tracked across 8 ecosystems. Last updated: 2026-04-22.*

## npm (60)
- [[npm/axios]] — axios HTTP client · advisory mapped · SSRF / DoS / request-routing history plus 2026 supply-chain compromise
- [[npm/esbuild]] — JavaScript bundler / dev server · advisory mapped · dev-server CORS exposure fixed in 0.25.0
- [[npm/ip]] — IP address helper · advisory mapped · SSRF-relevant private/public classification bypasses including an unresolved incomplete-fix chain through 2.0.1
- [[npm/cookie-parser]] — Express cookie middleware · baseline stub · no package-level GHSA / OSV record confirmed in this pass, but relevant dependency context via cookie 0.7.x
- [[npm/cors]] — Express CORS middleware · baseline stub · no package-level GHSA / OSV record confirmed in this pass; main risk boundary is application configuration
- [[npm/http-proxy-middleware]] — proxy middleware · advisory mapped · path-filter DoS plus 2025 fixRequestBody flaw chain
- [[npm/braces]] — brace-expansion utility · advisory mapped · ReDoS in 2.x plus 2024 imbalanced-input memory exhaustion fixed in 3.0.3
- [[npm/marked]] — markdown parser · advisory mapped · repeated XSS / sanitization-boundary and ReDoS history
- [[npm/markdown-it]] — Markdown parser · advisory mapped · published ReDoS / resource-exhaustion history through 14.1.1
- [[npm/handlebars]] — templating engine · advisory mapped · long XSS / prototype-pollution / ACE history plus 2026 v4.7.9 fix cluster
- [[npm/helmet]] — security-header middleware · baseline stub · no package-level GHSA / OSV record confirmed in this pass; strong disclosure posture via upstream SECURITY.md
- [[npm/ws]] — WebSocket library · advisory mapped · repeated header-parser and resource-exhaustion / DoS history
- [[npm/tar]] — archive extraction library · advisory mapped · long-running symlink / hardlink traversal, overwrite, and path-sanitization history
- [[npm/tough-cookie]] — cookie-jar library · advisory mapped · parser ReDoS history plus the 2023 prototype-pollution fix in 4.1.3
- [[npm/basic-ftp]] — FTP client library · advisory mapped · 2026 5.2.x path-traversal and CRLF command-injection fix chain
- [[npm/validator]] — string validation / sanitization helper · advisory mapped · legacy XSS-filter lineage plus modern URL / length / regex-boundary fixes
- [[npm/webpack-dev-server]] — frontend dev server · advisory mapped · repeated origin / cross-origin source-code exposure in HMR and local script-loading paths
- [[npm/yaml]] — YAML parser · advisory mapped · degenerate-input exception handling plus 2026 deeply nested collection stack-overflow fix
- [[npm/body-parser]] — request body parsing middleware · advisory mapped · 1.x and 2.x urlencoded-parser DoS fixes plus parser-boundary review notes
- [[npm/cookie]] — cookie parser/serializer · advisory mapped · strict serialize validation, parse-side minimal by design
- [[npm/cookie-signature]] — signed-cookie helper · advisory mapped · historical timing-attack fix in 1.0.4
- [[npm/cross-spawn]] — process-spawn helper · advisory mapped · 2024 ReDoS fix chain across 6.x and 7.x
- [[npm/debug]] — debug logging utility · advisory mapped · supply-chain compromise in 4.4.2 plus older ReDoS history
- [[npm/ejs]] — server-side templating engine · advisory mapped · historical renderFile/input-validation bugs plus later SSTI and prototype-pollution hardening
- [[npm/fastify]] — high-performance Node.js web framework · advisory mapped · recurring Content-Type parsing / validation-boundary flaws plus proxy-trust and DoS history
- [[npm/express]] — dominant Node.js web framework · advisory mapped · public package history plus deeper 2026 source review
- [[npm/follow-redirects]] — redirect-following HTTP helper · advisory mapped · repeated redirect credential / header leakage history
- [[npm/form-data]] — multipart request builder · advisory mapped · 2025 predictable-boundary fix across 2.x, 3.x, and 4.x
- [[npm/got]] — HTTP client · advisory mapped · redirect-to-UNIX-socket boundary flaw fixed in 11.8.5 and 12.1.0
- [[npm/glob-parent]] — glob utility dependency · advisory mapped · two ReDoS fixes across 5.1.2 and 6.0.1
- [[npm/undici]] — modern HTTP client / fetch foundation · advisory mapped · recurring redirect leakage, CRLF injection, and 2026 WebSocket / DoS cluster
- [[npm/jsonwebtoken]] — token verification library · advisory mapped · verification-semantic and key-confusion history
- [[npm/js-yaml]] — YAML parser · audit ingested · historical RCE plus disputed 2026 alias-expansion DoS finding
- [[npm/serialize-javascript]] — JavaScript serialization helper · advisory mapped · repeated browser/SSR injection history plus 2026 CPU-exhaustion DoS
- [[npm/koa-router]] — Koa routing middleware · audit ingested · 2026 v15.4.0 source review, prefix-strip boundary bug filed as koajs/router#232
- [[npm/lodash]] — lodash utility library · advisory mapped · prototype pollution, ReDoS, and template-injection history
- [[npm/moment]] — date/time library · advisory mapped · legacy ReDoS history plus 2022 locale traversal and RFC2822 regex fixes
- [[npm/mathjs]] — math expression engine · advisory mapped · 15.2.0 object-attribute / parser hardening security fix
- [[npm/micromatch]] — glob / pattern matcher · advisory mapped · ReDoS fixed in 4.0.8 after earlier incomplete mitigation
- [[npm/morgan]] — HTTP request logger · advisory mapped · 2019 format-compilation code injection fixed in 1.9.1
- [[npm/multer]] — multipart upload middleware · advisory mapped · dense 2025-2026 DoS fix train from 2.0.0 through 2.1.1
- [[npm/mime]] — MIME lookup utility · advisory mapped · historical ReDoS fixed in 1.4.1 and 2.0.3
- [[npm/minimist]] — minimist argument parser · advisory mapped · high transitive risk
- [[npm/nanoid]] — ID generator · advisory mapped · collision/predictability flaws fixed in 3.1.31, 3.3.8, and 5.0.9
- [[npm/node-fetch]] — fetch-compatible HTTP client · advisory mapped · redirect credential leakage, redirect size-limit bypass, and ReDoS history
- [[npm/pac-resolver]] — PAC file parser / executor · advisory mapped · pre-5.0.0 code-injection history tied to unsafe PAC handling and the `degenerator` sandbox boundary
- [[npm/next-intl]] — internationalization middleware package · advisory mapped · 2026 open redirect fix in 4.9.1
- [[npm/passport]] — authentication middleware foundation · advisory mapped · pre-0.6.0 session-fixation issue in login/logout session handling
- [[npm/path-parse]] — path parsing ponyfill · advisory mapped · pre-1.0.7 ReDoS fixed in 1.0.7
- [[npm/path-to-regexp]] — route parser · advisory mapped · audit and ReDoS history
- [[npm/postcss]] — CSS parser / transform foundation · advisory mapped · source-map ReDoS pair plus 2023 carriage-return parsing integrity bug
- [[npm/qs]] — query-string parser · advisory mapped · prototype-pollution and parser-limit bypass history
- [[npm/semver]] — semver version parser · advisory mapped · ReDoS history
- [[npm/shell-quote]] — shell-escaping helper · advisory mapped · two published command-injection fixes with the later regex hardening in 1.7.3
- [[npm/send]] — static file serving engine · advisory mapped · three published package advisories across traversal, path disclosure, and redirect-template XSS
- [[npm/serve-static]] — Express static-file middleware · advisory mapped · small package-level advisory set around redirect handling and redirect-page XSS
- [[npm/tmp]] — temporary-file helper · advisory mapped · symlink-based temp-path boundary bypass fixed in 0.2.4
- [[npm/xml2js]] — XML-to-object parser · advisory mapped · prototype-pollution fix in 0.5.0 on untrusted object-construction paths
- [[npm/yargs-parser]] — CLI argument parser · advisory mapped · prototype-pollution fix coordinated across multiple major lines

## Rust / crates.io (3)
- [[rust/serde]] — foundational serialization framework · baseline stub · no direct package-scoped OSV / RustSec advisory confirmed in this pass, but very high ecosystem blast radius
- [[rust/serde_yaml_ng]] — active fork of archived serde_yaml · audit ingested · YAML 1.2 Core schema signed non-decimal integer parsing gap filed as acatton/serde-yaml-ng#32
- [[rust/tokio]] — async runtime foundation · advisory mapped · memory-safety / unsoundness and Windows named-pipe boundary history

## .NET / NuGet (2)
- [[dotnet/Newtonsoft.Json]] — dominant JSON library · advisory mapped · nested-input DoS fixed in 13.0.1 and safer depth defaults
- [[dotnet/System.Text.Json]] — core .NET JSON stack · advisory mapped · 2024 deserialization DoS fixes in 8.0.4 / 8.0.5 and 6.0.10

## Python / PyPI (4)
- [[python/flask]] — Python web framework · advisory mapped · JSON-input DoS plus session / cache / signing-boundary history
- [[python/jinja2]] — Python templating engine · advisory mapped · recurring sandbox breakouts, xmlattr injection, and ReDoS history
- [[python/requests]] — Python HTTP client · advisory mapped · redirect, proxy, TLS, and credential-handling history
- [[python/urllib3]] — transport-layer HTTP library · advisory mapped · redirect, CRLF, TLS, and request-smuggling relevance

## Go (6)
- [[go/github.com/gin-contrib/cors]] — standalone Gin CORS middleware · advisory mapped · wildcard-origin trust-boundary flaw fixed in 1.6.0
- [[go/github.com/gin-gonic/gin]] — high-usage Go web framework · advisory mapped · proxy-header, logging, and attachment-sanitization history
- [[go/github.com/gorilla/mux]] — established Go router · baseline stub · no package-scoped OSV / GitHub advisory confirmed in this pass, disclosure path unclear
- [[go/github.com/labstack/echo-v4]] — high-usage Go web framework line · advisory mapped · static-handler traversal and open-redirect history plus support-policy context
- [[go/golang.org-x-crypto]] — foundational Go crypto module · advisory mapped · repeated SSH boundary flaws plus cryptobyte, autocert, and openpgp security history
- [[go/google.golang.org/grpc]] — core Go RPC framework · advisory mapped · HTTP/2 rapid reset, authz bypass, and metadata/memory exposure history

## Homebrew (1)
- [[homebrew/openssl@3]] — cryptographic foundation formula · baseline stub · high-value macOS TLS/toolchain anchor for future package and patch-lag tracking

## Kubernetes (1)
- [[kubernetes/kube-apiserver]] — control-plane API surface · audit ingested · RBAC, admission, authn, and impersonation risk review

## Linux (1)
- [[linux/openssl]] — cross-distro cryptographic library anchor · baseline stub · upstream-first page for future distro normalization
