# Python / PyPI Index

## Seed Pages
- [[python/litellm]] — LLM gateway/proxy package · advisory mapped · proxy vulnerabilities plus March 2026 malicious PyPI release incident
- [[python/telnyx]] — Telnyx SDK · advisory mapped · March 2026 malicious PyPI release incident (PYSEC-2026-3 / GHSA-955r-262c-33jc / MAL-2026-2254)
- [[python/flask]] — dominant Python web framework · advisory mapped · JSON-input DoS plus session / cache / signing-boundary history
- [[python/flask-cors]] — Flask CORS extension · advisory mapped · directory traversal plus 2024 CORS matching / private-network-header / debug-log injection fix train through 6.0.0
- [[python/jinja2]] — dominant Python templating engine · advisory mapped · recurring sandbox-escape, xmlattr injection, and ReDoS history
- [[python/pyyaml]] — dominant Python YAML parser · advisory mapped · long-running unsafe-deserialization / arbitrary-code-execution fix train through 5.4
- [[python/django]] — dominant Python web framework · advisory mapped · mature public security-release archive with recurring SQL-injection, ASGI/header-boundary, upload-limit, cache/session, traversal, and DoS history through 2026
- [[python/pillow]] — Python Imaging Library fork · advisory mapped · dense parser-boundary history across image decoder memory corruption, decompression / allocation DoS, ImageMath code execution, and 2026 PSD / FITS / PDF fixes through 12.2.0
- [[python/pip]] — Python package installer · advisory mapped · archive-extraction, VCS reference, installer import-order, and legacy transport / temp-dir security history through 26.1
- [[python/setuptools]] — Python packaging/build backend toolkit · advisory mapped · package-index transport, parsing, command-execution, and download path-traversal history through 78.1.1
- [[python/requests]] — dominant Python HTTP client · advisory mapped · credential, redirect, proxy, and TLS-boundary history
- [[python/httpx]] — async/sync Python HTTP client · advisory mapped · compact URL input-validation history with duplicate-advisory fixed-version discrepancy
- [[python/urllib3]] — foundational Python HTTP transport library · advisory mapped · redirect, TLS, parser, and decompression-security history
- [[python/cryptography]] — foundational Python cryptography library · advisory mapped · primitive, X.509/PKCS, buffer-boundary, and bundled-OpenSSL wheel history
- [[python/paramiko]] — Python SSH2 protocol library · advisory mapped · server-mode auth bypasses, private-key file race, SSH Terrapin, legacy randomness, and 2026 SHA-1 algorithm record
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
- [[python/twisted]] — event-driven networking framework · advisory mapped · HTTP parser/request-smuggling, TLS validation, redirect/header exposure, pipelining, SSH/DNS/HTTP2 DoS history through CVE-2026-42304
- [[python/tornado]] — Python web framework and async networking library · advisory mapped · HTTP request-smuggling, cookie / multipart DoS, CRLF / cookie-attribute injection, open redirect, and legacy XSRF side-channel history through 6.5.5
