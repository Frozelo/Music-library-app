from django.http import HttpResponse
from django.shortcuts import render

from src.music_app.models import Track, Album
from core.services import all_objects


def album_list(request):
    albums = all_objects(obj=Album.objects, select_related=('artist',))
    return render(request, 'album_list.html', {'albums': albums})
