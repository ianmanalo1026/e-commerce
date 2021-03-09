from django.contrib import admin
from .models import Item, Order, OrderItem


class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('stored',)
    
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('ordered_date',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)

