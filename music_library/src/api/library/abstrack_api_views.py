from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class AbstractLikeView(APIView):
    like_type = None
    permission_classes = [IsAuthenticated]

    def set_like(self, user, obj, relationship_model):
        like_instance, created = relationship_model.objects.get_or_create(user=user, **{self.like_type: obj})

        if created:
            message = self.create_message(operation='added')
            status_code = status.HTTP_201_CREATED
        else:
            like_instance.delete()
            message = self.create_message(operation='deleted')
            status_code = status.HTTP_200_OK

        return Response({'message': message}, status=status_code)

    def create_message(self, operation):
        message = f'Like {operation} for {self.like_type}'
        return message
