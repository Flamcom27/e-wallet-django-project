from django.contrib import admin
from django.urls import path

from . import views 


urlpatterns = [
    path('start-chat/<int:pk>/', views.StartChatView.as_view(), name="start_chat"),
    path('window/<int:pk>/', views.ChatWindowView.as_view(), name='chat_window')
]
