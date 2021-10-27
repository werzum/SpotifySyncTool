# Spotify Sync Tool

A tool that helps you download and update Spotify playlists on your harddrive, so you can keep your music library updated offline as mp3s.
By pressing the "sync" button, all songs of the entered playlists are downloaded into respective playlist folders

![Uploading image.png…](Image showing the user interface)

## Installation

### Binary (regular usage)

1. `pip install` the dependencies
2. Create a .env and add `client_id=<your_spotify_client_id` and `client_secret=<your_spotify_client_secret> to it.
3. Execute `main.exe`

### From Source

1. `pip install` the dependencies
2. Create a .env and add `client_id=<your_spotify_client_id` and `client_secret=<your_spotify_client_secret> to it.
3. Run the program with `python3 main.py`

## Usage

Install the tool with python

Since this tool relies on spotify_dl to parse the Spotify songs, you need to create a Spotify Developer account 
and export the 'client_id' and 'client_secret' environment variables. For further reference, have a look at the spotify_dl documentation (https://github.com/SathyaBhat/spotify-dl)

Then, spotipy_should be able to download songs.
