import django_filters
from django_filters import CharFilter, ChoiceFilter
from django import forms
from .models import Item, CATEGORY_CHOICES
from django.forms.widgets import TextInput
from django.forms.widgets import ChoiceWidget as RadioChoiceInput


class ItemFilter(django_filters.FilterSet):
    title=CharFilter(field_name='title', 
                     lookup_expr='icontains', 
                     label="", 
                     widget=TextInput(attrs=
                    {   'placeholder': 'Search Book Here', 
                        'class': 'form-control',
                        'size': 100,
                    }
                    ))
    category = ChoiceFilter(choices=CATEGORY_CHOICES,  
                            lookup_expr='icontains', 
                            label="")
    class Meta:
        model = Item
        fields = ['title', 'category']
        