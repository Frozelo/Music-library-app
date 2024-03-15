from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.services import all_objects
from .serializers import AlbumSerializer, ArtistSerializer
from ...music_app.models import Album, Artist


class ArtistView(ListAPIView):
    queryset = Artist.objects.all().select_related('genre')
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', 'genre']


class AlbumDetailView(APIView):
    def get(self, request, album_id):
        try:
            album = Album.objects.select_related('artist').get(id=album_id)
            serializer = AlbumSerializer(album)
            return Response(serializer.data)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
