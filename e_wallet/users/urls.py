from django.contrib import admin
from django.urls import path

from .views import (
    IndexView, RegistrationView, LoginView,
    LogoutView, SearchView
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="home"),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("search", SearchView.as_view(), name='search')
]
