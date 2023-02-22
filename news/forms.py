from .models import Articles
from django.forms import ModelForm, TextInput, DateInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Saitatiis satauri'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Statiis anonsi'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'weli-tve-ricxvi'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Statiis teqsti'
            }),
        }
