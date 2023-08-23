from django.shortcuts import render, redirect
from ...forms.information_footer_F import TopFooterHeadingForm, TopFooterContentForm, SocialMediaLinkForm
from ...models.information_footer_M import TopFooterHeading, TopFooterContent, SocialMediaLink

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

def create_top_footer_content(request):
    if request.method == 'POST':
        form = TopFooterContentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with the appropriate URL
    else:
        form = TopFooterContentForm()
    
    return render(request,
        'maindashboard/information_footer/create_top_footer_content.html', 
        {'form': form}
    )

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
