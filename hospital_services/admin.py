
# admin.py
from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'day', 'time', 'department', 'timestamp')
    list_filter = ('day', 'department', 'timestamp')
    search_fields = ('name', 'email', 'phone', 'department')
    readonly_fields = ('timestamp',)
