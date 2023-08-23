
from django.urls import path
from .views import *
from .admin_views.dashboard_home_V import *
from .admin_views.editing_views.homeP_infor_edit_V import *
from .admin_views.editing_views.homeP_cards_edit_V import *
from .admin_views.editing_views.aboutP_V import *
from .admin_views.editing_views.ContactSidebarCompanyInfo_edit_V import *
from .admin_views.editing_views.information_footer_edit_V import *
# from .admin_views.content_views.

urlpatterns = [
    path('', main_index, name='main_index'),
    # path('projects/', projects, name='projects'),
    path('about/', about, name='about'),
]

# ++++++++++++ Ulrs for Main Admin +++++++++++++++++
urlpatterns += [
    path('main-dashboard/', main_dashboard_home, name='main_dashboard_home'),
    # ===============EDIT HOMEPAGE CONTENT===============
    path('edit-home-page/', edit_home_page, name='edit_home_page'),
    path('front-page-card1/', home_page_card1_form, name='home_page_card1_form'),
    path('working-hours/', working_hours_form, name='working_hours_form'),
    path('front-page-card3/', home_page_card3_form, name='home_page_card3_form'),
    
    # ==========EDIT ABOUT PAGE CONTENT=========;
    path('about-page/', about_page_edit, name='about_page'),
    path('about-list/', about_list_edit, name='about_list'),
    # ==========EDIT COMPANY CONTACT INFORMATION======================
    path('edit-company_contact-info/', edit_company_contact_info, name='edit_company_contact_info'),
    # ============= TOP FOOTER INFORMATION EDIT===========
    path('create_top_footer_heading/', create_top_footer_heading, name='create_top_footer_heading'),
    path('create_top_footer_content/', create_top_footer_content, name='create_top_footer_content'),
    path('create_social_media_links/', create_social_media_links, name='create_social_media_links'),
]
