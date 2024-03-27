from django.http import HttpResponse
from django.shortcuts import render

from src.music_app.models import Track, Album, Artist
from core.services import all_objects
from src.music_app.services.album_filtres import apply_filters
from src.music_app.services.core_service import get_artist_list, get_album_list, get_genre_list
from src.scripts.itunes_api_script import fetch_artist_info_from_last_fm, save_artist_to_db


def album_list_view(request):
    """Отображает список альбомов с учетом фильтров и сортировки."""
    artists = get_artist_list()
    albums = get_album_list()

    if request.method == 'GET':
        albums = apply_filters(request, albums)

    return render(request, 'album_list.html', {'albums': albums, 'artists': artists})
