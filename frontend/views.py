from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


def login_index(request):
    return render(request, "login/index.html")


def register_index(request):
    return render(request, "register/index.html")


def error_404(request):
    return render(request, "404.html")


def error_500(request):
    return render(request, "500.html")