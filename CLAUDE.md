# Claude Code — Project Instructions

This file is read automatically at the start of every Claude Code session in this repository. It captures validated environment behaviour so each run doesn't have to rediscover it.

## Environment constraints (validated 2026-11-19)

### Git / push
As of 2026-11-19, `git push -u origin <branch>` works through the session's git proxy (`git push --dry-run origin HEAD:refs/heads/access-check` is a cheap check). The 2026-06-18 note that push returned HTTP 403 is no longer accurate. Commit locally and push the `nightly/oss-kb-<UTC YYYYMMDD-HHMM>` branch with git.

For PRs and merges, use the MCP GitHub tools (load them with ToolSearch if they are deferred):
- **Open PR:** `mcp__github__create_pull_request`
- **Merge PR:** `mcp__github__merge_pull_request` with `merge_method: squash`
- `mcp__github__create_branch` / `mcp__github__push_files` still work as a fallback if git push is refused.

### `gh` CLI
`gh` is installed, but use it only for search: `gh api -X GET search/code -f q='<terms> repo:github/advisory-database'` (a few searches per minute; sleep ~7s between calls). Use the MCP tools for everything else.

### Network reachability (2026-11-20)
- **Works:** raw.githubusercontent.com (advisory-database, rustsec/advisory-db, upstream project files such as `nginx/nginx/<branch>/docs/xml/nginx/changes.xml`, and `cisagov/kev-data/develop/known_exploited_vulnerabilities.json` for CISA KEV status), GitHub code search via `gh api`, WebSearch.
- **Blocked:** api.osv.dev, nginx.org, services.nvd.nist.gov, www.cve.org, my.f5.com, www.php.net, cert.europa.eu, www.openssh.org, www.openssh.com, unauthenticated api.github.com REST.

### OSV.dev API
`https://api.osv.dev` returns **HTTP 403** (blocked by network policy). Use these fallbacks:
- **RustSec advisories:** fetch `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/<crate>/<ID>.md` with curl or WebFetch, found via `gh api` code search with `repo:rustsec/advisory-db`.
- **GHSA records:** fetch `https://raw.githubusercontent.com/github/advisory-database/main/advisories/.../<GHSA-id>/<GHSA-id>.json`, found via `gh api` code search with `repo:github/advisory-database`. Unreviewed (non-package) records for C projects such as nginx live under `advisories/unreviewed/<YYYY>/<MM>/`.
- `mcp__github__get_file_contents` is restricted to `travis-burmaster/oss-security-kb` only.

### Notification
After a successful nightly pass, send a push notification via PushNotification so the owner sees results on mobile / email. Always send one — either on success (pages added, PR merged) or on failure (what blocked the run).

## Advisory-review pass — working procedure

1. **Read state:** `wiki/index.md`, `wiki/log.md` (newest-first), and the relevant ecosystem index files to establish what is already covered.
2. **Select targets:** 1–3 packages from under-covered ecosystems; prefer those with no existing KB page and high download counts or CNCF/critical-infrastructure importance.
3. **Research advisories:** Use `gh api` code search + raw.githubusercontent.com for rustsec/advisory-db and github/advisory-database. Use crates.io API, pkg.go.dev, and registry metadata via WebFetch.
4. **Write pages** under `wiki/<ecosystem>/` following `SCHEMA.md`. Every vulnerability row must cite a primary source (GHSA, RUSTSEC, OSV, or upstream advisory). No invented findings.
5. **Update indexes:** ecosystem index file, `wiki/index.md` (page count), `wiki/log.md` (prepend entry, newest-first).
6. **Save evidence:** `raw/advisory-review-<YYYYMMDD-HHMM>/notes.md` with all URLs consulted.
7. **Ship:**
   a. Create branch `nightly/oss-kb-<UTC YYYYMMDD-HHMM>` from up-to-date main.
   b. Commit all changed/new files in one commit and `git push -u origin <branch>` (fallback: `mcp__github__create_branch` + `mcp__github__push_files`).
   c. `mcp__github__create_pull_request` — base `main`, include self-review checklist in body.
   d. `mcp__github__merge_pull_request` — `merge_method: squash`.
8. **Notify** via PushNotification with PR number, pages added, and advisory counts.

## Ground rules

- **Advisory mapping only.** Every vulnerability row must be backed by a named public source. Do not infer or fabricate findings.
- **Own wiki only.** Only write to `wiki/` and `raw/` in this repository. Do not attempt to push to `rustsec/advisory-db`, `github/advisory-database`, or any other repo.
- **SCHEMA.md and METHODOLOGY.md compliance.** Page structure must match the schema.
- **No OSV.dev dependency.** Treat OSV as a nice-to-have; the pass must complete without it.
