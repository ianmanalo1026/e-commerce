from django.urls import path
from .views import SignUpView, SignInView, SignOutView, ProfileView, ProfileUpdateView


app_name = "account"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('signin/', SignInView.as_view(), name="signin"),
    path('signout/', SignOutView.as_view(), name="signout"),
    path('profile/<slug>', ProfileView.as_view(), name="profile"),
    path('profile/<slug>/update', ProfileUpdateView.as_view(), name="update"),
]
