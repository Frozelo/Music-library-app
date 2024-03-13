from django.urls import path

from src.music_app import views

urlpatterns = [
    path('', views.album_list)
]