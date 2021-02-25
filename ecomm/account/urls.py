from django.urls import path, reverse_lazy
from .views import SignUpView, SignInView, SignOutView
from django.contrib.auth import views as auth_views

app_name = "account"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('signin/', SignInView.as_view(), name="signin"),
    path('signout/', SignOutView.as_view(), name="signout"),
    
]
