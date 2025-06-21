from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http.request import HttpRequest
from django.views import View

from .forms import CustomUserCreationForm, CustomAuthenticationForm


class IndexView(View):
    def get(self, request: HttpRequest):
        return render(request, "index.html", {})


class RegistrationView(View):
    def get(self, request: HttpRequest):
        return render(request, "registration.html", {"user_form": CustomUserCreationForm()})
    
    def post(self, request: HttpRequest):
        user_form = CustomUserCreationForm(data=request.POST)

        if user_form.is_valid():
            user_form.save()
            return redirect("home")
        
        return render(request, "registration.html", {"user_form": user_form})


class LoginView(View):
    def get(self, request: HttpRequest):
        return render(request, "login.html", {"user_form": CustomAuthenticationForm()})
    
    def post(self, request: HttpRequest):
        user_form = CustomAuthenticationForm(request, data=request.POST)
        
        if user_form.is_valid():
            print(dir(user_form))
            login(request, user_form.get_user())
            
        user_form.add_error(field="username", error="That user does not exists or wrong password")
        return render(request, "login.html", {"user_form": user_form})
    