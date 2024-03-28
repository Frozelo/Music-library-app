from django.contrib.auth import get_user_model
from rest_framework import serializers

from src.api.library.serializers import TrackSerializer, TrackLikesSerializer, AbstractLikeSerializer, \
    ArtistLikesSerializer
from src.user.models import CustomUser
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    liked_tracks = TrackLikesSerializer(many=True, source='track_user_relation')
    liked_artists = ArtistLikesSerializer(many=True, source='artist_user_relation')

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'liked_artists', 'liked_tracks']


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(label=_("Confirm password"), write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'password2', 'bio', 'date_of_birth']

    def validate_email(self, value):
        if UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("A user with that email already exists."))
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs.pop('password2'):
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return attrs

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio'),
            date_of_birth=validated_data.get('date_of_birth')
        )
        return user
