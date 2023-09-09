from django.shortcuts import render
from ...models.information_footer_M import TopFooterHeading, TopFooterContent, SocialMediaLink

def top_footer_view(request):
    # Retrieve data from the models
    top_footer_headings = TopFooterHeading.objects.all() 
    top_footer_contents = TopFooterContent.objects.all()
    social_media_links = SocialMediaLink.objects.first()  # Assuming there's only one instance

    # Pass the data to the template
    context = {
        'top_footer_headings': top_footer_headings,
        'top_footer_contents': top_footer_contents,
        'social_media_links': social_media_links,
    }

    return render(request, 
        'maindashboard/information_footer/top_footer_view.html', 
        context)
