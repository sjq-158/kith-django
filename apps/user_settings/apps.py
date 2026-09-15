# from django.apps import AppConfig


# class UserSettingsConfig(AppConfig):
#     name = 'user_settings'

from django.apps import AppConfig


class UserSettingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.user_settings"