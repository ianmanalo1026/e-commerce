from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField 
import random


CATEGORY_CHOICES = (
    ('Classic', 'Classic'),
    ('Comic Book', 'Comic Book'),
    ('Fantacy', 'Fantacy'),
    ('Fiction', 'Fiction'),
    ('Educational', 'Educational'),
    ('Motivational', 'Motivational')
)

PAYMENT_CHOICES = (
    ('Paypal', 'Paypal'),
    ('Cash','Cash')
)

    

def get_upload_path(instance, filename):
    return 'Items/{0}/{1}'.format(instance.title, filename)

def create_new_ref_number():
      return str(random.randint(1000000000, 9999999999))

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stored = models.DateTimeField(auto_now_add=True)
    item_quantity = models.IntegerField(default=1)
    img = models.ImageField(upload_to=get_upload_path)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=15)
    slug = models.SlugField()
    
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Item, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})
    
    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })
    
    def get_remove_from_cart_url(self):
        return reverse("remove_from_cart", kwargs={
            'slug': self.slug
        })
        
    def get_add_single_item_to_cart_url(self):
        return reverse("add_single_item_to_cart", kwargs={
            'slug': self.slug
        })
    
    def get_remove_single_item_from_cart_url(self):
        return reverse("remove_single_item_from_cart", kwargs={
            'slug': self.slug
        })
        

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    def get_total_item_price(self):
        return self.quantity * self.item.price
    
    def get_final_price(self):
        return self.get_total_item_price()
    
    def get_quantity(self):
        return self.quantity
    
class ShippingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=True, blank=True)
    street_address = models.CharField(max_length=300)
    province = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.user)
    
    def get_phone_number(self):
        return self.phone_number
    
    @property  
    def get_full_address(self):
        return f"{self.street_address}, {self.province}, {self.city}, {self.country}, {self.zip_code}"
        
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(null=True, blank=True)
    shipping_address = models.CharField(max_length=500)
    reference_number = models.CharField(max_length=10, null=True, blank=True, default=create_new_ref_number())
    
    def get_absolute_url(self):
        return reverse("history-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.reference_number
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
    
    
