import validators
from dotenv import load_dotenv
import os

spotify_dl_env_var_text = """
You need to set your Spotify API credentials. You can do this by
setting environment variables like so:

export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
Get your credentials at
                https://developer.spotify.com/my-applications
"""


def check_valid_url(url):
	return validators.url(url)

def spotify_environment_variables_present():
	
	load_dotenv()
	client_id = os.getenv("SPOTIPY_CLIENT_ID")
	client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
	
	if client_id and client_secret:
		return True
	else:
		return False