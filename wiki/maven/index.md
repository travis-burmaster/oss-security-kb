# Maven / Java (Maven Central)

This section tracks **package-level, publicly disclosed vulnerabilities** for Java ecosystem artifacts published to Maven repositories.

Scope notes:
- Entries are evidence-backed and sourced from **public advisories** (OSV.dev, GitHub Advisory Database, CVE/NVD, maintainer advisories, changelogs).
- Some upstream projects publish **drop-in replacement JARs** outside Maven Central for emergency remediation. When this happens, we note it explicitly.

## Packages

- [[maven/org.apache.commons/commons-compress]] — Apache Commons archive compression/extraction library · advisory mapped · malformed archive DoS / resource-exhaustion history fixed through 1.26.0
- [[maven/org.apache.logging.log4j/log4j-core]] — Apache Log4j Core logging implementation · advisory mapped · Log4Shell / JNDI, socket deserialization, TLS hostname verification, structured-layout log injection, and log-event-loss history fixed through 2.25.4 on the 2.x line
- [[maven/org.geotools/gt-complex]] — GeoTools complex feature / XPath handling · advisory mapped · XPath-expression RCE risk when evaluating untrusted expressions (CVE-2024-36404)

---
*Last updated: 2026-05-06*
