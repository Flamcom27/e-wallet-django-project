from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    friends = models.ManyToManyField("self", blank=True, default=None)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    icon = models.ImageField(
        upload_to="images/", default="defaults/default_user_image.png", blank=True
        )

    def __str__(self):
        return self.username
# Create your models here.
class ImageTest(models.Model):
    image = models.ImageField(upload_to='images/') 
