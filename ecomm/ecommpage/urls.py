from django.urls import path
from .views import ItemListView


urlpatterns = [
    path('', ItemListView.as_view(), name="store"),
    # path('cart/', views.cart, name="cart"),
    # path('checkout/', views.checkout, name="checkout"),
]