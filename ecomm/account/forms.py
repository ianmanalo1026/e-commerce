from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = [
                "username",
                "password1",
                "password2",
                "first_name",
                "last_name",
                "email",
                ]

class UserSigninForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = [
                    "username",
                    "password"
                 ]