from multiprocessing import context
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from hospital_website.models.models import BaseData, ContactSidebarCompanyInfo
from .models import Profile
# Import User UpdateForm, ProfileUpdatForm
from .forms import *
from hospital_website.models.information_footer_M import TopFooterHeading, TopFooterContent, SocialMediaLink
  

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
    
    context = {
        'form': form,
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
    
    context = {
        'form': form,
        'side_info': side_info,
        }
    return render(request, 'registration/register.html', context)

# Update it here
@login_required
def profile(request):
    user = request.user
    print(user)
     # Check if a profile exists for the user, or create one if it doesn't exist
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        # Create a default or empty profile for the user
        profile = Profile.objects.create(user=user)

    # profile = request.user.profile  # Access the user's profile
    full_name = f"{profile.user.first_name} {profile.user.last_name}" if profile.user.first_name or profile.user.last_name else "None"

    # Create a dictionary to hold the profile data with "None" for empty fields
    profile_data = {
        
        'Title': profile.title,
        'Name': full_name, #profile.user.first_name,
        'Email': profile.user.email,
        'Phone Number': profile.phone_number,
        'Country': profile.country,
        'Description': profile.desc,
        
    }
    # Replace empty fields with "None"
    for key, value in profile_data.items():
        if not value:
            profile_data[key] = "None"
    context = {
        'profile_data': profile_data,
        'profile': profile,
        # 'user_profile': user_profile,
    }

    return render(request, 'profile/profile_view.html', context)

def profile_edit( request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        # Create a default or empty profile for the user
        profile = Profile.objects.create(user=user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        desc_form =  ProfileUpdateForm_desc(request.POST, instance=profile)
        if u_form.is_valid() and p_form.is_valid() and desc_form.is_valid():
            u_form.save()
            p_form.save() 
            desc_form.save()  # Save the description form
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        desc_form =  ProfileUpdateForm_desc(instance=profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'desc_form': desc_form,
        'profile': profile,
    }

    return render(request, 'profile/profile_edit.html', context) 