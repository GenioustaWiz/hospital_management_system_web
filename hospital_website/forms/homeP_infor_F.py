from django import forms
from ..models.models import HomePage

class HomePageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = ['heading', 'body']
