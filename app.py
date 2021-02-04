import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_KEY')
CLIENT_SECRET = os.getenv('SPOTIFY_KEY')

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST requesting client credential auth token
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()
# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': f'Bearer {access_token}'
}

BASE_URL = "https://api.spotify.com/v1/browse/new-releases"

r = requests.get(BASE_URL, headers=headers)
for i in range(10):
    print(r.json()['albums']['items'][i]['name'])