from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from hospital_website.models.models import BaseData, ContactSidebarCompanyInfo
from .models import Profile
# Import User UpdateForm, ProfileUpdatForm
from .forms import *

# @login_required
# def profile_home(request):
#     return render(request, 'profile/profile_home2.html',)
def Login(request):
    if request.method == 'POST':
        form = loginpage(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
            # return redirect('home')

    
    form = loginpage()
    side_info = ContactSidebarCompanyInfo.objects.first()
    base = BaseData.objects.first() #for Base.html
    context = {
        'form': form,
        'base': base,
        'side_info': side_info,
    }
    return render(request, 'registration/login.html', context)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Your account has been created! You are now able to log in') 
            return redirect('login')
    else:
        form = UserRegisterForm()
        side_info = ContactSidebarCompanyInfo.objects.first()
        base = BaseData.objects.first() #for Base.html
        context = {
            'base': base,
            'form': form,
            'side_info': side_info,
        }
    return render(request, 'registration/register.html', context)

# Update it here
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save() 
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        side_info = ContactSidebarCompanyInfo.objects.first()
        base = BaseData.objects.first() #for Base.html
        # user_profile = Profile()
    context = {
        'base': base,
        'u_form': u_form,
        'p_form': p_form,
        # 'user_profile': user_profile,
    }

    return render(request, 'profile/profile_home2.html', context)
