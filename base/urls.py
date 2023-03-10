from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/register/", views.register_view, name="register"),
    path("api/login/", views.login_view, name="login"),
    path("404/", views.error_404, name="404"),
    path("500/", views.error_500, name="500"),
]
