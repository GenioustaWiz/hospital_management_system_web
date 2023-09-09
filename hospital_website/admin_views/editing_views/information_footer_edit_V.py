from django.shortcuts import render, redirect
from ...forms.information_footer_F import *
from ...models.information_footer_M import *
from django.forms import inlineformset_factory

def create_top_footer(request, pk=None):
    HeadingFormSet = inlineformset_factory(TopFooterHeading, TopFooterContent, form=TopFooterContentForm, extra=0,)
    
    
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
