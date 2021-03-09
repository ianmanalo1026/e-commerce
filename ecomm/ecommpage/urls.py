from django.urls import path
from .views import (IndexListView,
                    ItemListView, 
                    ItemDetailView,
                    OrderSummaryView,
                    ItemCreateView, 
                    ItemUpdateView,
                    ItemDeleteView,
                    HistoryListView,
                    HistoryDetailView,
                    add_to_cart, 
                    remove_from_cart,
                    checkOut,
                    paymentComplete,
                    )


urlpatterns = [
    path('', IndexListView.as_view(), name="index"),
    path('store', ItemListView.as_view(), name="store"),
    path('create/', ItemCreateView.as_view(), name="create"),
    path('update/<slug>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<slug>/', ItemDeleteView.as_view(), name='delete'),
    path('history/', HistoryListView.as_view(), name='history'),
    path('history/<pk>/', HistoryDetailView.as_view(), name='history-detail'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('complete/', paymentComplete, name="complete"),
    path('check-out/', checkOut, name="check-out"),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
]