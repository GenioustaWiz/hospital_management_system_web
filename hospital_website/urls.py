
from django.urls import path
from .views import *
from .admin_views.frontP_card_V import *
urlpatterns = [
    path('', main_index, name='main_index'),
    # path('projects/', projects, name='projects'),
    path('about/', about, name='about'),
]

# ++++++++++++ Ulrs for Main Admin +++++++++++++++++
urlpatterns += [
    path('front-page-card1/', front_page_card1_form, name='front_page_card1_form'),
    path('working-hours/', working_hours_form, name='working_hours_form'),
    path('front-page-card3/', front_page_card3_form, name='front_page_card3_form'),
]