
"""
Django settings for hospital_management_webapp project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from pathlib import Path
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^6&3vnde7#2_*19h4-#t768*nz$52t=qqflcaad#@ce($e*p*b'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = ['hospitalmanagementsystemweb-production.up.railway.app']

CSRF_TRUSTED_ORIGINS = ['https://hospitalmanagementsystemweb-production.up.railway.app']
# Application definition

INSTALLED_APPS = [
    'users.apps.AccountsConfig',
    'hospital_website',
    'hospital_management',
    'phonenumber_field',
    'django_countries',
    'contact_us',
    'hospital_services',
    'hospital_blog',
    'django_cleanup', # overrides older images
    """"""
    # for changing adm,in app  side..pip install django-admin-soft-dashboard
    # 'admin_soft.apps.AdminSoftDashboardConfig',
    # pip install django-admin-material-dashboard
    # 'admin_material.apps.AdminMaterialDashboardConfig',
    """"""
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party Apps.
    'django_filters',
    'rest_framework',
    'taggit',
    'debug_toolbar',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # New Added
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


ROOT_URLCONF = 'hospital_management_webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hospital_management_webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Directory where uploaded media is saved.
MEDIA_URL = '/media/' # Public URL at the browser

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "main_index" #afterlogin
LOGOUT_REDIRECT_URL = "main_index"

# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))