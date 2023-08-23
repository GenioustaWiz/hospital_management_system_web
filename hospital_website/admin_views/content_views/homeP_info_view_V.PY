from django.shortcuts import render
from ...models.models import HomePage

def home_page(request):
    try:
        home_page = HomePage.objects.first()
    except HomePage.DoesNotExist:
        home_page = None

    return render(request, 
        'maindashboard/home_page/homepage_infor.html',
        {'home_page': home_page}
    )
