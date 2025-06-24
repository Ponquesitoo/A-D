from django import forms
from .models import Sources, Categories, Cat_x_Source

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
        model = Cat_x_Source
        fields = ['source', 'category']
        
