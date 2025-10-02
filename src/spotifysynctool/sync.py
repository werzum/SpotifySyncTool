"""Playlist synchronisation helpers."""

from __future__ import annotations

from subprocess import PIPE, Popen
from typing import List

import PySimpleGUI as sg


def sync_playlists(window: sg.Window, playlist_urls: List[str], playlist_names: List[str], output: List[str]) -> None:
    """Run ``spotify_dl`` for each playlist and stream the output to the UI."""
    for url, name in zip(playlist_urls, playlist_names):
        cmd = ["spotify_dl", "-l", url, "-o", name]
        process = Popen(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        for line in iter(process.stdout.readline, ""):
            output.append(line.rstrip())
            window["listbox_output"].update(output)
            window.refresh()
