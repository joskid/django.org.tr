# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from events.models import Event
from blog.models import Entry
from websites.models import WebSite


def index(request):
    events = Event.objects.filter(active=True).order_by('-start')[:5]
    return render_to_response('index.html',
                              {'events': events,
                               'entries': Entry.objects.all()[:5],
                               'sites': WebSite.objects.all()[:10]},
                               context_instance=RequestContext(request))