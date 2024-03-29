from django.db.models import Model
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from src.user.models import CustomUser


class AbstractLikeView(APIView):
    model = None
    relationship_model = None
    like_type = None
    permission_classes = [IsAuthenticated]

    def post(self, request: HttpRequest, *args, **kwargs):
        user = request.user
        object_id = kwargs.get('id')
        obj = get_object_or_404(self.model, pk=object_id)
        return self.set_like(user, obj)

    def set_like(self, user: CustomUser, obj: Model):
        like_instance, created = self.relationship_model.objects.get_or_create(
            user=user,
            **{self.like_type: obj}
        )

        if created:
            message = f'Like added to {self.like_type}'
            status_code = status.HTTP_201_CREATED
        else:
            like_instance.delete()
            message = f'Like removed from {self.like_type}'
            status_code = status.HTTP_200_OK

        return Response({'message': message}, status=status_code)
