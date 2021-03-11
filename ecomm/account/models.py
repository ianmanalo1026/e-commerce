
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField 
from django.urls import reverse


def get_upload_path(instance, filename):
    return 'images/{0}/{1}'.format(instance.user.first_name, filename)
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    since = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to=get_upload_path, blank=True, null=True, default='images/default.png')
    phone_number = PhoneNumberField(null=True, blank=True)
    street_address = models.CharField(max_length=300)
    province = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    slug = models.SlugField()
    
    def __str__(self):
        return str(self.user)
    
    def get_phone_number(self):
        return self.phone_number
    
    @property  
    def get_full_address(self):
        return f"{self.street_address}, {self.province}, {self.city}, {self.country}, {self.zip_code}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.first_name, self.user.last_name)
        super(Profile, self).save(*args, **kwargs)
        

    
