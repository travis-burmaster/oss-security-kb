# YamlDotNet (NuGet)

**Registry:** NuGet
**Weekly Downloads:** unknown (NuGet registration API does not surface per-package download counts in the standard response; YamlDotNet is the dominant .NET YAML library)
**Repository:** https://github.com/aaubry/YamlDotNet
**Security Contact:** GitHub security advisories (https://github.com/aaubry/YamlDotNet/security)
**Disclosure Policy:** GitHub security advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-rpch-cqj9-h65r / CVE-2018-1000210 | High (CVSS:3.0 9.0) | Insecure deserialization / arbitrary type instantiation: `Deserializer.Deserialize()` uses `Type.GetType(nodeEvent.Tag.Substring(1), throwOnError: false)` to resolve YAML type tags without any allowlist or type restriction, allowing a crafted YAML document to instantiate arbitrary .NET types available in the AppDomain. This enables code execution in the context of the deserializing process when YAML input is attacker-controlled. Fixed by restricting type resolution in 5.0.0 via a safe `ObjectFactory` model. Affects all versions through 4.3.2 | YamlDotNet ≥ 5.0.0 | [GHSA-rpch-cqj9-h65r](https://github.com/advisories/GHSA-rpch-cqj9-h65r) |

## Security Posture Notes

YamlDotNet is the dominant YAML parsing and serialization library for .NET, used across ASP.NET Core configuration, CI/CD tooling, Kubernetes client libraries, and game engines (Unity). The advisory above (CVE-2018-1000210) reflects a class of vulnerability well-known in the YAML ecosystem: unsafe deserialization of attacker-controlled YAML type tags.

**Insecure deserialization pattern:** The vulnerability mirrors `SnakeYAML`'s unsafe-deserialization history (see [[maven/org.yaml/snakeyaml]]) and `PyYAML`'s `yaml.load()` issues (see [[python/pyyaml]]). All three libraries historically resolved type information embedded in YAML `!!type` tags against the full runtime type system. The 5.0.0 fix introduced a safe `Deserializer` builder pattern that requires explicit type registration or uses a static type; callers who upgraded but retained the old `Deserializer()` constructor with `.WithTagMapping<T>()` for all possible types may have retained the risk.

**Current version:** YamlDotNet 18.1.0 (latest stable as of June 2026) — well past the vulnerable 4.3.2 boundary. The 5.0.0+ API redesign enforces an explicit type model by default.

**Ecosystem usage:** YamlDotNet is a transitive dependency in many .NET Kubernetes SDKs (`KubernetesClient`), Ansible integrations, and YAML-based configuration frameworks. Applications that use YamlDotNet to parse user-supplied or network-sourced YAML into typed objects should pin to 5.0.0+ and avoid `AllowAnyTagNodeTypeResolver` or equivalent open resolvers.

**One advisory on record:** The GitHub advisory database (github/advisory-database) contains exactly one reviewed advisory for this package. No additional public records were identified in this pass. This does not preclude undisclosed issues; YAML parsing complexity makes ReDoS and decompression-bomb DoS class vulnerabilities worth watching in future passes.

## Dependencies of Note

None flagged. YamlDotNet is a pure .NET library with no security-relevant transitive dependencies.

## Open Questions

- Are there any recent (2019–2026) advisories or maintainer security announcements not yet reflected in the GitHub advisory database?
- Does the 5.0.0+ `StaticDeserializer` pattern (or equivalent strict-mode API) fully mitigate the type-tag resolution risk, or are there edge cases with custom `INodeDeserializer` implementations?
- What is the download count on NuGet (blocked in this pass)? A high count would increase priority for a future full-pass recheck.
- YamlDotNet processes YAML anchors and aliases: should an alias-expansion DoS be evaluated similarly to what was filed against `go/gopkg.in/yaml.v3` (CVE-2022-28948)?

## Related Pages

- [[maven/org.yaml/snakeyaml]]
- [[python/pyyaml]]
- [[dotnet/System.Text.Json]]
- [[dotnet/index]]

---
*Last updated: 2026-07-11 | Sources: 1 (GHSA-rpch-cqj9-h65r via github/advisory-database)*
