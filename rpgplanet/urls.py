from os.path import dirname, join, normpath

import django
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import redirect_to

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

from rpgplanet.betainfo import urls as betaurls
from rpgplanet.registration import urls as registerurls

urlpatterns = patterns('',
    url(r'^beta/', include(betaurls, namespace="beta")),
    url(r'^registrace/', include(registerurls, namespace="registration")),
    url(r'^$', redirect_to, {'url' : '/beta/'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        # serve static files
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.rstrip('/').lstrip('/'), 'django.views.static.serve', {'document_root': settings.TEST_MEDIA_ROOT, 'show_indexes': True}),
    )



handler404 = 'ella.core.views.page_not_found'
handler500 = 'ella.core.views.handle_error'
