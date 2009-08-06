from os.path import join
from tempfile import gettempdir

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ENABLE_DEBUG_URLS = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = join(gettempdir(), 'rpghrac.db')
TEST_DATABASE_NAME = join(gettempdir(), 'rpghrac-test.db')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

SECRET_KEY = 'tlucebubenicektlucenabuben$$$'


# we want to reset whole cache in test
# until we do that, don't use cache
CACHE_BACKEND = 'dummy://'
CACHE_TIMEOUT = 10*60
CACHE_SHORT_TIMEOUT = 1*60
CACHE_LONG_TIMEOUT = 60*60

# can/should be set to None for production
TEST_MEDIA_URL = "/testing_media/"

NEWMAN_MEDIA_PREFIX = '/static/newman_media/'

SESSION_COOKIE_DOMAIN = '.rpghrac.cz'

MAIN_SUBDOMAIN = 'www'

