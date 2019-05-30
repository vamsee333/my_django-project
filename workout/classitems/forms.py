from .models import newitems
from django import forms

class Classitemform(forms.ModelForm):
    class Meta:
        model=newitems
        fields=[
            'title',
            'description',
            'price'
        ]
