from django import forms
from .models import Card, Category, Deck

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Category Name" 
            },
            max_length=30,
            help_text="Max length: 30 chars",
        )
    )
    
    class Meta:
        model = Category
        fields = ("name", "description")