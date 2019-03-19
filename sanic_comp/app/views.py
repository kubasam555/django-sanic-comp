from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from app.models import Post
from app.serializers import CreatePostSerializer
from app.serializers import ReadPostSerializer
from app.serializers import RegistrationSerializer

User = get_user_model()


class PostViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = ReadPostSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreatePostSerializer
        return super().get_serializer_class()


class UserRegister(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny, )

    def create(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            new_user = User.objects.create_user(
                username=serializer.validated_data['username'], password=serializer.validated_data['password']
            )
            return Response({'token': new_user.auth_token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
