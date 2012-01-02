from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from apps.events.views import EventList
from apps.events.views import EventDetail

urlpatterns = patterns(
    '',

    url(r'^$', view=EventList.as_view(), name='event_list'),
    url(r'^(?P<slug>[-\w]+)/$', view=EventDetail.as_view(),
        name='event_detail')
)


# url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/../$',
#     'event_detail', name='event_detail'),
