# -*- coding: utf-8 -*-

# Django base settings for rpghrac project.

from os.path import dirname, join

import ella
import django
import rpghrac


DEBUG = True
TEMPLATE_DEBUG = DEBUG


ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
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
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

ADMIN_ROOTS = (
    join(dirname(ella.__file__), 'newman', 'media'),
    join(dirname(django.__file__), 'contrib', 'admin', 'media'),
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'rpgplayer.middleware.SetDomainOwnerMiddleware'
)

ROOT_URLCONF = 'rpghrac.urls'

TEMPLATE_DIRS = (
    join(dirname(rpghrac.__file__), 'templates'),
    join(dirname(ella.__file__), 'newman', 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
    'ella.newman.context_processors.newman_media',
    'ella.core.context_processors.url_info',
    'rpghrac.rpgplayer.context_processors.is_site_owner',
)

INSTALLED_APPS = (
    # internal apps
    'rpghrac.service',
    'rpghrac.rpgplayer',
    'zapisnik',

    # external apps
    'rpgrules',
    'rpgext.extcore',
    'rpgext.drd',
    'rpgext.strepysnu',
    
#    'south',
    'ella',
    'ella.core',
    'ella.newman',
    'ella.newman.licenses',
    'ella.photos',
    'django.contrib.admin',
    'djangomarkup',

    # core django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
)

AUTH_PROFILE_MODULE = 'rpgplayer.UserProfile'
LOGIN_REDIRECT_URL = '/'

VERSION = rpghrac.__versionstr__

CHERRYPY_TEST_SERVER = True


