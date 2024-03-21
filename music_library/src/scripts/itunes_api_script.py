import requests
from django.shortcuts import redirect

from src.music_app.models import Genre, Artist, Album


def fetch_artist_info(artist_name):
    base_url = "https://itunes.apple.com/search"
    params = {
        "term": artist_name,
        "entity": "musicArtist",
        "limit": 1
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        if data['resultCount'] > 0:
            return data['results'][0]
        else:
            return None
    except requests.RequestException as e:
        print(f"Error fetching artist info: {e}")
        return None


def save_artist(artist_info):
    if artist_info:
        artist_itunes_id = artist_info['artistId']
        genre_name = artist_info.get('primaryGenreName', 'N/A')
        genre, _ = Genre.objects.get_or_create(name=genre_name)

        artist, created = Artist.objects.get_or_create(
            name=artist_info['artistName'],
            defaults={
                'genre': genre,
                'itunes_id': artist_itunes_id
            }
        )
        return artist_itunes_id if created else None
    else:
        return None


def fetch_and_save_artist_info(artist_name):
    """Функция для получения информации об артисте и его сохранения."""
    artist_info = fetch_artist_info(artist_name)
    artist_id = save_artist(artist_info)
    return artist_id


def get_albums_list(artist_id):
    if artist_id:
        base_url = f"https://itunes.apple.com/lookup?id={artist_id}&entity=album"
        try:
            response = requests.get(base_url)
            response.raise_for_status()
            data = response.json()
            if data['resultCount'] > 0:
                return data['results']
            else:
                return None
        except requests.RequestException as e:
            print(f"Error fetching albums list: {e}")
            return None
    else:
        return None


def save_artist_albums(artist_id):
    try:
        artist = Artist.objects.filter(itunes_id=artist_id).first()
        albums_data = get_albums_list(artist_id)

        if albums_data:
            print(albums_data)
            for album_index in range(1, len(albums_data)):
                if int(albums_data[album_index]['trackCount']) > 5:
                    album, created = Album.objects.get_or_create(
                        title=albums_data[album_index]['collectionName'],
                        release_year=int(albums_data[album_index]['releaseDate'][:4]),
                        artist=artist,
                    )
            return redirect('artist_details', artist_id=artist_id)
        else:
            return redirect('artist_list')
    except Artist.DoesNotExist:

        return redirect('artist_list')
    except Exception as e:
        print(f"Error saving artist albums: {e}")
        return redirect('artist_list')
