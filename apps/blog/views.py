# -*- coding: utf-8 -*-

import datetime
from django.shortcuts import get_list_or_404, render_to_response, get_object_or_404
from django.views.generic import list_detail
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.sitemaps import Sitemap
from apps.blog.models import Entry

'''#
def blog_list(request):
    blogs = Blog.objects.all()
    return render_to_response('blog/blog_list.html',
                              {'blogs': blogs})

def blog_detail(request, blog_slug):
    blog = Blog.objects.get(slug=blog_slug)
    entries = Entry.objects.filter(blog = blog)
    return render_to_response('blog/blog_detail.html',
                              {'entries': entries,
                               'blog': blog})
'''

def entry_list(request):
    entries = Entry.objects.all()
    return render_to_response('blog/entry_list.html',
                              {'entries': entries},
                              context_instance=RequestContext(request))

def entry_detail(request, entry_slug):
    entries = Entry.objects.all()
    entry = Entry.objects.get(slug=entry_slug)

    return render_to_response('blog/entry_detail.html',
                              {'entry': entry,
                               'entries': entries},
                              context_instance=RequestContext(request))
