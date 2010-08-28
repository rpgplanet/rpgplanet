# -*- coding: utf-8 -*-

from rpgcommon.settings.base import *

from os.path import dirname, join

import ella
import django
import rpgplanet as project


DEBUG = True
TEMPLATE_DEBUG = DEBUG


ADMINS = (
    ('Almad', 'almad@rpgplanet.cz'),
)
MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Prague'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'cs'

# Site ID
SITE_ID = 2

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

ROOT_URLCONF = 'rpgplanet.urls'

TEMPLATE_DIRS = (
    join(dirname(project.__file__), 'templates'),
    join(dirname(ella.__file__), 'newman', 'templates'),
)

#AUTH_PROFILE_MODULE = 'rpgplayer.UserProfile'
#LOGIN_REDIRECT_URL = '/'
SITE_DOMAIN = "rpgplanet.cz"

VERSION = project.__versionstr__

CHERRYPY_TEST_SERVER = True


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "django.middleware.transaction.TransactionMiddleware",

#    'ella.core.context_processors.url_info',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'ella.newman.context_processors.newman_media',
)