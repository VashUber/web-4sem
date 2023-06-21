from rest_framework import serializers
from users.models import MyUser

from .models import Article


class UserViewSerializer(serializers.Serializer):
    username = serializers.CharField(source="author.username")
    id = serializers.IntegerField(source="author.id")
    email = serializers.EmailField(source="author.email")
    avatar = serializers.ImageField(source="author.avatar")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        field = (
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
        )


class ArticleSerializer(serializers.ModelSerializer):
    author_data = UserViewSerializer(source="*", read_only=True)

    class Meta:
        model = Article
        fields = "__all__"
