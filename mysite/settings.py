"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/

"""

# import os
# from pathlib import Path
# import ssl


import os
from pathlib import Path
# import pymongo
# import ssl
# from pymongo import MongoClient

STRIPE_SECRET_KEY = 'sk_test_51NTsCzSCN1dWKbv0yoIRmSWwueY3KwaeuODKYqFKZUBXSTMbBnRatULoLSujTX7O0LksbmXJcuYC90ZplJKJyA9H00ivOg6Ofo'
STRIPE_PUBLISHABLE_KEY = 'pk_test_51NTsCzSCN1dWKbv0C0IPF1XgF8bWJNnLYHb4Zkx3aol5qKwM5aayGnSctOMi098rHXNXZ4dhfOUrkPtxmFORFuiB00nDK4iF1u'

# Set session cookie age (in seconds)
SESSION_COOKIE_AGE = 60 * 60  # 60 minutes

# Set session expiration age (in seconds)
SESSION_EXPIRE_SECONDS = 60 * 60  # 60 minutes

# Set session engine to use Djongo
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i0$^9o7v(tq=8%@0+)9(5oc$6bw1^*pjm7&%ggd0cd#360pr=#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

STATIC_TEMPLATE_TAGS = ['django.template.defaulttags.static']

# Application definition

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls.apps.PollsConfig',
    'admin_side',
    'Nutritionist_side',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Other middleware...
    'mysite.middleware.SessionIdleTimeoutMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'Fitfix',
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'fitfix',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb+srv://mrash:mrash123@project-is.js3ah72.mongodb.net/?retryWrites=true&w=majority',
            'tls': True,
            'tlsInsecure': True,
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'polls.CustomUser'

#manual add by ashar
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'polls/static') 
]
