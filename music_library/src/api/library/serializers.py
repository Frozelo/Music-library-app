from rest_framework import serializers

from core.services import filter_objects
from src.api.library.core_serializers import SimpleAlbumSerializer
from src.music_app.models import Album, Track, Artist, Genre, AlbumUserRelationship, TrackUserRelationship


class TrackSerializer(serializers.ModelSerializer):
    """"A serializer for tracks"""
    artist = serializers.StringRelatedField(many=True)
    total_likes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Track
        fields = ['id', 'title', 'duration', 'artist', 'audio_file', 'cover_image', 'total_likes', ]


class TrackLikesSerializer(serializers.ModelSerializer):
    """"A serializer for track likes"""
    user = serializers.StringRelatedField()

    class Meta:
        model = TrackUserRelationship
        fields = ['id', 'user', 'created_at']


class DetailAlbumSerializer(SimpleAlbumSerializer):
    """"A serializer for detail album view (artist, tracks)"""
    artist = serializers.StringRelatedField()
    tracks = TrackSerializer(many=True)
    total_likes = serializers.IntegerField(read_only=True)

    class Meta(SimpleAlbumSerializer.Meta):
        model = Album
        fields = SimpleAlbumSerializer.Meta.fields + ['artist', 'tracks', 'total_likes']


class GenreSerializer(serializers.ModelSerializer):
    """"A seriazlizer for genres"""
    class Meta:
        model = Genre
        fields = ('id', 'name')


class ArtistSerializer(serializers.ModelSerializer):
    """a serializer for artists"""
    genre = GenreSerializer()
    albums = SimpleAlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'country', 'avatar_image', 'genre', 'albums']

    def to_representation(self, instance):
        """"Sorting the given instance by release year"""
        representation = super(ArtistSerializer, self).to_representation(instance)
        representation['albums'] = SimpleAlbumSerializer(instance.albums.order_by('-release_year'), many=True).data
        return representation
