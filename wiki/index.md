# OSS Security KB — Master Index

*197 tracked pages across 9 ecosystems. Last updated: 2026-06-23.*

## npm (93)

- [[npm/axios]] — axios HTTP client · advisory mapped · SSRF / DoS / request-routing / prototype-pollution gadget history plus 2026 supply-chain compromise
- [[npm/ajv]] — JSON Schema validator · advisory mapped · prototype-pollution and `$data` / pattern ReDoS history across 6.x and 8.x
- [[npm/async]] — async control-flow utility · advisory mapped · prototype-pollution issue fixed in 2.6.4 and 3.2.2
- [[npm/graphql]] — GraphQL reference implementation · advisory mapped · 2023 overlapping-fields resource-exhaustion / DoS fixed in 16.8.1
- [[npm/react]] — core UI library · advisory mapped · two legacy pre-1.0 XSS records, with no newer direct package-level OSV / GHSA issue surfaced in this pass
- [[npm/react-server-dom-webpack]] — React Server Components webpack transport package · advisory mapped · 2025-2026 RSC RCE, source-code exposure, and DoS fix train through 19.0.5 / 19.1.6 / 19.2.5
- [[npm/zod]] — schema validation library · advisory mapped · 2023 email-validation ReDoS / DoS fixed in 3.22.3
- [[npm/esbuild]] — JavaScript bundler / dev server · advisory mapped · dev-server CORS exposure fixed in 0.25.0
- [[npm/vite]] — dominant frontend build tool / dev server · advisory mapped · dense dev-server file-boundary, cross-origin exposure, and XSS history through the 2026 fix train
- [[npm/ip]] — IP address helper · advisory mapped · SSRF-relevant private/public classification bypasses including an unresolved incomplete-fix chain through 2.0.1
- [[npm/cookie-parser]] — Express cookie middleware · baseline stub · no package-level GHSA / OSV record confirmed in this pass, but relevant dependency context via cookie 0.7.x
- [[npm/cors]] — Express CORS middleware · baseline stub · no package-level GHSA / OSV record confirmed in this pass; main risk boundary is application configuration
- [[npm/http-proxy]] — foundational Node.js proxy library · advisory mapped · direct package-level DoS history fixed through 1.18.1
- [[npm/http-proxy-middleware]] — proxy middleware · advisory mapped · path-filter DoS plus 2025 fixRequestBody flaw chain
- [[npm/braces]] — brace-expansion utility · advisory mapped · ReDoS in 2.x plus 2024 imbalanced-input memory exhaustion fixed in 3.0.3
- [[npm/brace-expansion]] — brace expansion parser utility · advisory mapped · ReDoS and zero-step sequence DoS history fixed across maintained major lines through 5.0.5
- [[npm/marked]] — markdown parser · advisory mapped · repeated XSS / sanitization-boundary and ReDoS history
- [[npm/markdown-it]] — Markdown parser · advisory mapped · published ReDoS / resource-exhaustion history through 14.1.1
- [[npm/handlebars]] — templating engine · advisory mapped · long XSS / prototype-pollution / ACE history plus 2026 v4.7.9 fix cluster
- [[npm/highlight.js]] — syntax highlighter · advisory mapped · prototype pollution plus grammar-driven ReDoS / freeze history fixed through 10.4.1
- [[npm/prismjs]] — syntax highlighter · advisory mapped · plugin XSS, grammar ReDoS, and DOM-clobbering history fixed through 1.30.0
- [[npm/protobufjs]] — protobuf serialization library · advisory mapped · prototype-pollution / generated-code injection and parser DoS history through the 7.5.6 / 8.0.2 fix train
- [[npm/mdast-util-to-hast]] — Markdown AST→HTML AST transformer · advisory mapped · class-injection / unsanitized class attribute issue fixed in 13.2.1
- [[npm/merge]] — object merge utility · advisory mapped · prototype-pollution CVEs fixed in 1.2.1 and 2.1.1
- [[npm/helmet]] — security-header middleware · baseline stub · no package-level GHSA / OSV record confirmed in this pass; strong disclosure posture via upstream SECURITY.md
- [[npm/ws]] — WebSocket library · advisory mapped · repeated header-parser and resource-exhaustion / DoS history
- [[npm/tar]] — archive extraction library · advisory mapped · long-running symlink / hardlink traversal, overwrite, and path-sanitization history
- [[npm/tar-fs]] — tar extraction helper · advisory mapped · recurring archive extraction boundary flaws across hardlinks, symlinks, and path traversal fixes through 3.1.1
- [[npm/tough-cookie]] — cookie-jar library · advisory mapped · parser ReDoS history plus the 2023 prototype-pollution fix in 4.1.3
- [[npm/vue]] — core frontend framework package · advisory mapped · currently one published package-level Vue 2 ReDoS record in public sources
- [[npm/basic-ftp]] — FTP client library · advisory mapped · 2026 5.2.x path-traversal and CRLF command-injection fix chain
- [[npm/validator]] — string validation / sanitization helper · advisory mapped · legacy XSS-filter lineage plus modern URL / length / regex-boundary fixes
- [[npm/webpack-dev-server]] — frontend dev server · advisory mapped · repeated origin / cross-origin source-code exposure in HMR and local script-loading paths
- [[npm/yaml]] — YAML parser · advisory mapped · degenerate-input exception handling plus 2026 deeply nested collection stack-overflow fix
- [[npm/body-parser]] — request body parsing middleware · advisory mapped · 1.x and 2.x urlencoded-parser DoS fixes plus parser-boundary review notes
- [[npm/cookie]] — cookie parser/serializer · advisory mapped · strict serialize validation, parse-side minimal by design
- [[npm/cookie-signature]] — signed-cookie helper · advisory mapped · historical timing-attack fix in 1.0.4
- [[npm/cross-spawn]] — process-spawn helper · advisory mapped · 2024 ReDoS fix chain across 6.x and 7.x
- [[npm/debug]] — debug logging utility · advisory mapped · supply-chain compromise in 4.4.2 plus older ReDoS history
- [[npm/openssl]] — deprecated OpenSSL CLI wrapper · advisory mapped · critical command-execution advisory with no published fix version
- [[npm/ejs]] — server-side templating engine · advisory mapped · historical renderFile/input-validation bugs plus later SSTI and prototype-pollution hardening
- [[npm/elliptic]] — JavaScript elliptic-curve crypto library · advisory mapped · signature malleability, ECDH validation, ECDSA private-key extraction, and one currently unfixed deterministic-`k` advisory
- [[npm/node-forge]] — JavaScript cryptography / PKI toolkit · advisory mapped · signature-verification, certificate-chain, ASN.1 parser, BigInteger DoS, URL parsing, and prototype-pollution history through 1.4.0
- [[npm/fastify]] — high-performance Node.js web framework · advisory mapped · recurring Content-Type parsing / validation-boundary flaws plus proxy-trust and DoS history
- [[npm/express]] — dominant Node.js web framework · advisory mapped · public package history plus deeper 2026 source review
- [[npm/express-session]] — HTTP session middleware for Express · baseline stub · high-usage package with no direct GHSA / OSV advisories confirmed at package level; notable dependency-context risk via `cookie` 0.7.x lineage and `cookie-signature` timing-attack fix history
- [[npm/follow-redirects]] — redirect-following HTTP helper · advisory mapped · repeated redirect credential / header leakage history
- [[npm/form-data]] — multipart request builder · advisory mapped · 2025 predictable-boundary fix across 2.x, 3.x, and 4.x
- [[npm/got]] — HTTP client · advisory mapped · redirect-to-UNIX-socket boundary flaw fixed in 11.8.5 and 12.1.0
- [[npm/glob-parent]] — glob utility dependency · advisory mapped · two ReDoS fixes across 5.1.2 and 6.0.1
- [[npm/glob]] — glob CLI/library package · advisory mapped · CLI `-c` / `--cmd` command-injection flaw fixed in 10.5.0 / 11.1.0
- [[npm/undici]] — modern HTTP client / fetch foundation · advisory mapped · recurring redirect leakage, CRLF injection, and 2026 WebSocket / DoS cluster
- [[npm/jsonwebtoken]] — token verification library · advisory mapped · verification-semantic and key-confusion history
- [[npm/js-yaml]] — YAML parser · audit ingested · historical RCE plus disputed 2026 alias-expansion DoS finding
- [[npm/serialize-javascript]] — JavaScript serialization helper · advisory mapped · repeated browser/SSR injection history plus 2026 CPU-exhaustion DoS
- [[npm/koa]] — Koa web framework · advisory mapped · ReDoS, redirect-helper XSS, open-redirect, and host-header injection history through 2.16.2 / 3.1.2
- [[npm/koa-router]] — Koa routing middleware · audit ingested · 2026 v15.4.0 source review, prefix-strip boundary bug filed as koajs/router#232
- [[npm/loader-utils]] — webpack ecosystem utility · advisory mapped · 2022 ReDoS pair plus prototype-pollution fixes across 1.x, 2.x, and 3.x
- [[npm/lodash]] — lodash utility library · advisory mapped · prototype pollution, ReDoS, and template-injection history
- [[npm/moment]] — date/time library · advisory mapped · legacy ReDoS history plus 2022 locale traversal and RFC2822 regex fixes
- [[npm/mathjs]] — math expression engine · advisory mapped · 15.2.0 object-attribute / parser hardening security fix
- [[npm/micromatch]] — glob / pattern matcher · advisory mapped · ReDoS fixed in 4.0.8 after earlier incomplete mitigation
- [[npm/minimatch]] — glob pattern matcher · advisory mapped · ReDoS / catastrophic backtracking history fixed across maintained major lines through 2026
- [[npm/morgan]] — HTTP request logger · advisory mapped · 2019 format-compilation code injection fixed in 1.9.1
- [[npm/multer]] — multipart upload middleware · advisory mapped · dense 2025-2026 DoS fix train from 2.0.0 through 2.1.1
- [[npm/mime]] — MIME lookup utility · advisory mapped · historical ReDoS fixed in 1.4.1 and 2.0.3
- [[npm/minimist]] — minimist argument parser · advisory mapped · high transitive risk
- [[npm/react-router]] — routing framework/library · advisory mapped · mode-sensitive 6.x/7.x history across cache poisoning, SSR XSS, redirects, and CSRF fixes through 7.12.0
- [[npm/nanoid]] — ID generator · advisory mapped · collision/predictability flaws fixed in 3.1.31, 3.3.8, and 5.0.9
- [[npm/nth-check]] — selector parser utility · advisory mapped · pre-2.0.1 regex-complexity DoS fixed by parser rewrite
- [[npm/node-fetch]] — fetch-compatible HTTP client · advisory mapped · redirect credential leakage, redirect size-limit bypass, and ReDoS history
- [[npm/uuid]] — foundational UUID generation utility · advisory mapped · 2026 caller-supplied buffer bounds-checking flaw fixed in 14.0.0
- [[npm/pug]] — templating engine · advisory mapped · compiler-option code-execution fixes in 3.0.1 and 3.0.3
- [[npm/pac-resolver]] — PAC file parser / executor · advisory mapped · pre-5.0.0 code-injection history tied to unsafe PAC handling and the `degenerator` sandbox boundary
- [[npm/next]] — Next.js framework · advisory mapped · 42 public OSV/GHSA records through 2026 covering middleware auth bypasses, Server Actions / RSC issues, image optimizer DoS, cache poisoning, SSRF, request smuggling, and RCE
- [[npm/next-intl]] — internationalization middleware package · advisory mapped · 2026 open redirect fix in 4.9.1
- [[npm/passport]] — authentication middleware foundation · advisory mapped · pre-0.6.0 session-fixation issue in login/logout session handling
- [[npm/path-parse]] — path parsing ponyfill · advisory mapped · pre-1.0.7 ReDoS fixed in 1.0.7
- [[npm/path-to-regexp]] — route parser · advisory mapped · audit and ReDoS history
- [[npm/postcss]] — CSS parser / transform foundation · advisory mapped · source-map ReDoS pair plus 2023 carriage-return parsing integrity bug
- [[npm/qs]] — query-string parser · advisory mapped · prototype-pollution and parser-limit bypass history
- [[npm/semver]] — semver version parser · audit ingested · ReDoS hardening reviewed
- [[npm/dompurify]] — HTML sanitizer · advisory mapped · dense mutation-XSS / configuration-bypass history plus recent 3.3.2 and 3.4.0 hardening releases
- [[npm/sanitize-html]] — HTML sanitizer · advisory mapped · repeated XSS / sanitization-bypass, input-validation, ReDoS, and information-exposure fixes through 2.17.3
- [[npm/shell-quote]] — shell-escaping helper · advisory mapped · two published command-injection fixes with the later regex hardening in 1.7.3
- [[npm/send]] — static file serving engine · advisory mapped · three published package advisories across traversal, path disclosure, and redirect-template XSS
- [[npm/serve-static]] — Express static-file middleware · advisory mapped · small package-level advisory set around redirect handling and redirect-page XSS
- [[npm/sharp]] — image processing library · advisory mapped · install-time build-environment injection plus bundled libwebp exposure
- [[npm/tmp]] — temporary-file helper · advisory mapped · symlink-based temp-path boundary bypass fixed in 0.2.4
- [[npm/xml2js]] — XML-to-object parser · advisory mapped · prototype-pollution fix in 0.5.0 on untrusted object-construction paths
- [[npm/xmldom]] — legacy XML DOM package family · advisory mapped · unscoped package remains frozen while the scoped fork carries the 2021-2026 fix train
- [[npm/y18n]] — localization helper · advisory mapped · prototype-pollution fix coordinated across 3.x, 4.x, and 5.x
- [[npm/yargs-parser]] — CLI argument parser · advisory mapped · prototype-pollution fix coordinated across multiple major lines

