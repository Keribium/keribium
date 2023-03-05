from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@login_required(login_url="/login/")
def index(request):
    return render(request, "home/index.html")


def login_index(request):
    if request.user.is_authenticated:
        return render(request, "home/index.html")
    return render(request, "login/index.html")


def error_404(request):
    return render(request, "404.html")


def error_500(request):
    return render(request, "500.html")
