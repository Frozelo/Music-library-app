from django.db.models import Count, Prefetch
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from core.caching import CacheMixin
from .abstrack_api_views import AbstractLikeView
from .serializers import DetailAlbumSerializer, ArtistSerializer, TrackSerializer
from ...music_app.models import Album, Artist, Track, AlbumUserRelationship, TrackUserRelationship, \
    ArtistUserRelationship


class AlbumListView(CacheMixin, ReadOnlyModelViewSet):
    queryset = Album.objects.select_related('artist').prefetch_related('tracks__artist').annotate(
        total_likes=Count('user'))
    serializer_class = DetailAlbumSerializer
    cache_prefix_key = 'album_view_cache_key'

    def get_queryset(self):
        return self.queryset.order_by('-release_year')


class TrackListView(CacheMixin, ReadOnlyModelViewSet):
    queryset = (Track.objects.prefetch_related('artist').
                annotate(total_likes=Count('user')).
                defer('album'))
    serializer_class = TrackSerializer
    cache_prefix_key = 'track_view_cache_key'


class ArtistListView(CacheMixin, ReadOnlyModelViewSet):
    queryset = Artist.objects.select_related('genre').prefetch_related('albums')
    serializer_class = ArtistSerializer
    cache_prefix_key = 'artist_view_cache_key'


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
