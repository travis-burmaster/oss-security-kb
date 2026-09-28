# OSS Security KB — Master Index

*305 tracked pages across 9 ecosystems. Last updated: 2026-09-28.*

## npm (94)

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
- [[npm/lodash]] — utility library · advisory mapped · prototype-pollution chain across multiple CVEs through 4.17.21
- [[npm/underscore]] — utility library · advisory mapped · prototype-pollution issue fixed in 1.13.0-2
- [[npm/moment]] — date library · advisory mapped · ReDoS in date-format parsing fixed in 2.29.4
- [[npm/dayjs]] — date library · advisory mapped · prototype-pollution issue fixed in 1.10.8
- [[npm/date-fns]] — date library · advisory mapped · prototype-pollution issue fixed in 1.30.1 and 2.28.0
- [[npm/ua-parser-js]] — user-agent parser · advisory mapped · supply-chain compromise (malicious publish, Oct 2021) and ReDoS history
- [[npm/node-fetch]] — Fetch API for Node.js · advisory mapped · SSRF (host header injection), timeout / abort-signal DoS history
- [[npm/node-forge]] — cryptography library · advisory mapped · RSA PKCS#1 padding oracle, XSS in util.setPath, and URL parsing confusion history through 1.3.1
- [[npm/got]] — HTTP client · advisory mapped · SSRF (redirect open redirect) and prototype-pollution gadget history
- [[npm/superagent]] — HTTP client · advisory mapped · zip-slip path traversal and prototype-pollution history
- [[npm/request]] — (deprecated) HTTP client · advisory mapped · SSRF / redirect / cookie-domain history; unmaintained
- [[npm/express]] — dominant Node.js web framework · advisory mapped · open-redirect, path-traversal, and request-smuggling history through 4.21.2 / 5.0.1
- [[npm/koa]] — Node.js web framework · advisory mapped · path-traversal and open-redirect history
- [[npm/fastify]] — high-performance Node.js web framework · advisory mapped · request-smuggling and header-injection history through 4.28.1 / 3.29.5
- [[npm/body-parser]] — Express body-parsing middleware · advisory mapped · DoS via large payloads and prototype-pollution history through 1.20.3
- [[npm/multer]] — multipart form-data file upload middleware · advisory mapped · DoS via malformed multipart input history through 1.4.5-lts.2
- [[npm/busboy]] — multipart parser (Fastify/Remix substrate) · advisory mapped · prototype-pollution (pre-1.0.0) and resource-exhaustion (many-field uploads) history
- [[npm/formidable]] — file-upload library · advisory mapped · path-traversal and prototype-pollution history through 3.5.2
- [[npm/passport]] — authentication middleware · advisory mapped · session fixation and type-confusion history through 0.6.0
- [[npm/jsonwebtoken]] — JWT library · advisory mapped · signature-bypass and algorithm-confusion history through 9.0.0
- [[npm/nodemailer]] — email-sending library · advisory mapped · header-injection history through 6.9.9
- [[npm/sequelize]] — ORM · advisory mapped · SQL-injection and prototype-pollution history through 6.35.0
- [[npm/mongoose]] — MongoDB ODM · advisory mapped · prototype-pollution and path-traversal gadget history through 7.6.3
- [[npm/mysql2]] — MySQL client · advisory mapped · SQL-injection, ASN.1 parsing, and cache-poisoning history through 3.11.0
- [[npm/pg]] — PostgreSQL client · advisory mapped · SQL-injection (via tagged-template literals) history through 8.11.3
- [[npm/redis]] — Redis client · advisory mapped · SSRF (RESP3 injection) history through 4.6.12
- [[npm/ioredis]] — Redis client · advisory mapped · SSRF (RESP3 injection) history through 5.3.2
- [[npm/ws]] — WebSocket library · advisory mapped · ReDoS and DoS (large fragmented messages) history through 8.17.1
- [[npm/socket.io]] — real-time WebSocket framework · advisory mapped · credential-fixation, header-injection, and resource-exhaustion history through 4.6.2
- [[npm/tar]] — tar archive library · advisory mapped · long path-traversal / symlink chain (2021–2021) fixed through 6.2.1
- [[npm/node-tar]] — (alias for npm/tar) · see [[npm/tar]]
- [[npm/glob]] — file-globbing library · advisory mapped · ReDoS history through 10.3.10
- [[npm/micromatch]] — glob matching · advisory mapped · ReDoS history through 4.0.8
- [[npm/minimatch]] — glob matching · advisory mapped · ReDoS history through 9.0.4
- [[npm/ansi-regex]] — ANSI escape code matching · advisory mapped · ReDoS history through 6.0.1 / 5.0.1
- [[npm/semver]] — semantic version parsing · advisory mapped · ReDoS history through 7.5.2
- [[npm/tough-cookie]] — cookie parsing · advisory mapped · prototype-pollution history through 4.1.3
- [[npm/qs]] — query-string parsing · advisory mapped · prototype-pollution history through 6.10.3
- [[npm/path-to-regexp]] — URL routing · advisory mapped · ReDoS history through 0.1.12 / 1.9.0
- [[npm/yargs]] — CLI argument parser · advisory mapped · prototype-pollution history through 14.2.3
- [[npm/minimist]] — argument parser · advisory mapped · prototype-pollution history through 1.2.6
- [[npm/flat]] — flat/unflatten utility · advisory mapped · prototype-pollution history through 5.0.2
- [[npm/cross-spawn]] — cross-platform child-process spawning · advisory mapped · ReDoS history through 7.0.5
- [[npm/shell-quote]] — shell argument quoting · advisory mapped · RCE via shell-metacharacter injection history through 1.7.3
- [[npm/vm2]] — sandboxed VM · advisory mapped · repeated sandbox-escape / RCE history; unmaintained
- [[npm/node-uuid]] — UUID generation · advisory mapped · predictable-random-values history; superseded by `uuid`
- [[npm/uuid]] — UUID generation · advisory mapped · predictable-random-values history through 9.0.0
- [[npm/nanoid]] — ID generation · advisory mapped · predictable-random-values history through 3.3.4
- [[npm/csurf]] — CSRF middleware · advisory mapped · CSRF-bypass history through 1.11.0; unmaintained
- [[npm/helmet]] — HTTP security headers · advisory mapped · header-injection and policy-bypass history through 7.1.0
- [[npm/dotenv]] — .env loader · advisory mapped · path-traversal history through 16.4.5
- [[npm/follow-redirects]] — redirect-following HTTP · advisory mapped · open-redirect and credential-leak history through 1.15.6
- [[npm/pac-resolver]] — PAC file resolver · advisory mapped · SSRF and RCE history through 7.0.1
- [[npm/webpack]] — module bundler · advisory mapped · prototype-pollution and source-code disclosure history through 5.88.0
- [[npm/next]] — Next.js framework · advisory mapped · SSRF, open-redirect, and header-injection history through 15.2.3
- [[npm/nuxt]] — Nuxt.js framework · advisory mapped · SSRF and open-redirect history through 3.11.1
- [[npm/gatsby]] — Gatsby framework · advisory mapped · SSRF and path-traversal history
- [[npm/strapi]] — headless CMS · advisory mapped · SQL-injection, SSRF, and auth-bypass history through 4.22.0
- [[npm/parse-server]] — Parse backend · advisory mapped · SQL-injection, SSRF, and RCE history through 6.5.0
- [[npm/keystone]] — headless CMS · advisory mapped · SQL-injection and SSRF history through 6.0.0-beta.7
- [[npm/electron]] — cross-platform desktop app framework · advisory mapped · remote-code-execution and sandbox-escape history through 28.2.2
- [[npm/sharp]] — image processing · advisory mapped · path-traversal and OOB-write history through 0.33.2
- [[npm/pdfkit]] — PDF generation · advisory mapped · SSRF via embedded links history
- [[npm/cheerio]] — HTML parsing · advisory mapped · prototype-pollution and ReDoS history through 1.0.0-rc.12
- [[npm/xml2js]] — XML parsing · advisory mapped · prototype-pollution history through 0.5.0
- [[npm/fast-xml-parser]] — XML parsing · advisory mapped · ReDoS history through 4.3.5
- [[npm/yaml]] — YAML parsing · advisory mapped · prototype-pollution and arbitrary code execution history through 2.3.4

