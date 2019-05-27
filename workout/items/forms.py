from django import forms
from .models import item

class Itemsform(forms.ModelForm):


    title=forms.CharField(max_length=50,label='product title')
    description=forms.CharField(max_length=50,
                                widget=forms.Textarea(attrs={'rows':10}))
    class Meta:
        model=item
        fields=[
            'title',
            'description',
            'price'
        ]

    def clean_title(self,*args):
       title= self.cleaned_data.get('title')
       if 'beer' in title:
            raise forms.ValidationError("Beer is not available")
       else:
            return title






