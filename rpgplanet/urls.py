from os.path import dirname, join, normpath

import django
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

import ella
from ella import newman

admin.autodiscover()
newman.autodiscover()


#urlpatterns = patterns('',)

ADMIN_ROOTS = (
    normpath(join(dirname(ella.__file__), 'newman', 'media')),
    normpath(join(dirname(django.__file__), 'contrib', 'admin', 'media')),
)

js_info_dict = {
    'packages': ('ella.newman',),
}

urlpatterns = patterns('',
    url('^$', include('betainfo.urls')),
    url("^zapisnik/new/$", 'zapisnik.views.new', name="zapisnik-new"),
    url("^zapisnik/dilna/$", 'zapisnik.views.workshop', name="zapisnik-workshop"),

    # ella urls
    ('^tvorba/', include('ella.core.urls')),

    # serve static files
    url(r'^%s/(?P<path>.*)$' % settings.TEST_MEDIA_URL.strip('/'), 'django.views.static.serve', {'document_root': settings.TEST_MEDIA_ROOT, 'show_indexes': True}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        # serve static files
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'), 'django.views.static.serve', {'document_root': settings.TEST_MEDIA_ROOT, 'show_indexes': True}),
    )



handler404 = 'ella.core.views.page_not_found'
handler500 = 'ella.core.views.handle_error'
