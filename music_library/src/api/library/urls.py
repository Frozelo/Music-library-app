from django.urls import path
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from .views import ArtistListView, AlbumListView, TrackListView, AlbumLikeView, TrackLikeView

router = SimpleRouter()

router.register(r'artists', ArtistListView)
router.register(r'albums', AlbumListView)
router.register(r'tracks', TrackListView)
urlpatterns = [
    path('albums/<int:id>/like/', AlbumLikeView.as_view(), name='album-like'),
    path('tracks/<int:id>/like/', TrackLikeView.as_view(), name='track-like'),

]

urlpatterns += router.urls
