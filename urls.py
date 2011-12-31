from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^$', 'index.views.index'),
    url(r'^blog/', include('blog.urls')),
    url(r'^websites/', include('websites.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^profile/', include('profiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social/', include('social_auth.urls')),
)
urlpatterns += staticfiles_urlpatterns()
