from django.urls import path
from .views import LoginScreen, RegisterScreen, LogoutScreen

urlpatterns = [
    path("", LoginScreen.as_view(), name="login"),
    path("register/", RegisterScreen.as_view(), name="register"),
    path("logout/", LogoutScreen.as_view(), name="logout"),
]