from rest_framework import serializers

from .models import MyUser


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = MyUser
        fields = ["email", "username", "password", "password2", "id", "avatar"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        user = MyUser(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
            avatar=self.validated_data["avatar"] or None,
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})
        user.set_password(password)
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        style={"input_type": "password"}, required=True
    )
    new_password = serializers.CharField(
        style={"input_type": "password"}, required=True
    )

    def validate_current_password(self, value):
        if not self.context["request"].user.check_password(value):
            raise serializers.ValidationError({"current_password": "Does not match"})
        return value


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            "id",
            "username",
            "email",
            "last_login",
            "is_admin",
            "is_active",
            "created_ad",
            "avatar",
        )

# from djoser.serializers import UserCreateSerializer
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class UserCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ("id", "email", "username", "first_name", "last_name", "password")
