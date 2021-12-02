# Spotify Sync Tool

A tool that helps you download and update Spotify playlists on your harddrive, so you can keep your music library updated offline as mp3s.
By pressing the "sync" button, all songs of the entered playlists are downloaded into respective playlist folders

![Image showing the user interface](https://user-images.githubusercontent.com/29024343/139120505-8072551f-e403-49eb-be5b-90f0e54317a4.png)

## Installation

You will need Python, poetry, ffmpeg and a Spotify Developer account in order for this program to run.
Complete the following steps:

1. Download this repository as a zip, extract it and navigate to the extracted folder (or `git clone` it).
2. Using the command line ([here is a guide to doing that](https://www.learnenough.com/command-line-tutorial#sec-running_a_terminal)),navigate to the extrated folder and run `pip install poetry` and `poetry install` to install the dependency manager poetry and then use it to actually install those dependencies.
3. The SyncTool needs a media conversion program called `ffmpeg` in order to function. Install `ffmpeg` and add it to your path as per this [tutorial](https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/).
4. Create a file called `.env` in the folder and enter the lines `client_id=<your_spotify_client_id` and `client_secret=<your_spotify_client_secret>` to it. The ID and secret are obtained by creating a Spotify Developer account and starting a sample app. Refer to the installation instruction from [spotipy here](https://github.com/plamere/spotipy) for a more exhaustive instruction.
5. Execute `main.exe` or run `python3 main.py` to start the tool.

## Usage

Install the tool and other requirements as specified above.
Since this tool relies on spotify_dl to parse the Spotify songs, you need to create a Spotify Developer account 
and export the 'client_id' and 'client_secret' environment variables before using it. 
For further reference, have a look at the spotify_dl documentation (https://github.com/SathyaBhat/spotify-dl)

Then, you can start the program. Add a playlist to your list of playlists to sync in the textfield at the bottom. Upon adding a playlist,
it is also stored in a local .CSV file that keeps track of the playlists you have, so they are restored on startup.

When you click sync, `spotify_dl` is executed for the given playlists, downloading the most recent songs you added.
