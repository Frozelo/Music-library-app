from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from src.api.user.serializers import UserSerializer, CreateUserSerializer
from src.user.models import CustomUser


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.prefetch_related(
        'track_user_relation',
        'artist_user_relation')
    serializer_class = UserSerializer


class CreateUserView(CreateAPIView):
    model = CustomUser
    permission_classes = []
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()
