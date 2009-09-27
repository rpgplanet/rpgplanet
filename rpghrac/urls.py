from os.path import dirname, join, normpath

import django
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

import ella
from ella import newman

from rpgplayer.views.home import home

admin.autodiscover()
newman.autodiscover()


urlpatterns = patterns('',)

ADMIN_ROOTS = (
    normpath(join(dirname(ella.__file__), 'newman', 'media')),
    normpath(join(dirname(django.__file__), 'contrib', 'admin', 'media')),
)

js_info_dict = {
    'packages': ('ella.newman',),
}

if settings.DEBUG:
    urlpatterns += patterns('',
        # serve static files
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

urlpatterns += patterns('',


    # newman JS translations
    (r'^cmsmin/jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),

    # main admin urls
    ('^cmsmin/', include(newman.site.urls)),
    
    # true root is from rpgplayer
    url( r'^$', home, name="root_homepage" ),

#    url( r'^$', home, name="root_homepage" ),

    # ella urls
    #('^', include('ella.core.urls')),

    # serve admin media static files
    (r'^static/newman_media/(?P<path>.*)$', 'ella.utils.views.fallback_serve', {'document_roots': ADMIN_ROOTS}),
    (r'^static/admin_media/(?P<path>.*)$', 'ella.utils.views.fallback_serve', {'document_roots': ADMIN_ROOTS}),
)

urlpatterns += patterns('',
    # serve static files
    url(r'^%s/(?P<path>.*)$' % settings.TEST_MEDIA_URL.strip('/'), 'django.views.static.serve', {'document_root': settings.TEST_MEDIA_ROOT, 'show_indexes': True}),
)


handler404 = 'ella.core.views.page_not_found'
handler500 = 'ella.core.views.handle_error'