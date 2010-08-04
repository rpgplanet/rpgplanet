from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('rpgplanet.registration.views',
    url("^$", 'inviteform', {'template' : 'registration/inviteform.html'}, name="inviteform"),
#    url("^registrace/$", registration, name="registration"),
)
