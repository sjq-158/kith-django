# from django.apps import AppConfig


# class RegisterConfig(AppConfig):
#     name = 'register'

from django.apps import AppConfig


class RegisterConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.register"