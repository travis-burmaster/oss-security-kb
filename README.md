# OSS Security Knowledge Base

A public, LLM-maintained knowledge base tracking **security audit coverage** of the most-downloaded open source packages across all major ecosystems.

> Built in the [Karpathy llm-wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): raw sources feed into a persistent, compounding wiki maintained by LLMs.

---

## Why This Exists

Every major vulnerability database (OSV, NVD, Snyk, GitHub Advisory) tracks vulnerabilities *after they're found*. None of them answer:

> **"Has anyone ever done a proactive security audit of this package?"**

A maintainer whose package has 50M weekly downloads has no way to know if anyone has systematically looked for RCE, prototype pollution, path traversal, or supply chain attacks in their code. This knowledge base fills that gap.

## What's Tracked

For each package:
- 📦 **Download stats** — weekly/monthly downloads from registry APIs
- 🔍 **Audit history** — who looked, when, what scope, what methodology
- 🐛 **Findings** — bugs found (with links to issues/CVEs), bugs *not* found (equally important)
- 🔒 **Security posture** — disclosure policy, security contact, last known review
- 🕸️ **Dependency risk** — transitive dependencies, known-vulnerable deps

## Ecosystems Covered

| Ecosystem | Registry | Top-N Tracked |
|-----------|----------|---------------|
| JavaScript/Node | npm | Top 200 |
| Rust | crates.io | Top 100 |
| .NET | NuGet | Top 100 |
| Python | PyPI | Top 100 |
| Go | pkg.go.dev | Top 100 |
| macOS | Homebrew | Top 100 |
| Kubernetes | CNCF/k8s.io | Core components |
| Linux | Distro packages | Core system libs |

## Structure

```
raw/                    ← Immutable source documents (audit reports, CVE writeups, researcher posts)
wiki/
  index.md              ← Master searchable index (LLM-maintained)
  log.md                ← Append-only ingest/audit log
  npm/                  ← One .md file per package
  rust/
  dotnet/
  python/
  go/
  homebrew/
  kubernetes/
  linux/
SCHEMA.md               ← LLM wiki maintenance instructions
```

## How to Use

**For maintainers:** Search the wiki for your package. If it's not there or shows "not audited" — that's a data point. Consider commissioning an audit or reaching out to security researchers.

**For security researchers:** After completing an audit (regardless of findings), open a PR adding or updating the package's wiki page. Zero-finding audits are just as valuable — they establish baseline coverage.

**For developers:** Before adding a dependency, check its audit history here alongside its CVE history.

## Contributing

1. Fork the repo
2. Add or update a wiki page in the appropriate ecosystem folder
3. Add your source document to `raw/` if applicable
4. Update `wiki/index.md` and `wiki/log.md`
5. Open a PR

See [SCHEMA.md](SCHEMA.md) for page format conventions.

## Relationship to Existing Databases

This is **not** a replacement for OSV, NVD, or Snyk. It's a **coverage layer on top** — tracking the research process, not just the outcomes.

| Database | Tracks | This KB Tracks |
|----------|--------|----------------|
| OSV.dev | Known CVEs | Whether audits happened |
| Snyk | Known CVEs + license | Audit scope + methodology |
| socket.dev | Behavioral anomalies | Historical research coverage |
| **This KB** | — | **Who looked, when, what they found or didn't find** |

## Vercel Website

A searchable web interface is planned at `oss-security.burmaster.com`. The GitHub repo is the source of truth; the website is a read-only view.

---

*Maintained by [Travis Burmaster](https://github.com/travis-burmaster) with LLM assistance. Not affiliated with any CVE authority or standards body.*
