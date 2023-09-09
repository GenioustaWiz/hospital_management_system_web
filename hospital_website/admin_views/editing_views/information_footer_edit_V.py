from django.shortcuts import render, redirect
from ...forms.information_footer_F import *
from ...models.information_footer_M import *
from django.forms import inlineformset_factory

def create_top_footer(request, pk=None):
    HeadingFormSet = inlineformset_factory(TopFooterHeading, TopFooterContent, form=TopFooterContentForm,)
    
    
    if request.method == 'POST':
        heading_form = TopFooterHeadingForm(request.POST, prefix='heading')
        formset = HeadingFormSet(request.POST, instance=TopFooterHeading(), prefix='content')
        print('======================------------headingformset-----------================')
        print(formset)
        if heading_form.is_valid() and formset.is_valid():
            heading = heading_form.save(commit=False)
            heading.save()  # Save the heading instance first
            instances = formset.save(commit=False)
            for instance in instances:
                print('==============Instances================')
                instance.heading = heading
                print(instance)
                instance.save()
            formset.save_m2m()  # Save many-to-many relationships if any
            return redirect('top_footer_view')  # Replace 'success_url' with the URL to redirect after successful submission
    else:
        heading_form = TopFooterHeadingForm(prefix='heading')
        formset = HeadingFormSet(instance=TopFooterHeading(), prefix='content')
    total_form_count = formset.total_form_count()  # Calculate the total number of forms
    return render(request, 'maindashboard/information_footer/create_top_footer_content.html', {
        'form_h': heading_form,
        'content_item_formset': formset,
        'total_form_count': total_form_count,  # Pass the total count to the JS for table indexing during creation
    })
    
def create_top_footer_content(request, pk=None):
    if request.method == 'POST':
        # form = TopFooterContentForm(request.POST)
        form_h =TopFooterHeadingForm(request.POST)
        content_item_formset = ContentItemForm(request.POST, prefix='content_items')
        print('================================helloo')
        if form_h.is_valid() and content_item_formset.is_valid():
            print("hello========================")
            heading_text = form_h.save(commit=False)
            heading_text = form_h.cleaned_data['heading']
            
            # Create a new TopFooterHeading instance or retrieve an existing one
            heading_instance, created = TopFooterHeading.objects.get_or_create(heading=heading_text)
            for form in content_item_formset:
                content_instance = form.save(commit=False)
                content_text = form.cleaned_data['content']
                url = form.cleaned_data['url']
                
                content_instance.heading = heading_instance
                content_instance.content = content_text
                content_instance.url = url
                content_instance.save()
            return redirect('top_footer_view')  # Redirect to a success page
    else:
        # form = TopFooterContentForm()
        form_h =TopFooterHeadingForm()
        content_item_formset = ContentItemForm(prefix='content_items')
    return render(request, 'maindashboard/information_footer/create_top_footer_content.html',
                  {
                    # 'form': form,
                   'form_h': form_h,
                    'content_item_formset': content_item_formset,
                   }
                  )
def add_top_footer_content(request, pk=None):
    if request.method == 'POST': 
        top_footer_content_form = TopFooterHeadingForm(request.POST)
        content_item_formset = ContentItemForm(request.POST, prefix='content_items')

        if top_footer_content_form.is_valid() and content_item_formset.is_valid():
            top_footer_content = top_footer_content_form.save()
            for form in content_item_formset:
                content_item = form.save(commit=False)
                content_item.top_footer_content = top_footer_content
                content_item.save()
            return redirect('view_top_footer_content')
    else:
        top_footer_content_form = TopFooterHeadingForm()
        content_item_formset = ContentItemForm(prefix='content_items')

    return render(request, 'maindashboard/information_footer/create_top_footer_content.html', {
        'top_footer_content_form': top_footer_content_form,
        'content_item_formset': content_item_formset,
    })

def create_top_footer_heading(request):
    if request.method == 'POST':
        form = TopFooterHeadingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with the appropriate URL
    else:
        form = TopFooterHeadingForm()
    
    return render(request,
        'maindashboard/information_footer/create_top_footer_heading.html',
        {'form': form}
    )

# def create_top_footer_content(request):
#     if request.method == 'POST':
#         form = TopFooterContentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Replace 'home' with the appropriate URL
#     else:
#         form = TopFooterContentForm()
    
#     return render(request,
#         'maindashboard/information_footer/create_top_footer_content.html', 
#         {'form': form}
#     )

def create_social_media_links(request):
    if request.method == 'POST':
        form = SocialMediaLinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with the appropriate URL
    else:
        form = SocialMediaLinkForm()
    
    return render(request, 
        'maindashboard/information_footer/create_social_media_links.html', 
        {'form': form}
        )
