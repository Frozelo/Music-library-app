from django.urls import path
from rest_framework import routers
from .views import AlbumDetailView, ArtistView



urlpatterns = [
    path('artists/', ArtistView.as_view(), name='artist_list'),
    path('albums/<int:album_id>/', AlbumDetailView.as_view(), name='album_detail'),
]



