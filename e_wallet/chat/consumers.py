from channels.generic.websocket import JsonWebsocketConsumer

class ChatConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()

        self.send_json({"message": "hello from server"})

    def receive_json(self, content, **kwargs):
        print(content["message"])

    def disconnect(self, code):
        print("Closed:", code)
