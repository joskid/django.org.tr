from django.conf.urls.defaults import *


urlpatterns = patterns(
    'apps.profiles.views',

    url(r'^form/$', 'profile_form', name='profile_form'),
    url(r'^$', 'profile_list', name='profile_list'),
    url(r'^(?P<username>[- \w]+)/$', 'profile_detail', name='profile_detail'),
)
