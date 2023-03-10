from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_index, name="login_index"),
    path("register/", views.register_index, name="register_index"),
    path("404/", views.error_404, name="404"),
    path("500/", views.error_500, name="500"),
]