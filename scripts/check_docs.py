#!/usr/bin/env python3
"""Check Markdown documentation files and repository-relative links.

This checker intentionally has no third-party dependencies. It validates file
presence and local link targets; it does not render Markdown, validate remote
URLs, or prove that heading fragments exist.
"""

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?(?:\[[^\]]*\])\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")


def markdown_files():
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
        and not any(
            part.startswith(".") and part not in {".github"}
            for part in path.relative_to(ROOT).parts
        )
    )


def without_fenced_code(text):
    """Remove fenced code blocks so examples are not treated as links."""
    kept = []
    fence_char = None
    fence_length = 0

    for line in text.splitlines():
        stripped = line.lstrip()
        marker = chr(96) * 3
        if stripped.startswith(marker) or stripped.startswith("~~~"):
            current = marker[0] if stripped.startswith(marker) else "~"
            run_length = len(stripped) - len(stripped.lstrip(current))
            if fence_char is None:
                fence_char = current
                fence_length = run_length
            elif current == fence_char and run_length >= fence_length:
                fence_char = None
                fence_length = 0
            continue

        if fence_char is None:
            kept.append(line)

    return "\n".join(kept)


def local_link_targets(markdown_path, source):
    for match in MARKDOWN_LINK.finditer(without_fenced_code(source)):
        target = match.group(1) or match.group(2) or ""
        parsed = urlsplit(target.strip())

        if parsed.scheme or parsed.netloc or target.startswith("//"):
            continue
        if not parsed.path:
            continue

        decoded_path = unquote(parsed.path)
        destination = (markdown_path.parent / decoded_path).resolve()

        try:
            destination.relative_to(ROOT.resolve())
        except ValueError:
            yield target, None
            continue

        yield target, destination


def main():
    files = markdown_files()
    if not files:
        raise SystemExit("Documentation check failed: no Markdown files found.")

    empty_files = [
        path for path in files
        if not path.read_text(encoding="utf-8").strip()
    ]
    if empty_files:
        for path in empty_files:
            print(f"ERROR: empty Markdown file: {path.relative_to(ROOT)}")
        raise SystemExit(1)

    required = (ROOT / "README.md", ROOT / "docs" / "README.md")
    missing_required = [path for path in required if not path.is_file()]
    if missing_required:
        for path in missing_required:
            print(f"ERROR: required documentation entry point is missing: {path}")
        raise SystemExit(1)

    broken = []
    checked_links = 0

    for markdown_path in files:
        source = markdown_path.read_text(encoding="utf-8")
        for target, destination in local_link_targets(markdown_path, source):
            checked_links += 1
            if destination is None or not destination.exists():
                broken.append((markdown_path, target))

    if broken:
        for source_path, target in broken:
            print(
                "ERROR: broken local link in "
                f"{source_path.relative_to(ROOT)}: {target}"
            )
        raise SystemExit(
            f"Documentation check failed: {len(broken)} broken local link(s)."
        )

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "docs/README.md" not in readme:
        raise SystemExit(
            "Documentation check failed: README must link to docs/README.md."
        )

    print(f"Markdown files checked: {len(files)}")
    print(f"Local Markdown links checked: {checked_links}")
    print("Documentation entry points: OK")
    print("Local Markdown link targets: OK")
    print("Note: remote URLs and heading fragments are not checked.")


if __name__ == "__main__":
    main()
