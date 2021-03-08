from django.urls import path
from .views import (IndexListView,
                    ItemListView, 
                    ItemDetailView,
                    OrderSummaryView,
                    ItemCreateView, 
                    ItemUpdateView,
                    ItemDeleteView,
                    history,
                    add_to_cart, 
                    remove_from_cart,
                    paymentComplete
                    )


urlpatterns = [
    path('', IndexListView.as_view(), name="index"),
    path('store', ItemListView.as_view(), name="store"),
    path('create/', ItemCreateView.as_view(), name="create"),
    path('update/<slug>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<slug>/', ItemDeleteView.as_view(), name='delete'),
    path('history/', history, name='history'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('complete/', paymentComplete, name="complete"),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
]