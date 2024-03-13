from django.http import HttpResponse
from django.shortcuts import render

from src.music_app.models import Track, Album, Artist
from core.services import all_objects
from src.music_app.services.album_filtres import apply_filters


def artist_list():
    return all_objects(obj=Artist.objects, select_related=('genre',))

def album_list(request):
    """Отображает список альбомов с учетом фильтров и сортировки."""
    artists = artist_list()
    albums = Album.objects.all()

    if request.method == 'GET':
        albums = apply_filters(request, albums)

    return render(request, 'album_list.html', {'albums': albums, 'artists': artists})