## Rust / crates.io (13)
- [[rust/base64]] — base64 encoding/decoding library · advisory mapped · RUSTSEC-2017-0004 heap overflow in encode path (CVSS 9.8), fixed in 0.5.2; ~250M weekly downloads
- [[rust/chrono]] — dominant date-and-time library · advisory mapped · RUSTSEC-2020-0159 / CVE-2020-26235 localtime_r segfault via concurrent env-var mutation, fixed in 0.4.20
- [[rust/h2]] — HTTP/2 implementation · advisory mapped · resource-exhaustion / DoS history through 0.3.26 / 0.4.4
- [[rust/hyper]] — foundational Rust HTTP implementation · advisory mapped · HTTP/1 parser/request-smuggling, header-injection, TLS hostname-verification, and parser soundness history
- [[rust/openssl]] — Rust bindings for OpenSSL · advisory mapped · 10 RUSTSEC advisories across MitM / use-after-free / arbitrary file read / UB / thread-safety history through RUSTSEC-2025-0022
- [[rust/regex]] — canonical Rust regex engine · advisory mapped · RUSTSEC-2022-0013 / CVE-2022-24713 complexity-limit ReDoS fixed in 1.5.5; ~183M weekly downloads
- [[rust/ring]] — widely used Rust cryptographic library · advisory mapped · RUSTSEC-2025-0009 / CVE-2025-4432 AES/QUIC overflow-check panic DoS fixed in 0.17.12; 0.16.x unmaintained (RUSTSEC-2025-0010)
- [[rust/rustls]] — dominant pure-Rust TLS implementation · advisory mapped · RUSTSEC-2024-0336 close_notify DoS (High) and RUSTSEC-2024-0399 fragmented-ClientHello panic DoS through 0.23.18
- [[rust/serde]] — foundational serialization framework · baseline stub · no direct package-scoped OSV / RustSec advisory confirmed in this pass, but very high ecosystem blast radius
- [[rust/serde_json]] — de facto standard Rust JSON library · baseline stub · no direct package-scoped RustSec/GHSA advisory confirmed; 1B+ all-time crates.io downloads; high ecosystem blast radius
- [[rust/serde_yaml_ng]] — active fork of archived serde_yaml · audit ingested · YAML 1.2 Core schema signed non-decimal integer parsing gap filed as acatton/serde-yaml-ng#32
- [[rust/reqwest]] — dominant Rust HTTP client · advisory mapped · no direct RustSec/GHSA advisories on record; ~126M weekly downloads with high ecosystem exposure
- [[rust/tokio]] — async runtime foundation · advisory mapped · memory-safety / unsoundness and Windows named-pipe boundary history

