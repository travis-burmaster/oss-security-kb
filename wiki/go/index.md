# Go Index

## Seed Pages
- [[go/github.com/gin-contrib/cors]] — standalone Gin CORS middleware · advisory mapped · wildcard-origin trust-boundary flaw fixed in 1.6.0
- [[go/github.com/gin-gonic/gin]] — high-usage Go web framework · advisory mapped · proxy-header, logging, and attachment-sanitization history
- [[go/github.com/golang-jwt/jwt]] — Go JWT implementation · advisory mapped · v4 ParseWithClaims error-handling boundary plus ParseUnverified memory-allocation DoS history through 4.5.2 / 5.2.2
- [[go/github.com/gorilla/mux]] — established Go router · baseline stub · no package-scoped OSV / GitHub advisory confirmed in this pass, disclosure path unclear
- [[go/github.com/gorilla/websocket]] — foundational Go WebSocket implementation · advisory mapped · integer-overflow / read-limit bypass DoS fixed in 1.4.1
- [[go/github.com/gorilla/schema]] — Gorilla form decoder/encoder · advisory mapped · sparse slice index memory-exhaustion DoS fixed in 1.4.1
- [[go/github.com/labstack/echo-v4]] — high-usage Go web framework line · advisory mapped · static-handler traversal and open-redirect history plus current support-policy context
- [[go/github.com/go-chi/chi]] — widely used Go router · advisory mapped · `RedirectSlashes` open-redirect and incomplete-fix chain through 5.2.4
- [[go/github.com/prometheus/client_golang]] — Prometheus Go instrumentation library · advisory mapped · promhttp method-label cardinality DoS fixed in 1.11.1
- [[go/go.opentelemetry.io/otel]] — core OpenTelemetry-Go API / propagation module · advisory mapped · multi-value W3C baggage header allocation-amplification DoS fixed in 1.41.0
- [[go/golang.org-x-crypto]] — foundational Go crypto module · advisory mapped · repeated SSH boundary flaws plus cryptobyte, autocert, and openpgp security history
- [[go/golang.org-x-net]] — foundational Go networking module · advisory mapped · HTTP/2 DoS / request-smuggling, HTML rendering / parser, and proxy-boundary history through 2025
- [[go/google.golang.org/grpc]] — core Go gRPC transport stack · advisory mapped · transport, metadata, and authz-sensitive surface
- [[go/google.golang.org/protobuf]] — foundational Go protobuf implementation · advisory mapped · prototext panic and protojson infinite-loop DoS history
- [[go/go.etcd.io/etcd-v3]] — distributed key-value store (Kubernetes backing store) · advisory mapped · 18 advisories spanning CSRF, RBAC bypass, WAL DoS, gateway TLS/auth, credential logging, debug-endpoint RCE, and 2026 gRPC auth-bypass cluster
- [[go/golang.org-x-text]] — foundational Go text / i18n / Unicode module · advisory mapped · UTF-16 decoder infinite loop, BCP 47 language tag OOB read panic, and ParseAcceptLanguage quadratic-time DoS fixed through 0.3.8
- [[go/gopkg.in/yaml.v3]] — canonical Go YAML library (v3) · advisory mapped · CVE-2022-28948 / GHSA-hp87-p4gw-j4gq Unmarshal panic DoS on malformed input fixed in v3.0.1; 34,113 importers; note yaml.v2 (60K+ importers) carries a separate three-advisory DoS chain (CVE-2019-11254, CVE-2021-4235, CVE-2022-3064)
