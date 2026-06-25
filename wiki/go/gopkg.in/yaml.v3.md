# gopkg.in/yaml.v3 (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-06-25); 34,113 known importers on pkg.go.dev
**Repository:** https://github.com/go-yaml/yaml
**Security Contact:** security@golang.org (Go vulnerability database)
**Disclosure Policy:** https://go.dev/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-25 | OSS Security KB | GHSA database lookup | automated | 1 public advisory row mapped (CVE-2022-28948 / GHSA-hp87-p4gw-j4gq) | [github/advisory-database](https://github.com/advisories/GHSA-hp87-p4gw-j4gq) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-28948 / GHSA-hp87-p4gw-j4gq | High (CVSS 7.5) | gopkg.in/yaml.v3: `Unmarshal` panics on malformed or invalid YAML input — a crafted YAML document triggers an internal panic (nil dereference or bounds violation), causing denial of service in any application deserializing user-controlled YAML. Two separate fixes shipped in v3.0.1 (commits 8f96da9 and f6f7691, merged 2022-05-18/19; tagged 2022-05-27). CWE-502 (Deserialization of Untrusted Data). Go vuln DB alias: GO-2022-0272. | v3.0.1 | [GHSA-hp87-p4gw-j4gq](https://github.com/advisories/GHSA-hp87-p4gw-j4gq) |

*OSV live record: https://osv.dev/list?ecosystem=Go&q=gopkg.in%2Fyaml.v3*

## Security Posture Notes

`gopkg.in/yaml.v3` is the current major version of the canonical Go YAML library, a pure-Go port of libyaml originally developed at Canonical for the Juju project. It supports YAML 1.2 with YAML 1.1 backwards compatibility. With 34,113 known importers on pkg.go.dev it is one of the most widely depended-upon modules in the Go ecosystem — used in Kubernetes configuration pipelines, CLI frameworks (`cobra`, `viper`), infrastructure automation tooling, and configuration management systems throughout the Go world.

**CVE-2022-28948 (May 2022):** The single published advisory for v3 targets panic behavior in `Unmarshal` on malformed input. Two patches landed in v3.0.1 (released May 27, 2022, eight days after the NVD publish date). The current and only formally-tagged stable release of yaml.v3 is v3.0.1; there is no v3.0.2 or v4 milestone. Applications pinned to v3.0.0 or pre-module pseudoversions should upgrade to v3.0.1.

**yaml.v2 advisory history (related):** The older `gopkg.in/yaml.v2` module (60,161 known importers; current release v2.4.0 from November 2020) carries a separate chain of three denial-of-service advisories via malicious YAML input:
- CVE-2019-11254 / GHSA-wxc4-f4m6-wwqv (Moderate CVSS 6.5): excessive CPU loop on malformed YAML; originally surfaced via the Kubernetes API server; fixed in yaml.v2 2.2.8.
- CVE-2021-4235 / GHSA-r88r-gmrh-7j83 (Moderate CVSS 5.5): unbounded alias chaining consumes significant resources; fixed in yaml.v2 2.2.3.
- CVE-2022-3064 / GHSA-6q6q-88xp-6f2r (High CVSS 7.5): parsing large or malicious YAML documents consumes excessive CPU or memory; fixed in yaml.v2 2.2.4.

The fully patched minimum for yaml.v2 is v2.2.8; the current v2.4.0 release is safe. Applications still on yaml.v2 should verify they are on 2.2.8+.

**Disclosure path:** Issues are typically reported to security@golang.org; the Go security team coordinates fixes and publishes entries to the Go vulnerability database (pkg.go.dev/vuln/GO-2022-0272 for CVE-2022-28948).

## Dependencies of Note

None flagged at the module level. `gopkg.in/yaml.v3` has no external Go-module dependencies; its security surface is the correctness of the libyaml-derived recursive-descent parser and decoder for complex YAML documents.

## Open Questions

- Verify whether GO-2022-0272 in the Go vuln database has any scope differences from GHSA-hp87-p4gw-j4gq.
- Confirm current weekly download stats (pkg.go.dev does not expose download counts; proxy.golang.org telemetry is unpublished).
- Determine whether `gopkg.in/yaml.v2` warrants a dedicated KB page given its 60K-importer footprint and three-advisory chain.
- Monitor for v3.0.2 or v4 releases that might introduce new advisory surface.

## Related Pages

- [[go/golang.org-x-net]]
- [[go/go.etcd.io/etcd-v3]]
- [[go/index]]

---
*Last updated: 2026-06-25 | Sources: 2 (github/advisory-database, pkg.go.dev)*
