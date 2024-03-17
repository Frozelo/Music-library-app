from rest_framework import serializers

from core.services import filter_objects
from src.music_app.models import Album, Track, Artist, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class ArtistSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    albums = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ['id', 'name', 'country', 'artist_image', 'genre', 'albums']

    def get_albums(self, instance):
        albums = filter_objects(obj=Album.objects.filter(artist=instance),
                                artist=instance,
                                select_related=('artist',))
        return AlbumSerializer(albums, many=True).data


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()
    tracks = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ['id', 'title', 'release_year', 'artist', 'biography', 'cover_image', 'tracks']

    def get_tracks(self, instance):
        tracks = filter_objects(obj=Track.objects.filter(album=instance),
                                album=instance,
                                select_related=('album',))
        return TrackSerializer(tracks, many=True).data


class TrackSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField(many=True)

    class Meta:
        model = Track
        fields = ['id', 'title', 'duration', 'artist', 'audio_file', 'cover_image']