## Rust / crates.io (49)

- [[rust/openssl-src]] — OpenSSL vendored source build crate · advisory mapped · 25 advisories 2020–2023 mapping upstream OpenSSL CVEs to bundled versions (111.x=1.1.1, 300.0.x=3.0.x): Critical SM2 buffer overflow (CVE-2021-3711 CVSS 9.8), High CA cert bypass (CVE-2021-3450), High BN_mod_sqrt DoS (CVE-2022-0778), High X.509 email stack overflow pair (CVE-2022-3602/3786), RSA timing oracle (CVE-2022-4304), 2023 PKCS7/PEM/BIO DoS cluster; latest 400.0.1+4.0.2 unaffected; ~21.6M/week est., ~105.6M total downloads
- [[rust/once_cell]] — single-assignment cells and lazy values · advisory mapped · RUSTSEC-2019-0017 / CVE-2019-16141 / GHSA-7j44-fv4x-79g9 (High CVSS 7.5: `Lazy<T>::deref` executes `unreachable_unchecked` after initialization panic — UB; fixed 1.0.1); current stable 1.21.4 unaffected; ~286.5M/week est., ~1.3B total downloads
- [[rust/tokio]] — dominant async runtime · advisory mapped · memory-safety / unsoundness and Windows named-pipe history
- [[rust/hyper]] — foundational HTTP implementation · advisory mapped · parser, smuggling, and hostname-verification history
- [[rust/reqwest]] — dominant HTTP client · advisory mapped · no direct RustSec/GHSA advisories on record
- [[rust/axum]] — web framework (tokio-rs) · advisory mapped · RUSTSEC-2022-0055 body-limit DoS
- [[rust/actix-web]] — high-performance web framework · advisory mapped · 2018 memory-safety cluster plus HTTP smuggling and 2026 DoS
- [[rust/rocket]] — type-safety web framework · advisory mapped · UB and UAF on 0.4.x line
- [[rust/tonic]] — gRPC framework · advisory mapped · RUSTSEC-2024-0376 DoS on 0.12.2
- [[rust/tower-http]] — HTTP middleware (axum foundation) · advisory mapped · Windows path traversal in ServeDir
- [[rust/rustls]] — pure-Rust TLS · advisory mapped · close_notify DoS and fragmented-ClientHello panic
- [[rust/rustls-webpki]] — X.509 verification · advisory mapped · 5 advisories 2023–2026 CPU DoS, revocation bypass, name-constraint bypass
- [[rust/openssl]] — OpenSSL Rust bindings · advisory mapped · 10 RUSTSEC advisories binding-layer flaws
- [[rust/ring]] — cryptographic library · advisory mapped · AES/QUIC panic DoS; 0.16.x unmaintained
- [[rust/quinn]] — QUIC implementation · advisory mapped · 5 DoS advisories through 2026
- [[rust/h2]] — HTTP/2 implementation · advisory mapped · resource-exhaustion / DoS history
- [[rust/mio]] — non-blocking I/O (Tokio substrate) · advisory mapped · SocketAddr cast UB, Windows named-pipe UAF
- [[rust/bytes]] — zero-copy byte buffers · advisory mapped · RUSTSEC-2026-0007 BytesMut::reserve overflow
- [[rust/tokio]] — (see above)
- [[rust/serde]] — serialization framework · baseline stub
- [[rust/serde_json]] — JSON library · baseline stub
- [[rust/serde_yaml_ng]] — YAML library · audit ingested
- [[rust/rand]] — random number generation · advisory mapped · RUSTSEC-2026-0097 thread_rng unsoundness
- [[rust/chrono]] — date-and-time · advisory mapped · localtime_r segfault
- [[rust/time]] — date-and-time · advisory mapped · localtime_r segfault and RFC 2822 stack DoS
- [[rust/regex]] — regex engine · advisory mapped · ReDoS fixed in 1.5.5
- [[rust/smallvec]] — small vector optimization · advisory mapped · 5 advisories 2018–2021 memory corruption
- [[rust/crossbeam]] — concurrent data structures · advisory mapped · 9 advisories double-free, data-race
- [[rust/parking_lot]] — synchronization primitives · advisory mapped · 5 data-race CVEs in lock_api
- [[rust/dashmap]] — concurrent HashMap · advisory mapped · RUSTSEC-2022-0002 UAF via Ref lifetime
- [[rust/image]] — image encoding/decoding · advisory mapped · HDR decoder UAF, pixel UB
- [[rust/prost]] — Protocol Buffers · advisory mapped · RUSTSEC-2020-0002 stack overflow DoS
- [[rust/sqlx]] — async SQL toolkit · advisory mapped · RUSTSEC-2024-0363 binary protocol injection
- [[rust/diesel]] — ORM and query builder · advisory mapped · 6 advisories 2021–2026 SQLite UAF, PostgreSQL smuggling
- [[rust/rsa]] — RSA implementation · advisory mapped · Marvin Attack timing side-channel (unpatched)
- [[rust/ed25519-dalek]] — Ed25519 signatures · advisory mapped · double-public-key oracle (pre-2.0)
- [[rust/curve25519-dalek]] — Curve25519 group operations · advisory mapped · LLVM timing side-channel
- [[rust/nix]] — POSIX/Unix bindings · advisory mapped · getgrouplist heap overflow
- [[rust/zerocopy]] — zero-copy memory · advisory mapped · RUSTSEC-2023-0074 Ref unsoundness
- [[rust/tar]] — tar archive · advisory mapped · 4 advisories symlink/path-traversal
- [[rust/zip]] — ZIP archive · advisory mapped · RUSTSEC-2025-0168 symlink path traversal
- [[rust/wasmtime]] — WebAssembly runtime · advisory mapped · 16 advisories Cranelift miscompilation, UAF
- [[rust/tracing]] — structured logging · advisory mapped · RUSTSEC-2023-0078 UAF in Instrumented
- [[rust/base64]] — base64 encoding · advisory mapped · RUSTSEC-2017-0004 heap overflow
- [[rust/lettre]] — email sending · advisory mapped · 3 advisories SMTP injection, TLS bypass
- [[rust/ammonia]] — HTML sanitization · advisory mapped · 6 advisories XSS, mXSS via SVG/MathML
- [[rust/borsh]] — binary serialization (NEAR/Solana) · advisory mapped · ZST deserialization UB
- [[rust/atty]] — TTY detection (unmaintained) · advisory mapped · Windows HANDLE unaligned read
- [[rust/connectrpc]] — Connect RPC (Tower) · advisory mapped · RUSTSEC-2026-0304 streaming DoS
- [[rust/futures]] — async primitives · advisory mapped · 4 advisories UAF, null-ptr, unsound Sync

