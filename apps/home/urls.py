# newly added
from django.urls import path
from .views import HomeScreen

app_name = "home"

urlpatterns = [
    path("", HomeScreen.as_view(), name="home"),
]