from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()
urlpatterns = patterns(
    '',

    url(r'^', include('apps.core.urls')),
    url(r'^planet/', include('apps.aggregator.urls')),
    url(r'^blog/', include('apps.blog.urls')),
    url(r'^websites/', include('apps.websites.urls')),
    url(r'^events/', include('apps.events.urls')),
    url(r'^profile/', include('apps.profiles.urls')),
    url(r'^social/', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
