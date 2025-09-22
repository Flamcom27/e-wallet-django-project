from django.contrib import admin
from django.urls import path


from . import views 


urlpatterns = [
    path('dialog/<int:pk>', admin.site.urls),
]