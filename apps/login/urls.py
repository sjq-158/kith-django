# newly added
from django.urls import path
from .views import LoginScreen, LogoutScreen

app_name = "login"

urlpatterns = [
    path("", LoginScreen.as_view(), name="login"),
    path("logout/", LogoutScreen.as_view(), name="logout"),
]