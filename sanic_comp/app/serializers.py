from rest_framework import serializers

from app.models import Post
from app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'date_joined')


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer class used for serializing and validating User registration input.
    """

    class Meta:
        model = User
        fields = ('username', 'password')


class ReadPostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'content')


class CreatePostSerializer(ReadPostSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta(ReadPostSerializer.Meta):
        pass