
from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse
from django.contrib import messages
from hospital_website.models.models import *
from django.contrib.auth.models import User
from twilio.rest import Client
# from .forms import ContactForm
from django.shortcuts import render, redirect
from users.models import Profile  #Importing Profile from Users app to display info on about page
from .forms import *
from .models import *
# Create your views here.
def services(request):
    service_categories = ServiceCategory.objects.all()
    messages =''
    if request.method == 'POST':
        form1 = AppointmentForm1(request.POST)
        form2 = AppointmentForm2(request.POST)
        form3 = AppointmentForm3(request.POST)
        form4 = AppointmentForm4(request.POST)
        print('time and date')
        print(form1)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            # Create an instance of the Appointment model and populate it with data
            appointment = Appointment(
                name=form1.cleaned_data['name'],
                email=form1.cleaned_data['email'],
                phone=form2.cleaned_data['phone'],
                date=form3.cleaned_data['date'],
                time=form3.cleaned_data['time'],
                service=form4.cleaned_data['service'],
                message=form4.cleaned_data['message']
            )
            appointment.save()
            print(appointment)
            
            messages = "Appointment was succefully booked, we will get back to you in due time"
            # Get the previous URL
            previous_url = request.META.get('HTTP_REFERER')
            # return to the previous Url if available
            return redirect(previous_url)
    
    else:
        form1 = AppointmentForm1()
        form2 = AppointmentForm2()
        form3 = AppointmentForm3()
        form4 = AppointmentForm4()
    context = {
        'service_categories': service_categories,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'messages': messages, 
        
        }

    # Render the response and send it back!
    return render(request, 'home_page_includes/services.html', context)

def services_offered(request, slug):
    category = get_object_or_404(ServiceCategory, slug=slug)
    services = category.serviceoffered_set.all()
    form1 = AppointmentForm1()
    form2 = AppointmentForm2()
    form3 = AppointmentForm3()
    form4 = AppointmentForm4()

    if request.method == 'POST':
        form1 = AppointmentForm1(request.POST)
        form2 = AppointmentForm2(request.POST)
        form3 = AppointmentForm3(request.POST)
        form4 = AppointmentForm4(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            try:
                form1.save()
                form2.save()
                form3.save()
                form4.save()
                success_message = "Appointment booked successfully."
            except Exception as e:
                # Handle exceptions (e.g., database errors)
                error_message = f"An error occurred: {str(e)}"
    
    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'services': services,
        }

    # Render the response and send it back!
    return render(request, 'services/services_offered.html', context)




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