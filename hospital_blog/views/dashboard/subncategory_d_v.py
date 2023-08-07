
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from ...models.categories_n_babies_m import *
from ...forms.category_n_babies_f import *
@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blogdashboard/category/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    print('In category')
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        print('In category ........')
        if form.is_valid():
            category = form.save(commit=False)
            print('In category =========')
            if form.cleaned_data['approved']:
                category.date_approved = timezone.now()
            category.save()
            messages.success(request, 'Category created successfully')
            return redirect('blog:category_create') 
        else:
            errors=form.errors()
            print(errors)
    else:
        form = CategoryForm()
    return render(request, 'blogdashboard/category/write_category.html', {'form': form})

@login_required
def category_edit(request, id):
    category = get_object_or_404(Category,  id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            if form.cleaned_data['approved']: 
                category.date_approved = timezone.now()
            form.save()
            messages.success(request, 'Category updated successfully')
            return redirect('blog:category_create')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'blogdashboard/category/write_category.html', {'form': form})

# #@login_required
# def category_delete(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     if request.method == 'POST':
#         category.delete()
#         messages.success(request, 'Category deleted successfully')
#         return redirect('category_list')
#     return render(request, 'category_delete.html', {'category': category})

# @login_required
def subcategory_list(request):
    subcategories = Subcategory.objects.all()
    return render(request, 'blogdashboard/subcategory/subcategory_list.html', {'subcategories': subcategories})
@login_required
def subcategory_create(request):
    categories = Category.objects.all()  # Retrieve all categories
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            subcategory = form.save(commit=False)
            if form.cleaned_data['approved']:
                subcategory.date_approved = timezone.now()
            subcategory.save()
            messages.success(request, 'Subcategory created successfully')
            return redirect('blog:subcategory_create')
    else:
        form = SubcategoryForm()
    return render(request, 'blogdashboard/subcategory/write_subcategory.html', {'form': form, 'category': categories})

@login_required
def subcategory_edit(request, id):
    subcategory = get_object_or_404(Subcategory, id=id)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            subcategory = form.save(commit=False)
            if form.cleaned_data['approved']:
                subcategory.date_approved = timezone.now()
            subcategory.save()
            messages.success(request, 'Subcategory updated successfully')
            return redirect('blog:subcategory_create')
    else:
        form = SubcategoryForm(instance=subcategory)
    return render(request, 'blogdashboard/subcategory/write_subcategory.html', {'form': form})

# @login_required
# def subcategory_delete(request, slug):
#     subcategory = get_object_or_404(Subcategory, slug=slug)
#     if request.method == 'POST':
#         subcategory.delete()
#         messages.success(request, 'Subcategory deleted successfully')
#         return redirect('subcategory_list')
#     return render(request, 'subcategory_delete.html', {'subcategory': subcategory})

