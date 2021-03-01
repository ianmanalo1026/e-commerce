from django import forms
# from .models import BillingAddress
from django_countries.fields import CountryField

# class CheckOutForm(forms.Form):
#     street_address = forms.CharField(max_length=500, required=True,
#                                      widget=forms.TextInput(attrs=(
#                                     'placeholder': '1234 Main St.'
#                                     )))
#     provice = forms.CharField(max_length=500, 
#                               required=True, 
#                               widget=forms.TextInput(attrs=(
#                              'placeholder': 'National Capital Region'
#                               )))
#     city = forms.CharField(max_length=500, 
#                             required=True, 
#                             widget=forms.TextInput(attrs=(
#                             'placeholder': 'Makati City'
#                             )))
#     country = CountryField(blank_label='(select country)').formfiled()
#     zip_code = forms.CharField(max_length=500, 
#                             required=True, 
#                             widget=forms.TextInput(attrs=(
#                             'placeholder': '1700'
#                             )))
    