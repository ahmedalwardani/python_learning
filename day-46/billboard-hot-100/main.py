import os

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt",
        username="Ahmed Alwardani"
    )
)

user_id = sp.current_user()["id"]

date_to_travel_to = input("Which date do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"{BILLBOARD_BASE_URL}/{date_to_travel_to}")
response.raise_for_status()

soup = BeautifulSoup(response.text, features="html.parser")

all_songs = soup.select("li ul li h3")
all_song_names = [song.getText().strip() for song in all_songs]

song_uris = []
year = date_to_travel_to.split("-")[0]

for song_name in all_song_names:
    result = sp.search(q=f"track:{song_name} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song_name} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date_to_travel_to} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)