# npm Index

## Advisory-Mapped / Audited Pages
- [[npm/axios]] — widely used HTTP client · advisory mapped · broad SSRF / DoS / request-routing history plus 2026 supply-chain compromise
- [[npm/ws]] — widely used WebSocket library · advisory mapped · repeated header-parser and resource-exhaustion / DoS history
- [[npm/tar]] — archive extraction library · advisory mapped · long-running symlink / hardlink traversal, overwrite, and path-sanitization history
- [[npm/basic-ftp]] — FTP client library · advisory mapped · 2026 5.2.x path-traversal and CRLF command-injection fix chain
- [[npm/debug]] — debug logging utility · advisory mapped · supply-chain compromise in 4.4.2 plus older ReDoS history
- [[npm/express]] — core web framework · audit ingested · public package history plus a deeper 2026 source review
- [[npm/jsonwebtoken]] — JWT verification surface · advisory mapped · 9.0.0 security watershed and one rejected CVE to interpret carefully
- [[npm/js-yaml]] — YAML parser · audit ingested · historical RCE plus 2026 alias-expansion DoS finding
- [[npm/lodash]] — utility library · advisory mapped · prototype pollution, ReDoS, and template-injection history
- [[npm/mathjs]] — math expression engine · advisory mapped · 15.2.0 object-attribute / parser hardening security fix
- [[npm/minimist]] — tiny CLI parser with outsized transitive blast radius
- [[npm/next-intl]] — i18n / routing middleware package · advisory mapped · 2026 open redirect fix in 4.9.1
- [[npm/path-to-regexp]] — routing parser · advisory mapped · legacy and modern ReDoS / route-expansion hardening history
- [[npm/qs]] — query-string parser · advisory mapped · prototype-pollution and parser-limit bypass history
- [[npm/semver]] — version parsing infrastructure · advisory mapped · ReDoS history
- [[npm/cookie]] — cookie parser/serializer · audit ingested · strict serialize validation, parse-side minimal by design
- [[npm/body-parser]] — request body parsing middleware · advisory mapped · 1.x and 2.x urlencoded-parser DoS fixes plus audit notes on parser boundaries
- [[npm/send]] — static file serving engine · audit ingested · historical traversal / path-disclosure advisories plus verified modern traversal defenses
- [[npm/koa-router]] — Koa routing middleware · audit ingested · 2026 v15.4.0 source review, prefix-strip boundary bug filed as koajs/router#232
