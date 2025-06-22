from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http.request import HttpRequest
from django.views import View
from django.utils.decorators import method_decorator

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import User


class IndexView(View):
    def get(self, request: HttpRequest):
        return render(request, "index.html", {})


class RegistrationView(View):
    def get(self, request: HttpRequest):
        return render(request, "registration.html", {"user_form": CustomUserCreationForm()})
    
    def post(self, request: HttpRequest):
        user_form = CustomUserCreationForm(data=request.POST)

        if user_form.is_valid():
            login(request, user_form.save())
            return redirect("home")
        
        return render(request, "registration.html", {"user_form": user_form})


class LoginView(View):
    def get(self, request: HttpRequest):
        return render(request, "login.html", {"user_form": CustomAuthenticationForm()})
    
    def post(self, request: HttpRequest):
        user_form = CustomAuthenticationForm(request, data=request.POST)
        
        if user_form.is_valid():
            login(request, user_form.get_user())
            return redirect("home")
            
        user_form.add_error(field="username", error="That user does not exists or wrong password")
        return render(request, "login.html", {"user_form": user_form})


@method_decorator(login_required, name='get')
class LogoutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect("home")


class SearchView(View):
    def get(self, request: HttpRequest):
        users = User.objects.filter(username__icontains=request.GET["username"])
        return render(request, "search.html", {"users": users})