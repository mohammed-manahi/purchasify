"""
Django settings for purchasify project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _

# Use dotenv to secure secret keys in the project
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'dev.machine']

# Application definition

INSTALLED_APPS = [
    # Add account app to installed apps
    'account',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add shop app to installed apps
    'shop',
    # Add cart app to installed apps
    'cart',
    # Add order app to installed apps
    'order',
    # Add payment app to installed apps
    'payment',
    # Add coupon app to installed apps
    'coupon',
    # Add rosetta third-party library for translation
    'rosetta',
    # Add parler third-party library for model translation
    'parler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Add localization middleware and it must be after session since it requires session data
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'purchasify.urls'

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
                # Add cart context processor
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'purchasify.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        # Configure postgres database connection
        'ENGINE': str(os.getenv('DATABASE_ENGINE')),
        'NAME': str(os.getenv('DATABASE_NAME')),
        'USER': str(os.getenv('DATABASE_USERNAME')),
        'PASSWORD': str(os.getenv('DATABASE_PASSWORD')),
        'HOST': str(os.getenv('DATABASE_HOST')),
        'PORT': str(os.getenv('DATABASE_PORT')),
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

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# Set static url and media root to serve static files
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Set media url and media root to serve media contents
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Set customized user model as default
AUTH_USER_MODEL = 'account.User'

# Override default authentication urls for login and logout
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# Set cart session id to store the cart in the user session
CART_SESSION_ID = 'cart'

# Set smtp for mailing in development environment
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Set stripe payment gateway configuration
STRIPE_PUBLISHABLE_KEY = str(os.getenv('STRIPE_PUBLISHABLE_KEY'))
STRIPE_SECRET_KEY = str(os.getenv('STRIPE_SECRET_KEY'))
STRIPE_API_VERSION = str(os.getenv('STRIPE_API_VERSION'))
STRIPE_WEBHOOK_SECRET = str(os.getenv('STRIPE_WEBHOOK_SECRET'))

# Set redis configuration
REDIS_HOST = str(os.getenv('REDIS_HOST'))
REDIS_PORT = str(os.getenv('REDIS_PORT'))
REDIS_DB = str(os.getenv('REDIS_DB'))

# Set supported projects languages. Note that this requires gettext package installed which comes by default on linux
LANGUAGES = [('en', _('English')), ('ar', _('Arabic')), ]

# Set locale directory
LOCALE_PATHS = [BASE_DIR / 'locale', ]

# Set parler configuration
PARLER_LANGUAGES = {
    None: ({'code': 'en'}, {'code': 'ar'},),
    'default': {'fallback': 'en', 'hide_untranslated': False, }
}
