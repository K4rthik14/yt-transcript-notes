"""Helper functions for text processing and formatting."""

import re


def extract_title_from_markdown(markdown_text: str) -> str:
    """
    Extract the main title (# Title) from generated Markdown.

    Args:
        markdown_text: The markdown content string.

    Returns:
        Extracted title or fallback title if not found.
    """
    if not markdown_text:
        return "notes"

    # Search for H1 header, e.g. "# Title Here"
    match = re.search(r"^#\s+(.+)$", markdown_text, re.MULTILINE)
    if match:
        # Strip markdown formatting like bold/italics from title
        clean_title = re.sub(r"[\*\_\`\#]", "", match.group(1)).strip()
        if clean_title:
            return clean_title

    # Fallback to first non-empty line
    for line in markdown_text.splitlines():
        cleaned = line.strip("# ").strip()
        if cleaned:
            return cleaned[:50]

    return "notes"


def generate_filename(markdown_text: str) -> str:
    """
    Generate a clean .md filename based on the markdown title.

    Args:
        markdown_text: The markdown content string.

    Returns:
        Sanitized filename with .md extension.
    """
    title = extract_title_from_markdown(markdown_text)
    # Convert to lowercase and replace spaces/special chars with hyphens
    slug = re.sub(r"[^\w\s-]", "", title.lower()).strip()
    slug = re.sub(r"[-\s]+", "-", slug)

    if not slug:
        slug = "notes"

    return f"{slug}.md"


def calculate_text_stats(text: str) -> tuple[int, int]:
    """
    Calculate character and word count for a given text.

    Args:
        text: Input string.

    Returns:
        Tuple of (character_count, word_count).
    """
    char_count = len(text)
    word_count = len(text.split())
    return char_count, word_count
