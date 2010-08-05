from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('rpgplanet.service.views',
    url("^uzivatel/(?P<user_slug>.*)$", 'user_profile', name="profile"),
)
