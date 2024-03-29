from rest_framework import serializers

from core.obj_services import filter_objects
from src.api.library.core_serializers import SimpleAlbumSerializer, AbstractLikeSerializer
from src.music_app.models import Album, Track, Artist, Genre, AlbumUserRelationship, TrackUserRelationship, \
    ArtistUserRelationship


class TrackSerializer(serializers.ModelSerializer):
    """"A serializer for tracks"""
    artist = serializers.StringRelatedField(many=True)
    total_likes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Track
        fields = ['id', 'title', 'duration', 'artist', 'audio_file', 'cover_image', 'total_likes', ]


class TrackLikesSerializer(AbstractLikeSerializer):
    """"A serializer for track likes"""

    class Meta(AbstractLikeSerializer.Meta):
        model = TrackUserRelationship
        fields = AbstractLikeSerializer.Meta.fields


class ArtistLikesSerializer(AbstractLikeSerializer):
    class Meta(AbstractLikeSerializer.Meta):
        model = ArtistUserRelationship
        fields = AbstractLikeSerializer.Meta.fields


class DetailAlbumSerializer(SimpleAlbumSerializer):
    """"A serializer for detail album view (artist, tracks)"""

    artist = serializers.StringRelatedField()
    tracks = TrackSerializer(many=True)
    total_likes = serializers.IntegerField(read_only=True)

    class Meta(SimpleAlbumSerializer.Meta):
        model = Album
        fields = SimpleAlbumSerializer.Meta.fields + ['artist', 'tracks', 'total_likes']


class GenreSerializer(serializers.ModelSerializer):
    """"A serializer for genres"""

    class Meta:
        model = Genre
        fields = ('id', 'name')


class ArtistSerializer(serializers.ModelSerializer):
    """A serializer for artists"""
    genre = GenreSerializer()
    albums = SimpleAlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'country', 'avatar_image', 'genre', 'albums']

    def to_representation(self, instance):
        """Sorting albums by release date within the representation"""
        representation = super(ArtistSerializer, self).to_representation(instance)

        # Sorting albums by release year within the representation
        sorted_albums = sorted(representation['albums'],
                               key=lambda album: album['release_year'] if album['release_year'] else 0, reverse=True)
        representation['albums'] = sorted_albums
        return representation
