from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    friends = models.ManyToManyField("self", blank=True, default=None)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.username
