from django.urls import path
from .views import HomeScreen

urlpatterns = [
    path("home/", HomeScreen.as_view(), name="home"),
]