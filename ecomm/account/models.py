from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    since = models.DateTimeField(auto_now_add=True)
    phone_number = PhoneNumberField()
    street_address = models.CharField(max_length=300)
    provice = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    photo = models.ImageField(upload_to=None)
    slug = models.SlugField()
    
    
    def __str__(self):
        return str(self.user)
        
    
