from django.conf.urls.defaults import *


urlpatterns = patterns('blog.views',
    #url('^(?P<blog_slug>[-\w]+)/$', 'blog_detail', name='blog_detail'),
    #url(r'^$', 'blog.views.blog_list', name='blog_list'),
    url(r'^$', 'entry_list', name='entry_list'),
    url('^(?P<entry_slug>[-\w]+)/$', 'entry_detail', name='entry_detail'),
)
