from django.shortcuts import redirect, render ,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView, 
                                  DeleteView)
from .models import (Item, 
                     Order, 
                     OrderItem)
from .forms import (ItemCreateForm, 
                    ItemUpdateForm)
from django.contrib.auth.models import User
from django_filters.views import FilterView
from account.models import Profile
from .filters import ItemFilter
from django.http import JsonResponse
import json

class ItemListView(FilterView):
    model = Item
    template_name = 'ecommpage/store.html'
    filterset_class = ItemFilter
    paginate_by = 6
    

class IndexListView(ListView):
    model = Item
    template_name = 'ecommpage/index.html'
    paginate_by = 3


class ItemDetailView(DetailView):
    model = Item
    template_name = "ecommpage/product.html"
    

class ItemCreateView(LoginRequiredMixin, CreateView):
    form_class = ItemCreateForm
    template_name = "ecommpage/create.html"
    success_url = '/'
    
    
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemUpdateForm
    template_name = "ecommpage/create.html"
    success_url = '/'
    

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    
    model = Item
    template_name = "ecommpage/delete.html"
    success_url = "/"
    
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Item, slug=slug)
      
class OrderSummaryView(LoginRequiredMixin, DetailView):

    def get(self, request, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'ecommpage/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect('store')
        
class HistoryListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "ecommpage/history.html"
    success_url = "/"
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, ordered=True).order_by('-ordered_date')
    
    
class HistoryDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "ecommpage/history_detail.html"
    success_url = "/"
    
    def get_context_data(self, *args, **kwargs):
        context = super(HistoryDetailView, self).get_context_data(**kwargs)
        context['order'] = Order.objects.filter(user=self.request.user, ordered=True)
        return context


class OrderStatus(LoginRequiredMixin, ListView):
    model = Order
    template_name = "ecommpage/orders.html"
    success_url = "/"
    
    
@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            if item.item_quantity <= order_item.quantity:
                messages.warning(request, "Out of Stock")
                return redirect("product", slug=slug)
            else:
                order_item.quantity += 1
                order_item.save()
                order.save()
                messages.success(request, "This item was updated to your cart.")
        else:
            messages.success(request, "This item was added to your cart.")
            order.items.add(order_item)
            order.save()
    else:
        order = Order.objects.create(
            user=request.user)
        order.items.add(order_item)
        order.save()
        messages.success(request, "This item was added to your cart.")
    return redirect("product", slug=slug)


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                order.save()
            else:
                order.items.remove(order_item)
                order_item.delete()
                order.save()
            messages.warning(request, "This item was removed from your cart.")
            return redirect("product", slug=slug)
        else:
            messages.warning(request, "This item was not in your cart.")
            return redirect("product", slug=slug)
    else:
        messages.warning(request, "You do not have an active order")
        return redirect("product", slug=slug)
    
    
@login_required
def add_single_item_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    if item.item_quantity == 0:
        messages.warning(request, "Out of stock")
    else:
        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False,
        )
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            # check if the order item is in the order
            if order.items.filter(item__slug=item.slug).exists():
                order_item.quantity += 1
                order_item.save()
                order.save()
                messages.success(request, "This item was updated to your cart.")
            else:
                messages.success(request, "This item was added to your cart.")
                order.items.add(order_item)
                order.save()
        else:
            order, created = Order.objects.get_or_create(
                user=request.user)
            order.items.add(order_item)
            order.save()
            messages.success(request, "This item was added to your cart.")
        return redirect("order-summary", slug=slug)
    

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                order.save()
            else:
                order.items.remove(order_item)
                order.save()
            messages.warning(request, "This item was removed from your cart.")
            return redirect("order-summary", slug=slug)
        else:
            messages.warning(request, "This item was not in your cart.")
            return redirect("order-summary", slug=slug)
    else:
        messages.warning(request, "You do not have an active order")
        return redirect("order-summary", slug=slug)
    
    
@login_required
def checkOut(request):
    try:
        shipping_address = Profile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        messages.warning(request, 'Please update first your billing address')
        return redirect('order-summary')
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        for order_item in order.items.all():
            if order_item.item.item_quantity >= order_item.quantity:
                return render(request, 'ecommpage/checkout.html', {'object':order, 'shipping_address': shipping_address})
            else:
                messages.warning(request, 'Out of stock!')
                return redirect('order-summary')
    except ObjectDoesNotExist:
        messages.error(request, "You do not have an active order")
        return redirect('store')
    
@login_required
def paymentComplete(request):
    try:
        body = json.loads(request.body)
        order = Order.objects.get(id=body['orderID'])
        address = Profile.objects.get(user=request.user)
        for order_item in order.items.all():
            order_item.item.item_quantity -= order_item.quantity
            order_item.item.save()
            order_item.ordered = True
            order_item.save()
        order.shipping_address = address.get_full_address
        order.save()
        order.ordered = True
        order.total_price = body['total']
        order.save()
        messages.success(request, "Order has been processed!")
        return JsonResponse('Payment Complete', safe=False)
    except:
        messages.warning(request, "Payment did not go throuh")
        return redirect('order-summary')

    
    