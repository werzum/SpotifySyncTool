import os
import subprocess
import PySimpleGUI as sg


playlist_urls = [
"https://open.spotify.com/playlist/6mWCb6tfH3P60ZHPIGsaLV?si=d5a58a4f8259492e",
"https://open.spotify.com/playlist/7s7ZxjKQ48dSCmuQgdd9rj?si=4b33d984cfec4894",
"https://open.spotify.com/playlist/6BDwGc3oqC2ECKn95xa2YW?si=d717f5fe30e849c7",
"https://open.spotify.com/playlist/1gGbG1LYP4dOdXHh0XXybP?si=a3c8bc82a45a40bf",
"https://open.spotify.com/playlist/19jt2QYR2EEiJCjsbrA7QD?si=fa1adf1520324dc9",
"https://open.spotify.com/playlist/1LdNIlSZgQPTwM9nGA1Oaf?si=487d951f480d4ddc",
"https://open.spotify.com/playlist/6SP4zGb7hO13Wi4O0OrX7f?si=318ca7bf1c9c4973",
"https://open.spotify.com/playlist/5ELy02oN5DweLRFLx64nJc?si=a09513e584eb4685",
"https://open.spotify.com/playlist/71pk02pQkKzww443kUf21h?si=dc3c1803a3f24827",
"https://open.spotify.com/playlist/1T8oQMP9iCSGwbbQvg3Rab?si=b8b263e1f2964319"]

def sync(playlists):
    sg.Popup('Sync Started', keep_on_top=True)
    for value in playlist_urls:
        subprocess.Popen('spotify_dl -l '+value+ " -o", shell=True)

#for value in playlist_urls:
#    subprocess.Popen('spotify_dl -l '+value)

# Define the window's contents
layout = [[sg.Text("Playlists to synchronize")],
          #[sg.Multiline(playlist_urls,key='playlists',size=(100, 20))],
          [sg.Listbox(values=playlist_urls,size=(80,10),key="listbox")],
          [sg.Input(key="input")],
          [sg.Button("Add"),sg.Button("Remove")],
          [sg.Button('Sync'), sg.Button('Quit')]]


# Create the window
window = sg.Window('Spotify Sync', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()

    if event == "Add":
        playlist_urls.append(values["input"])
        window["input"].value = ""
        window["listbox"].update(playlist_urls)


    if event == "Remove":
        selection = window.Element('listbox').Widget.curselection()[0]
        del playlist_urls[selection]
        window["listbox"].update(playlist_urls)

    if event == "Sync":
        sync(playlist_urls)

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

# Finish up by removing from the screen
window.close()


if __name__ == "__main__":
    main()
