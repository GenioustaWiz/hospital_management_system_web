from django import forms
from ..models.information_footer_M import TopFooterHeading, TopFooterContent, SocialMediaLink

class TopFooterHeadingForm(forms.ModelForm):
    class Meta:
        model = TopFooterHeading
        fields = ['heading']

class TopFooterContentForm(forms.ModelForm):
    class Meta:
        model = TopFooterContent
        fields = ['heading', 'content', 'url']

class SocialMediaLinkForm(forms.ModelForm):
    class Meta:
        model = SocialMediaLink
        fields = ['facebook_link', 'whatsapp_link', 'linkedIn_link', 'twitter_link']
