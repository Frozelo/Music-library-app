from core.services import all_objects
from src.music_app.models import Artist, Album, Genre


def get_artist_list():
    return all_objects(obj=Artist.objects, select_related=('genre',))


def get_album_list():
    return all_objects(obj=Album.objects, select_related=('artist',))


def get_genre_list():
    return all_objects(obj=Genre.objects, only=('id', 'name'))
