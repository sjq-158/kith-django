# from django.shortcuts import render

# # Create your views here.

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View


class LoginScreen(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "accounts/login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
        return render(request, "accounts/login.html", {"form": form})


class RegisterScreen(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "accounts/register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "accounts/register.html", {"form": form})


class LogoutScreen(View):
    def get(self, request):
        logout(request)
        return redirect("login")
