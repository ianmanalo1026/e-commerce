from django.urls import path
from .views import ItemListView, ItemDetailView


urlpatterns = [
    path('', ItemListView.as_view(), name="store"),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    # path('checkout/', views.checkout, name="checkout"),
]