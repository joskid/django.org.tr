# -*- coding: utf-8 -*-

from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from events.models import Event
from blog.models import Entry


def index(request):
    return render_to_response('index.html',
                              {'events': Event.objects.filter(end__gte=datetime.now(),
                                                              active=True)[:5],
                               'entries': Entry.objects.all()[:5]},
                               context_instance=RequestContext(request))