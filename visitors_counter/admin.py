from django.contrib import admin
from .models import Visit

class VisitAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'ip_address','visit_count',)
    search_fields = ('ip_address',)
    ordering = ('-timestamp',)

# Register the Visit model with the admin site
admin.site.register(Visit, VisitAdmin)