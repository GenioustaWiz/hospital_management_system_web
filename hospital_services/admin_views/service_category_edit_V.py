from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from ..models import ServiceCategory, ServiceOffered
from ..forms import ServiceCategoryForm, ServiceOfferedForm,ServiceOfferedFormSet

def create_services_category(request, pk=None):
    # Check if a primary key (pk) is provided in the URL to determine if we are editing an existing instance
    if pk:
        category = get_object_or_404(ServiceCategory, pk=pk)
        foredit = pk
    else:
        category = ServiceCategory()
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
            else:
                category = ServiceCategory.objects.get(id=selected_category)
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
        'edit_mode': pk is not None,  # True if in edit mode, False if in create new mode
    }
    return render(request, 'maindashboard/services/create_services.html', context)

# def create_services(request):
#     # Define categories outside of the if-else block
#     categories = ServiceCategory.objects.all()
#     if request.method == 'POST':
#         category_form = ServiceCategoryForm(request.POST, prefix='main')
#         formset = ServiceOfferedFormSet(request.POST, prefix='content')
        
#         if category_form.is_valid() and formset.is_valid():
            
#             category = category_form.save()
#             print('======================------------formset-----------================')
#             print(formset)
#             instances = formset.save(commit=False)
#             print('======================------------instances-----------================')
#             print(instances)
#             # we use formset.forms coz Instances is blank and can't be used
#             # and if instnces is used no dat will be saved hence sue of formset for iteration
#             for form in formset.forms:
                
#                 if form.is_valid():  # Check if the form has any changes
#                     print('======================------------formset.forms-----------================')
#                     print(form)
#                     instance = form.save(commit=False)
#                     instance.category = category
#                     instance.save()
            
#             return redirect('top_footer_view')  # Redirect to the service list view
#     else:
#         category_form = ServiceCategoryForm(prefix='main')
#         formset = ServiceOfferedFormSet(prefix='content')
#     total_form_count = formset.total_form_count()  # Calculate the total number of forms

#     context={
#         'category_form': category_form,
#         'formset': formset,
#         'total_form_count': total_form_count,
#         'categories': categories,
#     }
#     return render(request, 'maindashboard/services/create_services.html', context)

def category_list(request):
    categories = ServiceCategory.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
