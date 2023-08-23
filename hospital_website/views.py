from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib import messages
from .models.models import *
from .models.aboutP_M import *
from .models.homeP_cards_M import WorkingHours
from .models.information_footer_M import TopFooterHeading, TopFooterContent, SocialMediaLink

from django.contrib.auth.models import User
# from .forms import ContactForm
from users.models import Profile  #Importing Profile from Users app to display info on about page

# Create your views here.
def main_index(request):
    # Query database
    info = HomePage.objects.first()
    # tech= main_page_service_details.objects.all()
    base = BaseData.objects.first()
    working_hours = WorkingHours.objects.all()

    top_footer_headings = TopFooterHeading.objects.all()
    social_media_links = SocialMediaLink.objects.all()
    context = {
        'base': base,
        'info': info, 
        'working_hours': working_hours,
        'top_footer_headings': top_footer_headings,
        'social_media_links': social_media_links,
        }

    # Render the response and send it back!
    return render(request, 'home.html', context)

def about(request):
    base = BaseData.objects.first()
    a_display= AboutPage.objects.first()
    abtlist = AboutList.objects.all()
    
    top_footer_headings = TopFooterHeading.objects.all()
    social_media_links = SocialMediaLink.objects.all()
    context = {
        "user":request.user,
        'base': base,
        'about': a_display,
        'abtlist': abtlist,
        'top_footer_headings': top_footer_headings,
        'social_media_links': social_media_links,
        }
    return render(request, 'about.html', context)

