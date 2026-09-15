# from django.shortcuts import render

# # Create your views here.

# added
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from .models import Profile


@method_decorator(login_required, name="dispatch")
class ProfileScreen(View):
    def get(self, request):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        return render(request, "profiles/profile.html", {"profile": profile})

    def post(self, request):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        profile.full_name = request.POST.get("full_name", "")
        profile.bio = request.POST.get("bio", "")
        profile.save()
        return redirect("profiles:profile")