
from email import message
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from hospital_website.models.models import BaseData, ContactSidebarCompanyInfo
from hospital_website.models.information_footer_M import TopFooterHeading, TopFooterContent, SocialMediaLink
  
# Create your views here.

def contact(request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            phone_number = form.cleaned_data['phone_number']
            phone_no = str(phone_number)  #Convert number to string in order to embed it to body.
            subject = form.cleaned_data['subject']
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phone_no': phone_no,
                'message': form.cleaned_data['message']
            }
            message = '\n'.join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('main_index')
    form = ContactForm()
    side_info = ContactSidebarCompanyInfo.objects.first()
    base = BaseData.objects.first() #for Base.html
    top_footer_headings = TopFooterHeading.objects.all()
    social_media_links = SocialMediaLink.objects.first()  # Assuming there's only one instance
    
    context = {
        'top_footer_headings': top_footer_headings,
        'social_media_links': social_media_links,
        'form': form,
        'side_info': side_info,
        'base': base,
        'company_info': side_info,
    }
    return render(request, 'contact.html', context)
