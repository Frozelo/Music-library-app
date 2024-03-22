import os
from urllib.parse import quote

import requests
from dotenv import load_dotenv
from django.shortcuts import redirect
from src.music_app.models import Genre, Artist, Album

load_dotenv()

LAST_FM_API_KEY = os.getenv('LAST_FM_API_KEY')


def last_fm_request(params: dict):
    base_url = 'http://ws.audioscrobbler.com/2.0/'
    params['api_key'] = LAST_FM_API_KEY
    params['format'] = 'json'
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()


def fetch_artist_info_from_last_fm(artist_name: str):
    params = {
        'method': 'artist.getinfo',
        'artist': artist_name,
    }
    return last_fm_request(params)


def save_artist_to_db(response_data):
    artist_info = response_data.get('artist')

    genre_name = artist_info['tags']['tag'][0]['name'] if artist_info['tags']['tag'] else 'Unknown'
    genre, _ = Genre.objects.get_or_create(name=genre_name)

    artist, created = Artist.objects.get_or_create(
        name=artist_info['name'],
        defaults={
            'biography': artist_info['bio']['content'],
            'avatar_image': artist_info['image'][3]['#text'],
            'country': 'N/A',
            'genre': genre
        }
    )


def save_album_to_db(response_data):
    album_info = response_data.get('album')
    if album_info:
        artist, _ = Artist.objects.get_or_create(name=album_info['artist'])

        album, created = Album.objects.get_or_create(
            title=album_info['name'],
            artist=artist,
            defaults={
                'cover_image': album_info['image'][-1]['#text'] if album_info['image'] else None,
                'biography': album_info['wiki']['content'],
            }
        )


def fetch_album_info_from_last_fm(artist_name: str, album_name: str):
    params = {
        'method': 'album.getinfo',
        'artist': artist_name,
        'album': album_name,
    }
    return last_fm_request(params)
