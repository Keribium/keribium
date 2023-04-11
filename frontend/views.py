from django.shortcuts import render
import yaml


def profile(request):
    context = {
        "user": {
            "name": "Khushiyant",
            "bio": "Research Intern, Germany | Research Assistant, NTNU, Norway | Remote Developer | Building @Keribium | OpenSource Developer @zulip @unifyai | SIH’22 Winner",
        },
        "bookmarks": [
            {
                "title": "test",
                "description": "dfsdfsdfsdfvdsfdfbsdvsdvsd",
                "url": "https://www.google.com",
            },
            {
                "title": "test2",
                "description": "dfsdfsdfsdfvdsfdfbsdvsdvsd",
                "url": "https://www.google.com",
            },
            {
                "title": "test",
                "description": "dfsdfsdfsdfvdsfdfbsdvsdvsd",
                "url": "https://www.google.com",
            },
            {
                "title": "test2",
                "description": "dfsdfsdfsdfvdsfdfbsdvsdvsd",
                "url": "https://www.google.com",
            },
            {
                "title": "test",
                "description": "dfsdfsdfsdfvdsfdfbsdvsdvsd",
                "url": "https://www.google.com",
            },
            {
                "title": "test2",
                "description": "dfsdfsdfsdfvdsfdfbsdvsdvsd",
                "url": "https://www.google.com",
            }
        ]
    }
    return render(request, "profile/index.html", context=context)


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
