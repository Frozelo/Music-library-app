from django.urls import path
from . import views

urlpatterns = [
    path('artist/search/', views.artist_search_view, name='artist_search'),
    path('save_albums/<int:artist_id>/', views.save_artist_albums_view, name='save_artist_albums'),
]
