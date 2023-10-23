from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib import messages
from .models.models import *
from .models.aboutP_M import *
from .models.homeP_cards_M import WorkingHours
from .models.information_footer_M import TopFooterHeading, TopFooterContent, SocialMediaLink

from django.contrib.auth.models import User

# Import hOSPITAL Services data
from hospital_services.forms import *
from hospital_services.models import *
# Create your views here.
def main_index(request):
    # Query database
    info = HomePage.objects.first()
    # tech= main_page_service_details.objects.all()
    base = BaseData.objects.first()
    working_hours = WorkingHours.objects.all()
    side_info = ContactSidebarCompanyInfo.objects.first()
    top_footer_headings = TopFooterHeading.objects.all()
    social_media_links = SocialMediaLink.objects.first()  # Assuming there's only one instance
    
    ### SERVICES PAGE CODE STARTS HERE ##
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
    ### SERVICES CODE ENDS HERE ###
    ### THE ABOUT PAGE CODE STARTS HER ###
    about_display= AboutPage.objects.first()
    about_list = AboutList.objects.all()
    ### THE ABOUT PAGE CODE ENDS HERE ###
    context = {
        'info': info, 
        'working_hours': working_hours,
        # hospital services context
        'service_categories': service_categories,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'messages': messages, 
        # -===============end============
        #ABOUT PAGE CONTEXT
        "user":request.user,
        'about': about_display,
        'about_list': about_list,
        #==========END====================
        
        }

    # Render the response and send it back!
    return render(request, 'home.html', context)

# # Create your views here.
# def main_index(request):
#     # Query database
#     info = HomePage.objects.first()
#     # tech= main_page_service_details.objects.all()
#     base = BaseData.objects.first()
#     working_hours = WorkingHours.objects.all()
#     side_info = ContactSidebarCompanyInfo.objects.first()
#     top_footer_headings = TopFooterHeading.objects.all()
#     social_media_links = SocialMediaLink.objects.first()  # Assuming there's only one instance
#     context = {
#         'info': info, 
#         'working_hours': working_hours,
#         }

#     # Render the response and send it back!
#     return render(request, 'home.html', context)

def about(request):
    a_display= AboutPage.objects.first()
    about_list = AboutList.objects.all()
    context = {
        "user":request.user,
        'about': a_display,
        'about_list': about_list,
        }
    return render(request, 'about.html', context)

