#!/usr/bin/env python3
"""Clean Jina Reader noise from Surge documentation markdown files.

Removes GitBook page chrome (sidebar, share buttons, theme toggles, search
placeholders, pagination links) while preserving Title/URL Source/Published
Time metadata and all actual documentation content.

Usage:
    python clean_surge_docs.py
"""

import re
from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "docs" / "manual"


def clean_markdown(text: str) -> str:
    """Apply all cleaning rules to a markdown string, in order."""

    # 1. Remove "Markdown Content:" marker line
    text = re.sub(r"^Markdown Content:\n", "", text, flags=re.MULTILINE)

    # 2. Remove GitBook sidebar navigation block
    #    From "* [Back to Surge Website]" through "* [Published with GitBook]"
    #    Note: use [^\n]* instead of .* at the end to avoid DOTALL eating the rest
    text = re.sub(
        r"^\*\s+\[Back to Surge Website\].*?^\*\s+\[Published with GitBook\][^\n]*\n?",
        "",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )

    # 3. Remove duplicate setext h1: "XXX · GitBook\n=====\n"
    text = re.sub(r"^.+ · GitBook\n={3,}\n", "", text, flags=re.MULTILINE)

    # 4. Remove duplicate setext h1 with link: "[Title](url)\n=====\n"
    text = re.sub(
        r"^\[.+?\]\(https://manual\.nssurge\.com/[^)]*\)\n={3,}\n",
        "",
        text,
        flags=re.MULTILINE,
    )

    # 5. Remove empty anchor links (with #): [](url#) possibly two on same line
    text = re.sub(
        r"^\[?\]\(https://manual\.nssurge\.com/[^)]*#\)"
        r"(\[\]\(https://manual\.nssurge\.com/[^)]*#\))?\n",
        "",
        text,
        flags=re.MULTILINE,
    )

    # 6. Remove share buttons line
    text = re.sub(
        r"^Facebook Google\+Twitter Weibo Instapaper\n",
        "",
        text,
        flags=re.MULTILINE,
    )

    # 7. Remove theme toggle UI (three consecutive lines)
    text = re.sub(r"^A A\n+Serif Sans\n+White Sepia Night\n", "", text, flags=re.MULTILINE)

    # 8. Remove search placeholders
    text = re.sub(r'^results matching ""\n={3,}\n+', "", text, flags=re.MULTILINE)
    text = re.sub(r'^No results matching ""\n[=\-]{3,}\n', "", text, flags=re.MULTILINE)

    # 9. Remove pagination links at end of file (empty-text links, URL without #)
    text = re.sub(
        r"^\[\]\(https://manual\.nssurge\.com/[^#)]+\)"
        r"(\[\]\(https://manual\.nssurge\.com/[^#)]+\))?\s*$",
        "",
        text,
        flags=re.MULTILINE,
    )

    # 10. Collapse 3+ consecutive blank lines into 1
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 11. Strip leading/trailing whitespace
    text = text.strip() + "\n"

    return text


def main():
    md_files = sorted(DOCS_DIR.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files in {DOCS_DIR}")

    for path in md_files:
        original = path.read_text(encoding="utf-8")
        cleaned = clean_markdown(original)
        if cleaned != original:
            path.write_text(cleaned, encoding="utf-8")
            print(f"  Cleaned: {path.relative_to(DOCS_DIR)}")
        else:
            print(f"  Skipped (no change): {path.relative_to(DOCS_DIR)}")

    print(f"\nDone. Processed {len(md_files)} files.")


if __name__ == "__main__":
    main()
