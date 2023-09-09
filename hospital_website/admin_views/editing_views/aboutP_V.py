from django.shortcuts import render, redirect, get_object_or_404
from ...forms.aboutP_F import AboutPageForm, AboutListForm
from ...models.aboutP_M import *
def about_page_edit(request):
    # Get the existing home page instance or create a new one if it doesn't exist
    try:
        about_page = AboutPage.objects.first()
    except AboutPage.DoesNotExist:
        about_page = AboutPage() 
    if request.method == 'POST':
        form = AboutPageForm(request.POST, instance=about_page)
        if form.is_valid():
            form.save()
            return redirect('about_page_view')  # Replace 'about_page' with the actual URL name
    else:
        form = AboutPageForm(instance=about_page)

    return render(request, 
        'maindashboard/about_page/about_page_template.html', 
        {'form': form}
        )
def about_list_edit(request, pk=None):
    # If item_id is provided, get the item to edit, otherwise, create a new item
    if pk is not None:
        item = get_object_or_404(AboutList, pk=pk)
        image= item.image #
    else:
        item = None 
        image= None
    if request.method == 'POST':
        form = AboutListForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('about_page_view')  # Replace 'about_page' with the actual URL name for your about page
    else:
        form = AboutListForm(instance=item)
    
        context={
            'form': form,
            'image': image
            }

    return render(request, 'maindashboard/about_page/about_list_template.html', context)
# def about_list_edit(request):
#     if request.method == 'POST':
#         form = AboutListForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('about_page_view')  # Replace 'about_list' with the actual URL name
#     else:
#         form = AboutListForm()

#     return render(request, 
#         'maindashboard/about_page/about_list_template.html', 
#         {'form': form}
#         )
