
from django.urls import path
from .views import *
from .admin_views.service_category_edit_V import *

# app_name = 'services'
urlpatterns = [
    path('', services, name='services'),
    path('create-services-page', create_services, name='create_services'),
]