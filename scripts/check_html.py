#!/usr/bin/env python3
"""Validate the static storefront's required files and local HTML references.

This checker intentionally uses only Python's standard library. It is a fast
repository guard, not a complete HTML conformance or browser-rendering test.
"""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
HTML_FILE = ROOT / "index.html"
REQUIRED_FILES = ("index.html", "amazone.css", "amazone.js")


class PageInspector(HTMLParser):
    """Collect structural metadata and relative resource references."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = set()
        self.ids = set()
        self.duplicate_ids = set()
        self.local_references = []
        self.image_count = 0
        self.images_without_alt = []
        self.title_text = []
        self.in_title = False
        self.document_language = None
        self.has_charset = False
        self.has_viewport = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        self.tags.add(tag)

        if tag == "html":
            self.document_language = attributes.get("lang")

        if tag == "meta":
            if attributes.get("charset"):
                self.has_charset = True
            if attributes.get("name", "").lower() == "viewport":
                self.has_viewport = True

        element_id = attributes.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)

        if tag == "title":
            self.in_title = True

        if tag == "img":
            self.image_count += 1
            if "alt" not in attributes:
                self.images_without_alt.append(attributes.get("src", "<unknown src>"))

        for attribute in ("src", "href"):
            value = attributes.get(attribute)
            if not value:
                continue

            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc or value.startswith(("#", "/")):
                continue

            relative_path = unquote(parsed.path)
            if relative_path:
                self.local_references.append(relative_path)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text.append(data)


def fail(message):
    raise SystemExit(f"HTML validation failed: {message}")


def main():
    missing_required = [
        name for name in REQUIRED_FILES if not (ROOT / name).is_file()
    ]
    if missing_required:
        fail("missing required files: " + ", ".join(missing_required))

    page = PageInspector()
    try:
        page.feed(HTML_FILE.read_text(encoding="utf-8"))
        page.close()
    except (OSError, UnicodeError) as error:
        fail(f"could not read index.html: {error}")

    required_tags = {"html", "head", "body"}
    missing_tags = sorted(required_tags - page.tags)
    if missing_tags:
        fail("missing required document elements: " + ", ".join(missing_tags))

    if not page.document_language:
        fail("the html element must declare a document language")

    if not page.has_charset:
        fail("a character encoding declaration is required")

    if not page.has_viewport:
        fail("a viewport meta declaration is required")

    if not "".join(page.title_text).strip():
        fail("index.html must include a non-empty page title")

    if page.duplicate_ids:
        fail("duplicate HTML id values: " + ", ".join(sorted(page.duplicate_ids)))

    if page.images_without_alt:
        fail(
            "every img element must explicitly declare alt; review these sources: "
            + ", ".join(page.images_without_alt)
        )

    missing_references = sorted(
        {
            reference
            for reference in page.local_references
            if not (ROOT / reference).is_file()
        }
    )

    print("Static HTML structure: OK")
    print(f"Document language: {page.document_language}")
    print(f"Image elements with explicit alt attributes: {page.image_count}")
    print(f"Local file references checked: {len(page.local_references)}")

    if missing_references:
        print(
            "Missing local references (warning, not a CI failure): "
            f"{len(missing_references)} unique path(s)"
        )
        for reference in missing_references:
            print(f"  - {reference}")
    else:
        print("All local file references resolve.")


if __name__ == "__main__":
    main()
