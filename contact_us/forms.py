
from django.forms import ModelForm,TextInput
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import contact

class ContactForm1(ModelForm):
    phone_number = PhoneNumberField(
            widget=PhoneNumberPrefixWidget(initial='KE', attrs={'class': 'p-no'})
        )
    class Meta:
        model = contact
        fields = ['name', 'email',]
        # widgets = {
        #     'message': TextInput(attrs={
        #         # 'class': "full",
        #         'placeholder': 'Enter message here'
        #         }),
        # } 
        
class ContactForm2(ModelForm):
    phone_number = PhoneNumberField(
            widget=PhoneNumberPrefixWidget(initial='KE', attrs={'class': 'p-no'})
        )
    class Meta:
        model = contact
        fields = ['phone_number',]
        
class ContactForm3(ModelForm):
    class Meta:
        model = contact
        fields = ['subject', 'message',]