# newly added
from django.urls import path
from .views import RegisterScreen

app_name = "register"

urlpatterns = [
    path("", RegisterScreen.as_view(), name="register"),
]