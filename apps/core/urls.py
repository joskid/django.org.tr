from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from apps.core.views import CoreIndex

urlpatterns = patterns(
    '',

    url(r'^$', view=CoreIndex.as_view(), name='core-index'),
)
