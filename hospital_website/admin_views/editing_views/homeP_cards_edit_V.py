from django.shortcuts import render, redirect
from ...forms.homeP_cards_F import HomePageCard1Form, WorkingHoursForm, HomePageCard3Form

def home_page_card1_form(request):
    if request.method == 'POST':
        form = HomePageCard1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with the name of your success page
    else:
        form = HomePageCard1Form()
    
    return render(request,
        'maindashboard/home_page/home_page_card1_form.html',
        {'form': form}
    )

def working_hours_form(request):
    if request.method == 'POST':
        form = WorkingHoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with the name of your success page
    else:
        form = WorkingHoursForm()
    
    return render(request,
        'maindashboard/home_page/working_hours_form.html',
        {'form': form}
    )

def home_page_card3_form(request):
    if request.method == 'POST':
        form = HomePageCard3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with the name of your success page
        # If form is not valid, display errors
    else:
        form = HomePageCard3Form()
    
    return render(request,
        'maindashboard/home_page/home_page_card3_form.html',
        {'form': form}
    )
