from django.urls import path

from .views import LoginAPIView, RegisterAPIView, APILogoutView

urlpatterns = [
    path("api/register/", RegisterAPIView.as_view(), name="register"),
    path("api/login/", LoginAPIView.as_view(), name="login"),
    path("api/logout/", APILogoutView.as_view(), name="logout"),
]
