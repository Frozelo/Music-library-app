from django.urls import path, include
from rest_framework.routers import SimpleRouter

from src.api.library.views import ArtistListView, AlbumListView, TrackListView
from src.api.user.views import UserViewSet

router = SimpleRouter()

router.register(r'users', UserViewSet)
router.register(r'artists', ArtistListView)
router.register(r'albums', AlbumListView)
router.register(r'tracks', TrackListView)

urlpatterns = [
    path('', include('src.api.library.urls')),
    path('', include('src.api.user.urls')),
]

urlpatterns += router.urls
