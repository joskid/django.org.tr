# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from profiles.models import *
from django.views.generic.list_detail import object_list
from django import forms
from blog.models import Entry

def profile_list(request):
    queryset = Profile.objects.all()
    city_id = request.GET.get('city')
    
    if city_id:    
        queryset = queryset.filter(city__id=city_id)
    if city_id=='0':
        queryset = Profile.objects.all()
    cities = City.objects.all()
    return object_list(request, queryset=queryset,
                       template_name = 'profiles/profile_list.html',
                       extra_context={'cities':cities})

# Create your views here.

def profile_detail(request, profile_slug):
    profile = get_object_or_404(Profile, slug = profile_slug)
    user = profile.user
    entries = Entry.objects.filter(user = user)
    for entry in entries:
        print entry.title
    return render_to_response('profiles/profile_detail.html',
                              {'profile' : profile,
                               'entries' :entries},
                               context_instance=RequestContext(request))
    
