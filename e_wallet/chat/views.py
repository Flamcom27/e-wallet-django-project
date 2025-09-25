from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout
from django.http.request import HttpRequest
from django.views import View

from .models import Message, Chat
from users.models import User
# Create your views here.

@method_decorator(login_required, name="get")
class ChatView(View):
    def get(self, request: HttpRequest, pk: int):
        reciever = get_object_or_404(User, pk=pk)
        sender = request.user

        return render(request, "chat/chat.html", context={
            "reciever": reciever
        })
