from django.urls import path
from .views import ItemListView, ItemDetailView, add_to_cart


urlpatterns = [
    path('', ItemListView.as_view(), name="store"),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    # path('checkout/', views.checkout, name="checkout"),
]