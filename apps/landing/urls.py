from django.urls import path
from .views import LandingScreen

app_name = "landing"

urlpatterns = [
    path("", LandingScreen.as_view(), name="landing"),
]