from django.shortcuts import render, redirect

from ...models.models import HomePage
from ...forms.homeP_infor_F import HomePageForm

def edit_home_page(request):
    # Get the existing home page instance or create a new one if it doesn't exist
    try:
        home_page = HomePage.objects.first()
    except HomePage.DoesNotExist:
        home_page = HomePage() 

    if request.method == 'POST':
        form = HomePageForm(request.POST, instance=home_page)
        if form.is_valid():
            form.save()
            return redirect('home_page_view')  # Replace 'home' with the appropriate URL name for your homepage
    else:
        form = HomePageForm(instance=home_page)

    return render(request,
        'maindashboard/home_page/edit_home_page.html',
        {'form': form}
        )
# def edit_home_page(request):
#     if request.method == 'POST':
#         form = HomePageForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home_page_view')  # Redirect to the home page or any other appropriate view
            
#     else:
#         form = HomePageForm()

#     return render(request,
#         'maindashboard/home_page/edit_home_page.html',
#         {'form': form}
#     )
