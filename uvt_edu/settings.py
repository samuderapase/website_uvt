import os
import manage
#import warnings

SITE_ROOT = os.path.dirname(os.path.realpath(manage.__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'uvt.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_THOUSAND_SEPARATOR = True

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = '/media/'

STATIC_ROOT = ''

STATIC_URL = '/static/'

USE_TZ = True

#warnings.filterwarnings(
        #'error', r"DateTimeField received a naive datetime",
        #RuntimeWarning, r'django\.db\.models\.fields')
        
TINYMCE_JS_ROOT = '/media/tiny_mce/'
TINYMCE_JS_URL = os.path.join(MEDIA_URL, "tiny_mce/tiny_mce_src.js")
TINYMCE_DEFAULT_CONFIG = {
    'entity_encoding': 'raw', 
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'relative_urls': False,
}

TINYMCE_SPELLCHECKER = True

ORBITED_HOST = "localhost" # (use the domain name you used for orbited access). defaults to localhost
ORBITED_PORT = "9000" # defaults to 9000
STOMP_PORT = "61613" # defaults to 61613

STOMP_RESTQ_URL = "/live/restq/"

#Pengaturan untuk Registrasi 
ACCOUNT_ACTIVATION_DAYS=7
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'test@gmail.com'


#kategory

STATICFILES_DIRS = (

    #"/home/shellc0de/uvt/uvt/uvt_edu/static",
    os.path.join(os.path.abspath(os.path.dirname(__file__) + '/..'), 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '7edj@+$%-=%n3#nqr^=xx9)!vvi$lc=+p@5qfeg9ojci328fp&amp;'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    #"blogango.context_processors.extra_context",
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
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

ROOT_URLCONF = 'uvt_edu.urls'

WSGI_APPLICATION = 'uvt_edu.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(os.path.abspath(os.path.dirname(__file__) + '/..'), 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.comments',
    'django.contrib.sitemaps',
    'google_analytics',
    'mptt',
    #'dpaste',
    'pastebin',
    'perpustakaan',
    'categories',
    'categories.editor',
    'registration',
    'south',
    #'tagging', 
    'live',
    'disqus',
    'uvt',
    'articles',
    'pagination',
    'tinymce',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
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
    }
}
