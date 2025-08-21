from functools import partial

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http.request import HttpRequest
from django.views import View
from django.utils.decorators import method_decorator

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import User


registration_page = partial(render, template_name="registration.html")
login_page = partial(render, template_name="login.html")
# profile_page = partial(render, template_name="profile.html")


class IndexView(View):
    def get(self, request: HttpRequest):
        return render(request, "index.html", {})


class RegistrationView(View):
    def get(self, request: HttpRequest):
        return registration_page(
            request, context={"user_form": CustomUserCreationForm()}
            )

    def post(self, request: HttpRequest):
        user_form = CustomUserCreationForm(data=request.POST)

        if user_form.is_valid():
            login(request, user_form.save())
            return redirect("home")

        return registration_page(request, context={"user_form": user_form})


class LoginView(View):
    def get(self, request: HttpRequest):
        return login_page(request, context={
            "user_form": CustomAuthenticationForm()
            })

    def post(self, request: HttpRequest):
        user_form = CustomAuthenticationForm(request, data=request.POST)

        if user_form.is_valid():
            login(request, user_form.get_user())
            return redirect("home")

        error_message = "That user does not exist or wrong password"
        user_form.add_error(
            field="username", error=error_message
            )
        return login_page(request, context={"user_form": user_form})


@method_decorator(login_required, name='get')
class LogoutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect("home")


class SearchView(View):
    def get(self, request: HttpRequest):
        users = User.objects.filter(
            username__icontains=request.GET.get("username", "")
            )
        return render(request, "search.html", {"users": users})


# [x]TODO make ProfileView
class ProfileView(View):
    def get(self, request: HttpRequest, pk: int | None = None):
        user = request.user
        if pk:
            user = get_object_or_404(User, pk=pk)
        elif not user.is_authenticated:
            redirect("home")
        return render(request, "profile.html", {"data":user})
