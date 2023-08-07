from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib import messages
from .models.models import *
from .models.aboutP_M import *
from django.contrib.auth.models import User
# from .forms import ContactForm
from users.models import Profile  #Importing Profile from Users app to display info on about page

# Create your views here.
def main_index(request):
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
    return render(request, 'home.html', context)

def about(request):
    base = BaseData.objects.first()
    a_display= AboutPage.objects.first()
    abtlist = AboutList.objects.all()
    context = {
        "user":request.user,
        'base': base,
        'about': a_display,
        'abtlist': abtlist,
        }
    return render(request, 'about.html', context)
def blog(request):

    return render(request, "blog/blog_list.html")
    