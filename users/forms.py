# from turtle import textinput
from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from phonenumber_field.formfields import PhoneNumberField

class loginpage(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Create a UserUpdateForm to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() 

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'username',]
        widgets = {
            'email': EmailInput(attrs={
                'class': "email", 
                'placeholder': 'Email'
                })
        }
# Create a ProfileUpdateForm to update image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number','country','title','image','github','facebook','googleplus','instagram', ]
        widgets = {
            'phone_number': TextInput(attrs={
                'class': "P-no",
                
                'placeholder': 'Phone number'
                }),
            
        }    
    
# Create a ProfileUpdateForm to update image
class ProfileUpdateForm_desc(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['desc']