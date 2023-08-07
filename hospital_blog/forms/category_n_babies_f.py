
from django import forms
from django.forms import TextInput, FileInput
from ..models.categories_n_babies_m import *

class CategoryForm(forms.ModelForm): 
    class Meta:
        model = Category
        fields = ['name', 'image', 'approved']
        widgets = {
            'name': TextInput(attrs={
                                     'name': "category-name",
                                     'class': "form-control",
                                     'placeholder': "Enter Category Name",
                                     'id': "categoryname"
                                     }),
            'image': FileInput(attrs={
                                        "class": "form-control clearablefileinput",
                                        "type": "file",
                                        "id": "categoryImage",
                                        "name": "category-image"
                                      }

                               ),
        }


class SubcategoryForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(approved=True),
        widget=forms.Select(attrs={
            "class": "form-control selectpicker",
            "type": "text",
            "name": "article-category",
            "id": "subcategoryCategory",
            "data-live-search": "true"
        }),
        # ment to send slug instead of id. but it has so many disadvantages.
        # to_field_name='slug' 
        
    )
    class Meta:
        model = Subcategory
        fields = ['name', 'category', 'approved']

        widgets = {
            'name': TextInput(attrs={
                                     'name': "subcategoryname",
                                     'class': "form-control",
                                     'placeholder': "Enter Subcategory name",
                                     'id': "subcategoryname"
                                     }),

        }