## .NET / NuGet (5)
- [[dotnet/Microsoft.IdentityModel.JsonWebTokens]] — Microsoft JWT library · advisory mapped · CVE-2024-21319 JWE compression bomb DoS fixed in 7.1.2 / 6.34.0 / 5.7.0
- [[dotnet/Newtonsoft.Json]] — dominant JSON library · advisory mapped · nested-input DoS fixed in 13.0.1 and safer depth defaults
- [[dotnet/SixLabors.ImageSharp]] — .NET image processing library · advisory mapped · 7 GHSA advisories (CVE-2024-27929 through CVE-2025-54575) across PNG/JPEG/TGA/GIF decoders: use-after-free, memory-exhaustion DoS, data leakage, OOB write, and infinite-loop history
- [[dotnet/System.Text.Json]] — core .NET JSON stack · advisory mapped · 2024 deserialization DoS fixes in 8.0.4 / 8.0.5 and 6.0.10
- [[dotnet/System.Security.Cryptography.Xml]] — encrypted XML support · advisory mapped · 5 public XML-processing / information-disclosure / EncryptedXml advisories

## Python / PyPI (33)
- [[python/litellm]] — LLM gateway/proxy package · advisory mapped · proxy vulnerabilities plus March 2026 malicious PyPI release incident
- [[python/telnyx]] — Telnyx SDK · advisory mapped · March 2026 malicious PyPI release incident (PYSEC-2026-3 / GHSA-955r-262c-33jc / MAL-2026-2254)
- [[python/flask]] — Python web framework · advisory mapped · JSON-input DoS plus session / cache / signing-boundary history
- [[python/flask-cors]] — Flask CORS extension · advisory mapped · directory traversal plus 2024 CORS matching / private-network-header / debug-log injection fix train through 6.0.0
- [[python/jinja2]] — Python templating engine · advisory mapped · recurring sandbox breakouts, xmlattr injection, and ReDoS history
- [[python/pyyaml]] — YAML parser and emitter for Python · advisory mapped · long-running unsafe-deserialization / arbitrary-code-execution vulnerability chain addressed through successive fixes up to version 5.4
- [[python/lxml]] — XML / HTML parser and libxml2 binding · advisory mapped · recurring HTML-cleaner XSS bypasses plus parser DoS / XXE history through 6.1.0
- [[python/bleach]] — HTML sanitization library · advisory mapped · URI-scheme bypass, repeated mutation-XSS allowlist pitfalls, and style-attribute ReDoS history through 3.3.0
- [[python/python-jose]] — JOSE / JWT implementation · advisory mapped · HMAC timing, ECDSA key algorithm-confusion, and compressed-JWE DoS history through 3.4.0
- [[python/pyjwt]] — JWT implementation · advisory mapped · key-confusion, issuer partial-match, and JOSE `crit` header verification-boundary history through 2.12.0
- [[python/django]] — Python web framework · advisory mapped · mature public security-release archive with recurring SQL-injection, ASGI/header-boundary, upload-limit, cache/session, traversal, and DoS history through 2026
- [[python/pillow]] — Python Imaging Library fork · advisory mapped · dense parser-boundary history across image decoder memory corruption, decompression / allocation DoS, ImageMath code execution, and 2026 PSD / FITS / PDF fixes through 12.2.0
- [[python/pip]] — Python package installer · advisory mapped · archive-extraction, VCS reference, installer import-order, and legacy transport / temp-dir security history through 26.1
- [[python/setuptools]] — Python packaging/build backend toolkit · advisory mapped · package-index transport, parsing, command-execution, and download path-traversal history through 78.1.1
- [[python/requests]] — Python HTTP client · advisory mapped · redirect, proxy, TLS, and credential-handling history
- [[python/redis]] — Redis client / redis-py · advisory mapped · async connection-cancellation race-condition data-leak chain fixed through 4.4.4 / 4.5.4
- [[python/httpx]] — async/sync Python HTTP client · advisory mapped · URL input-validation issue with public fixed-version discrepancy
- [[python/h11]] — pure-Python HTTP/1.1 state machine · advisory mapped · malformed chunked-transfer parsing / request-smuggling boundary fixed in 0.16.0
- [[python/urllib3]] — transport-layer HTTP library · advisory mapped · redirect, CRLF, TLS, and request-smuggling relevance
- [[python/cryptography]] — foundational Python cryptography library · advisory mapped · primitive, X.509/PKCS, buffer-boundary, and bundled-OpenSSL wheel history
- [[python/paramiko]] — Python SSH2 protocol library · advisory mapped · server-mode authentication bypasses, private-key file race, SSH Terrapin, legacy randomness, and 2026 SHA-1 algorithm record
- [[python/aiohttp]] — async HTTP client/server framework · advisory mapped · parser / request-smuggling, static-file exposure, redirect leakage, multipart, and DoS history through 3.13.4
- [[python/gunicorn]] — WSGI HTTP server · advisory mapped · CRLF response/header injection plus 2024 HTTP request/response-smuggling parser-boundary fixes through 22.0.0
- [[python/uvicorn]] — ASGI HTTP server · advisory mapped · 2020 log-injection and HTTP response-splitting records fixed in 0.11.7
- [[python/werkzeug]] — foundational WSGI / request utility library · advisory mapped · debugger, multipart-parser, and Windows path-containment history through 3.1.6
- [[python/starlette]] — ASGI framework/toolkit · advisory mapped · multipart-parser and file-serving DoS / path-containment history through 0.49.1
- [[python/fastapi]] — ASGI web framework · advisory mapped · CSRF content-type parsing and dependency-mediated multipart ReDoS history through 0.109.1
- [[python/python-multipart]] — streaming multipart/form-data parser · advisory mapped · parser DoS, Content-Type ReDoS, part-header limits, and non-default upload-path traversal history through 0.0.27
- [[python/sqlalchemy]] — Python SQL toolkit / ORM · advisory mapped · compact but critical SQL-injection history around unsafe textual coercion in SQL construction APIs
- [[python/pydantic]] — Python data-validation library · advisory mapped · compact DoS history in date / datetime and email-validation boundaries
- [[python/celery]] — distributed task queue · advisory mapped · result-backend metadata command-injection and legacy worker privilege-dropping history
- [[python/twisted]] — Python event-driven networking framework · advisory mapped · HTTP parser/request-smuggling, TLS validation, redirect/header exposure, HTTP pipelining, SSH/DNS/HTTP2 DoS history through CVE-2026-42304
- [[python/tornado]] — Python web framework and async networking library · advisory mapped · HTTP request-smuggling, cookie / multipart DoS, CRLF / cookie-attribute injection, open redirect, and legacy XSRF side-channel history through 6.5.5

