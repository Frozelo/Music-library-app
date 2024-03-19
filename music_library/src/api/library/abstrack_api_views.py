from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class AbstractLikeView(APIView):
    def set_like(self, user, obj, relationship_model):
        print('hey!')
        like_instance, created = relationship_model.objects.get_or_create(user=user, **{self.like_type: obj})

        if created:
            message = f'Like added for {self.like_type}'
            status_code = status.HTTP_201_CREATED
        else:
            like_instance.delete()
            message = f'Like removed for {self.like_type}'
            status_code = status.HTTP_200_OK

        return Response({'message': message}, status=status_code)