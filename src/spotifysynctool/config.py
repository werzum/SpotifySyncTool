"""Configuration helpers for environment handling."""

from __future__ import annotations

import os
from typing import Tuple

from dotenv import load_dotenv

SPOTIFY_DL_ENV_VAR_TEXT = """
You need to set your Spotify API credentials. You can do this by
setting environment variables like so:

export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
Get your credentials at
                https://developer.spotify.com/my-applications
"""


def _load_environment() -> None:
    """Ensure values from a local .env file are visible in ``os.environ``."""
    load_dotenv()


def get_spotify_credentials() -> Tuple[str | None, str | None]:
    """Fetch Spotify client credentials from the environment."""
    _load_environment()
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    return client_id, client_secret


def spotify_environment_variables_present() -> bool:
    """Return ``True`` when the required Spotify credentials are configured."""
    client_id, client_secret = get_spotify_credentials()
    return bool(client_id and client_secret)
