"""
Django settings for project aclarknet.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'zsrzbhfdf4o&+%lgcqqd9pxa^u5+qe9&6d#g=g-@8e)f&a-1v&')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'django_extensions',
    'import_export',
    'solo',
    'aclarknet.database',
    'rest_framework',
    'social_django',
#    'webpack_loader',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware', )

ROOT_URLCONF = 'aclarknet.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'social_django.context_processors.backends',
            'social_django.context_processors.login_redirect',
        ],
    },
}, ]

WSGI_APPLICATION = 'aclarknet.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get(
        'DATABASE_URL', 'postgres://%s:%s@%s:%s/%s' %
        (os.environ.get('DB_USER', ''), os.environ.get('DB_PASS', ''),
         os.environ.get('DB_HOST', 'localhost'),
         os.environ.get('DB_PORT', '5432'),
         os.environ.get('DB_NAME', 'aclarknet'))))
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Django social auth
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend', )

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get(
    'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/google-oauth2/?next=/'

# Send mail with sendgrid
# DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
# EMAIL_HOST = os.environ.get('EMAIL_HOST')
# EMAIL_PORT = os.environ.get('EMAIL_PORT')
# EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
# EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
# EMAIL_USE_TLS = True

# Send mail with AWS SES
EMAIL_BACKEND = 'django_ses.SESBackend'
# EMAIL_FROM = os.environ.get('EMAIL_FROM')
EMAIL_FROM = 'aclark.net@aclark.net'

GRAVATAR_URL = 'https://www.gravatar.com/avatar/%s'

# Commas please
USE_L10N = True
USE_THOUSAND_SEPARATOR = True

# https://docs.djangoproject.com/en/dev/topics/logging/#examples
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# API
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':
    ('rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly', ),
}

# http://geezhawk.github.io/using-react-with-django-rest-framework
# https://github.com/ezhome/django-webpack-loader
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'webpack_bundles/', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}
