from django.contrib import admin
from django.urls import path


from . import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name="home"),
    path('registration/', views.RegistrationView.as_view(), name="registration"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path("search/", views.SearchView.as_view(), name='search'),
    path("profile/", views.ProfileView.as_view()), # []TODO fix users.models.User.DoesNotExist: User matching query does not exist.
    path("profile/<int:pk>/", views.ProfileView.as_view(), name="profile"),
]
