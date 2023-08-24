from django.shortcuts import render
from ...models.models import HomePage
from ...models.homeP_cards_M import *
def home_page_view(request):
    try:
        home_page = HomePage.objects.first()
        card1 = HomePageCard1.objects.first()
        workinghours = WorkingHours.objects.first()
        card3 = HomePageCard3.objects.first()
    except HomePage.DoesNotExist:
        home_page = None
        card1 = None
        workinghours = None
        card3 = None
    context ={
        'home_page': home_page,
        'card1' : card1,
        'card3' : card3,
        'workinghours' : workinghours,
        }
    return render(request, 
        'maindashboard/home_page/homepage_infor.html',
        context
    )
