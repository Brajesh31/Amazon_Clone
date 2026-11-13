#!/usr/bin/env python3
"""Dependency-free structural checks for the static storefront."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
HTML_FILE = ROOT / "index.html"
REQUIRED_FILES = ("index.html", "amazone.css", "amazone.js")


class PageInspector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = set()
        self.ids = set()
        self.duplicate_ids = set()
        self.local_references = []
        self.title_text = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.add(tag)

        element_id = attrs.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)

        if tag == "title":
            self.in_title = True

        for attribute in ("src", "href"):
            value = attrs.get(attribute)
            if not value:
                continue
            parts = urlsplit(value)
            if parts.scheme or parts.netloc or value.startswith(("#", "/")):
                continue
            self.local_references.append(value.split("?", 1)[0].split("#", 1)[0])

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text.append(data)


def main():
    missing_required = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing_required:
        raise SystemExit(f"Missing required project files: {', '.join(missing_required)}")

    source = HTML_FILE.read_text(encoding="utf-8")
    page = PageInspector()
    page.feed(source)
    page.close()

    if "html" not in page.tags or "head" not in page.tags or "body" not in page.tags:
        raise SystemExit("index.html must contain html, head, and body elements.")
    if not "".join(page.title_text).strip():
        raise SystemExit("index.html must include a non-empty page title.")
    if page.duplicate_ids:
        raise SystemExit(
            "Duplicate HTML id values: " + ", ".join(sorted(page.duplicate_ids))
        )

    missing_references = sorted(
        {
            reference
            for reference in page.local_references
            if not (ROOT / reference).is_file()
        }
    )
    print("Static HTML structure: OK")
    print(f"Local file references checked: {len(page.local_references)}")
    if missing_references:
        print(
            "Known/missing local assets (warning, not a CI failure): "
            f"{len(missing_references)} unique path(s)"
        )
        for reference in missing_references:
            print(f"  - {reference}")
    else:
        print("All local file references resolve.")


if __name__ == "__main__":
    main()
