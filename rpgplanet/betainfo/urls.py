from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

from rpgplanet.betainfo.views import registration

urlpatterns = patterns('',
    url("^$", direct_to_template, {'template' : 'betainfo/homepage.html'}, name="info"),
    url("^registrace/$", registration, name="registration"),
)
