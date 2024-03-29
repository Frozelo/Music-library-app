from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from src.music_app.models import Artist
from src.music_app.services.album_filtres import apply_filters
from src.music_app.services.core_service import get_artist_list, get_genre_list


def artist_list_view(request):
    """Отображает список артистов с учетом фильтров и сортировки."""
    artists = get_artist_list()
    genres = get_genre_list()

    if request.method == 'GET':
        artists = apply_filters(request, artists)

    return render(request, 'artist_list.html', {'artists': artists, 'genres': genres})


def detail_artist_view(request, artist_id):
    return render(request, 'artist_detail.html', {'artist_id': artist_id})
