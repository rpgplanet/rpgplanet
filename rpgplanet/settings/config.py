from os.path import dirname, join
from tempfile import gettempdir

import rpgplanet

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ENABLE_DEBUG_URLS = DEBUG

SECRET_KEY = 'tlucebubenicektlucenabuben$$$'

FACEBOOK_APPLICATION_ID = '147869781892995'
GOOGLE_ANALYTICS_CODE = 'UA-16432389-1'

STATIC_ROOT = join(dirname(rpgplanet.__file__), 'static')


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^980$0s46q1(toq*mu23m41_ac_@vwy)+mig=ka_97$m0^fh)v'


# we want to reset whole cache in test
# until we do that, don't use cache
CACHE_BACKEND = 'dummy://'
CACHE_TIMEOUT = 10*60
CACHE_SHORT_TIMEOUT = 1*60
CACHE_LONG_TIMEOUT = 60*60

NEWMAN_MEDIA_PREFIX = '/static/newman_media/'

#SESSION_COOKIE_DOMAIN = 'rpgplanet.cz'

