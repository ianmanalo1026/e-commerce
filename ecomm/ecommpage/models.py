from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils.text import slugify

CATEGORY_CHOICES = (
    ('C', 'Classic'),
    ('CB', 'Comic Book'),
    ('F', 'Fantacy'),
    ('FC', 'Fiction'),
    ('E', 'Educational'),
    ('M', 'Motivational')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stored = models.DateTimeField(auto_now_add=True)
    item_quantity = models.IntegerField(default=1)
    img = models.ImageField(upload_to='images/')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField(unique=True)
    
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


        
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    def get_total_item_price(self):
        return self.quantity * self.item.price
    
    def get_final_price(self):
        return self.get_total_item_price()
    
    
    
    
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total