from .models import productname
from django import forms
class MyForm(forms.ModelForm):

    class Meta:
        model=productname
        fields=[
            'title',
            'price'
        ]

    def clean_title(self):
        title=self.cleaned_data.get('title')
        if title =='abc':
            raise forms.ValidationError('not a proper title')
        return title
