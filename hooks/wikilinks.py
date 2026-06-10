"""MkDocs hook: resolve [[wikilinks]] in wiki pages to relative markdown links.

Supports [[path/to/page]], [[page]], and [[target|label]] forms. Targets are
resolved against the page's own directory first, then the docs root, then by
bare filename anywhere in the wiki. Unresolvable targets render as plain text.
"""

import posixpath
import re

_WIKILINK = re.compile(r"\[\[([^\]|#]+)(#[^\]|]*)?(?:\|([^\]]+))?\]\]")

_by_path = {}
_by_name = {}


def on_files(files, config):
    _by_path.clear()
    _by_name.clear()
    for f in files:
        if f.src_uri.endswith(".md"):
            key = f.src_uri[:-3]
            _by_path[key] = f.src_uri
            _by_name.setdefault(posixpath.basename(key), f.src_uri)
    return files


def on_page_markdown(markdown, page, config, files):
    src_dir = posixpath.dirname(page.file.src_uri)

    def repl(match):
        target = match.group(1).strip()
        anchor = match.group(2) or ""
        label = (match.group(3) or target).strip()
        dest = (
            _by_path.get(posixpath.normpath(posixpath.join(src_dir, target)))
            or _by_path.get(target)
            or _by_name.get(posixpath.basename(target))
        )
        if not dest:
            return label
        rel = posixpath.relpath(dest, src_dir or ".")
        return f"[{label}]({rel}{anchor})"

    return _WIKILINK.sub(repl, markdown)
