from django import forms

from .models import Author
from .models import Quote


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AddQuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['author', 'quote_text']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'quote_text': forms.Textarea(attrs={'class': 'form-control'}),
        }
