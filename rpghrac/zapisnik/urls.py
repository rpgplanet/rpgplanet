from django.conf.urls.defaults import url, patterns

from zapisnik.views import new, home

urlpatterns = patterns('',
    url("^$", home, name="zapisnik-home"),
    url("^new/$", new, name="zapisnik-new"),
)
