
from django.urls import path
from .views import *
from .admin_views.service_category_edit_V import *
from .admin_views.serviceoffered_edit_view import *
from .admin_views.service_list_view_V import *

# app_name = 'services'
urlpatterns = [
    path('', services, name='services'),
    path('serives-under/<slug:slug>/', services_offered, name='services_offered'),
    path('serivces-category-list/', view_service_categories, name='view_service_categories'),
    path('category/<int:category_id>/', services_of_category, name='services_of_category'),

    path('create-services-page/', create_services_category, name='create_services_category'),
    path('create-services-page/<int:pk>/', create_services_category, name='create_services_category'),
    path('category-delete/<int:pk>/', category_delete, name='category_delete'),
    
    path('edit-service/<int:pk>/', edit_service_offered, name='edit_service_offered'),
    path('delete-service-offered/<int:pk>/', delete_service_offered, name='delete_service_offered'),   
]