
# admin.py
from django.contrib import admin
from .models import *

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'day', 'time', 'department', 'timestamp')
    list_filter = ('day', 'department', 'timestamp')
    search_fields = ('name', 'email', 'phone', 'department')
    readonly_fields = ('timestamp',)

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'cat_description','iconInput')
    search_fields = ('category_name',)

@admin.register(ServiceOffered)
class ServiceOfferedAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'description', 'category')
    list_filter = ('category',)
    search_fields = ('service_name', 'category__category_name')