# from django.shortcuts import render

# # Create your views here.

# added
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from .models import UserSettings


@method_decorator(login_required, name="dispatch")
class SettingsScreen(View):
    def get(self, request):
        settings_obj, _ = UserSettings.objects.get_or_create(user=request.user)
        return render(request, "user_settings/settings.html", {"settings_obj": settings_obj})

    def post(self, request):
        settings_obj, _ = UserSettings.objects.get_or_create(user=request.user)
        settings_obj.dark_mode = "dark_mode" in request.POST
        settings_obj.email_notifications = "email_notifications" in request.POST
        settings_obj.save()
        return redirect("user_settings:settings")