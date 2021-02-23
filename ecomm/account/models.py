from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    since = models.DateTimeField(auto_now_add=True)
    phonenumber = models.IntegerField()
    photo = models.ImageField(upload_to=None)
    
    def __str__(self):
        self.user
