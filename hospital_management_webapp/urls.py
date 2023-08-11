
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Admin Customization
admin.site.site_header = "Login to CDT"
admin.site.site_title = "Welcome to CDT Dashboard"
admin.site.index_title = "Welcome to this Portal"
urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include('hospital_website.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    # path('hospital_management/', include('hospital_management.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('services/', include('hospital_services.urls')),
    path('news/', include('hospital_blog.urls')),

]

# if settings.DEBUG:# Only add this when we in debug mode
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# else:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
