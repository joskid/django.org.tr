from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url('^(?P<entry_slug>[-\w]+)/$', 'blog.views.blog_detail', name='blog_detail'),
    url(r'^$', 'blog.views.blog_list', name='blog_list'),
)
