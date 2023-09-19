
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import ServiceCategory, ServiceOffered
from .forms import ServiceCategoryForm, ServiceOfferedForm

from django.http import HttpResponse
from django.contrib import messages
from hospital_website.models.models import *
from django.contrib.auth.models import User
from twilio.rest import Client
# from .forms import ContactForm
from users.models import Profile  #Importing Profile from Users app to display info on about page
from .forms import AppointmentForm
from .models import Appointment
# Create your views here.
def services(request):
    form = AppointmentForm()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            try:
                # Create an instance of the Appointment model and save it
                appointment = Appointment(
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    phone=form.cleaned_data['phone'],
                    day=form.cleaned_data['day'],
                    time=form.cleaned_data['time'],
                    department=form.cleaned_data['department'],
                    message=form.cleaned_data['message']
                )
                appointment.save()
                # Send WhatsApp message using Twilio
                # send_whatsapp_message(appointment)
                # You can add success messages or other actions here
                success_message = "Appointment booked successfully."
            except Exception as e:
                # Handle exceptions (e.g., database errors)
                error_message = f"An error occurred: {str(e)}"
    
    # Query database
    info = HomePage.objects.first()
    # tech= main_page_service_details.objects.all()
    base = BaseData.objects.first()
    context = {
        'form': form,
        'base': base,
        'info': info, 
        # 'tech': tech,
        }

    # Render the response and send it back!
    return render(request, 'services.html', context)





# def send_whatsapp_message(appointment):
#     account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
#     auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
#     twilio_number = 'YOUR_TWILIO_PHONE_NUMBER'
#     recipient_number = 'RECIPIENT_PHONE_NUMBER_WITH_COUNTRY_CODE'

#     client = Client(account_sid, auth_token)
#     message = f"New Appointment:\nName: {appointment.name}\nEmail: {appointment.email}\nPhone: {appointment.phone}\nDepartment: {appointment.department}\nDay: {appointment.day}\nTime: {appointment.time}\nMessage: {appointment.message}"

#     client.messages.create(
#         body=message,
#         from_=twilio_number,
#         to=recipient_number,
#         provide_feedback=True
#     )