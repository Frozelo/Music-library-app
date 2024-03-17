from django.urls import path

from src.music_app import views

urlpatterns = [
    path('artists/', views.artist_list_view),
    path('', views.album_list_view)
]