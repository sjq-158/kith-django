# from django.shortcuts import render

# # Create your views here.

# added
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View


class LoginScreen(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login/login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home:home")
        return render(request, "login/login.html", {"form": form})


class LogoutScreen(View):
    def get(self, request):
        logout(request)
        return redirect("login:login")