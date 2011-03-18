from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'index.views.index'),
    (r'^blog/', include('blog.urls')),
    (r'^websites/', include('websites.urls')),
    (r'^events/', include('events.urls')),
    (r'^profile/', include('profiles.urls')),
    
    url(r'^', include('social_auth.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^(?P<path>.*\.(?i)(css|js|jpg|jpeg|png|gif|ico|swf|html|htm))$', 
         'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
