"""Playlist storage helpers."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, List


def save_playlist_urls(playlist_urls: Iterable[str], destination: str | Path = "playlist_urls.csv") -> None:
    """Persist the playlist URLs to a CSV file."""
    destination_path = Path(destination)
    with destination_path.open("w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerow(list(playlist_urls))


def read_playlist_urls(source: str | Path) -> List[str]:
    """Load playlist URLs from the CSV file located at *source*."""
    source_path = Path(source)
    if source_path.suffix != ".csv":
        source_path = source_path.with_suffix(".csv")

    try:
        with source_path.open() as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)
    except Exception as exc:  # pragma: no cover - closely mirrors previous behaviour
        raise Exception from exc

    if not rows:
        return []
    return list(rows[0])
