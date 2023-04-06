from django.urls import path, include

from .views import LoginAPIView, RegisterAPIView, APILogoutView

urlpatterns = [
    path("api/register/", RegisterAPIView.as_view(), name="register"),
    path("api/login/", LoginAPIView.as_view(), name="login"),
    path("api/logout/", APILogoutView.as_view(), name="logout"),
    path('accounts/', include('allauth.urls')),
]
