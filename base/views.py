from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserLoginSerializer, UserRegisterSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


def index(request):
    return render(request, "home/index.html")


def error_404(request):
    return render(request, "404.html")


def error_500(request):
    return render(request, "500.html")


@api_view(["POST"])
def login_view(request):
    try:
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            user = authenticate(email=email, password=password)
            if user:
                return Response(get_tokens_for_user(user), status=status.HTTP_200_OK)
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


@api_view(["POST"])
def register_view(request):
    try:
        data = request.data
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
