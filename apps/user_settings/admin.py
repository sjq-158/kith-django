# from django.contrib import admin

# # Register your models here.

# added
from django.contrib import admin
from .models import UserSettings

admin.site.register(UserSettings)