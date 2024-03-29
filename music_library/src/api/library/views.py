from django.db.models import Count, Prefetch
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from core.obj_services import all_objects
from core.request_services import get_params_from_kwargs
from .abstrack_api_views import AbstractLikeView
from .serializers import DetailAlbumSerializer, ArtistSerializer, TrackSerializer
from ...music_app.models import Album, Artist, Track, AlbumUserRelationship, TrackUserRelationship, \
    ArtistUserRelationship


class AlbumListView(ReadOnlyModelViewSet):
    queryset = (Album.objects.select_related('artist').prefetch_related('tracks__artist').
                annotate(total_likes=Count('user')))
    serializer_class = DetailAlbumSerializer

    def get_queryset(self):
        """
        Возвращает отсортированный по дате выхода (самые новые сначала) список альбомов.
        """
        return self.queryset.order_by('release_year')


class TrackListView(ReadOnlyModelViewSet):
    queryset = (Track.objects.prefetch_related('artist').
                annotate(total_likes=Count('user')).
                defer('album'))
    serializer_class = TrackSerializer


class ArtistListView(ReadOnlyModelViewSet):
    queryset = Artist.objects.select_related('genre').prefetch_related('albums')
    serializer_class = ArtistSerializer


class AlbumLikeView(AbstractLikeView):
    model = Album
    relationship_model = AlbumUserRelationship
    like_type = 'album'


class TrackLikeView(AbstractLikeView):
    model = Track
    relationship_model = TrackUserRelationship
    like_type = 'track'


class ArtistLikeView(AbstractLikeView):
    model = Artist
    relationship_model = ArtistUserRelationship
    like_type = 'artist'
