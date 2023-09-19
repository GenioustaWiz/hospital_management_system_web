
from django.urls import path
from .views import *
from .admin_views.service_category_edit_V import *
from .admin_views.service_list_view_V import *

# app_name = 'services'
urlpatterns = [
    path('', services, name='services'),
    path('serivces-category-list/', view_service_categories, name='view_service_categories'),
    path('create-services-page/', create_services_category, name='create_services_category'),
    path('create-services-page/<int:pk>/', create_services_category, name='create_services_category'),
]