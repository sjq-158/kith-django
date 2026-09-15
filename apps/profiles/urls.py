# newly added
from django.urls import path
from .views import ProfileScreen

app_name = "profiles"

urlpatterns = [
    path("", ProfileScreen.as_view(), name="profile"),
]