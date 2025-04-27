from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# --------------- FUNCTIONS ---------------------------------------------
def create_playlist(user_id, playlist_name):
    playlist = sp.user_playlist_create(user_id, playlist_name)
    print(f"New playlist: {playlist['name']}")
    return playlist['id']


def search_song(query):
    results = sp.search(query, limit=1, type='track')
    tracks = results['tracks']['items']
    if tracks:
        return tracks[0]['uri']
    else:
        print(f'Not found: {tracks}')
        return None

# --------------- GET A LIST OF TOP 100 SONGS ---------------------------------------------
date = input('Type the date in the format: YYYY-MM-DD: ')


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/", headers=header)
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

# --------------- AUTH SPOTIFY ---------------------------------------------
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-public playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USER_NAME,
    )
)

user_id = sp.current_user()['id']

# --------------- CREATE A PLAYLIST - SPOTIFY --------------------------------------------
playlist_name = date
playlist_id = create_playlist(user_id, playlist_name)

song_uris = []

for query in song_names:
    song_uri = search_song(query)
    if song_uri:
        song_uris.append(song_uri)

if song_uris:
    sp.playlist_add_items(playlist_id, song_uris)
else:
    print("Not fond any song")

