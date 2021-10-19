import csv
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import validators
import re

import PySimpleGUI as sg

#Sync Functionalities

def sync(playlists):
	sg.Popup('Sync Started', keep_on_top=True)
	for value in playlist_urls:
		subprocess.Popen('spotify_dl -l '+value+ " -o", shell=True)

def update_playlists(window,playlist_urls,playlist_names):
	window["listbox_url"].update(playlist_urls)
	window["listbox_name"].update(playlist_names)

def remove_from_playlist(window,playlist_urls,playlist_names,index):
	playlist_urls.pop(index)
	playlist_names.pop(index)
	update_playlists(window,playlist_urls,playlist_names)

## Loading playlists

def fetch_playlist_name(sp, playlist_url):
	#extract the id from the url, applying the regex from above and removing the contained
	#/ with this workaround - dont want to fiddle with the regex yet
	#regex pattern that matches the last / of the spotify url
	pattern = ".+(\/.+)$"
	playlist_id = re.search(pattern, playlist_url).group(1)[1:]

	try:
	   result = sp.user_playlist(user=None, playlist_id=playlist_id, fields="name")
	except Exception as err:
		sg.Popup(f"Could not fetch the url {playlist_url}")
		return err
	else:
	   return result["name"]


def check_valid_url(url):
	return validators.url(url)


## CSV loading and saving

def save_urls_to_csv(playlist_urls):
	with open("playlist_urls.csv","w") as csv_file:
		write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
		write.writerow(playlist_urls)

def read_playlist_urls():
	#read the urls from the CSV
	playlist_urls = []
	with open("playlist_urls.csv") as csv_file:
		reader = csv.reader(csv_file)
		#stupid unpacking hack that surely has a more elegant solution somewhere
		temp_list = list(reader)
		for elm in temp_list[0]:
			playlist_urls.append(elm)
	return playlist_urls
