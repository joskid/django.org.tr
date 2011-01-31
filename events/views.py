# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from events.models import Event
from django.views.generic.list_detail import object_list

def event_list(request):
    queryset = Event.objects.all().order_by('-start')
    return object_list(request, queryset=queryset,
                       template_name = 'events/event_list.html')

def event_detail(request, year, month, day, slug):
    event = get_object_or_404(Event, start__year=year, start__month=month,
                              start__day=day, slug=slug)
    events = Event.objects.all().order_by('-start')
    return render_to_response('events/event_detail.html',
                              {'event': event,
                               'events': events},
                               context_instance=RequestContext(request))
