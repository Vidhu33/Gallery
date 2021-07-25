from django import forms
from .models import Image
from taggit.forms import TagWidget

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ('image', 'tags',)
        widgets = {
            'tags': TagWidget(),
        }

        
