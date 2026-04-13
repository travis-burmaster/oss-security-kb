# OSS Security KB — Master Index

*28 packages tracked across 8 ecosystems. Last updated: 2026-04-13.*

## npm (17)
- [[npm/axios]] — axios HTTP client · advisory mapped · SSRF / DoS / request-routing history plus 2026 supply-chain compromise
- [[npm/basic-ftp]] — FTP client library · advisory mapped · 2026 5.2.x path-traversal and CRLF command-injection fix chain
- [[npm/body-parser]] — request body parsing middleware · audit ingested · parser-boundary review plus `allowPrototypes` concern in extended mode
- [[npm/cookie]] — cookie parser/serializer · audit ingested · strict serialize validation, parse-side minimal by design
- [[npm/debug]] — debug logging utility · advisory mapped · supply-chain compromise in 4.4.2 plus older ReDoS history
- [[npm/express]] — dominant Node.js web framework · audit ingested · public package history plus deeper 2026 source review
- [[npm/jsonwebtoken]] — token verification library · advisory mapped · verification-semantic and key-confusion history
- [[npm/js-yaml]] — YAML parser · audit ingested · historical RCE plus disputed 2026 alias-expansion DoS finding
- [[npm/koa-router]] — Koa routing middleware · baseline stub · routing-layer companion to path-to-regexp with audit history still sparse
- [[npm/lodash]] — lodash utility library · advisory mapped · prototype pollution history
- [[npm/mathjs]] — math expression engine · advisory mapped · 15.2.0 object-attribute / parser hardening security fix
- [[npm/minimist]] — minimist argument parser · advisory mapped · high transitive risk
- [[npm/next-intl]] — internationalization middleware package · advisory mapped · 2026 open redirect fix in 4.9.1
- [[npm/path-to-regexp]] — route parser · advisory mapped · audit and ReDoS history
- [[npm/qs]] — query-string parser · advisory mapped · prototype-pollution and parser-limit bypass history
- [[npm/semver]] — semver version parser · advisory mapped · ReDoS history
- [[npm/send]] — static file serving engine · audit ingested · path traversal defenses verified, symlink following by default

## Rust / crates.io (2)
- [[rust/serde]] — foundational serialization crate · baseline stub · high downstream deserialization surface
- [[rust/tokio]] — async runtime foundation · advisory mapped · memory-safety / unsoundness and Windows named-pipe boundary history

## .NET / NuGet (2)
- [[dotnet/Newtonsoft.Json]] — dominant JSON library · advisory mapped · nested-input DoS fixed in 13.0.1 and safer depth defaults
- [[dotnet/System.Text.Json]] — core .NET JSON stack · advisory mapped · 2024 deserialization DoS fixes in 8.0.4 / 8.0.5 and 6.0.10

## Python / PyPI (2)
- [[python/requests]] — Python HTTP client · advisory mapped · redirect, proxy, TLS, and credential-handling history
- [[python/urllib3]] — transport-layer HTTP library · advisory mapped · redirect, CRLF, TLS, and request-smuggling relevance

## Go (2)
- [[go/github.com/gin-gonic/gin]] — high-usage Go web framework · advisory mapped · proxy-header, logging, and attachment-sanitization history
- [[go/google.golang.org/grpc]] — core Go RPC framework · advisory mapped · HTTP/2 rapid reset, authz bypass, and metadata/memory exposure history

## Homebrew (1)
- [[homebrew/openssl@3]] — cryptographic foundation formula · baseline stub · high-value macOS TLS/toolchain anchor for future package and patch-lag tracking

## Kubernetes (1)
- [[kubernetes/kube-apiserver]] — control-plane API surface · audit ingested · RBAC, admission, authn, and impersonation risk review

## Linux (1)
- [[linux/openssl]] — cross-distro cryptographic library anchor · baseline stub · upstream-first page for future distro normalization
