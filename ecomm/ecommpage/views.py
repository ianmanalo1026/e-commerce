from django.shortcuts import render
from django.views.generic import ListView
from .models import Item, Order, OrderItem

class ItemListView(ListView):
    model = Item
    template_name = 'ecommpage/store.html'
    


# def cart(request):
#     context = {}
#     return render(request, 'ecommpage/cart.html', context)


# def checkout(request):
#     context = {}
#     return render(request, 'ecommpage/checkout.html', context)
