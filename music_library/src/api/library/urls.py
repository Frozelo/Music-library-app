from django.urls import path
from rest_framework import routers
from .views import AlbumDetailView, ArtistDetailView, TrackDetailView



urlpatterns = [
    path('artists/<int:artist_id>', ArtistDetailView.as_view(), name='artist_list'),
    path('albums/<int:album_id>/', AlbumDetailView.as_view(), name='album_detail'),
    path('track/<int:track_id>', TrackDetailView.as_view(), name='track_detail'),
]



