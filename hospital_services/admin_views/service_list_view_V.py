from django.shortcuts import render
from ..models import ServiceCategory

def view_service_categories(request):
    service_categories = ServiceCategory.objects.all()
    context ={
        'service_categories': service_categories
        }
    return render(request, 'maindashboard/services/services_list_view.html', context)
