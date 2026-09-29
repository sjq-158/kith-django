# from django.shortcuts import render

# # Create your views here.

# added - 09292026
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from .models import Admin, HeadPharmacist, Pharmacist

PROFILE_MODELS = {
    "admin": Admin,
    "head_pharmacist": HeadPharmacist,
    "pharmacist": Pharmacist,
}


def get_profile(user):
    profile, _ = PROFILE_MODELS[user.role].objects.get_or_create(user=user)
    return profile


@method_decorator(login_required, name="dispatch")
class ProfileScreen(View):
    def get(self, request):
        profile = get_profile(request.user)
        return render(request, "profiles/profile.html", {
            "profile": profile,
            "phone": getattr(profile, profile.phone_field),
            "has_license": hasattr(profile, "license_number"),
        })

    def post(self, request):
        profile = get_profile(request.user)
        profile.first_name = request.POST.get("first_name", "").strip()
        profile.last_name = request.POST.get("last_name", "").strip()
        setattr(profile, profile.phone_field, request.POST.get("phone", "").strip())
        if hasattr(profile, "license_number"):
            profile.license_number = request.POST.get("license_number", "").strip()
        profile.save()
        return redirect("profiles:profile")

# added - 09152026
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.utils.decorators import method_decorator
# from django.views import View

# from .models import Profile


# @method_decorator(login_required, name="dispatch")
# class ProfileScreen(View):
#     def get(self, request):
#         profile, _ = Profile.objects.get_or_create(user=request.user)
#         return render(request, "profiles/profile.html", {"profile": profile})

#     def post(self, request):
#         profile, _ = Profile.objects.get_or_create(user=request.user)
#         profile.full_name = request.POST.get("full_name", "")
#         profile.bio = request.POST.get("bio", "")
#         profile.save()
#         return redirect("profiles:profile")