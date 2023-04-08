from django.shortcuts import render
import json
import yaml


def profile(request):
    return render(request, "profile/index.html")


def index(request):
    context = yaml.load(open("static/yaml/faqs.yaml", "r"), Loader=yaml.FullLoader)
    # context["forum_results"] = [
    #     {"title": "test", "detail": "dfsdfsdfsdfvdsfdfbsdvsdvsd"},
    #     {"title": "test2", "detail": "dfsdfsdfsdfvdsfdfbsdvsdvsd"},
    #     {"title": "test", "detail": "dfsdfsdfsdfvdsfdfbsdvsdvsd"},
    #     {"title": "test2", "detail": "dfsdfsdfsdfvdsfdfbsdvsdvsd"},
    #     {"title": "test", "detail": "dfsdfsdfsdfvdsfdfbsdvsdvsd"},
    #     {"title": "test2", "detail": "dfsdfsdfsdfvdsfdfbsdvsdvsd"},
    # ]

    return render(request, "home/index.html", context=context)


def login_index(request):
    return render(request, "login/index.html")


def register_index(request):
    return render(request, "register/index.html")


def error_404(request):
    return render(request, "404.html")


def error_500(request):
    return render(request, "500.html")
