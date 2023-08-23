from django.shortcuts import render, redirect
from ...forms.aboutP_F import AboutPageForm, AboutListForm

def about_page_edit(request):
    if request.method == 'POST':
        form = AboutPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about_page')  # Replace 'about_page' with the actual URL name
    else:
        form = AboutPageForm()

    return render(request, 
        'maindashboard/about_page/about_page_template.html', 
        {'form': form}
        )

def about_list_edit(request):
    if request.method == 'POST':
        form = AboutListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about_list')  # Replace 'about_list' with the actual URL name
    else:
        form = AboutListForm()

    return render(request, 
        'maindashboard/about_page/about_list_template.html', 
        {'form': form}
        )
