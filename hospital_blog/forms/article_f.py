
from django import forms
from django.forms import TextInput, Select, FileInput, CharField
from tinymce.widgets import TinyMCE
from ..models.article_m import Blog, Category, Subcategory

class BlogForm(forms.ModelForm): 
    category = forms.ModelChoiceField(queryset=Category.objects.filter(approved=True),
                                      empty_label="Inactive", #REMOVE THIS ONE FOR MY BLOG
                                      widget=forms.Select(attrs=
                                                          {
                                                              "class": "form-control selectpicker",
                                                              "type": "text",
                                                              "name": "article-category",
                                                              "id": "articleCategory",
                                                              "data-live-search": "true"
                                                          }
                                      ),
                                    #   ADD THIS INORDER TO LOAD THE SLUG AS THE VALUE OF THE OPTIONS FIELD
                                    #   to_field_name='slug',
                                      label='Category',
                                      required=True
                                    )
    
    
    subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.filter(
                                      approved=True),
                                      empty_label="Click to select", #REMOVE THIS ONE FOR MY BLOG
                                      widget=forms.Select(attrs=
                                                          {
                                                              "class": "form-control selectpicker",
                                                              "type": "text",
                                                              "name": "article-subcategory",
                                                              "id": 'articleSubcategory',
                                                              "data-live-search": "true"
                                                          }
                                      ),
                                    #   to_field_name='slug',
                                    label='Subcategory',
                                    required=True

                                    )

    content =  forms.CharField(widget=TinyMCE ()) #tinymce Editor.
    rejection_reason = forms.CharField(widget=TinyMCE (), required=False )
    class Meta:
        # Article status constants
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # CHOICES
        STATUS_CHOICES = (
            (DRAFTED, 'Draft'),
            (PUBLISHED, 'Publish'),
        )
        
        model = Blog
        fields = ['title', 'content', 'image', 'image_credit', 
                  'category', 'subcategory', 'tags', 'approved', 
                  'rejected', 'rejection_reason' , 'status'
                  ]
        
        widgets = {
            'title': TextInput(attrs={
                                     'name': "article-title",
                                     'class': "form-control",
                                     'placeholder': "Enter Article Title",
                                     'id': "articleTitle"
                                     }),

            'image': FileInput(attrs={
                                        "class": "form-control clearablefileinput",
                                        "type": "file",
                                        "id": "articleImage",
                                        "name": "article-image"
                                      }

                               ),

            'image_credit': TextInput(attrs={
                'name': "image_credit",
                'class': "form-control",
                'placeholder': "Example: made4dev.com (Premium Programming T-shirts)",
                'id': "image_credit"
            }),

            # 'content': forms.CharField(widget=CKEditorWidget(config_name="default", attrs={
            #            "rows": 5, "cols": 20,
            #            'id': 'content',
            #            'name': "article_content",
            #            'class': "form-control",
            #            })),

            'tags': TextInput(attrs={
                                     'name': "tags",
                                     'class': "form-control tag-input",
                                     'placeholder': "Example: sports, game, politics",
                                     'id': "tags",
                                     'data-role': "tagsinput"
                                     }),

            
            'status': Select(choices=STATUS_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "status", "type": "text",
                                 "id": "articleStatus",
                                 "data-live-search": "true",
                                 "title": "Select Status"
                             }
                             ),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.category:
            self.fields['category'].queryset = Category.objects.filter(approved=True)
            self.fields['category'].widget.choices.field.to_field_name = 'id'
            self.fields['category'].initial = instance.category.name