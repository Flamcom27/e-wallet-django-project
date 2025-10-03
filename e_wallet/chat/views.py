import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth import login, logout
from django.urls import reverse
from django.forms.models import model_to_dict
from django.core import serializers
from django.http.request import HttpRequest
from django.views import View

from .models import Chat
from users.models import User
# Create your views here.

@method_decorator(never_cache, name="get")
@method_decorator(login_required, name="get")
class StartChatView(View):
    def get(self, request: HttpRequest, pk: int):
        participant1 = request.user
        reciever = get_object_or_404(User, pk=pk)
        participant1, participant2 = sorted(
            [request.user, reciever], 
            key=lambda user: user.pk
            )
        chat, _ = Chat.objects.get_or_create(
            participant1=participant1,
            participant2=participant2
            )
        
        request.session[f'reciever:{chat.pk}'] = {
            'pk': reciever.pk,
            'icon': {'url': reciever.icon.url},
            "username": reciever.username
        }
        request.session.modified = True
        return redirect('chat_window', pk=chat.pk,  permanent=True)
    
@method_decorator(login_required, name="get")
class ChatWindowView(View):
    def get(self, request: HttpRequest, pk:int):
        reciever = request.session.get(f'reciever:{pk}')

        if not reciever:
            chat = get_object_or_404(Chat, pk=pk)

            if chat.participant1.pk != request.user.pk:
                reciever = chat.participant1

            else:
                reciever = chat.participant2

            request.session[f'reciever:{chat.pk}'] = {
                'pk': reciever.pk,
                'icon': {'url': reciever.icon.url},
                "username": reciever.username
            }
            
            
        return render(request, "chat/chat.html", context={
            "reciever": reciever,
            "chat_id": pk
        })
