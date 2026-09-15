# newly added
from django.urls import path
from .views import SettingsScreen

app_name = "user_settings"

urlpatterns = [
    path("", SettingsScreen.as_view(), name="settings"),
]