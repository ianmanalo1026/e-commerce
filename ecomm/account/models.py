from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField  
from django.utils.text import slugify
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    since = models.DateTimeField(auto_now_add=True)
    phone_number = PhoneNumberField()
    street_address = models.CharField(max_length=300)
    province = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    photo = models.ImageField(upload_to=None)
    slug = models.SlugField()
    
    
    def __str__(self):
        return str(self.user)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.first_name, self.user.last_name)
        super(Profile, self).save(*args, **kwargs)
        
    def get_full_address(self):
        return f"{self.street_address}, {self.province}, {self.city}, {self.country}, {self.zip_code}"
        
    
