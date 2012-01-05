from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from apps.events.views import EventList
from apps.events.views import EventDetail

urlpatterns = patterns(
    '',

    url(r'^$', view=EventList.as_view(), name='event_list'),
    url(r'^(?P<event_date>[-\d]+)/(?P<slug>[-\w]+)/$',
        view=EventDetail.as_view(), name='event_detail')
)
