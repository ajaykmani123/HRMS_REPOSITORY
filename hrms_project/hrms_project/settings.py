"""
Django settings for hrms_project project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0^uf$ncl^q&^-^%$gquf!84c&v%=%a1&j94pww++7g6dwd0z0('

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

# ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ["35.225.224.226", "127.0.0.1"]
ALLOWED_HOSTS = ["34.58.114.68"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_app',
    'employee_app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hrms_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'hrms_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Scorpiq_Database',
        'USER': 'postgres',
        'PASSWORD': 'Ajay@2001',
        'HOST': 'db',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Add the following to make Django aware of your static files directory

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# BASE_DIR / "employee_app/static",  # Path to employee app's static directory
#
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# media configuration

import os

# MEDIA_URL and MEDIA_ROOT settings
MEDIA_URL = '/media/'  # URL prefix for serving media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Folder where media files are stored





# settings.py

AUTHENTICATION_BACKENDS = [
    'employee_app.backends.EmailBackend',  # Add your custom backend here
    'django.contrib.auth.backends.ModelBackend',  # Default backend (you can keep it as fallback)
]




# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ajaykmani2001@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'ubwehjqorupodwsq'  # Replace with your app password
DEFAULT_FROM_EMAIL = 'ajaykmani2001@gmail.com'



# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



import os

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),  # Ensure this exists
# ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For collectstatic
