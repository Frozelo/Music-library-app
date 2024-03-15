from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlbumSerializer
from ...music_app.models import Album

from core.services import get_objects, all_objects


class AlbumDetailView(APIView):
    def get(self, request, album_id):
        try:
            album = Album.objects.select_related('artist').get(id=album_id)
            serializer = AlbumSerializer(album)
            return Response(serializer.data)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