## .NET / NuGet (18)

- [[dotnet/newtonsoft-json]] — dominant JSON library · advisory mapped · prototype-pollution / type-confusion gadget history through 13.0.2
- [[dotnet/system-text-json]] — .NET built-in JSON · advisory mapped · JsonDocument dispose-UAF, deserializer RCE gadget chain history
- [[dotnet/aspnetcore]] — ASP.NET Core · advisory mapped · request-smuggling, path-traversal, auth-bypass, and open-redirect history
- [[dotnet/signalr]] — real-time communications · advisory mapped · CSRF and XSS history
- [[dotnet/dapper]] — micro-ORM · advisory mapped · SQL injection history through 2.0.151
- [[dotnet/npgsql]] — PostgreSQL client · advisory mapped · SQL-injection, SSRF, and buffer-overflow history
- [[dotnet/mysql-connector-net]] — MySQL client · advisory mapped · auth-bypass, information-disclosure history
- [[dotnet/serilog]] — structured logging · advisory mapped · format-string and deserialization history
- [[dotnet/log4net]] — logging framework · advisory mapped · XML external entity (XXE) and SSRF history
- [[dotnet/polly]] — resilience library · advisory mapped · DoS via policy-exhaustion history
- [[dotnet/moq]] — mocking library · advisory mapped · supply-chain-concern (SponsorLink) and dependency history
- [[dotnet/autofac]] — IoC container · advisory mapped · container-escape history
- [[dotnet/mediatr]] — CQRS mediator · advisory mapped · no direct package-level advisories confirmed
- [[dotnet/fluentvalidation]] — validation library · advisory mapped · no direct package-level advisories confirmed
- [[dotnet/refit]] — REST client · advisory mapped · no direct package-level advisories confirmed
- [[dotnet/identity-model]] — IdentityModel (JWT / OIDC) · advisory mapped · algorithm-confusion and token-replay history
- [[dotnet/microsoft-identity-web]] — Microsoft Identity Web · advisory mapped · auth-bypass history
- [[dotnet/azure-identity]] — Azure Identity · advisory mapped · credential-leakage history

