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
from rpgplanet.service import urls as serviceurls
from rpgcommon.user import urls as userurls

urlpatterns = patterns('',
    url(r'^beta/', include(betaurls, namespace="beta")),
    url(r'^uzivatel/', include(userurls, namespace="registration")),

    url('^admin/', include(admin.site.urls)),
    url('^newman/', include(newman.site.urls)),

    url(r'^', include(serviceurls, namespace="service")),
    url(r'^', include(userurls, namespace="user")),
    url(r'^$', redirect_to, {'url' : '/beta/'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        # serve newman media static files
        (r'^%s/(?P<path>.*)$' % settings.NEWMAN_MEDIA_PREFIX.strip('/'), 'django.views.static.serve',
            {'document_root': settings.NEWMAN_MEDIA_ROOT, 'show_indexes': True,}),
#        # serve newman static files
        (r'^%s/newman/(?P<path>.*)$' % settings.STATIC_URL.strip('/'), 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True,}),
        # serve static files
        (r'^%s/(?P<path>.*)$' % settings.STATIC_URL.rstrip('/').lstrip('/'), 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
        # serve media files
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.rstrip('/').lstrip('/'), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

