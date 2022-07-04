import requests
from bs4 import BeautifulSoup
import pdb
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify_key = os.environ.get("spotify_key")
spotify_id = os.environ.get("spotify_id")
spotify_user = os.environ.get("spotify_user")
g = spotipy.oauth2.SpotifyOAuth(
    client_id=spotify_id, client_secret=spotify_key, redirect_uri="http://example.com"
)
