from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib import messages
from .models.models import *
from .models.aboutP_M import *
from .models.frontP_card_M import WorkingHours
from .forms.frontP_card_F import WorkingHoursForm
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

    context = {
        'base': base,
        'info': info, 
        'working_hours': working_hours,
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

# def working_hours(request):
#     working_hours = WorkingHours.objects.all()
#     form = WorkingHoursForm()

#     # if request.method == 'POST':
#     #     form = WorkingHoursForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()

#     context = {
#             'working_hours': working_hours, 
#             #    'form': form
#        }
#     return render(request, 'home.html', context)