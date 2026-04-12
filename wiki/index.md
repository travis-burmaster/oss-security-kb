# OSS Security KB — Master Index

*16 packages tracked across 8 ecosystems. Last updated: 2026-04-12.*

## npm (12)
- [[npm/axios]] — axios HTTP client · advisory mapped · 2026 supply-chain compromise history
- [[npm/basic-ftp]] — FTP client library · advisory mapped · 2026 5.2.x path-traversal and CRLF command-injection fix chain
- [[npm/debug]] — debug logging utility · advisory mapped · supply-chain compromise in 4.4.2 plus older ReDoS history
- [[npm/express]] — dominant Node.js web framework · audit ingested · public package history plus deeper 2026 source review
- [[npm/jsonwebtoken]] — token verification library · advisory mapped · verification-semantic and key-confusion history
- [[npm/js-yaml]] — YAML parser · audit ingested · historical RCE plus 2026 alias-expansion DoS finding
- [[npm/lodash]] — lodash utility library · advisory mapped · prototype pollution history
- [[npm/mathjs]] — math expression engine · advisory mapped · 15.2.0 object-attribute / parser hardening security fix
- [[npm/minimist]] — minimist argument parser · advisory mapped · high transitive risk
- [[npm/next-intl]] — internationalization middleware package · advisory mapped · 2026 open redirect fix in 4.9.1
- [[npm/path-to-regexp]] — route parser · advisory mapped · legacy and modern ReDoS / route-expansion hardening history
- [[npm/semver]] — semver version parser · advisory mapped · ReDoS history

## Rust / crates.io (1)
- [[rust/serde]] — foundational serialization crate · baseline stub · high downstream deserialization surface

## .NET / NuGet (2)
- [[dotnet/Newtonsoft.Json]] — dominant JSON library · advisory mapped · nested-input DoS fixed in 13.0.1 and safer depth defaults
- [[dotnet/System.Text.Json]] — built-in .NET JSON stack · advisory mapped · 2024 deserialization DoS fixes in 8.0.4 / 8.0.5 and 6.0.10

## Python / PyPI (2)
- [[python/requests]] — Python HTTP client · advisory mapped · redirect, proxy, TLS, and credential-handling history
- [[python/urllib3]] — foundational HTTP transport library · advisory mapped · redirect, TLS, parser, and decompression vulnerability history

## Go (2)
- [[go/github.com/gin-gonic/gin]] — high-usage Go web framework · advisory mapped · proxy-header, logging, and attachment-sanitization history
- [[go/google.golang.org/grpc]] — core Go RPC framework · advisory mapped · HTTP/2 rapid reset, authz bypass, and metadata/memory exposure history

## Homebrew (0)
- _No package pages yet._

## Kubernetes (0)
- _No package pages yet._

## Linux (0)
- _No package pages yet._
