# Maven / Java (Maven Central)

This section tracks **package-level, publicly disclosed vulnerabilities** for Java ecosystem artifacts published to Maven repositories.

Scope notes:
- Entries are evidence-backed and sourced from **public advisories** (OSV.dev, GitHub Advisory Database, CVE/NVD, maintainer advisories, changelogs).
- Some upstream projects publish **drop-in replacement JARs** outside Maven Central for emergency remediation. When this happens, we note it explicitly.

## Packages

- [[maven/commons-fileupload/commons-fileupload]] — Apache Commons FileUpload multipart parser · advisory mapped · 1.x arbitrary-file-write, deserialization/RCE, temporary-file, and multipart DoS history fixed through 1.6.0
- [[maven/commons-io/commons-io]] — Apache Commons IO utility library · advisory mapped · path-normalization traversal and `XmlStreamReader` resource-consumption history fixed through 2.14.0
- [[maven/com.fasterxml.jackson.core/jackson-databind]] — Jackson data-binding library · advisory mapped · dense polymorphic-deserialization gadget CVE history plus XXE and resource-exhaustion records through 2022
- [[maven/org.apache.commons/commons-compress]] — Apache Commons archive compression/extraction library · advisory mapped · malformed archive DoS / resource-exhaustion history fixed through 1.26.0
- [[maven/org.apache.logging.log4j/log4j-core]] — Apache Log4j Core logging implementation · advisory mapped · Log4Shell / JNDI, socket deserialization, TLS hostname verification, structured-layout log injection, and log-event-loss history fixed through 2.25.4 on the 2.x line
- [[maven/org.yaml/snakeyaml]] — SnakeYAML YAML parser · advisory mapped · unsafe Java object construction / deserialization RCE, alias expansion, nested collection resource exhaustion, and parser stack-overflow DoS history through 2.0+
- [[maven/org.apache.tomcat.embed/tomcat-embed-core]] — Apache Tomcat embedded servlet-container core · advisory mapped · HTTP parsing, HTTP/2 and multipart DoS, security-constraint / CLIENT_CERT auth bypass, open redirect, and logging / information-disclosure history through 2026
- [[maven/org.bouncycastle/bcprov-jdk18on]] — Bouncy Castle Java cryptography provider · advisory mapped · timing side channels, certificate / ASN.1 DoS, LDAP injection, and DNS-poisoning-relevant certificate-validation history fixed through 1.84
- [[maven/org.springframework/spring-core]] — Spring Framework core package · advisory mapped · path/resource handling, authorization-boundary, logging, JSONP, deserialization, and web DoS history through CVE-2025-41249
- [[maven/org.springframework/spring-webmvc]] — Spring MVC web framework artifact · advisory mapped · data-binding RCE, static-resource/path traversal, XXE, CSRF/request-matching, RFD/XSS, cache-poisoning, SSE integrity, and DoS history through 2026
- [[maven/org.geotools/gt-complex]] — GeoTools complex feature / XPath handling · advisory mapped · XPath-expression RCE risk when evaluating untrusted expressions (CVE-2024-36404)

---
*Last updated: 2026-05-11*
