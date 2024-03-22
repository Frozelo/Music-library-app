import os
from urllib.parse import quote

import requests
from dotenv import load_dotenv
from django.shortcuts import redirect
from src.music_app.models import Genre, Artist, Album, Track

load_dotenv()

LAST_FM_API_KEY = os.getenv('LAST_FM_API_KEY')


def last_fm_request(api_method: str, **kwargs):
    base_url = 'http://ws.audioscrobbler.com/2.0/'
    params = {
        'method': api_method,
        'api_key': LAST_FM_API_KEY,
        'format': 'json',
        **kwargs
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()


def fetch_artist_info_from_last_fm(artist_name: str):
    try:
        return last_fm_request('artist.getinfo', artist=artist_name)
    except requests.HTTPError as e:
        raise


def fetch_album_info_from_last_fm(artist_name: str, album_name: str):
    try:
        return last_fm_request('album.getinfo', artist=artist_name, album=album_name)
    except requests.HTTPError as e:
        raise


def save_artist_to_db(response_data):
    artist_info = response_data.get('artist')

    if artist_info:
        genre_name = artist_info['tags']['tag'][0]['name'] if artist_info['tags']['tag'] else 'Unknown'
        genre, _ = Genre.objects.get_or_create(name=genre_name)

        image_url = artist_info['image'][3]['#text'] if len(artist_info['image']) > 3 else None
        artist, created = Artist.objects.get_or_create(
            name=artist_info['name'],
            defaults={
                'biography': artist_info.get('bio', {}).get('content', ''),
                'avatar_image': image_url,
                'country': 'N/A',
                'genre': genre
            }
        )


def save_album_to_db(response_data):
    album_info = response_data.get('album')
    if album_info:
        artist_name = album_info['artist']
        artist, _ = Artist.objects.get_or_create(name=artist_name)

        cover_image_url = album_info['image'][-1]['#text'] if album_info['image'] else None
        biography = album_info.get('wiki', {}).get('content', '') if 'wiki' in album_info else ''

        album, _ = Album.objects.get_or_create(
            title=album_info['name'],
            artist=artist,
            defaults={
                'cover_image': cover_image_url,
                'biography': biography,
            }
        )

        if 'tracks' in album_info and 'track' in album_info['tracks']:
            for track_info in album_info['tracks']['track']:
                if 'name' in track_info:
                    track, track_created = Track.objects.get_or_create(
                        title=track_info['name'],
                    )
                    track.artist.add(artist)
                    album.tracks.add(track)
        album.save()
