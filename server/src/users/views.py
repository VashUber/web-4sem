from django.conf import settings
import jwt
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MyUser
from .serializers import (
    PasswordChangeSerializer,
    RegistrationSerializer,
    UserListSerializer,
)
from .tasks import sendEmailVerification
from .utils import get_tokens_for_user

# Create your views here.


class RegistrationView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request):
        serializer = RegistrationSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()

            user = MyUser.objects.get(email=serializer.data["email"])

            user_serializer = UserListSerializer(
                user, context={"request": request}
            ).data

            current_site = get_current_site(request).domain
            relativeLink = reverse("email-verify")

            auth_data = get_tokens_for_user(user)

            email_subject = "email_subject"
            access_token = auth_data["access"]

            absurl = (
                "http://" + current_site + relativeLink + "?token=" + str(access_token)
            )
            email_body = (
                "Hi "
                + user_serializer["name"]
                + " Use the link below to verify your email \n"
                + absurl
            )

            data = {
                "email_subject": email_subject,
                "email_to": (user_serializer["email"],),
                "body": email_body,
            }

            sendEmailVerification.delay(data)

            return Response(
                {"user": user_serializer, "token": auth_data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request):
        if "email" not in request.data or "password" not in request.data:
            return Response(
                {"msg": "Credentials missing"}, status=status.HTTP_400_BAD_REQUEST
            )
        email = request.data["email"]
        password = request.data["password"]

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)

            return Response(
                {"msg": "Login Success", **auth_data}, status=status.HTTP_200_OK
            )
        return Response(
            {"msg": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response({"msg": "Successfully Logged out"}, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        serializer = PasswordChangeSerializer(
            context={"request": request}, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data["new_password"])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrentUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = MyUser.objects.get(email=request.user)
        serializer = UserListSerializer(user, context={"request": request})
        return Response(serializer.data)


class EmailVerifyView(APIView):
    def get(self, request):
        token = request.GET.get("token")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = MyUser.objects.get(id=payload["user_id"])

            if not user:
                return Response(
                    {"error": "Not user"}, status=status.HTTP_400_BAD_REQUEST
                )

            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response({"email": "Success"}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response(
                {"error": "Activations error"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.DecodeError as identifier:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )


class UserView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        user = MyUser.objects.get(id=pk)

        if not user:
            return Response({"error": "Пользователь не найден"})

        serializer = UserListSerializer(user, context={"request": request})

        return Response(serializer.data)