## Go (16)
- [[go/github.com/gin-contrib/cors]] — standalone Gin CORS middleware · advisory mapped · wildcard-origin trust-boundary flaw fixed in 1.6.0
- [[go/github.com/gin-gonic/gin]] — high-usage Go web framework · advisory mapped · proxy-header, logging, and attachment-sanitization history
- [[go/github.com/go-chi/chi]] — widely used Go router · advisory mapped · `RedirectSlashes` open-redirect and incomplete-fix chain through 5.2.4
- [[go/github.com/golang-jwt/jwt]] — Go JWT implementation · advisory mapped · v4 ParseWithClaims error-handling boundary plus ParseUnverified memory-allocation DoS history through 4.5.2 / 5.2.2
- [[go/github.com/gorilla/mux]] — established Go router · baseline stub · no package-scoped OSV / GitHub advisory confirmed in this pass, disclosure path unclear
- [[go/github.com/gorilla/schema]] — form decoder · advisory mapped · sparse slice-index deserialization memory-exhaustion DoS fixed in v1.4.1
- [[go/github.com/gorilla/websocket]] — foundational Go WebSocket implementation · advisory mapped · integer-overflow / read-limit bypass DoS fixed in 1.4.1
- [[go/github.com/labstack/echo-v4]] — high-usage Go web framework line · advisory mapped · static-handler traversal and open-redirect history plus support-policy context
- [[go/github.com/prometheus/client_golang]] — Prometheus Go instrumentation library · advisory mapped · promhttp method-label cardinality DoS fixed in 1.11.1
- [[go/go.opentelemetry.io/otel]] — core OpenTelemetry-Go API / propagation module · advisory mapped · multi-value W3C baggage header allocation-amplification DoS fixed in 1.41.0
- [[go/golang.org-x-crypto]] — foundational Go crypto module · advisory mapped · repeated SSH boundary flaws plus cryptobyte, autocert, and openpgp security history
- [[go/golang.org-x-net]] — foundational Go networking module · advisory mapped · HTTP/2 DoS / request-smuggling, HTML rendering / parser, and proxy-boundary history through 2025
- [[go/google.golang.org/grpc]] — core Go RPC framework · advisory mapped · HTTP/2 rapid reset, authz bypass, and metadata/memory exposure history
- [[go/google.golang.org/protobuf]] — foundational Go protobuf implementation · advisory mapped · prototext panic and protojson infinite-loop DoS history
- [[go/go.etcd.io/etcd-v3]] — distributed key-value store (Kubernetes backing store) · advisory mapped · 18 advisories spanning CSRF, RBAC bypass, WAL DoS, gateway TLS/auth issues, credential logging, debug-endpoint RCE (CVE-2021-28235), and 2026 gRPC auth-bypass cluster fixed in 3.6.9–3.6.11
- [[go/golang.org-x-text]] — foundational Go text / i18n / Unicode module · advisory mapped · UTF-16 decoder infinite loop, BCP 47 language tag OOB read panic, and ParseAcceptLanguage quadratic-time DoS through 0.3.8

