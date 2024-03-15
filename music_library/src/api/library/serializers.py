from rest_framework import serializers

from core.services import filter_objects
from src.music_app.models import Album, Track, Artist, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class ArtistSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Artist
        fields = ['id', 'name', 'country', 'avatar', 'genre']



class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()
    tracks = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ['id', 'title', 'release_year', 'artist', 'biography', 'cover_image', 'tracks']

    def get_tracks(self, instance):
        tracks = filter_objects(obj=Track.objects.filter(album=instance),
                                album=instance,
                                prefetch_related=('artist',))
        return TrackSerializer(tracks, many=True).data


class TrackSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField(many=True)

    class Meta:
        model = Track
        fields = ['id', 'title', 'duration', 'artist', 'audio_file', 'cover_image']
