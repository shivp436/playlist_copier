from django.http import HttpResponseRedirect, JsonResponse
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from requests import request, get, post
import os
import urllib.parse
from datetime import datetime


load_dotenv()
spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
spotify_redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')
spotify_scopes = os.getenv('SPOTIFY_SCOPES')


AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1'


def get_spotify_playlists(request):
    print(request.session)
    if 'spotify_access_token' not in request.session:
        print('No access token')
        print(login_spotify())
    
    playlist_info = []
    
    return playlist_info

def login_spotify():
    params = {
        'client_id': spotify_client_id,
        'response_type': 'code',
        'redirect_uri': spotify_redirect_uri,
        'scope': spotify_scopes,
        'show_dialog': True
    }
    print(params)
    
    auth_url = f'{AUTH_URL}?{urllib.parse.urlencode(params)}'
    return HttpResponseRedirect(auth_url)

def callback_spotify(request):
    if 'error' in request.GET:
        return JsonResponse({'error': request.GET['error']})

    if 'code' in request.GET:
        code = request.args['code']
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': spotify_redirect_uri,
            'client_id': spotify_client_id,
            'client_secret': spotify_client_secret
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = post(TOKEN_URL, data=data, headers=headers)
        token_info = response.json()

        # Save the token information to the session
        request.session['spotify_access_token'] = token_info['access_token']
        request.session['spotify_refresh_token'] = token_info['refresh_token']
        request.session['spotify_token_expires_at'] = datetime.now().timestamp() + token_info['expires_in']

        return JsonResponse({'success': True, 'message': 'Authentication successful'})