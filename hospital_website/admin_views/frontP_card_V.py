from django.shortcuts import render, redirect
from ..forms.frontP_card_F import FrontPageCard1Form, WorkingHoursForm, FrontPageCard3Form

def front_page_card1_form(request):
    if request.method == 'POST':
        form = FrontPageCard1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with the name of your success page
    else:
        form = FrontPageCard1Form()
    
    return render(request, 'front_page_card1_form.html', {'form': form})

def working_hours_form(request):
    if request.method == 'POST':
        form = WorkingHoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with the name of your success page
    else:
        form = WorkingHoursForm()
    
    return render(request, 'working_hours_form.html', {'form': form})

def front_page_card3_form(request):
    if request.method == 'POST':
        form = FrontPageCard3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success' with the name of your success page
        # If form is not valid, display errors
    else:
        form = FrontPageCard3Form()
    
    return render(request, 'front_page_card3_form.html', {'form': form})
