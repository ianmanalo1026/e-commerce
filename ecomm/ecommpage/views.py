from django.shortcuts import redirect, render ,get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item, Order, OrderItem
from .forms import ItemCreateForm, ItemUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist

class ItemListView(ListView):
    model = Item
    template_name = 'ecommpage/store.html'
    paginate_by = 10
    

class ItemDetailView(DetailView):
    model = Item
    template_name = "ecommpage/product.html"
    

class ItemCreateView(LoginRequiredMixin, CreateView):
    form_class = ItemCreateForm
    template_name = "ecommpage/create.html"
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(ItemCreateView, self).form_valid(form)
    

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    form_class = ItemUpdateForm
    template_name = "ecommpage/create.html"
    success_url = '/'
    
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.creator:
            return True
        return False
    

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    model = Item
    template_name = "ecommpage/delete.html"
    success_url = "/"
    
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Item, slug=slug)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.creator:
            return True
        return False
    
    
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
            return redirect('/')
 
 

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
            order_item.quantity += 1
            order_item.save()
            order.save()
            messages.success(request, "This item was updated to your cart.")
        else:
            messages.success(request, "This item was added to your cart.")
            order.items.add(order_item)
            order.save()
    else:
        final_price = OrderItem.objects.filter(user=request.user, ordered=False).annotate()
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
    
