
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


from ..models.comments_m import *
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        # labels = {
        #     'name': 'Your name',
        #     'email': 'Your email address',
        #     'content': 'Your comment'
        # }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        comment = super().save(commit=False)
        user = None
        if self.cleaned_data['name']:
            user_model = get_user_model()
            try:
                user = user_model.objects.get(username=self.cleaned_data['name'])
            except user_model.DoesNotExist:
                pass
        comment.user = user
        if commit:
            comment.save()
        return comment


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['name', 'email', 'content']