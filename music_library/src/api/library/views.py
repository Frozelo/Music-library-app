from django.db.models import Count
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from core.services import all_objects
from .abstrack_api_views import AbstractLikeView
from .serializers import AlbumSerializer, ArtistSerializer, TrackSerializer
from ...music_app.models import Album, Artist, Track, AlbumUserRelationship, TrackUserRelationship


class AlbumListView(ReadOnlyModelViewSet):
    queryset = (Album.objects.select_related('artist').prefetch_related('tracks__artist').
                annotate(total_likes=Count('user')))
    serializer_class = AlbumSerializer


class TrackListView(ReadOnlyModelViewSet):
    queryset = (Track.objects.prefetch_related('artist').
                annotate(total_likes=Count('user')).
                defer('album'))
    serializer_class = TrackSerializer


class ArtistListView(ReadOnlyModelViewSet):
    queryset = Artist.objects.select_related('genre')
    serializer_class = ArtistSerializer


class AlbumLikeView(AbstractLikeView):
    like_type = 'album'

    def post(self, request, *args, **kwargs):
        user = request.user
        object_id = kwargs.get('id')
        album = Album.objects.get(pk=object_id)
        return self.set_like(user, album, AlbumUserRelationship)


class TrackLikeView(AbstractLikeView):
    like_type = 'track'

    def post(self, request, *args, **kwargs):
        user = request.user
        object_id = kwargs.get('id')
        track = Track.objects.get(pk=object_id)
        return self.set_like(user, track, TrackUserRelationship)
