from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import ServiceOffered
from ..forms import ServiceOfferedForm  # Create a form for editing

def edit_service_offered(request, pk):
    service = get_object_or_404(ServiceOffered, pk=pk)

    if request.method == 'POST':
        form = ServiceOfferedForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('services_of_category', category_id=service.category.id)  # Redirect to category services
    else:
        form = ServiceOfferedForm(instance=service)
    context={
        'form': form, 
        'service': service,
        }
    return render(request, 'maindashboard/services/edit_service_offered.html', context)

def delete_service_offered(request, pk):
    print('Am in================================')
    service_offered = get_object_or_404(ServiceOffered, pk=pk)
    service_offered.delete()
    messages.success(request, 'The service_offered was Deleted successfully!')
    # return redirect('create_services_category')
    # Get the previous URL (referer)
    previous_url = request.META.get('HTTP_REFERER')

    if previous_url:
        return redirect(previous_url)
    else:
        # Handle the case where there's no previous URL
        return HttpResponse("Previous URL not available")
