from django import forms
from ..models.frontP_card_M import FrontPageCard1, WorkingHours, FrontPageCard3

class FrontPageCard1Form(forms.ModelForm):
    class Meta:
        model = FrontPageCard1
        fields = ['heading', 'body', 'color', 'iconInput']

class WorkingHoursForm(forms.ModelForm):
    class Meta:
        model = WorkingHours
        fields = ['day', 'opening_time', 'closing_time']

class FrontPageCard3Form(forms.ModelForm):
    class Meta:
        model = FrontPageCard3
        fields = ['heading', 'body', 'color', 'iconInput']
