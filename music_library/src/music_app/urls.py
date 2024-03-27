from django.urls import path

from src.music_app.views import artists_views, albums_views

urlpatterns = [
    path('artists/', artists_views.artist_list_view, name='artist_list'),
    path('artists/<int:artist_id>', artists_views.detail_artist_view, name='detail_artist_view'),
    path('', albums_views.album_list_view, name='album_list'),
]