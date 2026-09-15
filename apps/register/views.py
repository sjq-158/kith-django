# from django.shortcuts import render

# # Create your views here.

# added
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View


class RegisterScreen(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "register/register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login:login")
        return render(request, "register/register.html", {"form": form})