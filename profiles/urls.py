from django.conf.urls.defaults import *


urlpatterns = patterns('profiles.views',
    url('^form/$', 'profile_form', name='profile_form'),
    url(r'^$', 'profile_list', name='profile_list'),
    url('^(?P<username>[-\w]+)/$', 'profile_detail', name='profile_detail'),
)
