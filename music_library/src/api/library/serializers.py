from rest_framework import serializers

from core.services import filter_objects
from src.music_app.models import Album, Track, Artist, Genre, AlbumUserRelationship, TrackUserRelationship


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class ArtistSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Artist
        fields = ['id', 'name', 'country', 'avatar_image', 'genre', ]


class TrackLikesSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = TrackUserRelationship
        fields = ['id', 'user', 'created_at']


class TrackSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField(many=True)
    total_likes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Track
        fields = ['id', 'title', 'duration', 'artist', 'audio_file', 'cover_image', 'total_likes', ]


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()
    tracks = TrackSerializer(many=True)
    total_likes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'release_year', 'artist', 'biography', 'cover_image', 'tracks',
                  'total_likes']
