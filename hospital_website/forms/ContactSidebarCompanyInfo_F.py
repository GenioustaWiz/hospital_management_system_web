from django import forms
from ..models.models import ContactSidebarCompanyInfo

class ContactSidebarCompanyInfoForm(forms.ModelForm):
    class Meta:
        model = ContactSidebarCompanyInfo
        fields = ['name', 'phone_number', 'email', 'address']
