from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from ..models import ServiceCategory, ServiceOffered
from ..forms import ServiceCategoryForm, ServiceOfferedForm,ServiceOfferedFormSet

def create_services_category(request, pk=None):
    # Check if a primary key (pk) is provided in the URL to determine if we are editing an existing instance
    if pk:
        category = get_object_or_404(ServiceCategory, pk=pk)
        edit_mode = True  # Enable edit mode
        category_id = pk
    else:
        category = ServiceCategory()
        edit_mode = False  # Disable edit mode
        category_id = None
    # Define categories outside of the if-else block
    categories = ServiceCategory.objects.all()
    if request.method == 'POST':
        category_form = ServiceCategoryForm(request.POST, instance=category, prefix='main')
        formset = ServiceOfferedFormSet(request.POST, instance=category, prefix='content')
        # Get the selected category value from the form data
        selected_category = request.POST.get('category')

        if category_form.is_valid() and formset.is_valid():
            # Check if the selected category is an existing category or a new one
            if selected_category == 'add_new':
                category = category_form.save()
            elif selected_category is not None:
                category = ServiceCategory.objects.get(id=selected_category)
                print('======================------------selected Category-----------================')
                print(category)
            else:
                category = ServiceCategory.objects.get(id=pk)
                print('======================------------selected Category-----------================')
                print(category)
            print('======================------------formset-----------================')
            print(formset)
            # we use formset.forms coz Instances is blank and can't be used
            # and if instnces is used no dat will be saved hence sue of formset for iteration
            for form in formset.forms:
                
                if form.is_valid():  # Check if the form has any changes
                    print('======================------------formset.forms-----------================')
                    print(form)
                    instance = form.save(commit=False)
                    instance.category = category
                    instance.save()
                
            return redirect('view_service_categories')  # Redirect to the service list view
    else:
        category_form = ServiceCategoryForm(instance=category, prefix='main')
        formset = ServiceOfferedFormSet(instance=category, prefix='content')
    total_form_count = formset.total_form_count()  # Calculate the total number of forms

    context={
        'category_form': category_form,
        'formset': formset,
        'total_form_count': total_form_count,
        'categories': categories, 
        'edit_mode': edit_mode,
        'category_id': category_id,
    }
    return render(request, 'maindashboard/services/create_services.html', context)
@login_required
def category_delete(request, pk):
    category = get_object_or_404(ServiceCategory, pk=pk)
    category.delete()
    messages.success(request, 'The Category and its services were Deleted successfully!')
    # return redirect('view_service_categories')
    # Get the previous URL (referer)
    previous_url = request.META.get('HTTP_REFERER')

    if previous_url:
        return redirect(previous_url)
    else:
        # Handle the case where there's no previous URL
        return HttpResponse("Previous URL not available")

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