## Python / PyPI (22)

- [[python/requests]] — dominant HTTP client · advisory mapped · header-injection, redirect open-redirect, and credential-leakage history through 2.32.0
- [[python/pillow]] — image library · advisory mapped · buffer overflow, path-traversal, and DoS history through 10.3.0
- [[python/django]] — web framework · advisory mapped · SQL-injection, XSS, CSRF, and open-redirect history through 5.0.3
- [[python/flask]] — micro web framework · advisory mapped · open-redirect and session-fixation history
- [[python/fastapi]] — async API framework · advisory mapped · no direct package-level advisories on record; SSRF risk via request forwarding
- [[python/pydantic]] — data validation · advisory mapped · DoS via deeply nested input history through 2.6.3
- [[python/sqlalchemy]] — SQL toolkit and ORM · advisory mapped · SQL-injection and ReDoS history through 2.0.25
- [[python/celery]] — distributed task queue · advisory mapped · command-injection and auth-bypass history
- [[python/redis-py]] — Redis client · advisory mapped · SSRF history
- [[python/boto3]] — AWS SDK · advisory mapped · credential-leakage and SSRF history
- [[python/paramiko]] — SSH client/server · advisory mapped · host-key bypass and auth-bypass history through 3.4.0
- [[python/cryptography]] — cryptography library · advisory mapped · memory-safety (Rust/C bindings) and padding-oracle history
- [[python/pyjwt]] — JWT library · advisory mapped · algorithm-confusion and key-confusion history through 2.8.0
- [[python/oauthlib]] — OAuth library · advisory mapped · DoS and open-redirect history
- [[python/aiohttp]] — async HTTP client/server · advisory mapped · SSRF, request-smuggling, and path-traversal history through 3.9.4
- [[python/tornado]] — async web framework · advisory mapped · open-redirect and header-injection history
- [[python/httpx]] — async HTTP client · advisory mapped · SSRF (redirect open redirect) history
- [[python/werkzeug]] — WSGI utility library · advisory mapped · path-traversal and DoS history through 3.0.3
- [[python/lxml]] — XML/HTML library · advisory mapped · XXE, XSS, and buffer-overflow history
- [[python/jinja2]] — templating engine · advisory mapped · SSTI and sandbox-escape history through 3.1.3
- [[python/numpy]] — numerical computing · advisory mapped · buffer-overflow and integer-overflow history through 1.26.4
- [[python/scipy]] — scientific computing · advisory mapped · no direct package-level advisories on record

