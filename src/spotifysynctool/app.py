"""Application entry point and event loop."""

from __future__ import annotations

from typing import List, Tuple

import PySimpleGUI as sg

from .config import SPOTIFY_DL_ENV_VAR_TEXT, spotify_environment_variables_present
from .playlists import read_playlist_urls, save_playlist_urls
from .spotify import create_spotify_client, fetch_playlist_name
from .sync import sync_playlists
from .ui import (
    INPUT_KEY,
    PLAYLIST_NAME_KEY,
    PLAYLIST_URL_KEY,
    clear_input,
    create_main_window,
    update_playlist_lists,
)
from .validation import is_valid_url


def startup() -> Tuple[object, List[str], List[str], List[str]]:
    """Fetch initial data required by the application."""
    spotify_client = create_spotify_client()
    playlist_urls = read_playlist_urls("playlist_urls")
    playlist_names = [fetch_playlist_name(spotify_client, url) for url in playlist_urls]
    output: List[str] = []
    return spotify_client, playlist_urls, playlist_names, output


def run() -> None:
    """Run the GUI application."""
    spotify_client, playlist_urls, playlist_names, output = startup()
    window = create_main_window(playlist_urls, playlist_names, output)

    environment_checked = False

    while True:
        if not environment_checked:
            if not spotify_environment_variables_present():
                sg.Popup(SPOTIFY_DL_ENV_VAR_TEXT)
            environment_checked = True

        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Quit"):
            break

        if event == "Add":
            playlist_url = values.get(INPUT_KEY, "")
            if is_valid_url(playlist_url):
                try:
                    playlist_name = fetch_playlist_name(spotify_client, playlist_url)
                except Exception as exc:  # pragma: no cover - defensive logging only
                    print(exc)
                    print("error when fetching playlist name")
                else:
                    playlist_urls.append(playlist_url)
                    playlist_names.append(playlist_name)
                    clear_input(window)
                    update_playlist_lists(window, playlist_urls, playlist_names)
            else:
                sg.Popup("Malformed URL")

        if event == "Remove":
            selected = values.get(PLAYLIST_URL_KEY) or values.get(PLAYLIST_NAME_KEY)
            if selected:
                selected_value = selected[0]
                if selected_value in playlist_urls:
                    index = playlist_urls.index(selected_value)
                else:
                    index = playlist_names.index(selected_value)

                playlist_urls.pop(index)
                playlist_names.pop(index)
                update_playlist_lists(window, playlist_urls, playlist_names)
            else:
                sg.Popup("Select a playlist URL or name to be removed")

        if event == "Sync":
            sync_playlists(window, playlist_urls, playlist_names, output)

        if event == "Remove_All":
            playlist_urls.clear()
            playlist_names.clear()
            update_playlist_lists(window, playlist_urls, playlist_names)

        if event == "Save":
            save_playlist_urls(playlist_urls)

    window.close()


def main() -> None:
    """Poetry script entry point."""
    run()


if __name__ == "__main__":
    main()
