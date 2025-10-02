"""Spotify client helpers."""

from __future__ import annotations

import re
from typing import Any

import PySimpleGUI as sg
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from .config import get_spotify_credentials


def create_spotify_client() -> spotipy.Spotify:
    """Authenticate against Spotify and return a client instance."""
    client_id, client_secret = get_spotify_credentials()
    return spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    )


def fetch_playlist_name(spotify_client: spotipy.Spotify, playlist_url: str) -> Any:
    """Return the playlist name for the given URL."""
    pattern = r".+/(.+)$"
    match = re.search(pattern, playlist_url)
    if not match:
        raise ValueError(f"Unable to extract playlist id from URL: {playlist_url}")

    playlist_id = match.group(1)

    try:
        result = spotify_client.user_playlist(user=None, playlist_id=playlist_id, fields="name")
    except Exception as err:  # pragma: no cover - depends on Spotify responses
        sg.Popup(f"Could not fetch the url {playlist_url}")
        return err
    return result["name"]
