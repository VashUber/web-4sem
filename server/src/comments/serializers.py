from rest_framework import serializers

from .models import Comment

class UserViewSerializer(serializers.Serializer):
    username = serializers.CharField(source="author.name")
    id = serializers.IntegerField(source="author.id")
    email = serializers.EmailField(source="author.email")
    avatar = serializers.ImageField(source="author.avatar")


class CommentSerializer(serializers.ModelSerializer):
    author_data = UserViewSerializer(source="*", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
