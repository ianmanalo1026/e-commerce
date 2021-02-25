from django.db import models
from django.conf import settings

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stored = models.DateTimeField(auto_now_add=True)
    quality = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title

class OrderItem(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.title
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username