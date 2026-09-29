from django.shortcuts import render, redirect
from django.views import View


class LandingScreen(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home:home")
        return render(request, "landing/landing.html")