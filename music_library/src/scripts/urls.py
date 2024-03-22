from django.urls import path
from . import views

urlpatterns = [
    path('artist-search/', views.ArtistSearchView.as_view(), name='artist_search'),
    path('search-album/', views.AlbumSearchView.as_view(), name='save_album'),
]