## Go (14)

- [[go/golang-x-net]] — extended Go network library · advisory mapped · HTTP/2 DoS history through 0.23.0
- [[go/gin]] — web framework · advisory mapped · path-traversal and open-redirect history
- [[go/gorilla-mux]] — HTTP router · advisory mapped · no direct package-level advisories on record; ReDoS risk via regex routes
- [[go/go-jose]] — JOSE library · advisory mapped · algorithm-confusion, key-confusion, and denial-of-service history
- [[go/golang-jwt]] — JWT library · advisory mapped · algorithm-confusion history
- [[go/grpc-go]] — gRPC for Go · advisory mapped · header-injection and DoS history through 1.56.3
- [[go/go-yaml]] — YAML library · advisory mapped · prototype-pollution and DoS history through 3.0.0-20210107192922
- [[go/sprig]] — template functions · advisory mapped · SSRF via URL-building functions history
- [[go/etcd]] — distributed KV store · advisory mapped · auth-bypass and DoS history through 3.5.9
- [[go/hashicorp-vault]] — secrets management · advisory mapped · auth-bypass, SSRF, and privilege-escalation history through 1.14.1
- [[go/helm]] — Kubernetes package manager · advisory mapped · path-traversal, SSRF, and injection history through 3.14.3
- [[go/kubernetes]] — container orchestration · advisory mapped · auth-bypass, SSRF, and privilege-escalation history through 1.28.5
- [[go/terraform]] — infrastructure as code · advisory mapped · no direct package-level advisories on record
- [[go/opa]] — Open Policy Agent · advisory mapped · ReDoS history

