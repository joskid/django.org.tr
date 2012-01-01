from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

urlpatterns = patterns(
    'apps.events.views',

    url(r'^$', 'event_list', name='event_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', 'event_detail', name='event_detail'),
)