## Homebrew (1)
- [[homebrew/openssl@3]] — cryptographic foundation formula · baseline stub · high-value macOS TLS/toolchain anchor for future package and patch-lag tracking

## Maven / Java (25)
- [[maven/commons-fileupload/commons-fileupload]] — Apache Commons FileUpload multipart parser · advisory mapped · 1.x arbitrary-file-write, deserialization/RCE, temporary-file, and multipart DoS history fixed through 1.6.0
- [[maven/commons-io/commons-io]] — Apache Commons IO utility library · advisory mapped · path-normalization traversal and `XmlStreamReader` resource-consumption history fixed through 2.14.0
- [[maven/com.google.guava/guava]] — Google Guava core Java utility library · advisory mapped · deserialization allocation DoS plus local temp-file / temp-directory exposure history fixed through the 24.1.1 and 32.0.x lines
- [[maven/org.apache.commons/commons-lang3]] — Apache Commons Lang utility library · advisory mapped · `ClassUtils.getClass(...)` uncontrolled-recursion DoS fixed in 3.18.0
- [[maven/com.fasterxml.jackson.core/jackson-databind]] — Jackson data-binding library · advisory mapped · dense polymorphic-deserialization gadget CVE history plus XXE and resource-exhaustion records through 2022
- [[maven/org.apache.commons/commons-compress]] — Apache Commons archive compression/extraction library · advisory mapped · malformed archive DoS / resource-exhaustion history fixed through 1.26.0
- [[maven/org.apache.logging.log4j/log4j-core]] — Apache Log4j Core logging implementation · advisory mapped · Log4Shell / JNDI, socket deserialization, TLS hostname verification, structured-layout log injection, and log-event-loss history fixed through 2.25.4 on the 2.x line
- [[maven/org.apache.httpcomponents/httpclient]] — Apache HttpComponents HttpClient 4.x · advisory mapped · TLS hostname-verification, proxy credential leakage, SSL-handshake DoS, and malformed-URI host-confusion history through 4.5.13 / 5.0.3
- [[maven/org.apache.httpcomponents.client5/httpclient5]] — Apache HttpComponents HttpClient 5.x · advisory mapped · TLS domain-check regression and SCRAM-SHA-256 mutual-authentication verification history through 5.6.1
- [[maven/org.apache.kafka/kafka-clients]] — Apache Kafka Java client library · advisory mapped · OAUTHBEARER / JWT validation, producer buffer-pool misrouting, client config file/SSRF, sensitive logging, and impersonation history through 4.2.0
- [[maven/org.apache.zookeeper/zookeeper]] — Apache ZooKeeper coordination service · advisory mapped · quorum auth, AdminServer, ACL / watcher, TLS hostname-verification, logging exposure, and DoS history through 3.9.5
- [[maven/org.yaml/snakeyaml]] — SnakeYAML YAML parser · advisory mapped · unsafe Java object construction / deserialization RCE, alias expansion, nested collection resource exhaustion, and parser stack-overflow DoS history through 2.0+
- [[maven/io.netty/netty-codec-http]] — Netty HTTP/1.x codec · advisory mapped · request-smuggling / parser-boundary, response-splitting, CRLF injection, decompression DoS, and local disclosure history through the 4.1.133.Final / 4.2.13.Final fix cluster
- [[maven/org.eclipse.jetty/jetty-server]] — Eclipse Jetty server core artifact · advisory mapped · HTTP request-smuggling / parser-boundary, resource-exhaustion DoS, information-disclosure, error-response XSS, session/logout, cookie, gzip, and TLS handling history through 2026
- [[maven/org.apache.tomcat.embed/tomcat-embed-core]] — Apache Tomcat embedded servlet-container core · advisory mapped · HTTP parsing, HTTP/2 and multipart DoS, security-constraint / CLIENT_CERT auth bypass, open redirect, and logging / information-disclosure history through 2026
- [[maven/org.bouncycastle/bcprov-jdk18on]] — Bouncy Castle Java cryptography provider · advisory mapped · timing side channels, certificate / ASN.1 DoS, LDAP injection, and DNS-poisoning-relevant certificate-validation history fixed through 1.84
- [[maven/org.bouncycastle/bcpkix-jdk18on]] — Bouncy Castle Java PKIX / certificate package · advisory mapped · PEM / ASN.1 DoS, PKIX certificate-path allocation, and composite-signature validation history fixed through 1.84
- [[maven/org.springframework/spring-core]] — Spring Framework core package · advisory mapped · path/resource handling, authorization-boundary, logging, JSONP, deserialization, and web DoS history through CVE-2025-41249
- [[maven/org.springframework/spring-web]] — Spring Framework web foundation artifact · advisory mapped · URL parsing / host validation, RFD, conditional-request DoS, DataBinder, deserialization, XML-input DoS, XST, CSRF, and response-generation history through 2025
- [[maven/org.springframework/spring-webflux]] — Spring WebFlux reactive web framework artifact · advisory mapped · data-binding RCE, functional static-resource path traversal, CORS / RFD boundaries, script-template file disclosure, SSE integrity, multipart temp-file DoS, static-resource DoS, and cache poisoning through 2026
- [[maven/org.springframework/spring-webmvc]] — Spring MVC web framework artifact · advisory mapped · data-binding RCE, static-resource/path traversal, XXE, CSRF/request-matching, RFD/XSS, cache-poisoning, SSE integrity, and DoS history through 2026
- [[maven/org.springframework.security/spring-security-core]] — Spring Security core module · advisory mapped · authorization / authentication bypass, method-security annotation, cryptographic, deserialization, security-context, and DoS / enumeration history through 2026
- [[maven/org.springframework.security/spring-security-config]] — Spring Security configuration module · advisory mapped · WebFlux / servlet request-matcher and servlet-path authorization-boundary history through 2026
- [[maven/org.springframework.security/spring-security-web]] — Spring Security web module · advisory mapped · request-matcher bypass, WebFlux static-resource authorization, security-header, SecurityContext, and X.509 identity-extraction history through 2026
- [[maven/org.geotools/gt-complex]] — GeoTools complex feature / XPath handling · advisory mapped · XPath-expression evaluation RCE risk when fed untrusted expressions (CVE-2024-36404)