## Homebrew (4)

- [[homebrew/ffmpeg]] — multimedia processing · advisory mapped · buffer-overflow and use-after-free history through 6.1.1_7
- [[homebrew/imagemagick]] — image processing · advisory mapped · buffer-overflow, heap-overflow, and DoS history through 7.1.1-29
- [[homebrew/curl]] — data transfer tool · advisory mapped · cookie and credential leakage, SSRF, and DoS history through 8.7.1
- [[homebrew/openssl]] — TLS/crypto toolkit · advisory mapped · Heartbleed, padding oracle, and recent buffer-overflow history through 3.3.0

## Maven / Java (37)

- [[maven/org.springframework/spring-core]] — Spring Framework core · advisory mapped · DoS, RCE (Spring4Shell), and open-redirect history through 6.1.5
- [[maven/org.springframework.boot/spring-boot]] — Spring Boot · advisory mapped · actuator info-disclosure history
- [[maven/org.springframework.security/spring-security-core]] — Spring Security · advisory mapped · auth-bypass, CSRF, and path-traversal history through 6.2.3
- [[maven/com.fasterxml.jackson.core/jackson-databind]] — Jackson JSON · advisory mapped · polymorphic deserialization RCE gadget chain history through 2.16.1
- [[maven/org.apache.logging.log4j/log4j-core]] — Log4j 2 · advisory mapped · Log4Shell (CVE-2021-44228 CVSS 10.0) and follow-on deserialization history through 2.20.0
- [[maven/org.apache.commons/commons-text]] — Apache Commons Text · advisory mapped · Text4Shell (CVE-2022-42889 CVSS 9.8) string interpolation RCE history
- [[maven/org.apache.commons/commons-lang3]] — Apache Commons Lang 3 · advisory mapped · no direct package-level advisories confirmed
- [[maven/org.apache.struts/struts2-core]] — Apache Struts 2 · advisory mapped · OGNL injection RCE history through 6.3.0.2
- [[maven/org.apache.tomcat/tomcat]] — Apache Tomcat · advisory mapped · request-smuggling, path-traversal, and partial-put RCE history through 10.1.19
- [[maven/io.netty/netty-all]] — Netty framework · advisory mapped · HTTP/2 DoS, request-smuggling, and SSL-stripping history through 4.1.107
- [[maven/io.vertx/vertx-core]] — Vert.x core · advisory mapped · CRLF injection and DoS history
- [[maven/org.hibernate/hibernate-core]] — Hibernate ORM · advisory mapped · 3 confirmed GHSA advisories (2019–2026) for SQL injection via JPA Criteria API literal interpolation (CVE-2019-14900 Moderate, CVE-2020-25638 High, CVE-2026-0603 High); all target 5.x branch; no confirmed GHSA advisories for current 6.x/7.x
- [[maven/io.undertow/undertow-core]] — Undertow HTTP server · advisory mapped · 10 advisories 2014–2024 including Windows path traversal (CVE-2014-7816), WebSocket DoS (CVE-2017-2670), multiple HTTP request smuggling (CVE-2017-12165, CVE-2020-10719), and SSL handshake infinite loop (CVE-2023-1108)
- [[maven/com.squareup.okhttp3/okhttp]] — OkHttp · advisory mapped · SSRF (header injection) and certificate-pinning-bypass history through 4.12.0
- [[maven/ch.qos.logback/logback-classic]] — Logback logging · advisory mapped · JNDI injection and XML deserialization history through 1.5.6
- [[maven/com.google.guava/guava]] — Google Guava · advisory mapped · path-traversal and SSRF history through 32.0.1
- [[maven/org.bouncycastle/bcprov-jdk15on]] — Bouncy Castle · advisory mapped · timing-oracle and key-recovery history through 1.77
- [[maven/io.jsonwebtoken/jjwt]] — Java JWT · advisory mapped · algorithm-confusion history through 0.12.5
- [[maven/org.xwiki.platform/xwiki-platform-oldcore]] — XWiki · advisory mapped · SSTI / code-execution and CSRF history
- [[maven/org.keycloak/keycloak-core]] — Keycloak · advisory mapped · token-fixation, SSRF, and open-redirect history through 24.0.3
- [[maven/org.elasticsearch/elasticsearch]] — Elasticsearch · advisory mapped · script-injection and information-disclosure history through 7.17.18 / 8.13.0
- [[maven/org.apache.kafka/kafka]] — Apache Kafka · advisory mapped · SASL auth-bypass and DoS history
- [[maven/org.apache.zookeeper/zookeeper]] — Apache ZooKeeper · advisory mapped · auth-bypass and information-disclosure history through 3.9.2
- [[maven/org.apache.hadoop/hadoop-common]] — Apache Hadoop · advisory mapped · path-traversal and SSRF history
- [[maven/org.apache.spark/spark-core]] — Apache Spark · advisory mapped · RCE via serialization, SSRF, and ACL-bypass history through 3.5.0
- [[maven/org.apache.shiro/shiro-core]] — Apache Shiro · advisory mapped · authentication-bypass and path-traversal history through 1.13.0
- [[maven/org.apache.camel/camel-core]] — Apache Camel · advisory mapped · SSRF and header-injection history
- [[maven/org.quartz-scheduler/quartz]] — Quartz Scheduler · advisory mapped · SQL-injection and XXE history through 2.3.2
- [[maven/org.yaml/snakeyaml]] — SnakeYAML · advisory mapped · deserialization-RCE and DoS history through 2.2
- [[maven/com.thoughtworks.xstream/xstream]] — XStream · advisory mapped · serialization-RCE history through 1.4.20
- [[maven/org.dom4j/dom4j]] — dom4j · advisory mapped · XXE history through 2.1.4
- [[maven/xerces/xercesImpl]] — Xerces · advisory mapped · XXE and DoS history
- [[maven/commons-fileupload/commons-fileupload]] — Apache Commons FileUpload · advisory mapped · DoS history through 1.5
- [[maven/org.glassfish.jersey.core/jersey-common]] — Jersey · advisory mapped · XSS and SSRF history
- [[maven/io.grpc/grpc-core]] — gRPC Java · advisory mapped · HTTP/2 DoS history through 1.64.0
- [[maven/com.google.protobuf/protobuf-java]] — Protocol Buffers Java · advisory mapped · DoS and hash-flooding history through 3.25.3
- [[maven/org.jboss.resteasy/resteasy-core]] — RESTEasy · advisory mapped · XXE and DoS history

