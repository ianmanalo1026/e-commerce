from django.urls import path
from .views import (
                    ItemListView, 
                    ItemDetailView,
                    OrderSummaryView, 
                    add_to_cart, 
                    remove_from_cart, 
                    )


urlpatterns = [
    path('', ItemListView.as_view(), name="store"),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    # path('checkout/', views.checkout, name="checkout"),
]