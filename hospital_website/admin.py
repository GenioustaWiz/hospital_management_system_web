
from django.contrib import admin
from .models.models import *
from .models.information_footer_M import *
from .models.aboutP_M import *
from .models.frontP_card_M import *

# Register your models here.

class hp_Admin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'body',)
    list_display_links = ('heading',) 
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
admin.site.register(HomePage, hp_Admin)
class base_Admin(admin.ModelAdmin):
    list_display = ('id', 'logo_name', 'footer',)
    list_display_links = ('logo_name',) 
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
admin.site.register(BaseData, base_Admin)

class about_Admin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'body',)
    list_display_links = ('heading',) 
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
admin.site.register(AboutPage, about_Admin)

class abtList_Admin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',) 
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
admin.site.register(AboutList, abtList_Admin)

class contactsideinfo_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email', 'address')
    list_display_links = ('name',) 
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
admin.site.register(ContactSidebarCompanyInfo, contactsideinfo_Admin)

class FrontPageCard1_Admin(admin.ModelAdmin):
    list_display = ('id', 'heading','body','color','iconInput')
    list_display_links = ('heading',) 
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
admin.site.register(FrontPageCard1, FrontPageCard1_Admin)

class workinghours_Admin(admin.ModelAdmin):
    list_display = ('id', 'day','opening_time','closing_time')
    list_display_links = ('day',) 
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
admin.site.register(WorkingHours, workinghours_Admin)
class FrontPageCard3_Admin(admin.ModelAdmin):
    list_display = ('id', 'heading','body','color','iconInput')
    list_display_links = ('heading',) 
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
admin.site.register(FrontPageCard3, FrontPageCard3_Admin)