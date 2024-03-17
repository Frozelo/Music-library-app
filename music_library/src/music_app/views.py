from django.http import HttpResponse
from django.shortcuts import render

from src.music_app.models import Track, Album, Artist
from core.services import all_objects
from src.music_app.services.album_filtres import apply_filters
from src.music_app.services.core_service import get_artist_list, get_album_list, get_genre_list


def artist_list_view(request):
    """Отображает список артистов с учетом фильтров и сортировки."""
    artists = get_artist_list()
    genres = get_genre_list()

    if request.method == 'GET':
        artists = apply_filters(request, artists)

    return render(request, 'artist_list.html', {'artists': artists, 'genres': genres})


def album_list_view(request):
    """Отображает список альбомов с учетом фильтров и сортировки."""
    artists = get_artist_list()
    albums = get_album_list()

    if request.method == 'GET':
        albums = apply_filters(request, albums)

    return render(request, 'album_list.html', {'albums': albums, 'artists': artists})
