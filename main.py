import os
import PySimpleGUI as sg

from dotenv import load_dotenv

from playlist_management import *
from utilities import *

def startup():
	"""
	A method run at startup which reads URLs from the CSV to a list
	and fetches their names via the spotify API
	"""
	sp = create_spotify_client()

	#read the urls from the CSV
	playlist_urls = read_playlist_urls("playlist_urls")

	#and fetch the respective names from Spotify
	playlist_names = [fetch_playlist_name(sp,x) for x in playlist_urls]

	#empty stdout window
	output = []

	return sp, playlist_urls, playlist_names, output

def create_spotify_client():
	"""Load the environment vars and authenticate spotipy with them"""
	#load .env file
	load_dotenv()
	client_id = os.getenv("client_id")
	client_secret = os.getenv("client_secret")

	#authenticate with spotify to fetch info about playlist
	return spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
															   client_secret=client_secret))

def create_window_elements(playlist_urls,playlist_names, output):
	"""Define the contents of the window and return window, layout"""

	# Define the window's contents
	layout = [[sg.Frame(layout=[
				[sg.Listbox(values=playlist_urls,size=(80,10),key="listbox_url")],
				[sg.Listbox(values=playlist_names,size=(80,10),key="listbox_name")],
				[sg.Listbox(values=output,size=(80,5),key="listbox_output")]
			],title="Playlists")],
			[sg.Input(key="input",enable_events=True)],
			[sg.Button("Add",bind_return_key=True),sg.Button("Remove"),sg.Button("Remove_All")],
			[sg.Button('Sync'), sg.Button('Quit'), sg.Button("Save")]]


	# Create the window
	window = sg.Window('Spotify Sync', layout)
	return window, layout

def main():
	sp, playlist_urls, playlist_names, output = startup()

	window, layout = create_window_elements(playlist_urls,playlist_names, output)

	# Display and interact with the Window using an Event Loop
	counter = 0
	while True:

		#hacky solution for checking environment variable only once
		if counter == 0:
			if spotify_environment_variables_present() == False:
				sg.Popup(spotify_dl_env_var_text)
			counter+=1

		event, values = window.read()

		if event == "Add":
			input = values["input"]
			if check_valid_url(input):
				try:
					playlist_names.append(fetch_playlist_name(sp,input))
				except Exception as e:
					print(e)
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
			sync(window, playlist_urls, playlist_names, output)

		if event == "Remove_All":
			plalyist_urls = []
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
