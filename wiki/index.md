# OSS Security KB — Master Index

*46 packages tracked across 8 ecosystems. Last updated: 2026-04-18.*

## npm (32)
- [[npm/axios]] — axios HTTP client · advisory mapped · SSRF / DoS / request-routing history plus 2026 supply-chain compromise
- [[npm/http-proxy-middleware]] — proxy middleware · advisory mapped · path-filter DoS plus 2025 fixRequestBody flaw chain
- [[npm/braces]] — brace-expansion utility · advisory mapped · ReDoS in 2.x plus 2024 imbalanced-input memory exhaustion fixed in 3.0.3
- [[npm/marked]] — markdown parser · advisory mapped · repeated XSS / sanitization-boundary and ReDoS history
- [[npm/handlebars]] — templating engine · advisory mapped · long XSS / prototype-pollution / ACE history plus 2026 v4.7.9 fix cluster
- [[npm/ws]] — WebSocket library · advisory mapped · repeated header-parser and resource-exhaustion / DoS history
- [[npm/tar]] — archive extraction library · advisory mapped · long-running symlink / hardlink traversal, overwrite, and path-sanitization history
- [[npm/basic-ftp]] — FTP client library · advisory mapped · 2026 5.2.x path-traversal and CRLF command-injection fix chain
- [[npm/validator]] — string validation / sanitization helper · advisory mapped · legacy XSS-filter lineage plus modern URL / length / regex-boundary fixes
- [[npm/body-parser]] — request body parsing middleware · advisory mapped · 1.x and 2.x urlencoded-parser DoS fixes plus parser-boundary review notes
- [[npm/cookie]] — cookie parser/serializer · audit ingested · strict serialize validation, parse-side minimal by design
- [[npm/cross-spawn]] — process-spawn helper · advisory mapped · 2024 ReDoS fix chain across 6.x and 7.x
- [[npm/debug]] — debug logging utility · advisory mapped · supply-chain compromise in 4.4.2 plus older ReDoS history
- [[npm/ejs]] — server-side templating engine · advisory mapped · historical renderFile/input-validation bugs plus later SSTI and prototype-pollution hardening
- [[npm/express]] — dominant Node.js web framework · audit ingested · public package history plus deeper 2026 source review
- [[npm/follow-redirects]] — redirect-following HTTP helper · advisory mapped · repeated redirect credential / header leakage history
- [[npm/undici]] — modern HTTP client / fetch foundation · advisory mapped · recurring redirect leakage, CRLF injection, and 2026 WebSocket / DoS cluster
- [[npm/jsonwebtoken]] — token verification library · advisory mapped · verification-semantic and key-confusion history
- [[npm/js-yaml]] — YAML parser · audit ingested · historical RCE plus disputed 2026 alias-expansion DoS finding
- [[npm/serialize-javascript]] — JavaScript serialization helper · advisory mapped · repeated browser/SSR injection history plus 2026 CPU-exhaustion DoS
- [[npm/koa-router]] — Koa routing middleware · audit ingested · 2026 v15.4.0 source review, prefix-strip boundary bug filed as koajs/router#232
- [[npm/lodash]] — lodash utility library · advisory mapped · prototype pollution, ReDoS, and template-injection history
- [[npm/mathjs]] — math expression engine · advisory mapped · 15.2.0 object-attribute / parser hardening security fix
- [[npm/morgan]] — HTTP request logger · advisory mapped · 2019 format-compilation code injection fixed in 1.9.1
- [[npm/minimist]] — minimist argument parser · advisory mapped · high transitive risk
- [[npm/node-fetch]] — fetch-compatible HTTP client · advisory mapped · redirect credential leakage, redirect size-limit bypass, and ReDoS history
- [[npm/next-intl]] — internationalization middleware package · advisory mapped · 2026 open redirect fix in 4.9.1
- [[npm/path-to-regexp]] — route parser · advisory mapped · audit and ReDoS history
- [[npm/qs]] — query-string parser · advisory mapped · prototype-pollution and parser-limit bypass history
- [[npm/semver]] — semver version parser · advisory mapped · ReDoS history
- [[npm/send]] — static file serving engine · audit ingested · historical traversal / path-disclosure advisories plus verified modern traversal defenses
- [[npm/serve-static]] — Express static-file middleware · advisory mapped · small package-level advisory set around redirect handling and redirect-page XSS
- [[npm/yargs-parser]] — CLI argument parser · advisory mapped · prototype-pollution fix coordinated across multiple major lines

## Rust / crates.io (3)
- [[rust/serde]] — foundational serialization crate · baseline stub · high downstream deserialization surface
- [[rust/serde_yaml_ng]] — active fork of archived serde_yaml · audit ingested · YAML 1.2 Core schema signed non-decimal integer parsing gap filed as acatton/serde-yaml-ng#32
- [[rust/tokio]] — async runtime foundation · advisory mapped · memory-safety / unsoundness and Windows named-pipe boundary history

## .NET / NuGet (2)
- [[dotnet/Newtonsoft.Json]] — dominant JSON library · advisory mapped · nested-input DoS fixed in 13.0.1 and safer depth defaults
- [[dotnet/System.Text.Json]] — core .NET JSON stack · advisory mapped · 2024 deserialization DoS fixes in 8.0.4 / 8.0.5 and 6.0.10

## Python / PyPI (2)
- [[python/requests]] — Python HTTP client · advisory mapped · redirect, proxy, TLS, and credential-handling history
- [[python/urllib3]] — transport-layer HTTP library · advisory mapped · redirect, CRLF, TLS, and request-smuggling relevance

## Go (4)
- [[go/github.com/gin-contrib/cors]] — standalone Gin CORS middleware · advisory mapped · wildcard-origin trust-boundary flaw fixed in 1.6.0
- [[go/github.com/gin-gonic/gin]] — high-usage Go web framework · advisory mapped · proxy-header, logging, and attachment-sanitization history
- [[go/golang.org-x-crypto]] — foundational Go crypto module · advisory mapped · repeated SSH boundary flaws plus cryptobyte, autocert, and openpgp security history
- [[go/google.golang.org/grpc]] — core Go RPC framework · advisory mapped · HTTP/2 rapid reset, authz bypass, and metadata/memory exposure history

## Homebrew (1)
- [[homebrew/openssl@3]] — cryptographic foundation formula · baseline stub · high-value macOS TLS/toolchain anchor for future package and patch-lag tracking

## Kubernetes (1)
- [[kubernetes/kube-apiserver]] — control-plane API surface · audit ingested · RBAC, admission, authn, and impersonation risk review

## Linux (1)
- [[linux/openssl]] — cross-distro cryptographic library anchor · baseline stub · upstream-first page for future distro normalization
