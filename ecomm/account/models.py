from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    since = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    
    def __str__(self):
        return str(self.user)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.first_name, self.user.last_name)
        super(Profile, self).save(*args, **kwargs)
        

    
