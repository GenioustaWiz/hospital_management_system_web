from django.shortcuts import render, get_object_or_404
from ..models import ServiceCategory

def view_service_categories(request):
    service_categories = ServiceCategory.objects.all()
    context ={
        'service_categories': service_categories,
        }
    return render(request, 'maindashboard/services/services_category_list_view.html', context)

def services_of_category(request, category_id):
    category = get_object_or_404(ServiceCategory, pk=category_id)
    services = category.serviceoffered_set.all()
    context={
        'category': category, 
        'services': services,
        }
    return render(request, 'maindashboard/services/services_of_category_view.html', context)
