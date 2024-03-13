from django.urls import path
from .views import AlbumDetailView

urlpatterns = [
    path('albums/<int:album_id>/', AlbumDetailView.as_view(), name='album_detail'),
]