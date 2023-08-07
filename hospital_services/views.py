
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib import messages
from hospital_website.models.models import *
from django.contrib.auth.models import User
# from .forms import ContactForm
from users.models import Profile  #Importing Profile from Users app to display info on about page

# Create your views here.
def services(request):
    # Query database
    info = HomePage.objects.first()
    # tech= main_page_service_details.objects.all()
    base = BaseData.objects.first()
    context = {
        'base': base,
        'info': info, 
        # 'tech': tech,
        }

    # Render the response and send it back!
    return render(request, 'services.html', context)