from rest_framework import serializers

from src.music_app.models import Album


class AbstractLikeSerializer(serializers.ModelSerializer):
    """
    An abstract serializer for all like serializers
    I can set right here the abstract attribute True
    """

    class Meta:
        abstract = True
        fields = ['id', 'created_at']


class SimpleAlbumSerializer(serializers.ModelSerializer):
    """"A simple serializer for albums"""

    class Meta:
        model = Album
        fields = ['id', 'title', 'release_year', 'artist', 'biography', 'cover_image']
