# added - 09292026
from django.urls import path
from .views import HomeScreen

app_name = "home"

urlpatterns = [
    path("", HomeScreen.as_view(), name="home"),
]

# newly added - 09152026
# from django.urls import path
# from .views import HomeScreen

# app_name = "home"

# urlpatterns = [
#     path("", HomeScreen.as_view(), name="home"),
# ]