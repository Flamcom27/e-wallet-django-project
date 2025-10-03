from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync

from .models import Message, Chat

#[ ]TODO saving massages
#[ ]TODO cache recent messages
class ChatConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()
        self.send_json({
            "type": "context",
        })

    def receive_json(self, content, **kwargs):
        type_ = content["type"]
        if type_ == 'context':
            self.room_group_name = content["chatId"]
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
        elif type_ == 'message':
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "send_message",
                    "message": content["message"],
                    "sender": content["sender"]
                }
            )
        print("it Works!!!!!")
        print(content)

    def send_message(self, event):
        self.send_json({
            "type": "message",
            "message": event["message"],
            "sender": event["sender"]
        })

    def disconnect(self, code):
        print("Closed:", code)