## Kubernetes / CNCF (10)

- [[k8s/kubernetes]] — Kubernetes core · advisory mapped · auth-bypass, SSRF, and privilege-escalation history through 1.28.5
- [[k8s/etcd]] — distributed KV store · advisory mapped · auth-bypass and DoS history through 3.5.9
- [[k8s/helm]] — package manager · advisory mapped · path-traversal, SSRF, and injection history through 3.14.3
- [[k8s/ingress-nginx]] — NGINX ingress controller · advisory mapped · header-injection and RCE history through 1.9.6
- [[k8s/cert-manager]] — certificate management · advisory mapped · no direct package-level advisories confirmed
- [[k8s/argo-cd]] — GitOps continuous delivery · advisory mapped · path-traversal, SSRF, and auth-bypass history through 2.9.3
- [[k8s/flux]] — GitOps toolkit · advisory mapped · path-traversal and SSRF history
- [[k8s/open-policy-agent]] — policy engine · advisory mapped · ReDoS history
- [[k8s/falco]] — runtime security · advisory mapped · no direct package-level advisories confirmed
- [[k8s/trivy]] — vulnerability scanner · advisory mapped · path-traversal and DoS history through 0.49.1

## Linux (6)

- [[linux/openssl]] — OpenSSL · advisory mapped · Heartbleed, padding oracle, and recent buffer-overflow history through 3.3.0
- [[linux/curl]] — data transfer tool · advisory mapped · cookie and credential leakage, SSRF, and DoS history through 8.7.1
- [[linux/glibc]] — GNU C Library · advisory mapped · buffer-overflow and privilege-escalation history through 2.39
- [[linux/sudo]] — privilege escalation tool · advisory mapped · buffer-overflow and auth-bypass history through 1.9.15p5
- [[linux/bash]] — GNU Bash · advisory mapped · Shellshock and code-injection history
- [[linux/kernel]] — Linux kernel · advisory mapped · privilege-escalation, UAF, and OOB-write history through 6.8.0
