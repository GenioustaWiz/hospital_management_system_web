
from email import message
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from hospital_website.models.models import  ContactSidebarCompanyInfo
# Create your views here.

def contact(request): 
    if request.method == 'POST':
        form1 = ContactForm1(request.POST)
        form2 = ContactForm2(request.POST)
        form3 = ContactForm3(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            # Create an instance of the contact model and populate it with data
            contact = contact(
                name=form1.cleaned_data['name'],
                email=form1.cleaned_data['email'],
                phone_number=form2.cleaned_data['phone_number'],
                subject=form3.cleaned_data['subject'],
                message=form3.cleaned_data['message'],
            )
            contact.save()
            phone_number = form2.cleaned_data['phone_number']
            phone_no = str(phone_number)  #Convert number to string in order to embed it to body.
            subject = form3.cleaned_data['subject']
            body = {
                'name': form1.cleaned_data['name'],
                'email': form1.cleaned_data['email'],
                'phone_no': phone_no,
                'message': form3.cleaned_data['message']
            }
            message = '\n'.join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('main_index')
    form1 = ContactForm1()
    form2 = ContactForm2()
    form3 = ContactForm3()
    side_info = ContactSidebarCompanyInfo.objects.first()
    
    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'side_info': side_info,
    }
    return render(request, 'contact.html', context)
