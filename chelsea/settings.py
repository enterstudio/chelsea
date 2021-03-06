# Django settings for chelsea project.
import os
import urlparse
import dj_database_url

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

# Get an instance of a logger
import logging
logger = logging.getLogger('blog.logger')

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True if os.environ.get('BUILD')=='DEV' else False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Jenny', 'jennylc@gmail.com'),
    ('John', 'john.schimmel@gmail.com')
)

MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'https://chchchelsea.s3.amazonaws.com/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"


CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
   'awesome_ckeditor': {
       'skin': 'moono',
        'toolbar': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'RemoveFormat', 'SpellChecker', 'Undo', 'Redo'],
            ['Link', 'Image', 'Table', 'HorizontalRule','PageBreak'],
            ['spellchecker','TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'], ['Source'],
        ],
        'height': 291,
        'width': 835,
        'filebrowserWindowWidth': 940,
        'filebrowserWindowHeight': 725,
        'extraPlugins' : 'wsc'
    },
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c$-2zejruity=89i3x*w8=kg&amp;)9ahg7oj#klqa=g8=(idkqvby'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'chelsea.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'chelsea.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'suit',    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.sitemaps',
    'ckeditor',
    'storages',
    'blog',
    'redis_cache',
    'robots',
    'sorl.thumbnail'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'blog.logger' : {
            'handlers' : ['console'],
            'level' : 'DEBUG'
        }
    }
}

# Parse database configuration from $DATABASE_URL
DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Boto requires subdomain formatting.
# from S3 import CallingFormat
# AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False

# ROBOTS
ROBOTS_SITEMAP_URLS = [
    'http://www.hichelsea.com/sitemap.xml',
]

# REDIS CACHE
if os.environ.get('BUILD')=='DEV':
    CACHES = {
        "default": {
            "BACKEND": "redis_cache.cache.RedisCache",
            'LOCATION': 'localhost:6379:0',
            "OPTIONS": {
                "CLIENT_CLASS": "redis_cache.client.DefaultClient",
            }
        }
    }
    logger.info("LOCAL CACHE")
else:
    redis_url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))

    CACHES = {
        "default": {
            "BACKEND": "redis_cache.cache.RedisCache",
            'LOCATION': '%s:%s:0' % (redis_url.hostname, redis_url.port),
            "OPTIONS": {
                "PASSWORD":redis_url.password,
                "CLIENT_CLASS": "redis_cache.client.DefaultClient",
            }
        }
    }
    logger.info("REDISCLOUD CACHE")

# Django suit
SUIT_CONFIG = {
    'ADMIN_NAME': 'hichelsea admin'
}

THUMBNAIL_DEBUG=True