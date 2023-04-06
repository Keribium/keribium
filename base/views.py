from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import (BlacklistedToken,
                                                             OutstandingToken)
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserLoginSerializer, UserRegisterSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class APILogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if self.request.data.get("all"):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"message": "OK, goodbye, all refresh tokens blacklisted"}, status=status.HTTP_200_OK)
        refresh_token = self.request.data.get("refresh_token")
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response({"message": "OK, goodbye"}, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserLoginSerializer(data=data)
            if serializer.is_valid():
                email = serializer.validated_data["email"]
                password = serializer.validated_data["password"]

                user = authenticate(email=email, password=password)
                if user:
                    return Response(
                        get_tokens_for_user(user), status=status.HTTP_200_OK
                    )
                else:
                    return Response(
                        {"detail": "Invalid credentials"},
                        status=status.HTTP_401_UNAUTHORIZED,
                    )
            return Response(
                {"message": "Something went wrong", "errors": serializer.errors},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class RegisterAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            if data["password"] != data["confirm_password"]:
                return Response(
                    {
                        "message": "Something went wrong",
                        "errors": "Password and confirm password do not match",
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            serializer = UserRegisterSerializer(data=data)
            if serializer.is_valid():
                user = serializer.save()
                tokens = get_tokens_for_user(user)
                return Response(tokens, status=status.HTTP_201_CREATED)
            return Response(
                {"message": "Something went wrong", "errors": serializer.errors},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
