from django import forms
from .models import Sources, Categories, CatSource

class BulletinRequest(forms.ModelForm):
    class Meta:
        model = Sources
        fields = ['link']

class CatRequest(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['category']

class CxSRequest(forms.ModelForm):
    class Meta:
        model = CatSource
        fields = ['source', 'category']
        
