from rest_framework.viewsets import ModelViewSet

from src.api.user.serializers import UserSerializer
from src.user.models import CustomUser


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.only('username', 'first_name', 'last_name', 'bio')
    serializer_class = UserSerializer
