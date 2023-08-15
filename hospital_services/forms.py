# forms.py
from django import forms

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Phone No:'}))
    day = forms.CharField(max_length=20, widget=forms.Select(choices=[('Day', 'Day'), ('Sunday', 'Sunday'), ('Monday', 'Monday')]))
    time = forms.CharField(max_length=20, widget=forms.Select(choices=[('Time', 'Time'), ('AM', 'AM'), ('PM', 'PM')]))
    department = forms.CharField(max_length=100, widget=forms.Select(choices=[('Department', 'Department'), ('Eyes checkup', 'Eyes checkup'), ('Teeth Checkup', 'Teeth Checkup')]))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Your Message...'}))
