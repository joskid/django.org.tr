# -*- coding: utf-8 -*-

import datetime
from django.shortcuts import get_list_or_404, render_to_response, get_object_or_404
from blog.models import Blog, Entry
from django.views.generic import list_detail
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.sitemaps import Sitemap


def blog_list(request):
    return list_detail.object_list(request,
                                   queryset = Entry.objects.all(),
                                   paginate_by=20,
                                   template_name='blog/blog_list.html',
                                   extra_context={'blogs': Blog.objects.all()})

def blog_detail(request, entry_slug):
    e = Entry.objects.get(slug=entry_slug)
    return render_to_response('blog/blog_detail.html',
                              {'entry': Entry.objects.get(slug=entry_slug),
                               'blogs': Blog.objects.all()})# Create your views here.
