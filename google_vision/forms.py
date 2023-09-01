from django import forms
from .models import GoogleVision

class GoogleVisionForm(forms.ModelForm):
    image = forms.ImageField(label='Bir fotoğraf yükleyiniz.', widget=forms.ClearableFileInput(attrs={'class': 'file'}), required=True)

    class Meta:
        model = GoogleVision
        fields = ['image']
