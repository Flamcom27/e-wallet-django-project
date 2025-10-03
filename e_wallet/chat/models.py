from django.db import models
from django.db.models import Q, F, CheckConstraint
from users.models import User

# Create your models here.

class Chat(models.Model):
    participant1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participant1")
    participant2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participant2")

    def __str__(self):
        return f"Chat: {self.id}"
    
    class Meta:
        constraints = [
            CheckConstraint(
                check=~Q(participant1=F("participant2")),
                name="Participants are the same person"
            )
        ]
    
    

class Message(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField(max_length=4096, blank=False)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f'Message: "{self.text}"'
    
