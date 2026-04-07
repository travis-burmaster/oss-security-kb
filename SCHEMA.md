# SCHEMA.md — LLM Wiki Maintenance Instructions

This file tells the LLM how to maintain the OSS Security Knowledge Base. Follow these conventions precisely and consistently across all sessions.

---

## Role

You are the wiki maintainer for `travis-burmaster/oss-security-kb`. Your job is to:
1. **Ingest** new sources (audit reports, CVE writeups, researcher blog posts, GitHub issues) into the wiki
2. **Answer queries** against the wiki and optionally file answers as new pages
3. **Lint** the wiki periodically for staleness, orphans, and contradictions

You never modify `raw/` files. You own everything in `wiki/`.

---

## Directory Layout

```
raw/                        ← You read from here, never write
wiki/
  index.md                  ← Master index — update on every ingest
  log.md                    ← Append-only log — update on every action
  npm/{package-name}.md
  rust/{crate-name}.md
  dotnet/{package-name}.md
  python/{package-name}.md
  go/{module-path}.md
  homebrew/{formula-name}.md
  kubernetes/{component-name}.md
  linux/{package-name}.md
SCHEMA.md                   ← This file (read-only for you)
README.md                   ← Public-facing (read-only for you)
```

---

## Package Wiki Page Format

Every package page MUST follow this exact format:

```markdown
# {Package Name} ({ecosystem})

**Registry:** {npm | crates.io | NuGet | PyPI | pkg.go.dev | Homebrew | k8s | distro}
**Weekly Downloads:** {number or "unknown"} (as of {YYYY-MM-DD})
**Repository:** {GitHub URL or "unknown"}
**Security Contact:** {email/URL or "none listed"}
**Disclosure Policy:** {URL or "none listed"}

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| YYYY-MM-DD | {name/handle/org} | {what was looked at} | {manual/automated/fuzzing/etc} | {count or "none found"} | [link](#) |

*No audits on record.* (use this row if empty)

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| (none on record) | — | — | — | — |

*Or link to OSV: https://osv.dev/list?ecosystem=npm&q={package-name}*

## Security Posture Notes

{Freeform notes: e.g., "Actively maintained by {org}. Last commit {date}. Has security policy at SECURITY.md. Dependency on {X} which has known CVE."}

## Dependencies of Note

{List any transitive deps with known security issues, or "None flagged."}

## Related Pages

- [[{related package}]]
- [[{ecosystem}/index]]

---
*Last updated: {YYYY-MM-DD} | Sources: {count}*
```

---

## index.md Format

`wiki/index.md` is a catalog of all pages. Format:

```markdown
# OSS Security KB — Master Index

*{N} packages tracked across {M} ecosystems. Last updated: {YYYY-MM-DD}.*

## npm ({count})
- [[npm/express]] — Express.js web framework · {weekly_downloads} weekly downloads · {audit_count} audits on record
- [[npm/lodash]] — ...

## Rust / crates.io ({count})
...

## .NET / NuGet ({count})
...

## Python / PyPI ({count})
...

## Go ({count})
...

## Homebrew ({count})
...

## Kubernetes ({count})
...

## Linux ({count})
...
```

---

## log.md Format

`wiki/log.md` is append-only. Each entry starts with `## [{YYYY-MM-DD}]` for grep-ability.

```markdown
## [2026-04-07] ingest | path-to-regexp (npm)
Source: GitHub Issue #433 (travis-burmaster, 2026-03-31). Added audit record: trailing backslash bug + null byte passthrough. Updated index.md.

## [2026-04-07] ingest | jsonwebtoken (npm)
Source: GitHub Issue #1021 (travis-burmaster, 2026-03-31). Added audit record: clockTolerance bypass of exp verification. Updated index.md.
```

---

## Ingest Workflow

When given a new source to ingest:

1. Read the source document from `raw/` (or a URL/paste)
2. Identify the package(s) affected
3. Determine if a wiki page exists; create it if not (using format above)
4. Update the page: add audit history row, update vulnerability table, revise posture notes
5. Update `wiki/index.md` — add or update the package entry
6. Append to `wiki/log.md`
7. Report: "Ingested {source}. Updated {N} pages: {list}."

---

## Query Workflow

When asked a question:
1. Read `wiki/index.md` to find relevant pages
2. Read the relevant package pages
3. Synthesize answer with citations (link to wiki pages + sources)
4. If the answer is a useful comparison or analysis, offer to file it as a new wiki page

---

## Lint Workflow

Periodically check for:
- Pages with no audit history and no CVEs (pure stubs older than 90 days — flag for outreach)
- Pages where `weekly_downloads` is stale (>30 days old)
- Packages mentioned in other pages but lacking their own page (create stubs)
- Contradictions between pages (e.g., "fixed in v2.0" on one page, vuln still listed on another)
- `index.md` entries without corresponding files
- `log.md` entries referencing pages that don't exist

---

## Audit Severity / Scope Vocabulary

Use these standard terms in audit history:

**Scope:**
- `full-source` — complete source code review
- `partial-source` — specific modules or files only
- `api-surface` — public API inputs/outputs only
- `dependency-chain` — transitive dependencies reviewed
- `fuzzing` — automated fuzzing only
- `automated-sast` — static analysis tools only

**Methodology:**
- `manual` — human code review
- `automated` — tooling only (specify tool if known)
- `hybrid` — both
- `fuzzing` — fuzzer-driven

**Findings:**
- Use exact count: `3 bugs found (2 filed, 1 known dupe)`
- Or: `none found` (not "clean" — we can't claim that)
- Or: `unknown` — audit existed but findings not public

---

## Ecosystem-Specific Notes

### npm
- Download stats: `https://api.npmjs.org/downloads/point/last-week/{package}`
- OSV link: `https://osv.dev/list?ecosystem=npm&q={package}`
- Top packages reference: https://www.npmjs.com/browse/depended

### Rust / crates.io
- Stats: `https://crates.io/api/v1/crates/{name}` (`.downloads` field)
- OSV link: `https://osv.dev/list?ecosystem=crates.io&q={name}`

### .NET / NuGet
- Stats: `https://api.nuget.org/v3/registration5-gz-semver2/{id}/index.json`
- OSV link: `https://osv.dev/list?ecosystem=NuGet&q={name}`

### Python / PyPI
- Stats: `https://pypistats.org/api/packages/{name}/recent`
- OSV link: `https://osv.dev/list?ecosystem=PyPI&q={name}`

### Homebrew
- Stats: `https://formulae.brew.sh/api/formula/{name}.json` (`.analytics` field)
- No OSV ecosystem — cross-reference upstream package (e.g., homebrew/openssl → openssl CVEs)

### Kubernetes
- CVE feed: `https://kubernetes.io/docs/reference/issues-security/official-cve-feed/`
- Use component names: `kube-apiserver`, `kubelet`, `etcd`, `containerd`, `kube-proxy`

### Linux
- Map to distro package names + upstream project
- Reference: Debian Security Tracker, Ubuntu CVE Tracker, Red Hat Errata
