from django.urls import path
from . import views

app_name = "ecommpage"

urlpatterns = [
    path('', views.home, name="home")
]