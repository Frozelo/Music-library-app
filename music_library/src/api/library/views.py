from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.services import all_objects
from .serializers import AlbumSerializer, ArtistSerializer, TrackSerializer
from ...music_app.models import Album, Artist, Track


class ArtistDetailView(APIView):
    def get(self, request, artist_id):
        try:
            artist = Artist.objects.select_related('genre').get(id=artist_id)
            serializer = ArtistSerializer(artist)
            return Response(serializer.data)
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AlbumDetailView(APIView):
    def get(self, request, album_id):
        try:
            album = Album.objects.select_related('artist').get(id=album_id)
            serializer = AlbumSerializer(album)
            return Response(serializer.data)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TrackDetailView(APIView):
    def get(self, request, track_id):
        try:
            track = Track.objects.select_related('album').get(id=track_id)
            serializer = TrackSerializer(track)
            return Response(serializer.data)
        except Track.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
