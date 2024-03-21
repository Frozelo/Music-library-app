from rest_framework import serializers

from src.api.library.serializers import TrackSerializer, TrackLikesSerializer
from src.user.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    liked_tracks = TrackLikesSerializer(many=True, source='trackuserrelationship_set')
    liked_albums = Al

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'liked_tracks']
