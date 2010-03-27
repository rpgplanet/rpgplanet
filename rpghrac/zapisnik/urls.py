from django.conf.urls.defaults import url, patterns

from rpghrac.zapisnik.views import new, home, workshop

urlpatterns = patterns('',
    url("^$", home, name="zapisnik-home"),
    url("^novy/$", new, name="zapisnik-new"),
    url("^dilna/$", workshop, name="zapisnik-workshop"),
)
