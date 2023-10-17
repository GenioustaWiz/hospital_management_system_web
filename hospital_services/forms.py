# forms.py
from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class AppointmentForm1(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email',]
class AppointmentForm2(forms.ModelForm):
    phone = PhoneNumberField(
            widget=PhoneNumberPrefixWidget(initial='KE', attrs={'class': 'p-no'})
        )
    class Meta:
        model = Appointment
        fields = ['phone',]
class AppointmentForm3(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time',] 
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
class AppointmentForm4(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=ServiceOffered.objects.all(),  # Replace YourServiceModel with the actual model you're using
        empty_label="Click to choose a service",  # Set the default placeholder text
    )
    class Meta:
        model = Appointment
        fields = ['service', 'message']
    

class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ['category_name','iconInput', 'cat_description', ]  

class ServiceOfferedForm(forms.ModelForm):
    class Meta:
        model = ServiceOffered
        fields = ['service_name', 'description',]
        
ServiceOfferedFormSet = forms.inlineformset_factory(
    ServiceCategory,ServiceOffered,
    form=ServiceOfferedForm,
    extra=0,  # Number of empty forms to display
)