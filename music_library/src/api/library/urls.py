from django.urls import path
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from .views import ArtistListView, AlbumListView, TrackListView, AlbumLikeView, TrackLikeView

urlpatterns = [
    path('albums/<int:id>/like/', AlbumLikeView.as_view(), name='album-like'),
    path('tracks/<int:id>/like/', TrackLikeView.as_view(), name='track-like'),

]

