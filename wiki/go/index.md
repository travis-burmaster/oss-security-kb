# Go Index

## Seed Pages
- [[go/github.com/gin-contrib/cors]] — standalone Gin CORS middleware · advisory mapped · wildcard-origin trust-boundary flaw fixed in 1.6.0
- [[go/github.com/gin-gonic/gin]] — high-usage Go web framework · advisory mapped · proxy-header, logging, and attachment-sanitization history
- [[go/github.com/gorilla/mux]] — established Go router · baseline stub · no package-scoped OSV / GitHub advisory confirmed in this pass, disclosure path unclear
- [[go/github.com/gorilla/websocket]] — foundational Go WebSocket implementation · advisory mapped · integer-overflow / read-limit bypass DoS fixed in 1.4.1
- [[go/github.com/gorilla/schema]] — Gorilla form decoder/encoder · advisory mapped · sparse slice index memory-exhaustion DoS fixed in 1.4.1
- [[go/github.com/labstack/echo-v4]] — high-usage Go web framework line · advisory mapped · static-handler traversal and open-redirect history plus current support-policy context
- [[go/github.com/go-chi/chi]] — widely used Go router · advisory mapped · `RedirectSlashes` open-redirect and incomplete-fix chain through 5.2.4
- [[go/golang.org-x-crypto]] — foundational Go crypto module · advisory mapped · repeated SSH boundary flaws plus cryptobyte, autocert, and openpgp security history
- [[go/google.golang.org/grpc]] — core Go gRPC transport stack · advisory mapped · transport, metadata, and authz-sensitive surface

## Future Targets
- `go.opentelemetry.io/otel` — broad instrumentation surface with high downstream blast radius
