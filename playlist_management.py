import csv
import subprocess

from subprocess import Popen, PIPE

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import re
import PySimpleGUI as sg

#Sync Functionalities

def sync(window, playlist_urls, playlist_names, output):
	"""
	Call the spotify_dl function for the playlist_urls and playlist_names,
	passing the returned output to the listbox_output element
	"""
	for url,name in zip(playlist_urls,playlist_names):
		cmd = ["spotify_dl","-l",url,"-o",name]
		p = Popen(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True)
		for line in iter(p.stdout.readline, b''):
			output.append(line.rstrip())
			window["listbox_output"].update(output)
			window.Refresh()

def update_playlists(window,playlist_urls,playlist_names):
	"""update both passed arrays for listbox_url and listbox_name elements"""
	window["listbox_url"].update(playlist_urls)
	window["listbox_name"].update(playlist_names)

def remove_from_playlist(window,playlist_urls,playlist_names,index):
	"""remove the entry at the given index from playlist_names and playlist_urls"""
	playlist_urls.pop(index)
	playlist_names.pop(index)
	update_playlists(window,playlist_urls,playlist_names)

## Loading playlists

def fetch_playlist_name(sp, playlist_url):
	"""
	 Extracting the playlist id from the url with a regex removing the contained
	"/" with this workaround - dont want to fiddle with the regex yet, and return its name
	"""

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


## CSV loading and saving

def save_urls_to_csv(playlist_urls):
	""" Saving an array of URLs to a CSV called playlist_urls.csv """
	with open("playlist_urls.csv","w") as csv_file:
		write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
		write.writerow(playlist_urls)

def read_playlist_urls(csv_file_path):
	""" Read playlist URLs into array from a CSV on the given path """
	playlist_urls = []
	try:
		with open(csv_file_path+".csv") as csv_file:
			reader = csv.reader(csv_file)
			#stupid unpacking hack that surely has a more elegant solution somewhere
			temp_list = list(reader)
			for elm in temp_list[0]:
				playlist_urls.append(elm)

		return playlist_urls
	except:
		raise Exception