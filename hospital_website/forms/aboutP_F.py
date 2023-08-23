from django import forms
from ..models.aboutP_M import AboutPage, AboutList

class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = ['heading', 'body']

class AboutListForm(forms.ModelForm):
    class Meta:
        model = AboutList
        fields = ['title', 'image']
