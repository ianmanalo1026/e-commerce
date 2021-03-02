# from django import forms
# from .models import BillingAddress
# from django_countries.fields import CountryField

# class CheckOutForm(forms.Form):
#     street_address = forms.CharField(max_length=500, required=True,
#                                      widget=forms.TextInput(attrs={
#                                     'placeholder': '1234 Main St.'
#                                     }))
#     provice = forms.CharField(max_length=500, required=True,
#                                      widget=forms.TextInput(attrs={
#                                     'placeholder': '1234 Main St.'
#                                     }))
#     city = forms.CharField(max_length=500, required=True,
#                                      widget=forms.TextInput(attrs={
#                                     'placeholder': '1234 Main St.'
#                                     }))
#     country = CountryField(blank_label='(select country)').formfield()
#     zip_code = forms.CharField(max_length=500, required=True,
#                                      widget=forms.TextInput(attrs={
#                                     'placeholder': '1234 Main St.'
#                                     }))
    
#     class Meta:
#         model = BillingAddress
#         fields = [
#             'street_address',
#             'provice',
#             'city',
#             'country',
#             'zip_code',
#         ]
    