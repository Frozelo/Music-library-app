from rest_framework import serializers

from src.music_app.models import Album


class SimpleAlbumSerializer(serializers.ModelSerializer):
    """"A simple serializer for albums"""
    class Meta:
        model = Album
        fields = ['id', 'title', 'release_year', 'artist', 'biography', 'cover_image']
