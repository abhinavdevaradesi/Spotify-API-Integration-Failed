# auth.py
from spotipy.oauth2 import SpotifyOAuth
import spotipy

CLIENT_ID = 'e249fb899da44ff6b8dc447821e3268f'
CLIENT_SECRET = '1ad82882e6c540448e0e2af55c5cb346'
REDIRECT_URI = 'http://127.0.0.1:8888/callback'
SCOPE = 'user-top-read user-library-read'

def get_spotify_client():
    auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
	cache_path='.cache'
    )
    return spotipy.Spotify(auth_manager=auth_manager)
