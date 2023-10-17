from django import forms
import re
from ..models.models import ContactSidebarCompanyInfo
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ContactSidebarCompanyInfoForm(forms.ModelForm):
    class Meta:
        model = ContactSidebarCompanyInfo
        fields = ['name', 'email', 'address',] 
        
class ContactSidebarCompanyInfoForm2(forms.ModelForm):
    phone_number = PhoneNumberField(
            widget=PhoneNumberPrefixWidget(initial='KE', attrs={'class': 'p-no'})
        )
    class Meta:
        model = ContactSidebarCompanyInfo
        fields = ['phone_number',]

class ContactSidebarCompanyInfoForm3(forms.Form):
    whatsapp_number = forms.CharField(
        max_length=15,  # Set a suitable max length
        widget=PhoneNumberPrefixWidget(initial='KE', attrs={'class': 'p-no'})
    )

    def set_whatsapp_number(self, whatsapp_number):
        self.fields['whatsapp_number'].widget.initial = whatsapp_number