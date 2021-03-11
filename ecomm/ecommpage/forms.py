from django import forms
from .models import Item
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
        
        