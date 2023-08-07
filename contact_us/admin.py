
from django.contrib import admin
from .models import *
# Register your models here.
class contact_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'subject', 'message')
    list_filter = ('subject',)
    search_fields = ('subject', 'email') #
    list_display_links = ('name',) 
    list_per_page = 10
    search_help_text = 'Search the messages according to subject or email'
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
admin.site.register(contact, contact_Admin)