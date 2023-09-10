
from django.contrib import admin
from .models.models import *
from .models.information_footer_M import *
from .models.aboutP_M import *
from .models.homeP_cards_M import *

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
    list_display = ('id', 'title', 'image')
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

class HomePageCard1_Admin(admin.ModelAdmin):
    list_display = ('id', 'heading','body','color','iconInput')
    list_display_links = ('heading',) 
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
admin.site.register(HomePageCard1, HomePageCard1_Admin)

class workinghours_Admin(admin.ModelAdmin):
    list_display = ('id', 'day','opening_time','closing_time')
    list_display_links = ('day',) 
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
admin.site.register(WorkingHours, workinghours_Admin)
class HomePageCard3_Admin(admin.ModelAdmin):
    list_display = ('id', 'heading','body','color','iconInput')
    list_display_links = ('heading',) 
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
admin.site.register(HomePageCard3, HomePageCard3_Admin)


class TopFooterContentInline(admin.TabularInline):
    model = TopFooterContent
    #this will enable the list under the specific heading to be enterd together

class TopFooterHeadingAdmin(admin.ModelAdmin):
    inlines = [TopFooterContentInline]

class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'facebook_link', 'whatsapp_link', 'linkedIn_link', 'twitter_link')

admin.site.register(TopFooterHeading, TopFooterHeadingAdmin)
admin.site.register(SocialMediaLink, SocialMediaLinkAdmin)