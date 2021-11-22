"""
Django settings for timeweb project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

PROXY = 0

# SECURITY WARNING: don't run with debug turned on in production!
try:
    DEBUG = os.environ['DEBUG'] == "True"
except KeyError:
    DEBUG = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
if DEBUG:
    CSP_CONNECT_SRC = ("'self'", 'https://accounts.google.com')
    CSP_SCRIPT_SRC = ("'self'", )
else:
    CSP_CONNECT_SRC = ("'self'", 'https://www.google-analytics.com', 'https://www.googletagmanager.com', 'https://accounts.google.com')
    CSP_SCRIPT_SRC = ("'self'", 'https://www.googletagmanager.com') # Needs to be set so nonce can be added
    CSP_DEFAULT_SRC = ("'self'", 'https://www.googletagmanager.com')
CSP_INCLUDE_NONCE_IN = ('script-src', ) # Add nonce b64 value to header, use for inline scripts
CSP_OBJECT_SRC = ("'none'", )
CSP_BASE_URI = ("'none'", )
CSP_IMG_SRC = ("'self'", "data:")

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'timewebapp/static/js' if DEBUG else 'static/js', 'serviceworker.js')
PWA_APP_DEBUG_MODE = False
PWA_APP_NAME = "TimeWeb PS" if DEBUG else "TimeWeb"
PWA_APP_DESCRIPTION = "TimeWeb PS APP" if DEBUG else "TimeWeb App"
PWA_APP_THEME_COLOR = '#ffffff'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'fullscreen'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'portrait'
PWA_APP_START_URL = '/'
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
try:
    SECRET_KEY = os.environ['SECRETKEY']
except KeyError:
    from django.core.management.utils import get_random_secret_key
    SECRET_KEY = get_random_secret_key()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
if DEBUG:
    ALLOWED_HOSTS = ['localhost']
else:
    ALLOWED_HOSTS = ['timeweb.io', 'timeweb-308201.wl.r.appspot.com', 'www.timeweb.io', 'www.timeweb-308201.wl.r.appspot.com']
# Application definition

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = not DEBUG
SECURE_HSTS_SECONDS = 604800 # 7 days
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'timewebapp',
    'multiselectfield',
    'django.contrib.admin', # admin needs to be after 'timewebapp' for some reason I forgot but it needs to be here
    'pwa',
    'colorfield',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
    'timewebapp.middleware.CatchRequestDataTooBig',
]

ROOT_URLCONF = 'timeweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Add in registration template
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
# Redirect to home URL after login
LOGOUT_REDIRECT_URL = '/'
WSGI_APPLICATION = 'timeweb.wsgi.application'

MAX_UPLOAD_SIZE = 5242880 # 40 MiB (max background image size)
DATA_UPLOAD_MAX_MEMORY_SIZE = 1310720 # 10 MiB (max size for data sent by ajax by assignments)

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
if os.getenv('GAE_APPLICATION', None):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'timewebdb',
            'USER': 'postgres',
            'PASSWORD': os.environ['PASSWORD'],
            'HOST': '/cloudsql/timeweb-308201:us-west2:timewebdbinstance',
            'PORT': '5432',
        }
    }
else:
    if PROXY:
        # If running locally and connecting to server database, connect via the proxy.
        #
        #     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
        #
        # See https://cloud.google.com/sql/docs/mysql-connect-proxy for more info
        # 
        # 
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'HOST': '127.0.0.1',
                'PORT': '3306',
                'NAME': 'timewebdb',
                'USER': 'postgres',
                'PASSWORD': os.environ['PASSWORD'],
            }
        }
    else:
        # If running locally, use a sqlite database
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
DEFAULT_AUTO_FIELD='django.db.models.AutoField' 
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
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
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "America/Los_Angeles"

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
if not DEBUG:
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_BUCKET_NAME = 'timeweb-308201.appspot.com'

    GS_PROJECT_ID = 'timeweb-308201'
    from google.oauth2 import service_account
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
        BASE_DIR / "sa-private-key.json"
    )
# Django Logging config
ROOT_LOG_LEVEL = 'DEBUG' if DEBUG else 'WARNING'
DJANGO_LOG_LEVEL = 'INFO' if DEBUG else 'WARNING'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'root': {
        'handlers': ['console'],
        'level': ROOT_LOG_LEVEL,
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': DJANGO_LOG_LEVEL,
        }
    },
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d}>> {message}',
            'style': '{',
        },
        'simple': {
            'format': '{asctime} <<{levelname}>> {message}',
            'style': '{',
        },
    },
}