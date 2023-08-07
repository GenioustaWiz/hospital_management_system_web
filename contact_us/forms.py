
from django.forms import ModelForm,TextInput
from .models import contact


class ContactForm(ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
        # widgets = {
        #     'message': TextInput(attrs={
        #         # 'class': "full",
        #         'placeholder': 'Enter message here'
        #         }),
        # } 