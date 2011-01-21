from django.conf.urls.defaults import *


urlpatterns = patterns('profiles.views',
    url(r'^$', 'profile_list', name='profile_list'),
    url('^(?P<profile_slug>[-\w]+)/$', 'profile_detail', name='profile_detail'),
    
)
