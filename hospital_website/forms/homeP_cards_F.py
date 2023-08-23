from django import forms
from ..models.homeP_cards_M import HomePageCard1, WorkingHours, HomePageCard3

class HomePageCard1Form(forms.ModelForm):
    class Meta:
        model = HomePageCard1
        fields = ['heading', 'body', 'color', 'iconInput']

class WorkingHoursForm(forms.ModelForm):
    class Meta:
        model = WorkingHours
        fields = ['day', 'opening_time', 'closing_time']

class HomePageCard3Form(forms.ModelForm):
    class Meta:
        model = HomePageCard3
        fields = ['heading', 'body', 'color', 'iconInput']
