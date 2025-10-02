"""Validation helpers."""

import validators


def is_valid_url(url: str) -> bool:
    """Return ``True`` when *url* is a syntactically valid URL."""
    return bool(validators.url(url))
