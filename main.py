import os
import subprocess
import PySimpleGUI as sg
import spotipy
import re
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import validators
import csv


def startup():
	sp = create_spotify_client()

	#read the urls from the CSV
	playlist_urls = playlist_urls()

	#and fetch the respective names from Spotify
	playlist_names = [fetch_playlist_name(x) for x in playlist_urls]

	return sp, playlist_urls, playlist_names

def create_spotify_client():
	#load .env file
	load_dotenv()
	client_id = os.getenv("client_id")
	client_secret = os.getenv("client_secret")

	#authenticate with spotify to fetch info about playlist
	return spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
															   client_secret=client_secret))

#regex pattern that matches the last / of the spotify url
pattern = ".+(\/.+)$"

def fetch_playlist_name(playlist_url):
	#extract the id from the url, applying the regex from above and removing the contained
	#/ with this workaround - dont want to fiddle with the regex yet
	playlist_id = re.search(pattern, playlist_url).group(1)[1:]

	try:
	   result = sp.user_playlist(user=None, playlist_id=playlist_id, fields="name")
	except:
		sg.Popup(f"Could not fetch the url {playlist_url}")
		return Error
	else:
	   return result["name"]

def read_playlist_urls()
	#read the urls from the CSV
	playlist_urls = []
	with open("playlist_urls.csv") as csv_file:
		reader = csv.reader(csv_file)
		#stupid unpacking hack that surely has a more elegant solution somewhere
		temp_list = list(reader)
		for elm in temp_list[0]:
			playlist_urls.append(elm)
	return playlist_urls

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

def check_valid_url(url):
	return validators.url(url)

def save_urls_to_csv(playlist_urls):
	with open("playlist_urls.csv","w") as csv_file:
		write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
		write.writerow(playlist_urls)

def create_window_elements():
	# Define the window's contents
	layout = [[sg.Frame(layout=[
				[sg.Listbox(values=playlist_urls,size=(80,10),key="listbox_url")],
				[sg.Listbox(values=playlist_names,size=(80,10),key="listbox_name")],
			],title="Playlists")],
			[sg.Input(key="input",enable_events=True)],
			[sg.Button("Add",bind_return_key=True),sg.Button("Remove"),sg.Button("Remove_All")],
			[sg.Button('Sync'), sg.Button('Quit'), sg.Button("Save")]]


	# Create the window
	window = sg.Window('Spotify Sync', layout)

def main():
	sp, playlist_urls, playlist_names = startup()

	window, layout = create_window_elements()

	# Display and interact with the Window using an Event Loop
	while True:
		event, values = window.read()

		if event == "Add":
			input = values["input"]
			if check_valid_url(input):
				try:
					playlist_names.append(fetch_playlist_name(input))
				except:
					print("error when fetching playlist name")
				else:
					playlist_urls.append(input)
				
				window["input"].value = ""
				update_playlists(window,playlist_urls,playlist_names)
			else:
				sg.Popup('Malformed URL')

		if event == "Remove":
			try:
				index = window.Element('listbox_url').Widget.curselection()[0]
			except:
				try:
					index = window.Element('listbox_name').Widget.curselection()[0]
				except:
					sg.Popup("Select a playlist URL or name to be removed")
				else:
					remove_from_playlist(window,playlist_urls,playlist_names,index)    
			else:
				remove_from_playlist(window,playlist_urls,playlist_names,index)

		if event == "Sync":
			sync(playlist_urls)

		if event == "Remove_All":
			playlist_urls = []
			playlist_names = []
			update_playlists(window,playlist_urls,playlist_names)

		if event == "Save":
			save_urls_to_csv(playlist_urls)

		# See if user wants to quit or window was closed
		if event == sg.WINDOW_CLOSED or event == 'Quit':
			break

	# Finish up by removing from the screen
	window.close()


if __name__ == "__main__":
	main()
