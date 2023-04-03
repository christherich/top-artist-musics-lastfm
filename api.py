import asyncio
import requests
import tkinter as tk


# Last.fm API credentials
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# Function to fetch and display top tracks of an artist (async version)


async def get_top_tracks(artist):
    try:
        # Build URL for Last.fm API call
        url = f'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist}&api_key=28f316540a6ad3a8c0dc5aeaf181c30d&format=json'

        # Make API call
        response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)

        # Raise exception if API call failed
        response.raise_for_status()

        # Parse response JSON
        tracks = response.json()['toptracks']['track']

        # Display top tracks in results box
        return [f'- {track["name"]} ({track["playcount"]} plays)' for track in tracks]
    except (requests.RequestException, KeyError):
        # Display error message if API call failed
        return ['Error: Failed to fetch top tracks. Please try again.']

# Function to fetch and display top tracks of an artist (asynchronous wrapper)


def get_top_tracks_async(artist, results_box, error_label, search_button):
    # Disable search button and clear error message
    # search_button.config(state=tk.DISABLED)
    error_label.config(text='')

    # Fetch top tracks asynchronously
    asyncio.run(get_top_tracks_async_helper(
        artist, results_box, error_label, search_button))


async def get_top_tracks_async_helper(artist, results_box, error_label, search_button):
    try:
        tracks = await get_top_tracks(artist)
    except:
        tracks = ['Error: Failed to fetch top tracks. Please try again.']

    # Display results or error message
    results_box.config(state=tk.NORMAL)
    results_box.delete('1.0', tk.END)
    for track in tracks:
        results_box.insert(tk.END, f'{track}\n')
    results_box.config(state=tk.DISABLED)

    if 'Error' in tracks[0]:
        error_label.config(text=tracks[0])
