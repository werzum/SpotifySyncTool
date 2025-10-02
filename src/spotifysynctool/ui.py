"""UI helpers built with PySimpleGUI."""

from __future__ import annotations

from typing import List

import PySimpleGUI as sg


PLAYLIST_URL_KEY = "listbox_url"
PLAYLIST_NAME_KEY = "listbox_name"
OUTPUT_KEY = "listbox_output"
INPUT_KEY = "input"


def create_main_window(playlist_urls: List[str], playlist_names: List[str], output: List[str]) -> sg.Window:
    """Instantiate the main PySimpleGUI window."""
    layout = [
        [
            sg.Frame(
                layout=[
                    [sg.Listbox(values=playlist_urls, size=(80, 10), key=PLAYLIST_URL_KEY)],
                    [sg.Listbox(values=playlist_names, size=(80, 10), key=PLAYLIST_NAME_KEY)],
                    [sg.Listbox(values=output, size=(80, 5), key=OUTPUT_KEY)],
                ],
                title="Playlists",
            )
        ],
        [sg.Input(key=INPUT_KEY, enable_events=True)],
        [sg.Button("Add", bind_return_key=True), sg.Button("Remove"), sg.Button("Remove_All")],
        [sg.Button("Sync"), sg.Button("Quit"), sg.Button("Save")],
    ]

    return sg.Window("Spotify Sync", layout)


def update_playlist_lists(window: sg.Window, playlist_urls: List[str], playlist_names: List[str]) -> None:
    """Refresh the playlist listboxes with the provided data."""
    window[PLAYLIST_URL_KEY].update(playlist_urls)
    window[PLAYLIST_NAME_KEY].update(playlist_names)


def update_output(window: sg.Window, output: List[str]) -> None:
    """Refresh the output listbox."""
    window[OUTPUT_KEY].update(output)


def clear_input(window: sg.Window) -> None:
    """Clear the playlist URL input field."""
    window[INPUT_KEY].update("")
