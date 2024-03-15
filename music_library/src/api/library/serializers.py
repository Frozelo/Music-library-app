from rest_framework import serializers

from core.services import filter_objects
from src.music_app.models import Album, Track


# TODO Think about optimized serializer
class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()
    tracks = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ['id', 'title', 'release_year', 'artist', 'biography', 'cover_image', 'tracks']

    def get_tracks(self, instance):
        tracks = filter_objects(obj=Track.objects.filter(album=instance), album=instance, prefetch_related=('artist',))
        return TrackSerializer(tracks, many=True).data


class TrackSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField(many=True)

    class Meta:
        model = Track
        fields = ['id', 'title', 'duration', 'artist', 'audio_file', 'cover_image']