## Kubernetes (5)
- [[kubernetes/containerd]] — container runtime (OCI/CRI) · advisory mapped · 21 GHSA advisories spanning CRI plugin boundary failures, UID mishandling, side-channel exposure, and 2026 checkpoint/restore exploitation cluster through CVE-2026-53492
- [[kubernetes/helm]] — CNCF-graduated Kubernetes package manager · advisory mapped · 27 GHSA advisories spanning Helm 2 Tiller TLS/symlink, plugin zip-slip and injection, lookup data leakage, credential forwarding, strvals OOM/stack-overflow, chartutil JSON-schema panics, and 2026 Helm v4 plugin path traversal cluster through CVE-2026-35204
- [[kubernetes/kube-apiserver]] — control-plane API surface · audit ingested · RBAC, admission, authn, and impersonation risk review
- [[kubernetes/kubelet]] — node agent · advisory mapped · privilege assignment, DoS, adjacent-network access, seccomp bypass, Windows command injection, gitRepo RCE, and checkpoint-API disk-fill history through CVE-2025-0426
- [[kubernetes/runc]] — OCI low-level container execution runtime · advisory mapped · /proc/self/exe container escape, TOCTOU mount race, capabilities elevation, access-control regression, AppArmor/SELinux bypass, and CVE-2024-21626 fd-leak container breakout through 1.1.12

## Linux (6)
- [[linux/cve-2026-31431-copy-fail]] — Linux kernel Copy Fail advisory note · advisory mapped · page-cache write / local privilege escalation discussion from public write-up
- [[linux/curl]] — CLI/library URL transfer tool · advisory mapped · SOCKS5 heap overflow, OCSP stapling bypass, use-after-free, and credential/protocol-selection history through CVE-2025-0167
- [[linux/nginx]] — dominant web server and reverse proxy · advisory mapped · range-filter integer overflow, HTTP request smuggling, critical DNS resolver off-by-one, and ngx_http_mp4_module memory-corruption/disclosure cluster through CVE-2024-7347
- [[linux/openssl]] — cross-distro cryptographic library anchor · baseline stub · upstream-first page for future distro normalization
- [[linux/openssh]] — remote access daemon · advisory mapped · ssh-agent PKCS#11 RCE, regreSSHion SIGALRM race, Terrapin, and VerifyHostKeyDNS MITM history through 9.9p2
- [[linux/sudo]] — privilege-boundary package · advisory mapped · pwfeedback, Baron Samedit, host-option, and chroot local privilege-escalation history
