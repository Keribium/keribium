from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_index, name="login"),
    path("404/", views.error_404, name="404"),
    path("500/", views.error_500, name="500"),
]
