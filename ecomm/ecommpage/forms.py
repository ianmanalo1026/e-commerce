from django import forms
from .models import Item, ShippingAddress

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'title',
            'description',
            'price',
            'item_quantity',
            'img',
            'category',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'item_quantity': forms.TextInput(attrs={'class':'form-control'}),
        }
        
class ItemUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = [
            'title',
            'description',
            'price',
            'item_quantity',
            'img',
            'category',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'item_quantity': forms.TextInput(attrs={'class':'form-control'}),

        }
        
        
class ShippingAddressForm(forms.ModelForm):
    
    class Meta:
        model = ShippingAddress
        fields = [
            'street_address',
            'province',
            'city',
            'country',
            'zip_code',
        ]
        widgets = {
            'street_address': forms.TextInput(attrs={'class':'form-control'}),
            'province': forms.Textarea(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.TextInput(attrs={'class':'form-control'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control'}),
        }